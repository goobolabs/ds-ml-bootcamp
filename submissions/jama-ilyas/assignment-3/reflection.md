# Reflection

In this assignment, I cleaned and prepared the raw car dataset for machine learning. First, I inspected the dataset using `.head()`, `.shape`, `.info()`, missing value counts, and category counts. This helped me understand the structure of the data and identify problems such as missing values, inconsistent categories, duplicate rows, and outliers.

I cleaned the `Price` column because some values contained dollar signs and commas, which made the column a string instead of numeric. I removed the symbols and converted the column to a numeric type so that it could be used for analysis and modeling.

For the `Location` column, I fixed category errors such as changing `Subrb` to `Suburb`. I also converted unknown values such as `??` and empty values into missing values. After that, I checked the full value counts to confirm that only valid categories remained.

For missing values, I used the median for `Odometer_km` because mileage can contain outliers, and the median is more stable than the mean when extreme values exist. I used the mode for `Doors` and `Location` because these are categorical or discrete values, so the most frequent value is a sensible replacement. I used `.mode()[0]` because `.mode()` returns a Series, and `[0]` selects the first most frequent value.

I removed duplicate rows to avoid repeated records affecting the model. I checked the shape before and after removing duplicates to confirm how many rows were removed.

I used IQR capping for `Price` and `Odometer_km` to reduce the effect of extreme outliers without deleting rows. This was important especially for `Price`, because it had high skewness and very large values compared to most cars. Capping allowed me to keep the data while limiting the influence of extreme values.

I also engineered new features. `CarAge` was created from the year of the car, because age can affect price. `Km_per_year` was created to show how heavily the car has been used each year. `Is_Urban` was added as a simple 0/1 feature based on whether the location was City. I also created `LogPrice` as an alternative target to reduce the effect of skewness in price.

Finally, I one-hot encoded the `Location` column and scaled only the continuous feature columns. I did not scale `Price` or `LogPrice` because they are target variables, and I did not scale dummy variables because they are already 0/1 values. At the end, I confirmed there were no missing values and saved the cleaned dataset as `clean_car_dataset.csv`.