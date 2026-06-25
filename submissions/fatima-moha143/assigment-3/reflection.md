# reflection.md

## Data Preprocessing Reflection

### 1. Data Inspection

I first inspected the dataset using `head()`, `shape`, `info()`, and missing value counts. This helped identify missing values, inconsistent category labels, currency formatting in the target variable, duplicate rows, and potential outliers.

### 2. Price Cleaning

The `Price` column contained currency symbols and commas. These characters were removed and the column was converted to a numeric type. This ensured that statistical analysis and machine learning algorithms could process the target variable correctly.

### 3. Category Cleaning

The `Location` column contained inconsistent labels and typographical errors such as "Subrb". These values were standardized before imputation so that the same category was not represented multiple times. Invalid values such as "??" were converted to missing values.

### 4. Missing Value Imputation

I used the **median** for `Odometer_km` because mileage data can contain outliers and the median is more robust than the mean. I used the **mode** for `Doors`, `Accidents`, and `Location` because these variables are categorical or discrete and the most frequent value is the most appropriate replacement.

### 5. Duplicate Removal

Duplicate rows were removed to prevent the same observation from influencing the analysis and model training multiple times.

### 6. Outlier Treatment

I applied **IQR capping** to `Price` and `Odometer_km`. Instead of deleting observations, extreme values were clipped to the IQR bounds. This reduces the influence of outliers while preserving the size of the dataset.

### 7. One-Hot Encoding

The categorical variable `Location` was transformed into binary indicator columns (`Location_City`, `Location_Rural`, and `Location_Suburb`). This allows machine learning algorithms to use the information without assuming an ordinal relationship between categories.

### 8. Feature Engineering

Several new features were created:

* **CarAge** = Current Year − Year
* **Km_per_year** = Odometer_km / CarAge
* **Is_Urban** = Indicator for cars located in the city
* **LogPrice** = log(Price + 1) as an alternative target to reduce skewness

These features provide additional information about vehicle age, usage intensity, location characteristics, and target distribution.

### 9. Feature Scaling

Continuous predictor variables were standardized using `StandardScaler`. Target variables (`Price` and `LogPrice`) and one-hot encoded columns were not scaled because scaling them would not provide additional value.

### 10. Final Validation

Final checks confirmed that no missing values remained, all required features were present, and the cleaned dataset was successfully saved for future machine learning tasks.
