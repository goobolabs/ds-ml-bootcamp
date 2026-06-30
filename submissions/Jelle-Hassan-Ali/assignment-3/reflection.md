# Car Dataset Preprocessing Reflection

## 1. Missing Values
I handled missing values using median for numerical columns (Odometer_km, Doors) because median is robust to outliers. For categorical data (Location), I used mode since it preserves the most common category.

## 2. Data Cleaning
Location inconsistencies such as "Subrb" and "??" were corrected or replaced with missing values before imputation. This ensured consistent categorical encoding later.

## 3. Duplicate Removal
Duplicates were removed to prevent bias in model training and ensure each observation represents a unique car listing.

## 4. Outlier Handling
I used IQR capping for Price and Odometer_km. This method reduces extreme outlier influence while preserving data distribution better than removing rows.

## 5. Feature Engineering
I created:
- CarAge: to represent vehicle age from year
- Km_per_year: to normalize usage over time
- Is_Urban: simplified urban/rural grouping
- LogPrice: reduced skewness in target variable

## 6. Encoding
One-hot encoding was applied to Location to convert categorical data into numerical form for machine learning models.

## 7. Scaling
StandardScaler was applied only to continuous features to ensure fair contribution in distance-based or gradient-based models. Target variables were not scaled.

## Conclusion
The dataset is now clean, consistent, and ready for machine learning modeling.