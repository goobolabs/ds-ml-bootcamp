Data Preprocessing Reflection

In this assignment, I built a full data preprocessing pipeline to clean and prepare a messy car price dataset for machine learning.

1. Missing Values Handling

I handled missing values using different strategies depending on the data type:

For Odometer_km, I used the median because it is not affected by extreme values (outliers), making it more reliable for numerical data.
For Doors, Accidents, and Location, I used the mode because these are categorical or discrete values, and the most frequent value is the best representation of missing entries.
2. Price Cleaning

The Price column contained currency symbols and commas, so I removed them and converted the column into a numeric (float) type. I also checked the skewness to understand the distribution of the target variable.

3. Category Cleaning

I fixed inconsistencies in the Location column such as typos (e.g., “Subrb” → “Suburb”) and invalid values like “??”. This step was important to ensure consistent encoding during modeling.

4. Duplicate Removal

I removed duplicate rows to prevent bias in the dataset. Duplicate records can mislead the model by giving extra weight to repeated observations.

5. Outlier Handling (IQR Capping)

I used the IQR (Interquartile Range) method to detect and cap outliers in Price and Odometer_km. This method is effective because it keeps most of the data while limiting extreme values that can distort model training.

6. Feature Engineering

I created new features to improve model understanding:

CarAge: shows how old the car is, which strongly affects price.
Km_per_year: measures usage intensity of the car.
LogPrice: a log-transformed version of Price to reduce skewness and improve model stability.

I also created Is_Urban based on Location to capture whether the car is in an urban area.

7. Feature Scaling

I applied StandardScaler only to numerical input features (Odometer_km, CarAge, Km_per_year). This ensures all features are on the same scale, improving performance for many machine learning models. I did not scale Price or LogPrice because they are target variables.

8. Final Outcome

After preprocessing:

The dataset has no missing values
All categorical variables are encoded
Outliers are reduced using IQR capping
Features are properly scaled and engineered

The final dataset is clean and ready for machine learning modeling.

Conclusion

This preprocessing pipeline improved data quality, consistency, and model readiness. Each step was chosen carefully based on the type of data and its role in machine learning.