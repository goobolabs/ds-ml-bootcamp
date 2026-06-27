import pandas as pd
import numpy as np 
from sklearn.preprocessing import StandardScaler
print
csv_path ="raw_car_dataset.csv"
df = pd.read_csv(csv_path)

# 1) ==== initial snapshot =====

# print("\n=== initial head===")

# print(df.head())


# print("\n=== initial info===")

# print(df.info())

# print("\n=== initial missing values===")

# print(df.isnull().sum())

# 2) clean target formating

df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float) 

# ("\n=== after formating  head===")

# print(df.head(50))

# 3) fix  categorical issues before imputtion

df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})

# print(df.tail(40))


# 4) immpute missing values


df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0]).astype("Int64")
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

print("\n=== after filling  missing values===")

print(df.isnull().sum())


print("\n=== after impution info===")

print(df.info())

print("\n=== after formating  head===")

print(df.head())


# 5) remove duplicates 

before = df.shape

df = df.drop_duplicates()

after = df.shape

print(f"removed duplicates: {after} {before}")

# 6) IQR capping

def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr =  q3 - q1
    lower= q1 - k * iqr
    upper= q3 + k * iqr
    return lower, upper


low_Price, high_Price = iqr_fun(df["Price"])
low_km, high_km = iqr_fun(df["Odometer_km"])

df["Price"] = df["Price"].clip(lower=low_Price, upper=high_Price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_km, upper= high_km)

print(df.head(50))

# 7 ) one hot encode
df = pd.get_dummies(df, columns=["Location"],drop_first=False,dtype="int")

print("\n=== after one hot encode info===")

print(df.info())

print(df.head())

# 8) feature engeneering 

current_year = 2026

df["Car_Age"] = current_year - df["Year"]

df["Km_per_Year"] = df["Odometer_km"] / (df["Car_Age"] + 1)


df["IS_City"] = df["Location_City"].astype(int)
df["LogPrice"] = np.log1p(df["Price"])

print(df.info())
print(df.head())

# 9) future scaling (x only ; keep targets and dumies unscaled)

dont_scale = {"Price" , "LogPrice"}

numeric_cols = df.select_dtypes(include=["number"]).columns.to_list()
exclude = [c for c in df.columns if c.startswith("Location") ] + ["IS_City"]
num_futures_to_scale = [c for c in numeric_cols if c not in dont_scale and  c not in exclude]


scaler = StandardScaler()
df[num_futures_to_scale] = scaler.fit_transform(df[num_futures_to_scale])


print(df[num_futures_to_scale].head)



# final check
print(df.head(10))
print(df.info())
print(df.describe())
print(df.isnull().sum())







# 10) save 

OUT_PATH = "./practice/car_l3_clean_ready.csv"

df.to_csv("car_l3_clean_ready.csv")
