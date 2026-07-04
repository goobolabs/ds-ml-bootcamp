import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
CSV_PATH = r"C:\Users\Ali Black\Desktop\bootcamp1\ds-ml-bootcamp\submissions\Ahmetttt37\assigment 3\raw_car_dataset.csv"
df = pd.read_csv(CSV_PATH)
# print(df.shape)

# print(df.info())


# print(df.describe())
# replace
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})
# print(df["Location"].value_counts(dropna = False))
df["Price"] = df["Price"].replace(r"[/ $,]", "", regex = True).astype(float)

# fillna

df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())

df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])

df["Location"] = df["Location"].fillna(df["Location"].mode()[0])
# print(df.isnull().sum())

# deplicte

df = df.drop_duplicates()


# print(before, after)

# outliers

def iqr_fun(series, k=5):
    q1, q2 = series.quantile([0.25, 0.75])
    iqr = q2 - q1
    lower_bound = q1 - k * iqr
    uper_bound = q2 + k * iqr
    return lower_bound, uper_bound

lower_price, higher_price = iqr_fun(df["Price"])
lower_odometer, higher_odometer = iqr_fun(df["Odometer_km"])

df["Price"] = df["Price"].clip(lower_price, higher_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower_odometer, higher_odometer)

# one hot_encoding

df = pd.get_dummies(df, columns=["Location"], drop_first=False)

# future engineering

CURENT_YEAR = 2026
df["car_age"] = CURENT_YEAR - df["Year"]
df["is_city"] = df["Location_City"].astype(int)
df["long_price"] = np.log1p(df["Price"])


# future scaling

# 9) Feature scaling (X only; keep targets & dummies unscaled)
dont_scale = {"Price", "LogPrice"}

numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()

exclude = [c for c in df.columns if c.startswith("Location_")] + ["Is_City"]

num_features_to_scale = [
    c for c in numeric_cols
    if c not in dont_scale and c not in exclude
]

scaler = StandardScaler()

df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])


# === FINAL SNAPSHOT ===
print("\n=== FINAL HEAD ===")
print(df.head())

print("\n=== FINAL INFO ===")
print(df.info())

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())


# 10) Save
OUT_PATH = r"C:\Users\Ali Black\Desktop\bootcamp1\ds-ml-bootcamp\submissions\Ahmetttt37\assigment 3\clean_car_dataset.csv"

df.to_csv(OUT_PATH, index=False)






