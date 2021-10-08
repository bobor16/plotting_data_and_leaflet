import pandas as pd
import matplotlib.pyplot as plt
import folium
import numpy as np
import csv

# Read the biking.csv file
base_df = pd.read_csv("data/Biking.csv")


def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w


# Data for plotting
x = base_df["phone_lat"]
y = base_df["phone_long"]

x_mean = moving_average(x, 10)
y_mean = moving_average(y, 10)

fieldNames = ['lng', 'lat']
rows = [
    {'lng': x_mean,
     'lat': y_mean}
]

with open('handled_csv/mean.csv', 'w', encoding='UTF8', newline='') as f:

    writer = csv.DictWriter(f, fieldnames=fieldNames)
    writer.writeheader()
    writer.writerows(rows)

df = pd.read_csv('handled_csv/mean.csv')


# Create a map with a location start point
myMap = folium.Map(zoom_start=12, location=[56.25714966666666, 10.0690625])

# Iterate through the csv file and save a html file with the
for i, r in base_df.iterrows():
    folium.map.Marker(
        location=[r['phone_lat'], r['phone_long']],
        # location=[test_x, test_y],
        popup=[x, y],
        icon=folium.Icon(color="green", icon="bicycle", prefix='fa')
    ).add_to(myMap)

myMap.save('html/mean.html')
