# simple linear regression

#importing the libraries 
import numpy as np
import matplotlib as plt
import pandas as pd 


#importing the date sets
 dataset = pd.read_csv('Salary_Data.csv')
 x=dataset.iloc[:,:-1].values
 y=dataset.iloc[:,-1].values
 
 #Splitting the dataset into the Training set and Test set
 from sklearn.model_selection import train_test_split
 x_train,x_test,y_train,y_test  = train_test_split(X, y, test_size = 1/3, random_state = 0)