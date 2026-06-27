# Reflection on Data Preprocessing

During this assignment, I learned that raw data is usually not ready to be used directly in machine learning models and needs preprocessing first.

The first step was inspecting the dataset to identify missing values, incorrect formats, and duplicates. The **Price** column contained currency symbols and commas, so I cleaned it and converted it into a numeric data type.

Missing values were handled using different techniques depending on the feature. I used the **median** for `Odometer_km` because mileage data can contain extreme values, while the **mode** was used for `Doors`, `Accidents`, and `Location` since these are categorical features.

I also handled outliers in `Price` and `Odometer_km` using the IQR capping method to reduce the effect of extreme values without removing records from the dataset.

For categorical data, I applied one-hot encoding to the `Location` feature so it could be used by machine learning algorithms. In addition, I created new features such as `CarAge`, `Km_per_year`, and `Is_Urban` to provide more useful information for the model.

Finally, I created `LogPrice` as an alternative target variable to reduce skewness in the price distribution.

Overall, this preprocessing process helped me understand the importance of cleaning and preparing data before building machine learning models. I learned that good preprocessing can improve both the quality of the dataset and the performance of future models.