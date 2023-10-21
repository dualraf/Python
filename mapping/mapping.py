import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#version 3.8
import matplotlib as mpl
import math

mpl.rcParams['figure.figsize'] = [16.0,8.0]

#sacando la data
df=pd.read_csv("mapping/wipeout.csv")
#print(df.head())

#It turns out that this particular data source is trying to capture 
# the maximum prescision possible in an unsigned integer, so we 
# first need to convert these to more traditional decimal format

df["position_lat_degrees"] = df["position_lat"] * ( 180 / 2**31 )
df["position_long_degrees"] = df["position_long"] * ( 180 / 2**31 )

#https://wiki.openstreetmap.org/wiki/Mercator
#convertir de latitude a Mercantor projection flat

def lat2y(a):
  return 180.0/math.pi*math.log(math.tan(math.pi/4.0+a*(math.pi/180.0)/2.0))
df["position_lat_degrees_mercantor"]=df["position_lat_degrees"].apply(lat2y)

df=df[['timestamp','enhanced_altitude','enhanced_speed','heart_rate','position_lat_degrees_mercantor',
       'position_long_degrees','position_lat_degrees']].dropna()
print(df.head())

# First the image. I got mine through an export from Open Street Map and saved it in map.png. You can get a
# map directly from http://www.openstreetmap.org. To display this, we use the pyplot imread() function and
# pair it with imshow()
image=plt.imread("mapping/map.png")
plt.imshow(image, alpha=0.5, extent=[-83.77141,-83.75977,46.75230,46.76620])
#plt.show()

# Plot our longitude and mercantor projected latitude data. We can set the series of data we want to be the
# colors of points using the c parameters, and we can choose from different color maps using the cmap
# parameter. Also, I'm only going to plot those points which actually appear on the map itself.
small_df = df[(df["position_long_degrees"] > -83.77141) & (df["position_long_degrees"] < -83.75977) & 
              (df["position_lat_degrees_mercantor"] > 46.75230) & (df["position_lat_degrees_mercantor"] < 46.76620)]

plt.scatter(small_df["position_long_degrees"],small_df["position_lat_degrees_mercantor"],
            s=10, c=small_df["heart_rate"], cmap='Blues', alpha=0.75)
# Now we get pyplot to render a colorbar so we know the meeting of the colors
plt.colorbar().set_label("Heart Rate (bpm)")
# And let's set a meaningful title
plt.suptitle("Heart Rate data from {} to {}".format(np.min(small_df["timestamp"]),np.max(small_df["timestamp"])),size='20')
#plt.show()

# Let's import Folium
import folium
# Now let's render a spot from our previous data, for this we pick the center point of the map and a zoom level
m=folium.Map(location=[42.24,-83.764], zoom_start=12)
# A key eye will notice that I had to reverse our longitude and latitude for this library, *and* I'm not using
# the mercantor changed values for longitude. Welcome to geographical information systems!
#m.show_in_browser()

# We can add callouts to the map using the Marker class, let's set this for our start and end.
m=folium.Map(location=[42.296,-83.768], zoom_start=15)
folium.Marker([df["position_lat_degrees"].iloc[0],df["position_long_degrees"].iloc[0]],popup="Start").add_to(m)
folium.Marker([df["position_lat_degrees"].iloc[-1],df["position_long_degrees"].iloc[-1]],popup="Stop").add_to(m)
route=folium.PolyLine(locations=zip(df["position_lat_degrees"],df["position_long_degrees"]),weight=5,color='blue').add_to(m)

m.show_in_browser()