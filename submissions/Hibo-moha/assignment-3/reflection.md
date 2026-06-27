# Reflection

## Data Inspection

The dataset contained inconsistent text formatting, mixed numeric formats, outliers, and invalid values.

## Data Cleaning

Minutes Late values such as "10min" and "15 min" were converted into numeric values. Attendance Rate values containing percentages (%) were cleaned and converted to numeric format. Invalid values such as "A" were converted into missing values.

## Missing Value Handling

The missing Attendance Rate value was replaced using the median because it is less sensitive to extreme values.

## Duplicate Removal

The dataset was checked for duplicate records. No duplicates were found.

## Outlier Treatment

IQR capping was applied to Age, Minutes Late, and Attendance Rate to reduce the influence of extreme values while preserving observations.

## Feature Engineering

Three new features were created:

* IsLate
* HighAttendance
* AttendanceScore

These features help represent employee punctuality and attendance performance.

## Encoding and Scaling

Categorical variables were converted using one-hot encoding. Numerical features were standardized using StandardScaler to make them suitable for machine learning models.

## Final Result

The final dataset contains cleaned, transformed, and scaled features with no missing values and is ready for further analysis or machine learning.
