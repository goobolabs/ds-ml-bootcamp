# Final Project Proposal

**Date:** July 2026

---

# 1. Certificate Name

**Abdullahi Hassan Shire**

---

# 2. Project Title and Description

## Title

**Student Academic Performance Prediction System Using Machine Learning**

## Description

Educational institutions collect large amounts of student data, including attendance records, study habits, previous academic performance, and demographic information. Analyzing this information can help identify students who may need additional academic support before their final examinations.

The goal of this project is to develop a machine learning system that predicts whether a student is likely to pass or fail based on academic and personal characteristics. The system will assist teachers and school administrators in identifying at-risk students early, allowing timely interventions to improve academic performance.

The final model will be deployed using **FastAPI**, providing a REST API that accepts student information and returns a prediction. This project demonstrates the complete machine learning workflow, including data preprocessing, model training, evaluation, comparison of multiple algorithms, and deployment.

---

# 3. Problem Type

## Classification (Supervised Learning)

The objective of this project is to predict whether a student will successfully pass or fail.

### Output

* Pass
* Fail

---

# 4. Dataset

## Source

**Student Performance Dataset (Kaggle)**

https://www.kaggle.com/datasets

(A student performance dataset containing more than 1,000 records will be selected.)

## Dataset Size

* More than 1,000 rows
* Multiple numerical and categorical features

## Target Column

`Final_Result`

### Classes

* Pass
* Fail

## Main Features

* Age
* Gender
* Study Hours
* Attendance
* Previous Grades
* Internet Access
* Parent Education
* Family Support
* School Type
* Extra Classes

## Preprocessing Plan

* Perform Exploratory Data Analysis (EDA).
* Remove duplicate records.
* Handle missing values.
* Encode categorical variables.
* Scale numerical features.
* Detect and treat outliers.
* Perform feature selection.
* Split the dataset into training and testing sets.

---

# 5. Algorithms I Plan to Train

## Logistic Regression

A simple and interpretable classification algorithm that will be used as the baseline model.

## Decision Tree Classifier

A tree-based algorithm capable of learning complex decision rules from the data.

## Random Forest Classifier

An ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting. It is expected to produce the best performance.

---

# 6. Evaluation Plan

The following classification metrics will be used to compare all models:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

The best model will be selected based on the **highest F1-Score**, since it balances Precision and Recall and provides a reliable evaluation for classification problems.

After selecting the best-performing model, at least three sanity checks will be performed using sample student records to verify that the predictions are reasonable.

---

# 7. Deployment Sketch

## Backend

* FastAPI
* REST API
* Interactive API documentation (`/docs`)

## API Endpoint

### Student Performance Prediction

```http
POST /predict
```

### Example Input

```json
{
  "age": 18,
  "gender": "Male",
  "study_hours": 4,
  "attendance": 92,
  "previous_grade": 78,
  "internet_access": "Yes",
  "family_support": "Yes"
}
```

### Example Output

```json
{
  "prediction": "Pass",
  "probability": 0.94
}
```

The API will preprocess the input data, load the trained machine learning model, generate a prediction, and return the result as a JSON response.

---

# 8. Repository Plan

```text
student-performance-prediction/
│
├── dataset/
│   ├── raw_student_data.csv
│   └── clean_student_data.csv
│
├── notebooks/
│   ├── eda.ipynb
│   └── model_training.ipynb
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
├── api/
│   └── app.py
│
├── models/
│   ├── best_model.pkl
│   ├── scaler.pkl
│   └── encoder.pkl
│
├── requirements.txt
├── README.md
└── project_paper.md
```

## Planned Commands

```bash
python src/train.py

uvicorn api.app:app --reload
```

---

# 9. Expected Outcome

This project is expected to produce an accurate machine learning model capable of predicting student academic performance. The final system will compare three classification algorithms, select the best-performing model based on evaluation metrics, and deploy it through a FastAPI REST API. The completed project will demonstrate practical skills in data preprocessing, supervised machine learning, model evaluation, API development, and software project organization.
