Assignment Four – Part A: Regression Theory and Practice
1. Introduction to Regression
What is Regression in Machine Learning?

Regression is a supervised machine learning technique used to predict continuous numerical values based on one or more input variables. The goal of regression is to learn the relationship between the input features (independent variables) and the target variable (dependent variable). Once trained, the model can estimate future or unknown values.

Regression is widely used in many industries because it helps organizations make predictions using historical data. Examples include predicting house prices, sales revenue, fuel consumption, stock prices, and weather temperatures.

Difference Between Regression and Classification

Although both regression and classification are supervised learning methods, they solve different types of problems.

Regression predicts continuous numerical values such as prices, temperatures, or salaries.

Classification predicts categories or classes such as "Yes" or "No," "Spam" or "Not Spam," or "Healthy" or "Diseased."

For example, predicting the selling price of a car is a regression problem because the output is a number. Predicting whether an email is spam is a classification problem because the output belongs to one of two categories.

Real-Life Examples

Regression Example:
A real estate company predicts the selling price of a house based on its size, location, number of bedrooms, and age.

Classification Example:
A bank predicts whether a customer will repay a loan or default.

2. Types of Regression
Linear Regression
Basic Idea

Linear Regression is the simplest regression algorithm. It assumes that there is a straight-line relationship between the independent variable and the dependent variable. The model finds the best-fitting line by minimizing prediction errors.

Real-World Use Case

Predicting house prices based only on house size.

Advantages
Simple and easy to understand.
Fast to train.
Easy to interpret.
Works well when the relationship is linear.
Limitations
Cannot model complex relationships.
Sensitive to outliers.
Assumes linearity between variables.
Multiple Linear Regression
Basic Idea

Multiple Linear Regression extends Linear Regression by using two or more independent variables to predict the target value.

Instead of using only house size, it can also use location, number of bedrooms, age of the house, and parking spaces.

Real-World Use Case

Predicting car prices using mileage, brand, engine size, year, and fuel type.

Advantages
More accurate than simple linear regression.
Uses multiple factors for prediction.
Useful for real-world datasets.
Limitations
More difficult to interpret.
Can suffer from multicollinearity when features are highly correlated.
Still assumes a linear relationship.
Polynomial Regression
Basic Idea

Polynomial Regression models curved relationships by adding polynomial terms such as x² or x³. Although it is based on linear regression, it can fit nonlinear patterns.

Real-World Use Case

Predicting population growth or temperature changes where the relationship is curved rather than linear.

Advantages
Can model nonlinear relationships.
More flexible than linear regression.
Often provides better accuracy when data is curved.
Limitations
High-degree polynomials may overfit the training data.
Harder to interpret.
Sensitive to noise and outliers.
3. Regression Metrics

Regression metrics measure how well a model predicts continuous values.

Mean Absolute Error (MAE)

MAE is the average of the absolute differences between predicted values and actual values.

It tells us the average prediction error without considering whether the prediction is too high or too low.

A smaller MAE indicates better model performance.

Mean Squared Error (MSE)

MSE is the average of squared prediction errors.

Squaring gives more weight to large errors, making MSE useful when large mistakes are especially undesirable.

Lower MSE values indicate better performance.

Root Mean Squared Error (RMSE)

RMSE is the square root of MSE.

Because it is measured in the same units as the target variable, it is easier to interpret than MSE.

RMSE also penalizes large errors more heavily than MAE.

R² (Coefficient of Determination)

R² measures how much of the variation in the target variable is explained by the model.

R² = 1 means perfect prediction.
R² = 0 means the model performs no better than predicting the average.
Higher R² values indicate a better model.
Comparison of Regression Metrics
Metric	Measures	Units	Sensitive to Large Errors	Better Value
MAE	Average absolute error	Same as target	Low	Lower
MSE	Average squared error	Squared units	Very High	Lower
RMSE	Square root of MSE	Same as target	High	Lower
R²	Explained variance	No units	Not directly	Higher
4. Underfitting and Overfitting
Underfitting

Underfitting occurs when a model is too simple to learn the patterns in the data.

An underfitted model performs poorly on both the training data and new unseen data because it cannot capture the underlying relationships.

Example:
Using a straight-line model to fit highly curved data.

Overfitting

Overfitting occurs when a model learns not only the true patterns but also the random noise in the training data.

An overfitted model achieves excellent training accuracy but performs poorly on new data.

Causes of Overfitting

Overfitting is especially common in Polynomial Regression when:

The polynomial degree is too high.
The dataset is too small.
There are too many input features.
The model is too complex.
Methods to Prevent Overfitting

Some common methods include:

Use a lower polynomial degree.
Collect more training data.
Apply regularization techniques such as Ridge or Lasso Regression.
Use cross-validation to evaluate the model.
Remove unnecessary features through feature selection.

These methods improve the model's ability to generalize to new data.

5. Real-World Case Study
Predicting House Prices Using Multiple Linear Regression
Goal

A real estate company wanted to predict house prices accurately to help buyers and sellers make informed decisions.

Data Used

The dataset included:

House size
Number of bedrooms
Number of bathrooms
Location
Age of the house
Garage size

Thousands of house records were collected from previous sales.

Regression Method

The project used Multiple Linear Regression because house prices depend on several factors rather than a single variable.

Results

The model successfully identified the most important factors affecting house prices. House size and location had the greatest influence on price. The predictions helped improve pricing decisions and reduced estimation errors compared to manual valuation methods.

This case demonstrates how regression can support data-driven decision-making in the real estate industry.

References
An Introduction to Statistical Learning
Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow
Pattern Recognition and Machine Learning