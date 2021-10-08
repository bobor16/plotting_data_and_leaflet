import pandas as pd
import matplotlib.pyplot as plt
import folium
import numpy as np
import csv

# Read the biking.csv file
base_df = pd.read_csv("leaflejs/data/Driving.csv")


def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w


# Data for plotting
x = base_df["phone_lat"]
y = base_df["phone_long"]


# Create a map with a location start point
myMap = folium.Map(zoom_start=12, location=[56.25714966666666, 10.0690625])

# Iterate through the csv file and save a html file with the
for i, r in base_df.iterrows():
    folium.map.Marker(
        location=[r['phone_lat'], r['phone_long']],
        popup=[r['phone_lat'], r['phone_long']],
        icon=folium.Icon(color="green", icon="car", prefix='fa')
    ).add_to(myMap)

myMap.save('html/mean.html')
