import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

CSV_path = 'raw_car_dataset.csv'
df = pd.read_csv(CSV_path)
df.Price = df.Price.replace(r"[\$,]", "", regex=True).astype(float)
df["Location"] = df["Location"].replace({"Subrb":"Suburb", "??":pd.NA})
# print(df["Location"].value_counts(dropna=False))

df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])


before = df.shape

df =df.drop_duplicates()

after = df.shape

def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25,0.75])
    iqr = q3-q1
    lower = q1-k*iqr
    upper = q3+k*iqr
    return lower,upper
low_price, high_price = iqr_fun(df["Price"])
odo_low, odo_high = iqr_fun(df["Odometer_km"])


df = pd.get_dummies(df, columns=["Location"],drop_first=False)

print(df.head())

CURRENT_YEAR = 2026

df["CarAge"] = CURRENT_YEAR - df["Year"]

df["Km_per_year"] = (
    df["Odometer_km"] /
    df["CarAge"].replace(0, 1)
)

df["Is_Urban"] = (
    df["Location_City"] +
    df["Location_Suburb"]
).clip(upper=1)

df["LogPrice"] = np.log1p(df["Price"])
dont_scale = {"Price","LogPrice"}

numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()

exclude = [c for c in df.columns if c.startswith("Location")]+["is_city"]

num_features_to_scale =[c for c in numeric_cols if c not in dont_scale and c not in exclude]

scaler = StandardScaler()


df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])


sample_cols = ["Price","LogPrice"]

sample_cols +=[c for c in df.columns if c not in sample_cols]

OUT_PATH = "processed-car-dataset.csv"

df.to_csv(OUT_PATH)
