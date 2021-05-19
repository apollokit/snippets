import matplotlib.pyplot as plt

ax1 = plt.gca()
ax2 = plt.twinx()

# plot stuff
ticker_hist['Adj Close'].plot(ax=ax1, grid=True, label='price')
aves['short_mavg'].plot(ax=ax1, grid=True, label='short')
aves['long_mavg'].plot(ax=ax1, grid=True, label='long')

portfolio_value_history['total'].plot(ax=ax2, grid=False, label='portfolio total', color='r')

# add legend and labels
ax1.set_ylabel('Asset price')
ax2.set_ylabel('Portfolio total value')
plt.title(f'MomentumDayTrader, ticker: {self.ticker}')

line_labels = [l.get_label() for l in ax1.lines + ax2.lines]
plt.legend(ax1.lines + ax2.lines, line_labels,
           ncol=4, loc='upper right')

plt.show()