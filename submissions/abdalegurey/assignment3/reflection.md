# Reflection – Car Price Data Cleaning & Feature Engineering

In this project, I performed a full data preprocessing pipeline including cleaning, handling missing values, outlier treatment, encoding, feature engineering, and scaling. Each step was chosen carefully to ensure data quality and prevent data leakage before modeling.

## 1. Data Cleaning Decisions

The first step was cleaning the `Price` column by removing symbols like `$` and commas and converting it into a numeric format. This was necessary because machine learning models require numerical inputs.

For categorical inconsistencies in the `Location` column (e.g., "Subrb", "??"), I replaced incorrect values with standardized labels or missing values. This helped ensure consistency in categorical features.

## 2. Handling Missing Values

For missing numerical values such as `Odometer_km`, I used the **median** because it is robust to outliers and skewed distributions. Median is preferred over mean in datasets where extreme values exist.

For categorical features like `Doors` and `Location`, I used the **mode (most frequent value)** because it preserves the most common category and maintains data distribution.

## 3. Outlier Treatment (IQR Capping)

I applied **IQR (Interquartile Range) capping** to `Price` and `Odometer_km` to reduce the effect of extreme values. This method was chosen because it is robust and does not remove data but instead limits extreme values within a reasonable range, preserving dataset size while reducing skewness.

## 4. Encoding Categorical Variables

I used **one-hot encoding** for the `Location` column to convert categorical values into numerical form without introducing ordinal relationships. This ensures that the model does not assume any ranking between categories like City, Suburb, or Rural.

## 5. Feature Engineering (No Leakage)

I created several new features to improve model learning while avoiding data leakage:

* **CarAge** = Current year (2026) minus manufacturing year. This captures vehicle depreciation over time.
* **KmPerYear** = Odometer divided by car age (+1 to avoid division by zero). This measures average yearly usage.
* **DoorAccidentRatio** = Doors divided by (Accidents + 1). This helps capture structural complexity vs accident history.
* **HasAccident** (optional concept) indicates whether a car has been in any accident, improving interpretability.

All engineered features use only independent variables (Year, Odometer, Doors, Accidents), ensuring there is no leakage from the target variable `Price`.

## 6. Scaling

I applied **StandardScaler** to numeric features to normalize their distributions. This is important for models sensitive to scale such as linear regression and gradient-based algorithms. I excluded target-related variables (`Price`, `LogPrice`) and one-hot encoded features from scaling.

## Conclusion

Overall, the preprocessing pipeline ensures clean, consistent, and model-ready data. Each decision was made to balance data quality, model performance, and prevention of data leakage. The final dataset is suitable for training machine learning models for car price prediction.
