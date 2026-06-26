


import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


import os

print(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(__file__)
CSV_PATH = os.path.join(BASE_DIR, "raw_car_dataset.csv")

df = pd.read_csv(CSV_PATH)

# print(df.head(10))

# print(df.shape)

# print(df.info)


df["Odometer_km"].value_counts(dropna=False)

# print(df.isnull().sum())

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

df["Price"] = df["Price"].replace(r"[$]", "", regex=True).astype(float)  



df["Location"]= df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})

# print(df["Location"].unique())
# print(df["Location"].value_counts(dropna=False))


print(df["Price"].skew())

df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())

df["Doors"] = df["Doors"].fillna(df["Doors"].mode())


# print("Ka hor:", df["Price"].isnull().sum())

df = df.dropna(subset=["Price"])

# print("Kadib:", df["Price"].isnull().sum())

# print(df.head(10))

before = df.shape

df = df.drop_duplicates()

after = df.shape

print("before:", before, "after:", after)


def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 -q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

low_Price, high_Price = iqr_fun(df["Price"])

print("IQR OF PRICE IS: ")

print("low_price: ", low_Price, "high_price: ", high_Price)

df["Price"] = df["Price"].clip(lower = low_Price, upper = high_Price )

# print(df["Price"].describe())

df = pd.get_dummies(df, columns = ["Location"], drop_first = False)

# print(df.head(10))

CURRENT_YEAR = 2025

df["Car_Age"] = CURRENT_YEAR - df["Year"]

df["LogPrice"] = np.log1p(df["Price"])

# print(df.head(10))


numeric_features = [
    "Odometer_km",
    "Doors",
    "Accidents",
    "Car_Age"
]


scaler = StandardScaler()


df[numeric_features] = scaler.fit_transform(df[numeric_features])


print(df.head())

OUT_PATH = "clean_car_dataset.csv"

df.to_csv(OUT_PATH)

print("saved to: ", OUT_PATH)
