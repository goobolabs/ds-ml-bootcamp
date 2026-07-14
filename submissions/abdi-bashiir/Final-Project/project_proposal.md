# Final Project Proposal

## 1. Certificate Name

**Abdi Bashir Ali**

---

## 2. Project Title and Description

### Project Title
**Appliances Energy Consumption Prediction API** 

### Description
Energy consumption in modern homes is continuously increasing, leading to higher electricity costs and greater environmental impact. This project aims to develop a machine learning regression model that predicts the energy consumption of household appliances based on indoor sensor measurements and weather-related data. The final solution will be deployed as a FastAPI application that accepts sensor values as input and returns the predicted appliance energy consumption. This system can help homeowners and energy management systems monitor and optimize electricity usage.

---

## 3. Problem Type

**Regression**

This project is a regression problem because it predicts a continuous numerical value: the energy consumption of household appliances measured in Watt-hours (Wh).

---

## 4. Dataset

- **Dataset Name:** Appliances Energy Prediction
- **Source:** UCI Machine Learning Repository
- **Dataset Link:** [https://archive.ics.uci.edu/dataset/380/appliances+energy+prediction](https://www.kaggle.com/datasets/sohommajumder21/appliances-energy-prediction-data-set)
- **Expected Size:** 19,735 rows
- **Target Column:** `Appliances` (Energy consumption in Watt-hours)
**Main Features:**
- Indoor temperature sensors (`T1`–`T9`)
- Indoor humidity sensors (`RH_1`–`RH_9`)
- Outdoor temperature (`T_out`)
- Outdoor humidity (`RH_out`)
- Atmospheric pressure (`Press_mm_hg`)
- Wind speed (`Windspeed`)
- Visibility (`Visibility`)

These features provide environmental and weather information that influences household energy consumption.

---

## 5. Algorithms I Plan to Train

| Algorithm | Reason for Selection |
|------------|---------------------|
| **Linear Regression** | It serves as a simple and interpretable baseline model for predicting continuous values. |
| **Random Forest Regressor** | It captures complex nonlinear relationships and usually provides strong predictive performance on tabular datasets. |
| **Gradient Boosting Regressor** | It is an advanced ensemble algorithm that often achieves high prediction accuracy by combining multiple weak learners. |

These three algorithms will be trained and compared to identify the best-performing regression model.

---

## 6. Evaluation Plan

The following evaluation metrics will be used to compare all regression models:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

**Best Model Selection**

The best model will be selected primarily based on the **highest R² Score**, while also considering the **lowest RMSE**. These metrics provide a reliable measure of prediction accuracy and overall model performance for regression tasks.

---

## 7. Deployment Sketch

- **Framework:** FastAPI
- **Endpoint:** `POST /predict`

### Input (JSON)

```json
{
  "T1": 21.5,
  "RH_1": 45.0,
  "T_out": 12.8,
  "RH_out": 78.0,
  "Windspeed": 5.3,
  "Press_mm_hg": 755.0
}
```

### Output (JSON)

```json
{
  "predicted_energy_wh": 98.74
}
```

The API will receive sensor measurements and weather information, then return the predicted household appliance energy consumption in Watt-hours.

---

## 8. Repository Plan

```text
energy-prediction-api/
├── dataset/
│   └── energy_data.csv
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── evaluate.py
├── api/
│   └── app.py
├── models/
│   └── best_model.pkl
├── notebooks/
│   └── experimentation.ipynb
├── README.md
├── requirements.txt
└── project_paper.md
```

This repository structure separates data, source code, trained models, API implementation, documentation, and experimentation notebooks, making the project organized, maintainable, and easy to deploy.
