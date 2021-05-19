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


## Drop rows with duplicate indices
# Drop any duplicate rows, only keeping last row seen
# this is necessary because sometimes yahoo finance will return duplicate rows 
# for a given date. Saw this on 2021-03-28 for ETH-USD
# 2021-03-27,1732.8243408203125,1674.3193359375,1703.0361328125,1716.49462890625,18102277710.0,1716.49462890625
# 2021-03-28,1728.5841064453125,1672.660400390625,1716.4056396484375,1691.35595703125,16599472938.0,1691.35595703125
# 2021-03-28,1837.18798828125,1683.716552734375,1691.26318359375,1819.6849365234375,22796570548.0,1819.6849365234375
# 2021-03-29,1860.9747314453125,1793.92236328125,1819.46630859375,1846.03369140625,22512781703.0,1846.03369140625
dedup = ticker_data.groupby(ticker_data.index).last()



## Example of creating an empty dataframe and then adding columns to it

def percent_return(start_val: float, end_val: float) -> float:
    """Calculate percent return"""
    return ((end_val - start_val)/start_val) * 100

def percent_return_df(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate inter-index percent returns all the columns of a dataframe

    Args:
        df: the input data frame

    Returns:
        a new dataframe with percent returns for all of the columns
    """
    new_df = pd.DataFrame()
    for column in df.columns:
        shifted = df[column].shift(1)
        new_df[column] = percent_return(shifted, df[column])
    return new_df