from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score
import pickle

df1 = pd.read_csv('final1.csv')
df1.drop(columns='Unnamed: 0',inplace=True)
X = df1.drop(columns = ['rating_engineTransmission'])
Y = df1['rating_engineTransmission']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.33)

print(X_train)

clf = DecisionTreeClassifier(random_state=0)
clf.fit(X_train, Y_train)

print(clf.score(X_train, Y_train))
print(clf.score(X_test, Y_test))

pickle.dump(clf, open('model.pkl','wb'))