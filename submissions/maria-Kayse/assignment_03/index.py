import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

CSV_PATH = "./dataset/raw_car_dataset.csv"
df = pd.read_csv(CSV_PATH)

# === STEP 1: LOAD & INSPECT ===

print("\n=== HEAD(10) ===")
print(df.head(10))

print(df.shape)

print("\n=== INFO ===")
print(df.info())

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

print("\n=== LOCATION COUNTS ===")
print(df["Location"].value_counts(dropna=False))


# STEP 2: CLEAN PRICE

df["Price"] = pd.to_numeric(
    df["Price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False),
    errors="coerce"
)

print("\n=== STEP 2: CLEAN PRICE ===")
print("Price dtype:", df["Price"].dtype)
print("Price skewness:", df["Price"].skew())


# STEP 3: FIX LOCATION ERRORS

df["Location"] = df["Location"].replace({
    "Subrb": "Suburb",
    "Citty": "City",
    "Rurall": "Rural",
    "??": pd.NA,
    "unknown": pd.NA
})

print("\n=== STEP 3: LOCATION CLEANING ===")
print(df["Location"].value_counts(dropna=False))


# STEP 4: IMPUTE MISSING VALUES

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

print("\n=== STEP 4: IMPUTATION ===")
print(df.isnull().sum())


# STEP 5: REMOVE DUPLICATES

before = df.shape

df = df.drop_duplicates()

after = df.shape

print("\n=== STEP 5: REMOVE DUPLICATES ===")
print("Before:", before)
print("After :", after)
print("Rows Removed:", before[0] - after[0])


# STEP 6: IQR CAPPING

def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

low_price, high_price = iqr_fun(df["Price"])
low_odometer, high_odometer = iqr_fun(df["Odometer_km"])

df["Price"] = df["Price"].clip(
    lower=low_price,
    upper=high_price
)

df["Odometer_km"] = df["Odometer_km"].clip(
    lower=low_odometer,
    upper=high_odometer
)

print("\n=== STEP 6: IQR CAPPING ===")
print(df[["Price", "Odometer_km"]].describe())


# STEP 7: ONE HOT ENCODING

df = pd.get_dummies(
    df,
    columns=["Location"],
    drop_first=False,
    dtype="int"
)

print("\n=== STEP 7: ENCODING ===")

location_cols = [
    col for col in df.columns
    if col.startswith("Location_")
]

print(location_cols)


# STEP 8: FEATURE ENGINEERING

CURRENT_YEAR = 2026

df["CarAge"] = CURRENT_YEAR - df["Year"]

df["CarAge"] = df["CarAge"].replace(0, 1)

df["Km_per_year"] = (
    df["Odometer_km"] /
    df["CarAge"]
)

df["Is_Urban"] = (
    df[["Location_City", "Location_Suburb"]]
    .max(axis=1)
)

df["LogPrice"] = np.log1p(df["Price"])

print("\n=== STEP 8: FEATURE ENGINEERING ===")
print(
    df[
        [
            "CarAge",
            "Km_per_year",
            "Is_Urban",
            "LogPrice"
        ]
    ].head()
)


# STEP 9: SCALING

dont_scale = {"Price", "LogPrice"}

numeric_cols = df.select_dtypes(
    include=["int64", "float64"]
).columns.to_list()

exclude = [
    c for c in df.columns
    if c.startswith("Location_")
] + ["Is_Urban"]

num_features_to_scale = [
    c for c in numeric_cols
    if c not in dont_scale
    and c not in exclude
]

scaler = StandardScaler()

df[num_features_to_scale] = scaler.fit_transform(
    df[num_features_to_scale]
)

print("\n=== STEP 9: SCALING ===")
print(df[num_features_to_scale].head())


# STEP 10: FINAL CHECKS

print("\n=== FINAL INFO ===")
print(df.info())

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())

print("\n=== FINAL DESCRIBE ===")
print(df.describe())


# SANITY CHECKS

assert pd.api.types.is_numeric_dtype(df["Price"])
assert "LogPrice" in df.columns
assert df.isnull().sum().sum() == 0
assert any(
    col.startswith("Location_")
    for col in df.columns
)

print("\nAll sanity checks passed!")


# SAVE DATASET

OUT_PATH = "./dataset/clean_car_dataset.csv"

df.to_csv(
    OUT_PATH,
    index=False
)

print("\nDataset saved successfully!")