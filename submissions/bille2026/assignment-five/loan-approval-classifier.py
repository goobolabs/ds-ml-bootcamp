# ===============================
# Loan Approval Classification (Clean)
# - Logistic Regression, Decision tree & Random Forest
# - Uses cleaned loan dataset with engineered features
# - Clear comments at every step
# ===============================

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

# --------------------------------
# 1) Load the cleaned dataset
# --------------------------------
CSV_PATH = "./clean_loan_dataset.csv"
df = pd.read_csv(CSV_PATH)

# --------------------------------
# 2) Split features (X) and target (y)
# --------------------------------
# Features = applicant info; label = Approved (1) or Rejected (0)
X = df.drop(columns=["Approved"])
y = df["Approved"]

# --------------------------------
# 3) Train/test split (stratified)
# L2: stratify keeps class ratio in both sets — important for classification
# --------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
# print("=== SPLIT SIZES ===")
# print(f"Train: {X_train.shape[0]}  |  Test: {X_test.shape[0]}")

# --------------------------------
# 4) Train classifiers
# --------------------------------
log_reg = LogisticRegression(max_iter=1000, random_state=42)
rf = RandomForestClassifier(n_estimators=1000, random_state=42)
dt = DecisionTreeClassifier(random_state=42)

dt.fit(X_train, y_train)
log_reg.fit(X_train, y_train)
rf.fit(X_train, y_train)


# 5) Helper functions: metrics + confusion matrix
# --------------------------------
def print_clf_metrics(name, y_true, y_pred, pos_label=1):
    """Print Accuracy, Precision, Recall, F1. pos_label=1 means Approved is positive."""
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, pos_label=pos_label)
    rec = recall_score(y_true, y_pred, pos_label=pos_label)
    f1 = f1_score(y_true, y_pred, pos_label=pos_label)
    print(f"\n{name} Performance:")
    print(f"  Accuracy : {acc:.3f}")
    print(f"  Precision: {prec:.3f}  (positive = Approved=1)")
    print(f"  Recall   : {rec:.3f}  (positive = Approved=1)")
    print(f"  F1-Score : {f1:.3f}  (positive = Approved=1)")


    
# 6) Show results for both models
# --------------------------------
dt_preds = dt.predict(X_test)
print_clf_metrics("Decision Tree", y_test, dt_preds, pos_label=1)


log_reg_preds = log_reg.predict(X_test)
print_clf_metrics("Logistic Regression", y_test, log_reg_preds, pos_label=1)


rf_preds = rf.predict(X_test)
print_clf_metrics("Random Forest", y_test, rf_preds, pos_label=1)


def print_confmat(name, y_true, y_pred):
    """
    Confusion matrix with readable labels.
    Rows = Actual, Cols = Predicted
    Order: [Approved(1), Rejected(0)]
    """
    cm = confusion_matrix(y_true, y_pred, labels=[1, 0])
    cm_df = pd.DataFrame(
        cm,
        index=["Actual: Approved (1)", "Actual: Rejected (0)"],
        columns=["Pred: Approved (1)", "Pred: Rejected (0)"],
    )
    print(f"\n{name} – Confusion Matrix:\n{cm_df}")


def label_str(v):
     return "Approved (1)" if v == 1 else "Rejected (0)"


print_confmat("Decision Tree", y_test, dt_preds)

print_confmat("Logistic Regression", y_test, log_reg_preds)
print_confmat("Random Forest", y_test, rf_preds)

# --------------------------------
# 7) Single-row sanity check
# --------------------------------
i = 0
x_one_df = X_test.iloc[[i]]
y_true = y_test.iloc[i]

print("\n=== SINGLE APPLICATION CHECK ===")
print(f"  Actual label          : {label_str(y_true)}")
print(f"  Decision Tree         : {label_str(int(dt.predict(x_one_df)[0]))}")
print(f"  Logistic Regression   : {label_str(int(log_reg.predict(x_one_df)[0]))}")
print(f"  Random Forest         : {label_str(int(rf.predict(x_one_df)[0]))}")