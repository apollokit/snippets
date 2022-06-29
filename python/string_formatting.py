# see https://python-reference.readthedocs.io/en/latest/docs/functions/format.html

yo = 0.323432
# print as float with two decimal places
print(f'hey yo: {yo:0.2f}')


yo = 234.23423
# General format. Same as ‘g’ except switches to ‘E’ if the number gets too large. 
# The representations of infinity and NaN are uppercased, too.
print(f'hey yo: {yo:0.2G}')



# print out a well formatted block of text from a list

wid = 12
wid_dollar = 13

print(f'Portfolio day end summary, {str(query_time.date())}')
print(f'{"Ticker":<{wid}}{"Quantity":<{wid}}{"PricePer":<{wid_dollar}}{"Value":<{wid_dollar}}')
for pos in self.positions:
    price = self._assets_data.get_day_close_price(pos.ticker, query_time)
    qnt = pos.quantity
    print(f'{pos.ticker:<{wid}}{qnt:<{wid}}${price:<{wid},.2f}${price*qnt:<{wid},.2f}')

# prints this:
# Portfolio day end summary, 2021-04-26
# Ticker      Quantity    PricePer     Value        
# AAPL        10          $134.84      $1,348.40    
# ETH-USD     10          $379.48      $3,794.84    
# DOGE-USD    10          $0.00        $0.03  



# remove trailing 0s from a float number
# from https://stackoverflow.com/a/2440786/4292910
def float_format(val) -> str:
    return f'{val}'.rstrip('0').rstrip('.')