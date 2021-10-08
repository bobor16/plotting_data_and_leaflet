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


fig, ax = plt.subplots()

ax.plot(x, y)
ax.plot(x_mean, y_mean)

ax.set(xlabel='phone_lat', ylabel='phone_long',
       title='')
ax.grid()

fig.savefig("Mean.png")
plt.show()