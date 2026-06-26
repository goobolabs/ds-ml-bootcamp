import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


# 1. LOAD and INSPECT

df = pd.read_csv("raw_car_dataset.csv")
df.info()
df.shape
df.isnull().sum()
df["Location"].value_counts(dropna=False)
# print(df.head(10))


# 2. CLEAN TARGET FORMATTING (PRICE)
df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)
# print("After Formatting Price", df["Price"].head())

# 3. FIX CATEGORY ERRORS BEFORE IMPUTATION
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??" : pd.NA })
# print(df["Location"].value_counts(dropna=False))

# 4. IMPUTE MISSING VALUES (justify choices)
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].median())
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])


# 5. REMOVE DUPLICATES
before = df.shape
df = df.drop_duplicates()
after = df.shape
# print("Before Removed Duplicates: ", before)
# print("After Removed Duplicates: ", after)


# 6. OUTLIERS (IQR Capping)
def iqr_capping(series):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return lower, upper

low_price, high_price = iqr_capping(df["Price"])
low_odometer, high_odometer = iqr_capping(df["Odometer_km"])

df["Price"] = df["Price"].clip(lower=low_price, upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_odometer, upper=high_odometer)

# 7. ONE-HOT ENCODE CATEGORIGAL(s)
df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype=int)
# print([c for c in df.columns if c.startswith("Location")])


# 8. FEATURE ENGINEERING (no Leakage)
CURRENT_YEAR = 2026
df["CarAge"] = (CURRENT_YEAR - df["Year"]).clip(lower=1)
df["Km_per_year"] = df["Odometer_km"] / df["CarAge"]
df["Is_City"] = df["Location_City"]
df["LogPrice"] = np.log1p(df["Price"])


# 9. FEATURE SCALING (X Only)
dont_scale = {"Price", "LogPrice"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
exclude = [c for c in df.columns if c.startswith("Location")] + ["Is_City"]
features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]
scaler = StandardScaler()
df[features_to_scale] = scaler.fit_transform(df[features_to_scale])


# 10. FINAL CHECKS & SAVE
OUT_PATH = "clean_car_dataset.csv"
df.to_csv(OUT_PATH)




