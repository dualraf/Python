import pandas as pd
df = pd.read_csv('assets/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')

df['Data_Value']=df['Data_Value']/10
tmax=df[df['Element']=='TMAX']
tmin=df[df['Element']=='TMIN']

# create a DataFrame of maximum temperature by date
tmaxdays=tmax[(tmax['Date']!='2012-02-29') & (tmax['Date']!='2008-02-29')]
tmaxdays=tmaxdays.set_index('Date').sort_index()
tmaxdays=tmaxdays.groupby('Date').agg({'Data_Value':np.max})
# create a DataFrame of minimum temperatures by date
tmindays=tmin[(tmin['Date']!='2012-02-29') & (tmin['Date']!='2008-02-29')]
tmindays=tmindays.set_index('Date').sort_index()
tmindays=tmindays.groupby('Date').agg({'Data_Value':np.min})

# calculate the minimum and maximum values for the day of the year for 2005 through 2014
tmaxdays=tmaxdays.reset_index()
tmindays=tmindays.reset_index()
daysmax=tmaxdays[tmaxdays['Date'] < '2015']
daysmax['Date']=pd.to_datetime(daysmax['Date'])
daysmax['year']=daysmax['Date'].dt.year
daysmax['month']=daysmax['Date'].dt.month
daysmax['day']=daysmax['Date'].dt.day
daysmax=daysmax.pivot_table(index=('month','day'),values='Data_Value',aggfunc='max')
daysmax=daysmax.reset_index()
daysmax=daysmax['Data_Value']

daysmin=tmindays[tmindays['Date'] < '2015']
daysmin['Date']=pd.to_datetime(daysmin['Date'])
daysmin['year']=daysmin['Date'].dt.year
daysmin['month']=daysmin['Date'].dt.month
daysmin['day']=daysmin['Date'].dt.day
daysmin=daysmin.pivot_table(index=('month','day'),values='Data_Value',aggfunc='min')
daysmin=daysmin.reset_index()
daysmin=daysmin['Data_Value']

# calculate the minimum and maximum values for the years 2015
tmax2015=tmaxdays[tmaxdays['Date'] >= '2015']['Data_Value']
tmin2015=tmindays[tmindays['Date'] >= '2015']['Data_Value']

# put your plotting code here!
days=np.arange(0,365)
plt.figure(figsize=(15,8))
plt.plot(days,daysmax,'--r',color='blue',label='Maximum daily temperatures from 2005-2014')
plt.plot(days,daysmin,'--r',color='red',label='Minimum daily temperatures from 2005-2014')
plt.gca().fill_between(range(len(days)),daysmin,daysmax,facecolor='gray',alpha=0.2)

for day in days:
    if tmax2015.iloc[day]<=daysmax.iloc[day]:
        tmax2015.iloc[day]=np.nan
    if tmin2015.iloc[day]>=daysmin.iloc[day]:
        tmin2015.iloc[day]=np.nan

plt.scatter(days,tmax2015,s=30,c='black',label='Data from 2015 which is greater/less than 2005-2014')
plt.scatter(days,tmin2015,s=30,c='black')

plt.xlabel('Days of the year')
plt.ylabel('Temperature °C')
plt.title('Temperature records of 2015 based on records from 2005-2014')
plt.legend(loc=4,frameon=False,title='Legend');