import pandas as pd

## Constructing a dataframe from a bunch of price data, and writing to a csv
# file

# price_data entries look like
# '2010-06-29': {'1. open': '19.0000', '2. high': '25.0000', '3. low': '17.5400', '4. close': '23.8900', '5. volume': '18766300'}

dates = list(price_data.keys())

opens = [val['1. open'] for val in price_data.values()]
highs = [val['2. high'] for val in price_data.values()]
lows = [val['3. low'] for val in price_data.values()]
closes = [val['4. close'] for val in price_data.values()]
volumes = [val['5. volume'] for val in price_data.values()]

df = pd.DataFrame({
    'open': opens,
    'high': highs,
    'low': lows,
    'close': closes,
    'volume': volumes,
    })

# set the dates as the index
df['date'] = pd.to_datetime(dates)
df = df.set_index('date')

# seems like csv from pandas dataframe is fairly compact
df.to_csv(path.join(output_dir, f'{symbol}.dailys.csv'))



## to reimport the file later

df = pd.read_csv(path.join(output_dir, f'{symbol}.dailys.csv'))
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')



# filter a datetime index
if start:
    start_loc = ticker_data.index.get_loc(str(start))
if end:
    end_loc = ticker_data.index.get_loc(str(end))
ticker_data = ticker_data[start_loc:end_loc+1]


# df is like:
# runNum        0                   1                             2                             3    ...       97        98                            99                            100                    
# varIdx          0    1    2         0         1         2         0         1         2         0  ...         2         0         1         2         0         1         2         0         1         2
# time[ns]                                                                                           ...                                                                                                    
# 0.000000e+00  0.0  0.0  0.0  0.095588  0.350777 -0.165411  0.253272  0.153135  0.083613 -0.159307  ... -0.314341  0.052382 -0.141720 -0.211703  0.292257 -0.371662 -0.012782 -0.104897 -0.446828  0.259766
# 2.000000e+11  0.0  0.0  0.0  0.120648  0.347103 -0.155609  0.265635  0.158582  0.052724 -0.159420  ... -0.304203  0.041312 -0.129319 -0.248985  0.308730 -0.395921 -0.044882 -0.166941 -0.445805  0.243711
# 4.000000e+11  0.0  0.0  0.0  0.145668  0.342700 -0.145792  0.278320  0.163664  0.021782 -0.159864  ... -0.294010  0.030634 -0.116601 -0.286191  0.324685 -0.420652 -0.077007 -0.229036 -0.442972  0.227596
# 6.000000e+11  0.0  0.0  0.0  0.170641  0.337567 -0.135900  0.291326  0.168372 -0.009115 -0.160639  ... -0.283759  0.020352 -0.103578 -0.323324  0.340118 -0.445841 -0.109095 -0.291168 -0.438326  0.211417
# 8.000000e+11  0.0  0.0  0.0  0.195563  0.331706 -0.126012  0.304650  0.172695 -0.040025 -0.161746  ...

# count number of runNum indices:
num_mc = df.columns.levshape[0]
# can access all the rows for runNum, varIdx with 
df.loc[:, (runNum, varIdx)]
# and al the columns that have varIdx==0 with
df.loc[:, (slice(None), 0)]
# that slice(None) slices across all of the top level index (runNum)

