# Import libraries:
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def print_metrics(model_name, y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    print(f"{model_name} -> MAE: {mae:,.2f}, RMSE: {rmse:,.2f}, R2: {r2:.4f}")

# Load dataset
CSV_PATH = "clean_house_l5_dataset (2).csv"
df = pd.read_csv(CSV_PATH)

print("Dataset Shape:", df.shape)
df.head(5)

df = df.dropna().reset_index(drop=True)

df['Price'] = pd.to_numeric(
    df['Price'].astype(str).str.replace('$', '', regex=False).str.replace(',', '', regex=False)
)

# Prepare features and target
X = pd.get_dummies(df.drop(columns=['Price']), drop_first=True)
y = df['Price']

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


print(f"Train shape: {X_train.shape}, Test shape: {X_test.shape}")

# Train Linear Regression Model
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)

# Train Random Forest
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)

# Evaluate both models
print_metrics("Linear Regression", y_test, lr_pred)
print_metrics("Random Forest", y_test, rf_pred)

# Single-row Sanity Check
i = 2
x_one = X_test.iloc[[i]]
y_true = y_test.iloc[i]

p_lr = float(lr.predict(x_one)[0])
p_rf = float(rf.predict(x_one)[0])

print("\nSingle-row Sanity Check:")
print(f"  Actual Price: ${y_true:,.0f}")
print(f"  LR Pred     : ${p_lr:,.0f}")
print(f"  RF Pred     : ${p_rf:,.0f}")