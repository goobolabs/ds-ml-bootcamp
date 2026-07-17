# Hotel Reservation Cancellation Prediction Using Machine Learning

**FINAL PROJECT PROPOSAL**

**CERTIFICATE NAME:** Mohamed Abdalle Aden

*A Supervised Machine Learning Classification Project*

Dataset Source: Kaggle — Hotel Reservations Classification Dataset
Deployment: FastAPI | Primary Metric: F1 Score

---

## 1. Certificate Name

**Mohamed Abdalle Aden**

## 2. Project Title and Description

**Project Title:**
Hotel Reservation Cancellation Prediction Using Machine Learning

**Project Description:**

Hotel booking cancellations are a major challenge for the hospitality industry, leading to lost revenue, inefficient room inventory management, and difficulty in forecasting occupancy. Being able to predict in advance whether a reservation is likely to be canceled allows hotels to apply better overbooking strategies, adjust pricing, and improve customer relationship management. The goal of this project is to build a machine learning model that predicts whether a hotel booking will be canceled or not, based on booking details such as lead time, number of guests, room type, meal plan, market segment, special requests, and booking history.

This project is motivated by the practical value it offers to the hospitality industry — helping hotels reduce revenue loss from last-minute cancellations and plan resources more effectively.

## 3. Problem Type

**Classification**

This project is a supervised machine learning classification problem. The model will predict one of two classes:

- 0 = Not Canceled
- 1 = Canceled

## 4. Dataset

**Source:**
Kaggle — Hotel Reservations Classification Dataset
https://www.kaggle.com/datasets/ahsan81/hotel-reservations-classification-dataset

**Dataset Size:**
36,275 rows and 19 columns.

**Target Column:**
- booking_status — Canceled = 1, Not_Canceled = 0

**Main Features:**

| Feature | Description |
| --- | --- |
| no_of_adults | Number of adults included in the booking |
| no_of_children | Number of children included in the booking |
| no_of_weekend_nights | Number of weekend nights (Sat/Sun) booked |
| no_of_week_nights | Number of weekday nights booked |
| type_of_meal_plan | Type of meal plan booked by the customer |
| required_car_parking_space | Whether the customer required a car parking space |
| room_type_reserved | Type of room reserved by the customer |
| lead_time | Number of days between booking date and arrival date |
| arrival_year / arrival_month / arrival_date | Date of arrival |
| market_segment_type | How the booking was made (Online, Offline, Corporate, etc.) |
| repeated_guest | Whether the customer is a repeat guest |
| no_of_previous_cancellations | Number of previous bookings canceled by the customer |
| no_of_previous_bookings_not_canceled | Number of previous bookings not canceled by the customer |
| avg_price_per_room | Average price per day of the reservation (in euros) |
| no_of_special_requests | Number of special requests made by the customer |

*These features will be used to predict whether a hotel reservation will be canceled.*

## 5. Algorithms I Plan to Train

**1. Logistic Regression**
Used as a baseline model because it is simple, fast, and performs well for binary classification problems.

**2. Decision Tree Classifier**
Can learn complex decision rules and is easy to interpret, useful for identifying which booking factors drive cancellations.

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

The F1 Score will be the primary metric for selecting the best model because it balances Precision and Recall, making it more reliable when the classes are not perfectly balanced (there are typically more "Not Canceled" bookings than "Canceled" ones).

## 7. Deployment Sketch

The best-performing model will be deployed using FastAPI.

**Input**

The `/predict` endpoint will accept JSON data such as:

```json
{
  "no_of_adults": 2,
  "no_of_children": 0,
  "no_of_weekend_nights": 1,
  "no_of_week_nights": 2,
  "type_of_meal_plan": "Meal Plan 1",
  "required_car_parking_space": 0,
  "room_type_reserved": "Room_Type 1",
  "lead_time": 85,
  "arrival_year": 2018,
  "arrival_month": 10,
  "market_segment_type": "Online",
  "repeated_guest": 0,
  "no_of_previous_cancellations": 0,
  "no_of_previous_bookings_not_canceled": 0,
  "avg_price_per_room": 105.5,
  "no_of_special_requests": 1
}
```

**Output**

The API will return a prediction and probability. Example:

```json
{
  "prediction": "Canceled",
  "probability": 0.87
}
```

## 8. Repository Plan

The project repository will be organized as follows:

```
hotel-reservation-cancellation-project/
|
|-- dataset/
|   |-- hotel_reservations.csv
|
|-- notebooks/
|   |-- hotel_cancellation_prediction.ipynb
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
|   |-- hotel_cancellation_model.pkl
|
|-- README.md
|
|-- project_paper.md
```

The repository will contain the dataset, preprocessing scripts, model training code, evaluation scripts, the trained model, the FastAPI application, project documentation, and the final project report. This structure will keep the project organized and easy to maintain.
