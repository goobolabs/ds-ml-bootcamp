# Final Project Proposal

## 1. Certificate Name

**Hibo Mohamed Omar**



# 2. Project Title and Description

## Project Title

**Telecom Customer Churn Prediction Using Machine Learning**

### Project Description

Customer churn is one of the biggest challenges faced by telecommunication companies because losing existing customers reduces revenue and increases customer acquisition costs. This project aims to build a machine learning model that predicts whether a customer is likely to leave a telecom service based on customer demographics, account information, subscribed services, and billing details. The prediction will help telecom companies identify at-risk customers early and take proactive retention actions, ultimately improving customer satisfaction and business performance.



# 3. Problem Type

**Classification**

This is a binary classification problem because the model predicts whether a customer will **Churn (Yes)** or **Not Churn (No)**.



# 4. Dataset

### Dataset Source

**Kaggle – IBM Telco Customer Churn Dataset**

https://www.kaggle.com/datasets/blastchar/telco-customer-churn

### Dataset Size

* Approximately **7,043 rows**
* **21 columns**

This satisfies the project requirement of at least 1,000 rows.

### Target Column

**Churn**

The target column indicates whether a customer left the telecom company.

* Yes = Customer left
* No = Customer stayed

### Main Features

The model will use the following features:

* Gender
* SeniorCitizen
* Partner
* Dependents
* Tenure
* PhoneService
* MultipleLines
* InternetService
* OnlineSecurity
* OnlineBackup
* DeviceProtection
* TechSupport
* StreamingTV
* StreamingMovies
* Contract
* PaperlessBilling
* PaymentMethod
* MonthlyCharges
* TotalCharges

These features describe customer demographics, subscription details, billing information, and service usage that may influence customer churn.



# 5. Algorithms You Plan to Train

### 1. Logistic Regression

Logistic Regression is a strong baseline classification algorithm that is simple, interpretable, and performs well for binary classification problems.

### 2. Decision Tree Classifier

Decision Trees can capture nonlinear relationships between customer attributes and churn while providing easy-to-understand decision rules.

### 3. Random Forest Classifier

Random Forest combines multiple decision trees to improve prediction accuracy and reduce overfitting, making it one of the most reliable classification algorithms.

### (Optional)

If time allows, I will also experiment with **XGBoost** to compare its performance with the other models.



# 6. Evaluation Plan

The models will be evaluated using the following metrics:

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC Score

### Best Model Selection

The primary evaluation metric will be **F1-Score** because customer churn datasets are often imbalanced. F1-Score provides a balanced measure by considering both Precision and Recall, making it more suitable than Accuracy alone.



# 7. Deployment Sketch

The trained model will be deployed using **FastAPI**.

### Input

The `/predict` endpoint will accept customer information in JSON format, including fields such as:

* Gender
* SeniorCitizen
* Partner
* Tenure
* InternetService
* Contract
* MonthlyCharges
* TotalCharges

### Output

The API will return:

* Predicted Churn (Yes or No)
* Probability of Churn

Example response:

```json
{
    "prediction": "Yes",
    "probability": 0.91
}
```

---

# 8. Repository Plan

```
telecom-customer-churn-prediction/
│
├── dataset/
│   └── telco_customer_churn.csv
│
├── notebooks/
│   └── telecom_churn_analysis.ipynb
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
│   └── churn_model.pkl
│
├── images/
│
├── README.md
├── requirements.txt
├── project_paper.md
└── .gitignore
```

This repository structure separates the dataset, source code, trained models, API, documentation, and project report, making the project organized, maintainable, and easy to understand.
