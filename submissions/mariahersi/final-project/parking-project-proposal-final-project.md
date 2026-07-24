# Project Proposal — Parking Occupancy Prediction Web Application

**Date:** July 2026

---
replinl:https://github.com/mariahersi/ds-ml-bootcamp
## 1. Certificate Name

**Maryamo Hersi Hassan**

---

## 2. Project Title and Description

### Project Title

**Parking Occupancy Prediction Web Application Using Machine Learning**

### Project Description

Finding available parking spaces is a common challenge in busy urban areas. Drivers may spend a long time searching for parking, which can increase traffic congestion, fuel consumption, and travel delays. Parking managers also need reliable information to understand demand and use available parking capacity efficiently.

This project develops a machine learning-based web application that predicts parking occupancy levels using historical parking data. The system will analyze information such as parking capacity, occupancy, location code, working day, month, day, hour, and time period. Users will enter parking and time-related information through a React frontend, and the Flask backend will process the input and return a predicted parking occupancy level.

The completed system will provide a simple and user-friendly interface that can help parking operators and users estimate whether a parking facility is likely to have low, medium, or high occupancy.

---

## 3. Problem Type

**Supervised Machine Learning — Ordinal Prediction / Regression**

The target variable is `per_occupancy`, which represents parking occupancy ranges:

- `0 - 25`
- `25 - 50`
- `50 - 75`
- `75 - 100`

The target categories will be converted into numerical values during preprocessing. The trained model will predict the expected occupancy range based on the supplied parking information.

---

## 4. Business Problem

Parking facilities often experience changing demand depending on location, capacity, day, working-day status, and time. Without a prediction system, drivers may arrive at a full parking facility, while parking operators may struggle to plan capacity and improve resource utilization.

The proposed system addresses this problem by using historical parking data to predict occupancy levels. The prediction can support better parking decisions, reduce unnecessary driving, improve customer satisfaction, and help parking managers identify busy periods.

---

## 5. Project Objectives

The main objective is to develop a machine learning web application for predicting parking occupancy levels.

The specific objectives are:

1. To clean and preprocess the parking occupancy dataset.
2. To analyze the major factors that influence parking occupancy.
3. To train and compare multiple machine learning algorithms.
4. To select and save the best-performing model.
5. To develop a Flask REST API for serving predictions.
6. To design a responsive React frontend for user input and prediction results.
7. To integrate the React frontend with the Flask backend.

---

## 6. Research Questions

1. Which factors have the strongest influence on parking occupancy?
2. Can machine learning accurately predict parking occupancy levels?
3. Which machine learning algorithm produces the lowest prediction error?
4. How can a React and Flask web application make parking predictions easier to access?
5. How can parking occupancy predictions support better parking management?

---

## 7. Dataset

### Dataset Name

**Parking Occupancy Dataset**

### Dataset Size

- **Rows:** 35,332
- **Original columns:** 11

### Target Variable

- `per_occupancy` — parking occupancy percentage range.

### Main Features

| Feature | Description |
|---|---|
| `SystemCodeNumber` | Unique parking facility or system code |
| `Capacity` | Total number of available parking spaces |
| `Occupancy` | Number of occupied parking spaces |
| `per_usage` | Percentage of parking capacity currently used |
| `year` | Year of the observation |
| `month` | Month of the observation |
| `day` | Day of the week |
| `WorkingDay` | Indicates whether the date is a working day |
| `hour` | Hour of the observation |
| `period` | AM or PM period |
| `per_occupancy` | Target occupancy range |

### Data Preprocessing Plan

The following preprocessing steps will be applied:

1. Inspect the dataset using `head()`, `info()`, descriptive statistics, and missing-value counts.
2. Remove duplicate rows.
3. Handle missing numerical values using the median.
4. Handle missing categorical values using the mode.
5. Detect and cap numerical outliers using the IQR method.
6. Convert categorical variables into numerical values using encoding.
7. Create useful time-related features where appropriate.
8. Split the dataset into 80% training data and 20% testing data.
9. Scale numerical features using `StandardScaler`.
10. Save the fitted encoder and scaler for deployment.

---

## 8. Machine Learning Algorithms

Five machine learning algorithms will be trained and compared.

| # | Algorithm | Reason for Selection |
|---|---|---|
| 1 | Linear Regression | Provides a simple and interpretable baseline model |
| 2 | Decision Tree Regressor | Captures non-linear relationships and is easy to interpret |
| 3 | Random Forest Regressor | Combines several trees and usually improves stability and accuracy |
| 4 | Gradient Boosting Regressor | Learns from previous prediction errors and performs well on tabular data |
| 5 | Support Vector Regression | Can model complex non-linear relationships after feature scaling |

Hyperparameter tuning will be performed using `GridSearchCV` with cross-validation where appropriate.

---

## 9. Model Evaluation Plan

All models will be evaluated using the same held-out testing dataset.

### Evaluation Metrics

- **Mean Absolute Error:** Measures the average absolute difference between actual and predicted values.
- **Mean Squared Error:** Gives a larger penalty to large prediction errors.
- **Root Mean Squared Error:** Expresses the prediction error in the target variable’s scale.
- **R² Score:** Measures how much variation in the target variable is explained by the model.

