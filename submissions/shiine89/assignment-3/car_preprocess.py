"""
Car Price Data Preprocessing Pipeline
========================================
Assignment 3 - DS/ML Bootcamp

This script implements a complete preprocessing pipeline for the raw car dataset.
"""

import pandas as pd
import numpy as np
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# STEP 1: Load & Inspect
# ============================================================================
print("="*70)
print("STEP 1: Load & Inspect")
print("="*70)

# Load the dataset
df = pd.read_csv('dataset/raw_car_dataset.csv')

print(f"\nShape: {df.shape}")
print(f"\nFirst 10 rows:")
print(df.head(10))

print(f"\nData Types Info:")
print(df.dtypes)

print(f"\nMissing Values:")
print(df.isnull().sum())

print(f"\nLocation Value Counts (before cleaning):")
print(df['Location'].value_counts(dropna=False))

print("\n>>> Key Issues Found:")
print("- Price column has currency symbols ($)")
print("- Location has typos like 'Subrb' and unknowns like '??'")
print("- Some missing values in various columns")

# ============================================================================
# STEP 2: Clean Target Formatting (Price)
# ============================================================================
print("\n" + "="*70)
print("STEP 2: Clean Target Formatting (Price)")
print("="*70)

# Function to clean price - remove $ and commas, convert to numeric
def clean_price(price):
    if pd.isna(price):
        return np.nan
    price_str = str(price)
    # Remove $ and commas
    price_str = price_str.replace('$', '').replace(',', '').strip()
    try:
        return float(price_str)
    except:
        return np.nan

df['Price'] = df['Price'].apply(clean_price)

print(f"\nPrice dtype: {df['Price'].dtype}")
print(f"Price skewness: {df['Price'].skew():.4f}")
print(f"\nPrice sample after cleaning:")
print(df['Price'].head(10))

# ============================================================================
# STEP 3: Fix Category Errors before Imputation
# ============================================================================
print("\n" + "="*70)
print("STEP 3: Fix Category Errors before Imputation")
print("="*70)

# Normalize Location text and fix typos
def clean_location(loc):
    if pd.isna(loc):
        return np.nan
    loc = str(loc).strip().title()
    # Fix typos
    if loc in ['Subrb', 'Suburbx', 'Subrbx']:
        return 'Suburb'
    # Convert unknowns to missing
    if loc in ['??', 'Unknown', 'Na', 'N/A', '']:
        return np.nan
    return loc

df['Location'] = df['Location'].apply(clean_location)

print(f"\nLocation Value Counts (after fixing typos):")
print(df['Location'].value_counts(dropna=False))

print(f"\nMissing values after converting unknowns:")
print(df.isnull().sum())

# ============================================================================
# STEP 4: Impute Missing Values (with justification)
# ============================================================================
print("\n" + "="*70)
print("STEP 4: Impute Missing Values")
print("="*70)

print("\n>>> Imputation Justification:")
print("- Odometer_km: Median - robust to outliers")
print("- Doors: Mode - categorical-like (most common is 4)")
print("- Accidents: Mode - discrete count, most common is 0")
print("- Location: Mode - categorical, most common is City")

# Odometer_km: Median imputation
odometer_median = df['Odometer_km'].median()
df['Odometer_km'] = df['Odometer_km'].fillna(odometer_median)
print(f"\nOdometer_km imputed with median: {odometer_median}")

# Doors: Mode imputation
doors_mode = df['Doors'].mode()[0]
df['Doors'] = df['Doors'].fillna(doors_mode)
print(f"Doors imputed with mode: {doors_mode}")

# Accidents: Mode imputation
accidents_mode = df['Accidents'].mode()[0]
df['Accidents'] = df['Accidents'].fillna(accidents_mode)
print(f"Accidents imputed with mode: {accidents_mode}")

# Location: Mode imputation
location_mode = df['Location'].mode()[0]
df['Location'] = df['Location'].fillna(location_mode)
print(f"Location imputed with mode: {location_mode}")

print(f"\nMissing values after imputation:")
print(df.isnull().sum())

# ============================================================================
# STEP 5: Remove Duplicates
# ============================================================================
print("\n" + "="*70)
print("STEP 5: Remove Duplicates")
print("="*70)

shape_before = df.shape[0]
df = df.drop_duplicates()
shape_after = df.shape[0]

print(f"\nShape before removing duplicates: {shape_before} rows")
print(f"Shape after removing duplicates: {shape_after} rows")
print(f"Number of duplicate rows removed: {shape_before - shape_after}")

# ============================================================================
# STEP 6: Outliers (IQR Capping)
# ============================================================================
print("\n" + "="*70)
print("STEP 6: Outliers (IQR Capping)")
print("="*70)

def cap_outliers_iqr(series, column_name):
    """Cap outliers using IQR method"""
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    print(f"\n{column_name}:")
    print(f"  Q1: {Q1:.2f}, Q3: {Q3:.2f}, IQR: {IQR:.2f}")
    print(f"  Lower bound: {lower_bound:.2f}, Upper bound: {upper_bound:.2f}")

    before_min = series.min()
    before_max = series.max()

    capped = series.clip(lower=lower_bound, upper=upper_bound)

    print(f"  Before: min={before_min:.2f}, max={before_max:.2f}")
    print(f"  After:  min={capped.min():.2f}, max={capped.max():.2f}")
    print(f"  Capped values: {((series < lower_bound) | (series > upper_bound)).sum()}")

    return capped

# Apply IQR capping to Price and Odometer_km
df['Price'] = cap_outliers_iqr(df['Price'], 'Price')
df['Odometer_km'] = cap_outliers_iqr(df['Odometer_km'], 'Odometer_km')

