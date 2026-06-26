Student Lifestyle Habits and Academic Performance - A Self-Collected Survey Dataset

_Practical Assignment 2 - Data Foundations for Machine Learning_

# 1\. Title & Collection Method

This dataset was collected through a structured self-administered questionnaire distributed to university students across different year groups. Each student was asked to self-report their daily habits, demographic information, and academic outcomes. Data was recorded manually and logged into a spreadsheet over a one-week period. A total of 56 responses were collected (including 1 duplicate entry introduced during logging), resulting in 55 unique valid samples across 9 columns.

# 2\. Description of Features & Labels

| **Column**                 | **Type**    | **Role**    | **Description**                          |
| -------------------------- | ----------- | ----------- | ---------------------------------------- |
| Student_ID                 | Categorical | Identifier  | Unique student code (e.g., STU001)       |
| Age                        | Numerical   | Feature (X) | Student age in years (17-24)             |
| Gender                     | Categorical | Feature (X) | Male / Female (with some typos)          |
| Study_Hours_Per_Day        | Numerical   | Feature (X) | Average daily study hours                |
| Sleep_Hours_Per_Day        | Numerical   | Feature (X) | Average daily sleep hours                |
| Social_Media_Hours_Per_Day | Numerical   | Feature (X) | Daily social media usage in hours        |
| Attendance\_%              | Numerical   | Feature (X) | Class attendance percentage (50-100%)    |
| Part_Time_Job              | Categorical | Feature (X) | Whether student works part-time (Yes/No) |
| GPA                        | Numerical   | Label (y)   | Grade Point Average on a 1.0-4.0 scale   |

Input Features (X): Age, Gender, Study Hours, Sleep Hours, Social Media Hours, Attendance %, Part-Time Job

Target Label (y): GPA - this is what we want to predict

# 3\. Dataset Structure

\- Rows: 56 (including 1 duplicate)

\- Columns: 9 (1 identifier + 7 features + 1 label)

Sample Table (first 5 rows):

| **Student_ID** | **Age** | **Gender** | **Study_Hrs** | **Sleep_Hrs** | **Social_Media_Hrs** | **Attendance\_%** | **Part_Time_Job** | **GPA** |
| -------------- | ------- | ---------- | ------------- | ------------- | -------------------- | ----------------- | ----------------- | ------- |
| STU001         | 23      | FEMALE     | 5.3           | 8.4           | 0.9                  | 53                | No                | 4.00    |
| STU002         | 20      | Male       | 2.2           | 5.3           | 1.8                  | 87                | No                | 3.20    |
| STU003         | 21      | Male       | 6.1           | 6.5           | NaN                  | 97                | No                | 4.00    |
| STU004         | 23      | Male       | 2.1           | 4.9           | 1.7                  | 84                | Yes               | 2.42    |
| STU005         | 19      | Female     | 3.7           | 8.6           | 1.2                  | 53                | Yes               | 2.97    |

# 4\. Quality Issues

| **Issue**                   | **Description**                                                     | **Count** |
| --------------------------- | ------------------------------------------------------------------- | --------- |
| Missing Values              | Sleep_Hours_Per_Day has blank entries                               | 5 rows    |
| Missing Values              | Social_Media_Hours_Per_Day has blank entries                        | 3 rows    |
| Duplicate Row               | STU001 appears twice due to logging error                           | 1 row     |
| Typos / Inconsistent Casing | Gender has entries like "male", "FEMALE" instead of "Male"/"Female" | 2 rows    |
| Outlier                     | Study_Hours_Per_Day = 15.0 (impossible for a daily value)           | 1 row     |

Preprocessing needed (Lesson 3):

- Impute or drop missing values
- Standardize the Gender column (lowercase/uppercase normalization)
- Remove duplicate rows
- Cap or remove the outlier in Study_Hours_Per_Day
- Encode categorical variables (Gender, Part_Time_Job) using Label Encoding or One-Hot Encoding
- Scale numerical features using Min-Max or Standard Scaler

# 5\. Learning Type - Supervised Learning

This is a Supervised Learning problem because:

- We have a clearly defined label (y) - the GPA column
- Every row has a known output value paired with its input features
- The goal is to learn a mapping from features X → label y, so the model can predict GPA for new students
- Quote: "Supervised learning requires labeled data - data where the correct output is already known." - Lesson 2
- Since GPA is a continuous numerical value (1.0 to 4.0), this is specifically a Regression task, not classification.

# 6\. Use Case & Data Science Lifecycle Fit

ML Use Case Table:

| **Task**           | **Description**                                                                              |
| ------------------ | -------------------------------------------------------------------------------------------- |
| Regression         | Predict a student's GPA based on their lifestyle habits                                      |
| Classification     | Predict Pass/Fail by converting GPA to a binary label (e.g., GPA ≥ 2.0 = Pass)               |
| Feature Importance | Identify which habits (study hours, sleep, social media) most influence academic performance |

Data Science Lifecycle Table:

| **Phase**                     | **How This Dataset Fits**                                   |
| ----------------------------- | ----------------------------------------------------------- |
| 1\. Problem Definition        | Can we predict student GPA from lifestyle habits?           |
| 2\. Data Collection           | Survey distributed to 55+ students - Done                   |
| 3\. Data Preprocessing        | Handle missing values, typos, outliers, encoding - Lesson 3 |
| 4\. Exploratory Data Analysis | Correlate study hours vs GPA, attendance vs GPA             |
| 5\. Modeling                  | Train a Linear Regression or Decision Tree model            |
| 6\. Evaluation                | Use RMSE, MAE, or R² score to evaluate predictions          |
| 7\. Deployment                | A student advisory tool that flags at-risk students         |