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