#  see http://cis.bentley.edu/sandbox/wp-content/uploads/Documentation-on-f-strings.pdf

yo = 0.323432
# print as float with two decimal places
print(f'hey yo: {yo:0.2f}')




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