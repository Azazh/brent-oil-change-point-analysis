from flask import Flask, jsonify
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

# Get the absolute path to the data file
current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of app.py
data_path = os.path.join(current_dir, '..', 'data', 'processed_brent_oil_prices.csv')  # Navigate to the data folder

# Load processed data
data = pd.read_csv(data_path, parse_dates=['Date'], index_col='Date')

@app.route('/api/prices', methods=['GET'])
def get_prices():
    # Convert the index (Timestamp) to strings and create a dictionary
    prices_dict = {str(date): price for date, price in data['Price'].items()}
    return jsonify(prices_dict)

if __name__ == "__main__":
    app.run(debug=True)