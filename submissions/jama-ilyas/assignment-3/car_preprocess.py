import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("dataset/raw_car_dataset.csv")
print(df.head(10))
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df['Location'].value_counts())
df.isnull().sum()

# Step 2: Clean Price
df["Price"] = df["Price"].astype(str)
df["Price"] = df["Price"].str.replace("$", "", regex=False)
df["Price"] = df["Price"].str.replace(",", "", regex=False)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

print(df["Price"].dtype)
print(df["Price"].skew())
print(df[["Price"]].head(10))

# Step 3: Fix Location category errors


df["Location"] = df["Location"].astype(str).str.strip()
df["Location"] = df["Location"].replace({
    "Subrb": "Suburb",
    "CITY": "City",
    "city": "City",
    "subUrban": "Suburb"
})

df["Location"] = df["Location"].replace({
    "": np.nan,
    "nan": np.nan,
    "??": np.nan,
    "unknown": np.nan,
    "Unknown": np.nan,
    "N/A": np.nan
})

# result
print(df["Location"].value_counts(dropna=False).to_string())
print("Total:", df["Location"].value_counts(dropna=False).sum())
print("Unique values:", df["Location"].unique())

# Step 4: Handle Missing Values / Imputation

df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())

df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])

df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

# Check missing values again
print(df.isnull().sum())

# Step 5: Remove duplicate rows
before = df.shape
duplicate_count = df.duplicated().sum()
df = df.drop_duplicates()
after = df.shape

# Print results
print("Shape before:", before)
print("Duplicate rows:", duplicate_count)
print("Shape after:", after)
print("Rows removed:", before[0] - after[0])

# Step 6: IQR Capping for Outliers

def iqr_cap(df, column_name):
    # Before capping
    print(f"\nBefore capping {column_name}:")
    print(df[column_name].describe())

    # Calculate Q1, Q3, and IQR
    Q1 = df[column_name].quantile(0.25)
    Q3 = df[column_name].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    print(f"{column_name} Q1:", Q1)
    print(f"{column_name} Q3:", Q3)
    print(f"{column_name} IQR:", IQR)
    print(f"{column_name} Lower Bound:", lower_bound)
    print(f"{column_name} Upper Bound:", upper_bound)

    outliers_before = ((df[column_name] < lower_bound) | (df[column_name] > upper_bound)).sum()
    print(f"{column_name} Outliers before capping:", outliers_before)

    df[column_name] = df[column_name].clip(lower=lower_bound, upper=upper_bound)

    outliers_after = ((df[column_name] < lower_bound) | (df[column_name] > upper_bound)).sum()
    print(f"{column_name} Outliers after capping:", outliers_after)
    print(f"\nAfter capping {column_name}:")
    print(df[column_name].describe())

    return df

df = iqr_cap(df, "Price")
df = iqr_cap(df, "Odometer_km")
# Step 7: One-Hot Encode Location

df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype=int)

print("New columns after encoding:")
print(df.columns)
# Step 8: Feature Engineering

current_year = 2026

df["CarAge"] = current_year - df["Year"]

df["Km_per_year"] = df["Odometer_km"] / df["CarAge"].replace(0, 1)

df["Is_Urban"] = df["Location_City"]

df["LogPrice"] = np.log(df["Price"] + 1)

print(df[["Year", "CarAge", "Odometer_km", "Km_per_year", "Is_Urban", "Price", "LogPrice"]].head())
# Step 9: Feature Scaling


scaler = StandardScaler()

columns_to_scale = ["Odometer_km", "CarAge", "Km_per_year"]

df[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])

print(df[columns_to_scale].head())
# Step 10: Final Checks and Save

print(df.info())
print(df.isnull().sum())
print(df.describe())

df.to_csv("dataset/clean_car_dataset.csv", index=False)

print("Clean dataset saved successfully!")
