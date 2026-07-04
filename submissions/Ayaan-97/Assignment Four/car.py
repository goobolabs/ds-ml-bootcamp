# Import libraries:
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# 1. Load Dataset
df = pd.read_csv('dataset/car-clean-dataset.csv')

# Quick look to ensure everything loaded correctly
print("Dataset Shape:", df.shape)
df.head(5)

# 2. Prepare Features & Target
#--------------------------------
X = df.drop(columns=['Price', 'LogPrice'], errors='ignore')
y = df['Price']

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


print(f"Train shape: {X_train.shape}, Test shape: {X_test.shape}")

# 4. Train Models
# Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)

# Random Forest Regression
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)

print("Models trained successfully!")

# 5. Evaluate Performance
def evaluate_model(model, X_test, y_test, model_name):
    predictions = model.predict(X_test)
    
    # Calculate metrics
    r2 = r2_score(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    
    # Print formatted output
    # print(f"{model_name} Performance:")
    print(f"  R²   : {r2:.2f}")
    print(f"  MAE  : {mae:,.0f}")
    print(f"  MSE  : {mse:,.0f}")
    print(f"  RMSE : {rmse:,.0f}")
    print("-" * 30)

# Call the helper function for both models
evaluate_model(lr_model, X_test, y_test, "Linear Regression")
evaluate_model(rf_model, X_test, y_test, "Random Forest")
