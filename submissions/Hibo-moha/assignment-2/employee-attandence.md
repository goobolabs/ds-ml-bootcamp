# Employee Attendance and Punctuality Analysis Dataset for Machine Learning

## 1. Title & Collection Method

### Title

Employee Attendance and Punctuality Analysis Dataset for Machine Learning

### Collection Method

This dataset was collected through a Google Form survey distributed to employees working in different departments. The questionnaire gathered information about employee demographics, attendance behavior, arrival times, transportation methods, and workplace punctuality.

A total of 50 employee responses were collected manually. The purpose of collecting this dataset is to analyze factors that influence employee punctuality and attendance and to explore how Machine Learning can be used to predict whether an employee is likely to arrive at work on time or late.

According to the Data Science lifecycle, this project is currently in the Data Collection stage, where relevant data is gathered before preprocessing and analysis.

---

## 2. Description of Features and Label

The dataset contains eight input variables (features X) and one output variable (label y).

### Features (X)

1. Age – Employee age in years.
2. Gender – Employee gender.
3. Department – Department where the employee works.
4. Work_Start_Time – Official starting time of work.
5. Arrival_Time – Actual arrival time of the employee.
6. Minutes_Late – Number of minutes the employee arrived late.
7. Transport_Method – Method of transportation used by the employee.
8. Attendance_Rate – Employee attendance percentage.

### Label (y)

Punctuality_Status

The target variable indicates whether an employee arrived on time or late.

Categories:

* On Time
* Late

The label can be generated from the Minutes_Late column:

* 0 minutes = On Time
* Greater than 0 minutes = Late

---

## 3. Dataset Structure

### Dataset Information

* Number of Rows (Samples): 50
* Number of Columns: 9
* Number of Features: 8
* Number of Labels: 1

### Sample Dataset

| Age | Gender | Department       | Work Start Time | Arrival Time | Minutes Late | Transport Method | Attendance Rate | Punctuality Status |
| --- | ------ | ---------------- | --------------- | ------------ | ------------ | ---------------- | --------------- | ------------------ |
| 25  | Male   | HR               | 8:00 AM         | 8:00 AM      | 0            | Bus              | 90              | On Time            |
| 34  | Female | Public Health    | 8:00 AM         | 8:20 AM      | 20           | Taxi             | 85              | Late               |
| 24  | Male   | Computer Science | 8:00 AM         | 8:00 AM      | 0            | Car              | 95              | On Time            |
| 30  | Female | Management       | 8:30 AM         | 9:00 AM      | 30           | Walk             | 80              | Late               |
| 23  | Male   | IT               | 8:00 AM         | 8:10 AM      | 10           | Bus              | 90              | Late               |

Each row represents one employee, while each column represents a specific attribute collected from the survey.

---

## 4. Quality Issues

The collected dataset contains several quality issues that need preprocessing before Machine Learning modeling.

### Missing and Invalid Values

Some attendance values contain invalid entries such as “A” instead of numerical percentages.

### Inconsistent Formats

Time values appear in different formats, such as:

* 8:00
* 08:00
* 8:00AM
* 8:00 AM

These formats should be standardized.

### Inconsistent Department Names

Examples include:

* IT
* it
* Computer science
* COMPUTER
* Software engineer
* software engneer

These values represent similar categories but are written differently.

### Mixed Numerical Formats

Minutes late values include:

* 10
* 10min
* 12min
* 15 min

These should be converted into a consistent numeric format.

### Categorical Data

Gender, Department, and Transport Method are categorical variables and require encoding before model training.

### Possible Duplicates

Some responses may need verification to ensure no employee submitted multiple responses.

---

## 5. Learning Type

This dataset represents a Supervised Learning problem.

According to Machine Learning concepts, supervised learning uses labeled data where the output variable is known. In this dataset, the target variable is Punctuality_Status.

The Machine Learning model will learn patterns from employee characteristics and attendance behavior and then predict whether an employee is likely to be on time or late.

Because the output belongs to categories rather than numerical values, this is a Classification problem.

---

## 6. Use Case

This dataset can be used to develop a Machine Learning classification model for predicting employee punctuality.

Possible applications include:

* Employee attendance monitoring.
* Predicting employee lateness.
* Human resource analytics.
* Workforce management.
* Improving organizational productivity.
* Identifying factors that contribute to employee lateness.

Organizations can use these insights to improve attendance policies and workplace efficiency.

---

## 7. Data Science Lifecycle

This project follows the Data Science lifecycle discussed in Lesson 1.

### 1. Problem Definition

Determine whether employee punctuality can be predicted using attendance-related factors.

### 2. Data Collection

Collect employee information through Google Forms.

### 3. Data Cleaning and Preprocessing

Handle missing values, correct errors, standardize formats, and encode categorical variables.

### 4. Exploratory Data Analysis (EDA)

Analyze attendance trends, lateness patterns, and relationships among variables.

### 5. Feature Engineering

Create useful variables such as punctuality categories and attendance groups.

### 6. Modeling

Train a Machine Learning classification model.

### 7. Evaluation

Measure the model's prediction accuracy and performance.

### 8. Communication and Deployment

Present findings through reports or dashboards and deploy the model if required.

---

## Conclusion

The Employee Attendance and Punctuality Dataset contains 50 employee records and multiple features related to attendance behavior. The dataset was collected using Google Forms and is suitable for supervised machine learning classification because it contains a clear target variable (Punctuality_Status). After preprocessing and cleaning, the dataset can be used to predict employee punctuality and support data-driven decision-making in organizations.
