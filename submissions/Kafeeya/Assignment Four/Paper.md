1. Introduction to Regression
What is Regression in Machine Learning?
Regression is a supervised machine learning technique used to predict continuous numerical values based on input features. It finds the relationship between independent variables (features) and a dependent variable (target).
For example, regression can predict:
•	House prices
•	Student exam scores
•	Sales revenue
•	Temperature
How is Regression Different from Classification?
Regression	Classification
Predicts continuous numerical values	Predicts categories or classes
Output is a number	Output is a label
Example: Predict house price	Example: Predict spam or not spam
Real-Life Examples
Regression Example:
A real estate company predicts the selling price of a house using its size, location, and number of bedrooms.
Classification Example:
An email system predicts whether an email is Spam or Not Spam.
2. Types of Regression
A. Linear Regression
Basic Idea
Linear Regression models a straight-line relationship between one independent variable and one dependent variable.
Equation:
[
Y = b_0 + b_1X
]
Where:
•	Y = predicted value
•	X = independent variable
•	b₀ = intercept
•	b₁ = slope
Real-World Use Case
Predicting house prices using only house size.
Advantages
•	Simple to understand
•	Fast to train
•	Easy to interpret
Limitations
•	Assumes a linear relationship
•	Performs poorly with complex data
•	Sensitive to outliers
B. Multiple Linear Regression
Basic Idea
Multiple Linear Regression uses two or more independent variables to predict one target variable.
Equation:
[
Y = b_0 + b_1X_1 + b_2X_2 + ... + b_nX_n
]
Real-World Use Case
Predicting employee salary using:
•	Education
•	Experience
•	Age
•	Skills
Advantages
•	Uses more information
•	More accurate than simple linear regression
•	Can analyze the effect of multiple variables
Limitations
•	Can suffer from multicollinearity
•	More complex to interpret
•	Requires more data
C. Polynomial Regression
Basic Idea
Polynomial Regression models curved relationships by adding powers of the independent variable.
Example:
[
Y=b_0+b_1X+b_2X^2+b_3X^3
]
Real-World Use Case
Predicting crop growth over time or vehicle fuel consumption.
Advantages
•	Captures nonlinear relationships
•	More flexible
•	Better fit for complex datasets
Limitations
•	Easily overfits the data
•	More computationally expensive
•	Harder to interpret
Comparison of Regression Types
Type	Number of Features	Relationship	Example
Linear Regression	1	Straight line	House price vs size
Multiple Linear Regression	Multiple	Straight line	Salary prediction
Polynomial Regression	1 or more	Curved	Crop growth prediction

3. Regression Metrics
A. MAE (Mean Absolute Error)
Definition
MAE is the average of the absolute differences between actual and predicted values.
Formula
[
MAE=\frac{1}{n}\sum|y-\hat y|
]
Measures
Average prediction error.
Interpretation
Lower MAE means better model performance.
B. MSE (Mean Squared Error)
Definition
MSE calculates the average squared difference between actual and predicted values.
Formula
[
MSE=\frac{1}{n}\sum(y-\hat y)^2
]
Measures
Average squared error.
Interpretation
Large errors receive much larger penalties.
C. RMSE (Root Mean Squared Error)
Definition
RMSE is the square root of MSE.
Formula
[
RMSE=\sqrt{MSE}
]
Measures
Prediction error in the same unit as the target variable.
Interpretation
Lower RMSE indicates better predictions.
D. R² (Coefficient of Determination)
Definition
R² measures how well the model explains the variation in the target variable.
Range
0 to 1
•	1 = Perfect prediction
•	0 = Poor prediction
Interpretation
Higher R² indicates a better model fit.
Comparison Table
Metric	Units	Sensitive to Large Errors?	Meaning
MAE	Same as target	No	Average absolute error
MSE	Squared units	Yes	Average squared error
RMSE	Same as target	Yes	Root of squared error
R²	No units	No	Percentage of variance explained

4. Under fitting and Over fitting
Underfitting
Underfitting occurs when a model is too simple to learn the patterns in the data.
Characteristics
•	High training error
•	High testing error
•	Poor predictions
Example:
Using a straight line to fit highly curved data.
Overfitting
Overfitting occurs when a model learns the training data too well, including noise and random fluctuations.
Characteristics
•	Very low training error
•	High testing error
•	Poor generalization
Causes of Overfitting (Especially in Polynomial Regression)
•	Using a very high polynomial degree
•	Too many features
•	Small training dataset
•	Learning noise instead of actual patterns
Methods to Prevent Overfitting
1.	Use a lower-degree polynomial.
2.	Apply regularization techniques (such as Ridge or Lasso Regression).
3.	Increase the amount of training data or use cross-validation.
5. Real-World Case Study
Healthcare: Predicting Medical Insurance Charges
Goal
Predict a person's medical insurance charges based on personal characteristics.
Data Used
The dataset included:
•	Age
•	Body Mass Index (BMI)
•	Smoking status
•	Number of children
•	Gender
•	Region
Type of Regression
Multiple Linear Regression
Key Results and Insights
•	Smoking status was the strongest predictor of higher insurance charges.
•	Age and BMI also had a significant impact on costs.
•	The model helped estimate future healthcare expenses and supported pricing decisions for insurance companies.
Conclusion
Regression is a fundamental supervised machine learning technique used to predict continuous values. Linear Regression is suitable for simple relationships, Multiple Linear Regression handles multiple input variables, and Polynomial Regression models nonlinear patterns. Model performance is commonly evaluated using MAE, MSE, RMSE, and R². To build reliable models, it is important to avoid underfitting and overfitting by selecting appropriate model complexity, using regularization, and validating performance on unseen data. Regression is widely applied in fields such as business, healthcare, education, finance, and transportation to support accurate predictions and informed decision-making.

