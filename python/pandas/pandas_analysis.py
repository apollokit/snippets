import pandas as pd
from datetime import datetime

# make df somehow...

## takes the difference between subsequent rows (first discrete difference)
df_diff = df['column'].diff()


## rolling mean over three subsequent rows
df_plot = df['column'].diff()
df_plot = df_plot.rolling(window = 3).mean()


## latch onto the maximum value over a window of the preceding 30 rows
# note that min_periods = 1 means that even if we have a window with 29 NaNs
# in it, we'll still use the one valid data point. This is useful for the
# beginning of a dataframe
df_plot = df['column'].rolling(window = 30, min_periods=1).max()

## apply a function over a window
def window_diff(array: np.ndarray):
    return array[-1] - array[0]
df_plot = df['column'].rolling(window = 30, min_periods=1).apply(window_diff, raw = True)

## find latest date (or index) that a certain condition is true
# assume the index of the dataframe is a date time index
is_down = df_down[df_down == 1]
latest_time: datetime = is_down.index[-1].to_pydatetime()

## reverse a dataframe
df = df.iloc[::-1]