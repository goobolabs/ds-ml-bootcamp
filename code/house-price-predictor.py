# ===============================
# House Price Prediction (Clean)
# - Linear Regression & Random Forest
# - Uses cleaned dataset with engineered features
# - Clear comments at every step
# ===============================

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# --------------------------------
# 1) Load the cleaned dataset
# --------------------------------
CSV_PATH = "dataset/clean_house_l5_dataset.csv"
df = pd.read_csv(CSV_PATH)

# --------------------------------
# 2) Split features (X) and target (y)
# --------------------------------
# We predict "Price". We also drop "LogPrice" from X so we don't leak target info.
X = df.drop(columns=["Price", "LogPrice"])
y = df["Price"]

# --------------------------------
# 3) Train/test split for fair evaluation
# --------------------------------
# Keep 20% of data for testing generalization. random_state for reproducibility.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --------------------------------
# 4) Train Linear Regression
# --------------------------------
# Linear model is simple and interpretable; good baseline.
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)

# --------------------------------
# 5) Train Random Forest
# --------------------------------
# Ensemble model captures non-linear relationships; often stronger than linear.
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)

# --------------------------------
# 6) Helper to print metrics nicely
# --------------------------------
def print_metrics(name, y_true, y_pred):
    """Print R², MAE, MSE, RMSE for a model's predictions."""
    r2  = r2_score(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    print(f"\n{name} Performance:")
    print(f"  R²   : {r2:.3f}")          # higher is better (max = 1.0)
    print(f"  MAE  : {mae:,.0f}")        # lower is better (absolute error)
    print(f"  MSE  : {mse:,.0f}")        # lower is better (squared error)
    print(f"  RMSE : {rmse:,.0f}")       # lower is better (same units as Price)

# --------------------------------
# 7) Show results for both models
# --------------------------------
print_metrics("Linear Regression", y_test, lr_pred)
print_metrics("Random Forest",   y_test, rf_pred)

# --------------------------------
# 8) Single-row prediction (sanity check)
# --------------------------------
# Pick one unseen row from X_test and predict both models.
# Use iloc[[i]] (double brackets) to keep it as a DataFrame with column names
i = 3
x_one_df = X_test.iloc[[i]]   # 1-row DataFrame (keeps feature names)
y_true   = y_test.iloc[i]     # scalar

p_lr_one = float(lr.predict(x_one_df)[0])
p_rf_one = float(rf.predict(x_one_df)[0])

print("\nSingle-row sanity check:")
print(f"  Actual Price: ${y_true:,.0f}")
print(f"  LR Pred     : ${p_lr_one:,.0f}")
print(f"  RF Pred     : ${p_rf_one:,.0f}")