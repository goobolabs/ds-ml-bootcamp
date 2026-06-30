import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("student_study_dataset.csv")

# ---------------------------------------------------------------
# Step 1 - Load the dataset and check the data
# ---------------------------------------------------------------
print("=== STEP 1: Load & Inspect ===")

print(df.head(10).to_string())
print("\nShape:", df.shape)
df.info()
print("\nMissing values:\n", df.isnull().sum())
print("\nIncome categories:\n", df["family_income_category"].value_counts(dropna=False))

# Things I found:
# - study_hours_per_day has one missing value
# - family_income_category is a categorical column
# - gender, internet_access and part_time_job need encoding
# - study_hours_per_day and sleep_hours may have outliers

# ---------------------------------------------------------------
# Step 2 - Convert the target column to numbers
# ---------------------------------------------------------------
print("\n=== STEP 2: Clean Target (final_exam_score) ===")

df["final_exam_score"] = pd.to_numeric(
    df["final_exam_score"],
    errors="coerce"
).astype(float)

print("dtype:", df["final_exam_score"].dtype)
print("skewness:", round(df["final_exam_score"].skew(), 4))

# ---------------------------------------------------------------
# Step 3 - Clean the category names
# ---------------------------------------------------------------
print("\n=== STEP 3: Fix Category Errors ===")

df["family_income_category"] = (
    df["family_income_category"]
    .astype(str)
    .str.strip()
    .str.title()
)

INCOME_MAP = {
    "High": "High",
    "Middle": "Middle",
    "Low": "Low"
}

df["family_income_category"] = df["family_income_category"].map(INCOME_MAP)

print(df["family_income_category"].value_counts(dropna=False))

# ---------------------------------------------------------------
# Step 4 - Fill missing values
# ---------------------------------------------------------------
print("\n=== STEP 4: Impute Missing Values ===")

# Use median for numerical data
study_median = df["study_hours_per_day"].median()

df["study_hours_per_day"] = df["study_hours_per_day"].fillna(study_median)

print(
    f"study_hours_per_day filled with median ({study_median})"
)

# Use mode for categorical data
for col in [
    "gender",
    "internet_access",
    "part_time_job",
    "family_income_category"
]:

    if df[col].isnull().any():

        mode = df[col].mode()[0]
        df[col] = df[col].fillna(mode)

        print(f"{col} filled with mode ({mode})")

print("\nMissing values after filling:")
print(df.isnull().sum())

# ---------------------------------------------------------------
# Step 5 - Remove duplicate rows
# ---------------------------------------------------------------
print("\n=== STEP 5: Remove Duplicates ===")

before = len(df)

df = df.drop_duplicates()

print(f"Removed {before-len(df)} duplicate rows.")

# student_id is only an ID, so remove it
df = df.drop(columns=["student_id"])

print("student_id removed.")

# ---------------------------------------------------------------
# Step 6 - Handle outliers using IQR
# ---------------------------------------------------------------
print("\n=== STEP 6: Outlier Capping (IQR) ===")

def iqr_clip(col):

    q1 = col.quantile(0.25)
    q3 = col.quantile(0.75)

    iqr = q3 - q1

    lower = q1 - (1.5 * iqr)
    upper = q3 + (1.5 * iqr)

    return col.clip(lower, upper), lower, upper

df["study_hours_per_day"], s_low, s_high = iqr_clip(df["study_hours_per_day"])
df["sleep_hours"], sl_low, sl_high = iqr_clip(df["sleep_hours"])

print(df[["study_hours_per_day", "sleep_hours"]].describe())

# ---------------------------------------------------------------
# Step 7 - Encode categorical columns
# ---------------------------------------------------------------
print("\n=== STEP 7: Encode Categorical Columns ===")

df["gender"] = df["gender"].map({"Male": 0, "Female": 1})
df["internet_access"] = df["internet_access"].map({"No": 0, "Yes": 1})
df["part_time_job"] = df["part_time_job"].map({"No": 0, "Yes": 1})

df = pd.get_dummies(
    df,
    columns=["family_income_category"],
    drop_first=True,
    dtype=int
)

income_cols = [
    c
    for c in df.columns
    if c.startswith("family_income_category")
]

print("New columns:", income_cols)

# ---------------------------------------------------------------
# Step 8 - Create new features
# ---------------------------------------------------------------
print("\n=== STEP 8: Feature Engineering ===")

# Combine study hours and attendance
df["Study_Efficiency"] = (
    df["study_hours_per_day"] *
    df["attendance_rate"]
)

# GPA for each subject
df["GPA_per_Subject"] = (
    df["previous_gpa"] /
    df["num_subjects"]
)

# Compare study time and sleep
df["Study_Sleep_Ratio"] = (
    df["study_hours_per_day"] /
    df["sleep_hours"].replace(0, np.nan)
)

# Student lives more than 10 km away
df["Far_From_School"] = (
    df["distance_to_school_km"] > 10
).astype(int)

# Attendance is 90% or more
df["High_Attendance"] = (
    df["attendance_rate"] >= 90
).astype(int)

# Log version of the target
df["Log_Final_Exam"] = np.log1p(df["final_exam_score"])

# ---------------------------------------------------------------
# Step 9 - Scale numerical columns
# ---------------------------------------------------------------
print("\n=== STEP 9: Feature Scaling ===")

dont_scale = {
    "final_exam_score",
    "Log_Final_Exam"
}

exclude = {
    "gender",
    "internet_access",
    "part_time_job",
    "Far_From_School",
    "High_Attendance"
} | set(income_cols)

scale_cols = [

    c

    for c in df.select_dtypes(include=["int64", "float64"]).columns

    if c not in dont_scale and c not in exclude
]

df[scale_cols] = StandardScaler().fit_transform(df[scale_cols])

print(df[scale_cols].head())

# ---------------------------------------------------------------
# Step 10 - Final check and save
# ---------------------------------------------------------------
print("\n=== STEP 10: Final Checks & Save ===")

df.info()

print(df.isnull().sum())

assert df["final_exam_score"].dtype == float
assert pd.api.types.is_numeric_dtype(df["Log_Final_Exam"])
assert df.isnull().sum().sum() == 0
assert len(income_cols) > 0

print("All checks passed.")

df.to_csv("Student_Clean.csv", index=False)

print("Student_Clean.csv saved.")
print("Final shape:", df.shape)