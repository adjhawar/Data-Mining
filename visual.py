import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings

def visual_l1(x):
	count=0
	boys=x.sum()
	girls=len(x)-boys
	l=["Music","Movie"]
	for y in l1:
		nf=y.merge(x.to_frame(), left_index=True, right_index=True)
		cols=y.columns
		like={}
		temp_male=[]
		temp_female=[]
		for i in cols:
			like[i]=nf[nf[i]>=4]
			temp=like[i].groupby("Gender").count()[i]
			temp_male.append(temp[1])
			temp_female.append(temp[0])
		indices = range(len(cols))
		width = np.min(np.diff(indices))/3.
		fig = plt.figure()
		ax = fig.add_subplot(111)
		ax.bar(indices-width/2.,temp_female/girls,width,color='b',label='Female')
		ax.bar(indices+width/2.,temp_male/boys,width,color='r',label='Male')
		ax.set_xticks(indices)
		ax.axes.set_xticklabels(cols)
		plt.xticks(rotation=90)
		plt.legend(loc="upper right")
		plt.title(l[count]+" preferences with Gender")
		count=count+1
		plt.show()

def visual_l2(x):
	count=0
	boys=x.sum()
	girls=len(x)-boys
	l=["Interests","Hobbies","Phobias","Spending"]
	for y in l2:
		nf=y.merge(x.to_frame(), left_index=True, right_index=True)
		cols=y.columns
		like={}
		temp_male=[]
		temp_female=[]
		for i in cols:
			like[i]=nf[nf[i]>=4]
			temp=like[i].groupby("Gender").count()[i]
			temp_male.append(temp[1])
			temp_female.append(temp[0])
		indices = range(len(cols))
		width = np.min(np.diff(indices))/3.
		fig = plt.figure()
		ax = fig.add_subplot(111)
		ax.bar(indices-width/2.,temp_female/girls,width,color='b',label='Female')
		ax.bar(indices+width/2.,temp_male/boys,width,color='r',label='Male')
		ax.set_xticks(indices)
		ax.axes.set_xticklabels(cols)
		plt.xticks(rotation=90)
		plt.legend(loc="upper right")
		plt.title(l[count]+" with Gender")
		plt.show()
		count=count+1

def visual_l3(x):
	print("Health and traits left")

warnings.filterwarnings("ignore")
df=pd.read_csv("filled_responses.csv")
music = df.ix[:,0:19]
movies = df.ix[:,19:31]
interests = df.ix[:,31:46]
hobbies = df.ix[:,46:63]
phobias = df.ix[:,63:73]
health = df.ix[:,73:76]
traits = df.ix[:,76:133]
spending = df.ix[:,133:140]
demographics = df.ix[:,140:150]

l1=[music,movies]
l2=[interests,hobbies,phobias,spending]
#visual_l1(df["Gender"])
visual_l2(df["Gender"])
#visual_l3(df["Gender"])
