# Car Data Preprocessing Reflection

## Step 1: Load & Inspect
I examined the dataset structure using head, info, and missing value counts to understand data quality issues.

## Step 2: Price Cleaning
Removed currency symbols and commas and converted Price to numeric for modeling compatibility.

## Step 3: Category Fixing
Standardized Location values and converted invalid entries to missing to ensure consistency.

## Step 4: Missing Value Imputation
Used median for numerical variables and mode for categorical variables to reduce bias and preserve distribution shape.

## Step 5: Duplicate Removal
Checked for duplicates and removed redundant rows to avoid training bias.

## Step 6: Outlier Handling
Used IQR capping for Price and Odometer to reduce extreme value distortion while keeping dataset size intact.

## Step 7: Encoding
Applied one-hot encoding to Location to convert categorical data into machine-readable format.

## Step 8: Feature Engineering
Created CarAge, Km_per_year, Is_Urban, and LogPrice to improve predictive power without introducing leakage.

## Step 9: Scaling
Standardized continuous features using StandardScaler to improve model convergence and comparability.

## Step 10: Final Checks
Verified no missing values remained and saved final cleaned dataset for modeling.