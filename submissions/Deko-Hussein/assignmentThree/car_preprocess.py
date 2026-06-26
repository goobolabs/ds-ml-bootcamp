# 1.Load & Inspect
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("submissions/Deko-Hussein/assignmentThree/raw_car_dataset.csv")

print("\n=== the head(10) ====")
print(df.head(10))

print("\n=== the shape of dataset is:===")
print(df.shape)
print("the information of dataset is:")
print(df.info())
print("\n=== the missing count of data set is ===")
print(df.isnull().sum())
print("\n== Location value counts ===")
print(df["Location"].value_counts(dropna=False))

# 2.Clean Target Formatting (Price)
# print("\n ===Remove currency symbols and commas; ensure the column is numeric==:")
df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)
print("\n=== PRICE CHECK ===")
print("Price dtype:", df["Price"].dtype)
print("Price skewness:", df["Price"].skew())

# 3. Fix Category Errors before Imputation

df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})
print("\n=== LOCATION AFTER CLEANING ===")
print(df["Location"].value_counts(dropna=False))
# 4.Impute Missing Values (justify choices)
df["Odometer_km"] =df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])
print("\n=== MISSING COUNTS AFTER IMPUTATION ===")
print(df.isnull().sum())

#5. Remove Duplicates

print("\nShape before duplicates:", df.shape)
df = df.drop_duplicates()
print("Shape after duplicates:", df.shape)
print("Rows removed:", len(df))

#6. Outliers (IQR capping)
def iqr_cap(col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df[col] = np.clip(df[col], lower, upper)

iqr_cap("Price")
iqr_cap("Odometer_km")
print("\n=== AFTER IQR CAPPING SUMMARY ===")
print(df[["Price", "Odometer_km"]].describe())

#7. One-Hot Encode Categorical(s)

df = pd.get_dummies(df, columns=["Location"], drop_first=False)

location_cols = [c for c in df.columns if "Location_" in c]

print("\n=== LOCATION DUMMY COLUMNS ===")
print(location_cols)

#8. Feature Engineering 
current_year = 2026

df["CarAge"] = current_year - df["Year"]
df["Km_per_year"] = df["Odometer_km"] / (df["CarAge"] + 1)

df["Is_Urban"] = df["Location_Urban"].astype(int) if "Location_Urban" in df.columns else 0

df["LogPrice"] = np.log1p(df["Price"])

print("\n=== NEW FEATURES SAMPLE ===")
print(df[["CarAge", "Km_per_year", "LogPrice"]].head())

# 9. FEATURE SCALING (X ONLY)
num_cols = ["Odometer_km", "CarAge", "Km_per_year"]

scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

print("\n=== SCALED SAMPLE ===")
print(df[num_cols].head())

# 10. FINAL CHECKS & SAVE
print("\n=== FINAL INFO ===")
print(df.info())

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum().sum())

assert df["Price"].dtype == "float64"
assert "LogPrice" in df.columns
assert df.isnull().sum().sum() == 0
assert any("Location_" in c for c in df.columns)


OutputPath = "submissions/Deko-Hussein/assignmentThree/dataset/car_dataset.csv"
df.to_csv(OutputPath)
print("Saved to:", OutputPath)



