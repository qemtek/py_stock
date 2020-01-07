import plotly.express as px
import yfinance as yf
import pandas as pd

stocks = yf.Tickers('msft aapl goog')
print(stocks)

# Get stock info
info = {}
info['MSFT'] = stocks.tickers.MSFT.info
info['AAPL'] = stocks.tickers.aapl.info
info['GOOG'] = stocks.tickers.goog.info

# Create a dictionary to store historical data
hist = {}
hist['MSFT'] = stocks.tickers.MSFT.history(period="max").reset_index()
hist['MSFT']['Company'] = 'Microsoft'
hist['AAPL'] = stocks.tickers.AAPL.history(period="max").reset_index()
hist['AAPL']['Company'] = 'Apple'
hist['GOOG'] = stocks.tickers.GOOG.history(period="max").reset_index()
hist['GOOG']['Company'] = 'Google'

# Plot microsoft
fig = px.line(hist['MSFT'], x='Date', y='Close')
fig.show()

# Create a dataframe containing all companies and plot together
hist_large = pd.concat([hist['MSFT'], hist['AAPL'], hist['GOOG']], axis=0)
fig = px.line(hist_large, x='Date', y='Close', color='Company')
fig.show()
