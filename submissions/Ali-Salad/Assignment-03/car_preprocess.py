import pandas as pd 
import numpy as np
from sklearn.preprocessing import StandardScaler

CSV_PATH = './Dataset/raw_car_dataset.csv'
df = pd.read_csv(CSV_PATH)

print("\n =======INITIAL HEAD========")
print(df.head(10))

print("\n =======INITIAL info========")
print(df.info())

print(df["Location"].value_counts(dropna=False))

print("\n=====missing values====")
print(df.isnull().sum())

print("\n =====clean target =====")
df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)

print(df.value_counts())

print("\n ====fixed categoral errors before imputation=====")
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})
print("Location Counts after fixed type/unkown")
print(df["Location"].value_counts(dropna=False))

# print("\n====impute misiing values=====")
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

print("\n =====removing duplicates =====")
before = df.shape
df = df.drop_duplicates()
after = df.shape

print("before :", before)
print("after:", after)
print("removed:", before[0]-after[0])

print("\n ===IQR Capping======")
def iqr_fun(series, k=1.5):
    q1,q3 = series.quantile([0.25, 0.75])
    iqr = q3 -q1
    lower = q1-k*iqr
    upper = q3 + k *iqr
    return lower, upper

low_price, high_price = iqr_fun(df["Price"])
low_Odometer_km, high_Odometer_km = iqr_fun(df["Odometer_km"])

print("\n low_price, high price")
print(f"low_price:{low_price}")
print(f"high_price:{high_price}")

print("\n low_Odometer_km, high_Odometer_km")
print(f"low_Odometer_km:{low_Odometer_km}")
print(f"high_Odometer_km:{high_Odometer_km}")


df["Price"] = df["Price"].clip(lower=low_price, upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_Odometer_km, upper=high_Odometer_km)

print("\n summery after capping ")
print(df[["Price", "Odometer_km"]].describe())
print("\n outlier handiling is complete")


print("\n =====one hot encoding======")
df = pd.get_dummies(df, columns=["Location"],drop_first=False, dtype="int")

print("\n ====feature engineering=======")
CURRENT_YEAR= 2026
df["CarAge"]= CURRENT_YEAR-df["Year"]
df["Km_per_year"]= df["Odometer_km"]/df["CarAge"].replace(0,np.nan)
df["Accident_per_door"]= df["Accidents"]/df["Doors"]
df["Is_Urban"] = (df["Location_City"]).astype(int)
df["LogPrice"] = np.log1p(df["Price"])

print(df.head())

print("\n")


dont_scale = {"Price","LogPrice"}
numeric_cols = (df.select_dtypes(include=["int64", "float64"]).columns)

exclude = [
    c for c in df.columns
    if c.startswith("Location_")
]
exclude.append("Is_Urban")
to_scale = [
    c for c in numeric_cols
    if c not in dont_scale
    and c not in exclude
]
scaler = StandardScaler()
df[to_scale] = (scaler.fit_transform(df[to_scale]))

print("\nScaled sample:")
print(df[to_scale].head())

print("\n =====final cheks  and save=====")
print("\n ====final head====")
print(df.head())

print("\n =====final info=====")
print(df.info())

print("\n =====final describe=====")
print(df.describe())

print("\n====final mising values======")
print(df.isnull().sum())


print("\n=====saving======")
OUT = "./clean_car_dataset.csv"
df.to_csv(OUT, index=False)




