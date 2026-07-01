import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# =====================================================
# STEP 1: Load & Inspect
# =====================================================

BASE_DIR = os.path.dirname(__file__)
CSV_PATH = os.path.join(BASE_DIR, "raw_car_dataset.csv")

df = pd.read_csv(CSV_PATH)

print("\n========== STEP 1: LOAD & INSPECT ==========")
print(df.head(10))
print("\nShape:", df.shape)

print("\nInfo:")
df.info()

print("\nMissing values:")
print(df.isnull().sum())

print("\nLocation counts:")
print(df["Location"].value_counts(dropna=False))

# =====================================================
# STEP 2: Clean Price
# =====================================================

print("\n========== STEP 2: CLEAN PRICE ==========")

df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

print("Price dtype:", df["Price"].dtype)
print("Price skewness:", df["Price"].skew())

# =====================================================
# STEP 3: Fix Location
# =====================================================

print("\n========== STEP 3: FIX LOCATION ==========")

df["Location"] = (
    df["Location"]
    .replace("Subrb", "Suburb")
    .replace("??", np.nan)
)

print(df["Location"].value_counts(dropna=False))

# =====================================================
# STEP 4: Missing Value Imputation
# =====================================================

print("\n========== STEP 4: IMPUTATION ==========")

if "Odometer_km" in df.columns:
    df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())

if "Doors" in df.columns:
    df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])

if "Accidents" in df.columns:
    df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])

df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

print(df.isnull().sum())

# =====================================================
# STEP 5: Remove Duplicates
# =====================================================

print("\n========== STEP 5: REMOVE DUPLICATES ==========")

before = df.shape

df = df.drop_duplicates()

after = df.shape

print("Before:", before)
print("After :", after)
print("Rows removed:", before[0] - after[0])

# =====================================================
# STEP 6: IQR Capping
# =====================================================

print("\n========== STEP 6: OUTLIER CAPPING ==========")

def cap_iqr(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    return series.clip(lower, upper), lower, upper


df["Price"], low, high = cap_iqr(df["Price"])

print(f"Price bounds: ({low:.2f}, {high:.2f})")

if "Odometer_km" in df.columns:
    df["Odometer_km"], low, high = cap_iqr(df["Odometer_km"])
    print(f"Odometer bounds: ({low:.2f}, {high:.2f})")

# =====================================================
# STEP 7: One-Hot Encoding
# =====================================================

print("\n========== STEP 7: ONE-HOT ENCODING ==========")

df = pd.get_dummies(df, columns=["Location"])

location_cols = [c for c in df.columns if c.startswith("Location_")]

print(location_cols)

# =====================================================
# STEP 8: Feature Engineering
# =====================================================

print("\n========== STEP 8: FEATURE ENGINEERING ==========")

CURRENT_YEAR = 2026

df["CarAge"] = CURRENT_YEAR - df["YearBuilt"]

if "Odometer_km" in df.columns:
    df["Km_per_year"] = df["Odometer_km"] / df["CarAge"].replace(0, 1)

if "Location_City" in df.columns:
    df["Is_Urban"] = df["Location_City"].astype(int)

df["LogPrice"] = np.log1p(df["Price"])

print(df.head())

# =====================================================
# STEP 9: Scaling
# =====================================================

print("\n========== STEP 9: SCALING ==========")

continuous = []

for col in ["Size_sqft", "Odometer_km", "CarAge", "Km_per_year"]:
    if col in df.columns:
        continuous.append(col)

scaler = StandardScaler()

df[continuous] = scaler.fit_transform(df[continuous])

print(df[continuous].head())

# =====================================================
# STEP 10: Final Checks & Save
# =====================================================

print("\n========== STEP 10: FINAL CHECK ==========")

df.info()

print("\nMissing values:")
print(df.isnull().sum())

print("\nSummary:")
print(df.describe())

# ---------------- Assertions ----------------

assert df["Price"].dtype == float
assert "LogPrice" in df.columns
assert pd.api.types.is_numeric_dtype(df["LogPrice"])
assert df.isnull().sum().sum() == 0

assert any(col.startswith("Location_") for col in df.columns)

OUT_PATH = os.path.join(BASE_DIR, "clean_car_dataset.csv")

df.to_csv(OUT_PATH, index=False)

print("\nDataset saved successfully!")
print("Saved to:", OUT_PATH)