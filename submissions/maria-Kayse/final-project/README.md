# Hotel Booking Cancellation Prediction Using Machine Learning

## Project Overview

This project uses machine learning techniques to predict whether a hotel booking will be canceled or not.

The system analyzes customer details, booking information, and reservation characteristics to help hotels reduce cancellation risks and improve decision-making.

## Dataset

**Hotel Booking Demand Dataset (Kaggle)**

- 119,390 records
- 32 features
- Target: `is_canceled`

## Machine Learning Approach

### Classification Models:
- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier

### Clustering Models:
- K-Means Clustering
- Agglomerative Clustering

## Workflow

- Data Cleaning
- Exploratory Data Analysis
- Feature Selection
- Model Training
- Model Evaluation
- Model Comparison

## Evaluation

Models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC

The best model is selected based on F1-score.

## Deployment

The final model can be deployed using FastAPI to provide booking cancellation predictions through an API.

## Technologies

- Python
- Pandas
- Scikit-learn
- XGBoost
- FastAPI

## Author

**Maryan Ahmed Warsame**