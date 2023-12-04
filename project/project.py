import csv
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)

df = pd.read_csv("Food-Prices_Peru.csv")

df = df.drop(df.columns[[0,1,2,3,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,34,36,37]], axis=1)

df = df.rename({'Population [Pop]':'Pop','Millions of people who cannot afford a healthy diet [CoHD_unafford_n]':'CoHD_unafford_n',
              'Percent of the population who cannot afford a healthy diet [CoHD_headcount]':'CoHD_headcount',
              'Affordability of a healthy diet: ratio of cost to the food poverty line [CoHD_pov]':'CoHD_pov',
              'Cost of a healthy diet [CoHD]':'CoHD'},axis=1)

df.replace('..',np.NaN,inplace=True)
df=df[0:15]
df=df.astype(float)
df=df.groupby(by='Time').mean()

print(df)
