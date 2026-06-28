import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# STEP 1: LOADING & INSPECTING THE DATASET
CSV_PATH = 'raw_car_dataset.csv'
df = pd.read_csv(CSV_PATH)

# print("INITIAL HEAD OF DATA:")
# print(df.head(10))

# print(" INITIAL MISSING VALUES ")
# print(df.isnull().sum())

# STEP 2: CLEAN TARGET FORMATTING
df["Price"] = df["Price"].replace(r"[ \$, ]", "", regex=True).astype(float)
print(df["Price"].head(10))
print(df["Price"].skew())

# STEP 3: FIX CATEGORY ERRORS BEFORE IMPUTATION 
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})
print("Location value counts after Type/unkown: ")
print(df["Location"].value_counts(dropna=False))

# STEP 4: MISSING VALUES === Filling holes with Median for numbers and Mode for categories
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])
print(df.isnull().sum())

# STEP 5: REMOVE DUPLICATES 
before = df.shape
df = df.drop_duplicates()
after = df.shape
print(f" Dropped duplicates: {before} → {after}")

# STEP 6: OUTLIERS
def iqr_fun(series, k = 1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

low_price, high_price = iqr_fun(df["Price"])
low_Odometer_km, high_Odometer_km = iqr_fun(df["Odometer_km"])
# print("IQR OF PRICE: ")
# print( "low_price: ", low_price, "high_price: ", high_price)
# print("IQR OF ODOMETER_KM: ")
# print( "low_Odometer_km: ", low_Odometer_km, "high_Odometer_km: ", high_Odometer_km)

df["Price"] = df["Price"].clip(lower = low_price, upper = high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower = low_Odometer_km, upper = high_Odometer_km)

print("PRICE AFTER IQR CAPPING: ")
print(df["Price"].describe())

# STEP 7: ONE-HOT ENCODE == *Turning city/suburb names into 0 and 1 columns*
df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")
print("COLUMNS AFTER ONE-HOT ENCODING: ")   
print([c for c in df.columns if c.startswith("Location")])
print(df.head(10))

# STEP 8: FEATURE ENGINEERING 
CURRENT_YEAR = 2026

# Feature 1: CarAge
df["CarAge"] = CURRENT_YEAR - df["Year"]
# print(df.head())

# Feature 2: Accidents_per_year (using +1 to avoid division by zero)
df["Accidents_per_year"] = df["Accidents"] / (df["CarAge"] + 1)

print(df[["Accidents", "CarAge", "Accidents_per_year"]].head(10))

# Feature 3: Km_per_year
df["Km_per_year"] = df["Odometer_km"] / (df["CarAge"] + 1)

print(df[["Odometer_km", "CarAge", "Km_per_year"]].head(10))

# Feature 4: Is_City
df["Is_City"] = df["Location_City"].astype(int)
print(df.head(5))

# Alternative Target: LogPrice
df["LogPrice"] = np.log1p(df["Price"])
print(df.head(5))

# STEP 9: FEATURE SCALING (X ONLY)
dont_scale = {"Price", "LogPrice"}

# Finding all number columns
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()

# Protecting 0/1 dummies and the target
exclude = [ c for c in df.columns if c.startswith("Location ")]+["Is_City"]
num_features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]

scaler = StandardScaler() 
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])

print("SCALED NUMERIC FEATURES: ")
print(df.head)

# STEP 10: FINAL SNAPSHOT & SAVE 
print(" FINAL HEAD ")
print(df.head(10))

print(" FINAL MISSING VALUES ")
print(df.isnull().sum())

# Saving the clean car dataset
OUT_PATH = "car-clean-dataset.csv"
df.to_csv(OUT_PATH)
print("Clean dataset Saved to {OUT_PATH}")