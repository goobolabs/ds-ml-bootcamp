# car_preprocess.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

print("=" * 50)
print("STEP 1: LOAD & INSPECT DATA")
print("=" * 50)

# Load dataset
df = pd.read_csv("raw_car_dataset.csv")

print("\nFirst 10 rows:")
print(df.head(10))

print("\nShape:")
print(df.shape)

print("\nInfo:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nLocation value counts:")
print(df["Location"].value_counts(dropna=False))


print("\n" + "=" * 50)
print("STEP 2: CLEAN PRICE")
print("=" * 50)

# Remove currency symbols and commas
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

# Convert to numeric
df["Price"] = pd.to_numeric(
    df["Price"],
    errors="coerce"
)

print("Price datatype:")
print(df["Price"].dtype)

print("\nPrice skewness:")
print(df["Price"].skew())


print("\n" + "=" * 50)
print("STEP 3: FIX CATEGORY ERRORS")
print("=" * 50)

# Normalize text
df["Location"] = (
    df["Location"]
    .astype(str)
    .str.strip()
    .str.title()
)

# Fix typos
location_map = {
    "Subrb": "Suburb",
    "??": np.nan,
    "Unknown": np.nan
}

df["Location"] = (
    df["Location"]
    .replace(location_map)
)

print(df["Location"].value_counts(dropna=False))


print("\n" + "=" * 50)
print("STEP 4: IMPUTE MISSING VALUES")
print("=" * 50)

# Odometer → median
df["Odometer_km"] = (
    df["Odometer_km"]
    .fillna(df["Odometer_km"].median())
)

# Doors → mode
df["Doors"] = (
    df["Doors"]
    .fillna(df["Doors"].mode()[0])
)

# Accidents → mode
df["Accidents"] = (
    df["Accidents"]
    .fillna(df["Accidents"].mode()[0])
)

# Location → mode
df["Location"] = (
    df["Location"]
    .fillna(df["Location"].mode()[0])
)

print("Missing values after imputation:")
print(df.isnull().sum())


print("\n" + "=" * 50)
print("STEP 5: REMOVE DUPLICATES")
print("=" * 50)

before = df.shape

df = df.drop_duplicates()

after = df.shape

removed = before[0] - after[0]

print("Before:", before)
print("After:", after)
print("Removed:", removed)


print("\n" + "=" * 50)
print("STEP 6: IQR OUTLIER CAPPING")
print("=" * 50)

for col in ["Price", "Odometer_km"]:

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df[col] = df[col].clip(lower, upper)

    print(f"\n{col} summary:")
    print(df[col].describe())


print("\n" + "=" * 50)
print("STEP 7: ONE HOT ENCODING")
print("=" * 50)

df = pd.get_dummies(
    df,
    columns=["Location"],
    prefix="Location"
)

location_cols = [
    col for col in df.columns
    if "Location_" in col
]

print("New columns:")
print(location_cols)


print("\n" + "=" * 50)
print("STEP 8: FEATURE ENGINEERING")
print("=" * 50)

current_year = 2026

# Feature 1
df["CarAge"] = (
    current_year - df["Year"]
)

# Feature 2
df["Km_per_year"] = (
    df["Odometer_km"] /
    (df["CarAge"] + 1)
)

# Feature 3
if "Location_City" in df.columns:
    df["Is_Urban"] = (
        df["Location_City"]
        .astype(int)
    )
else:
    df["Is_Urban"] = 0

# Alternative target
df["LogPrice"] = np.log(
    df["Price"] + 1
)

print(df[[
    "CarAge",
    "Km_per_year",
    "Is_Urban",
    "LogPrice"
]].head())


print("\n" + "=" * 50)
print("STEP 9: FEATURE SCALING")
print("=" * 50)

scale_cols = [
    "Odometer_km",
    "Year",
    "CarAge",
    "Km_per_year"
]

scaler = StandardScaler()

df[scale_cols] = (
    scaler.fit_transform(
        df[scale_cols]
    )
)

print(df[scale_cols].head())


print("\n" + "=" * 50)
print("STEP 10: FINAL CHECKS")
print("=" * 50)

print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDescribe:")
print(df.describe())


# Assertions

assert df["Price"].dtype == "float64"
assert "LogPrice" in df.columns
assert df.isnull().sum().sum() == 0
assert any(
    col.startswith("Location_")
    for col in df.columns
)

print("\nAssertions passed")


# Save final dataset

df.to_csv(
    "clean_car_dataset.csv",
    index=False
)

print("\nDataset saved successfully")