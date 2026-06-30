import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

CSV_PATH = 'car_l3_dataset.csv'

df = pd.read_csv(CSV_PATH)


# print(df.head(10))
# print(df.shape)
# print(df.info())
# print(df.isnull().sum())

# print(df["Location"].value_counts(dropna=False))

df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)
# print(df["Price"].head(10))

df["Location"] = df["Location"].replace({"Subrb": "Suburb","??": pd.NA})

# print(df["Location"].value_counts(dropna=False))

df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())

df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])

df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

before = df.shape

df = df.drop_duplicates()

after = df.shape

# print("Before: ", before, "After: ", after)

def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

low_price , high_price = iqr_fun(df["Price"])
low_meter , high_meter = iqr_fun(df["Odometer_km"])

# print("IQR Of Price: ")
# print("low_price: ", low_price, "high_price: ", high_price)

# print("IQR Of mitir: ")
# print("low_meter: ", low_meter, "high_meter: ", high_meter)

df["Price"] = df["Price"].clip(lower=low_price, upper= high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_meter, upper= high_meter)

# print("Price after IQR Clipping")
# print(df["Price"].describe())

df = pd.get_dummies(df, columns=["Location"], drop_first=False).astype(int)

# print("one Hot Encoled of Location: ")
# print([c for c in df.columns if c.startswith("Location")])

CURRENT_YEAR = 2026

df["CarAge"] = CURRENT_YEAR - df["Year"]

df["Km_Per_Year"] = df["Odometer_km"] / df["CarAge"].replace(0, np.nan)

df["Is_Urban"] = df["Location_City"].astype(int)

df["Has_Accident"] = (df["Accidents"]>0).astype(int)

df["LogPrice"] = np.log1p(df["Price"])


# print("After price Log")
# print(df.head())

don_scale = {"Price", "LogPrice"}

numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()

exclude = [c for c in df.columns if c.startswith("Location_")] + ["Is_Urban"]

num_features_to_scale = [c for c in numeric_cols if c not in don_scale and c not in exclude]

scaler = StandardScaler()

df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])

sample_cols = ["Price","LogPrice"]

sample_cols += [c for c in df.columns if c not in sample_cols]

# print(df.head())
# print(df[sample_cols].describe())

OUT_PATH = "clean_car_dataset.csv"
df.to_csv(OUT_PATH)

print("Saved to ", OUT_PATH)



