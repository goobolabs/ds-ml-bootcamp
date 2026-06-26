#Import libraries
import pandas as pd
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

#step1: Load EDA
df = pd.read_csv("raw_car_dataset.csv")

#inspect Data
print("==Head==")
print(df.head())
print("==Info==")
print(df.info())
print("==Describe==")
print(df.describe())
print("==Null Values==")
print(df.isnull().sum())
print("==Duplicates==")
print(df.duplicated().sum())
print("==Columns==")
print(df["Location"].value_counts())


#step2: clean target variable
df["Price"] = df["Price"].str.replace(r"[\$,]", "", regex=True).astype(float)
# print("==Price Column Cleaned==")
# print(df["Price"].head(10))

#step3: clean categorical issues imputation
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})
print("==after clean==")
print(df["Location"].value_counts(dropna=False))

#step4: fix imputation missing values
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

print("==after fix")
print(df.isnull().sum())
print(df["Location"].value_counts(dropna=False))

#step5: Remove Duplicates
before = df.shape
df = df.drop_duplicates()
after = df.shape

print("==After drop duplicates==")
print("before:", before, "after:", after)

#step5: Outliers (IQR capping)
def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])

    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper
low_price, high_price = iqr_fun(df["Price"])
low_km, high_km = iqr_fun(df["Odometer_km"])

print("==after use IQR==")
print("low_price:", low_price, "high_price:", high_price)
print("low_km:", low_km, "high_km:", high_km)


df["Price"] = df["Price"].clip(lower = low_price, upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_km, upper=high_km)

print("==price after iqr capping==")
print(df["Price"].describe())


#step6: Feature Engineering
CURRUNT_YEAR = 2026
df["CarAge"] = CURRUNT_YEAR - df["Year"]

df["Km_Per_Year"] = df["Odometer_km"] / df["CarAge"].replace(0, 1)

df["Is_Urban"] = df["Location"].isin(["City", "Suburb"]).astype(int)

df["LogPrice"] = np.log1p(df["Price"])

print("==after feature ENG==")
print(df[["CarAge", "Km_Per_Year", "Is_Urban", "LogPrice"]].head())
print(df.columns)
print(df[["Year", "CarAge"]].head(10))

#step7: One-hot Encoding
df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")

print("== after one-hot encoding==")
print(df.head(10))

#step8: Feature Scaling
dont_scale = {"Price", "LogPrice"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
exclude = [ c for c in df.columns if c.startswith("Location")] + ["Is_Urban"]
num_feature_scale = [ c for c in numeric_cols if c not in dont_scale and c not in exclude]

scaler = StandardScaler()
df[num_feature_scale] = scaler.fit_transform(df[num_feature_scale])

print("==Final Snapshot==")
print(df.head())
print(df.info())

#step8: Clean Data Saving
OURPATH = "clean_car_dataset.csv"
df.to_csv(OURPATH)

print("Saved to:", OURPATH)