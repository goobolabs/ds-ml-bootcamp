import os
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

# ==========================
# Read CSV file
# ==========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "car_clean_dataset.csv")

df = pd.read_csv(CSV_PATH)

# ==========================
# Split features and target
# ==========================
X = df.drop(columns=["Price", "Log_Price"])
y = df["Price"]

# ==========================
# Train/Test Split
# ==========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ==========================
# Linear Regression
# ==========================
lr = LinearRegression()

lr.fit(X_train, y_train)

lr_predict = lr.predict(X_test)

print("=" * 45)
print("Linear Regression Predictions")
print("=" * 45)
print(lr_predict)

# ==========================
# Random Forest Regression
# ==========================
rfr = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rfr.fit(X_train, y_train)

rfr_predict = rfr.predict(X_test)

print("=" * 45)
print("Random Forest Predictions")
print("=" * 45)
print(rfr_predict)

# ==========================
# Evaluation Function
# ==========================
def logRegressionMetrics(model_name, y_true, y_pred):

    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)

    print("\n" + "=" * 45)
    print(f"{model_name} Performance")
    print("=" * 45)
    print(f"Mean Absolute Error : {mae:,.4f}")
    print(f"Mean Squared Error  : {mse:,.4f}")
    print(f"Root MSE            : {rmse:,.4f}")
    print(f"R² Score            : {r2:.4f} ({r2*100:.2f}%)")

# Evaluate models
logRegressionMetrics("Linear Regression", y_test, lr_predict)
logRegressionMetrics("Random Forest", y_test, rfr_predict)

# ==========================
# Feature Scaling
# ==========================
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

X_train_scaled_df = pd.DataFrame(
    X_train_scaled,
    columns=X_train.columns
)

print("\n" + "=" * 45)
print("First 5 Rows of Scaled Data")
print("=" * 45)
print(X_train_scaled_df.head())

print("\n" + "=" * 45)
print("Scaler Parameters")
print("=" * 45)

for feature, mean, std in zip(
    X_train.columns,
    scaler.mean_,
    scaler.scale_,
):
    print(
        f"{feature:<20} Mean: {mean:.4f}   Std Dev: {std:.4f}"
    )

# ==========================
# Training/Test Scores
# ==========================
print("\n" + "=" * 45)
print("Linear Regression Scores")
print("=" * 45)

lr_train_score = lr.score(X_train, y_train)
lr_test_score = lr.score(X_test, y_test)

print(f"Train Score : {lr_train_score:.4f}")
print(f"Test Score  : {lr_test_score:.4f}")

print("\n" + "=" * 45)
print("Random Forest Scores")
print("=" * 45)

rfr_train_score = rfr.score(X_train, y_train)
rfr_test_score = rfr.score(X_test, y_test)

print(f"Train Score : {rfr_train_score:.4f}")
print(f"Test Score  : {rfr_test_score:.4f}")

# ==========================
# Predict One Sample
# ==========================
i = 5

X_one = X_test.iloc[[i]]
y_true = y_test.iloc[i]

lr_one = lr.predict(X_one)[0]
rfr_one = rfr.predict(X_one)[0]

print("\n" + "=" * 45)
print("Single Row Prediction")
print("=" * 45)

print(f"Actual Price              : {y_true:,.0f}")
print(f"Linear Regression Predict : {lr_one:,.0f}")
print(f"Random Forest Predict     : {rfr_one:,.0f}")