import pandas as pd
import numpy as np
from sklearn.preprocessing import RobustScaler

# 1 LOAD and INSPECT

PATH = "raw_loan_dataset.csv"

df = pd.read_csv(PATH)
# print("=======INITIAL DATA HEAD======")
# print(df.head())
# print("=======DATA INFO======")
# print(df.info())
# print("=======DATA ISNULL======")
# print(df.isnull().sum())

# CHECKING WRONG INCOME VALUES
wrong_inc_values = df["Income"].astype(str).str.contains(r"\$", regex=True).sum()
wrong_LoanA_values = df["LoanAmount"].astype(str).str.contains(r"\$", regex=True).sum()


# 2. CLEAN CURRENCY FORMATTING
df["Income"] = df["Income"].replace(r"[\$,]", "", regex=True).astype(float)
df["LoanAmount"] = df["LoanAmount"].replace(r"[\$,]", "", regex=True).astype(float)


# 3. FIX CATEGORY ERRORS BEFORE IMPUTATION
df["HasCollateral"] = df["HasCollateral"].astype(str).str.strip().str.lower().replace({"y": "Yes", "n": "No", "no": "No", "yse": "Yes", "yes": "Yes", "NaN": np.nan})
df["PreviousDefaults"] = df["PreviousDefaults"].astype(str).str.strip().str.lower().replace({"yes": "Yes", "no": "No", "y": "Yes", "n": "No", "1": "Yes", "0": "No" ,"NaN": np.nan})
df["Approved"] = df["Approved"].astype(str).str.strip().str.lower().replace({"approved": "Yes", "rejected": "No", "YES": "Yes", "NO": "No", "yes": "Yes", "no": "No" ,"NaN": np.nan})


# 4. IMPUTE MISSING VALUES
df["Income"] = df["Income"].fillna(df["Income"].median())
df["LoanAmount"] = df["LoanAmount"].fillna(df["LoanAmount"].median())
df["CreditScore"] = df["CreditScore"].fillna(df["CreditScore"].median())
df["EmploymentYears"] = df["EmploymentYears"].fillna(df["EmploymentYears"].median())
df["HasCollateral"] = df["HasCollateral"].fillna(df["HasCollateral"].mode()[0])
df["PreviousDefaults"] = df["PreviousDefaults"].fillna(df["PreviousDefaults"].mode()[0])



# 5. REMOVE DUPLICATES
before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]
print(f"Before droped duplicates {before} rows ----> \nAfter removed duplicated {after} rows ")

   

# 6. OUTLIERS (IQR CAPPING)
def iqr_capping(series):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return lower, upper

low_income, high_income = iqr_capping(df["Income"])
low_cScore, high_cScore = iqr_capping(df["CreditScore"])
low_L_Amount, high_L_Amount = iqr_capping(df["LoanAmount"])
low_E_Year, high_E_Year = iqr_capping(df["EmploymentYears"])

df["Income"] = df["Income"].clip(lower=low_income, upper=high_income)
df["CreditScore"] = df["CreditScore"].clip(lower=low_cScore, upper=high_cScore)
df["LoanAmount"] = df["LoanAmount"].clip(lower=low_L_Amount, upper=high_L_Amount)
df["EmploymentYears"] = df["EmploymentYears"].clip(lower=low_E_Year, upper=high_E_Year)



# 7. LABEL ENCODING
df["HasCollateral"] = df["HasCollateral"].map({"Yes": 1, "No": 0}).astype(int)
df["Approved"] = df["Approved"].map({"Yes": 1, "No": 0}).astype(int)
df["PreviousDefaults"] = df["PreviousDefaults"].map({"Yes": 1, "No": 0}).astype(int)


# 8. CLASS BALANCE CHECK
class_ratio = df["Approved"].value_counts(normalize=True).min()
if class_ratio < 0.30:
    print("Warning: severely imbalanced classes.")
else:
    print("\nClass balance OK for baseline Accuracy.")


# 9. FEATURE ENGINEERING (no leakage)
df["LoanToIncome"] = df["LoanAmount"] / df["Income"].replace(0, np.nan)
df["IncomePerEmploymentYear"] = df["Income"] / (df["EmploymentYears"] + 1)



# 10. FEATURE SCALING
num_cols = ["Income","CreditScore","EmploymentYears","LoanAmount", "IncomePerEmploymentYear", "LoanToIncome"]
scaler = RobustScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

binary_cols = {"HasCollateral", "PreviousDefaults", "Approved"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
scale_cols = [c for c in numeric_cols if c not in binary_cols]


# FINAL CHECKS and SAVES
df.to_csv("clean_load_dataset.csv", index=False)

print(df.head())




