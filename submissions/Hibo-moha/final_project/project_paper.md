# Telecom Customer Churn Prediction Using Machine Learning

## 1. Problem Statement and Motivation

Customer churn is a major concern for telecommunication companies. When customers leave a service provider, companies lose recurring revenue and must spend additional resources to acquire new customers. Predicting customer churn can help organizations identify customers who are at risk of leaving and take preventive actions.

The objective of this project is to build a machine learning model that predicts whether a customer will churn based on customer demographics, account information, subscribed services, and billing details.

---

## 2. Dataset and Preprocessing

### Dataset Source

IBM Telco Customer Churn Dataset

Source:
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

### Dataset Size

* 7,043 rows
* 21 columns

### Target Variable

Churn

* Yes = Customer left
* No = Customer stayed

### Features

Important features include:

* Gender
* SeniorCitizen
* Partner
* Dependents
* Tenure
* InternetService
* OnlineSecurity
* TechSupport
* Contract
* PaymentMethod
* MonthlyCharges
* TotalCharges

### Preprocessing Steps

Several preprocessing operations were performed:

1. Converted TotalCharges to numeric values.
2. Replaced missing values using median imputation.
3. Removed customerID because it does not contribute to prediction.
4. Encoded categorical variables using Label Encoding.
5. Standardized numerical features using StandardScaler.
6. Split the dataset into 80% training data and 20% testing data.

---

## 3. Algorithms

### Logistic Regression

Logistic Regression is a widely used classification algorithm that estimates the probability of a class outcome. It is simple, interpretable, and effective for binary classification problems.

### Decision Tree Classifier

Decision Trees create a tree-like structure of decisions and conditions. They can capture nonlinear relationships and are easy to interpret.

### Random Forest Classifier

Random Forest combines multiple decision trees to improve prediction accuracy and reduce overfitting. It is one of the most popular ensemble learning methods.

---

## 4. Results and Discussion

### Model Comparison

| Model               | Accuracy | Precision | Recall | F1 Score |
| ------------------- | -------- | --------- | ------ | -------- |
| Logistic Regression | 0.7991   | 0.6426    | 0.5481 | 0.5916   |
| Decision Tree       | 0.7303   | 0.4924    | 0.5187 | 0.5052   |
| Random Forest       | 0.7899   | 0.6345    | 0.4920 | 0.5542   |

### Best Model

Logistic Regression achieved the highest F1 Score of 0.5916 and was selected as the final model.

The F1 Score was chosen as the primary metric because it balances Precision and Recall, which is important when identifying customers likely to churn.

### Sanity Checks

Three sample predictions were tested:

* Sample 1 → No Churn
* Sample 2 → Churn
* Sample 3 → No Churn

A confusion matrix was also generated to visualize model performance.

---

## 5. Deployment Notes

The selected Logistic Regression model was deployed using FastAPI.

### API Endpoint

POST /predict

The endpoint accepts customer information in JSON format and returns a churn prediction.

### Example Response

{
"prediction": 0,
"churn": "No"
}

The API was tested successfully using FastAPI Swagger documentation and local requests.

---

## 6. Lessons Learned

This project provided practical experience in building a complete machine learning pipeline from data preprocessing to deployment.

Key lessons learned include:

* The importance of data preprocessing before model training.
* How to compare multiple machine learning algorithms fairly.
* Why F1 Score can be more useful than Accuracy for classification tasks.
* How to save and load trained models using Joblib.
* How to deploy machine learning models using FastAPI.
* How to document and organize a professional machine learning project.

### Future Improvements

Future work could include:

* Hyperparameter tuning
* Feature engineering
* Cross-validation
* XGBoost implementation
* Cloud deployment

## Conclusion

This project successfully developed and deployed a machine learning solution for telecom customer churn prediction. Three algorithms were trained and evaluated, with Logistic Regression producing the best overall performance. The final model was deployed through a FastAPI endpoint capable of generating customer churn predictions from JSON input.


## Repository
https://github.com/Hibo-moha/telecom-customer-churn-prediction-using-machine-learning