import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import sklearn

CSV_PATH = './data-set/raw_car_dataset.csv'
df = pd.read_csv(CSV_PATH)

# === INITIAL SNAPSHOT ===
print("\n=== INITIAL HEAD ===")
print(df.head())

print("\n=== INITIAL INFO ===")
print(df.info())


print("\n=== INITIAL MISSING VALUES ===")
print(df.isnull().sum())

# 2) Clean target formatting
df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)

print("\n=== AFTER HEAD ===")
print(df.head(10))

# 3) Fix categorical issues BEFORE imputation
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})

print("\n=== AFTER LOCATION CLEANING ===")
print(df.head(10))


# 4) Impute Missing Values

df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())

df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])

df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])

df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

print("\n=== AFTER IMPUTATION ===")
print(df.isnull().sum())

# 5) Remove duplicates
before = df.shape
df = df.drop_duplicates()
after = df.shape

print("\n=== REMOVE DUPLICATES ===")
print(f"Shape before: {before}")
print(f"Shape after : {after}")
print(f"Rows removed: {before[0] - after[0]}")

import pandas as pd

summary = []

def iqr_fun(series, k=1.5):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1

    lower = q1 - k * iqr
    upper = q3 + k * iqr

    return lower, upper


def cap_outliers(df, column):
    lower, upper = iqr_fun(df[column])

    outliers = ((df[column] < lower) | (df[column] > upper)).sum()

    df[column] = df[column].clip(lower, upper)

    summary.append({
        "column": column,
        "lower_bound": lower,
        "upper_bound": upper,
        "outliers_capped": outliers
    })

    return df


# APPLY OUTLIERS CAPPING (OUTSIDE FUNCTION)
df = cap_outliers(df, "Price")
df = cap_outliers(df, "Odometer_km")

# SUMMARY TABLE
summary_df = pd.DataFrame(summary)
print(summary_df)

df = pd.get_dummies(df, columns=["Location"], drop_first=True)

print("\n=== AFTER HEAD ===")
print(df.head(10))

#Feature engineering
# Car Age
df["CarAge"] = 2026 - df["Year"]

# Km per Year (safe)
df["Km_per_year"] = df["Odometer_km"] / (df["CarAge"] + 1)

# Is_Urban
df["Is_Urban"] = (
    (df.get("Location_City", 0) == 1) |
    (
        (df.get("Location_Rural", 0) == 0) &
        (df.get("Location_Suburb", 0) == 0)
    )
).astype(int)

# Log Price (alternative target)
df["LogPrice"] = np.log1p(df["Price"])

# Quick check
print("\n=== FEATURE ENGINEERING RESULT ===")
print(df[["CarAge", "Km_per_year", "Is_Urban", "LogPrice"]].head())

# === INITIAL SNAPSHOT ===
print("\n=== INITIAL HEAD ===")
print(df.head())

# Feature Scaling (X only)

from sklearn.preprocessing import StandardScaler

# Continuous features only
continuous_features = [
    "Odometer_km",
    "Doors",
    "Accidents",
    "Year",
    "CarAge",
    "Km_per_year"
]

# Create scaler
scaler = StandardScaler()

# Scale only continuous features
df[continuous_features] = scaler.fit_transform(df[continuous_features])

# Show sample
print("\n=== SCALED FEATURES SAMPLE ===")
print(df[continuous_features].head())

# FINAL CHECKS

print("\n=== FINAL INFO ===")
df.info()

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())

print("\n=== DESCRIBE TABLE ===")
print(df.describe())

#SAVE CLEAN DATASET

OUTPUT_PATH = "car_l3_clean_ready.csv"

df.to_csv(OUTPUT_PATH, index=False)

print(f"\n Clean dataset saved successfully as: {OUTPUT_PATH}")