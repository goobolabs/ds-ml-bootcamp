import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# ============================
# Load Dataset
# ============================

CSV_PATH = "raw_car_dataset.csv"
df = pd.read_csv(CSV_PATH)

# ============================
# INITIAL SNAPSHOT
# ============================

print("\n=== INITIAL HEAD ===")
print(df.head())

print("\n=== INITIAL INFO ===")
print(df.info())

print("\n=== INITIAL MISSING VALUES ===")
print(df.isnull().sum())

# ============================
# Clean Price Column
# ============================

df["Price"] = (
    df["Price"]
    .replace(r"[\$,]", "", regex=True)
    .astype(float)
)

# ============================
# Fix Categorical Errors
# ============================

df["Location"] = df["Location"].replace({
    "Subrb": "Suburb",
    "??": pd.NA
})

# ============================
# Fill Missing Values
# ============================

df["Odometer_km"] = df["Odometer_km"].fillna(
    df["Odometer_km"].median()
)

df["Doors"] = df["Doors"].fillna(
    df["Doors"].mode()[0]
)

df["Location"] = df["Location"].fillna(
    df["Location"].mode()[0]
)

# ============================
# Remove Duplicates
# ============================

before = df.shape
df = df.drop_duplicates()
after = df.shape

print(f"\nDuplicates Removed: {before} -> {after}")

# ============================
# IQR Function
# ============================

def iqr_fun(series, k=1.5):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)

    iqr = q3 - q1

    lower = q1 - k * iqr
    upper = q3 + k * iqr

    return lower, upper

# ============================
# Handle Outliers
# ============================

low_price, high_price = iqr_fun(df["Price"])
low_odo, high_odo = iqr_fun(df["Odometer_km"])

df["Price"] = df["Price"].clip(
    lower=low_price,
    upper=high_price
)

df["Odometer_km"] = df["Odometer_km"].clip(
    lower=low_odo,
    upper=high_odo
)

# ============================
# One-Hot Encoding
# ============================

df = pd.get_dummies(
    df,
    columns=["Location"],
    drop_first=False,
    dtype="int"
)

# ============================
# Feature Engineering
# ============================

CURRENT_YEAR = 2025

df["CarAge"] = CURRENT_YEAR - df["Year"]

df["Km_per_Year"] = (
    df["Odometer_km"] /
    df["CarAge"].replace(0, 1)
)

df["Price_per_Door"] = (
    df["Price"] /
    df["Doors"].replace(0, np.nan)
)

df["Has_Accident"] = (
    df["Accidents"] > 0
).astype(int)

df["Is_City"] = df["Location_City"].astype(int)

df["LogPrice"] = np.log1p(df["Price"])

# ============================
# Feature Scaling
# ============================

dont_scale = {"Price", "LogPrice"}

numeric_cols = df.select_dtypes(
    include=["int64", "float64"]
).columns.tolist()

exclude = [
    col for col in df.columns
    if col.startswith("Location_")
] + ["Is_City", "Has_Accident"]

num_features_to_scale = [
    col
    for col in numeric_cols
    if col not in dont_scale
    and col not in exclude
]

scaler = StandardScaler()

df[num_features_to_scale] = scaler.fit_transform(
    df[num_features_to_scale]
)

# ============================
# FINAL SNAPSHOT
# ============================

print("\n=== FINAL HEAD ===")
print(df.head())

print("\n=== FINAL INFO ===")
print(df.info())

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())

# ============================
# Save Dataset
# ============================

OUT_PATH = "clean_car_dataset.csv"

df.to_csv(OUT_PATH, index=False)

print("\nDataset cleaned successfully!")
print(f"Saved to: {OUT_PATH}")