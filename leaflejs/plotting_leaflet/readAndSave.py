import pandas as pd
import matplotlib.pyplot as plt
import folium
import numpy as np
import csv

# with open('handled_csv/mean.csv') as file:
#     reader = csv.reader(file, delimiter=' ')
#     line_count = 0
#     for row in reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(
#                 f'\tLatitude: {row[1]}, Longitude: {row[2]}.')
#             line_count += 1
#     print(f'Processed {line_count} lines.')

df = pd.read_csv('leaflejs\data\Biking.csv',
                 index_col='phone_long',
                #  index_col='phone_lat',
                 header=0,
                 names=['lng', 'lat'])
df.to_csv('handled_csv/test.csv')
