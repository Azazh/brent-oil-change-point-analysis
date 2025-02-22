import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from arch import arch_model

def fit_arima(data):
    model = ARIMA(data, order=(5, 1, 0))  # Example order (p, d, q)
    results = model.fit()
    return results

def fit_garch(data):
    model = arch_model(data, vol='Garch', p=1, q=1)
    results = model.fit()
    return results

# Example usage
if __name__ == "__main__":
    data = pd.read_csv('../data/processed_brent_oil_prices.csv', parse_dates=['Date'], index_col='Date')
    arima_results = fit_arima(data['Price'])
    garch_results = fit_garch(data['Price'])