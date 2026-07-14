Project Proposal
## 1. Certificate Name

Abdikani Aweys Yusuf

## 2. Project Title and Description

Title: Flight Delay Passenger Satisfaction Prediction Using Machine Learning

Description:

This project aims to develop a machine learning model that predicts whether an airline passenger will be satisfied or dissatisfied based on factors such as flight delay, airline service, travel class, age, travel type, and onboard experience. The model can help airlines identify dissatisfied passengers in advance and improve customer service by taking proactive measures.

## 3. Problem Type

### Classification- binary output:

The model predicts one of two categories:

   a) Satisfied
   b) Dissatisfied (or Neutral/Dissatisfied)

### Source:
 Kaggle – Airline Passenger Satisfaction Dataset

https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction

### Expected Size:
About 129,880 rows (well above the required 1,000 rows)

### Target Column:

satisfaction – Indicates whether a passenger is satisfied or dissatisfied.

### Main Features:

Gender
Customer Type
Age
Type of Travel
Class
Departure Delay in Minutes
Arrival Delay in Minutes
Check-in Service
Cleanliness
Baggage Handling

## 5. Algorithms You Plan to Train

#### 1. Logistic Regression – 
A strong baseline classification algorithm.
#### 2. Decision Tree Classifier – 
Easy to interpret and captures nonlinear relationships.
#### 4. Random Forest Classifier – 
Improves prediction accuracy by combining multiple decision trees.

(Optional)

XGBoost
Support Vector Machine (SVM)

## 6. Evaluation Plan

Metrics:

Accuracy
Precision
Recall
F1-Score

Best Model Selection:
F1-Score

F1-Score is chosen because it balances precision and recall, making it suitable for predicting passenger satisfaction accurately.

## 7. Deployment Sketch

Framework:
FastAPI

/predict accepts JSON such as:

{
  "age": 35,
  "departure_delay": 30,
  "arrival_delay": 25,
  "class": "Business",
}

Returns

{
  "prediction": "Satisfied",
  "probability": 0.92
}

## 8. Repository Plan

flight-delay-passenger-satisfaction/
├── dataset/
├── notebooks/
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── evaluate.py
├── api/
│   └── app.py
├── models/
├── README.md
└── project_paper.md
