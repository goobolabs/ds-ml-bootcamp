# Data Foundations for Machine Learning: Mobile Phone Usage Dataset

## 1. Title and Collection Method

### Title

**Mobile Phone Usage and Daily Habit Dataset**

### Collection Method

This dataset was created to study how daily habits affect mobile phone usage. The data was collected using a simple survey. Participants answered questions about their age, gender, occupation, sleep hours, study/work hours, and mobile phone usage level.

The survey was shared with people such as students, employees, and unemployed individuals. The responses were recorded manually in Google Sheets. A total of **28 valid samples** were collected for this version of the dataset.

---

## 2. Description of Features and Label

In Machine Learning, **features (X)** are input variables used for prediction, while the **label (y)** is the output we want to predict.

### Features (X)

| Feature          | Description                             |
| ---------------- | --------------------------------------- |
| Age              | Age of the participant                  |
| Gender           | Male or Female                          |
| Occupation       | Student, Employee, or Unemployed        |
| Sleep_Hours      | Hours of sleep per day                  |
| Work_Study_Hours | Hours spent working or studying per day |

### Label (y)

| Label       | Description                                        |
| ----------- | -------------------------------------------------- |
| Phone_Usage | Daily mobile phone usage level (Low, Medium, High) |

The label represents the target variable that a machine learning model will predict.

---

## 3. Dataset Structure

The dataset contains:

* **28 rows (samples)**
* **6 columns**
* **5 features**
* **1 label**

### Sample Data

| Age | Gender | Occupation | Sleep_Hours | Work_Study_Hours | Phone_Usage |
| --- | ------ | ---------- | ----------- | ---------------- | ----------- |
| 24  | Male   | Student    | 7           | 9                | Low         |
| 30  | Female | Unemployed | 3           | 0                | High        |
| 19  | Male   | Student    | 8           | 8                | Low         |
| 21  | Male   | Student    | 8           | 6                | Medium      |
| 35  | Male   | Unemployed | 7           | 7                | High        |

Each row represents one participant and each column represents a feature or label.

---

## 4. Data Quality Issues

This dataset contains several real-world data problems.

### Missing Values

Some responses had missing or unclear values for work/study hours.

### Typographical Errors

Participants used different formats for the same values.

Examples:

* “8 hour”
* “8hours”
* “7 hours”
* “5 or 4 hour per day”
* “30min”

These values must be converted into a standard format.

### Inconsistent Data Formats

Sleep and work hours were written in different formats such as:

* Numbers (8)
* Text (8 hours)
* Ranges (5 or 4 hours)

### Invalid or Unclear Values

Some values are not clear or realistic for machine learning models, such as:

* “30min”
* mixed ranges like “5 or 4 hour per day”

### Small Dataset Size

The dataset currently has only 14 samples, which is small. A larger dataset (50+ rows) is recommended for better machine learning performance.

---

## 5. Learning Type

This is a **Supervised Learning** problem because the dataset includes a clear output label (**Phone_Usage**).

The model learns from input features such as age, occupation, and habits to predict phone usage level.

Since the label has categories (Low, Medium, High), this is a **Classification problem**.

---

## 6. Machine Learning Use Case

This dataset can be used to predict a person’s phone usage level based on daily habits.

Possible applications:

* Digital wellbeing tools
* Screen-time monitoring
* Student behavior analysis
* Productivity tracking systems

Possible algorithms:

* Logistic Regression
* Decision Tree
* Random Forest
* K-Nearest Neighbors (KNN)

---

## 7. Data Science Lifecycle

This dataset fits into the following stages:

| Stage                     | Description                                 |
| ------------------------- | ------------------------------------------- |
| Problem Definition        | Understand phone usage behavior             |
| Data Collection           | Survey responses from participants          |
| Data Cleaning             | Fix missing values and inconsistent formats |
| Exploratory Data Analysis | Find patterns in habits                     |
| Feature Engineering       | Prepare usable features                     |
| Modeling                  | Train ML classification model               |
| Evaluation                | Measure accuracy                            |
| Deployment                | Use model in real applications              |

---

## 8. Conclusion

This dataset was created to analyze how daily habits affect mobile phone usage. It includes real-world data with inconsistencies such as missing values and different formats.

The dataset is suitable for supervised machine learning classification. However, before building a model, the data must be cleaned and standardized. This project demonstrates the importance of data collection, cleaning, and preparation in the Data Science process.
