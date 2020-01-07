import yfinance as yf
import pandas as pd
import datetime as dt
import os

# Get a list of all of the major companies
company_data = pd.read_excel('yahoo_ticker_symbols.xlsx')
codes = company_data['Yahoo Stock Tickers'].iloc[3:]

# Get todays date
today_string = str(dt.datetime.today().date())

# Create 'data' folder if it dosent exist
if not os.path.exists('data'):
    os.mkdir('data')

# Download all data from the year 2000 to now for the first 100 codes
for code in codes[0:100]:
    data = yf.download("{}".format(code), start="2000-01-01", end=today_string)
    data.to_csv('data/{}.csv'.format(code))
