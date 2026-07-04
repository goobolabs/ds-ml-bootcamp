import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

# ==========================================================
# Load dataset
# ==========================================================
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "Cleaned_Loan_Dataset.csv"  # make sure file name is correct!

df = pd.read_csv(CSV_PATH)

print(df.head())
print(df.info())

# ==========================================================
# Train/test split
# ==========================================================
X = df.drop(columns=["Approved"])
y = df["Approved"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

print("Training samples:", len(X_train))
print("Testing samples :", len(X_test))

# ==========================================================
# SCALE DATA (FIX FOR LOGISTIC REGRESSION)
# ==========================================================
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ==========================================================
# Train models
# ==========================================================
logistic = LogisticRegression(max_iter=2000, random_state=42)
random_forest = RandomForestClassifier(n_estimators=100, random_state=42)
decision_tree = DecisionTreeClassifier(random_state=42)

logistic.fit(X_train_scaled, y_train)
random_forest.fit(X_train, y_train)
decision_tree.fit(X_train, y_train)

print("Models trained successfully.")

# ==========================================================
# Metrics functions
# ==========================================================
def print_metrics(name, y_true, y_pred):
    print(f"\n{name} Performance:")
    print(f"  Accuracy : {accuracy_score(y_true, y_pred):.3f}")
    print(f"  Precision: {precision_score(y_true, y_pred, zero_division=0):.3f}")
    print(f"  Recall   : {recall_score(y_true, y_pred, zero_division=0):.3f}")
    print(f"  F1-Score : {f1_score(y_true, y_pred, zero_division=0):.3f}")


def print_confusion(name, y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    cm_df = pd.DataFrame(
        cm,
        index=["Actual Rejected", "Actual Approved"],
        columns=["Predicted Rejected", "Predicted Approved"]
    )
    print(f"\n{name} Confusion Matrix")
    print(cm_df)

# ==========================================================
# Evaluate models
# ==========================================================
results = []

# Logistic Regression (SCALED)
log_pred = logistic.predict(X_test_scaled)
print_metrics("Logistic Regression", y_test, log_pred)
print_confusion("Logistic Regression", y_test, log_pred)

results.append({
    "Model": "Logistic Regression",
    "Accuracy": accuracy_score(y_test, log_pred),
    "Precision": precision_score(y_test, log_pred, zero_division=0),
    "Recall": recall_score(y_test, log_pred, zero_division=0),
    "F1 Score": f1_score(y_test, log_pred, zero_division=0)
})

# Random Forest
rf_pred = random_forest.predict(X_test)
print_metrics("Random Forest", y_test, rf_pred)
print_confusion("Random Forest", y_test, rf_pred)

results.append({
    "Model": "Random Forest",
    "Accuracy": accuracy_score(y_test, rf_pred),
    "Precision": precision_score(y_test, rf_pred, zero_division=0),
    "Recall": recall_score(y_test, rf_pred, zero_division=0),
    "F1 Score": f1_score(y_test, rf_pred, zero_division=0)
})

# Decision Tree
dt_pred = decision_tree.predict(X_test)
print_metrics("Decision Tree", y_test, dt_pred)
print_confusion("Decision Tree", y_test, dt_pred)

results.append({
    "Model": "Decision Tree",
    "Accuracy": accuracy_score(y_test, dt_pred),
    "Precision": precision_score(y_test, dt_pred, zero_division=0),
    "Recall": recall_score(y_test, dt_pred, zero_division=0),
    "F1 Score": f1_score(y_test, dt_pred, zero_division=0)
})

# ==========================================================
# Comparison table
# ==========================================================
comparison = pd.DataFrame(results)
print("\nModel Comparison")
print(comparison)

# ==========================================================
# Sample prediction
# ==========================================================
i = 2
sample = X_test.iloc[[i]]
sample_scaled = X_test_scaled[i].reshape(1, -1)
actual = y_test.iloc[i]

print("\nActual:", actual)
print("Logistic Regression:", logistic.predict(sample_scaled)[0])
print("Random Forest:", random_forest.predict(sample)[0])
print("Decision Tree:", decision_tree.predict(sample)[0])