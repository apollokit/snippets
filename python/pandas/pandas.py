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
