# Reflection — Data Preprocessing Pipeline

In this preprocessing pipeline, I first inspected the dataset to understand missing values, data types, duplicates, category errors, and outliers. The `Price` column contained currency symbols and commas, so I cleaned it and converted it into a numeric float column.

For missing values, I used median imputation for `Odometer_km` because mileage can contain extreme outliers, and the median is more robust than the mean. For `Doors`, `Accidents`, and `Location`, I used mode imputation because these columns are categorical or discrete, so the most frequent value is a reasonable replacement.

Before imputation, I fixed category errors in `Location`, such as mapping `Subrb` to `Suburb` and converting unknown values like `??` into missing values. I removed duplicate rows to avoid repeated records affecting the analysis or future model training.

For outliers, I used IQR capping on `Price` and `Odometer_km`. I chose capping instead of deleting rows because extreme values may still represent real cars, but they can strongly distort the dataset. Capping limits values to reasonable lower and upper bounds while keeping the records.

I encoded `Location` using one-hot encoding so that machine learning models can understand the categorical values without creating a false ranking between City, Suburb, and Rural.

For feature engineering, I created `CarAge` from `Year`, `Km_per_year` from odometer and car age, and `Is_Urban` from location dummy columns. These features help represent car condition and usage more clearly. I also created `LogPrice` as an alternative target to reduce the effect of skewed price values, but I did not treat it as an input feature.

Finally, I standardized only continuous input features using `StandardScaler`. I did not scale `Price` or `LogPrice` because they are targets, and I left 0/1 dummy columns unscaled because they already represent binary categories.
