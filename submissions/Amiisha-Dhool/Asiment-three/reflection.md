# Reflection

In this assignment, I cleaned and prepared the car dataset for machine learning. I converted the **Price** column into a numeric format by removing currency symbols and commas. I corrected invalid values in the **Location** column by replacing **"Subrb"** with **"Suburb"** and converting **"??"** into missing values.

For missing data, I used the **median** for **Odometer_km** because it is less affected by outliers, while I used the **mode** for **Doors**, **Accidents**, and **Location** since they are categorical or discrete variables.

I removed duplicate rows to improve data quality and applied **IQR capping** to reduce the impact of extreme outliers in **Price** and **Odometer_km**.

Next, I encoded the **Location** column using one-hot encoding and created new features such as **CarAge**, **Km_per_year**, and **Is_Urban**. I also created **LogPrice** as an alternative target variable.

Finally, I standardized the continuous features using **StandardScaler**, checked that there were no missing values left, and saved the cleaned dataset as **clean_car_dataset.csv**. These preprocessing steps improved the dataset and made it ready for machine learning.
