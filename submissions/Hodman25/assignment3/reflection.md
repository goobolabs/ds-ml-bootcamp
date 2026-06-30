# Car Dataset Preprocessing Reflection


## Data Cleaning

The dataset was loaded using Pandas and inspected for missing values, incorrect formats, and duplicates.

The following preprocessing steps were performed:

* Converted the **Price** column from text format (containing `$` and commas) into numeric values.
* Fixed category errors in the **Location** column (e.g., correcting `Subrb` to `Suburb`).
* Filled missing values:

  * **Odometer_km** using the median.
  * **Doors** using the mode.
  * **Location** using the most frequent category.


### Removed duplicate records.

## Outlier Treatment

Outliers in **Price** and **Odometer_km** were detected using the IQR method and capped using the `clip()` function to reduce the impact of extreme values while keeping all records.

## Feature Engineering

new features were created:

* **car_Age**
* **Km_per_year** 
* **Is_Urban** 
* **Log_price** 
## Encoding and Scaling

The categorical **Location** column was converted into numerical variables using One-Hot Encoding. Numerical features were standardized using **StandardScaler** to ensure they were on a similar scale. The target variables (**Price** and **Log_price**) were not scaled.

## Conclusion

The dataset was successfully cleaned, transformed, and prepared for Machine Learning. Missing values, duplicates, and outliers were handled, while new features were created to improve predictive performance. The final cleaned dataset was saved as **clean_car_dataset.csv** and is ready for further analysis and model building.
