# Final Project Proposal

## 1. Certificate Name

**Miski Mohamed Nur**

---

## 2. Project Title and Description

### Project Title

**Diabetes Prediction System Using Machine Learning**

### Project Description

Diabetes is one of the most common chronic diseases in the world. Early prediction can help patients receive medical attention before serious complications develop. The goal of this project is to build a machine learning model that predicts whether a person is likely to have diabetes based on medical and demographic information. This system can support healthcare professionals by providing a quick prediction tool, and it can also increase public awareness of diabetes risk.

---

## 3. Problem Type

**Classification**

This project is a binary classification problem because the target variable has two possible outcomes:

* **0 = No Diabetes**
* **1 = Diabetes**

The machine learning model will classify each patient into one of these two categories.

---

## 4. Dataset

### Source

Kaggle Diabetes Prediction Dataset

https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset

### Expected Size

Approximately **100,000 rows** and **9 columns**, which satisfies the bootcamp requirement of at least 1,000 records.

### Target Column

**diabetes**

Represents whether the patient has diabetes.

* **0 = No Diabetes**
* **1 = Diabetes**

### Main Features

| Feature             | Description                                        |
| ------------------- | -------------------------------------------------- |
| gender              | Patient's gender                                   |
| age                 | Age in years                                       |
| hypertension        | Whether the patient has hypertension               |
| heart_disease       | Whether the patient has heart disease              |
| smoking_history     | Smoking status                                     |
| bmi                 | Body Mass Index                                    |
| HbA1c_level         | Average blood sugar level over the past 2–3 months |
| blood_glucose_level | Current blood glucose measurement                  |

These features will be used to predict the diabetes status.

---

## 5. Algorithms I Plan to Train

### 1. Logistic Regression

Logistic Regression is a simple and effective baseline algorithm for binary classification problems such as diabetes prediction.

### 2. Decision Tree Classifier

Decision Tree can capture non-linear relationships between medical features and the target while remaining easy to interpret.

### 3. Random Forest Classifier

Random Forest combines multiple decision trees to improve prediction accuracy and reduce overfitting.

After training all three models, I will compare their performance and choose the best one for deployment.

---

## 6. Evaluation Plan

Since this is a classification problem, I will evaluate the models using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

### Best Model Selection

I will use **F1-Score** as the primary evaluation metric because it balances Precision and Recall, making it suitable for medical prediction tasks where both false positives and false negatives are important.

---

## 7. Deployment Sketch

I will deploy the final model using **Flask**.

### `/predict` Endpoint Input (JSON)

```json
{
  "gender": "Female",
  "age": 45,
  "hypertension": 0,
  "heart_disease": 0,
  "smoking_history": "never",
  "bmi": 27.5,
  "HbA1c_level": 5.8,
  "blood_glucose_level": 140
}
```

### API Response

```json
{
  "prediction": "Diabetes",
  "prediction_value": 1,
  "probability": 0.91
}
```

The API will accept patient information and return the predicted diabetes status together with the prediction probability.

---

## 8. Repository Plan

```
diabetes-prediction-system/
│
├── dataset/
│   └── diabetes_prediction_dataset.csv
│
├── notebooks/
│   └── diabetes_prediction.ipynb
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
├── models/
│   └── diabetes_model.pkl
│
├── api/
│   └── app.py
│
├── requirements.txt
├── README.md
└── project_paper.md
```

This structure separates the dataset, preprocessing scripts, training code, evaluation scripts, deployment API, trained models, and documentation. It will make the project easier to develop, maintain, and deploy.
