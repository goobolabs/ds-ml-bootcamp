import pandas as pd
import numpy as np
from  sklearn.preprocessing import StandardScaler



# step 1: load and inspect
csv_file_path = "raw_car_dataset.csv"
df = pd.read_csv(csv_file_path)
print("=============step 1: load and inspect============")
print(df.head(10))

print("\n shape:" ,df.shape)
print("\n info:")
df.info()
print("missing values")
print(df.isnull().sum())
print("\nLocation value counts:")
print(df["Location"].value_counts(dropna=False))
print("\nKey issues found:")
print("- Missing values")
print("- Duplicate rows")
print("- Price contains $ and commas")
print("- Location has typos (Subrb)")
print("- Unknown values ??")
print("- Possible outliers")

# STEP 2: CLEAN TARGET (PRICE)
print("\n========== STEP 2: CLEAN PRICE ==========")
df["Price"] = df["Price"].replace(r'[/$,]' ,"" ,regex = True).astype(float)
# print(df.head(10))

print("Price data type",df["Price"].dtype)

print("Price skewness",df["Price"].skew())
# STEP 3: Fix Category Errors before Imputation

print("=========Fix Category Errors before Imputation")
df["Location"] = df["Location"].replace({"Subrb":"Suburb","??" :pd.NA})
print(df["Location"].value_counts(dropna=False))

# step4:Impute Missing Values (justify choices)
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])


print("Missing values after imputation:")
print(df.isnull().sum())
# REMOVE DUPLICATES

print("\n========== STEP 5: REMOVE DUPLICATES ==========")
before = df.shape
df.drop_duplicates()
after = df.shape
print("Before:", before)
print("After :", after)
print("Rows removed:", before[0] - after[0])
# STEP 6: IQR OUTLIER CAPPING
print("\n========== STEP 6: OUTLIER CAPPING ==========")
def iqr_cap(series,k=1.5):
    q1,q3 = series.quantile([0.25,0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k *iqr
    return lower,upper
low_price,high_price = iqr_cap(df["Price"])
low_Odometer_km,high_Odometer_km = iqr_cap(df["Odometer_km"])

print("iqr price")
print("low price",low_price,"high price",high_price)
print("low_Odometer_km: ",low_Odometer_km,"high_Odometer_km: ",high_Odometer_km)
df["Price"] = df["Price"].clip(lower=low_price,upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_Odometer_km,upper=high_Odometer_km)
print("\nSummary after capping:")
print(df[["Price", "Odometer_km"]].describe())

# step 7:One-Hot Encode Categorical(s)
print("\n========== STEP 7: ONE HOT ENCODING ==========")
df = pd.get_dummies(df,columns=["Location"] ,drop_first=False,dtype=int)
location_cols = [c for c in df.columns if c.startswith("Location")]
print("created columns")
print(location_cols)
#STEP 8: FEATURE ENGINEERINg
print("\n========== STEP 8: FEATURE ENGINEERING ==========")
# carAge
CURRENT_YEAR = 2026
df["CarAge"] =   CURRENT_YEAR -  df["Year"] 
## Km_per_year
df["Km_per_year"] = df["Odometer_km"] / np.maximum(df["CarAge"],1)
#is urban
df["Is_Urban"] = df["Location_City"].astype(int)
df["LogPrice"] = np.log1p(df["Price"])

print(df[[
    "CarAge",
    "Km_per_year",
    "Is_Urban",
    "LogPrice"
]].head())


#FEATURE SCALING 
print("\n========== STEP 9: FEATURE SCALING ==========")


dont_scale = {"Price","LogPrice"}
num_cols = df.select_dtypes(include= ["int64","float64"]).columns.to_list()
exclude_cols = [c for c in df.columns if c.startswith("Location")] + ["Is_Urban"]
num_features_to_scale = [c for c in num_cols if c not in dont_scale and c not in exclude_cols]
scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])

print(df.head(10))
print("\n========== STEP 10: FINAL CHECK ==========")

print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDescribe:")
print(df.describe())
OUTPUT_CSV_PATH= "clean_car_dataset.csv"

df.to_csv(OUTPUT_CSV_PATH)
print("\nSaved successfully as" , OUTPUT_CSV_PATH)