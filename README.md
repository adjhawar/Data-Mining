The rows containing null values were removed.

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
The most correlated columns were found out using 0.5 as the threshold. The value to be used in case of eprfect correlation was multiplied with the correlation factor and then rounded up to the nearest integer in most cases of ordinal data.
For handling continuous data like :"Age","Height" and "Weight", normalisation was used before multiplying by the correlation
In case of binary data like "Gender", the distribution was found out in the each group and the value was filled using a biased bernoulli distribution.
The uncorrelated ordinal values are similarly filled as the binary categories.
