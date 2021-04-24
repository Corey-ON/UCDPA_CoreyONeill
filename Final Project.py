#import numpy as np
#import seaborn as sns
#import matplotlib.pyplot as plt

import pandas as pd

dataset = pd.read_csv("nyc-rolling-sales.csv")

##print my first 5 row
print(dataset.head())

##sort by SALE PRICE
print(dataset.sort_values('SALE PRICE'))

##check for missing values
print(dataset.isnull().sum())

## fill the missing values with 0
cleaned_data = dataset.fillna(0)
print(cleaned_data.isnull().sum())

## drop duplicates based on column
drop_duplicates = dataset.drop_duplicates(subset=['NEIGHBORHOOD'])
print(dataset.shape,drop_duplicates.shape)

## Sample DataFrame
df = pd.DataFrame({'BUILDING' : ['A1','A1','B1','B1','B1','B9','C0','C0','C0','C0','C0'],
                   'ZIP CODE' : [10457, 10458, 10457, 10457, 10457, 10458, 10458, 10458, 10458, 10457, 10457],
                   'RESIDENTIAL UNITS' : [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]})
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
    if x == 'SALES PRICE':
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
                   'RESIDENTIAL UNITS' : [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]})
print(df1)

##Create DataFrame 2
df2 = pd.DataFrame({'BUILDING' : ['A1','A1','B1','B1','B1','B9','C0','C0','C0','C0','C0'],
                   'ZIP CODE' : [10457, 10458, 10457, 10457, 10457, 10458, 10458, 10458, 10458, 10457, 10457]})
print(df2)

##Merge DataFrame
df3 = pd.merge(df1,df2, on='BUILDING')
print(df3)

## Define count_entries()
def count_entries(df, BUILDING):

    ## Initialize an empty dictionary: ADDRESS_count
    ADDRESS_count = {}

    ## Extract column from DataFrame: col
    col = df[BUILDING]

    ## Iterate over ADDRESS column in DataFrame
    for entry in col:

    # if the address is in ADDRESS_counts, add 1
    if entry in ADDRESS_count.keys():
        ADDRESS_count[entry] += 1