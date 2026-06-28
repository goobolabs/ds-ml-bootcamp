import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# =========================
# 1. LOAD & INSPECT
# =========================
df = pd.read_csv("raw_car_dataset.csv")

print("\nSTEP 1 - HEAD")
print(df.head(10))

print("\nSHAPE:", df.shape)
print("\nINFO:")
print(df.info())

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nLOCATION COUNTS:")
print(df["Location"].value_counts(dropna=False))


# =========================
# 2. CLEAN PRICE
# =========================
print("\nSTEP 2 - CLEAN PRICE")

df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

print("Price dtype:", df["Price"].dtype)
print("Skewness:", df["Price"].skew())


# =========================
# 3. CLEAN LOCATION
# =========================
print("\nSTEP 3 - FIX LOCATION")

df["Location"] = df["Location"].astype(str).str.strip()

df["Location"] = df["Location"].replace({
    "Subrb": "Suburb",
    "??": np.nan,
    "nan": np.nan,
    "": np.nan
})

print(df["Location"].value_counts(dropna=False))


# =========================
# 4. IMPUTE MISSING VALUES
# =========================
print("\nSTEP 4 - IMPUTATION")

df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

print(df.isnull().sum())


# =========================
# 5. REMOVE DUPLICATES
# =========================
print("\nSTEP 5 - DUPLICATES")

before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]

print("Before:", before)
print("After:", after)
print("Removed:", before - after)


# =========================
# 6. OUTLIERS (IQR CAPPING)
# =========================
print("\nSTEP 6 - OUTLIERS")

def iqr_cap(data, col):
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    data[col] = np.clip(data[col], lower, upper)
    return data

df = iqr_cap(df, "Price")
df = iqr_cap(df, "Odometer_km")

print(df[["Price", "Odometer_km"]].describe())


# =========================
# 7. ONE HOT ENCODING
# =========================
print("\nSTEP 7 - ENCODING")

df = pd.get_dummies(df, columns=["Location"], drop_first=True)

print(df.columns)


# =========================
# 8. FEATURE ENGINEERING
# =========================
print("\nSTEP 8 - FEATURES")

current_year = 2026

df["CarAge"] = current_year - df["Year"]
df["Km_per_year"] = df["Odometer_km"] / (df["CarAge"] + 1)
df["HasAccident"] = (df["Accidents"] > 0).astype(int)

df["LogPrice"] = np.log1p(df["Price"])

print(df[["CarAge", "Km_per_year", "HasAccident", "LogPrice"]].head())


# =========================
# 9. FEATURE SCALING
# =========================
print("\nSTEP 9 - SCALING")

scaler = StandardScaler()

scale_cols = ["Odometer_km", "Doors", "Accidents", "CarAge", "Km_per_year"]

df[scale_cols] = scaler.fit_transform(df[scale_cols])

print(df[scale_cols].head())


# =========================
# 10. FINAL CHECK + SAVE
# =========================
print("\nSTEP 10 - FINAL CHECK")

print(df.isnull().sum())
print(df.describe())

df.to_csv("clean_car_dataset.csv", index=False)

print("\nSaved successfully!")