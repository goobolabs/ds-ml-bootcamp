Final Project Proposal

Date:10 July 2026

1. Certificate Name

Nasteho Abdi Aden

---

2. Project Title and Description

Project Title

Employee Attrition Prediction API

Project Description

Employee attrition is a major challenge for many organizations because replacing experienced employees is expensive and time-consuming. This project aims to develop a machine learning model that predicts whether an employee is likely to leave a company based on employee information such as age, job role, monthly income, overtime status, work experience, and job satisfaction. The final system will be deployed as a FastAPI REST API that accepts employee information in JSON format and returns an attrition prediction. This project can help Human Resources (HR) departments identify employees who may be at risk of leaving and support employee retention planning.

---

3. Problem Type

Classification (Binary Classification)

This project predicts whether an employee will leave the company (Yes) or stay (No). The target variable is Attrition, making this a supervised machine learning classification problem.

---

4. Dataset

Source: IBM HR Analytics Employee Attrition Dataset (Kaggle)

Link: https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset

Dataset Size:

- Approximately 1,470 rows
- 35 columns

Target Column:

- Attrition (Yes / No)

Main Features:

- Age
- BusinessTravel
- Department
- DistanceFromHome
- Education
- EnvironmentSatisfaction
- Gender
- JobRole
- JobSatisfaction
- MaritalStatus
- MonthlyIncome
- OverTime
- TotalWorkingYears
- YearsAtCompany
- YearsInCurrentRole

---

5. Algorithms I Plan to Train

1. Logistic Regression

This algorithm is simple, fast, and provides a strong baseline for binary classification problems.

2. Decision Tree Classifier

Decision Trees are easy to interpret and can model non-linear relationships between employee characteristics and attrition.

3. Random Forest Classifier

Random Forest combines multiple decision trees to improve prediction accuracy and reduce overfitting, making it well suited for structured HR datasets.

These three algorithms are different, and both Logistic Regression and Decision Tree are covered in the bootcamp.

---

6. Evaluation Plan

All models will be trained using the same train/test split for a fair comparison.

The evaluation metrics will include:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

The F1-Score will be used to select the best model because it balances Precision and Recall, making it suitable for predicting employee attrition where correctly identifying employees who may leave is important.

---

7. Deployment Sketch

The project will use FastAPI.

Endpoint

POST /predict

The API will accept employee information in JSON format, including fields such as:

- Age
- Department
- JobRole
- MonthlyIncome
- OverTime
- JobSatisfaction
- TotalWorkingYears
- YearsAtCompany

The API will return:

- Prediction (Yes or No)
- Probability Score

Example Response:

{
  "prediction": "Yes",
  "probability": 0.91
}

---

8. Repository Plan

employee-attrition-api/
├── dataset/
│   └── employee_attrition.csv
├── src/
│   ├── preprocess.py
│   └── train.py
├── api/
│   └── app.py
├── models/
├── README.md
├── requirements.txt
└── project_paper.md

The repository will include data preprocessing, model training, evaluation, model saving, API deployment, documentation, and the final project paper. The best-performing model will be deployed as a FastAPI REST API after comparing all trained algorithms.