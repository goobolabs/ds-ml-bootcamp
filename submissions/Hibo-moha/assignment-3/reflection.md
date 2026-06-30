# Reflection

## 1. Data Inspection
I inspected the dataset using head(), shape, info(), and missing value counts. I identified missing values, inconsistent category names, duplicates, outliers, and currency formatting issues in the Price column.

## 2. Price Cleaning
The Price column contained currency symbols and commas. These were removed and the column was converted to numeric format. This ensures proper statistical analysis and modeling.

## 3. Category Cleaning
The Location column contained spelling mistakes such as "Subrb" and invalid values such as "??". These were standardized before imputation to avoid creating incorrect categories.

## 4. Missing Value Imputation
Median was used for Odometer_km because it is robust to outliers. Mode was used for Doors, Accidents, and Location because they are categorical/discrete variables.

## 5. Duplicate Removal
Duplicate rows were removed to prevent bias and repeated information in the dataset.

## 6. Outlier Treatment
IQR capping was applied to Price and Odometer_km. This method reduces the influence of extreme values while preserving all records.

## 7. Encoding
One-hot encoding was used for Location because machine learning algorithms require numerical input.

## 8. Feature Engineering
Three features were created:
- CarAge = Current Year − Year
- Km_per_year = Odometer_km / CarAge
- Is_Urban = 1 for City/Suburb and 0 otherwise

LogPrice was created as an alternative target variable for models that benefit from reduced skewness.

## 9. Scaling
Continuous features were standardized using StandardScaler. Target variables (Price and LogPrice) were not scaled to avoid information leakage.

## 10. Final Validation
Final checks confirmed there were no missing values, encoded columns existed, and scaled features had approximately zero mean and unit variance.