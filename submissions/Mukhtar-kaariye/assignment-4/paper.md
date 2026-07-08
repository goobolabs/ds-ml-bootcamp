Regression — Theory and Practice
Part A: Theory

Introduction

Regression is one of the most widely used supervised machine learning techniques for predicting continuous numerical values. It identifies the relationship between one or more independent variables (features) and a dependent variable (target). By learning patterns from historical data, regression models can estimate future or unknown numerical outcomes, making them valuable in fields such as business, healthcare, finance, transportation, and education (IBM, 2024).

Unlike regression, classification predicts categorical outcomes rather than numerical values. A regression model predicts values such as house prices, employee salaries, or monthly sales, whereas a classification model predicts categories such as spam or not spam, pass or fail, or fraudulent versus legitimate transactions (Google Developers, 2024).

A practical example of regression is predicting the selling price of a used car based on features such as age, mileage, number of doors, and accident history. An example of classification is predicting whether a customer will purchase a product, where the output is either "Yes" or "No."

1. Introduction to Regression

Regression is a supervised learning technique used to predict continuous numerical values. During training, the algorithm learns the relationship between input features and the target variable, then uses this relationship to make predictions on new data. Regression is commonly applied when the goal is forecasting or estimating quantities rather than assigning categories (IBM, 2024).

The main difference between regression and classification is the type of output produced. Regression predicts numerical values such as prices, temperatures, or sales revenue, while classification predicts predefined categories such as approved or rejected, healthy or sick, and positive or negative (Microsoft Learn, 2024).

2. Types of Regression
Linear Regression

Linear Regression models the relationship between one independent variable and one dependent variable using a straight-line equation. The model assumes that as the independent variable changes, the target variable changes proportionally. It is widely used because it is simple to implement and easy to interpret (AWS, 2024).

Use Case: Predicting house prices using house size.

Advantages

Easy to understand and implement.
Fast to train.
Produces interpretable results.

Limitations

Assumes a linear relationship.
Performs poorly when relationships are complex.
Multiple Linear Regression

Multiple Linear Regression extends Linear Regression by using two or more independent variables to predict one numerical target. Instead of relying on a single feature, the model combines several variables to improve prediction accuracy (IBM, 2024).

Use Case: Predicting employee salary using education level, years of experience, and job position.

Advantages

Uses multiple predictors.
Often produces more accurate predictions.
Helps identify the contribution of each feature.

Limitations

More sensitive to multicollinearity.
Requires careful feature selection.
Polynomial Regression

Polynomial Regression is an extension of Linear Regression that captures curved relationships between variables by adding polynomial terms. Although the equation becomes more complex, it is still considered a regression technique (Google Developers, 2024).

Use Case: Predicting vehicle fuel consumption based on speed.

Advantages

Models nonlinear relationships.
Can improve prediction accuracy when data follows a curve.

Limitations

Can easily overfit the training data.
Selecting the correct polynomial degree can be difficult.

3. Regression Metrics

Regression metrics evaluate how well a model predicts numerical values. Different metrics measure prediction errors from different perspectives.

Mean Absolute Error (MAE)

MAE calculates the average absolute difference between actual values and predicted values. It is easy to interpret because the error remains in the same unit as the target variable (scikit-learn, 2025).

Mean Squared Error (MSE)

MSE calculates the average squared difference between actual and predicted values. Squaring the errors gives greater weight to large prediction mistakes, making this metric useful when large errors should be penalized (Microsoft Learn, 2024).

Root Mean Squared Error (RMSE)

RMSE is the square root of MSE. Because it returns the error in the original unit of measurement, it is easier to interpret than MSE while still penalizing larger errors (IBM, 2024).

R² (Coefficient of Determination)

R² measures how much of the variation in the target variable is explained by the regression model. Values closer to 1 indicate better model performance, while values near 0 indicate that the model explains little of the variation (AWS, 2024).

Comparison of Regression Metrics
Metric	  Unit	          Sensitive to Large Errors    Meaning
MAE	      Same as target	Low	Average                 absolute prediction error
MSE	      Squared unit	    High	                    Average squared prediction error
RMSE	  Same as target	High	                    Square root of MSE; easier to interpret
R²	      No unit	        No	                       Percentage of variance explained by the model

4. Underfitting and Overfitting

Underfitting occurs when a regression model is too simple to capture the underlying patterns in the data. As a result, it performs poorly on both the training and testing datasets.

Overfitting occurs when a model learns not only the real patterns but also the random noise in the training data. Such models usually achieve excellent training accuracy but perform poorly when making predictions on new data. Polynomial Regression is particularly prone to overfitting when a very high polynomial degree is used because the model becomes unnecessarily complex (Google Developers, 2024).

Several techniques can reduce overfitting:

Use a simpler model.
Apply cross-validation during model evaluation.
Increase the amount of training data or use regularization techniques.

5. Real-World Case Study (Business)

A business application of regression was carried out by Walmart to improve retail sales forecasting. The objective was to predict weekly sales for different stores using historical sales records, holidays, fuel prices, and weather conditions. Multiple Linear Regression was one of the methods used to understand the relationship between these variables and future sales.

The analysis showed that holidays and seasonal trends significantly influenced weekly sales. Accurate sales forecasting helped Walmart improve inventory planning, reduce stock shortages, and optimize supply chain operations. This project demonstrates how regression supports business decision-making by providing reliable numerical predictions. Within the Data Science lifecycle, the project included data collection, preprocessing, model building, evaluation, and deployment for business forecasting (Kaggle, 2014).

References

AWS. (2024). What is regression? https://aws.amazon.com/what-is/regression/

Google Developers. (2024). Introduction to machine learning. https://developers.google.com/machine-learning/crash-course

IBM. (2024). Regression analysis. https://www.ibm.com/think/topics/regression-analysis

Kaggle. (2014). Walmart recruiting: Store sales forecasting. https://www.kaggle.com/competitions/walmart-recruiting-store-sales-forecasting

Microsoft Learn. (2024). Introduction to regression models. https://learn.microsoft.com/en-us/training/modules/train-evaluate-regression-models/

scikit-learn. (2025). Regression metrics. https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics

This version follows your requested style: concise, academic, easy to read, uses website references with matching in-text citations, includes the required comparison table, and keeps the content within the expected 2–3 page length.