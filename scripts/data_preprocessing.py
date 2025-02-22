import pandas as pd

def preprocess_data(filepath):
    # Load data
    data = pd.read_csv(filepath, parse_dates=['Date'], index_col='Date')
    
    # Handle missing values
    data.fillna(method='ffill', inplace=True)  # Forward fill missing values
    
    # Convert data types if necessary
    data['Price'] = data['Price'].astype(float)
    
    return data

# Example usage
if __name__ == "__main__":
    data = preprocess_data('../data/brent_oil_prices.csv')
    data.to_csv('../data/processed_brent_oil_prices.csv')