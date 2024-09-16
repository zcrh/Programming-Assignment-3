#!/usr/bin/env python
# coding: utf-8

# # Experiment # 3 - Python Data Analysis (PANDAS)
# 
# ### I.Intended Learning Outcomes:
# ##### 1. To identify the codes and functions incorporated in the Pandas library 
# ##### 2. To be able to apply and use the different codes and functions in creating a Python program using a Pandas library
# 
# ### II. Instructions:
# ##### Write a python script/code in the Jupyter Notebook to do the given problems. You may submit your Jupyter notebook in the dedicated submission bin.

# ### Probem 1

# ##### A. Load the corresponding .csv file into a data frame named cars using pandas

# In[70]:


import pandas as pd


# In[68]:


# the pd.read_csv is a function that reads data from the cars.csv file into a Dataframe
# the variable cars now holds the data in which you can view and manipulate
cars = pd.read_csv('cars.csv')

# this will show you the contents of the Dataframe
cars


# ##### Expected Outcome: It displays all the data stored in the cars excel file.

# ##### B. Display the first five and last five rows of the resulting cars

# In[37]:


# This line of code displays the string 'First five rows:' 
print("\nFirst five rows: ")
# .head returns the first five rows of the Dataframe cars. Using the print function, it displays the result.
print(cars.head())


# ##### Expected Outcome: The output will show the first five rows of the Dataframs cars

# In[77]:


# This line of code displays the string 'Last five rows:' 
print("\nLast five rows: ")
# .tail returns the last five rows of the Dataframe cars. Using the print function, it displays the result.
print(cars.tail())


# ##### Expected Outcome: The output will show the last five rows of the Dataframs cars
