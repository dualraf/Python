import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn-colorblind')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)

food_prices = pd.read_csv("Food-Prices_Peru.csv")

food_prices = food_prices.drop(food_prices.columns[[0,1,2,3,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,34,36,37]], axis=1)

food_prices = food_prices.rename({'Population [Pop]':'Pop','Millions of people who cannot afford a healthy diet [CoHD_unafford_n]':'CoHD_unafford_n',
              'Percent of the population who cannot afford a healthy diet [CoHD_headcount]':'CoHD_headcount',
              'Affordability of a healthy diet: ratio of cost to the food poverty line [CoHD_pov]':'CoHD_pov',
              'Cost of a healthy diet [CoHD]':'CoHD'},axis=1)

food_prices.replace('..',np.NaN,inplace=True)
food_prices=food_prices[0:15]
food_prices=food_prices.astype(float)
food_prices=food_prices.groupby(by='Time').mean()
food_prices=food_prices.set_index(pd.Index([2017,2018,2019,2020,2021]))

co2 = pd.read_csv("CO2-Emissions.csv")
co2=co2.drop([4,5,6,7],axis=0)
co2=co2.rename({'1990 [YR1990]':'1990','2000 [YR2000]':'2000','2013 [YR2013]':'2013','2014 [YR2014]':'2014','2015 [YR2015]':'2015',
                '2016 [YR2016]':'2016','2017 [YR2017]':'2017','2018 [YR2018]':'2018','2019 [YR2019]':'2019','2020 [YR2020]':'2020'
                ,'2021 [YR2021]':'2021','2022 [YR2022]':'2022'},axis=1)

emissions=co2[0:2]
emissions.drop(emissions.columns[[0,1,3,14,15]], axis=1,inplace=True)
#emissions=emissions[1:].astype(float)
emissions=emissions.set_index("Country Name")
emissions=emissions.T.astype(float).set_index(pd.Index([1990,2000,2013,2014,2015,2016,2017,2018,2019,2020]))

plt.figure(1)
plt.subplot(2,2,1)
emissions.World.plot(figsize=(20,10),ylabel="CO2",xlabel="Years",title="World Contamination");
plt.subplot(2,2,2)
emissions.Peru.plot(ax=plt.gca(),figsize=(20,10),ylabel="CO2",xlabel="Years",title="Peru Contamination",color="r");

food_prices.iloc[:,:-1].plot(kind = 'barh',figsize=(10,8),ylabel="Years").legend(loc=(1, 0));
#v3 = np.concatenate((v1,v2))

#relation between both datasets
emissions_world=emissions.iloc[6:,0]
#Percent of the population who cannot afford a healthy diet
coHD_headcount = food_prices.iloc[:-1,2]
coHD = food_prices.iloc[:-1,0]
coHD_unafford = food_prices.iloc[:-1,3]
dataset=pd.concat([emissions_world,coHD,coHD_headcount,coHD_unafford],axis=1)

normalized_df=(dataset-dataset.min())/(dataset.max()-dataset.min())

normalized_df.plot(figsize=(10,8),marker='o',linewidth=4).legend(loc=(1, 0));


