Reflection

Missing Value Decisions

I used the median method for Odometer_km because mileage data often contains outliers, and the median is less affected by extreme values compared to the mean.

I used the mode method for Doors, Accidents, and Location because these columns contain categorical or discrete values. Replacing missing values with the most frequent value helps maintain consistency in the dataset.

Outlier Handling

I used the IQR capping method for Price and Odometer_km. This approach helps reduce the impact of extreme values without removing records from the dataset. It preserves useful information while making the data more stable for machine learning models.

Feature Engineering

I created the following new features:

- CarAge = Current Year − Year
- Km_per_year = Odometer_km ÷ (CarAge + 1)
- Is_Urban = Indicates whether the car location is urban (city)
- LogPrice = log(Price + 1)

These features were created to improve the predictive power of the dataset and avoid data leakage.

Scaling

I standardized continuous variables using StandardScaler because machine learning algorithms generally perform better when numerical features are on a similar scale.

I did not scale binary variables and target columns (Price and LogPrice) because scaling them was unnecessary.