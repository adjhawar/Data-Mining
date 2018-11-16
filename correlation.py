
import pandas as pd
import numpy as np
import missingno as msno
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import math

def warn(*args, **kwargs):
    pass

warnings.warn = warn

from sklearn.svm import SVC 
from sklearn.linear_model import LogisticRegression as lr
from sklearn.utils import resample
from sklearn.cross_validation import train_test_split as tts
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.metrics import recall_score

CORR_THRESHOLD = 0.25
df= pd.read_csv("filled_responses.csv")
features = []

def corr_plot():
	global features	
	corr = df.corrwith(df['Gender'])
	corr = corr.sort_values()[:-1]            # The last value is for the gender column itself which is not needed
	corr = corr[abs(corr) >= CORR_THRESHOLD]
	features = list(corr.index)
	sns.barplot(corr.values,corr.index)
	#plt.show()
	


def classification():
	cols = features + ["Gender"]
	data_bal = df[cols]
	'''data_male = data[data['Gender']==1]
	data_female = data[data['Gender']==0]
	print("Distribution of Gender")
	print(data['Gender'].value_counts())
	print("As we can see that there is class imbalance between the two classes, we will use resampling to increase the size of male class, so that classification algorithms are not biased")
	data_male_extra = resample(data_male , replace=True , n_samples = 179 , random_state =23)
	data_bal = pd.concat([data_female, data_male , data_male_extra])
	print("After resampling:")
	print(data_bal['Gender'].value_counts())'''
	x = np.array(data_bal.iloc[:,:-1])
	y = np.array(data_bal.iloc[:,-1])
	x_train, x_test, y_train, y_test = tts(x,y,test_size = 0.25,random_state=23)
	classifiers = [rfc(n_estimators=100,random_state=23) , lr(random_state = 23) , SVC(random_state=23)]
	methods = ["Random Forest Classifier" , "Logistic Regression" , "Support Vector Machines"]
	print("We are using the mean of recall scores of individual classes as our accuracy measure ")
	for i in range(len(methods)):
		clf = classifiers[i]
		print("Classifier : {}".format(methods[i]))
		clf.fit(x_train,y_train)
		y_pred = clf.predict(x_test)
		acc = recall_score(y_test, y_pred , average=None).mean()
		print("Accuracy Score :{}".format(acc))
	
corr_plot()
classification()
	



