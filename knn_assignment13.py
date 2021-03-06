# -*- coding: utf-8 -*-
"""KNN_Assignment13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rGMeOwtf5f7FEaJ60sJhz7h51eWOTaql
"""

#Social_Networks_Ads.csv

"""**Importing the libraries**"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split



"""**Importing the dataset**"""

data=pd.read_csv('Social_Network_Ads.csv')
data.info()

data=data.drop('User ID',axis=1)
label_encode=LabelEncoder()
data['Gender']=label_encode.fit_transform(data['Gender'])
data

"""**Splitting the dataset into the Training set and Test set**"""

x=data[['Gender','Age','EstimatedSalary']]
y=data[['Purchased']]
X_Train,X_Test,y_Train,y_Test=train_test_split(x,y,test_size=0.25,random_state=2)

"""**Feature Scaling**"""

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_Train=sc.fit_transform(X_Train)
X_Test=sc.transform(X_Test)

"""**Fitting K-NN to the Training set**"""

from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier()
model.fit(X_Train,y_Train)

"""**Predicting the Test set results**"""

y_predict=model.predict(X_Test)

"""**Making the Confusion Matrix**"""

from sklearn.metrics import confusion_matrix,plot_roc_curve,accuracy_score
cnf_matrix = confusion_matrix(y_Test, model.predict(X_Test))
print(cnf_matrix)
print(accuracy_score(y_Test, model.predict(X_Test)))

plot_roc_curve(model, X_Test, y_Test)