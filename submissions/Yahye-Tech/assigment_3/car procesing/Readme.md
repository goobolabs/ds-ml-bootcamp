Car Price Data Cleaning & Preprocessing Project
Overview
In this project, I worked with a messy car price dataset and built a full preprocessing pipeline to clean and prepare it for machine learning. The dataset was not ready for analysis at the beginning because it contained missing values, inconsistent formats, and noisy data.
The main goal was to transform this raw dataset into a clean, structured version that can be used for modeling and analysis.
About the Dataset
The dataset contains information about cars such as price, mileage, number of doors, accident history, location, and manufacturing year.
However, the data had several issues, including:
Inconsistent price formats such as "$1,500" and 1500
Missing values in multiple columns
Typos and unknown values in the Location column
Duplicate rows
Outliers in numerical columns
What I Did (Step by Step)
I started by loading and inspecting the dataset to understand its structure and issues.
First, I cleaned the Price column by removing symbols like "$" and commas, then converted it into a numeric format.
Next, I handled missing values by applying appropriate strategies:
Median for numerical columns such as Odometer_km
Mode for categorical columns such as Doors and Location
After that, I standardized inconsistent values in the Location column by fixing typos such as “Subrb” into “Suburb” and replacing unknown values with the most frequent category.
I then removed duplicate rows to ensure data quality.
For outlier handling, I used the IQR method to cap extreme values in key numerical columns such as Price and Odometer_km.
After cleaning, I applied one-hot encoding to convert categorical variables into a machine-readable format.
Feature Engineering
I created additional features to improve the dataset:
CarAge calculated from the difference between the current year and manufacturing year
Km_per_year calculated from odometer and car age
Is_Urban indicating whether the location is a city
LogPrice created using log transformation of price for better model performance
Feature Scaling
I standardized numerical features so that all values are on the same scale. This ensures that machine learning models do not get biased toward variables with larger numerical ranges.
Final Output
The cleaned dataset was saved as:
clean_car_dataset.csv
The final dataset is now complete, consistent, and ready for machine learning tasks.
Summary
This project demonstrates a full data preprocessing pipeline, including data cleaning, handling missing values, encoding categorical variables, feature engineering, and feature scaling. It transforms a raw and messy dataset into a structured format suitable for predictive modeling.