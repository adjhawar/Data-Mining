import pandas as pd
import numpy as np
import math
import missingno as msno
import matplotlib.pyplot as plt

#removing the null rows
def remove_null():	
	f="replaced_responses.csv"
	df=pd.read_csv(f)
	df1=df.dropna(axis=0)
	df1.to_csv("non_null_responses.csv",index=False)

#map strings to ordinal numbers
def map_values():
	f="replaced_responses.csv"
	df=pd.read_csv("responses.csv")
	l=df.select_dtypes(include=['object']).columns
	for x in l:
		unique=df[x].unique()
		if isinstance(unique[-1],float):
			unique=unique[:-1]
		if x=="Alcohol":
			l=[2,1,0]
		elif x=="Education":
			l=[3,2,1,4,5,0]
		else:
			l=[i for i in range(len(unique))]
		dic=dict(zip(unique,l))
		df[x]=df[x].replace(dic)
	df.to_csv(f,index=False)

#fill ordinal missing values
def fill_ordinal(df):
	missing = df.isnull()
	p=[]
	a=[0,1,2,3,4,5]
	for x in a:
		p.append((df==x).sum(axis=0))
	s=sum(p)
	p=p/s
	df.loc[missing]=np.random.choice(a, size=len(df[missing]),p=p)
	return df

def to_fill(df,col1,col2):
	corr=df[col1].corr(df[col2])
	if col1!="Weight" and col1!="Height" and col1!="Gender" and col1!="Education" and col1!="Age":
		temp=df.dropna(subset=[col1])
		temp[col2]=temp.groupby(col1)[col2].apply(lambda x:x.fillna(math.ceil(x.name*corr)))
		df.update(temp)
		temp=df.dropna(subset=[col2])
		temp[col1]=temp.groupby(col2)[col1].apply(lambda x:x.fillna(math.ceil(x.name*corr)))
		df.update(temp)
	elif col2=="Age":
		min=df[col2].min()
		df[col1]=df[col1].fillna(-1)
		df[col2]=df.groupby(col1)[col2].apply(lambda x:x.fillna(round((x.mean()-min)*corr+min)))
		df[col1]=df[col1].replace(to_replace=-1,value=np.nan)
		df[col1]=df.groupby(col2)[col1].apply(lambda x:x.fillna(round(x.mean()*corr)))
	elif col2!="Gender":
		temp=df.dropna(subset=[col1,col2],how='all')
		min=df[col1].min()
		temp=temp.dropna(subset=[col2])
		temp[col1]=temp.groupby(col2)[col1].apply(lambda x:x.fillna(math.ceil((x.mean()-min)*corr+min)))
		df.update(temp)
		min=df[col2].min()
		temp=temp.dropna(subset=[col1])
		temp[col2]=temp.groupby(col1)[col2].apply(lambda x:x.fillna(math.ceil((x.mean()-min)*corr+min)))
		df.update(temp)
	else:
		temp=df.dropna(subset=[col2])
		min=df[col1].min()
		temp[col1]=temp.groupby(col2)[col1].apply(lambda x:x.fillna(math.ceil((x.mean()-min)*corr+min)))
		temp=df.dropna(subset=[col1])
		temp[col2]=temp.groupby(col1)[col2].apply(lambda x:fill_ordinal(x))
		df.update(temp)
	return df

#fill uncorrelated columns
def fill_uncorr(df):
	cols=df.columns[df.isna().any()].tolist()
	for c in cols:
		n=len(df[c].unique())
		if n>6:
			df[c]=df[c].fillna(round(df[c].mean()))
		else:
			df[c]=fill_ordinal(df[c])
	return df

#find columns whose correlation is greater than 0.5
def fill_corr_cols():
	df=pd.read_csv("non_null_responses.csv")
	c=df.corr()
	s = c.unstack()
	so = s.sort_values(kind="quicksort")
	values = [0 if i<0.50 else i for i in so ]
	m1=list(filter(lambda a:a !=0,values))
	values = [0 if i==1.0 else i for i in m1]
	m2=list(filter(lambda a:a !=0,values))
	s1=so[-len(m1):len(m2)-len(m1)].iloc[::2]
	df=pd.read_csv("replaced_responses.csv")
	for i in range(len(s1)-1,-1,-1):
		col1=s1.index[i][0]
		col2=s1.index[i][1]
		df=to_fill(df,col1,col2)
	df=fill_uncorr(df)
	df.to_csv("filled_responses.csv",index=False)

#map_values()
#remove_null()
#fill_corr_cols()
#df=pd.read_csv("non_null_responses.csv")
'''music=df.iloc[:,0:19]
movie=df.iloc[:,19:32]
hobbies=df.iloc[:,32:64]
phobias=df.iloc[:,64:74]
health=df.iloc[:,74:77]
personality=df.iloc[:,77:134]
spending=df.iloc[:,134:140]
demography=df.iloc[:,140:151]

music=music.merge(demography,how="outer",left_index=True,right_index=True)
m_cols=music.columns
groups=music.groupby(["Gender","Age"])
for l in m_cols:
	print(l,groups[l].mean())'''
