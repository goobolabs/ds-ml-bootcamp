import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# ==========================================================
# Load the cleaned dataset
# ==========================================================
BASE_DIR = Path.cwd()
CSV_PATH = BASE_DIR / "Cleaned_Loan_Dataset.csv"

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
# Train the three models
# ==========================================================
logistic = LogisticRegression(max_iter=1000, random_state=42)
random_forest = RandomForestClassifier(n_estimators=100, random_state=42)
decision_tree = DecisionTreeClassifier(random_state=42)

logistic.fit(X_train, y_train)
random_forest.fit(X_train, y_train)
decision_tree.fit(X_train, y_train)

print("Models trained successfully.")

# ==========================================================
# Third Classifier: Decision Tree
#
# Why Decision Tree?
# Decision Trees are easy to interpret, handle nonlinear relationships,
# and work well for binary classification problems such as loan approval
# prediction.
#
# Research Source:
# https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
# ==========================================================

# ==========================================================
# Metric + confusion matrix helper functions
# ==========================================================
def print_metrics(name, y_true, y_pred):
    print(f"\n{name} Performance:")
    print(f"  Accuracy : {accuracy_score(y_true, y_pred):.3f}")
    print(f"  Precision: {precision_score(y_true, y_pred):.3f}  (positive = Approved=1)")
    print(f"  Recall   : {recall_score(y_true, y_pred):.3f}  (positive = Approved=1)")
    print(f"  F1-Score : {f1_score(y_true, y_pred):.3f}  (positive = Approved=1)")


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
# Evaluate all three models
# ==========================================================
models = {
    "Logistic Regression": logistic,
    "Random Forest": random_forest,
    "Decision Tree": decision_tree
}

results = []

for name, model in models.items():
    pred = model.predict(X_test)
    print_metrics(name, y_test, pred)
    print_confusion(name, y_test, pred)

    results.append({
        "Model": name,
        "Accuracy": accuracy_score(y_test, pred),
        "Precision": precision_score(y_test, pred),
        "Recall": recall_score(y_test, pred),
        "F1 Score": f1_score(y_test, pred)
    })

comparison = pd.DataFrame(results)

print("\nModel Comparison")
print(comparison)

# ==========================================================
# Sample prediction check
# ==========================================================
i = 2
sample = X_test.iloc[[i]]
actual = y_test.iloc[i]

print("Actual:", actual)
print("Logistic Regression:", logistic.predict(sample)[0])
print("Random Forest:", random_forest.predict(sample)[0])
print("Decision Tree:", decision_tree.predict(sample)[0])