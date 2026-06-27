# Name: Mukhtar-kaariye
# Program: Data Preprocessing Pipeline

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

print("=" * 60)
print("STEP 1: LOAD & INSPECT")
print("=" * 60)

# Load dataset
df = pd.read_csv("dataset/raw_car_dataset.csv")

# First 10 rows
print("\nFirst 10 rows")
print(df.head(10))

# Shape
print("\nDataset Shape")
print(df.shape)

# Information
print("\nDataset Information")
df.info()

# Missing values
print("\nMissing Values")
print(df.isnull().sum())

# Value counts for Location
print("\nLocation Value Counts")
print(df["Location"].value_counts(dropna=False))

print("\nInspection Complete.")

# =====================================
# STEP 2: CLEAN TARGET FORMATTING (Price)
# =====================================

print("\n" + "=" * 60)
print("STEP 2: CLEAN TARGET FORMATTING (Price)")
print("=" * 60)

# Display Price before cleaning
print("\nPrice Before Cleaning")
print(df["Price"].head())

# Remove currency symbols and commas
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.replace("USD", "", regex=False)
    .str.strip()
)

# Convert Price to numeric
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# Display Price after cleaning
print("\nPrice After Cleaning")
print(df["Price"].head())

# Data type
print("\nPrice Data Type:")
print(df["Price"].dtype)

# Skewness
print("\nPrice Skewness:")
print(df["Price"].skew())

# =====================================
# STEP 3: FIX CATEGORY ERRORS
# =====================================

print("\n" + "=" * 60)
print("STEP 3: FIX CATEGORY ERRORS")
print("=" * 60)

# Display Location before cleaning
print("\nLocation Before Cleaning")
print(df["Location"].value_counts(dropna=False))

# Convert all text to lowercase and remove extra spaces
df["Location"] = df["Location"].str.strip().str.lower()

# Correct spelling mistakes
df["Location"] = df["Location"].replace({
    "subrb": "suburb",
    "cty": "city",
    "rual": "rural",
    "rurel": "rural",
    "citty": "city"
})

# Convert invalid values to missing
df["Location"] = df["Location"].replace({
    "??": np.nan,
    "unknown": np.nan,
    "": np.nan
})

# Convert names back to title case
df["Location"] = df["Location"].str.title()

# Display Location after cleaning
print("\nLocation After Cleaning")
print(df["Location"].value_counts(dropna=False))

# =====================================
# STEP 4: IMPUTE MISSING VALUES
# =====================================

print("\n" + "=" * 60)
print("STEP 4: IMPUTE MISSING VALUES")
print("=" * 60)

# Missing values before imputation
print("\nMissing Values Before Imputation")
print(df.isnull().sum())

# Fill Odometer_km using the median
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())

# Fill Doors using the mode
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])

# Fill Accidents using the mode
df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])

# Fill Location using the mode
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

# Missing values after imputation
print("\nMissing Values After Imputation")
print(df.isnull().sum())

# =====================================
# STEP 5: REMOVE DUPLICATES
# =====================================

print("\n" + "=" * 60)
print("STEP 5: REMOVE DUPLICATES")
print("=" * 60)

# Shape before removing duplicates
print("\nShape Before Removing Duplicates:")
print(df.shape)

# Count duplicate rows
duplicate_count = df.duplicated().sum()
print("\nNumber of Duplicate Rows:")
print(duplicate_count)

# Remove duplicates
df = df.drop_duplicates()

# Shape after removing duplicates
print("\nShape After Removing Duplicates:")
print(df.shape)

print("\nDuplicates Removed Successfully.")

# =====================================
# STEP 6: OUTLIER HANDLING (IQR CAPPING)
# =====================================

print("\n" + "=" * 60)
print("STEP 6: OUTLIER HANDLING (IQR CAPPING)")
print("=" * 60)

# Function to cap outliers
def cap_outliers(column):

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - (1.5 * IQR)
    upper_bound = Q3 + (1.5 * IQR)

    print(f"\n{column}")
    print("Q1:", Q1)
    print("Q3:", Q3)
    print("IQR:", IQR)
    print("Lower Bound:", lower_bound)
    print("Upper Bound:", upper_bound)

    df[column] = df[column].clip(lower_bound, upper_bound)

    print("\nSummary After Capping")
    print(df[column].describe())


# Apply IQR capping
cap_outliers("Price")
cap_outliers("Odometer_km")

# =====================================
# STEP 7: ONE-HOT ENCODE LOCATION
# =====================================

print("\n" + "=" * 60)
print("STEP 7: ONE-HOT ENCODE LOCATION")
print("=" * 60)

# Convert Location into dummy variables
df = pd.get_dummies(df, columns=["Location"], dtype=int)

# Display the new columns
print("\nNew Columns Created:")
print(df.columns.tolist())

# Show the first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# =====================================
# STEP 8: FEATURE ENGINEERING
# =====================================

print("\n" + "=" * 60)
print("STEP 8: FEATURE ENGINEERING")
print("=" * 60)

# Feature 1: Car Age
df["CarAge"] = 2026 - df["Year"]

# Feature 2: Kilometers driven per year
# Replace 0 with 1 to avoid division by zero
df["Km_per_year"] = df["Odometer_km"] / df["CarAge"].replace(0, 1)

# Feature 3: Urban indicator (1 = City or Suburb, 0 = Rural)
df["Is_Urban"] = (
    (df["Location_City"] == 1) |
    (df["Location_Suburb"] == 1)
).astype(int)

# Alternative target (NOT a feature)
df["LogPrice"] = np.log(df["Price"] + 1)

# Display the new columns
print("\nNew Features:")
print(df[["CarAge", "Km_per_year", "Is_Urban", "LogPrice"]].head())

# =====================================
# STEP 9: FEATURE SCALING (X ONLY)
# =====================================

print("\n" + "=" * 60)
print("STEP 9: FEATURE SCALING (X ONLY)")
print("=" * 60)

# Continuous features to standardize
scale_columns = [
    "Odometer_km",
    "Year",
    "CarAge",
    "Km_per_year"
]

# Create the scaler
scaler = StandardScaler()

# Standardize the selected features
df[scale_columns] = scaler.fit_transform(df[scale_columns])

# Display a sample of the scaled values
print("\nSample of Scaled Features:")
print(df[scale_columns].head())

# Display the mean and standard deviation
print("\nMean of Scaled Features:")
print(df[scale_columns].mean())

print("\nStandard Deviation of Scaled Features:")
print(df[scale_columns].std(ddof=0))

print("\nPrice and LogPrice were NOT scaled.")
print("Location dummy columns and Is_Urban were also left unchanged.")

# =====================================
# STEP 10: FINAL CHECKS & SAVE
# =====================================

print("\n" + "=" * 60)
print("STEP 10: FINAL CHECKS & SAVE")
print("=" * 60)

# Check dataset info
print("\nDataset Info:")
df.info()

# Check missing values (should be 0)
print("\nMissing Values Check:")
print(df.isnull().sum())

# Summary statistics
print("\nDataset Description:")
print(df.describe())

# Save cleaned dataset
df.to_csv("clean_car_dataset.csv", index=False)

print("\nFile saved successfully as clean_car_dataset.csv")
print("Preprocessing pipeline completed successfully.")