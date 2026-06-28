# Practical Assignment: Data Foundations for Machine Learning

# Project Overview

This project demonstrates the fundamental concepts of Data Science and Machine Learning through the creation of an original dataset. Instead of using an existing public dataset, the data was collected using a self-designed Google Forms survey. The survey focuses on internet usage and daily lifestyle habits of participants.

The purpose of this project is to understand how raw data is collected, organized, analyzed, and prepared before it is used in Machine Learning models.

---

# Dataset Description

The dataset contains responses collected from **52 participants**.

Each participant answered questions related to their daily internet usage, social media activity, study/work habits, and lifestyle.

The dataset contains both categorical and numerical variables, making it suitable for practicing data preprocessing techniques.

---

# Data Collection Method

The data was collected through a Google Forms questionnaire.

Steps followed:

1. Designed the survey.
2. Shared the survey with participants.
3. Collected responses.
4. Exported the responses as a CSV file.
5. Prepared the data for Machine Learning.

Because the data was collected directly from participants, it is considered an original dataset.

---

# Features (Input Variables)

The independent variables (X) include information such as:

- Age
- Gender
- Daily Internet Usage
- Social Media Usage
- Online Gaming Hours
- Sleeping Hours
- Study Hours
- Work Hours

These variables describe the participants and can be used as input features for Machine Learning.

---

# Target Variable (Label)

For this assignment, the selected target variable is:

**Study/Work Hours**

This variable can be predicted using the remaining features.

---

# Dataset Structure

- Total Samples: **52**
- Total Features: **Based on the survey columns**
- File Format: CSV
- Source: Self-collected using Google Forms

Example:

| Age | Gender | Internet Hours | Social Media | Study Hours |
|-----|--------|---------------|--------------|------------|
| 22 | Male | 5 | High | 4 |
| 20 | Female | 6 | Medium | 5 |
| 24 | Male | 8 | High | 2 |
| 19 | Female | 4 | Low | 6 |
| 23 | Male | 7 | Medium | 3 |

---

# Data Quality Issues

Although the dataset is usable, several quality issues may exist:

- Missing values
- Typographical errors
- Different text formats
- Duplicate responses
- Mixed categorical and numerical data

These issues should be handled during preprocessing.

---

# Data Preprocessing

Before training a Machine Learning model, the following preprocessing steps should be performed:

- Remove duplicate records
- Handle missing values
- Encode categorical variables
- Normalize numerical values if necessary
- Detect and remove outliers
- Verify data consistency

These steps improve model accuracy and reliability.

---

# Learning Type

This dataset represents a **Supervised Learning** problem because a target variable (Study/Work Hours) has been selected.

The model learns the relationship between input features and the target variable.

If no target variable were selected, the same dataset could also be used for **Unsupervised Learning**, such as clustering participants with similar internet usage habits.

---

# Machine Learning Applications

This dataset can be used for several Machine Learning tasks:

## Classification

Predict whether a participant studies many or few hours.

## Regression

Predict the exact number of study/work hours.

## Clustering

Group participants with similar online behavior.

---

# Data Science Lifecycle

This project follows the Data Science lifecycle:

1. Problem Definition
2. Data Collection
3. Data Cleaning
4. Data Preprocessing
5. Exploratory Data Analysis
6. Machine Learning Model Development
7. Model Evaluation
8. Deployment

---

# Tools Used

- Google Forms
- CSV Dataset
- Microsoft Excel
- Git & GitHub
- Python (planned for preprocessing and model building)

---

# Conclusion

This project demonstrates the complete process of creating a dataset from scratch for Machine Learning. The collected data provides practical experience in understanding features, labels, dataset quality, preprocessing, and selecting an appropriate Machine Learning approach.

The dataset can be expanded with additional participants and features in future work to improve model performance and produce more accurate predictions.

---

# Repository Contents

```
README.md
ASSIGMENT 2.csv
```

---

## Author

**Mohamed Hajji**

Data Foundations for Machine Learning Assignment