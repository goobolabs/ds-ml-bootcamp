import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (r2_score, mean_absolute_error, mean_squared_error)


# Load Dataset


CSV_PATH = r"C:\Users\Ali Black\Desktop\bootcamp1\ds-ml-bootcamp\submissions\Ahmetttt37\assigment4\clean_car_dataset.csv"

df = pd.read_csv(CSV_PATH)


# Prepare Features & Target


X = df.drop(columns=["Price", "LogPrice"], errors="ignore")
y = df["Price"]

# columns into numbers
X = pd.get_dummies(X, drop_first=True)

# Split Dataset


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)


# Train Linear Regression


linear_model = LinearRegression()
linear_model.fit(X_train, y_train)


# Train Random Forest


rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)


# Evaluation Function


def evaluate_model(model, X_test, y_test, model_name):

    predictions = model.predict(X_test)

    r2 = r2_score(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)

    print("\n" + "=" * 40)
    print(model_name)
    print("=" * 40)
    print(f"R²   : {r2:.4f}")
    print(f"MAE  : {mae:,.2f}")
    print(f"MSE  : {mse:,.2f}")
    print(f"RMSE : {rmse:,.2f}")


# Evaluate Models


evaluate_model(
    linear_model,
    X_test,
    y_test,
    "Linear Regression Performance"
)

evaluate_model(
    rf_model,
    X_test,
    y_test,
    "Random Forest Performance"
)

# Sanity Check

i = 0

sample = X_test.iloc[[i]]

actual_price = y_test.iloc[i]

linear_prediction = linear_model.predict(sample)[0]
rf_prediction = rf_model.predict(sample)[0]

print("\n" + "=" * 40)
print("Sanity Check")
print("=" * 40)

print(f"Actual Price             : {actual_price:,.2f}")
print(f"Linear Regression Price  : {linear_prediction:,.2f}")
print(f"Random Forest Price      : {rf_prediction:,.2f}")
