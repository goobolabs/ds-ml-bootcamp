# Project Proposal

## Student Information

**Student Name:** Jelle Hassan Ali

**Certificate Name:**
Data Science and Machine Learning Bootcamp

---

# Project Title

Flight Ticket Price Prediction API using Machine Learning

---

# Problem Statement

Airline ticket prices change frequently depending on several factors such as airline company, travel date, departure time, arrival time, source city, destination city, number of stops, and flight duration.

For travelers, it is difficult to know whether a ticket price is reasonable or whether they should wait before booking.

The goal of this project is to build a Machine Learning model that predicts the expected price of a flight ticket based on travel information. The final model will be deployed as a REST API using FastAPI so that users can send flight details and receive an estimated ticket price.

---

# Machine Learning Task

Regression

The target variable is:

**Price**

The model predicts a continuous numeric value instead of a category.

---

# Dataset

Dataset Name:

Flight Price Prediction Dataset

Source:

Kaggle

Expected Size:

More than 10,000 flight records

Main Features include:

- Airline
- Source
- Destination
- Date of Journey
- Departure Time
- Arrival Time
- Duration
- Total Stops
- Additional Information
- Price (Target)

---

# Planned Data Preprocessing

The dataset will be cleaned and prepared using several preprocessing techniques learned during the bootcamp.

These include:

- Handling missing values
- Removing duplicate records
- Converting date and time columns into useful numerical features
- Encoding categorical variables
- Feature engineering
- Detecting and handling outliers where appropriate
- Scaling numerical features if required

---

# Planned Machine Learning Models

The project will compare three regression algorithms.

### 1. Linear Regression

Used as a baseline regression model.

### 2. Random Forest Regressor

Used because it can model complex nonlinear relationships and generally performs well on structured datasets.

### 3. Ridge Regression

Chosen because it improves Linear Regression by reducing overfitting using L2 Regularization.

The performance of all three models will be compared before selecting the best one.

---

# Model Evaluation

The following regression metrics will be used:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

The best-performing model will be selected for deployment.

---

# Deployment Plan

After training and evaluating the models, the best model will be saved using Joblib.

A REST API will then be developed using FastAPI.

The API will include:

- Home endpoint
- Prediction endpoint
- Automatic Swagger documentation

Users will be able to send flight information as JSON and receive a predicted ticket price.

---

# Expected Outcome

The final system will allow users to estimate airline ticket prices before booking flights.

The project will demonstrate the complete Machine Learning workflow including:

- Data preprocessing
- Feature engineering
- Model training
- Model evaluation
- Model comparison
- API deployment using FastAPI

---

# Tools and Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- FastAPI
- Uvicorn
- Jupyter Notebook
- Git
- GitHub

---

# Deliverables

- Complete Machine Learning pipeline
- Trained regression models
- Model comparison report
- FastAPI prediction service
- GitHub repository
- Project paper