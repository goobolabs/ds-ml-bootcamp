import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import (accuracy_score, classification_report, confusion_matrix)


# Load Processed Data
CSV_PATH = r"C:\Users\Ali Black\Desktop\bootcamp1\ds-ml-bootcamp\submissions\Ahmetttt37\final project\processed_features.csv"
T_PATH = r"C:\Users\Ali Black\Desktop\bootcamp1\ds-ml-bootcamp\submissions\Ahmetttt37\final project\target.csv"
X = pd.read_csv(CSV_PATH)
y = pd.read_csv(T_PATH)
y = y["Response"]

# Train Test Split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Model 1 Logistic Regression

lr = LogisticRegression(max_iter=1000, random_state=42)
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)

# Model 2 Random Forest

rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)

# Model 3 XGBoost

xgb = XGBClassifier(n_estimators=200, learning_rate=0.05, max_depth=5, random_state=42, eval_metric="logloss") 
xgb.fit(X_train, y_train)
xgb_pred = xgb.predict(X_test)

# Evaluation Function

def evaluate_model(name, y_true, y_pred):
    print("\n====================")
    print(name)
    print("====================")

    print("Accuracy:", accuracy_score(y_true, y_pred))
    print(classification_report(y_true, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_true, y_pred))

evaluate_model("Logistic Regression", y_test, lr_pred)
evaluate_model("Random Forest", y_test, rf_pred)
evaluate_model("XGBoost", y_test, xgb_pred)

# ===============================
# Sanity Check (Single Customer Prediction)
# ===============================

print("\n====================")
print("Sanity Check")
print("====================")

# Take one customer from test data

sample_customer = X_test.iloc[[0]]
real_value = y_test.iloc[0]
# Predictions
lr_result = lr.predict(sample_customer)[0]
rf_result = rf.predict(sample_customer)[0]
xgb_result = xgb.predict(sample_customer)[0]

print("Real Response:", real_value)

print("Logistic Regression Prediction:", lr_result)
print("Random Forest Prediction:", rf_result)
print("XGBoost Prediction:", xgb_result)

# ===============================
# Save Models
# ===============================

import os

os.makedirs(
    "models",
    exist_ok=True
)


joblib.dump(
    lr,
    "models/logistic_regression.pkl"
)


joblib.dump(
    rf,
    "models/random_forest.pkl"
)


joblib.dump(
    xgb,
    "models/xgboost.pkl"
)


print("\nModels Saved Successfully!")