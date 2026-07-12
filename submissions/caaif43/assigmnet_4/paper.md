

# Introduction

Regression is one of the most important supervised learning techniques in Machine Learning. It is used to predict continuous numerical values by learning the relationship between input variables and a target variable. Regression helps businesses and organizations make predictions based on historical data. It is widely used in finance, healthcare, education, transportation, and many other fields.

---

# 1. Introduction to Regression

## What is Regression?

Regression is a supervised machine learning technique that predicts continuous numerical values. The algorithm learns patterns from historical data and estimates future values based on those patterns.

Examples of regression include predicting house prices, car prices, salaries, temperatures, and sales revenue.

### Difference Between Regression and Classification

Regression predicts numerical values, while classification predicts categories or labels.

| Regression | Classification |
|------------|---------------|
| Predicts continuous values | Predicts categories |
| Output is a number | Output is a class label |
| Example: Car price | Example: Spam or Not Spam |

### Real-Life Example of Regression

Predicting the selling price of a used car using features such as mileage, age, and number of accidents.

### Real-Life Example of Classification

Predicting whether an email is spam or not spam.

---

# 2. Types of Regression

## Linear Regression

### How It Works

Linear Regression models a straight-line relationship between one independent variable and one dependent variable.

### Real-World Use

Predicting employee salary based on years of experience.

### Advantages

- Easy to understand
- Fast to train
- Easy to interpret

### Limitations

- Assumes a linear relationship
- Sensitive to outliers
- Cannot model complex data

---

## Multiple Linear Regression

### How It Works

Multiple Linear Regression predicts a target variable using two or more independent variables.

### Real-World Use

Predicting house prices using house size, location, number of bedrooms, and age.

### Advantages

- Uses multiple features
- Often more accurate than simple linear regression
- Easy to explain

### Limitations

- Can suffer from multicollinearity
- Assumes linear relationships
- Sensitive to irrelevant variables

---

## Polynomial Regression

### How It Works

Polynomial Regression extends Linear Regression by adding polynomial terms, allowing it to model curved relationships.

### Real-World Use

Predicting fuel consumption or population growth where relationships are nonlinear.

### Advantages

- Models nonlinear patterns
- More flexible than Linear Regression

### Limitations

- Can easily overfit
- More difficult to interpret
- Choosing the polynomial degree can be challenging

---

# Comparison of Regression Types

| Type | Relationship | Example | Advantages | Limitations |
|------|--------------|----------|------------|-------------|
| Linear Regression | Linear | Salary Prediction | Simple and fast | Cannot model nonlinear data |
| Multiple Linear Regression | Linear with many variables | House Prices | Uses multiple features | Sensitive to correlated variables |
| Polynomial Regression | Curved | Population Growth | Models nonlinear relationships | Risk of overfitting |

---

# 3. Regression Metrics

## Mean Absolute Error (MAE)

MAE measures the average absolute difference between predicted and actual values. Lower MAE indicates better performance.

## Mean Squared Error (MSE)

MSE measures the average squared difference between predicted and actual values. Large errors receive a greater penalty.

## Root Mean Squared Error (RMSE)

RMSE is the square root of MSE. It is expressed in the same unit as the target variable, making it easier to interpret.

## R² (Coefficient of Determination)

R² measures how well the model explains the variation in the target variable. Values closer to 1 indicate better performance.

---

# Comparison of Regression Metrics

| Metric | Unit | Sensitive to Large Errors | Meaning |
|---------|------|--------------------------|---------|
| MAE | Same as target | Low | Average prediction error |
| MSE | Squared unit | Very High | Penalizes large errors |
| RMSE | Same as target | High | Typical prediction error |
| R² | No unit | No | Percentage of explained variance |

---

# 4. Underfitting and Overfitting

## Underfitting

Underfitting occurs when a model is too simple to learn the patterns in the training data. As a result, it performs poorly on both training and testing data.

## Overfitting

Overfitting occurs when a model learns both the true patterns and the noise in the training data. It performs well on training data but poorly on new data.

### Why Polynomial Regression Can Overfit

A polynomial model with a very high degree becomes too flexible and memorizes the training data instead of learning the true relationship.

### Methods to Prevent Overfitting

- Reduce model complexity.
- Use cross-validation.
- Apply regularization techniques such as Ridge or Lasso Regression.

---

# 5. Real-World Case Study

## House Price Prediction

Many real estate companies use Multiple Linear Regression to estimate house prices.

### Goal

Predict house prices accurately based on property features.

### Data Used

- House size
- Number of bedrooms
- Number of bathrooms
- Location
- Age of the house

### Regression Method

Multiple Linear Regression

### Results

The model successfully estimated house prices and helped buyers, sellers, and real estate companies make better financial decisions.

---