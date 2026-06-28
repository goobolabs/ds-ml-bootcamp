import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# ============================
# STEP 1 - Load & Inspectclear

# ============================
print("\n========== STEP 1: LOAD & INSPECT ==========\n")

df = pd.read_csv("dataset/row_car_dataset.csv")

print(df.head(10))
print("\nShape:", df.shape)
print("\nInfo:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nLocation Value Counts:")
print(df["Location"].value_counts(dropna=False))

# ============================
# STEP 2 - Clean Price
# ============================
print("\n========== STEP 2: CLEAN PRICE ==========\n")

df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("$","",regex=False)
    .str.replace(",","",regex=False)
)

df["Price"] = pd.to_numeric(df["Price"])

print("Price dtype:",df["Price"].dtype)
print("Price Skewness:",df["Price"].skew())

# ============================
# STEP 3 - Fix Category Errors
# ============================
print("\n========== STEP 3: FIX LOCATION ==========\n")

df["Location"] = df["Location"].replace("Subrb","Suburb")
df["Location"] = df["Location"].replace("??",np.nan)

print(df["Location"].value_counts(dropna=False))
print("\nMissing:")
print(df.isnull().sum())

# ============================
# STEP 4 - Missing Values
# ============================
print("\n========== STEP 4: IMPUTATION ==========\n")

df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())

df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])

df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])

df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

print(df.isnull().sum())

# ============================
# STEP 5 - Remove Duplicates
# ============================
print("\n========== STEP 5: DUPLICATES ==========\n")

before = df.shape

df = df.drop_duplicates()

after = df.shape

print("Before:",before)
print("After :",after)
print("Removed:",before[0]-after[0])

# ============================
# STEP 6 - Outliers (IQR)
# ============================
print("\n========== STEP 6: OUTLIERS ==========\n")

for col in ["Price","Odometer_km"]:

    Q1 = df[col].quantile(.25)
    Q3 = df[col].quantile(.75)

    IQR = Q3-Q1

    lower = Q1-1.5*IQR
    upper = Q3+1.5*IQR

    df[col]=df[col].clip(lower,upper)

print(df[["Price","Odometer_km"]].describe())

# ============================
# STEP 7 - One Hot Encoding
# ============================
print("\n========== STEP 7: ONE HOT ==========\n")

df = pd.get_dummies(df,columns=["Location"],dtype=int)

print(df.columns)

# ============================
# STEP 8 - Feature Engineering
# ============================
print("\n========== STEP 8: FEATURE ENGINEERING ==========\n")

CURRENT_YEAR = 2025

df["CarAge"] = CURRENT_YEAR-df["Year"]

df["Km_per_year"] = df["Odometer_km"]/df["CarAge"].replace(0,1)

urban_cols=[c for c in df.columns if "Location_City" in c or "Location_Suburb" in c]

if urban_cols:
    df["Is_Urban"]=(df[urban_cols].sum(axis=1)>0).astype(int)
else:
    df["Is_Urban"]=0

df["LogPrice"]=np.log(df["Price"]+1)

print(df[["CarAge","Km_per_year","Is_Urban","LogPrice"]].head())

# ============================
# STEP 9 - Scaling
# ============================
print("\n========== STEP 9: SCALING ==========\n")

scale_cols=[
    "Odometer_km",
    "Doors",
    "Accidents",
    "Year",
    "CarAge",
    "Km_per_year"
]

scaler=StandardScaler()

df[scale_cols]=scaler.fit_transform(df[scale_cols])

print(df[scale_cols].head())

# ============================
# STEP 10 - Final Check
# ============================
print("\n========== STEP 10: FINAL ==========\n")

print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

print("\nDescribe")
print(df.describe())

df.to_csv("clean_car_dataset.csv",index=False)

print("\nDataset Saved Successfully!")

# ============================
# Assertions
# ============================

assert df["Price"].dtype=="float64"

assert "LogPrice" in df.columns

assert df.isnull().sum().sum()==0

assert any(col.startswith("Location_") for col in df.columns)

means=df[scale_cols].mean().round()

stds=df[scale_cols].std(ddof=0).round()

print("\nScaled Means")
print(means)

print("\nScaled Std")
print(stds)

print("\nAll Checks Passed Successfully.")