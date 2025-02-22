import pandas as pd
import yfinance as yf

# Fetch Brent oil prices
brent_prices = yf.download('BZ=F', start='1987-05-20', end='2022-09-30')
brent_prices.to_csv('../data/brent_oil_prices.csv')

# Fetch additional data (e.g., GDP, inflation rates)
# Example: Fetch US GDP data from FRED
# Note: You may need an API key for FRED or other sources.