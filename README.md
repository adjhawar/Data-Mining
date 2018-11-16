					CS685A Project: Effect of Gender on Young People
						Group 18
Instructions:
responses.csv is the original data file and columns.csv contains the description of all the column names. Filled responses is the file  which contains the data after missing values are filled and outliers are  removed.

1. Run: python preprocess.py
replaced_responses.csv replaces the string values with the given map:
a. Smoking {'never smoked': 0, 'tried smoking': 1, 'current smoker': 2, 'former smoker': 3}
b. Alcohol {'drink a lot': 2, 'social drinker': 1, 'never': 0}
c. Punctuality {'i am always on time': 0, 'i am often early': 1, 'i am often running late': 2}
d. Lying {'never': 0, 'sometimes': 1, 'everytime it suits me': 2, 'only to avoid hurting someone': 3}
e. Internet usage {'few hours a day': 0, 'less than an hour a day': 1, 'most of the day': 2}
f. Gender {'female': 0, 'male': 1}
g. Left - right handed {'right handed': 0, 'left handed': 1}
h. Education {'college/bachelor degree': 3, 'secondary school': 2, 'primary school': 1, 'masters degree': 4, 'doctorate degree': 5, 'currently a primary school pupil': 0}
i. Only child {'no': 0, 'yes': 1}
j. Village - town {'village': 0, 'city': 1}
k. House - block of flats {'block of flats': 0, 'house/bungalow': 1}

filled_responses.csv contains the csv final preprocessed csv file after filing missing values, outlier removal and information correction.

2. Run:python correlation.py

Correlation.py contains three functions. First one is corr_plot which does feature reduction on the basis of correlation and finds the good features which are stored in variable features. Second one is classification, which builds different classifiers from the important features and tries to predict the gender. Their respective accuracies are calculated.

3. Run:python visual.py
This file generates plots for each column with "Gender"
