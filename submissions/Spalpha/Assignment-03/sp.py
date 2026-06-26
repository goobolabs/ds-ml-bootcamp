
import pandas as pd
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler



CSV_PATH = "raw_car_dataset.csv"
df = pd.read_csv(CSV_PATH)

print (df.head(10))

print (df.shape)

print (df.info())

print ("Missing values :")
print (df.isnull().sum())

print ("show counts of Location")
print (df['Location'].value_counts(dropna=False))

df ["Price"] = df ["Price"].replace(r"[\$,]", "", regex=True).astype(float)
print (df.head(10))


print(df["Price"].skew())


df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})
print(df["Location"].value_counts())


df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])
print(df.isnull().sum())


before = df.shape
df = df.drop_duplicates()
after = df.shape
print ("Before:", before, "After:", after)


def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - (k * iqr)
    upper = q3 + (k * iqr)
    return lower, upper
low_price, high_price = iqr_fun(df["Price"])
low_size, high_size = iqr_fun(df["Odometer_km"])



df = pd.get_dummies(df, columns=["Location"], drop_first=True, dtype="int")
print(df.head(10))



CURRENT_YEAR = 2026
df["car_age"] = CURRENT_YEAR - df["Year"]
df["km/Year"] = df["Odometer_km"] / (df["car_age"] + 1)
df["accident_rate"] = df["Accidents"] / df["Odometer_km"]
print(df.head(10))


df["LogPrice"] = np.log1p(df["Price"])
print(df.head(10))

continuous_features = ["Odometer_km", "car_age", "km/Year", "accident_rate"]


scaler = StandardScaler()
df[continuous_features] = scaler.fit_transform(df[continuous_features])


sample_cols = ["Price", "LogPrice", "Odometer_km", "car_age", "Location_Rural", "Location_Suburb"]
print(df[sample_cols].head(10))


OUR_PATH = "car_l3_clean_ready.csv"
df.to_csv(OUR_PATH, index=False)
PRINT_PATH = "car_l3_clean_ready.csv"
print(f"Final dataset saved to {PRINT_PATH}")
