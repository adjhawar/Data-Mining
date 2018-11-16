					CS685A Project: Effect of Gender on Young People
						Group 18
Instructions:
Responses.csv is the original data file and columns.csv contains the description of all the column names. Filled responses is the file  which contains the data after missing values are filled and outliers are  removed. 

1. Run python preprocess.py
 
2. Run correlation.py

Correlation.py contains three functions. First one is corr_plot which does feature reduction on the basis of correlation and finds the good features which are stored in variable features. Second one is classification, which builds different classifiers from the important features and tries to predict the gender. Their respective accuracies are calculated.  

Data PreProcessing

The rows containing null values for "Gender" are removed.

The some data values contain String values. Those values were mapped to integers as:
1. Smoking {'never smoked': 0, 'tried smoking': 1, 'current smoker': 2, 'former smoker': 3}
2. Alcohol {'drink a lot': 2, 'social drinker': 1, 'never': 0}
3. Punctuality {'i am always on time': 0, 'i am often early': 1, 'i am often running late': 2}
4. Lying {'never': 0, 'sometimes': 1, 'everytime it suits me': 2, 'only to avoid hurting someone': 3}
5. Internet usage {'few hours a day': 0, 'less than an hour a day': 1, 'most of the day': 2}
6. Gender {'female': 0, 'male': 1}
7. Left - right handed {'right handed': 0, 'left handed': 1}
8. Education {'college/bachelor degree': 3, 'secondary school': 2, 'primary school': 1, 'masters degree': 4, 'doctorate degree': 5, 'currently a primary school pupil': 0}
9. Only child {'no': 0, 'yes': 1}
10. Village - town {'village': 0, 'city': 1}
11. House - block of flats {'block of flats': 0, 'house/bungalow': 1}

Filling missing values
The most correlated columns were found out using 0.43 as the threshold. The values are filled using the mean of the respective groups.
The uncorrelated columns are filled using probability distribution
