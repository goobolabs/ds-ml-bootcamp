
# Crop Recommendation Classification
# - Logistic Regression, Random Forest, & XGBoost
# - Uses cleaned crop dataset with engineered features
# - joblib save for the API (deployment only)
# ===============================================

import json
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)

RANDOM_STATE = 42

# --------------------------------
# 1) Load the cleaned dataset
# --------------------------------
CSV_PATH = "clean_crop_dataset.csv"
df = pd.read_csv(CSV_PATH)

# Soo rar Crop Mapping-kii aan ku samaynay processing-ka si aan u naqaano dalag kasta magiciisa
mapping_data = json.load(open("models/crop_mapping.json", "r"))
idx_to_crop = mapping_data["idx_to_crop"]

def label_str(v):
    """U beddel lambarka index-ka magaca rasmiga ah ee dalagga."""
    return idx_to_crop[str(v)]

# --------------------------------
# 2) Split features (X) and target (y)
# --------------------------------
X = df.drop(columns=["label"])
y = df["label"]

# --------------------------------
# 3) Train/test split (stratified)
# --------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y
)

print("=== SPLIT SIZES ===")
print(f"Train: {X_train.shape[0]}  |  Test: {X_test.shape[0]}")

# --------------------------------
# 4) Train classifiers (LR, RF, and XGBoost)
# --------------------------------
log_reg = LogisticRegression(max_iter=1000, random_state=RANDOM_STATE)
rf = RandomForestClassifier(n_estimators=100, random_state=RANDOM_STATE)
xgb = XGBClassifier(n_estimators=100, random_state=RANDOM_STATE, eval_metric='mlogloss')

print("\nModel-lada ayaa la tababarayaa...")
log_reg.fit(X_train, y_train)
rf.fit(X_train, y_train)
xgb.fit(X_train, y_train)
print("Tababarkii waa dhammaaday!")

# --------------------------------
# 5) Helper functions: metrics + confusion matrix
# --------------------------------
def print_clf_metrics(name, y_true, y_pred):
    """Print Accuracy, Precision, Recall, F1 for Multi-class."""
    acc = accuracy_score(y_true, y_pred)
    # Maadaama ay dalagyo badan yihiin (Multi-class), waxaan isticmaalaynaa average='macro'
    prec = precision_score(y_true, y_pred, average='macro', zero_division=0)
    rec = recall_score(y_true, y_pred, average='macro', zero_division=0)
    f1 = f1_score(y_true, y_pred, average='macro', zero_division=0)
    
    print(f"\n{name} Performance:")
    print(f"  Accuracy : {acc:.3f}")
    print(f"  Precision: {prec:.3f} (Macro Avg)")
    print(f"  Recall   : {rec:.3f} (Macro Avg)")
    print(f"  F1-Score : {f1:.3f} (Macro Avg)")


def print_confmat(name, y_true, y_pred):
    """Confusion matrix faahfaahsan."""
    cm = confusion_matrix(y_true, y_pred)
    unique_labels = sorted(y_true.unique())
    crop_names = [idx_to_crop[str(lbl)] for lbl in unique_labels]
    
    cm_df = pd.DataFrame(
        cm,
        index=[f"Actual: {c}" for c in crop_names],
        columns=[f"Pred: {c}" for c in crop_names]
    )
    print(f"\n{name} – Confusion Matrix (Top 5 rows/cols for preview):")
    print(cm_df.iloc[:5, :5])  # Waxaan u tusaynaa 5-ta hore si aanay shaashadu u buuxsamin

# --------------------------------
# 6) Show results for all three models
# --------------------------------
log_reg_preds = log_reg.predict(X_test)
print_clf_metrics("Logistic Regression", y_test, log_reg_preds)

rf_preds = rf.predict(X_test)
print_clf_metrics("Random Forest", y_test, rf_preds)
print_confmat("Random Forest", y_test, rf_preds)

xgb_preds = xgb.predict(X_test)
print_clf_metrics("XGBoost", y_test, xgb_preds)
print_confmat("XGBoost", y_test, xgb_preds)

# --------------------------------
# 7) Single-row sanity check
# --------------------------------
i = 7
x_one_df = X_test.iloc[[i]]
y_true = y_test.iloc[i]

print("\n=== SINGLE CROP CHECK ===")
print(f"  Actual label        : {label_str(y_true)}")
print(f"  Logistic Regression : {label_str(int(log_reg.predict(x_one_df)[0]))}")
print(f"  Random Forest       : {label_str(int(rf.predict(x_one_df)[0]))}")
print(f"  XGBoost             : {label_str(int(xgb.predict(x_one_df)[0]))}")

# --------------------------------
# 8) SAVE MODELS (for API/Serving)
# --------------------------------
joblib.dump(log_reg, "models/lr_crop_model.joblib")
joblib.dump(rf, "models/rf_crop_model.joblib")
joblib.dump(xgb, "models/xgb_crop_model.joblib")
print("\nSaved models → models/lr_crop_model.joblib, rf_crop_model.joblib, and xgb_crop_model.joblib")




# --------------------------------
# 6) Show results for all three models (Train vs Test)
# --------------------------------
print("\n=== HUBINTA OVERFITTING-KA (TRAIN VS TEST) ===")

# --- Random Forest ---
rf_train_preds = rf.predict(X_train)
rf_test_preds = rf.predict(X_test)
print(f"Random Forest:")
print(f"  -> Train Accuracy: {accuracy_score(y_train, rf_train_preds) * 100:.2f}%")
print(f"  -> Test Accuracy : {accuracy_score(y_test, rf_test_preds) * 100:.2f}%")

# --- XGBoost ---
xgb_train_preds = xgb.predict(X_train)
xgb_test_preds = xgb.predict(X_test)
print(f"\nXGBoost:")
print(f"  -> Train Accuracy: {accuracy_score(y_train, xgb_train_preds) * 100:.2f}%")
print(f"  -> Test Accuracy : {accuracy_score(y_test, xgb_test_preds) * 100:.2f}%")

# --- Logistic Regression ---
lr_train_preds = log_reg.predict(X_train)
lr_test_preds = log_reg.predict(X_test)
print(f"\nLogistic Regression:")
print(f"  -> Train Accuracy: {accuracy_score(y_train, lr_train_preds) * 100:.2f}%")
print(f"  -> Test Accuracy : {accuracy_score(y_test, lr_test_preds) * 100:.2f}%")