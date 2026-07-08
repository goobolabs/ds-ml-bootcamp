# ===============================
# Loan Approval Classification (Clean)
# - Logistic Regression & Random Forest & KNeighborsClassifier
# - Uses cleaned loan dataset with engineered features
# - Clear comments at every step
# ===============================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

CSV_PATH = "dataset/clean_loan_dataset.csv"
df = pd.read_csv(CSV_PATH)
df.head()

# Prepare Features & Target
y = df["Approved"]
X = df.drop(columns=["Approved"])   

print("Features:", list(X.columns))
print("Target: Approved")
print("X shape:", X.shape, "| y shape:", y.shape)

# Split Data
#--------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)   
print("Train shape:", X_train.shape)
print("Test shape :", X_test.shape)
# Train Models 
#--------------------------------
# Logistic Regression
log_reg = LogisticRegression(max_iter=1000, random_state=42)
log_reg.fit(X_train, y_train)

# Random Forest Classifier
rf = RandomForestClassifier(n_estimators=1000, random_state=42)
rf.fit(X_train, y_train)  
print("Models Random Forest & Logistic Regression trained successfully!")  

# K-Nearest Neighbors
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
print("Models Knearest neighbors trained successfully!")  

# Evaluate Performance
#--------------------------------

def evaluate_model(name, model, X_test, y_test):
    """Print Accuracy, Precision, Recall, F1-Score (positive class = Approved = 1)
    and the confusion matrix for a fitted classifier."""
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, pos_label=1)
    rec = recall_score(y_test, y_pred, pos_label=1)
    f1 = f1_score(y_test, y_pred, pos_label=1)

    print(f"{name} Performance:")
    print(f"  Accuracy : {acc:.3f}")
    print(f"  Precision: {prec:.3f}  (positive = Approved=1)")
    print(f"  Recall   : {rec:.3f}  (positive = Approved=1)")
    print(f"  F1-Score : {f1:.3f}  (positive = Approved=1)")
    print()

  

    return y_pred

log_reg_preds = evaluate_model("Logistic Regression", log_reg, X_test, y_test)
rand_forest_preds = evaluate_model("Random Forest", rf, X_test, y_test)
knn_preds = evaluate_model("K-Nearest Neighbors", knn, X_test, y_test)

# Sanity Check
#--------------------------------

i = 3

sample = X_test.iloc[[i]]

print("Sample features:")

print(sample)

print("\nActual label            :", y_test.iloc[i])
print("Logistic Regression pred:", log_reg.predict(sample)[0])
print("Random Forest pred      :", rf.predict(sample)[0])
print("KNN pred                :", knn.predict(sample)[0])