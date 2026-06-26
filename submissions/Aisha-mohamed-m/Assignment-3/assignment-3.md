Project Report: Advanced Data Preprocessing & Feature Engineering
1. Introduction
The objective of this phase was to clean the raw vehicle dataset and apply advanced Data Preparation techniques. This ensures that the Machine Learning model can accurately learn the underlying data patterns without encountering runtime errors, bias, or distortion from unscaled features.

2. Core Data Cleaning
A. Text and Character Stripping
Price Column (Price): The original raw data contained currency symbols such as the dollar sign ($) and commas. A string-cleansing script was executed to strip these characters, and the column was successfully converted into a numeric data type (float/int) to enable mathematical computations and target predictions.

B. Text Standardization
Location Column (Location): Location names that were inconsistent due to varying case types (uppercase/lowercase) or typographical errors were standardized. They were mapped into three clean, distinct categories: City, Suburb, and Rural.

3. Handling Missing Values (Imputation Strategy)
To handle missing values (NaN or blank entries) effectively without introducing bias, two distinct statistical techniques were applied based on the nature of each feature:

A. Imputation of the Location Column (Mode Imputation)
Method Used: Mode (The most frequent value).

Justification: Since Location is a categorical feature (text-based), calculating a mathematical average (mean) or midpoint (median) is impossible. The most statistically sound approach is to fill the missing spaces with the most common location in the dataset, ensuring the general distribution of the data remains natural.

B. Imputation of the Odometer_km / Distance Columns (Median Imputation)
Method Used: Median (The middle value).

Justification: Distance data (Odometer_km) often contains extreme Outliers—such as brand-new cars with almost zero kilometers or exceptionally old cars with massive mileage. If the Mean (average) were used, these extreme outliers would heavily skew the number, making the imputed values artificially high. The Median is robust against outliers and represents the true typical midpoint of the data.

4. Feature Engineering
To provide the machine learning model with deeper contextual knowledge, several engineered features were derived from the existing columns:

carage (Vehicle Age): Calculated by subtracting the manufacturing year from the current operational year (2026−Year).

km_per_Year: Measures the average distance driven per year, calculated by dividing the total mileage by the car's age (Odometer_km/(carage+1)). Adding 1 prevents a critical Division by Zero error for brand-new cars.

accident_rate: Quantifies the frequency of accidents relative to the distance the vehicle has traveled (Accidents/Odometer_km).

logPrice: A logarithmic transformation (np.log1p) was applied to the target variable (Price) to stabilize its variance and reshape it closer to a Normal Distribution, which significantly helps linear models perform better.

5.  One-Hot Encoding: To prevent the Rural class from being completely overshadowed during average calculation due to structural dummy formatting (True/False), a temporary location column (Temp_location) was utilized. This allowed the smooth calculation of 

Location_Avg_Price (the true average price per geographical sector) before dropping the temporary column.Bug Fix: A typo that accidentally generated a duplicate column named Location_AVg_Price (with a capital 'V') alongside the correct Location_Avg_Price was 

detected and dropped (df.drop), successfully streamlining the dataset schema.6. Feature ScalingA StandardScaler from the sklearn.preprocessing library was utilized to standardize the continuous numeric features.Scaled Features: All continuous columns (Odometer_km, Doors, Accidents, Year, carage, km_per_Year, accident_rate, Location_Avg_Price) were scaled to have a mean of $0$ and a standard deviation of $1$.Excluded Features: The target variables (Price, logPrice) and the binary dummy variables (Location_City, Location_Rural, Location_Suburb) were intentionally excluded from scaling to maintain their strict native constraints.