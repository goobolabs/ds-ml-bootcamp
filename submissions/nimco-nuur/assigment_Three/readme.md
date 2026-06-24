 Car Dataset Preprocessing Project
 Overview

This project cleans and prepares a raw car dataset for machine learning. It includes data inspection, cleaning, feature engineering, outlier handling, encoding, and scaling.

Dataset Description

The dataset contains information about used cars:

Price (target variable)
Odometer_km (mileage)
Doors (number of doors)
Accidents (number of accidents)
Location (City, Suburb, Rural)
Year (manufacturing year)
 Data Cleaning Steps
1. Load & Inspect
Checked dataset shape, info, and missing values
Identified inconsistent formats and typos
2. Price Cleaning
Removed $ and ,
Converted Price to numeric (float)
3. Fixing Categories
Standardized Location values (e.g., Subrb → Suburb)
Converted invalid values (??) to NaN
4. Missing Values Imputation
Odometer_km → median
Doors → mode
Accidents → mode
Location → mode
5. Duplicate Removal
Removed duplicate rows to ensure data quality
 Outlier Handling (IQR Capping)
Used IQR method to detect outliers
Applied clipping to Price and Odometer_km
Reduced effect of extreme values without deleting data
Feature Engineering

Created new features:

CarAge = 2026 - Year
Km_per_year = Odometer_km / CarAge
Is_Urban (City = 1, others = 0)
LogPrice = log(Price + 1)
 Feature Scaling
Applied StandardScaler to numeric features
Kept target variable (Price, LogPrice) unchanged
 Output

Final cleaned dataset saved as:

clean_car_dataset.csv
Key Insights
Dataset is highly skewed (many low prices)
Outliers exist in Price and Odometer_km
IQR capping improved data stability
Missing values handled using statistical methods
 Requirements
pandas
numpy
scikit-learn
Goal

To prepare a clean, structured dataset ready for machine learning models to predict car prices accurately.