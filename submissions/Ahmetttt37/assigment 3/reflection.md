# Reflection

## Data Cleaning

I first checked the dataset for missing values, duplicate rows, and incorrect data types. Cleaning the data before analysis helps improve data quality and model performance.

## Handling Missing Values

For numerical columns, I used the **median** to fill missing values because the median is less affected by outliers than the mean. For categorical columns, I used the **mode** because it represents the most common category and is appropriate for missing categorical data.

## Handling Outliers

I used the **IQR (Interquartile Range) method** to detect and cap outliers. Instead of removing rows, I capped extreme values at the lower and upper IQR limits. This keeps all observations while reducing the influence of unusually large or small values.

## Feature Engineering

I created new features to make the dataset more useful for machine learning. I applied one-hot encoding to categorical variables using `pd.get_dummies()` so that machine learning algorithms can process categorical data. I also created additional binary features where appropriate to represent important categories.

## Feature Scaling

I used **StandardScaler** to standardize the numerical features. Scaling ensures that features with different units are on a similar scale, which improves the performance of many machine learning algorithms. I excluded the target variable and one-hot encoded columns from scaling.

## Final Thoughts

After completing data cleaning, feature engineering, and feature scaling, the dataset became cleaner, more consistent, and ready for machine learning. These preprocessing steps help improve the reliability and accuracy of future predictive models.
