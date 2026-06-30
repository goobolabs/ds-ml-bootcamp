import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

print("=" * 50)
print("STEP 1: LOAD & INSPECT")
print("=" * 50)

df = pd.read_csv("dataset/raw_car_dataset.csv")

print("\nHead (10 rows)")
print(df.head(10))

print("\nShape:")
print(df.shape)

print("\nInfo:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nLocation Value Counts:")
print(df["Location"].value_counts(dropna=False))

print("""
Key Issues:
- Missing values
- Currency symbols in Price
- Location typos
- Possible outliers
- Duplicate rows
""")

print("\n" + "=" * 50)
print("STEP 2: CLEAN PRICE")
print("=" * 50)

df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

print("Price dtype:", df["Price"].dtype)
print("Price skewness:", df["Price"].skew())

print("\n" + "=" * 50)
print("STEP 3: FIX LOCATION ERRORS")
print("=" * 50)

df["Location"] = df["Location"].astype(str).str.strip().str.title()

location_map = {
    "Subrb": "Suburb",
    "Suburb ": "Suburb",
    "Rurl": "Rural",
    "Cityy": "City",
    "??": np.nan,
    "Unknown": np.nan,
    "Nan": np.nan
}

df["Location"] = df["Location"].replace(location_map)

print(df["Location"].value_counts(dropna=False))

print("\n" + "=" * 50)
print("STEP 4: IMPUTE MISSING VALUES")
print("=" * 50)

df["Odometer_km"] = df["Odometer_km"].fillna(
    df["Odometer_km"].median()
)

df["Doors"] = df["Doors"].fillna(
    df["Doors"].mode()[0]
)

df["Accidents"] = df["Accidents"].fillna(
    df["Accidents"].mode()[0]
)

df["Location"] = df["Location"].fillna(
    df["Location"].mode()[0]
)

print("Missing after imputation:")
print(df.isnull().sum())

print("\n" + "=" * 50)
print("STEP 5: REMOVE DUPLICATES")
print("=" * 50)

before = df.shape[0]

df = df.drop_duplicates()

after = df.shape[0]

print("Before:", before)
print("After :", after)
print("Removed:", before - after)

print("\n" + "=" * 50)
print("STEP 6: IQR CAPPING")
print("=" * 50)

for col in ["Price", "Odometer_km"]:

    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)

    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    print(f"\n{col}")
    print("Lower Bound:", lower)
    print("Upper Bound:", upper)

    df[col] = df[col].clip(lower, upper)

print("\nSummary after capping:")
print(df[["Price", "Odometer_km"]].describe())


print("\n" + "=" * 50)
print("STEP 7: ONE HOT ENCODING")
print("=" * 50)

df = pd.get_dummies(
    df,
    columns=["Location"],
    dtype=int
)

location_cols = [
    col for col in df.columns
    if col.startswith("Location_")
]

print("New Columns:")
print(location_cols)


print("\n" + "=" * 50)
print("STEP 8: FEATURE ENGINEERING")
print("=" * 50)

current_year = 2026

df["CarAge"] = current_year - df["Year"]

df["Km_per_year"] = (
    df["Odometer_km"] /
    np.where(df["CarAge"] == 0, 1, df["CarAge"])
)

urban_cols = [
    c for c in df.columns
    if "City" in c or "Suburb" in c
]

df["Is_Urban"] = (
    df[urban_cols].sum(axis=1) > 0
).astype(int)


df["LogPrice"] = np.log1p(df["Price"])

print(df[
    ["CarAge", "Km_per_year",
     "Is_Urban", "LogPrice"]
].head())

print("\n" + "=" * 50)
print("STEP 9: FEATURE SCALING")
print("=" * 50)

continuous_cols = [
    "Odometer_km",
    "Doors",
    "Accidents",
    "Year",
    "CarAge",
    "Km_per_year"
]

scaler = StandardScaler()

df[continuous_cols] = scaler.fit_transform(
    df[continuous_cols]
)

print(df[continuous_cols].head())

print("\n" + "=" * 50)
print("STEP 10: FINAL CHECKS")
print("=" * 50)

print("\nInfo:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDescribe:")
print(df.describe())


assert pd.api.types.is_float_dtype(df["Price"])

assert "LogPrice" in df.columns

assert pd.api.types.is_numeric_dtype(df["LogPrice"])

assert df.isnull().sum().sum() == 0

assert len(location_cols) > 0

for col in continuous_cols:
    assert abs(df[col].mean()) < 0.1

print("\nAll sanity checks passed!")

df.to_csv(
    "clean_car_dataset.csv",
    index=False
)

print("\nSaved as clean_car_dataset.csv")