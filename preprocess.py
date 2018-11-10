import pandas as pd
import numpy as np

#removing the null rows
def remove_null():	
	f="responses.csv"
	df=pd.read_csv(f)
	df1=df.dropna(axis=0)
	df1.to_csv("non_null_responses.csv",index=False)

def map_values():
	f="replaced_responses.csv"
	df=pd.read_csv("responses.csv")
	l=df.select_dtypes(include=['object']).columns
	for x in l:
		unique=df[x].unique()
		if x=="Alcohol":
			l=[2,1,0]
		elif x=="Education":
			l=[3,2,1,4,5,0]
		else:
			l=[i for i in range(len(unique))]
		dic=dict(zip(unique,l))
		df[x]=df[x].replace(dic)
	df.to_csv(f,index=False)

map_values()
remove_null()
'''
c=df1.corr().abs()
s = c.unstack()
so = s.sort_values(kind="quicksort")
values = [0 if i<0.5 else i for i in so ]
m1=list(filter(lambda a:a !=0,values))
values = [0 if i==1.0 else i for i in m1]
m2=list(filter(lambda a:a !=0,values))
print(len(m1))
print(len(m2))
print(so[-len(m1):len(m2)-len(m1)])'''
