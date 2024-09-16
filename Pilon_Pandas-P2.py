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

# ### Problem 2

# In[1]:


import pandas as pd


# In[3]:


cars = pd.read_csv('cars.csv')
cars


# ##### A. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.

# In[19]:


# Selects the first 5 rows and every second (odd-numbered) column from the cars DataFrame and stores it in result.
result = cars.iloc[:5, ::2]

# Displays the content of the result
print(result)


# ##### Expected Outcome: First five rows displaying only its odd column

# ##### B. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

# In[29]:


# creates a filter to check if each car’s model is 'Mazda RX4'
# .loc uses this filter to return only the rows where the car model is Maxda RX4
cars.loc[cars['Model']=='Mazda RX4']


# ##### Expected Outcome: Row of Mazda RX4 with all of the columns

# ##### C. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have? 

# In[23]:


# Here we use .loc to access specific row and columns in the Dataframe. 
# This check each rows if there is a Camaro Z28 under model. In which it creates a series of true and false values.
# From the rows where model is Camaro Z28, it picks out cyl column which has the number of cylinders
# Since we expect only one row for 'Camaro Z28', [0] picks the first (and only) value from the array.
cyl = cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0]

# To make the output better, we make use of the print function.
print("The Camaro Z28 has", cyl, "cylinders")



# ##### Expected Outcome: It will display how many cylinders Camaro Z28 has

# ##### D. Determine how many cylinders ('cyl') and what gear type ('gear') do the models 'Mazda RX4 Wag', 'Ford Pantera L' and 'Honda Civic' have.

# In[40]:


# this checks if the values in the 'Model' are  Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’
# It uses a bitwise OR so it can combine the conditions.
result = cars.loc[
    (cars['Model'] == 'Mazda RX4 Wag') | 
    (cars['Model'] == 'Ford Pantera L') | 
    (cars['Model'] == 'Honda Civic'), 
# This specify to only return the 'cyl' and 'gear' column from the rows ehere the models matches
    ['cyl', 'gear']
]

# Display the result
print(result)


# ##### Expected Outcome: It will show how many cylinders and gears the Mazda RX4 Wag, Ford Pantera L, and Honda Civic have.

# In[ ]:




