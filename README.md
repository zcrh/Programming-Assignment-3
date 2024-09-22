# PROGRAMMING ASSIGNMENT 3 ✏️
## PYTHON DATA ANALYSIS (PANDAS)
A Python library called Pandas is used to manipulate data collections. Its features include data manipulation, cleansing, analysis, and exploration.
Wes McKinney came up with the moniker "Pandas" in 2008. It stands for both "Panel Data" and "Python Data Analysis".


### I. Intended Learning Outcomes:
1. To identify the codes and functions incorporated in the Pandas library
2. To be able to apply and use the different codes and functions in creating a Python program using a Pandas library

### II. Instructions:
For this programming assignment, download the following file and save to your default user folder:
http://bit.ly/Cars_file

## **_PROBLEM 1_** 
Save your file as Surname_Pandas-P1.py.

Using knowledge obtained from the experiment and demonstrations:

a. Load the corresponding .csv file into a data frame named cars using pandas

b. Display the first five and last five rows of the resulting cars.

### In this problem, we:
- Load a .csv file into a pandas DataFrame named cars using the pandas library.
- Display the first five rows of the DataFrame.
- Display the last five rows of the DataFrame.

### 🖥️ INPUT CODE (A):
```python
# the pd.read_csv is a function that reads data from the cars.csv file into a Dataframe
# the variable cars now holds the data in which you can view and manipulate
cars = pd.read_csv('cars.csv')

# this will show you the contents of the Dataframe
cars
```
### 🏁 EXPECTED OUTPUT (A):
```
Model	mpg	cyl	disp	hp	drat	wt	qsec	vs	am	gear	carb
0	Mazda RX4	21.0	6	160.0	110	3.90	2.620	16.46	0	1	4	4
1	Mazda RX4 Wag	21.0	6	160.0	110	3.90	2.875	17.02	0	1	4	4
2	Datsun 710	22.8	4	108.0	93	3.85	2.320	18.61	1	1	4	1
3	Hornet 4 Drive	21.4	6	258.0	110	3.08	3.215	19.44	1	0	3	1
4	Hornet Sportabout	18.7	8	360.0	175	3.15	3.440	17.02	0	0	3	2
5	Valiant	18.1	6	225.0	105	2.76	3.460	20.22	1	0	3	1
6	Duster 360	14.3	8	360.0	245	3.21	3.570	15.84	0	0	3	4
7	Merc 240D	24.4	4	146.7	62	3.69	3.190	20.00	1	0	4	2
8	Merc 230	22.8	4	140.8	95	3.92	3.150	22.90	1	0	4	2
9	Merc 280	19.2	6	167.6	123	3.92	3.440	18.30	1	0	4	4
10	Merc 280C	17.8	6	167.6	123	3.92	3.440	18.90	1	0	4	4
11	Merc 450SE	16.4	8	275.8	180	3.07	4.070	17.40	0	0	3	3
12	Merc 450SL	17.3	8	275.8	180	3.07	3.730	17.60	0	0	3	3
13	Merc 450SLC	15.2	8	275.8	180	3.07	3.780	18.00	0	0	3	3
14	Cadillac Fleetwood	10.4	8	472.0	205	2.93	5.250	17.98	0	0	3	4
15	Lincoln Continental	10.4	8	460.0	215	3.00	5.424	17.82	0	0	3	4
16	Chrysler Imperial	14.7	8	440.0	230	3.23	5.345	17.42	0	0	3	4
17	Fiat 128	32.4	4	78.7	66	4.08	2.200	19.47	1	1	4	1
18	Honda Civic	30.4	4	75.7	52	4.93	1.615	18.52	1	1	4	2
19	Toyota Corolla	33.9	4	71.1	65	4.22	1.835	19.90	1	1	4	1
20	Toyota Corona	21.5	4	120.1	97	3.70	2.465	20.01	1	0	3	1
21	Dodge Challenger	15.5	8	318.0	150	2.76	3.520	16.87	0	0	3	2
22	AMC Javelin	15.2	8	304.0	150	3.15	3.435	17.30	0	0	3	2
23	Camaro Z28	13.3	8	350.0	245	3.73	3.840	15.41	0	0	3	4
24	Pontiac Firebird	19.2	8	400.0	175	3.08	3.845	17.05	0	0	3	2
25	Fiat X1-9	27.3	4	79.0	66	4.08	1.935	18.90	1	1	4	1
26	Porsche 914-2	26.0	4	120.3	91	4.43	2.140	16.70	0	1	5	2
27	Lotus Europa	30.4	4	95.1	113	3.77	1.513	16.90	1	1	5	2
28	Ford Pantera L	15.8	8	351.0	264	4.22	3.170	14.50	0	1	5	4
29	Ferrari Dino	19.7	6	145.0	175	3.62	2.770	15.50	0	1	5	6
30	Maserati Bora	15.0	8	301.0	335	3.54	3.570	14.60	0	1	5	8
31	Volvo 142E	21.4	4	121.0	109	4.11	2.780	18.60	1	1	4	2

```
For much clearer result:

![Screenshot 2024-09-23 034350](https://github.com/user-attachments/assets/22ade6a0-5f87-47ea-ae5a-ddca55b2b6e0)

The expected output will display all the data stored in the excel file

### 🖥️ INPUT CODE (B):
```python
# This line of code displays the string 'First five rows:' 
print("\nFirst five rows: ")
# .head returns the first five rows of the Dataframe cars. Using the print function, it displays the result.
print(cars.head())
```
### 🏁 EXPECTED OUTPUT (B):
```
First five rows: 
               Model   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  carb
0          Mazda RX4  21.0    6  160.0  110  3.90  2.620  16.46   0   1     4     4
1      Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1     4     4
2         Datsun 710  22.8    4  108.0   93  3.85  2.320  18.61   1   1     4     1  
3     Hornet 4 Drive  21.4    6  258.0  110  3.08  3.215  19.44   1   0     3     1
4  Hornet Sportabout  18.7    8  360.0  175  3.15  3.440  17.02   0   0     3     2

```
The expected output will display the first five rows of the dataframe cars.

To save the Jupyter Notebook file as .py, go to the File tab, find the Save and Export Notebook as..., and choose Executable Script


## **_PROBLEM 2_** 
Save your file as Surname_Pandas-P2.py

Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and
indexing operations.

a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4
Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

### In this problem, we:
- Display the first five rows of a DataFrame with odd-numbered columns.
- Filter the DataFrame to find the row for 'Mazda RX4'.
- Find how many cylinders the 'Camaro Z28' has.
- Extract both the number of cylinders and the gear type for three specific car models: 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic'.

### 🖥️ INPUT CODE (INITIALIZE):
```python
# the pd.read_csv is a function that reads data from the cars.csv file into a Dataframe
# the variable cars now holds the data in which you can view and manipulate
cars = pd.read_csv('cars.csv')

# this will show you the contents of the Dataframe
cars
```
### 🏁 EXPECTED OUTPUT (INITIALIZE):
```
Model	mpg	cyl	disp	hp	drat	wt	qsec	vs	am	gear	carb
0	Mazda RX4	21.0	6	160.0	110	3.90	2.620	16.46	0	1	4	4
1	Mazda RX4 Wag	21.0	6	160.0	110	3.90	2.875	17.02	0	1	4	4
2	Datsun 710	22.8	4	108.0	93	3.85	2.320	18.61	1	1	4	1
3	Hornet 4 Drive	21.4	6	258.0	110	3.08	3.215	19.44	1	0	3	1
4	Hornet Sportabout	18.7	8	360.0	175	3.15	3.440	17.02	0	0	3	2
5	Valiant	18.1	6	225.0	105	2.76	3.460	20.22	1	0	3	1
6	Duster 360	14.3	8	360.0	245	3.21	3.570	15.84	0	0	3	4
7	Merc 240D	24.4	4	146.7	62	3.69	3.190	20.00	1	0	4	2
8	Merc 230	22.8	4	140.8	95	3.92	3.150	22.90	1	0	4	2
9	Merc 280	19.2	6	167.6	123	3.92	3.440	18.30	1	0	4	4
10	Merc 280C	17.8	6	167.6	123	3.92	3.440	18.90	1	0	4	4
11	Merc 450SE	16.4	8	275.8	180	3.07	4.070	17.40	0	0	3	3
12	Merc 450SL	17.3	8	275.8	180	3.07	3.730	17.60	0	0	3	3
13	Merc 450SLC	15.2	8	275.8	180	3.07	3.780	18.00	0	0	3	3
14	Cadillac Fleetwood	10.4	8	472.0	205	2.93	5.250	17.98	0	0	3	4
15	Lincoln Continental	10.4	8	460.0	215	3.00	5.424	17.82	0	0	3	4
16	Chrysler Imperial	14.7	8	440.0	230	3.23	5.345	17.42	0	0	3	4
17	Fiat 128	32.4	4	78.7	66	4.08	2.200	19.47	1	1	4	1
18	Honda Civic	30.4	4	75.7	52	4.93	1.615	18.52	1	1	4	2
19	Toyota Corolla	33.9	4	71.1	65	4.22	1.835	19.90	1	1	4	1
20	Toyota Corona	21.5	4	120.1	97	3.70	2.465	20.01	1	0	3	1
21	Dodge Challenger	15.5	8	318.0	150	2.76	3.520	16.87	0	0	3	2
22	AMC Javelin	15.2	8	304.0	150	3.15	3.435	17.30	0	0	3	2
23	Camaro Z28	13.3	8	350.0	245	3.73	3.840	15.41	0	0	3	4
24	Pontiac Firebird	19.2	8	400.0	175	3.08	3.845	17.05	0	0	3	2
25	Fiat X1-9	27.3	4	79.0	66	4.08	1.935	18.90	1	1	4	1
26	Porsche 914-2	26.0	4	120.3	91	4.43	2.140	16.70	0	1	5	2
27	Lotus Europa	30.4	4	95.1	113	3.77	1.513	16.90	1	1	5	2
28	Ford Pantera L	15.8	8	351.0	264	4.22	3.170	14.50	0	1	5	4
29	Ferrari Dino	19.7	6	145.0	175	3.62	2.770	15.50	0	1	5	6
30	Maserati Bora	15.0	8	301.0	335	3.54	3.570	14.60	0	1	5	8
31	Volvo 142E	21.4	4	121.0	109	4.11	2.780	18.60	1	1	4	2

```
For much clearer result:


![Screenshot 2024-09-23 034350](https://github.com/user-attachments/assets/22ade6a0-5f87-47ea-ae5a-ddca55b2b6e0)

The expected output will display all the data stored in the excel file where we will get all the relevant datas.

### 🖥️ INPUT CODE (A):
```python
# Selects the first 5 rows and every second (odd-numbered) column from the cars DataFrame and stores it in result.
result = cars.iloc[:5, ::2]

# Displays the content of the result
print(result)
```
### 🏁 EXPECTED OUTPUT (A):
```
               Model  cyl   hp     wt  vs  gear
0          Mazda RX4    6  110  2.620   0     4
1      Mazda RX4 Wag    6  110  2.875   0     4
2         Datsun 710    4   93  2.320   1     4
3     Hornet 4 Drive    6  110  3.215   1     3
4  Hornet Sportabout    8  175  3.440   0     3

```
The expected output will display the first five rows with odd-numbered columns

### 🖥️ INPUT CODE (B):
```python
# creates a filter to check if each car’s model is 'Mazda RX4'
# .loc uses this filter to return only the rows where the car model is Maxda RX4
cars.loc[cars['Model']=='Mazda RX4']
```
### 🏁 EXPECTED OUTPUT (B):
```
      Model	  mpg	  cyl	  disp	   hp	  drat	  wt	qsec	vs	am	gear	carb
0	Mazda RX4	  21.0	  6	  160.0	  110	  3.9	  2.62	16.46	 0	 1	   4	   4

```
For much clearer result:
![Screenshot 2024-09-23 034634](https://github.com/user-attachments/assets/4d7d87c3-f442-4f08-aab4-3ce7e22bb67c)

The expected output will display the row of Maxda RX4 with all of its columns

### 🖥️ INPUT CODE (C):
```python
# Here we use .loc to access specific row and columns in the Dataframe. 
# This check each rows if there is a Camaro Z28 under model. In which it creates a series of true and false values.
# From the rows where model is Camaro Z28, it picks out cyl column which has the number of cylinders
# Since we expect only one row for 'Camaro Z28', [0] picks the first (and only) value from the array.
cyl = cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0]

# To make the output better, we make use of the print function.
print("The Camaro Z28 has", cyl, "cylinders")
```
### 🏁 EXPECTED OUTPUT (C):
```
The Camaro Z28 has 8 cylinders
```

The expected output will display how many cylinders Camaro Z28 has.

### 🖥️ INPUT CODE (D):
```python
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

```
### 🏁 EXPECTED OUTPUT (D):
```
    cyl  gear
1     6     4
18    4     4
28    8     5

```

The expected output will display how many cylinders, gears, and the row where Mazda RX4 Wag, Ford Pantera L, and Honda Civic are located.


