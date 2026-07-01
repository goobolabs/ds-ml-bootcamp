# Reflection – Data Preprocessing Pipeline

## 1. Price Cleaning
I removed currency symbols and commas to convert Price into numeric format. This was necessary for analysis and scaling.

## 2. Missing Values
- Odometer_km → median (robust to outliers)
- Doors & Location → mode (categorical nature)

## 3. Location Fixing
Corrected typos like "Subrb" and replaced unknown values ("??") with NaN before imputation.

## 4. Outliers
Used IQR capping to reduce extreme values in Price and Odometer_km without deleting data.

## 5. Encoding
One-hot encoding was used for Location to convert categorical data into numeric format.

## 6. Feature Engineering
Created:
- CarAge (important for depreciation)
- Km_per_year (usage intensity)
- Is_Urban (city-based indicator)
- LogPrice for normalization of target

## 7. Scaling
StandardScaler was applied only to numerical features (not target variables) to ensure fair model training.

Overall, the pipeline ensures clean, structured, and model-ready data.