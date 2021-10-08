import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
base_df = pd.read_csv("Running.csv")


def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w


# Data for plotting
x = base_df["phone_lat"]
y = base_df["phone_long"]

x_mean = moving_average(x, 10)
y_mean = moving_average(y, 10)

x_median = x.rolling(10).median()
y_median = y.rolling(10).median()

fig, ax = plt.subplots()

ax.plot(x, y, color='red')
ax.plot(x_median, y_median, color='green')

ax.set(xlabel='phone_lat', ylabel='phone_long',
       title='Median')
ax.grid()

fig.savefig("images/Median.png")
plt.show()