print("\n>>> Summary after capping:")
print(df[['Price', 'Odometer_km']].describe())

# ============================================================================
# STEP 7: One-Hot Encode Categorical(s)
# ============================================================================
print("\n" + "="*70)
print("STEP 7: One-Hot Encode Categorical(s)")
print("="*70)

# One-hot encode Location
location_dummies = pd.get_dummies(df['Location'], prefix='Location')
print(f"\nNew columns created from Location encoding:")
print(location_dummies.columns.tolist())

# Add the dummy columns to the dataframe
df = pd.concat([df, location_dummies], axis=1)

print(f"\nSample of Location dummy columns:")
print(df[['Location'] + location_dummies.columns.tolist()].head(5))

# ============================================================================
# STEP 8: Feature Engineering (no leakage)
# ============================================================================
print("\n" + "="*70)
print("STEP 8: Feature Engineering")
print("="*70)

# Feature 1: CarAge - age of the car
current_year = 2026
df['CarAge'] = current_year - df['Year']
print(f"\n1. CarAge = Current Year (2026) - Year")

# Feature 2: Km_per_year - average kilometers per year
# Handle edge case where CarAge could be 0
df['Km_per_year'] = df['Odometer_km'] / df['CarAge'].replace(0, 1)
print(f"2. Km_per_year = Odometer_km / CarAge")

# Feature 3: Is_Urban - binary indicator for urban location
df['Is_Urban'] = (df['Location'] == 'City').astype(int)
print(f"3. Is_Urban = 1 if Location is 'City', else 0")

# Feature 4: LogPrice - log transformation as alternative target (NOT a feature)
df['LogPrice'] = np.log(df['Price'] + 1)
print(f"4. LogPrice = log(Price + 1) - alternative target variable")

print("\n>>> Engineered Features Summary:")
print(df[['CarAge', 'Km_per_year', 'Is_Urban', 'LogPrice']].describe())

# ============================================================================
# STEP 9: Feature Scaling (X only)
# ============================================================================
print("\n" + "="*70)
print("STEP 9: Feature Scaling")
print("="*70)

from sklearn.preprocessing import StandardScaler

# Define continuous features to scale (NOT Price, LogPrice, or dummy columns)
# Only scale: Odometer_km, CarAge, Km_per_year
continuous_features = ['Odometer_km', 'CarAge', 'Km_per_year']

# Create scaler and fit_transform on continuous features
scaler = StandardScaler()
df[continuous_features] = scaler.fit_transform(df[continuous_features])

print(f"\nScaled features: {continuous_features}")
print(f"\nScaled values sample (first 5 rows):")
print(df[continuous_features].head())

print(f"\n>>> Verification - scaled features statistics:")
print(f"Odometer_km - Mean: {df['Odometer_km'].mean():.6f}, Std: {df['Odometer_km'].std():.6f}")
print(f"CarAge - Mean: {df['CarAge'].mean():.6f}, Std: {df['CarAge'].std():.6f}")
print(f"Km_per_year - Mean: {df['Km_per_year'].mean():.6f}, Std: {df['Km_per_year'].std():.6f}")

print("\n>>> Note: Location_* dummy columns (0/1) left unscaled as recommended")

# ============================================================================
# STEP 10: Final Checks & Save
# ============================================================================
print("\n" + "="*70)
print("STEP 10: Final Checks & Save")
print("="*70)

print(f"\nFinal DataFrame Info:")
print(f"Shape: {df.shape}")
print(f"\nColumn names:")
print(df.columns.tolist())

print(f"\nMissing values (should all be zero):")
print(df.isnull().sum())

print(f"\nDescribe table (numeric columns):")
print(df.describe())

# Save the cleaned dataset
output_path = 'submissions/shiine89/assignment-3/clean_car_dataset.csv'
df.to_csv(output_path, index=False)
print(f"\n>>> Cleaned data saved to: {output_path}")

# ============================================================================
# SANITY CHECKS (Recommended Assertions)
# ============================================================================
print("\n" + "="*70)
print("SANITY CHECKS")
print("="*70)

# Check 1: Price is float
assert df['Price'].dtype == np.float64, "Price should be float"
print("[OK] Price is float64")

# Check 2: LogPrice exists and is numeric
assert 'LogPrice' in df.columns, "LogPrice column should exist"
assert pd.api.types.is_numeric_dtype(df['LogPrice']), "LogPrice should be numeric"
print("[OK] LogPrice exists and is numeric")

# Check 3: No missing values (excluding Year/CarAge/Km_per_year which may have NaN)
main_cols = ['Price', 'Odometer_km', 'Doors', 'Accidents', 'Location', 'Is_Urban', 'LogPrice']
assert df[main_cols].isnull().sum().sum() == 0, "No missing values should remain in main columns"
print("[OK] No missing values remain in main columns")

# Check 4: At least one Location_* dummy column exists
location_cols = [col for col in df.columns if col.startswith('Location_')]
assert len(location_cols) > 0, "At least one Location_* dummy column should exist"
print(f"[OK] {len(location_cols)} Location dummy column(s) exist: {location_cols}")

# Check 5: Scaled columns have mean ~ 0 and std ~ 1
for col in continuous_features:
    assert abs(df[col].mean()) < 0.01, f"{col} mean should be ~0"
    assert abs(df[col].std() - 1) < 0.01, f"{col} std should be ~1"
print("[OK] Scaled columns have mean ~ 0 and std ~ 1")

print("\n" + "="*70)
print("PREPROCESSING PIPELINE COMPLETED SUCCESSFULLY!")
print("="*70)