### Best Model Selection Rule

The best model will be selected primarily based on:

1. Lowest RMSE
2. Lowest MAE
3. Highest R² score
4. Stable cross-validation performance

The selected model and preprocessing objects will be saved using `joblib` or `pickle`.

---

## 10. Proposed System Architecture

The application will contain three main components:

### React Frontend

The frontend will be developed using React. It will provide:

- A clean parking prediction form
- Input fields for parking location, capacity, time, day, and related features
- Input validation
- Loading and error messages
- A prediction result card
- Responsive design for desktop and mobile devices

### Flask Backend

The backend will be developed using Flask. It will:

- Load the trained machine learning model
- Load saved encoders and scaler
- Receive prediction requests from React
- Validate and preprocess input data
- Generate a parking occupancy prediction
- Return the result as JSON
- Enable frontend communication using Flask-CORS

### Machine Learning Model

The model will be trained in a Jupyter Notebook using Python and scikit-learn. The final selected model will be exported and loaded by the Flask application.

### System Data Flow

```text
User
  ↓
React Prediction Form
  ↓
HTTP POST Request
  ↓
Flask REST API
  ↓
Saved Preprocessor and Machine Learning Model
  ↓
Prediction Result
  ↓
React Result Display
```

---

## 11. API Deployment Sketch

### Framework

**Flask**

### Endpoint

```http
POST /api/predict
```

### Example Input

```json
{
  "SystemCodeNumber": "BHMBCCMKT01",
  "Capacity": 577,
  "Occupancy": 150,
  "per_usage": 26.0,
  "year": 2016,
  "month": "October",
  "day": "Tuesday",
  "WorkingDay": "Yes",
  "hour": 9,
  "period": "AM"
}
```

### Example Output

```json
{
  "prediction_code": 1,
  "occupancy_level": "25 - 50",
  "message": "The predicted parking occupancy level is between 25% and 50%."
}
```

---

## 12. Frontend Pages and Components

The React frontend will include:

1. **Home Page** — introduces the parking prediction system.
2. **Prediction Page** — contains the input form.
3. **Result Section** — displays the predicted occupancy range.
4. **About Page** — explains the project, dataset, and machine learning model.
5. **Navbar and Footer** — provide navigation and project information.

Suggested React components:

```text
components/
├── Navbar.jsx
├── PredictionForm.jsx
├── PredictionResult.jsx
├── LoadingSpinner.jsx
└── Footer.jsx
```

---

## 13. Repository Plan

```text
parking-occupancy-prediction/
├── dataset/
│   └── ParkingDataset.xlsx
├── notebook/
│   └── Parking.ipynb
├── backend/
│   ├── app.py
│   ├── model/
│   │   ├── best_model.pkl
│   │   ├── scaler.pkl
│   │   └── encoders.pkl
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
├── README.md
└── project-proposal.md
```

---

## 14. Technologies and Tools

### Machine Learning and Data Analysis

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook
- Joblib or Pickle

### Backend

- Flask
- Flask-CORS
- REST API
- Python

### Frontend

- React
- Vite
- JavaScript
- HTML
- CSS or Tailwind CSS
- Axios or Fetch API

### Development Tools

- Visual Studio Code
- Git
- GitHub
- Google Colab or Jupyter Notebook

---

## 15. Expected Outcomes

At the end of the project, the following deliverables are expected:

1. A cleaned parking occupancy dataset.
2. A completed exploratory data analysis notebook.
3. Five trained and evaluated machine learning models.
4. A comparison table showing model performance.
5. A saved best-performing model.
6. A Flask REST API for parking predictions.
7. A responsive React web interface.
8. A fully integrated parking occupancy prediction application.
9. A GitHub repository containing the project source code and documentation.

---

## 16. Project Limitations

The model’s predictions will depend on the quality and scope of the historical dataset. The dataset may not include external factors such as weather, public events, road closures, or real-time traffic conditions. The application will therefore provide an estimated occupancy level rather than a guaranteed real-time parking availability result.

Another limitation is that features such as `Occupancy` and `per_usage` may be closely related to the target variable. During final model validation, feature leakage will be checked carefully. A second model may be trained without directly related occupancy fields to measure how well the system predicts future demand using only location and time information.

---

## 17. Future Improvements

Future versions of the system may include:

- Real-time parking sensor data
- Weather and traffic information
- Map-based parking location selection
- User authentication
- Parking history dashboards
- Live space availability
- Cloud deployment
- Mobile application support
- Automatic model retraining

---

## 18. Conclusion

This project proposes a machine learning-based parking occupancy prediction web application. Historical parking information will be cleaned, analyzed, and used to train five machine learning models. The best model will be deployed through a Flask REST API and connected to a React frontend.

The proposed application can help users and parking operators estimate occupancy levels, understand busy periods, and make better parking decisions. It also demonstrates the complete machine learning workflow, including data preprocessing, model training, evaluation, API development, frontend design, and system integration.
