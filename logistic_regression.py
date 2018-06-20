# Logistic Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

# Importing the dataset
dataset = pd.read_csv('https://true-story-web-service.herokuapp.com/getTrackingWithHeader.php')
#indepandant varibale [:meens all line, :-1 meend all culumn without the last one]
X = dataset.iloc[:,[0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]].values
#dependet varible [:all lines, 3 only 3 culomn]
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 42)

# Feature Scaling - without dummy
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting Logistic Regression to the Training set - learning
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

result = classifier.score(X_test, y_test)

# Predicting the Test set results - y_pred will be the vector of prediction
y_pred = classifier.predict(X_test)

# save the model to disk
filename = 'finalized_model.sav'
pickle.dump(classifier, open(filename, 'wb'))

# save the score to disk
filename = 'score_model.sav'
pickle.dump(result, open(filename, 'wb'))
