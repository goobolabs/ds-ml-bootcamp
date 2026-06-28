# Reflection

In this preprocessing task, I cleaned and prepared the car dataset so it can be used for analysis or machine learning. First, I converted the `Price` column from text into numeric format by removing symbols such as `$` and commas. This was necessary because numeric columns must be stored as numbers before calculations, scaling, or modeling can be done.

For missing values, I used the **median** for `Odometer_km` because odometer values can contain extreme values, and the median is less affected by outliers than the mean. For categorical or discrete columns such as `Doors` and `Location`, I used the **mode** because it replaces missing values with the most common valid category.

I removed duplicate rows to avoid repeated records affecting the final dataset. I also corrected inconsistent category values in `Location`, such as changing `Subrb` to `Suburb` and treating `??` as missing.

To handle outliers, I used the **IQR capping method** on `Price` and `Odometer_km`. I chose capping instead of deleting rows because some extreme values may still be useful, but very large or very small values can negatively affect scaling and model performance. Capping keeps the data size while reducing the effect of outliers.

I used one-hot encoding for the `Location` column so that categorical values could be converted into numeric features. I then created new features: `Car_Age`, `km_per_year`, `accident_rate`, `Is_City`, and `LogPrice`. These features give more useful information than the original columns alone. For example, `Car_Age` shows how old the car is, `km_per_year` shows usage level, `accident_rate` shows accident frequency, and `LogPrice` helps reduce price skewness.

Finally, I applied standard scaling to selected numeric features so they have a similar scale. I did not scale target-related columns such as `Price` and `LogPrice`, and I avoided scaling one-hot encoded columns because they already represent categories using 0 and 1 values. The final cleaned dataset was saved as `clean_car_dataset.csv` inside the `assignment3` folder.
