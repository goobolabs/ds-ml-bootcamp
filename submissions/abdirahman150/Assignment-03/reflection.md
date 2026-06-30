# Practical Assignment: Data Preprocessing Pipeline

## Clean Target Formatting (Price)

I removed currency symbols ($) and commas (,) from the Price column and converted it to a numeric type. I also checked its skewness to determine whether transformation was needed.

## clean categorical issues imputation

I corrected spelling errors in the Location column and replaced unknown values (??) with missing values to improve data consistency.

## fix imputation missing values

I used different imputation methods based on my data type.

1. Odometer_km: Median, because it is less affected by outliers.
2. Doors: Mode, since it is a discrete feature.
3. Accidents: Mode, to preserve the most common category.
4. Location: Mode, because it is a categorical feature.

## Remove Duplicates

Duplicate rows were removed to improve data quality and prevent repeated observations from affecting the model.

## Outliers (IQR Capping)
IQR Capping: is an Outlier treatment technique that limits extreme values instead of removing them.

I applied IQR capping to Price and Odometer_km to reduce the effect of extreme values while keeping all records.

## Feature Engineering

I created four new features:

1. CarAge: Vehicle age.
2. Km_per_year: Average yearly mileage.
3. Is_Urban: Indicates whether the location is urban.
4. LogPrice: Reduces target skewness for better model performance.

## One-Hot Encode Categorical(s)

I applied one-hot encoding to the Location column, converting categories into binary variables for machine learning.

## Feature Scaling

I standardized continuous numerical features using StandardScaler while leaving binary columns and target variables unchanged.

## Final Checks & Save

Finally, I verified that the dataset contained no missing values, confirmed the correct data types, and saved the cleaned dataset as clean_car_dataset.csv


## Prepared by:
Abdirahman khadar mohamed