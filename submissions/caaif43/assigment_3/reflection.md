# Reflection

## Introduction

During this project, I performed several data preprocessing steps to prepare the car dataset for machine learning. Each preprocessing technique was selected based on the type and quality of the data.

## Cleaning the Price Column

The Price column contained dollar signs ($) and commas (,), making it a text field instead of a numeric field. I removed these symbols and converted the column to a float data type so that it could be used in machine learning algorithms.

## Handling Missing Values

For the Odometer_km column, I used the median because mileage data may contain outliers. The median is more robust than the mean and is less affected by extremely large or small values.

For the Doors column, I used the mode because it is a categorical/discrete variable. Replacing missing values with the most common number of doors preserves the natural distribution of the data.

For the Location column, I also used the mode because it is a categorical feature. Filling missing values with the most frequent location is a simple and commonly used preprocessing technique.

## Removing Duplicates

Duplicate rows were removed to avoid giving the machine learning model repeated information. Duplicate records can bias the model and reduce its ability to generalize.

## Outlier Handling

I used the Interquartile Range (IQR) method to detect outliers in the Price and Odometer_km columns. Instead of deleting outliers, I applied IQR capping using the clip() function. This approach reduces the influence of extreme values while preserving all observations.

## One-Hot Encoding

The Location column contains categorical values that machine learning algorithms cannot process directly. I used One-Hot Encoding to convert each location into separate binary columns.

## Feature Engineering

I created two new features:

- CarAge = Current Year − Year
- Km_per_Year = Odometer_km / CarAge

CarAge provides information about the age of each vehicle, while Km_per_Year estimates how much the vehicle has been driven each year. These engineered features may improve the predictive performance of machine learning models.

## Feature Scaling

I used StandardScaler to standardize the numerical features. Scaling helps algorithms that depend on feature magnitude, such as K-Nearest Neighbors, Support Vector Machines, and Logistic Regression.
