
# initially create dataframe with a single row
if df is None:
    dates = [timestamp]

    # create a dictionary of all the asset quantities (plus cash)
    # need to use lists the first time
    assets_row = {pos.ticker: [pos.quantity] for pos in portfolio.positions}
    assets_row['cash ($)'] = [portfolio.cash]

    df = pd.DataFrame(assets_row)
    df['timestamp_utc'] = pd.to_datetime(dates)
    df = df.set_index('timestamp_utc')

    return

# add a new row to the dataframe

# BIG FAT NOTE: this is a bad idea. It's super slow. In my own experience,
# it's much better to save individual columns off in separate lists, and then
# join them together into a single dataframe at the very end.

else:
    # create a dictionary of all the asset quantities (plus cash)
    # they have to be scalars, not lists this time
    assets_row = {pos.ticker: pos.quantity for pos in portfolio.positions}
    assets_row['cash ($)'] = portfolio.cash

    # add columns for any assets that currently aren't stored in the history
    existing_columns = [col_name for col_name in df.columns]
    for pos in portfolio.positions:
        if not pos.ticker in existing_columns:
            # default to NaN because we have no data for this asset up to now,
            # and new rows automatically get filled with Nan below
            df[pos.ticker] = np.nan

    # add a new row for the current timestamp with the new portfolio data
    df.loc[timestamp] = assets_row 