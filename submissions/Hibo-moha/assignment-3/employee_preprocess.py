import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

print("=" * 50)
print("STEP 1: LOAD DATA")
print("=" * 50)

df = pd.read_csv("dataset/employee_dataset.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())

# Clean column names

df.columns = (
    df.columns
    .str.strip()
    .str.replace("\t", "", regex=False)
)

print("\nColumns:")
print(df.columns.tolist())

print("\nSTEP 2: CLEAN MINUTES LATE")

df["Minutes Late"] = (
    df["Minutes Late"]
    .astype(str)
    .str.replace("min", "", regex=False)
    .str.replace(" ", "", regex=False)
)

df["Minutes Late"] = pd.to_numeric(
    df["Minutes Late"],
    errors="coerce"
)

print(df["Minutes Late"].head())
print(df["Minutes Late"].dtype)

print("\nSTEP 3: CLEAN ATTENDANCE")

df["Attendance Rate (%)"] = (
    df["Attendance Rate (%)"]
    .astype(str)
    .str.replace("%", "", regex=False)
    .str.strip()
)

df["Attendance Rate (%)"] = pd.to_numeric(
    df["Attendance Rate (%)"],
    errors="coerce"
)

print(df["Attendance Rate (%)"].head())
print(df["Attendance Rate (%)"].dtype)

print("\nMissing Values After Conversion")

print(df.isnull().sum())

print("\nSTEP 4: CLEAN CATEGORIES & IMPUTE")

# Gender
df["Gender"] = (
    df["Gender"]
    .astype(str)
    .str.strip()
    .str.title()
)

# Department
df["Department"] = (
    df["Department"]
    .astype(str)
    .str.strip()
    .str.title()
)

# Transport Method
df["Transport Method"] = (
    df["Transport Method"]
    .astype(str)
    .str.strip()
    .str.title()
)

# Fill missing Attendance Rate with median
df["Attendance Rate (%)"] = df["Attendance Rate (%)"].fillna(
    df["Attendance Rate (%)"].median()
)

print("\nMissing After Imputation:")
print(df.isnull().sum())

print("\nSTEP 5: REMOVE DUPLICATES")

before = df.shape[0]

df = df.drop_duplicates()

after = df.shape[0]

print("Rows Before:", before)
print("Rows After :", after)
print("Removed    :", before - after)

print("\nSTEP 6: IQR CAPPING")

for col in ["Age", "Minutes Late", "Attendance Rate (%)"]:

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    print(f"\n{col}")
    print("Lower:", lower)
    print("Upper:", upper)

    df[col] = df[col].clip(lower, upper)

    print("\nSTEP 7: FEATURE ENGINEERING")

df["IsLate"] = (
    df["Minutes Late"] > 0
).astype(int)

df["HighAttendance"] = (
    df["Attendance Rate (%)"] >= 90
).astype(int)

df["AttendanceScore"] = (
    df["Attendance Rate (%)"]
    - df["Minutes Late"]
)

print(
    df[
        [
            "IsLate",
            "HighAttendance",
            "AttendanceScore"
        ]
    ].head()
)

df["Department"] = df["Department"].replace({
    "Public Adminstration": "Public Administration",
    "Software Engneer": "Software Engineer",
    "Human Resource": "Human Resources",
    "Hr": "Human Resources",
    "It": "IT",
    "Project Management": "Project Planning And Management",
    "Computer": "Computer Science",
    "Account Finance": "Accounting",
    "Accounting": "Finance",
    "Account Finance": "Finance"
})

print("\nSTEP 8: ONE HOT ENCODING")

df = pd.get_dummies(
    df,
    columns=[
        "Gender",
        "Department",
        "Transport Method"
    ],
    dtype=int
)

new_cols = [
    c for c in df.columns
    if c.startswith("Gender_")
    or c.startswith("Department_")
    or c.startswith("Transport Method_")
]

print("\nNew Dummy Columns:")
print(new_cols)

from sklearn.preprocessing import StandardScaler

print("\nSTEP 9: FEATURE SCALING")

scaler = StandardScaler()

scale_cols = [
    "Age",
    "Minutes Late",
    "Attendance Rate (%)",
    "AttendanceScore"
]

df[scale_cols] = scaler.fit_transform(
    df[scale_cols]
)

print(df[scale_cols].head())

print("\nSTEP 10: FINAL CHECKS")

print("\nShape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDescribe:")
print(df.describe())

assert df.isnull().sum().sum() == 0

df.to_csv(
    "clean_employee_dataset.csv",
    index=False
)

print("\nDataset saved successfully!")
print("File: clean_employee_dataset.csv")