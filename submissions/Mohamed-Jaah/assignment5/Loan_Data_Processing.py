import pandas as pd
import numpy as np
from pathlib import Path

# ==========================================================
# File Paths
# ==========================================================
BASE_DIR = Path(__file__).resolve().parent

DATASET_DIR = BASE_DIR.parent.parent.parent / "dataset"

CSV_PATH = DATASET_DIR / "raw_loan_dataset.csv"
OUT_PATH = BASE_DIR / "Cleaned_Loan_Dataset.csv"

# ==========================================================
# STEP 1: Load & Inspect
# ==========================================================
df = pd.read_csv(CSV_PATH)

print("\n--- CHECKPOINT 1: Load & Inspect ---")
print("\nHEAD:")
print(df.head())

print("\nINFO:")
print(df.info())

print("\nMISSING VALUE COUNTS:")
print(df.isnull().sum())

print("\nUnique values in HasCollateral:", df["HasCollateral"].unique())
print("Unique values in PreviousDefaults:", df["PreviousDefaults"].unique())
print("Unique values in Approved:", df["Approved"].unique())

# ==========================================================
# STEP 2: Clean Currency Formatting
# ==========================================================
df["Income"] = (
    df["Income"]
    .astype(str)
    .str.replace(r"[\$,]", "", regex=True)
    .astype(float)
)

df["LoanAmount"] = (
    df["LoanAmount"]
    .astype(str)
    .str.replace(r"[\$,]", "", regex=True)
    .astype(float)
)

print("\n--- CHECKPOINT 2: Currency Cleaned ---")
print("Income dtype:", df["Income"].dtype, "| LoanAmount dtype:", df["LoanAmount"].dtype)
print(df[["Income", "LoanAmount"]].head())

# ==========================================================
# STEP 3: Fix Category Errors
# ==========================================================
category_fix_map = {
    "yes": "Yes",
    "y": "Yes",
    "yse": "Yes",
    "1": "Yes",
    "approved": "Yes",
    "no": "No",
    "n": "No",
    "0": "No",
    "rejected": "No",
}

for col in ["HasCollateral", "PreviousDefaults", "Approved"]:
    df[col] = (
        df[col]
        .astype(str)
        .str.strip()
        .str.lower()
        .replace(category_fix_map)
        .replace({"nan": np.nan})
    )

    print(f"\n--- CHECKPOINT 3: value_counts() for {col} after normalization ---")
    print(df[col].value_counts(dropna=False))

# ==========================================================
# STEP 4: Impute Missing Numeric Values
# ==========================================================
numeric_cols_to_impute = [
    "Income",
    "CreditScore",
    "EmploymentYears",
    "LoanAmount",
]

for col in numeric_cols_to_impute:
    avg_value = df[col].mean()
    n_missing = df[col].isnull().sum()
    df[col] = df[col].fillna(avg_value)
    print(f"Imputed {n_missing} missing value(s) in '{col}' with average = {avg_value:.2f}")

print("\n--- CHECKPOINT 4: Missing Values After Numeric Imputation ---")
print(df.isnull().sum())

# ==========================================================
# STEP 5: Impute Missing Categorical Values
# ==========================================================
categorical_cols_to_impute = [
    "HasCollateral",
    "PreviousDefaults",
]

for col in categorical_cols_to_impute:
    mode_value = df[col].mode()[0]
    n_missing = df[col].isnull().sum()
    df[col] = df[col].fillna(mode_value)
    print(f"Imputed {n_missing} missing value(s) in '{col}' with mode = {mode_value}")

print("\n--- CHECKPOINT 5: Missing Values After Categorical Imputation ---")
print(df.isnull().sum())

# ==========================================================
# STEP 6: Remove Duplicates
# ==========================================================
rows_before = df.shape[0]
df = df.drop_duplicates()
rows_after = df.shape[0]

print("\n--- CHECKPOINT 6: Duplicates Removed ---")
print(f"Rows before: {rows_before} | Rows after: {rows_after}")

# ==========================================================
# STEP 7: Outlier Capping (IQR)
# ==========================================================
def get_iqr_bounds(series, k=1.5):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper


cols_to_cap = [
    "Income",
    "CreditScore",
    "LoanAmount",
    "EmploymentYears",
]

for col in cols_to_cap:
    low, high = get_iqr_bounds(df[col])
    df[col] = df[col].clip(lower=low, upper=high)

    print(f"\n--- CHECKPOINT 7: {col} capped to [{low:.2f}, {high:.2f}] ---")
    print(df[col].describe()[["min", "max"]])

# ==========================================================
# STEP 8: Label Encoding
# ==========================================================
df["Approved"] = df["Approved"].map({"Yes": 1, "No": 0}).astype(int)
df["HasCollateral"] = df["HasCollateral"].map({"Yes": 1, "No": 0}).astype(int)
df["PreviousDefaults"] = df["PreviousDefaults"].map({"Yes": 1, "No": 0}).astype(int)

print("\n--- CHECKPOINT 8: Approved Class Distribution ---")
print(df["Approved"].value_counts())

print("\n--- CHECKPOINT 8: Remaining Nulls ---")
print(df[["HasCollateral", "PreviousDefaults"]].isnull().sum())

# ==========================================================
# STEP 9: Feature Engineering
# ==========================================================
df["DebtToIncome"] = df["LoanAmount"] / df["Income"].replace(0, np.nan)
df["IncomePerYearEmployed"] = df["Income"] / (df["EmploymentYears"] + 1)

print("\n--- CHECKPOINT 9: New Features ---")
print(df[["DebtToIncome", "IncomePerYearEmployed"]].describe())

# ==========================================================
# STEP 10: Final Checks & Save
# ==========================================================
print("\n--- CHECKPOINT 10: Final Head ---")
print(df.head())

print("\n--- CHECKPOINT 10: Final Info ---")
print(df.info())

print("\n--- CHECKPOINT 10: Final Missing Values ---")
print(df.isnull().sum())

df.to_csv(OUT_PATH, index=False)

print(f"\n✅ Cleaned dataset saved to:\n{OUT_PATH}")