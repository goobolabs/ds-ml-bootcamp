Title & Collection Method

This project focuses on a dataset called “Student Study Habits and Exam Performance Dataset.” The main goal of this dataset is to understand how different student behaviors affect academic performance, especially exam outcomes.

The dataset was collected using a survey-based manual data collection method. Fifty (50) students were asked questions related to their daily study habits, attendance, and social media usage. The responses were recorded manually and organized into a structured dataset.

The key idea behind this dataset is to explore whether student lifestyle factors can be used to predict exam success. This makes the dataset useful for applying machine learning concepts learned in Data Foundations for Machine Learning.

2. Description of Features & Label

The dataset contains 5 input features (X) and 1 output label (y).

Features (X):
Age – The age of the student in years.
Gender – The gender of the student (Male/Female).
Study_Hours – The number of hours the student studies per day.
Attendance – The percentage of class attendance.
Social_Media_Hours – The number of hours spent on social media daily.
Label (y):
Pass_Status – This is the target variable.
1 = Pass
0 = Fail

The purpose of the label is to determine whether a student passes or fails an exam based on their habits and behavior.

3. Dataset Structure

The dataset consists of:

50 rows (samples)
6 columns (5 features + 1 label)
Sample Data (First 10 Rows)
Age	Gender	Study_Hours	Attendance	Social_Media_Hours	Pass_Status
19	M	4	90	2	1
20	F	3	85	3	1
18	M	1	60	6	0
22	F	5	95	1	1
21	M	2	70	5	0
20	F	4	88	2	1
19	M	2	75	4	0
23	F	6	97	1	1
18	M	1	55	7	0
21	F	3	82	3	1

This structure allows the dataset to be used for machine learning tasks such as classification.

4. Quality Issues

Although the dataset is structured, it may contain several real-world data quality problems:

1. Missing Values

Some students may skip survey questions, leading to missing values in fields such as study hours or social media usage. Missing data can reduce model accuracy if not handled properly.

2. Typographical Errors

Data entry mistakes may occur, such as inconsistent gender values (“M”, “Male”, “male”) or incorrect numerical entries. These errors can affect data consistency.

3. Duplicate Records

There is a possibility of repeated entries for the same student. Duplicate data can bias the model and make results less reliable.

4. Inconsistent Data Formats

Some values may be recorded in different formats, such as attendance written as “90%” instead of “90”. This inconsistency must be cleaned during preprocessing.

5. Class Imbalance

The dataset may contain more “Pass (1)” values than “Fail (0)” values. This imbalance can cause the model to favor the majority class and reduce prediction fairness.

6. Outliers

Unusual values such as extremely high study hours or unrealistic attendance percentages may exist. These outliers can negatively affect model training.

5. Learning Type

This dataset is designed for Supervised Machine Learning, specifically a Classification problem.

This is because:

The dataset contains a clear label (Pass_Status).
The goal is to predict a category (Pass or Fail).
The model learns from labeled examples.
6. Use Case & Data Science Lifecycle
Use Case

This dataset can be used to build a machine learning model that predicts whether a student will pass or fail an exam based on their study habits and lifestyle factors. It can also help educators identify students who may need academic support.

Machine Learning Task
Type: Classification
Output: Pass or Fail prediction
Data Science Lifecycle Application
Data Collection – Survey responses from students.
Data Cleaning – Handling missing values, duplicates, and errors.
Data Exploration – Understanding relationships between study habits and performance.
Model Building – Training a classification model (e.g., Logistic Regression, Decision Tree).
Evaluation – Measuring accuracy, precision, and recall.
Deployment – Using the model to predict future student performance.
