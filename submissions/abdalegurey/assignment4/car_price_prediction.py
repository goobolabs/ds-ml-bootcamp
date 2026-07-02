import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# --------------------------------
# 1) Load the cleaned dataset
# --------------------------------
CSV_PATH = "./clean_car_dataset.csv"
df = pd.read_csv(CSV_PATH)

print("\n=== DATASET HEAD ===")
print(df.head(20))


# 2)Prepare Features & Target

X = df.drop(columns=["Price", "LogPrice"])

y = df["Price"]


# 3) Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


#  4)Train Models

lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)


rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)


# 5)Evaluate Performance

def print_metrics(name, y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)

    print(f"\n{name} Performance:")
    print(f"  R²   : {r2:.4f}")
    print(f"  MAE  : {mae:,.2f}")
    print(f"  MSE  : {mse:,.2f}")
    print(f"  RMSE : {rmse:,.2f}")





print_metrics("Linear Regression", y_test, lr_pred)
print_metrics("Random Forest", y_test, rf_pred)

# --------------------------------
# 7) Sanity Check
# --------------------------------

i = 0  # You can change this index

sample = X_test.iloc[[i]]

actual_price = y_test.iloc[i]

lr_prediction = lr.predict(sample)[0]
rf_prediction = rf.predict(sample)[0]

print("\n=== SANITY CHECK ===")
print(f"Actual Price              : {actual_price:,.2f}")
print(f"Linear Regression Predict : {lr_prediction:,.2f}")
print(f"Random Forest Predict     : {rf_prediction:,.2f}")
