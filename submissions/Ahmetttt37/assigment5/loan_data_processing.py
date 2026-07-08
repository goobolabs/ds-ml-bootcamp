import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

CSV_PATH = r"C:\Users\Ali Black\Desktop\bootcamp1\ds-ml-bootcamp\submissions\Ahmetttt37\assigment5\raw_loan_dataset.csv"
OUT_PATH = "./dataset/clean_loan_dataset.csv"


# 1) Load + initial snapshot

df = pd.read_csv(CSV_PATH)

# 2) Clean currency formatting

df["Income"] = df["Income"].replace(r"[\$,]", "", regex=True).astype(float)
df["LoanAmount"] = df["LoanAmount"].replace(r"[\$,]", "", regex=True).astype(float)


# 3) Normalize categorical typos BEFORE imputation

yes_no_map = {
    "yes": "Yes", "y": "Yes", "yse": "Yes", "1": "Yes", "approved": "Yes",
    "no": "No", "n": "No", "0": "No", "rejected": "No",
}

df["HasCollateral"] = df["HasCollateral"].astype(str).str.strip().str.lower().replace(yes_no_map).replace({"nan": np.nan})
df["PreviousDefaults"] = df["PreviousDefaults"].astype(str).str.strip().str.lower().replace(yes_no_map).replace({"nan": np.nan})
df["Approved"] = df["Approved"].astype(str).str.strip().str.lower().replace(yes_no_map).replace({"nan": np.nan})


# 4) Impute missing values

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


# 7) Label encoding (Yes/No → 0/1)
# L3: same mapping for target (Approved) and two-category features
# Approved=1, Rejected=0

df["Approved"] = df["Approved"].map({"Yes": 1, "No": 0}).astype(int)

print("\n=== CLASS DISTRIBUTION (after label encoding) ===")
print(df["Approved"].value_counts())
print(df["Approved"].value_counts(normalize=True).round(3))


# 8) Class balance check

class_ratio = df["Approved"].value_counts(normalize=True).min()
if class_ratio < 0.30:
    print("\nWarning: severely imbalanced classes — consider balancing techniques (L3).")
else:
    print("\nClass balance OK for baseline Accuracy (both classes well represented).")

df["HasCollateral"] = df["HasCollateral"].map({"Yes": 1, "No": 0}).astype(int)
df["PreviousDefaults"] = df["PreviousDefaults"].map({"Yes": 1, "No": 0}).astype(int)

# --------------------------------
# 9) Feature engineering 

df["DebtToIncome"] = df["LoanAmount"] / df["Income"].replace(0, np.nan)
df["IncomePerYearEmployed"] = df["Income"] / (df["EmploymentYears"] + 1)


# 10) Feature Scaling (RobustScaler)

from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()

numeric_features = [ "Income", "CreditScore", "EmploymentYears", "LoanAmount", "DebtToIncome", 
"IncomePerYearEmployed"]

df[numeric_features] = scaler.fit_transform(df[numeric_features])

print("\n=== Scaled Numeric Features ===")
print(df[numeric_features].head())



# 11) Final Checks & Save



OUT_PATH = r"C:\Users\Ali Black\Desktop\bootcamp1\ds-ml-bootcamp\submissions\Ahmetttt37\assigment5\clean_loan_dataset.csv"

df.to_csv(OUT_PATH, index=False)

