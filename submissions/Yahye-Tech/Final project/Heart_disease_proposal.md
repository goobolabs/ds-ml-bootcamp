Project Proposal — Heart Disease Prediction API

«This proposal presents the plan for my final machine learning project.»

Date: 12 July 2026

---

1. Certificate Name

Yahye Ahmed Mohamud

---

2. Project Title and Description

Title: Heart Disease Prediction API

Heart disease remains one of the leading causes of death worldwide. Early prediction of heart disease can help healthcare professionals make informed decisions and provide timely treatment to patients. With the increasing availability of medical data, machine learning has become an effective tool for identifying patterns that may not be obvious through manual analysis.

The purpose of this project is to build a machine learning model that predicts whether a patient is likely to have heart disease based on medical information such as age, blood pressure, cholesterol level, glucose level, smoking status, diabetes, and other health indicators. The completed model will be deployed as a REST API using FastAPI. Users will submit patient information in JSON format, and the API will return a prediction together with a probability score that indicates the confidence of the prediction.

---

3. Problem Type

Classification — Binary Classification

This is a supervised machine learning classification problem because the model will be trained using historical patient records where the diagnosis is already known.

The target column is TenYearCHD, where:

- 1 = Patient is likely to develop coronary heart disease.
- 0 = Patient is unlikely to develop coronary heart disease.

The goal is to classify new patient records accurately using the trained model.

---

4. Dataset

- Source: Kaggle – Framingham Heart Study Dataset
- Size: Approximately 4,240 patient records with 15 medical features and 1 target column.
- Target: "TenYearCHD"

Main Features

- "male" – Gender
- "age" – Age of the patient
- "currentSmoker" – Smoking status
- "cigsPerDay" – Average cigarettes smoked per day
- "BPMeds" – Blood pressure medication
- "prevalentStroke" – Previous stroke history
- "prevalentHyp" – Hypertension status
- "diabetes" – Diabetes status
- "totChol" – Total cholesterol
- "sysBP" – Systolic blood pressure
- "diaBP" – Diastolic blood pressure
- "BMI" – Body Mass Index
- "heartRate" – Resting heart rate
- "glucose" – Blood glucose level

Preprocessing Plan

Before training the machine learning models, the dataset will be prepared by:

- Removing duplicate records.
- Handling missing values using suitable imputation techniques.
- Encoding categorical variables where necessary.
- Scaling numerical features using StandardScaler.
- Splitting the dataset into 80% training and 20% testing sets.
- Verifying the cleaned dataset before model training.

---

5. Algorithms I Plan to Train

#| Algorithm| Why it fits
1| Logistic Regression| Serves as a simple and interpretable baseline model for binary classification.
2| Random Forest| Handles complex feature relationships and reduces overfitting through ensemble learning.
3| Gradient Boosting (Scikit-learn)| Often achieves high prediction accuracy on structured healthcare datasets and is suitable for classification tasks.

These three algorithms satisfy the minimum project requirement. Their performance will be compared, and the best-performing model will be selected for deployment.

---

6. Evaluation Plan

All models will be evaluated using the same testing dataset.

The following evaluation metrics will be used:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

Best Model Selection

The final model will be selected based on the highest F1-Score, as it provides a good balance between Precision and Recall. If two models achieve similar F1-Scores, the model with the higher Recall will be chosen because identifying patients who are at risk of heart disease is especially important.

A comparison table containing the performance of all trained algorithms will be included in the final report.

---

7. Deployment Sketch

- Framework: FastAPI
- Endpoint: "POST /predict"

Input JSON Example

{
  "male": 1,
    "age": 52,
      "currentSmoker": 1,
        "cigsPerDay": 10,
          "BPMeds": 0,
            "prevalentStroke": 0,
              "prevalentHyp": 1,
                "diabetes": 0,
                  "totChol": 240,
                    "sysBP": 140,
                      "diaBP": 90,
                        "BMI": 27.8,
                          "heartRate": 78,
                            "glucose": 92
                            }

                            Output JSON Example

                            {
                              "prediction": "High Risk",
                                "probability": 0.89
                                }

                                The API will load the best trained model from "models/best_model.pkl" together with the preprocessing files. After receiving patient information, the API will process the data and return a prediction in real time.

                                ---

                                8. Repository Plan

                                heart-disease-api/
                                ├── dataset/
                                │   └── framingham.csv
                                ├── src/
                                │   ├── preprocess.py
                                │   └── train.py
                                ├── api/
                                │   └── app.py
                                ├── models/
                                │   ├── best_model.pkl
                                │   └── scaler.pkl
                                ├── notebooks/
                                │   └── exploration.ipynb
                                ├── README.md
                                ├── requirements.txt
                                └── project_paper.md

                                Planned Commands

                                python src/train.py
                                uvicorn api.app:app --reload

                                The first command trains all machine learning models, compares their performance, and saves the best-performing model. The second command starts the FastAPI application locally, allowing users to test the prediction API through a web browser or API testing tools.