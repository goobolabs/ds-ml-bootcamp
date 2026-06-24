# Reflection

This preprocessing pipeline was designed to transform the raw car dataset into a clean and machine-learning-ready dataset. The first step involved inspecting the data structure, missing values, and category distributions to identify quality issues that needed correction.

For the **Price** column, currency symbols and commas were removed before converting the values to numeric format. This ensured that price could be used in statistical analysis and machine learning models. In the **Location** column, spelling mistakes such as "Subrb" and "Citty" were corrected, while invalid values like "??" and "unknown" were treated as missing values to improve data consistency.

Missing values were handled using different strategies depending on the variable type. For **Odometer_km**, I used the **median** because mileage data is often skewed and may contain outliers; the median is more robust than the mean in such cases. For categorical variables (**Doors**, **Accidents**, and **Location**), I used the **mode** because it preserves the most common category and is appropriate for non-numeric data.

Duplicate records were removed to prevent repeated observations from biasing analysis and model training. To handle extreme values in **Price** and **Odometer_km**, I applied **IQR capping** rather than deleting rows. This approach reduces the influence of outliers while retaining all observations, which is particularly useful when working with relatively small datasets.

The categorical **Location** feature was transformed using **one-hot encoding** so that machine learning algorithms could process it as numerical input without introducing artificial ordering between categories.

Several new features were engineered to capture additional information. **CarAge** was created from the vehicle year to represent how old the car is, which is often a strong predictor of value. **Km_per_year** was calculated to measure average yearly vehicle usage, providing more insight than total mileage alone. **Is_Urban** was introduced to distinguish urban from rural locations, and **LogPrice** was created to reduce skewness in the target variable and improve model behavior.

Finally, numerical features were standardized using **StandardScaler** to place them on a common scale. This helps algorithms that are sensitive to feature magnitude, such as KNN, SVM, and linear models. The resulting dataset is clean, consistent, and ready for further analysis and model development.
