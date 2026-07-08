import pandas as pd
import numpy as np
df = pd.read_csv("raw_car_dataset.csv")
#display first 10 rows
print(df.head(11))
#info of data
print(df.info())
# #shape
# print(df.shape)
# #missing counts
# print(df.isnull().sum())
# #locatin value
# print(df["Location"].value_counts(dropna=False))
# #Key issues found: Price is a mixed-format string ,Location has typos ('Subrb') and unknowns ('??'),Missing values in Odometer_km, Doors, Location
df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)
print(df["Price"].dtype)
print(df["Price"].skew())
# 3) FIX CATEGORY ERRORS BEFORE IMPUTATION
df["Location"] = df["Location"].str.strip()
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": np.nan})
print(df["Location"].value_counts(dropna=False))
# 4) IMPUTE MISSING VALUES
# Odometer_km is continuous and skewed -> median is safer than mean
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
# Doors, Accidents, Location are categorical/discrete -> use mode
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])
print(df.isnull().sum())
# 5) REMOVE DUPLICATES
before = df.shape
df = df.drop_duplicates()
after = df.shape
print(before, after)
print("rows removed:", before[0] - after[0])
# 6) OUTLIERS (IQR CAPPING)
q1, q3 = df["Price"].quantile([0.25, 0.75])
iqr = q3 - q1
df["Price"] = df["Price"].clip(q1 - 1.5*iqr, q3 + 1.5*iqr)

q1, q3 = df["Odometer_km"].quantile([0.25, 0.75])
iqr = q3 - q1
df["Odometer_km"] = df["Odometer_km"].clip(q1 - 1.5*iqr, q3 + 1.5*iqr)
print(df[["Price", "Odometer_km"]].describe())
# 7) ONE-HOT ENCODE LOCATION
df = pd.get_dummies(df, columns=["Location"], dtype="int")
print([c for c in df.columns if c.startswith("Location_")])
# 8) FEATURE ENGINEERING (no leakage)
CURRENT_YEAR = 2026
df["CarAge"] = CURRENT_YEAR - df["Year"]
df["Km_per_year"] = df["Odometer_km"] / df["CarAge"].replace(0, np.nan)
df["Is_Urban"] = df["Location_City"]
df["LogPrice"] = np.log1p(df["Price"])  # alt target, not a feature
print(df[["CarAge", "Km_per_year", "Is_Urban", "LogPrice"]].head())
# 9) FEATURE SCALING (X only, not Price/LogPrice, not dummies)
from sklearn.preprocessing import StandardScaler

dont_scale = {"Price", "LogPrice"}
dummy_cols = [c for c in df.columns if c.startswith("Location_")] + ["Is_Urban"]
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
cols_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in dummy_cols]

scaler = StandardScaler()
df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])
print(df[cols_to_scale].mean())
print(df[cols_to_scale].std())

# 10) FINAL CHECKS & SAVE
print(df.info())
print(df.isnull().sum())
print(df.describe())
df.to_csv("clean_car_dataset.csv", index=False)
