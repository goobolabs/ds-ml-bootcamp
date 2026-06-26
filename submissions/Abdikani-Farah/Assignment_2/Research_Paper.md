# Water Intake & Health Survey (Biyo Cabis & Caafimaad): A Self-Collected Dataset for Machine Learning

## Introduction

This research paper presents a self-collected dataset titled **“Water Intake & Health Survey (Biyo Cabis & Caafimaad)”**. The dataset was created to explore the relationship between daily water intake and lifestyle factors such as sleep duration, exercise habits, weight, and overall energy level.

Hydration is widely believed to affect human energy, productivity, and physical well-being. This dataset provides a practical foundation for machine learning, especially for learning how to work with real-world data that contains messy values, inconsistent formats, and data quality issues that require preprocessing.

---

## Dataset Collection Method

The dataset was collected using a survey questionnaire.

### Collection Process

1. A survey form was created with questions related to hydration and daily lifestyle habits.
2. The form was shared with different participants.
3. Responses were collected and exported into a CSV file.
4. The final dataset contains **52 responses (samples)**.

### Why is this Dataset Self-Collected?

This dataset is self-collected because the data was gathered directly from respondents and was not taken from any pre-made dataset repository such as Kaggle, UCI Machine Learning Repository, or any other online source.

---

## Features and Label (X and y)

### Input Features (X)

The dataset contains the following input features:

* **Age** – respondent age (numeric)
* **Gender** – respondent gender (categorical)
* **Weight (kg)** – respondent weight (numeric, but contains mixed formats such as “59kg”)
* **Water Intake (Liters)** – daily water consumption (mixed formats such as “1liter”, “2 liter”, “ma ogi”)
* **Exercise Hours per Day** – daily exercise duration (mixed formats such as “30 mins”, “1hour”, “mar mar”)
* **Sleep Hours per Night** – nightly sleep duration (mixed formats such as “6-7 hrs”, “6 saac”)

### Output Label (y)

The dataset contains one primary target variable:

* **Energy Level (1–10)** – self-rated energy level reported by participants.

The goal is to predict energy levels using lifestyle and hydration-related features.

---

## Learning Type

This dataset is primarily a **Supervised Learning** dataset because it contains a clearly defined target variable (**Energy Level**). A machine learning model can learn the relationship between the input features (age, gender, weight, water intake, exercise, and sleep) and the output label (energy level).

The dataset may also be used for **Unsupervised Learning** if the Energy Level column is removed and clustering techniques are applied to identify groups of individuals with similar hydration and lifestyle habits.

---

## Dataset Structure

### Dataset Summary

* **Rows (Samples):** 52
* **Columns:** 7
* **Features:** 6
* **Label:** 1

### Final Clean Column Names (ML-Friendly)

1. Age
2. Gender
3. Weight_kg
4. Water_Intake_L
5. Exercise_Hours
6. Sleep_Hours
7. Energy_Level

### Sample Table (10 Records)

| Age | Gender | Weight | Water Intake        | Exercise          | Sleep         | Energy |
| --- | ------ | ------ | ------------------- | ----------------- | ------------- | ------ |
| 19  | Gabar  | 59kg   | Ugu yaran hal galas | 30 daqiqo subaxdi | 6 ila 7       | 7      |
| 23  | Male   | 59     | ma ogi              | ma sameeyo        | 6 ilaa 5 saac | 10     |
| 20  | Male   | 50     | 1                   | 5                 | 7             | 10     |
| 21  | Lab    | 71kg   | Hal galas le cawa   | 2                 | 7             | 8      |
| 20  | Female | 59     | 1liter              | 1hour             | 7             | 10     |
| 21  | Dhedig | 58     | Text response       | mar mar           | 6saac         | 10     |
| 22  | Dhedig | 60     | 1 litir             | 2hours            | 6hours        | 8      |
| 24  | Male   | 80kg   | 2 liter             | 0                 | 6             | 8.9    |
| 20  | Male   | 60     | 2                   | 5                 | 8             | 8      |
| 22  | Male   | 57kg   | 6 liters            | 30 mins           | 6–7 hrs       | 9      |

---

## Data Quality Issues

Since the dataset was collected from real participants, it contains several common real-world data quality problems.

### 1. Inconsistent Text Formats

Gender values appear in different forms, including:

* Male
* Lab
* Nin
* Female
* Gabar
* Dhedig
* Dumar

These values represent similar categories but use different spellings and languages.

### 2. Mixed Numeric and Text Values

Weight values appear in multiple formats, such as:

* 59
* 59kg
* 58 kg

The unit “kg” will need to be removed during preprocessing.

### 3. Water Intake Format Differences

Water intake responses are not standardized. Examples include:

* 1
* 1liter
* 2 liter
* 6 liters
* ma ogi
* Ugu yaran hal galas

These values require conversion into a consistent numerical format.

### 4. Exercise Data is Not Standardized

Exercise duration appears in different forms, including:

* 30 mins
* 1hour
* 2hours
* mar mar
* ma sameeyo

These entries must be standardized into a common unit.

### 5. Sleep Data Contains Ranges and Text

Examples include:

* 6 ila 7
* 6–7 hrs
* 6 saac
* 7 hour

These values require transformation into consistent numerical values.

### 6. Possible Outliers

Some records may contain unusual values such as:

* Water intake of 6 liters per day
* Exercise durations of 5 hours per day

These values should be investigated before model training.

### 7. Possible Data Entry Errors

A few records appear to contain incorrect entries, such as:

* Unrealistic weight values (e.g., 2 kg)
* Incorrect values entered in categorical fields

These errors should be identified and corrected during preprocessing.

---

## Use Cases for Machine Learning

### A. Regression (Supervised Learning)

The dataset can be used to predict a person’s energy level based on hydration and lifestyle factors.

**Features (X):**

* Age
* Gender
* Weight
* Water Intake
* Exercise Hours
* Sleep Hours

**Label (y):**

* Energy Level

### B. Classification

Energy levels can be converted into categories:

* Low Energy (1–4)
* Medium Energy (5–7)
* High Energy (8–10)

Classification algorithms can then be used to predict the category of a participant.

### C. Clustering (Unsupervised Learning)

If the Energy Level column is removed, clustering algorithms can group participants into similar lifestyle profiles, such as:

* High Water Intake + High Energy
* Low Sleep + Low Energy
* Healthy Lifestyle Group

---

## Data Science Lifecycle

This dataset fits into multiple stages of the Data Science Lifecycle:

### 1. Problem Definition

The project aims to investigate whether hydration and lifestyle habits influence energy levels.

### 2. Data Collection

Survey responses were collected directly from participants.

### 3. Data Preparation

The dataset contains inconsistencies, missing information, and mixed formats that require cleaning and preprocessing.

### 4. Model Building

Machine learning models can be trained using the cleaned dataset.

### 5. Model Evaluation

Model performance can be measured using appropriate evaluation metrics.

### 6. Deployment

A trained model could be integrated into a health-monitoring or lifestyle recommendation system.

---

## Conclusion

The **Water Intake & Health Survey (Biyo Cabis & Caafimaad)** dataset is a self-collected dataset containing **52 samples and 7 columns**. It includes both numerical and categorical features related to hydration and lifestyle habits. Because the dataset was collected manually from real participants, it contains realistic data quality issues such as inconsistent formats, mixed text and numerical values, data entry errors, and potential outliers.

The dataset is suitable for machine learning applications including regression, classification, and clustering. It also provides an excellent opportunity to learn data preprocessing techniques such as cleaning, encoding, scaling, and feature engineering before building predictive models.
