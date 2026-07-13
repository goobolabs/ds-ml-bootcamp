# Diabetes Prediction Using Machine Learning

**FINAL PROJECT PROPOSAL**

**CERTIFICATE NAME:** Mohamed Abdalle Aden

*A Supervised Machine Learning Classification Project*

Dataset Source: Kaggle — Diabetes Prediction Dataset
Deployment: FastAPI | Primary Metric: F1 Score

---

## 1. Certificate Name

**Mohamed Abdalle Aden**

## 2. Project Title and Description

**Project Title:**
Diabetes Prediction Using Machine Learning

**Project Description:**

Diabetes is one of the most common chronic diseases worldwide. Early prediction can help patients receive timely medical care and reduce the risk of serious complications. The goal of this project is to build a machine learning model that predicts whether a person is likely to have diabetes based on health-related information such as age, BMI, blood glucose level, HbA1c level, hypertension, heart disease, and smoking history. This system can assist healthcare professionals by providing a quick prediction that supports early screening and decision-making.

This project is also personally motivated: my father lives with diabetes, and seeing the daily impact of the disease on his life inspired me to explore how machine learning can support earlier detection and better health outcomes for patients like him.

## 3. Problem Type

**Classification**

This project is a supervised machine learning classification problem. The model will predict one of two classes:

- 0 = No Diabetes
- 1 = Diabetes

## 4. Dataset

**Source:**
Kaggle — Diabetes Prediction Dataset
https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset

**Dataset Size:**
Above 1,000 rows and 9 columns.

**Target Column:**
- diabetes — 0 = No Diabetes, 1 = Diabetes

**Main Features:**

| Feature | Description |
| --- | --- |
| gender | Gender of the patient |
| age | Age in years |
| hypertension | Whether the patient has hypertension |
| heart_disease | Whether the patient has heart disease |
| smoking_history | Smoking status |
| bmi | Body Mass Index |
| HbA1c_level | Average blood sugar level over the past few months |
| blood_glucose_level | Current blood glucose level |

*These features will be used to predict whether a patient has diabetes.*

## 5. Algorithms I Plan to Train

**1. Logistic Regression**
Used as a baseline model because it is simple, fast, and performs well for binary classification problems.

**2. Decision Tree Classifier**
Can learn complex decision rules and is easy to interpret.

**3. Random Forest Classifier**
Combines many decision trees to improve prediction accuracy and reduce overfitting.

**4. Support Vector Machine (Optional)**
May also be compared because SVM often performs well on classification datasets with clear class boundaries.

## 6. Evaluation Plan

All models will be evaluated using the following metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

The F1 Score will be the primary metric for selecting the best model because it balances Precision and Recall, making it more reliable when the classes are not perfectly balanced.

## 7. Deployment Sketch

The best-performing model will be deployed using FastAPI.

**Input**

The `/predict` endpoint will accept JSON data such as:

```json
{
  "gender": "Male",
  "age": 45,
  "hypertension": 1,
  "heart_disease": 0,
  "smoking_history": "never",
  "bmi": 31.2,
  "HbA1c_level": 6.8,
  "blood_glucose_level": 180
}
```

**Output**

The API will return a prediction and probability. Example:

```json
{
  "prediction": "Diabetes",
  "probability": 0.94
}
```

## 8. Repository Plan

The project repository will be organized as follows:

```
diabetes-prediction-project/
|
|-- dataset/
|   |-- diabetes_prediction_dataset.csv
|
|-- notebooks/
|   |-- diabetes_prediction.ipynb
|
|-- src/
|   |-- preprocess.py
|   |-- train.py
|   |-- evaluate.py
|
|-- api/
|   |-- app.py
|
|-- models/
|   |-- diabetes_model.pkl
|
|-- README.md
|
|-- project_paper.md
```

The repository will contain the dataset, preprocessing scripts, model training code, evaluation scripts, the trained model, the FastAPI application, project documentation, and the final project report. This structure will keep the project organized and easy to maintain.
