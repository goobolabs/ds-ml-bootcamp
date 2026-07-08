import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
    )


# 1) data loading 
CSV_PATH = "./dataset/clean_loan_dataset.csv"

df = pd.read_csv(CSV_PATH)

df["PreviousDefaults"] = df["PreviousDefaults"].fillna(
    df["PreviousDefaults"].median()
)

print("\n=== DATASET HEAD ===")
print(df.head())

print("\n=== DATASET INFO ===")
print(df.info())

# 2) features and target

X = df.drop("Approved", axis=1)

y = df["Approved"]

print("\nFeature Shape:", X.shape)
print("Target Shape:", y.shape)


# 3) train test split

# 80%
# 20%

# stratify=y
#random_state=42


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    stratify=y,
    random_state=42
)

print("\nTrain Shape:", X_train.shape)
print("Test Shape :", X_test.shape)


# 4) logistic regression
log_model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

log_model.fit(X_train, y_train)

# 5) Random forest 
rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

# 6) Third classifier
dt_model = DecisionTreeClassifier(
    random_state=42
)

dt_model.fit(X_train, y_train)

# 7) Evaluation function


def evaluate_model(model, name):

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    precision = precision_score(y_test, y_pred)

    recall = recall_score(y_test, y_pred)

    f1 = f1_score(y_test, y_pred)

    cm = confusion_matrix(y_test, y_pred)

    print(f"\n{name} Performance")

    print("-" * 40)

    print(f"Accuracy : {accuracy:.3f}")

    print(f"Precision: {precision:.3f}")

    print(f"Recall   : {recall:.3f}")

    print(f"F1-Score : {f1:.3f}")

    print("\nConfusion Matrix")

    print(cm)

    return {
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1": f1
    }

# 8) evaluate all models

log_results = evaluate_model(
    log_model,
    "Logistic Regression"
)

rf_results = evaluate_model(
    rf_model,
    "Random Forest"
)

dt_results = evaluate_model(
    dt_model,
    "Decision Tree"
)


# 9) comparing models

results_df = pd.DataFrame({
    "Logistic Regression": log_results,
    "Random Forest": rf_results,
    "Decision Tree": dt_results
})

print("\n=== MODEL COMPARISON ===")
print(results_df.T)


# 10) Sanity check

sample = X_test.iloc[[0]]

actual = y_test.iloc[0]

print("\n=== SANITY CHECK ===")

print("Actual Label:", actual)

print(
    "Logistic Regression:",
    log_model.predict(sample)[0]
)

print(
    "Random Forest:",
    rf_model.predict(sample)[0]
)

print(
    "Decision Tree:",
    dt_model.predict(sample)[0]
)
