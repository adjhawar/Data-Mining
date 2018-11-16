import pandas as pd
import numpy as np
import missingno as msno
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import math

CORR_THRESHOLD = 0.25
df= pd.read_csv("filled_responses.csv")
good_ones = []

def corr_plot():
	global good_ones	
	corr = df.corrwith(df['Gender'])
	corr = corr.sort_values()[:-1]            # The last value is for the gender column itself which is not needed
	corr = corr[abs(corr) >= CORR_THRESHOLD]
	good_ones = df[list(corr.index)]
	sns.barplot(corr.values,corr.index)
	#plt.show()
	
corr_plot()



