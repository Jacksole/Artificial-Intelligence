# Required Imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def read_data(input_file):
    input_data = np.loadtxt(input_file, delimiter=None)


dates = pd.date_range('1950-01', periods=input_data.shape[0], freq='M')

output = pd.Series(input_data[:, index], index=dates)
return output

if __name__ == '__main__':

input_file = "./AO.txt"
timeseries = read_data(input_file)

plt.figure()
timeseries.plot()
plt.show()

timeseries['1980':'1990'].plot()
<matplotlib.axes._subplots.AxesSubplot at 0xa0e4b00 >

plt.show()

timeseries.mean()
timeseries.max()
timeseries.min()
timeseries.describe()
timeseries_mm = timeseries.resample("A").mean()
timeseries_mm.plot(style='g--')
plt.show()
timeseries_mm = timeseries.resample("A").median()
timeseries_mm.plot()
plt.show()
timeseries.rolling(window=12, center=False).mean().plot(style='-g')
plt.show()
