import pandas as pd
import numpy as np
import missingno as msno
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import math

warnings.filterwarnings("ignore")
#map strings to ordinal numbers and remove rows containing null values in "Gender" column
def map_values(df):
	df.dropna(inplace=True,axis=0,subset=["Gender"])
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
	df.to_csv("replaced_responses.csv",index=False)

def plots(so,flag):
	if flag==0:
		so.plot(kind='bar',color='slateblue')
		plt.show()
	elif flag==1:
		col=["Height","Weight"]
		plt.scatter(df[col[0]],df[col[1]])
		plt.xlabel(col[0])
		plt.ylabel(col[1])
		plt.show()

#rows that are incorrectly filled are modified
def cheats(df):
	col=["Only child","Number of siblings"]
	'''groups=df.groupby(col)
	for name,group in groups:
		print(name,len(group))'''
	for index,row in df.iterrows():
		if row[col[1]]>0:
			row[col[0]]=0
		else:
			row[col[0]]=1
	'''groups=df.groupby(col)
	for name,group in groups:
		print(name,len(group))'''	
	return df	

#removes outliers from the data that do not satisfy our domain knowledge
def outliers(df):
	#plots(df,1)
	remove=df[df["BMI"]>=40].index.values
	df.drop(remove,inplace=True)
	remove=df[df["Number of siblings"]>6].index.values
	df.drop(remove,inplace=True)
	df=cheats(df)
	'''groups=df.groupby("Education")["Age"]
	for name,group in groups:
		print(name)
		print(group.sort_values().unique())
		print("######")'''
	return df

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
	if col1=="Gender":
		df[col2]=df.groupby(col1)[col2].apply(lambda x:x.fillna(math.ceil(x.mean())))
	elif col2=="Gender":
		df[col1]=df.groupby(col2)[col1].apply(lambda x:x.fillna(math.ceil(x.mean())))
	elif col1=="Only child" and col2=="Number of siblings":
		temp=df[df[col2]==0]
		temp[col1].fillna(value=1,inplace=True)
		df.update(temp)
		temp=df[df[col2]>0]
		temp[col1].fillna(value=0,inplace=True)
		df.update(temp)
		temp=df[df[col1]==1]
		temp[col2].fillna(value=0,inplace=True)
		df.update(temp)
		temp=df[df[col1]==0]
		temp[col2].fillna(round(temp[col2].mean()),inplace=True)
		df.update(temp)
	else:
		temp=df.dropna(subset=[col1])
		temp[col2]=temp.groupby(col1)[col2].apply(lambda x:x.fillna(math.ceil(x.mean())))
		df.update(temp)
		temp=df.dropna(subset=[col2])
		if col1=="Height" and col2=="Weight":
			temp.drop(index=880,inplace=True)
		temp[col1]=temp.groupby(col2)[col1].apply(lambda x:x.fillna(math.ceil(x.mean())))
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
	df=pd.read_csv("replaced_responses.csv")
	c=df.corr()
	s = c.unstack()
	so = s.abs().sort_values(ascending=False)
	so=s[so.index]
	so=so[abs(so)>0.43]
	so=so[so!=1].iloc[::2]
	#plots(so.sort_values(),0)
	for i in range(0,len(so)):
		col1=so.index[i][0]
		col2=so.index[i][1]
		df=to_fill(df,col1,col2)
	df=fill_uncorr(df)
	#adding a new column+
	df["BMI"]=df.apply(lambda row:10000*row["Weight"]/(row["Height"]**2),axis=1)
	df=outliers(df)
	df.to_csv("filled_responses.csv",index=False)
	
#df=pd.read_csv("responses.csv")
#map_values(df)
#fill_corr_cols()
df=pd.read_csv("filled_responses.csv")
