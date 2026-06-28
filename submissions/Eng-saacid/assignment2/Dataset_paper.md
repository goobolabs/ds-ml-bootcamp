# Employee Salary Prediction Dataset
---
## Practical Assignment: Data Foundations for Machine Learning

---

## 1. Introduction

Data Science is the process of collecting, organizing, analyzing, and interpreting data to extract useful information and support decision-making. Machine Learning is a branch of Data Science that enables computers to learn patterns from data and make predictions without being explicitly programmed.

This project focuses on an Employee Salary Prediction Dataset. The purpose of the dataset is to understand how employee characteristics such as age, education level, work experience, and job level influence salary. The dataset can later be used to build a machine learning model that predicts employee salaries.

---

## 2. Data Collection Method

The dataset was created manually by recording employee-related information. Data was collected through observation and manual entry into a spreadsheet. Information such as age, education level, years of experience, job level, and salary was recorded.

A total of **50 employee records** were collected.

The dataset was created specifically for this assignment and was not taken from Kaggle, UCI, or any other public dataset repository.

---

## 3. Features and Label

Machine Learning datasets contain features (inputs) and labels (outputs).

### Features (X)

1. Employee_ID
2. Age
3. Education
4. Experience_Years
5. Job_Level

### Label (y)

* Salary

The features describe the characteristics of employees, while the label represents the salary that a machine learning model will attempt to predict.

---

## 4. Dataset Structure

The dataset contains:

* Number of Rows (Samples): 50
* Number of Columns: 6
* Features: 5
* Label: 1

### Sample Records

| Employee_ID | Age | Education | Experience_Years | Job_Level | Salary    |
| ----------- | --- | --------- | ---------------- | --------- | --------- |
| 1           | 22  | Bachelor  | 1                | Junior    | 400       |
| 2           | 23  | Bachelor  | 1                | Junior    | 420       |
| 3           | 24  | Diploma   | 2                | Junior    | 450       |
| 4           | 25  | Bachelors | 2                | Junior    | 480       |
| 5           | 26  | Bachelor  | 3                | Junior    | *Missing* |

---

## 5. Data Quality Issues

Real-world datasets often contain quality issues that must be addressed before machine learning can be applied.

The following issues exist in this dataset:

* Missing values in some records (e.g., Salary and Education).
* Duplicate records (one employee record appears more than once).
* Inconsistent naming formats (e.g., "Bachelor" and "Bachelors", "Master" and "Masters").
* Possible data entry errors during manual collection.

These issues will be handled during data preprocessing through cleaning, encoding, validation, and duplicate removal.

---

## 6. Learning Type

This dataset is suitable for **Supervised Learning** because it contains a clearly defined target variable (**Salary**).

The machine learning algorithm will learn the relationship between employee characteristics and salary values.

This problem is specifically a **Regression Problem** because the output variable (Salary) is a continuous numerical value.

---

## 7. Use Case and Data Science Lifecycle

This dataset can be used to build a machine learning model that predicts employee salaries based on employee characteristics.

Possible applications include:

* Employee salary prediction.
* Human resource planning.
* Compensation analysis.
* Recruitment and hiring support.
* Workforce management systems.

Within the Data Science lifecycle, this dataset belongs primarily to the following stages:

1. Data Collection
2. Data Understanding
3. Data Preparation
4. Model Building
5. Evaluation and Deployment

---

## 8. Conclusion

 

The Employee Salary Prediction Dataset provides a practical example of data collection and preparation for machine learning. The dataset contains meaningful employee-related features and a numerical target variable, making it suitable for supervised machine learning regression tasks.

Future work will include preprocessing the data, handling missing values and duplicates, performing exploratory data analysis, training machine learning models, and evaluating prediction performance.

