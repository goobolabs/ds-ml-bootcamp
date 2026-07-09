# ==========================================
# Loan Approval Prediction
# ==========================================

import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("clean_loan_dataset.csv")

print("Dataset Loaded Successfully\n")
print(df.head())

# ==========================================
# Prepare Features and Target
# ==========================================

X = df.drop("Approved", axis=1)
y = df["Approved"]

# ==========================================
# Split Dataset
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    stratify=y,
    random_state=42,
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples :", len(X_test))

# ==========================================
# Train Models
# ==========================================

# Logistic Regression
log_model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

log_model.fit(X_train, y_train)

# Random Forest
rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

# ==========================================
# Third Classifier (Decision Tree)
# ==========================================

dt_model = DecisionTreeClassifier(
    random_state=42
)

dt_model.fit(X_train, y_train)

# ==========================================
# Evaluation Function
# ==========================================

def evaluate_model(name, model):

    prediction = model.predict(X_test)

    print(f"\n{name} Performance")
    print("-" * 35)

    print(f"Accuracy : {accuracy_score(y_test, prediction):.3f}")
    print(f"Precision: {precision_score(y_test, prediction):.3f}")
    print(f"Recall   : {recall_score(y_test, prediction):.3f}")
    print(f"F1-Score : {f1_score(y_test, prediction):.3f}")

    print("\nConfusion Matrix")
    print(confusion_matrix(y_test, prediction))


# ==========================================
# Evaluate Models
# ==========================================

evaluate_model("Logistic Regression", log_model)

evaluate_model("Random Forest", rf_model)

evaluate_model("Decision Tree", dt_model)

# ==========================================
# Sanity Check
# ==========================================

print("\n==============================")
print("Sanity Check")
print("==============================")

i = 0

sample = X_test.iloc[[i]]

actual = y_test.iloc[i]

log_prediction = log_model.predict(sample)[0]
rf_prediction = rf_model.predict(sample)[0]
dt_prediction = dt_model.predict(sample)[0]

print("Actual Label                :", actual)
print("Logistic Regression Predict :", log_prediction)
print("Random Forest Predict       :", rf_prediction)
print("Decision Tree Predict       :", dt_prediction)