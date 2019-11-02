# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 23:56:59 2019

@author: simiyu
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset = pd.read_csv('H:/training/data/projects/datascience/simple linear regression/python/kc_house_data.csv')

print(dataset.head())

dataset.shape

"""To see the statistical details of the dataset, we can use describe()"""

dataset.describe()

"""check which are the columns the contains NaN values"""

dataset.isnull().any()

"""Our next step is to divide the data into “attributes” and “labels”.
 X variable contains all the attributes/features and y variable contains labels
 
 //For multiple regression
 X = dataset[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH',
 'sulphates','alcohol']].values"""
 
y = dataset['price'].values
x = dataset['sqft_living'].values

"""Let's check the average value of the "Price" column."""

plt.figure(figsize=(15,10))
plt.tight_layout()
seabornInstance.distplot(dataset['price'])

"""Now lets fit our model."""

model = LinearRegression()
model.fit(x.reshape(-1, 1), y.reshape(-1, 1))



"""And finally, let’s plot our data points on a 2-D graph to eyeball our dataset and see if we can manually find any 
relationship between the data"""

dataset.plot(x='sqft_living', y='price', style='o')  
plt.title('sqft_living vs price')  
plt.xlabel('sqft_living')  
plt.ylabel('price')  
plt.show()