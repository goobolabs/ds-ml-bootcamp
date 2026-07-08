# Part A : theory
## lesson 4 Regression :

Introduction to Regression
Regression is a supervised Machine Learning technique used to predict continuous numerical values from input data. It helps identify relationships between variables and estimate future outcomes. Regression is commonly used when the output is a number, such as predicting prices, temperatures, or sales.

Regression differs from classification because regression predicts numerical values, while classification predicts categories or labels. For example:

Regression example: Predicting the price of a used car.

Classification example: Predicting whether an email is spam or not spam.

---

Types of Regression

1. Linear Regression

Linear Regression models the relationship between one independent variable and one dependent variable using a straight line.

How it works:
The algorithm finds the best-fit line that minimizes prediction errors.

Real-world use case:
Predicting employee salary based on years of experience.

Advantages:

- Easy to understand
- Fast to train
- Simple implementation

Limitations:

- Cannot model complex relationships
- Sensitive to outliers
- Assumes linear relationships

---

2. Multiple Linear Regression

Multiple Linear Regression uses multiple independent variables to predict a target variable.

How it works:
Several variables are combined together to estimate one output value.

Real-world use case:
Predicting house prices using area, number of rooms, and location.

Advantages:

- Uses several features
- More realistic for real-world problems
- Often more accurate

Limitations:

- Sensitive to multicollinearity
- Requires more data
- Can become difficult to interpret

---

3. Polynomial Regression

Polynomial Regression models nonlinear relationships by fitting a curve instead of a straight line.

How it works:
Polynomial terms are added to capture more complex patterns.

Real-world use case:
Predicting population growth over time.

Advantages:

- Captures nonlinear patterns
- Flexible model

Limitations:

- High risk of overfitting
- More complex
- Harder to interpret

---

Regression Metrics

MAE (Mean Absolute Error)

MAE measures the average absolute difference between actual values and predicted values.

MSE (Mean Squared Error)

MSE measures the average squared difference between predicted and actual values.

RMSE (Root Mean Squared Error)

RMSE is the square root of MSE and represents prediction error in the original units.

R² (Coefficient of Determination)

R² measures how much variation in the target variable is explained by the model.

Metric| Units| Sensitivity to Large Errors| Meaning
MAE| Same as target| Low| Average absolute error
MSE| Squared units| High| Average squared error
RMSE| Same as target| High| Standard prediction error
R²| No units| Medium| Explained variance

---

Underfitting and Overfitting

Underfitting happens when a model is too simple and fails to learn patterns from data.

Overfitting happens when a model learns unnecessary details and noise from training data.

Polynomial regression can cause overfitting when a very high polynomial degree is used.

Methods to prevent overfitting:

- Use more training data
- Apply cross-validation
- Use regularization techniques

---

Real-World Case Study

Car Price Prediction System

Goal:
Estimate used car prices accurately.

Data used:

- Mileage
- Model year
- Fuel type
- Engine size
- Transmission type

Type of Regression Applied:
Multiple Linear Regression

Results and Insights:

The study showed that car age and mileage strongly affected vehicle prices. Newer cars with lower mileage generally had higher prices. Regression models improved prediction accuracy and supported better decision-making.

---

References

1. Géron, A. Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow.

2. James, G., Witten, D., Hastie, T., Tibshirani, R. An Introduction to Statistical Learning.

3. Scikit-Learn Documentation.
