# Workforce Performance Prediction Using Human Resource Data from Amal Bank Puntland

**Author:** Eng Shiine
**Course:** DS-ML Bootcamp — Assignment 2
**Dataset:** Amal Bank Puntland HR Dataset
**Submission Date:** June 2026

---

# Table of Contents

1. Collection Method
2. Features and Label
3. Dataset Structure
4. Data Quality Issues
5. Learning Type
6. Machine Learning Use Cases
7. Position in the Data Science Lifecycle
8. Conclusion

---

# 1. Collection Method

Human Resource (HR) departments generate large amounts of workforce data every day. Employee information such as experience, salary, department, performance ratings, and employment status can provide valuable insights into organizational performance and workforce management.

For this assignment, a Human Resource dataset was created to represent employee records collected from different branches of Amal Bank operating across Puntland, Somalia. The dataset focuses on understanding factors that may influence employee performance and workforce outcomes within the banking sector.

The data was manually compiled through observation of HR-style employee records and organizational workforce structures commonly found in Somali financial institutions. To protect privacy, all employee information was anonymized and represented using fictional but realistic Somali names.

Data collection focused on six branch locations:

* Garowe
* Bosaso
* Galkacyo
* Qardho
* Burtinle
* Dangorayo

The final dataset contains 66 employee records representing staff from different departments including:

* Information Technology (IT)
* Finance
* Human Resources (HR)
* Operations
* Sales
* Marketing

Each employee record contains information related to employment history, work arrangement, salary level, experience, and performance evaluation.

The purpose of collecting this dataset is to explore how workforce characteristics relate to employee performance and how Machine Learning could support HR decision-making.

---

# 2. Features and Label

In Machine Learning, data is divided into:

* Features (X): Input variables used for prediction.
* Label (y): Target variable the model learns to predict.

For this project, the goal is to predict employee performance.

## Features (X)

| No. | Feature          | Type        | Description           |
| --- | ---------------- | ----------- | --------------------- |
| 1   | Employee_ID      | Identifier  | Unique employee code  |
| 2   | Department       | Categorical | Employee department   |
| 3   | Job_Title        | Categorical | Position held         |
| 4   | Hire_Date        | Date        | Employment start date |
| 5   | Location         | Categorical | Branch location       |
| 6   | Experience_Years | Numerical   | Years of experience   |
| 7   | Status           | Categorical | Active or Resigned    |
| 8   | Work_Mode        | Categorical | On-site or Hybrid     |
| 9   | Salary_USD       | Numerical   | Monthly salary        |

## Label (y)

| Label              | Type      | Values |
| ------------------ | --------- | ------ |
| Performance_Rating | Numerical | 1–5    |

The Performance Rating represents employee evaluation scores assigned by management.

A rating of:

* 1 = Poor Performance
* 2 = Below Average
* 3 = Average
* 4 = Good
* 5 = Excellent

The Machine Learning model would learn how employee characteristics influence performance ratings.

---

# 3. Dataset Structure

The dataset contains:

| Property             | Value |
| -------------------- | ----- |
| Total Rows (Samples) | 66    |
| Total Columns        | 11    |
| Features             | 10    |
| Label                | 1     |

## Sample Records

| Employee_ID | Department | Location | Experience | Salary | Performance |
| ----------- | ---------- | -------- | ---------- | ------ | ----------- |
| EMP001      | IT         | Garowe   | 8          | 1200   | 4           |
| EMP002      | Finance    | Bosaso   | 5          | 800    | 3           |
| EMP003      | HR         | Garowe   | 3          | 700    | 4           |
| EMP004      | Operations | Galkacyo | 10         | 1300   | 5           |
| EMP005      | Marketing  | Qardho   | 4          | 650    | 3           |
| EMP006      | IT         | Bosaso   | 2          | 900    | 4           |
| EMP007      | Finance    | Garowe   | 11         | 1500   | 5           |

Several preliminary patterns can already be observed. Employees with greater experience and higher-level positions generally receive higher salaries and stronger performance ratings.

---

# 4. Data Quality Issues

Real-world datasets are rarely clean. The HR dataset intentionally contains several quality issues that require preprocessing.

## Missing Values

Some records contain missing values in:

* Salary_USD
* Performance_Rating

Machine Learning algorithms cannot directly process missing data.

### Solution

* Numerical values → Mean or Median Imputation
* Categorical values → Mode Imputation

---

## Duplicate Records

One employee record appears twice within the dataset.

Duplicate observations can bias analysis and cause the model to overemphasize a specific employee profile.

### Solution

Remove duplicate rows during preprocessing.

---

## Class Imbalance

Most employees have ratings between 3 and 5.

Very few employees receive ratings of 1 or 2.

This creates an imbalance problem where the model may become biased toward predicting higher ratings.

### Solution

* Oversampling minority classes
* Undersampling majority classes
* Synthetic data generation techniques

---

## Date Formatting Issues

Hire dates may appear in different formats.

Examples:

* 2018-03-12
* 03/12/2018

Machine Learning models require a standardized format.

### Solution

Convert all dates into a consistent datetime format before analysis.

---

## Categorical Encoding Challenges

Columns such as:

* Department
* Job_Title
* Location
* Status
* Work_Mode

must be converted into numerical form.

### Solution

Apply Label Encoding or One-Hot Encoding.

---

# 5. Learning Type

This dataset represents a **Supervised Learning** problem.

The reason is simple:

Every employee already has a known Performance Rating.

The model can examine employee characteristics and learn how those characteristics relate to performance outcomes.

Supervised Learning works like studying with an answer sheet. The model sees both the employee information and the correct performance rating during training.

## Why Not Unsupervised Learning?

Unsupervised Learning is used when there is no target variable.

Since this dataset contains a clearly defined label (Performance Rating), it belongs to the supervised learning category.

---

# 6. Machine Learning Use Cases

The dataset supports several Machine Learning applications.

## Employee Performance Prediction

A model could predict future employee performance using experience, salary, department, and location.

### Suitable Algorithms

* Random Forest
* Decision Tree
* XGBoost

---

## Workforce Classification

Employees can be categorized into:

* High Performers
* Average Performers
* Low Performers

This allows management to identify training needs.

---

## Salary Analysis

The dataset can be used to study relationships between:

* Experience
* Department
* Performance
* Salary

This supports fair compensation planning.

---

## Employee Retention Analysis

By studying employee status (Active vs Resigned), management could identify patterns linked to turnover.

---

# 7. Position in the Data Science Lifecycle

This project demonstrates the first stages of the Data Science Lifecycle.

| Stage                | Status      |
| -------------------- | ----------- |
| Problem Definition   | Completed   |
| Data Collection      | Completed   |
| Data Cleaning        | Next Lesson |
| Exploratory Analysis | Next Lesson |
| Modeling             | Future Step |
| Evaluation           | Future Step |
| Deployment           | Future Step |

The assignment primarily focuses on Data Collection and Dataset Understanding, which form the foundation of every successful Data Science project.

---

# 8. Conclusion

This project developed a Human Resource dataset representing employees from Amal Bank branches across Puntland, Somalia. The dataset contains workforce information such as department, experience, salary, work mode, and performance ratings.

Although the dataset includes realistic quality issues such as missing values and duplicate records, these challenges reflect the realities of real-world organizational data. After preprocessing, the dataset can be used for supervised Machine Learning tasks including employee performance prediction, workforce classification, and HR analytics.

The project demonstrates how data collection serves as the foundation of the Data Science lifecycle and prepares the dataset for future Machine Learning applications.
