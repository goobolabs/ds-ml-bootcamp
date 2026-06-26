# Reflection - Data Preprocessing Pipeline
*In this assignment, I build full preprocessing pipeline to clear messy car dataset and prepare it for machine learning.*
---
- First I inspected the dataset to to understant the issues such as missing values, inconsistent formatting in the Price column and categorical errors in the Location features. 
- I cleaned the Price column by removing currency symbols and converting it into a numeric.
- For missing values, I used median imputation for Odometer_km because it is robust to outliers, and mode imputation for categorical variables like Location and Doors.
- I removed duplicates that was 5 to ensure data quality and prevent bias in model training.
- To handle outliers, I have used the IQR with capping instead of deleting rows.
- I applied **ONE-HOT** encoding to convert the location column into numerical features.
- I performed feature engineering and created CarAge, Km_per_year and Is_City
- Finally, I applied StandardScaler to numerical features to ensure they are on the same scale.

*Overall, the preprocessing pipeline improved data quality, reduced noise, and prepared the dataset for reliable machine learning modeling.*