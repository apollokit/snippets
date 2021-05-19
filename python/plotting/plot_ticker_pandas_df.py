# output example: plt_hz100d_AAPL.png

def plot_ticker_mvg(data: AssetsData, ticker: str, 
        output_dir = 'output',
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
        show_plot = True,
        fig_size = (15, 9),
        prefix = 'plt_'):
    """[summary]
    
    [description]
    
    Args:
        data: [description]
        ticker: [description]
        start: the start time for plotting the data
        end: the end time for plotting the data
        show_plot: whether or not to show plots at termination time
        fig_size:  output plot figure size
    """

    ticker_data = data.get_ticker_data(ticker)
    signals = dual_moving_average(ticker_data)
    pcnt_returns = percent_return_df(ticker_data)

    start_loc = 0
    end_loc = len(ticker_data)
    if start:
        query_date = ticker_data.index[-1]
        for dt in reversed(ticker_data.index):
            if dt <= start:
                query_date = dt
                break
        start_loc = ticker_data.index.get_loc(query_date)
    if end:
        query_date = ticker_data.index[-1]
        for dt in reversed(ticker_data.index):
            if dt <= end:
                query_date = dt
                break
        end_loc = ticker_data.index.get_loc(query_date)

    ticker_data = ticker_data[start_loc:end_loc+1]
    signals = signals[start_loc:end_loc+1]
    pcnt_returns = pcnt_returns[start_loc:end_loc+1]


    # Create a figure
    fig = plt.figure(figsize=fig_size)

    ax1 = fig.add_subplot(211, ylabel='Price $')
    ax2 = fig.add_subplot(212, ylabel='Day to day percent return (%)')

    ax1.set_title(f'Ticker: {ticker}')

    # Plot the equity curve in dollars
    ticker_data['Adj Close'].plot(ax=ax1, grid=True, label='adj close', marker='o')
    pcnt_returns['Adj Close'].plot(ax=ax2, grid=True, label='d2d pcnt', color='m', marker='^', linestyle=':')
    
    signals['short_mavg'].plot(ax=ax1, grid=True, label='short')
    signals['long_mavg'].plot(ax=ax1, grid=True, label='long')

    line_labels = [l.get_label() for l in ax1.lines]
    ax1.legend(ax1.lines, line_labels, ncol=4, loc='upper right')
    
    line_labels = [l.get_label() for l in ax2.lines]
    ax2.legend(ax2.lines, line_labels, ncol=4, loc='upper right')
    
    if show_plot:
        plt.show()
    else:
        plt.savefig(path.join(output_dir, prefix + ticker))
