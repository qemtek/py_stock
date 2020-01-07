import yfinance as yf

msft = yf.Ticker("MSFT")
print(msft)

# Get stock info
info = msft.info

# Get historical market data, here max is 5 years.
historical = msft.history(period="max")

# show actions (dividends, splits)
actions = msft.actions

# show dividends
dividends = msft.dividends

# show splits
splits = msft.splits

# show financials
financials = msft.financials
q_financials = msft.quarterly_financials

# show major holders
major_holders = msft.major_holders

# show institutional holders
inst_holders = msft.institutional_holders

# show balance sheet
balance_sheet = msft.balance_sheet
q_balance_sheet = msft.quarterly_balance_sheet

# show cashflow
cashflow = msft.cashflow
q_cashflow = msft.quarterly_cashflow

# show earnings
earnings = msft.earnings
q_earnings = msft.quarterly_earnings

# show sustainability
sus = msft.sustainability

# show analysts recommendations
rec = msft.recommendations

# show next event (earnings, etc)
cal = msft.calendar

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
isin = msft.isin

# show options expirations
opt_exp = msft.options

# get option chain for specific expiration
opt = msft.option_chain('2020-01-10')
# data available via: opt.calls, opt.puts
