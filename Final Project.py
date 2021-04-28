#import numpy as np
#import seaborn as sns
#import matplotlib.pyplot as plt

import pandas as pd

dataset = pd.read_csv("nyc-rolling-sales.csv")

## To display any top 5 rows
print(dataset.head())

##sort by SALE PRICE
print(dataset.sort_values('SALE PRICE'))

##check for missing values
print(dataset.isnull().sum())

## drop duplicates based on column
drop_duplicates = dataset.drop_duplicates(subset=['NEIGHBORHOOD'])
print(dataset.shape,drop_duplicates.shape)

## Sample DataFrame
df = pd.DataFrame({'BUILDING' : ['A1','A1','B1','B1','B1','B9','C0','C0','C0','C0','C0'],
                   'ZIP_CODE' : [10457, 10458, 10457, 10457, 10457, 10458, 10458, 10458, 10458, 10457, 10457],
                   'RESIDENTIAL_UNITS' : [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]})
print(df)

## looping
BUILDING = ['A1','A1','B1','B1','B1','B9','C0','C0','C0','C0','C0']
for BUILDING in BUILDING:
    print(BUILDING)

Data = dataset
for Data in Data:
    print(Data)

Data = dataset
for x in dataset:
    if x == 'SALES_PRICE':
        continue
        print(x)

Data = dataset
for x in dataset:
    if x == 'corey':
        continue
        print(x)
    else:
        print('NA')

## Merging DataFrames
##Create DataFrame 1
df1 = pd.DataFrame({'BUILDING' : ['A1','A1','B1','B1','B1','B9','C0','C0','C0','C0','C0'],
                   'RESIDENTIAL_UNITS' : [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]})
print(df1)

##Create DataFrame 2
df2 = pd.DataFrame({'BUILDING' : ['A1','A1','B1','B1','B1','B9','C0','C0','C0','C0','C0'],
                   'ZIP_CODE' : [10457, 10458, 10457, 10457, 10457, 10458, 10458, 10458, 10458, 10457, 10457]})
print(df2)

##Merge DataFrame
df3 = pd.merge(df1,df2, on='BUILDING')
print(df3)

## Create a list of strings
NYC = ['BOROUGH', 'NEIGHBORHOOD', 'BUILDING', 'BLOCK',  'ADDRESS']


# Define generator function get_lengths
def get_lengths(input_lists):

    #Yield the length of a string
    for word in input_lists:
        yield len(word)

#print the values generated by get_lengths()
for value in get_lengths(NYC):
    print(value)

##Create a list comprehension
RESIDENTIAL_UNITS = [[0, 0, 0,
                     1, 1, 1,
                     2, 2, 2,
                     3, 3, 3]]
RESIDENTIAL_UNITS = [[col for col in range (3)] for row in range(3)]

##Print squares_RESIDENTIAL_UNITS
for row in RESIDENTIAL_UNITS:
    print(row)

import numpy as np
##calculate monthly rate for mortgage loan that extends for 25 years, amount is $6625000 at annual interest rate 5%
monthly_rate = ((1+0.05)**(1/12) - 1)
print(monthly_rate)

## calculate monthly payment
monthly_payment = -1*(np.pmt(rate=monthly_rate, nper=12*25, pv=6625000))
print(monthly_payment)

##Plot the histogram
import matplotlib.pyplot as plt
##Sample dataframe extraced from dataset
df = pd.DataFrame({'RESIDENTIAL_UNITS' : (5,10,6,8,24,10,24,47,132,3),
                   'SALES_PRICE' : (6625000,3936272,8000000,3192840,16232000,10350000,11900000,28000000,52625000,3300000)})

plt.hist(df)

#Label the axes
plt.xlabel('X')
plt.ylabel('Y')

#show the figure
plt.show()

#Tidy up histogram chart
plt.hist(df, bins = 40)

#Label the axes
plt.xlabel('SALE_PRICE')
plt.ylabel('RESIDENTIAL_UNITS')

plt.title('NYC_Properties')

#show the figure
plt.show()




