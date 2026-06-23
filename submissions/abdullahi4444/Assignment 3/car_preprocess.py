import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

#1. Load data
df = pd.read_csv("./raw_car_dataset.csv")
print("\n--------HEAD DATA--------\n")
print(df.head(10))
print("\n\n--------INFO DATA--------\n")
print(df.info())
print("\n\n--------MISSING--------\n")
print(df.isnull().sum())
print("\n")

#2. Clean target formatting
print("\n--------CLEAN--------\n")
df["Price"] = (df["Price"].replace(r"[\$,]", "", regex=True).astype(float))
print("\nPrice dtype:")
print(df["Price"].dtype)
print("\nPrice skewness:")
print(df["Price"].skew())
print("\n")

#3. Fix Location
print("\n--------FIX LOCATION--------\n")
df["Location"] = df["Location"].replace({"Subrb": "Suburb","??": pd.NA})
print(df["Location"].value_counts(dropna=False))
print("\n")

#4. Fill missing values
print("\n--------Fill missing values--------\n")
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])
print("\nMissing after imputation:")
print(df.isnull().sum())
print("\n")

#5. Remove duplicates
print("\n--------Remove duplicates--------\n")
before = df.shape
df = df.drop_duplicates()
after = df.shape
print("\nBefore:", before)
print("After:", after)
print("Rows removed:", before[0] - after[0])
print("\n")

# 6. Handle Outliers (IQR Capping)
print("\n-------- Handle Outliers --------\n")
# Make sure columns are numeric
df["Price"] = pd.to_numeric(df["Price"])
df["Odometer_km"] = pd.to_numeric(df["Odometer_km"])
def iqr_bounds(series, k=1.5):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - (k * iqr)
    upper = q3 + (k * iqr)
    return lower, upper
# Calculate bounds
low_p, high_p = iqr_bounds(df["Price"])
low_o, high_o = iqr_bounds(df["Odometer_km"])
# Print bounds
print("Price Bounds:")
print(f"Lower Bound: {low_p}")
print(f"Upper Bound: {high_p}")
print("\nOdometer_km Bounds:")
print(f"Lower Bound: {low_o}")
print(f"Upper Bound: {high_o}")
# Apply IQR capping
df["Price"] = df["Price"].clip(lower=low_p, upper=high_p)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_o, upper=high_o)
# Summary after capping
print("\nSummary after capping:")
print(df[["Price", "Odometer_km"]].describe())
print("\nOutlier handling completed.\n")

#7. One-Hot Encoding
print("\n-------- One-Hot Encoding --------\n")
df = pd.get_dummies(df,columns=["Location"],drop_first=False,dtype="int")
print("\nNew columns:")
print(df.columns)
print("\n")

#8. Create new features
print("\n--------Create new features--------\n")
CURRENT_YEAR = 2026
# Car age
df["CarAge"] = CURRENT_YEAR - df["Year"]
# Safe division
df["Km_per_year"] = (df["Odometer_km"] / df["CarAge"].replace(0, np.nan))
# Accident density
df["Accidents_per_Door"] = (df["Accidents"] / df["Doors"])
# Urban flag
df["Is_Urban"] = (df["Location_City"]).astype(int)
# Alternative target
df["LogPrice"] = np.log1p(df["Price"])
print(df.head())
print("\n")

#9. Feature Scaling
print("\n--------Feature Scaling--------\n")
dont_scale = {"Price","LogPrice"}
numeric_cols = (df.select_dtypes(include=["int64", "float64"]).columns)
exclude = [c for c in df.columns if c.startswith("Location_")]
exclude.append("Is_Urban")
to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]
scaler = StandardScaler()
df[to_scale] = (scaler.fit_transform(df[to_scale]))
print("\nScaled sample:")
print(df[to_scale].head())
print("\n")

#10. Final checks + Save
print("\n-------- Final checks + Save --------\n")
print("\nFINAL INFO")
print(df.info())
print("\nFINAL MISSING")
print(df.isnull().sum())
print("\nDESCRIBE")
print(df.describe())
# Assertions
assert df["Price"].dtype == float
assert "LogPrice" in df.columns
assert df.isnull().sum().sum() == 0
assert any(c.startswith("Location_")for c in df.columns)
# Save
OUT = "./clean_car_dataset.csv"
df.to_csv(OUT,index=False)
print("\nSaved:", OUT)
print("\n")