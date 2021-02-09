stocks = pd.read_csv('data/stock_price.csv', parse_dates=['Date'], index_col='Date')
display(stocks.head())

# Investigate missing values - pct of nulls in the Price column

print(f'Percentage of missing values in Price is {stocks.isnull().mean()}\n')

# percentage of nulls by weekday

print('Percentage of missing values by weekday:')
display(
    stocks
    .assign(Weekday = stocks.index.weekday)
    .groupby('Weekday')
    .agg(lambda x: x.isnull().sum()/len(x))
)

# fill na using the fill previous method

print('Filled NA using ffill method:')
display(stocks.fillna(method='ffill'))


ax = (
    stocks
    .fillna(method='ffill')
    .assign(
        rolling_mean_center=lambda df: df['Price'].rolling(20, center=True).mean()
    )
    .plot(figsize=(16,4))
)

ax.set_title('Rolling mean of Stock Prices');