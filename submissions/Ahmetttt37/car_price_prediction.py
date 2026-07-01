import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

# Load dataset
CSV_PATH = r"C:\Users\Ali Black\Desktop\bootcamb\ds-ml-bootcamp\submissions\Ahmetttt37\assigment4\clean_car_dataset.csv"

df = pd.read_csv(CSV_PATH)

# Prepare features and target
y = df["Price"]

# Remove Price and LogPrice (if LogPrice exists)
X = df.drop(columns=["Price", "LogPrice"], errors="ignore")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Linear Regression
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Train Random Forest
rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
rf_model.fit(X_train, y_train)

# Evaluation function
def evaluate_model(model, X_test, y_test, model_name):
    predictions = model.predict(X_test)

    r2 = r2_score(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)

    print(f"\n{model_name} Performance:")
    print(f"R²   : {r2:.4f}")
    print(f"MAE  : {mae:,.2f}")
    print(f"MSE  : {mse:,.2f}")
    print(f"RMSE : {rmse:,.2f}")

# Evaluate models
evaluate_model(
    linear_model,
    X_test,
    y_test,
    "Linear Regression"
)

evaluate_model(
    rf_model,
    X_test,
    y_test,
    "Random Forest"
)

# Sanity Check
i = 0

sample = X_test.iloc[[i]]

actual_price = y_test.iloc[i]

linear_prediction = linear_model.predict(sample)[0]
rf_prediction = rf_model.predict(sample)[0]

print("\nSanity Check")
print("Actual Price            :", actual_price)
print("Linear Regression Price :", linear_prediction)
print("Random Forest Price     :", rf_prediction)