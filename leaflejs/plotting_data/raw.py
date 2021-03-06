import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
base_df = pd.read_csv("leaflejs\data\Biking.csv")


def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w


# Data for plotting
x = base_df["phone_lat"]
y = base_df["phone_long"]


fig, ax = plt.subplots()

ax.plot(x, y, color='aqua')

ax.set(xlabel='phone_long', ylabel='phone_lat',
       title='Raw')
ax.grid()

fig.savefig("images/raw.png")
plt.show()
