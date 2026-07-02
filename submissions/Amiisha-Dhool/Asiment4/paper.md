# Assignment Four 

# 1. Introduction to Regression

## What is Regression in Machine Learning?

Regression is a supervised machine learning technique used to predict continuous numerical values based on input data. It identifies the relationship between independent variables (features) and a dependent variable (target). Regression is commonly used to estimate values such as car prices, house prices, salaries, and sales.

## Difference Between Regression and Classification

Regression predicts continuous numerical values, while classification predicts categories or labels. For example, regression can estimate the selling price of a car, whereas classification can determine whether an email is spam or not spam.

## Real-Life Examples

**Regression Example:** Predicting the price of a used car based on mileage, age, and location.

**Classification Example:** Predicting whether a customer will buy a product (Yes or No).

---

# 2. Types of Regression

## Linear Regression

Linear Regression models the relationship between one independent variable and one dependent variable using a straight line.

**Use Case:** Predicting house prices based on house size.

**Advantages:**

* Simple and easy to understand.
* Fast to train.

**Limitations:**

* Assumes a linear relationship.
* Sensitive to outliers.

### Multiple Linear Regression

Multiple Linear Regression uses two or more independent variables to predict one dependent variable.

**Use Case:** Predicting car prices using mileage, year, number of doors, and location.

**Advantages:**

* Uses multiple features.
* Produces more accurate predictions.

**Limitations:**

* More complex than simple linear regression.
* Can be affected by multicollinearity.

### Polynomial Regression

Polynomial Regression models non-linear relationships by fitting a curved line instead of a straight line.

**Use Case:** Predicting crop production based on rainfall and temperature.

**Advantages:**

* Captures non-linear patterns.
* Can improve prediction accuracy.

**Limitations:**

* Easily overfits the data.
* Choosing the correct polynomial degree is difficult.

---

# 3. Regression Metrics

## Mean Absolute Error (MAE)

MAE measures the average absolute difference between predicted and actual values. Lower MAE indicates better model performance.

## Mean Squared Error (MSE)

MSE measures the average squared difference between predicted and actual values. Large errors receive a higher penalty.

## Root Mean Squared Error (RMSE)

RMSE is the square root of MSE. It is easier to interpret because it has the same unit as the target variable.

## R² (Coefficient of Determination)

R² measures how well the model explains the variation in the target variable. A value closer to 1 indicates better performance.

| Metric | Unit           | Sensitive to Large Errors | Best Value  |
| ------ | -------------- | ------------------------- | ----------- |
| MAE    | Same as target | No                        | Lower       |
| MSE    | Squared unit   | Yes                       | Lower       |
| RMSE   | Same as target | Yes                       | Lower       |
| R²     | No unit        | No                        | Closer to 1 |

---

# 4. Underfitting and Overfitting

Underfitting happens when a model is too simple to learn the patterns in the data, resulting in poor performance on both training and testing data.

Overfitting happens when a model learns the training data too well, including noise, and performs poorly on new data.

Polynomial regression can overfit when the polynomial degree is too high.

### Methods to Prevent Overfitting

* Use simpler models.
* Apply cross-validation.
* Reduce unnecessary features.
* Collect more training data.

---

# 5. Real-World Case Study

A real-world example of regression is used by car-selling companies to estimate vehicle prices. The goal is to predict the selling price based on features such as mileage, vehicle age, location, and number of doors. Multiple Linear Regression is commonly applied because several factors influence the price. The model helps buyers and sellers estimate fair market values, improve pricing decisions, and reduce manual effort.

---

# References

1. Aurélien Géron. *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* (3rd Edition), O'Reilly, 2022.

2. Gareth James, Daniela Witten, Trevor Hastie, and Robert Tibshirani. *An Introduction to Statistical Learning* (2nd Edition), Springer, 2021.

3. Christopher M. Bishop. *Pattern Recognition and Machine Learning*, Springer, 2006.
