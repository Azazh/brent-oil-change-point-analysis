from sklearn.metrics import mean_squared_error, mean_absolute_error

def evaluate_model(actual, predicted):
    mse = mean_squared_error(actual, predicted)
    mae = mean_absolute_error(actual, predicted)
    return mse, mae

# Example usage
if __name__ == "__main__":
    actual = [1, 2, 3, 4, 5]
    predicted = [1.1, 2.1, 3.1, 4.1, 5.1]
    mse, mae = evaluate_model(actual, predicted)
    print(f'MSE: {mse}, MAE: {mae}')