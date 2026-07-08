# Reflection

## Step 1: Load and Inspect
I first loaded the dataset and inspected it using head(), shape, info(), missing values, and value counts. This helped identify missing values, duplicate rows, inconsistent category names, and formatting issues in the Price column.

## Step 2: Clean Target Formatting
The Price column contained currency symbols and commas. I removed these characters and converted the column to float so that numerical analysis could be performed correctly.

## Step 3: Fix Category Errors
The Location column contained inconsistent values such as "Subrb" and "??". I corrected spelling mistakes and converted unknown values to missing values before imputation.

## Step 4: Impute Missing Values
I used the median for Odometer_km because it is less affected by outliers. I used the mode for Doors, Accidents, and Location because they are categorical or discrete variables.

## Step 5: Remove Duplicates
Duplicate rows were removed to improve data quality and prevent repeated information from affecting the analysis.

## Step 6: Handle Outliers
I used the IQR method to identify outliers and clipped extreme values instead of deleting rows. This preserves the dataset while reducing the effect of extreme observations.

## Step 7: One-Hot Encoding
The Location column was converted into dummy variables so that machine learning algorithms can process categorical data.

## Step 8: Feature Engineering
I created new features including CarAge, Km_per_year, Is_Urban, and LogPrice. These features provide additional useful information while avoiding data leakage.

## Step 9: Feature Scaling
I standardized only the continuous input features using StandardScaler. I did not scale Price or LogPrice because they are target variables.

## Step 10: Final Check
Finally, I confirmed that there were no missing values remaining, verified the dataset structure, and saved the cleaned dataset as clean_car_dataset.csv.