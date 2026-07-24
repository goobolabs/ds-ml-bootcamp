# Used Car Price Prediction - Project Paper
GitHub Repository:
https://github.com/bille2026/used-car-price-prediction


# 1. Problem Statement and Motivation

The used car market contains many factors that influence vehicle prices, including brand, model year, mileage, engine specifications, and vehicle condition.

Estimating the correct price of a used car manually can be difficult because different features affect the value of a vehicle. This project aims to build a Machine Learning regression system that predicts used car prices based on available vehicle information.

The goal of this project is to create a complete Machine Learning workflow from data preprocessing to model deployment through an API.


# 2. Dataset and Preprocessing


## Dataset Description

The dataset used in this project is a Used Car Price Dataset collected from Kaggle.

Dataset information:

- Number of samples: 3918
- Number of original features: 13
- Problem type: Regression

The target variable is:

- Price


The main features include:

- Brand
- Model year
- Mileage
- Fuel type
- Transmission
- Accident history
- Clean title
- Horsepower
- Engine capacity
- Layout
- Model
- Engine


## Data Cleaning

Before training the models, several preprocessing steps were performed:

- Converted price values from text format into numerical values
- Removed unnecessary symbols from price data
- Converted mileage values into numerical format
- Checked missing values
- Checked duplicate rows


## Feature Engineering

New features were created to improve model performance:

### Car_Age

This feature represents how old the vehicle is.

Formula:

Car_Age = Current Year - Model Year


### Mileage_per_Year

This feature represents the average mileage driven per year.

Formula:

Mileage_per_Year = Mileage / Car_Age


## Encoding and Scaling

Categorical features cannot be directly used by Machine Learning algorithms.

Therefore:

- One-Hot Encoding was applied to categorical variables.
- Numerical features were scaled using StandardScaler.

All preprocessing steps were included inside the Machine Learning pipeline to ensure the same transformations are applied during prediction.


# 3. Machine Learning Algorithms


Three different regression algorithms were trained and compared.


## Linear Regression

Linear Regression was used as a baseline model.

It attempts to find a linear relationship between input features and the target price.


Advantages:

- Simple and fast
- Easy to interpret


Limitations:

- Cannot capture complex relationships between features


## Decision Tree Regressor

Decision Tree creates rules by splitting the data into different groups.

Advantages:

- Handles non-linear relationships
- Easy to understand


Limitations:

- Can overfit training data


## Random Forest Regressor

Random Forest combines multiple decision trees and uses their average prediction.

Advantages:

- Reduces overfitting
- Handles complex patterns
- Usually provides better generalization


This model was selected as the final deployment model.


# 4. Results and Discussion


The models were evaluated using three regression metrics:

- MAE
- RMSE
- R² Score


## Model Comparison


| Model | MAE | RMSE | R² Score |
|---|---|---|---|
| Linear Regression | 21774.61 | 125052.77 | 0.1184 |
| Decision Tree | 18395.86 | 127045.46 | 0.0901 |
| Random Forest | 16049.05 | 121640.53 | 0.1659 |


## Best Model

Random Forest Regressor achieved the best performance.

The selection rule was based on:

- Lowest MAE
- Lowest RMSE
- Highest R² Score


Therefore, Random Forest was saved and deployed as the final prediction model.


## Sanity Checks

The final model was tested using new sample vehicle inputs.


Example results:


Toyota Camry 2021

Predicted Price:

$31398.47


BMW M340i 2020

Predicted Price:

$54830.52


Ford Mustang 2018

Predicted Price:

$47533.98


These tests confirmed that the deployed model can receive new vehicle information and return price predictions.


# 5. Deployment Notes


The final model was deployed using FastAPI.

The saved pipeline contains:

- Feature engineering
- Encoding
- Scaling
- Random Forest model


Model file:

models/car_price_pipeline.pkl


API Endpoint:

POST /predict


The API accepts vehicle information in JSON format and returns the predicted price.


Example response:


{
    "predicted_price": 31398.47
}


The API was tested successfully using FastAPI Swagger documentation:

http://127.0.0.1:8000/docs


# 6. Lessons Learned


During this project, several important Machine Learning concepts were applied.

The main challenges included:

- Cleaning real-world vehicle data
- Handling categorical variables
- Selecting the best model
- Preparing the model for deployment


The project improved understanding of the complete Machine Learning lifecycle, including data preparation, model training, evaluation, and API deployment.


Future improvements could include:

- Collecting more vehicle data
- Testing advanced algorithms such as Gradient Boosting or XGBoost
- Improving feature selection
- Deploying the API online


# Conclusion

This project successfully developed a complete Machine Learning system for used car price prediction.

Three regression algorithms were trained and compared. Random Forest Regressor achieved the best results and was deployed as a FastAPI service capable of making real-time price predictions.






## Author

**Bille Abdul Ali**

Computer Science Student

Machine Learning Project - Used Car Price Prediction
```