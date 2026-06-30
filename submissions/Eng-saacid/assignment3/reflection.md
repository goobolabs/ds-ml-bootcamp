# Reflection - Car Price Dataset Preprocessing

## Data Cleaning Decisions

During preprocessing, I cleaned the dataset by handling missing values, inconsistent categories, and formatting issues. The Price column contained currency symbols and commas, so these were removed and converted into numeric format to make it suitable for machine learning models.

## Missing Value Handling

I used median imputation for `Odometer_km` because mileage data can contain extreme values, and the median is less affected by outliers compared to the mean.

I used mode imputation for `Doors`, and `Location` because these columns contain categorical or discrete values. The mode represents the most common value and is suitable for replacing missing categories.

## Outlier Handling

I applied IQR (Interquartile Range) capping to `Price` and `Odometer_km`. Instead of removing outliers, I limited extreme values to the calculated upper and lower bounds. This helps reduce the influence of extreme observations while keeping the available data.

## Feature Engineering

I created additional features to improve the information available for the machine learning model:

* `CarAge`: Calculated from Year to represent the age of each vehicle. Vehicle age can have a strong relationship with price.
* `Km_per_year`: Calculated using Odometer_km divided by CarAge. This represents the average usage of the vehicle per year. Safe handling was applied to avoid division by zero.
* `Has_Accident`: Created from Accidents to indicate whether a vehicle has any accident history (0 or 1).

I also created `LogPrice = log(Price + 1)` as an alternative target to reduce the effect of price skewness. It was not used as a feature.

## Scaling Decision

I standardized continuous input features only because machine learning algorithms can perform better when numerical features have similar scales. I did not scale `Price` or `LogPrice` because they are target variables. Binary dummy variables from Location encoding were also left unscaled because they already have values of 0 and 1.

Overall, these preprocessing steps created a cleaner and more consistent dataset suitable for machine learning modeling.
