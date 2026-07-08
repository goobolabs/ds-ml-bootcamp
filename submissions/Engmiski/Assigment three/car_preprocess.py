import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


# 1) LOAD DATA

CSV_PATH = "Data/car_l3_dataset.csv"
df = pd.read_csv(CSV_PATH)


# 2) CLEAN TARGET (Price)

df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)


# 3) FIX CATEGORICAL ISSUES

df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})


# 4) HANDLE MISSING VALUES

df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])


# 5) REMOVE DUPLICATES

df = df.drop_duplicates()


# 6) IQR CAPPING

def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

low_price, high_price = iqr_fun(df["Price"])
low_odo, high_odo = iqr_fun(df["Odometer_km"])

df["Price"] = df["Price"].clip(lower=low_price, upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_odo, upper=high_odo)


# 7) FEATURE ENGINEERING

CURRENT_YEAR = 2026
df["CarAge"] = CURRENT_YEAR - df["Year"]

df["km_per_year"] = df["Odometer_km"] / df["CarAge"]

df["is_urban"] = df["Location"].apply(lambda x: 1 if x == "City" else 0)

df["LogPrice"] = np.log1p(df["Price"])


# 8) ONE HOT ENCODING

df = pd.get_dummies(df, columns=["Location"], drop_first=False)


# 9) FEATURE SCALING

dont_scale = ["Price", "LogPrice"]
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
exclude = [c for c in df.columns if c.startswith("Location_")] + ["is_urban"]

features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]

scaler = StandardScaler()
df[features_to_scale] = scaler.fit_transform(df[features_to_scale])


# 10) FINAL CLEAN

df = df.dropna()


# 11) SAVE CLEAN DATA

df.to_csv("Data/car_l3_clean_ready.csv", index=False)

print(" Data Saved Successfully ")
print(df.head())

print("add new feature")