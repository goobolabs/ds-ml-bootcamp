# Telecom Customer Churn Prediction Using Machine Learning

## Project Overview

Customer churn is one of the biggest challenges faced by telecommunication companies. Losing existing customers reduces revenue and increases customer acquisition costs. This project uses machine learning to predict whether a customer is likely to leave a telecom service based on demographic information, account details, subscribed services, and billing information.

The goal is to help telecom companies identify at-risk customers and take proactive actions to improve customer retention.

---

## Dataset

**Source:** IBM Telco Customer Churn Dataset

Dataset Link:
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

### Dataset Information

* Rows: 7,043
* Columns: 21
* Target Variable: Churn

### Target Classes

* 0 = No Churn
* 1 = Churn

---

## Data Preprocessing

The following preprocessing steps were applied:

* Converted TotalCharges to numeric format
* Handled missing values using median imputation
* Removed customerID column
* Encoded categorical features using Label Encoding
* Scaled features using StandardScaler
* Split data into training and testing sets (80/20)

---

## Algorithms Trained

Three classification algorithms were trained and evaluated:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier

All models were trained using the same train-test split to ensure a fair comparison.

---

## Model Comparison

| Model               | Accuracy | Precision | Recall | F1 Score |
| ------------------- | -------- | --------- | ------ | -------- |
| Logistic Regression | 0.7991   | 0.6426    | 0.5481 | 0.5916   |
| Decision Tree       | 0.7303   | 0.4924    | 0.5187 | 0.5052   |
| Random Forest       | 0.7899   | 0.6345    | 0.4920 | 0.5542   |

### Best Model

Logistic Regression achieved the highest F1 Score (0.5916) and was selected as the final deployed model.

F1 Score was chosen as the primary evaluation metric because customer churn prediction is a classification problem where balancing Precision and Recall is important.

---

## Evaluation Results

Best Model: Logistic Regression

* Accuracy: 0.7991
* Precision: 0.6426
* Recall: 0.5481
* F1 Score: 0.5916

### Sanity Checks

Sample 1 → Prediction: No Churn

Sample 2 → Prediction: Churn

Sample 3 → Prediction: No Churn

A confusion matrix was generated and saved in the images folder.

---

## Project Structure

telecom-customer-churn-prediction/

* dataset/
* notebooks/
* src/
* api/
* models/
* images/
* README.md
* project_paper.md
* requirements.txt

---

## Running the Project

### Install Dependencies

pip install -r requirements.txt

### Data Preprocessing

python src/preprocess.py

### Train Models

python src/train.py

### Evaluate Best Model

python src/evaluate.py

### Run API

uvicorn api.app:app --reload

---

## API Endpoint

### POST /predict

Example JSON Input:

{
"gender": 1,
"SeniorCitizen": 0,
"Partner": 1,
"Dependents": 0,
"tenure": 24,
"PhoneService": 1,
"MultipleLines": 0,
"InternetService": 1,
"OnlineSecurity": 1,
"OnlineBackup": 0,
"DeviceProtection": 1,
"TechSupport": 1,
"StreamingTV": 0,
"StreamingMovies": 1,
"Contract": 1,
"PaperlessBilling": 1,
"PaymentMethod": 2,
"MonthlyCharges": 75.5,
"TotalCharges": 1800
}

Example Response:

{
"prediction": 0,
"churn": "No"
}

---

## Results Summary

Three machine learning classification models were trained and compared for customer churn prediction. Logistic Regression achieved the highest F1 Score and was selected as the final model. The model was successfully deployed using FastAPI and exposed through a working /predict endpoint.

