# Reflection: Student Data Preprocessing Pipeline

## Step 1 – Load & Inspect

The first step was to load the dataset and inspect its structure. I checked the first 10 rows, the shape of the dataset, the data types, missing values, and the categorical columns. I found one missing value in `study_hours_per_day`. I also noticed that `family_income_category` is a categorical column that needs One-Hot Encoding, while `gender`, `internet_access`, and `part_time_job` contain text values that need to be converted into numbers. Finding these problems early helped me prepare the preprocessing pipeline.

---

## Step 2 – Clean Target (final_exam_score)

The target column, `final_exam_score`, must be in numeric format before any analysis. I used `pd.to_numeric(errors="coerce")` to convert the values into numbers. Any invalid values were changed to missing values. After that, I checked the skewness of the target column. The skewness was close to zero, which means the data is almost normally distributed and suitable for machine learning.

---

## Step 3 – Fix Category Errors Before Imputation

Before filling missing values, I cleaned the text in the `family_income_category` column. I removed extra spaces, made the text format consistent, and mapped the values to the correct categories (`High`, `Middle`, and `Low`). Cleaning the categories first ensures that the mode is calculated correctly during imputation.

---

## Step 4 – Impute Missing Values

I used different methods to fill missing values based on the type of data.

| Column | Method | Reason |
|---------|--------|--------|
| `study_hours_per_day` | **Median** | The median is less affected by outliers than the mean, so it is a better choice for numerical data. |
| `gender`, `internet_access`, `part_time_job`, `family_income_category` | **Mode** | These columns contain categorical values, so the mode (most common value) is the best method for filling missing data. |

After filling the missing values, I checked the dataset again to make sure no missing values remained.

---

## Step 5 – Remove Duplicates

I removed duplicate rows to make sure every record is unique. Although this dataset did not contain duplicate rows, using `drop_duplicates()` is a good practice. I also removed the `student_id` column because it is only an identifier and does not provide useful information for prediction.

---

## Step 6 – Handle Outliers (IQR Capping)

I used the Interquartile Range (IQR) method to handle outliers. Instead of deleting rows with extreme values, I capped them within the lower and upper limits. This keeps all records in the dataset while reducing the effect of unusually large or small values.

---

## Step 7 – Encode Categorical Columns

The binary columns (`gender`, `internet_access`, and `part_time_job`) were converted into 0 and 1 using manual mapping. I used One-Hot Encoding for `family_income_category` because it has multiple categories with no natural order. This makes the data suitable for machine learning algorithms.

---

## Step 8 – Feature Engineering

I created several new features from the existing columns to provide more useful information for the model.

- **Study_Efficiency** combines study hours and attendance.
- **GPA_per_Subject** shows the average GPA for each subject.
- **Study_Sleep_Ratio** compares study hours with sleep hours.
- **Far_From_School** shows whether a student lives more than 10 km from school.
- **High_Attendance** shows whether attendance is at least 90%.
- **Log_Final_Exam** is a log-transformed version of the target variable that may be useful for future models.

These features were created only from the input variables, so they do not cause data leakage.

---

## Step 9 – Feature Scaling

I used `StandardScaler` to standardize only the continuous numerical features. The target columns and binary columns were not scaled because they are already easy to interpret. After scaling, the numerical features have a mean close to 0 and a standard deviation close to 1.

---

## Step 10 – Final Checks

Finally, I performed several validation checks to make sure the preprocessing pipeline was completed successfully. I confirmed that:

- The target column is numeric.
- The `Log_Final_Exam` column exists and is numeric.
- There are no missing values in the dataset.
- One-Hot Encoding created the required dummy columns.
- The scaled numerical features have approximately zero mean and unit standard deviation.

After all checks passed, I saved the cleaned dataset as **Student_Clean.csv**. The dataset is now clean and ready for machine learning.