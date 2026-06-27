# Reflection – Data Preprocessing Pipeline

## Overview
This project focused on building a complete data preprocessing pipeline for a used car dataset. The dataset contained missing values, inconsistent categories, duplicates, and outliers. The goal was to clean the data and prepare it for machine learning by applying standard data science techniques.

---

## 1. Handling Missing Values (Median vs Mode)

For numerical columns such as **Odometer_km**, I used the **median** because it is not affected by extreme values (outliers). Car mileage data often contains very large or very small values, so the median gives a more realistic central value.

For categorical columns such as **Doors, Accidents, and Location**, I used the **mode** because it represents the most frequent category in the dataset. This ensures missing values are filled with the most common and realistic value.

---

## 2. Fixing Category Errors

The Location column contained inconsistent values such as typos (e.g., “Subrb”) and unknown entries like “??” or “unknown”. These were standardized and converted into missing values before imputation. This step ensured that all categories were consistent and suitable for encoding.

---

## 3. Removing Duplicates

Duplicate rows were removed to prevent bias in analysis and machine learning models. Duplicates can artificially increase the importance of certain records, so removing them ensures each observation is unique and meaningful.

---

## 4. Outlier Handling (IQR Capping)

I used the **Interquartile Range (IQR) method** to detect and handle outliers in **Price** and **Odometer_km**. This method is effective because it focuses on the middle 50% of the data and identifies extreme values outside a reasonable range.

Instead of deleting outliers, I used **capping (clipping)** to replace extreme values with upper or lower bounds. This preserves data points while reducing the impact of extreme values on model performance.

---

## 5. Feature Engineering

Three new features were created:

- **CarAge**: calculated from the difference between the current year and manufacturing year. It provides insight into vehicle depreciation.
- **Km_per_year**: measures how much the car is driven annually. It helps understand usage intensity.
- **Is_Urban**: a binary feature indicating whether a car is from a city/suburb or rural area. It captures location-based patterns.

Additionally, **LogPrice** was created as an alternative target variable to reduce skewness in price distribution and improve model stability.

---

## 6. Feature Scaling

Standardization was applied to continuous features such as **Odometer_km, Year, CarAge, and Km_per_year**. Scaling ensures that all features are on the same scale, which improves the performance of many machine learning algorithms.

Categorical dummy variables and binary features were not scaled because they already have meaningful fixed values (0 and 1).

---

## Conclusion

The preprocessing pipeline successfully transformed a messy dataset into a clean and structured format suitable for machine learning. Each step—from handling missing values to feature engineering—was applied with consideration of data quality, statistical properties, and model requirements.