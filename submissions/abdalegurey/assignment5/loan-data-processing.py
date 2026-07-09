import pandas as pd
import numpy as np
from sklearn.preprocessing import RobustScaler



CSV_PATH = "./dataset/raw_loan_dataset.csv"

# --------------------------------
# 1) Load & Inspect
# --------------------------------
df = pd.read_csv(CSV_PATH)

print("\n=== INITIAL HEAD ===")
print(df.head())

print("\n=== INITIAL INFO ===")
print(df.info())

print("\n=== INITIAL MISSING VALUES ===")
print(df.isnull().sum())

# --------------------------------
# 2)Clean Currency Formatting
# --------------------------------
df["Income"] = df["Income"].replace(r"[\$,]", "", regex=True).astype(float)
df["LoanAmount"] = df["LoanAmount"].replace(r"[\$,]", "", regex=True).astype(float)


# --------------------------------
# 3)Fix Category Errors before Imputation
# --------------------------------
yes_no_map = {
    "yes": "Yes", "y": "Yes", "yse": "Yes", "1": "Yes", "approved": "Yes",
    "no": "No", "n": "No", "0": "No", "rejected": "No",
}

df["HasCollateral"] = df["HasCollateral"].astype(str).str.strip().str.lower().replace(yes_no_map).replace({"nan": np.nan})
df["PreviousDefaults"] = df["PreviousDefaults"].astype(str).str.strip().str.lower().replace(yes_no_map).replace({"nan": np.nan})
df["Approved"] = df["Approved"].astype(str).str.strip().str.lower().replace(yes_no_map).replace({"nan": np.nan})

# --------------------------------
# 4) Impute missing values
# --------------------------------
df["Income"] = df["Income"].fillna(df["Income"].median())
df["CreditScore"] = df["CreditScore"].fillna(df["CreditScore"].median())
df["EmploymentYears"] = df["EmploymentYears"].fillna(df["EmploymentYears"].median())
df["LoanAmount"] = df["LoanAmount"].fillna(df["LoanAmount"].median())
df["HasCollateral"] = df["HasCollateral"].fillna(df["HasCollateral"].mode()[0])
df["PreviousDefaults"] = df["PreviousDefaults"].fillna(df["PreviousDefaults"].mode()[0])

# 5) Remove duplicates

before = df.shape[0]
df = df.drop_duplicates()
print(f"\nDropped duplicates: {before} -> {df.shape[0]} rows")


# 6) IQR capping on numeric columns


def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

low_income,  high_income  = iqr_fun(df["Income"])
low_credit,  high_credit  = iqr_fun(df["CreditScore"])
low_loan,    high_loan    = iqr_fun(df["LoanAmount"])
low_emp,     high_emp     = iqr_fun(df["EmploymentYears"])

df["Income"]          = df["Income"].clip(lower=low_income,  upper=high_income)
df["CreditScore"]     = df["CreditScore"].clip(lower=low_credit, upper=high_credit)
df["LoanAmount"]      = df["LoanAmount"].clip(lower=low_loan,    upper=high_loan)
df["EmploymentYears"] = df["EmploymentYears"].clip(lower=low_emp,     upper=high_emp)

# --------------------------------
# 7)Label Encoding

# --------------------------------
df["Approved"] = df["Approved"].map({"Yes": 1, "No": 0}).astype(int)

print("\n=== CLASS DISTRIBUTION (after label encoding) ===")
print(df["Approved"].value_counts())
print(df["Approved"].value_counts(normalize=True).round(3))

# 8)Class Balance Check


class_ratio = df["Approved"].value_counts(normalize=True).min()
if class_ratio < 0.30:
    print("\nWarning: severely imbalanced classes — consider balancing techniques (L3).")
else:
    print("\nClass balance OK for baseline Accuracy (both classes well represented).")

df["HasCollateral"] = df["HasCollateral"].map({"Yes": 1, "No": 0}).astype(int)
df["PreviousDefaults"] = df["PreviousDefaults"].map({"Yes": 1, "No": 0}).astype(int)

# --------------------------------
# 9) Feature engineering (no leakage from label)
# --------------------------------
df["DebtToIncome"] = df["LoanAmount"] / df["Income"].replace(0, np.nan)
df["IncomePerYearEmployed"] = df["Income"] / (df["EmploymentYears"] + 1)


# 10) StandardScaler on numeric features

binary_cols = {"HasCollateral", "PreviousDefaults", "Approved"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
scale_cols = [c for c in numeric_cols if c not in binary_cols]

scaler = RobustScaler()
df[scale_cols] = scaler.fit_transform(df[scale_cols])

# Chosen Scaler: RobustScaler
# I chose RobustScaler because it is less affected by outliers than StandardScaler. Although I capped extreme values using the IQR method, RobustScaler still provides robust scaling by using the median and interquartile range, making it a good choice for this loan dataset.

# 11) Final snapshot + save

print("\n=== FINAL HEAD ===")
print(df.head())

print("\n=== FINAL INFO ===")
print(df.info())

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())

OUT_PATH = "./dataset/clean_loan_dataset.csv"
df.to_csv(OUT_PATH, index=False)