# Part A — Theory

## 1. Introduction to Regression

Regression is a supervised learning technique used to predict continuous numerical values by learning relationships between input variables (features) and an output variable (target). It helps understand how changes in one or more factors influence a measurable outcome and is widely used in forecasting, risk analysis, decision-making and trend estimation.

#### How is it different from classification?
To understand how machine learning models make predictions, it’s important to know the difference between Classification and Regression. Both are supervised learning techniques, but they solve different types of problems depending on the nature of the target variable.

- Classification predicts categories or labels like spam/not spam, disease/no disease, etc.
- Regression predicts continuous values like price, temperature, sales, etc.

### real-life example of regression and one of classification.
- regression 
 Predicting the exact sale price of a house.

- classification exampla
   Identifying whether an incoming email is "Spam" or "Not Spam"

## 2. Types of Regression

**Linear regression** is a statistical technique used to find the relationship between variables. In an ML context, linear regression finds the relationship between features and a label

### How It Works linear regression
Simple Linear Regression models the relationship between one independent variable (predictor) and one dependent variable (target) by fitting a straight line to the observed data. The goal is to find the line of best fit that minimizes the sum of squared errors (the distances between the actual data points and the line).

### Real-World Use Case
Predicting house prices based on house size.

### Advantages
- Simple and easy to understand.
- Fast to train and implement.
- Results are highly interpretable.

### Limitations
- Assumes a linear relationship between variables.
- Cannot capture complex patterns in data.
- Sensitive to outliers.

# 2. Multiple Linear Regression
**Multiple Linear Regression** is a statistical method used to predict the value of a dependent variable based on two or more independent variables

## How It Works
Multiple Linear Regression extends Linear Regression by using two or more independent variables to predict a target value.

## Real-World Use Case
Predicting house prices based on:

- House size
- Number of bedrooms
- Number of bathrooms
- Location rating
Using multiple factors usually produces more accurate predictions than using only one feature.

## Advantages
Uses multiple factors to make predictions.
Often more accurate than simple Linear Regression.
Helps identify the influence of each feature on the target variable.

## Limitations
Assumes a linear relationship between features and the target.
Can suffer from multicollinearity (when features are highly correlated).
More complex than simple Linear Regression.


### 3. Polynomial Regression
Polynomial Regression is used when the relationship between the input and output is non-linear. Instead of fitting a straight line, it fits a curve by adding polynomial terms.

#### Real-World Use Case
Predicting fuel consumption based on vehicle speed.

Fuel consumption often does not change in a straight-line pattern as speed increases, making Polynomial Regression a better choice.

### Advantages
Can model non-linear relationships.
More flexible than Linear Regression.
Often provides better accuracy for curved data patterns.

### Limitations
Higher-degree polynomials may cause overfitting.
More difficult to interpret.
Performance can decrease on new data if the model becomes too complex.

# 3. Regression Metrics
Mean Absolute Error (MAE) is a popular evaluation metric used to measure the average magnitude of errors in a set of predictions

Mean Squared Error (MSE) is a standard metric used in statistics and machine learning to measure the average squared difference between estimated values and actual values.

Root Mean Squared Error (RMSE) is a standard metric used to measure the difference between values predicted by a model and the actual observed values.

R² (Coefficient of Determination):  is a statistical metric that measures the proportion of variance in a dependent variable that is explained by the independent variable(s) in a regression model

|Metric|Units|Sensitivity to Large Errors|Meaning|
|------|-----|---------------------------|-------|
|MAE   |Same as target variable| Low |Average absolute error between actual and predicted values|
|MSE   |Squared units of target variable| Very High |Average squared error between actual and predicted values |
|RMSE  |Same as target variable| High |Typical size of prediction errors|
|R²    | No unit| N/A| Proportion of variance explained by the model|

# 4.  Underfitting and Overfitting
underfitting means the model is too simple to capture the underlying trend, while 
overfitting means the model is too complex and memorizes the training data, including random noise

### What causes overfitting, especially in polynomial regression?
 In polynomial regression, this occurs because higher-degree polynomials introduce excessive flexibility, leading to wild oscillations and poor predictions on unseen data

 ###  methods to prevent overfitting.
- Use More Training Data
- Reduce Model Complexity
- Cross-Validation

# 5. Real-World Case Study
## Predicting Medical Insurance Costs
A health insurance company wanted to predict the annual medical insurance charges of customers. Accurate predictions help the company set appropriate insurance premiums and manage financial risk.

## Data Used
The dataset included information about policyholders such as:

- Age
- Gender
- Body Mass Index (BMI)
- Number of children
- Smoking status
- Region
- Annual medical charges (target variable)

## Type of Regression Applied
**Multiple Linear Regression**
Multiple Linear Regression was used because medical costs are affected by several factors simultaneously.

## Key Results and Insights
- Smoking status was the most influential factor affecting medical costs.
- Higher BMI was associated with higher healthcare expenses.
- Older individuals generally had higher medical charges.
- The model successfully identified the factors that contributed most to healthcare spending.

## Conclusion
This healthcare project shows how Multiple Linear Regression can be used to predict medical insurance costs and reveal the factors that have the greatest impact on healthcare expenses. It demonstrates the practical value of regression in data-driven decision-making within the healthcare industry.