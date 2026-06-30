# Conclusion and Reflection

Conclusion and Reflection
This project focused on cleaning, preprocessing, and improving a car price dataset to make it suitable for machine learning. Several important decisions were made during data preparation to improve data quality and model performance.
Why Median vs Mode?
Missing values in numerical features were filled using the median because numerical variables often contain extreme values or outliers. Unlike the mean, the median is not heavily affected by unusually high or low values, making it a more reliable measure of central tendency.
For categorical features, the mode was used because it represents the most frequently occurring category. Replacing missing categorical values with the mode helps maintain the original distribution of the dataset and avoids introducing unrealistic categories.
Why IQR Capping?
Outliers were handled using the Interquartile Range (IQR) method. Instead of removing records containing extreme values, I applied IQR capping to limit values within acceptable lower and upper bounds.
This approach was chosen because deleting outliers may result in the loss of valuable information, especially when the dataset is not very large. IQR capping reduces the influence of extreme observations while preserving all available data for analysis and model training.
Which Features Were Engineered and Why?
Several new features were created to improve the predictive power of the dataset:
CarAge = Current Year − Manufacturing Year
This feature captures the age of the vehicle, which is an important factor affecting resale price.
Km_per_year = Odometer_km / CarAge
This feature measures how intensively a vehicle has been used over time and provides more meaningful information than total mileage alone.
Encoded Categorical Features
Categorical variables such as location were transformed into numerical representations using encoding techniques so that machine learning algorithms could process them effectively.
These engineered features provide additional information that may not be directly available in the original dataset and help machine learning models identify patterns more accurately.
Conclusion
Overall, the preprocessing pipeline improved the dataset by handling missing values, reducing the impact of outliers, and creating meaningful new features. The use of median imputation, mode imputation, IQR capping, and feature engineering resulted in a cleaner and more informative dataset that is better suited for machine learning tasks. These decisions help improve model reliability, reduce noise, and increase the likelihood of achieving accurate predictions.