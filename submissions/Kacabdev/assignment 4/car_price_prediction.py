import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error



# 1. Load Dataset
df = pd.read_csv("car_l3_clean_ready.csv")
print("Dataset shape:", df.shape)
print(df.head())
print()



# 2. Prepare Features & Target
# Target (y) = Price
# Features (X) = everything except Price and LogPrice
# (LogPrice is dropped too since it's just a transformed copy of the
# target and would leak information into the model)
y = df["Price"]
X = df.drop(columns=["Price", "LogPrice"])
print("Features used:", list(X.columns))
print()



# 3. Split Data (80% train / 20% test, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print("Training set size:", X_train.shape)
print("Testing set size :", X_test.shape)
print()



# 4. Train Models
lr = LinearRegression()
lr.fit(X_train, y_train)

rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

print("Both models trained.")
print()


# 5. Evaluate Performance
def evaluate_model(name, model, X_test, y_test):
    """Print R², MAE, MSE, and RMSE for a given fitted model."""
    preds = model.predict(X_test)
    r2 = r2_score(y_test, preds)
    mae = mean_absolute_error(y_test, preds)
    mse = mean_squared_error(y_test, preds)
    rmse = np.sqrt(mse)

    print(f"{name} Performance:")
    print(f"  R²   : {r2:.2f}")
    print(f"  MAE  : {mae:,.2f}")
    print(f"  MSE  : {mse:,.2f}")
    print(f"  RMSE : {rmse:,.2f}")
    print()
    return r2, mae, mse, rmse


lr_metrics = evaluate_model("Linear Regression", lr, X_test, y_test)
rf_metrics = evaluate_model("Random Forest", rf, X_test, y_test)



# 6. Sanity Check
# Pick one row from the test set and compare the actual price with
# what each model predicted.
i = 0
row = X_test.iloc[[i]]
actual = y_test.iloc[i]
pred_lr = lr.predict(row)[0]
pred_rf = rf.predict(row)[0]

print("Sanity check — row index in original dataset:", X_test.index[i])
print(row)
print()
print(f"Actual price          : {actual:,.2f}")
print(f"Linear Reg predicts    : {pred_lr:,.2f}")
print(f"Random Forest predicts : {pred_rf:,.2f}")