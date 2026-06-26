import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from pathlib import Path

CSV_PATH = Path(__file__).parent / "raw_car_dataset.csv"

df = pd.read_csv(CSV_PATH)

# print(df.head(50))
# print(df.shape)
# print(df.info())

# # Removing \ $ _ , and so on.
df["Price"] = df["Price"].replace(r"[\$,]" , "", regex=True).astype(float)
# print(df.tail(50))

# Fixing Categoreis
df["Location"] = df["Location"].replace({"Subrb" : "Suburb", "??" : pd.NA})
# print("Location Counts After fixed : ")
# print(df["Location"].value_counts(dropna=False))
# print(df.head(40))

# Checking Missing Values and reArranging
print(df.isnull().sum())

df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode() [0])
df["Location"] = df["Location"].fillna(df["Location"].mode() [0])

print("After ReArranging missing values : ", df.isnull().sum())

print(df.tail(50))

# Removing duplicates 
before = df.shape
df = df.drop_duplicates()
after = df.shape
# print("Before Removing duplicates : ",before , "After Removing duplicates : ", after)

# Fixing the outlairs IQR............................................

# print(df["Price"].skew())
# print(df.describe())

def iqr_func(series, k = 1.5):
    q1,q3 = series.quantile([0.25,0.75])
    iqr = q3-q1 
    upper = q3 + k*iqr
    lower = q1 - k*iqr
    return upper , lower

high_price , low_price = iqr_func(df["Price"])
high_Odometer_km , low_Odometer_km = iqr_func(df["Odometer_km"])

df["Price"] = df["Price"].clip(upper = high_price , lower = low_price)
df["Odometer_km"] = df["Odometer_km"].clip(upper = high_Odometer_km , lower = low_Odometer_km)

# print("After IQR of Clipping")
# print(df["Price"].describe())

# print("After IQR of Clipping")
# print(df["Odometer_km"].describe())


# One hot encoling 
df = pd.get_dummies(df, columns = ["Location"],drop_first = False)
# print("One hot Encoled of Location")
# print(df.head(10))

#Feature Engineering.
CRRENT_YEAR = 2026
df["Car_Age"] = CRRENT_YEAR - df["Year"]
print(df.head())

df["km_per_year"] = (df["Odometer_km"] / df["Car_Age"])
print(df.head(10))

df["accident_rate"] = df["Accidents"] / df["Odometer_km"]

df["Is_City"] = df["Location_City"].astype(int)
print(df.head(10))

df["LogPrice"] = np.log1p(df["Price"])

# SCALING
dont_scale = {"Price", "LogPrice"}

numeric_cols = df.select_dtypes(
    include=["int64", "float64"]).columns.to_list()

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
print(df[num_features_to_scale].head())

# Final check or final test
print(df.head(10))
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df["Price"].skew())


OUT_PATH = Path(__file__).parent / "clean_car_dataset.csv"

df.to_csv(OUT_PATH, index=False)

print("\nDataset saved successfully!")