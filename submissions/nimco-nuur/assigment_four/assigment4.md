Regression in Machine Learning: Car Price Prediction Study
1. Introduction to Regression

Regression is a supervised machine learning technique used to predict continuous numerical values based on input features. It models the relationship between independent variables (features) and a dependent variable (target).

Unlike classification, which predicts categories such as “Yes/No” or “Spam/Not Spam,” regression predicts real-valued outputs such as price, temperature, or salary.

In this study, regression is applied to predict car prices based on features such as mileage, year, accidents, and location.

Real-world examples:

Predicting house prices based on size and location (regression)
Predicting whether a loan will be approved (classification)
2. Types of Regression
2.1 Linear Regression

Linear Regression is the simplest form of regression. It assumes a linear relationship between input variables and the output.

Formula:
y = b0 + b1x1 + b2x2 + ... + bnxn

Working principle:
It finds the best-fit line that minimizes the error between predicted and actual values.

Use case:
Predicting car prices using mileage and manufacturing year.

Advantages:

Simple and easy to interpret
Fast computation
Works well with linear relationships

Limitations:

Cannot capture complex patterns
Sensitive to outliers
2.2 Multiple Linear Regression

Multiple Linear Regression extends simple linear regression by using multiple input features simultaneously.

It assumes all features contribute linearly to the target variable.

Use case:
Car price prediction using mileage, year, accidents, and location.

Advantages:

More realistic than simple regression
Uses multiple features for better prediction

Limitations:

Still assumes linear relationships
Can struggle with complex nonlinear data
2.3 Polynomial Regression

Polynomial Regression extends linear regression by adding polynomial terms such as squares or cubes of features.

Example:
y = ax² + bx + c

Use case:
Modeling nonlinear relationships such as growth trends or complex pricing behavior.

Advantages:

Captures nonlinear relationships
More flexible than linear regression

Limitations:

Can easily overfit the data
Becomes complex with high-degree polynomials
3. Regression Metrics

Regression models are evaluated using the following metrics:

Metric	Meaning	Sensitivity	Unit
MAE (Mean Absolute Error)	Average absolute difference between predicted and actual values	Medium	Same as target
MSE (Mean Squared Error)	Average squared differences	High (penalizes large errors)	Squared units
RMSE (Root Mean Squared Error)	Square root of MSE, more interpretable	High	Same as target
R² (Coefficient of Determination)	Measures how well the model explains variance	—	0 to 1

Interpretation:

MAE shows average error size
RMSE penalizes large mistakes more heavily
R² shows overall model performance
4. Underfitting and Overfitting
Underfitting

Underfitting occurs when the model is too simple to capture patterns in the data. It performs poorly on both training and testing datasets.

Causes:

Simple models
Insufficient features
High bias
Overfitting

Overfitting occurs when the model learns the training data too well, including noise, resulting in poor generalization on new data.

Common in:

High-degree polynomial regression
Complex decision trees

Causes:

Too many parameters
Small datasets
No regularization
Prevention methods:
Cross-validation
Regularization techniques (L1, L2)
Reducing model complexity
Increasing dataset size
5. Real-World Case Study: Car Price Prediction

Car price prediction is widely used in automotive marketplaces such as online car sales platforms.

Goal:
Estimate the fair market value of a used car.

Data used:

Mileage (Odometer)
Manufacturing year
Accident history
Location type (urban/rural)
Car age

Models applied:

Linear Regression
Random Forest Regression

Findings:
Random Forest performed better than Linear Regression because it can capture nonlinear relationships between features and price. Linear Regression struggled with complex patterns and produced higher prediction errors.

6. Conclusion

Regression is a fundamental machine learning technique used for predicting continuous values. In this study, both Linear Regression and Random Forest were applied to car price prediction.

The results show that ensemble methods like Random Forest generally outperform linear models due to their ability to capture complex relationships in data. However, Linear Regression remains valuable for its simplicity and interpretability.

Future improvements include adding more features such as car brand, engine size, and fuel type to improve prediction accuracy.