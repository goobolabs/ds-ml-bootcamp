# Final Project Proposal

## 1. Certificate Name

**Bille Cabdul Cali**

---

## 2. Project Title and Description

### Project Title

**Used Car Price Prediction Using Machine Learning**

### Description

The price of a used car depends on many factors, including the car brand, model year, mileage, engine specifications, fuel type, and transmission. Buyers and sellers often find it difficult to estimate a fair market price for a used vehicle. This project aims to develop a machine learning system that predicts the price of a used car based on its features. The system can help customers, car dealers, and sellers make better pricing decisions using data-driven predictions.

---

## 3. Problem Type

**Regression**

This project is a regression problem because the goal is to predict a numerical value, which is the price of a used car.

---

## 4. Dataset

**Dataset Name:**
Used Car Price Prediction Dataset (Cleaned & Feature Engineered)

**Source:**
Kaggle
https://www.kaggle.com/datasets/taeefnajib/used-car-price-prediction-dataset

**Dataset Size:**
The dataset contains **3,918 rows and 13 columns**, which satisfies the requirement of having more than 1,000 rows.

**Target Column:**

* **price** — represents the selling price of the used vehicle.

**Main Features:**

* **brand** — manufacturer of the vehicle (e.g., Toyota, BMW).
* **model** — specific vehicle model.
* **model_year** — year the vehicle was manufactured.
* **milage** — total distance traveled by the vehicle.
* **fuel_type** — type of fuel used by the vehicle.
* **transmission** — transmission system type.
* **accident** — indicates whether the vehicle has accident history.
* **clean_title** — indicates whether the vehicle has a clean title.
* **horsepower** — engine power output.
* **engine_capacity** — engine size in liters.
* **layout** — engine configuration such as I4, V6, or V8.

---

## 5. Algorithms You Plan to Train

### 1. Linear Regression

Linear Regression will be used as a baseline model because it is simple, interpretable, and useful for understanding relationships between car features and price.

### 2. Decision Tree Regressor

Decision Tree Regressor is suitable because it can capture non-linear relationships between vehicle characteristics and price.

### 3. Random Forest Regressor

Random Forest Regressor combines multiple decision trees to improve prediction accuracy and reduce overfitting compared to a single tree.

---

## 6. Evaluation Plan

The regression models will be evaluated using:

* **Mean Absolute Error (MAE)**
* **Root Mean Squared Error (RMSE)**
* **R² Score**

The main metric used to select the best model will be **MAE (Mean Absolute Error)** because it shows the average prediction error in the same unit as the car price, making the results easier to understand.

---

## 7. Deployment Sketch

The project will be deployed using **FastAPI**.

The `/predict` endpoint will accept JSON input containing vehicle information:

```json
{
  "brand": "Toyota",
  "model": "Camry",
  "model_year": 2020,
  "milage": 45000,
  "fuel_type": "Gasoline",
  "transmission": "Automatic",
  "horsepower": 203,
  "engine_capacity": 2.5,
  "layout": "I4"
}
```

The API will return the predicted car price:

```json
{
  "predicted_price": 18500
}
```

---

## 8. Repository Plan

The project will be developed using **Visual Studio Code (VS Code)** and managed using Git and GitHub.

Repository structure:

```text
used-car-price-prediction/
│
├── dataset/
│   └── used_car_cleaned.csv
│
├── notebooks/
│   └── eda.ipynb
│
├── src/
│   ├── preprocess.py
│   ├── feature_engineering.py
│   ├── train.py
│   └── evaluate.py
│
├── api/
│   └── app.py
│
├── models/
│   └── best_model.pkl
│
├── README.md
├── project-proposal.md
├── project_paper.md
└── requirements.txt
```
