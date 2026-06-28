# Reflection – Car Dataset Preprocessing

## Overview

I cleaned and prepared a car dataset. The raw data had missing values, errors, and different formats. I fixed these problems step by step.

---

## Missing Values

I used **median** for numbers like `Odometer_km` because it is not affected by very large or very small values. I used **mode** for categories like `Doors` and `Location` because it is the most common value and makes sense for missing data.

---

## Data Cleaning

I cleaned the `Price` column by removing symbols like `$` and commas. This was needed so the values become numbers.

I also fixed the `Location` column by replacing wrong values like `"Subrb"` and `"??"` with correct or missing values.

---

## Removing Duplicates

I removed duplicate rows using `drop_duplicates()`. This is important because duplicate data can make the model learn wrong patterns.

---

## Outliers (IQR Method)

I used the IQR method to find extreme values in `Price` and `Odometer_km`. I did not delete them. Instead, I limited them (capping). This keeps data but reduces extreme effects.

---
## Encoding Data

I used one-hot encoding for `Location` because machine learning models cannot understand text.

---

## Feature Engineering

I created new features:

* **CarAge**: How old the car is.
* **Km_per_year**: How much the car is used each year.
* **Is_Urban**: Shows if car is in city or suburb.
* **LogPrice**: Makes price distribution more normal.

These features help the model understand the data better.

---



## Scaling

I used StandardScaler to make all numbers on the same scale. This helps the model learn better.

---

## Conclusion

After all steps, the dataset is clean, consistent, and ready for machine learning. Each step helped improve data quality and make better predictions.
