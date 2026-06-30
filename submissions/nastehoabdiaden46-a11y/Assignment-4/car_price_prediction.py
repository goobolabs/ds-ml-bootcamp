#part B practice
# Assignment Four: Car Price Prediction

# Step 1: Import libraries

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

# ==========================================
# Step 2: Load Dataset
# ==========================================

df = pd.read_csv("clean_car_dataset.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

# ==========================================
# Step 3: Prepare Features and Target
# ==========================================

# Target variable
y = df["Price"]

# Features
X = df.drop(["Price", "LogPrice"], axis=1)

# Convert categorical columns into numbers
X = pd.get_dummies(X, drop_first=True)

print("\nFeatures Shape:")
print(X.shape)

# ==========================================
# Step 4: Split Dataset
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Shape:", X_train.shape)
print("Testing Shape:", X_test.shape)

# ==========================================
# Step 5: Train Models
# ==========================================

# Linear Regression

linear_model = LinearRegression()

linear_model.fit(
    X_train,
    y_train
)

# Random Forest

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(
    X_train,
    y_train
)

# ==========================================
# Step 6: Evaluation Function
# ==========================================

def evaluate_model(model, X_test, y_test):

    predictions = model.predict(X_test)

    r2 = r2_score(
        y_test,
        predictions
    )

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    mse = mean_squared_error(
        y_test,
        predictions
    )

    rmse = np.sqrt(mse)

    print(f"R²   : {r2:.2f}")
    print(f"MAE  : {mae:.2f}")
    print(f"MSE  : {mse:.2f}")
    print(f"RMSE : {rmse:.2f}")

# ==========================================
# Step 7: Evaluate Linear Regression
# ==========================================

print("\nLinear Regression Performance:")

evaluate_model(
    linear_model,
    X_test,
    y_test
)

# ==========================================
# Step 8: Evaluate Random Forest
# ==========================================

print("\nRandom Forest Performance:")

evaluate_model(
    rf_model,
    X_test,
    y_test
)

# ==========================================
# Step 9: Sanity Check
# ==========================================

sample = X_test.iloc[[0]]

actual_price = y_test.iloc[0]

linear_prediction = linear_model.predict(sample)

rf_prediction = rf_model.predict(sample)

print("\nSanity Check")

print("Actual Price:")
print(actual_price)

print("\nLinear Regression Prediction:")
print(linear_prediction[0])

print("\nRandom Forest Prediction:")
print(rf_prediction[0])
