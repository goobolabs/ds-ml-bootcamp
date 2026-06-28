import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

CSV_PATH = './raw_car_dataset.csv'
df = pd.read_csv(CSV_PATH)

# === INITIAL SNAPSHOT ===
print("\n=== INITIAL HEAD ===")





# 2) 
df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)

# 3) Fix categorical issues BEFORE imputation
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})



# 4) 
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"]  = df["Doors"].fillna(df["Doors"].mode()[0])


df["Location"]  = df["Location"].fillna(df["Location"].mode()[0])

print(df.isnull().sum())

print(df.head(20))

# 5) Remove duplicates
before = df.shape
df = df.drop_duplicates()
after = df.shape
print(f"Dropped duplicates: {before} → {after}")


# 6) IQR capping
def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

low_price, high_price = iqr_fun(df["Price"])
low_Odometer_km,  high_Odometer_km  = iqr_fun(df["Odometer_km"])

df["Price"]     = df["Price"].clip(lower=low_price, upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_Odometer_km,  upper=high_Odometer_km)

# 7) One-hot encode
df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")




# 8) Feature engineering (no leakage)


current_year = 2026


df["CarAge"] = current_year - df["Year"]


df["KmPerYear"] = df["Odometer_km"] / (df["CarAge"] + 1)

df["DoorAccidentRatio"] = df["Doors"] / (df["Accidents"] + 1)

df["Is_City"] = df["Location_City"].astype(int)
df["LogPrice"] = np.log1p(df["Price"])






dont_scale = {"Price", "LogPrice"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
exclude = [c for c in df.columns if c.startswith("Location_")] + ["Is_City"]
num_features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]

scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])

# === FINAL SNAPSHOT ===
print("\n=== FINAL HEAD ===")
print(df.head())

print("\n=== FINAL INFO ===")
print(df.info())

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())
print(df.head(20))
# 10) Save
OUT_PATH = "./clean_car_dataset.csv"
df.to_csv(OUT_PATH, index=False)