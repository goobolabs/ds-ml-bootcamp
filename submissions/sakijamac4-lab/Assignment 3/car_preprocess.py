import pandas as pd
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler


 

CSV_PATH = r'C:\Users\SAKARIYE JAMA\Desktop\new\dataset\raw_car_dataset.csv'
df = pd.read_csv(CSV_PATH)

     #Q1
# print("\n=== INITIAL HEAD ===")
# print(df.head(10))
# print("\n=== shape  ===")
# print(df.shape)
# print("\n=== INITIAL INFO ===")

# print(df.info())

# print("\n=== INITIAL MISSING VALUES ===")
# print(df.isnull().sum())

# print(df["Location"].value_counts())

                  # Q2
# print(df["Price"].value_counts())
# # 2) Clean price formatting
df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)

# print(df["Price"].value_counts())

            #   Q3
# 3) Fix categorical issues BEFORE imputation
print(df["Location"].value_counts())
print(df["Location"].isnull().sum())
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})
print(df["Location"].value_counts())
print(df["Location"].isnull().sum())

        #   Q4
# 4) Impute missing values
# print("\n=== MISSING VALUES BEFORE IMPUTATION ===")
# print(df["Doors"].isnull().sum() )
# print(df["Odometer_km"].isnull().sum() )
# print(df["Location"].isnull().sum() )

df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])

df["Odometer_km"]  = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Location"]  = df["Location"].fillna(df["Location"].mode()[0])
print("\n=== MISSING VALUES AFTER IMPUTATION ===")
# print(df["Doors"].isnull().sum() )
# print(df["Odometer_km"].isnull().sum() )
# print(df["Location"].isnull().sum() )

     # # Q5

# 5) Remove duplicates

before = df.shape
df = df.drop_duplicates()
after = df.shape
print(f"Dropped duplicates: {before} → {after}")
         ## 6
         # Xariiqdan ku dar KAHOR iqr_fun

# print("\n=== before IQR ===")
# print(df["Price"].describe())

# print(df["Odometer_km"].describe())

def iqr_fun(series, k=1.5):
     q1, q3 = series.quantile([0.25, 0.75])
     iqr = q3 - q1
     lower = q1 - k * iqr
     upper = q3 + k * iqr
     return lower, upper

low_price, high_price = iqr_fun(df["Price"])
low_odometer,  high_odometer  = iqr_fun(df["Odometer_km"])

df["Price"]     = df["Price"].clip(lower=low_price, upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_odometer,  upper=high_odometer)
# print("\n=== after IQR ===")

# print(df["Price"].describe())

# print(df["Odometer_km"].describe())

     #q7

# 7) One-hot encode
df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")
print([c for c in df.columns if "Location_" in c])
# print(df.head(10))

# 8) Feature engineering (no leakage)
CURRENT_YEAR = 2026

df["CarAge"] = CURRENT_YEAR - df["Year"]
df["Is_Urban"] = ((df["Location_City"] == 1) | (df["Location_Suburb"] == 1)).astype(int)
df["Km_per_year"] = df["Odometer_km"] / df["CarAge"]
df["LogPrice"] = np.log1p(df["Price"])

# print(df.head(10))
# print(df.shape)
# print(df.info())


dont_scale = {"Price", "LogPrice"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
exclude = [c for c in df.columns if c.startswith("Location_")] + ["Is_Urban"]
num_features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]
scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])
# print(df.head(10))
# print(df.shape)
# print(df.info())
print("\n=== FINAL HEAD ===")
print(df.head())

print("\n=== FINAL INFO ===")
print(df.info())

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())

# 10) Save

OUT_PATH = r'C:\Users\SAKARIYE JAMA\Desktop\new\dataset\clean_car_dataset.csv'
df.to_csv(OUT_PATH, index=False)