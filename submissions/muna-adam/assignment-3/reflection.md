
# Reflection on Data Cleaning and Feature Engineering

For this project, I worked with a used-car dataset containing missing values, inconsistent price formatting, outliers, and categorical features. I made several preprocessing decisions to improve data quality and prepare the dataset for machine learning.

## 1. Handling Missing Values

For numerical columns such as Odometer_km, I used the median instead of the mean. The dataset contains some unusually high and low mileage values, so the median is more robust to outliers and represents a typical car better than the mean.

For categorical columns such as Location, I used the mode because it fills missing values with the most frequently occurring category. This preserves the overall distribution of locations in the dataset.

## 2. IQR Capping for Outliers

I applied IQR (Interquartile Range) capping to numerical features such as Price and Odometer_km. Instead of deleting outliers, I capped values outside the lower and upper IQR bounds. I chose this method because removing rows would reduce the dataset size, while capping keeps all observations but limits the influence of extreme values on the model.

## 3. Feature Engineering

I created a new feature called Car_Age using:

Car_Age = Current_Year - Year

This feature is more meaningful than the raw manufacturing year because car depreciation is usually related to how old the vehicle is.

I also created LogPrice using a logarithmic transformation of Price. Car prices were highly right-skewed, so the log transformation reduced skewness and made the target variable more suitable for regression modeling.

## 4. Encoding Categorical Variables

I used One-Hot Encoding for the Location column, creating features such as Location_City, Location_Rural, and Location_Suburb. This allows machine-learning models to use location information without assuming an artificial numeric order between categories.

## 5. Feature Scaling

I applied StandardScaler to numerical features (Odometer_km, Doors, Accidents, and Car_Age). Scaling helps features with different ranges contribute more equally to models such as Linear Regression. I did not scale the target variable LogPrice, since the logarithmic transformation was already sufficient.

## Conclusion

Overall, these preprocessing steps were chosen to create a cleaner, more consistent dataset, reduce the effect of outliers, preserve useful information, and improve the performance and interpretability of the machine-learning model.