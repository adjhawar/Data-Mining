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
from sklearn.neural_network import MLPClassifier as NN
from sklearn.linear_model import LogisticRegression as lr
from sklearn.utils import resample
from sklearn.model_selection import train_test_split as tts
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.metrics import balanced_accuracy_score as bac
from sklearn.model_selection import cross_val_score as cvs

warnings.filterwarnings("ignore")
CORR_THRESHOLD = 0.25
df= pd.read_csv("filled_responses.csv")
features = []
feat_val = []

def corr_plot():
	global features	
	corr = df.corrwith(df['Gender'])
	corr = corr.sort_values()[:-1]            # The last value is for the gender column itself which is not needed
	corr = corr[abs(corr) >= CORR_THRESHOLD]
	corr = corr.drop("Weight")
	features = list(corr.index)
	cmap = sns.diverging_palette(220,10,as_cmap=False)
	#sns.barplot(corr.values,corr.index )
	#plt.show()
	
def classification():
	global feat_val
	cols = features + ["Gender"]
	data = df[cols]
	data_bal=data	
	x = np.array(data_bal.iloc[:,:-1])
	y = np.array(data_bal.iloc[:,-1])
	x_train, x_test, y_train, y_test = tts(x,y,test_size = 0.25,random_state=23)
	classifiers = [rfc(n_estimators=100,random_state=23) , lr(random_state = 23) , SVC(random_state=23) ]
	methods = ["Random Forest Classifier" , "Logistic Regression" , "Support Vector Machines"]
	print("We are using the K-fold cross-validation for estimating accuracy of the models ")
	print("The accuracy mean with its 95% confidence interval for different methods is as follows")
	for i in range(len(methods)):
		clf = classifiers[i]
		print("Classifier : {}".format(methods[i]))
		clf.fit(x_train,y_train)
		if(i==0):
			feat_val = clf.feature_importances_
		y_pred = clf.predict(x_test)
		#acc = recall_score(y_test, y_pred , average=None).mean()
		#acc = bac(y_test,y_pred)
		#print("Accuracy : {}".format(acc))
		acc = cvs(clf , x,y, cv = 5)
		print("Accuracy: %0.4f (+/- %0.2f)" % (acc.mean(), acc.std() * 2))

def feat_plot():
	global feat_val
	imp_feat = pd.DataFrame(feat_val , index=features , columns=["Importance"])
	imp_feat = imp_feat.sort_values(by = ["Importance"])
	#sns.barplot(imp_feat["Importance"],imp_feat.index)
	#plt.show()

corr_plot()
classification()
feat_plot()


