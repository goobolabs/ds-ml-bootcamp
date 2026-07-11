import pandas as pd
import numpy as np
from sklearn.preprocessing import RobustScaler

# =====================================================
# ASSIGNMENT 5 - PART B1
# LOAN DATA PREPROCESSING
# =====================================================

CSV_PATH = "./dataset/raw_loan_dataset.csv"

df = pd.read_csv(CSV_PATH)

# =====================================================
# 1. LOAD & INSPECT
# =====================================================

print("\n=== INITIAL HEAD ===")
print(df.head())

print("\n=== INITIAL INFO ===")
print(df.info())

print("\n=== INITIAL MISSING VALUES ===")
print(df.isnull().sum())

# =====================================================
# 2. CLEAN CURRENCY FORMATTING
# =====================================================

df["Income"] = (
    df["Income"]
    .replace(r"[\$,]", "", regex=True)
    .astype(float)
)

df["LoanAmount"] = (
    df["LoanAmount"]
    .replace(r"[\$,]", "", regex=True)
    .astype(float)
)

print("\n=== CURRENCY CLEANING COMPLETE ===")

# =====================================================
# 3. FIX CATEGORY ERRORS
# =====================================================

yes_no_map = {
    "yes": "Yes",
    "y": "Yes",
    "yse": "Yes",
    "approved": "Yes",
    "approve": "Yes",

    "no": "No",
    "n": "No",
    "rejected": "No",
    "reject": "No"
}

for col in ["HasCollateral", "PreviousDefaults", "Approved"]:

    df[col] = (
        df[col]
        .astype(str)
        .str.strip()
        .str.lower()
        .replace(yes_no_map)
        .replace({"nan": np.nan})
    )

    print(f"\n=== {col} VALUE COUNTS ===")
    print(df[col].value_counts(dropna=False))

# =====================================================
# 4. IMPUTE MISSING VALUES
# =====================================================

numeric_cols = [
    "Income",
    "CreditScore",
    "EmploymentYears",
    "LoanAmount"
]

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

categorical_cols = [
    "HasCollateral",
    "PreviousDefaults",
    "Approved"
]

for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])
    

print("\n=== MISSING VALUES AFTER IMPUTATION ===")
print(df.isnull().sum())

# =====================================================
# 5. REMOVE DUPLICATES
# =====================================================

rows_before = len(df)

df = df.drop_duplicates()

rows_after = len(df)

print("\n=== DUPLICATES REMOVED ===")
print("Rows Before:", rows_before)
print("Rows After :", rows_after)
print("Removed    :", rows_before - rows_after)

# =====================================================
# 6. OUTLIER CAPPING (IQR)
# =====================================================

def iqr_bounds(series, k=1.5):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)

    iqr = q3 - q1

    lower = q1 - (k * iqr)
    upper = q3 + (k * iqr)

    return lower, upper


outlier_columns = [
    "Income",
    "CreditScore",
    "LoanAmount",
    "EmploymentYears"
]

for col in outlier_columns:

    lower, upper = iqr_bounds(df[col])

    df[col] = df[col].clip(
        lower=lower,
        upper=upper
    )

    print(f"\n{col}")
    print("Lower Bound:", lower)
    print("Upper Bound:", upper)

# =====================================================
# 7. LABEL ENCODING
# =====================================================

binary_map = {
    "Yes": 1,
    "No": 0
}

df["Approved"] = df["Approved"].map(binary_map)
df["HasCollateral"] = df["HasCollateral"].map(binary_map)
df["PreviousDefaults"] = df["PreviousDefaults"].map(binary_map)

print("\n=== APPROVED CLASS DISTRIBUTION ===")
print(df["Approved"].value_counts())

# =====================================================
# 8. CLASS BALANCE CHECK
# =====================================================

print("\n=== CLASS COUNTS ===")
print(df["Approved"].value_counts())

print("\n=== CLASS PROPORTIONS ===")
print(df["Approved"].value_counts(normalize=True))

class_ratio = df["Approved"].value_counts(normalize=True).min()

if class_ratio < 0.30:
    print("\nWarning: Classes are imbalanced.")
else:
    print("\nDataset appears reasonably balanced.")

# =====================================================
# 9. FEATURE ENGINEERING
# =====================================================

df["DebtToIncome"] = (
    df["LoanAmount"] /
    df["Income"]
)

df["IncomePerYearEmployed"] = (
    df["Income"] /
    (df["EmploymentYears"] + 1)
)

print("\n=== FEATURE ENGINEERING COMPLETE ===")

# =====================================================
# 10. FEATURE SCALING
# Using RobustScaler
# =====================================================

binary_cols = [
    "Approved",
    "HasCollateral",
    "PreviousDefaults"
]

scale_cols = [
    col
    for col in df.select_dtypes(include="number").columns
    if col not in binary_cols
]

scaler = RobustScaler()

df[scale_cols] = scaler.fit_transform(df[scale_cols])

print("\n=== SCALING COMPLETE ===")

# =====================================================
# 11. FINAL CHECKS
# =====================================================

print("\n=== FINAL HEAD ===")
print(df.head())

print("\n=== FINAL INFO ===")
print(df.info())

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())

# =====================================================
# SAVE CLEAN DATASET
# =====================================================

OUT_PATH = "./dataset/clean_loan_dataset.csv"

df.to_csv(
    OUT_PATH,
    index=False
)

print(f"\nClean dataset saved to: {OUT_PATH}")