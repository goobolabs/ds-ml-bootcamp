# Reflection

## Dataset Cleaning and Preparation Reflection

In this project, I cleaned and prepared a used car dataset for machine learning analysis. My goal was to improve data quality, handle inconsistencies, and create useful features while avoiding data leakage.

### Price Cleaning

The Price column contained different formats, including currency symbols ($) and commas. I removed these characters and converted the column to a numeric data type so that statistical analysis and machine learning algorithms could process it correctly.

### Handling Categorical Errors

The Location column contained inconsistent values such as "Subrb" and unknown values represented by "??". I corrected spelling errors by mapping "Subrb" to "Suburb" and converted unknown values to missing values before performing imputation. This ensured consistency in the categorical data.

### Missing Value Imputation

Different imputation methods were chosen based on the nature of each variable.

* **Odometer_km:** I used the median because mileage data can contain extreme values (outliers), and the median is more robust than the mean.
* **Doors:** I used the mode because the number of doors is a categorical/discrete feature, and the most common value is a reasonable replacement.
* **Accidents:** I used the mode because it represents the most frequently occurring category.
* **Location:** I used the mode because it is a categorical feature and the most common location provides a practical estimate.

### Duplicate Removal

Duplicate records were removed to avoid giving certain observations more influence than others during analysis and model training.

### Outlier Treatment

I used the Interquartile Range (IQR) method to identify outliers in the Price and Odometer_km columns. Instead of deleting rows, I applied IQR capping (winsorization), which limits extreme values to the calculated lower and upper bounds. This approach preserves data while reducing the impact of unusually large or small values.

### One-Hot Encoding

The Location feature was transformed using one-hot encoding. Machine learning algorithms require numerical inputs, so categorical values were converted into binary indicator columns.

### Feature Engineering

I created several new features:

* **CarAge:** Calculated as the current year minus the vehicle year. Older vehicles often have lower prices.
* **Km_per_year:** Measures average yearly usage and provides more information than total mileage alone.
* **Is_Urban:** Indicates whether the vehicle is located in a city or suburb, which may influence vehicle demand and pricing.
* **LogPrice:** Created as an alternative target variable to reduce skewness and improve model performance.

### Feature Scaling

Continuous numerical variables were standardized using StandardScaler. Scaling helps machine learning models perform better by ensuring features are on a similar scale. The target variables (Price and LogPrice) and one-hot encoded columns were not scaled.

Overall, these preprocessing steps improved data quality, reduced noise, and prepared the dataset for machine learning tasks.
