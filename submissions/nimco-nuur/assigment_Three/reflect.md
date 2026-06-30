# Reflection

## Missing Values
I used median for Odometer_km because mileage can contain outliers and the median is robust. I used mode for Doors, and Location because they are categorical/discrete variables.

## Category Cleaning
I corrected "Subrb" to "Suburb" and converted "??" into missing values before imputation to avoid treating invalid categories as real values.

## Duplicate Removal
Duplicate rows were removed to prevent repeated observations from biasing the analysis.

## Outlier Handling
I used IQR capping for Price and Odometer_km because it reduces the effect of extreme values while preserving rows.

## Feature Engineering
Three new features were created:
- CarAge = current year − manufacturing year.
- Km_per_year = average annual usage.
- Is_Urban = whether the car is located in a city.

LogPrice was created as an alternative target because price distribution is skewed.

## Scaling
Only continuous features were standardized. Price and LogPrice were not scaled because they are target variables. One-hot encoded columns were left unchanged.