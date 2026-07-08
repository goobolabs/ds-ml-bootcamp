- Introduction to Regression
  Regression in Machine Learning is a supervised learning technique used to predict a continuous numerical value based on one or more input features (e.g., predicting a price, temperature, or score).
  Difference from classification: Regression predicts continuous outputs (numbers), while classification predicts discrete categories or labels (e.g., "spam" vs "not spam"). Regression answers "how much/how many," classification answers "which class."
  Examples:

Regression: predicting a house's selling price based on size, location, and number of rooms.
Classification: predicting whether an email is spam or not spam.

# \* Types of Regression

Linear Regression

How it works: fits a straight line (y = mx + b) that best models the relationship between one independent variable and one dependent variable, minimizing the distance between predicted and actual points.
Use case: predicting sales revenue based on advertising spend.
Advantages: simple, fast, easy to interpret.
Limitations: only works well when the relationship is truly linear; sensitive to outliers.

Multiple Linear Regression

How it works: extends linear regression to use two or more independent variables to predict one dependent variable (y = b0 + b1x1 + b2x2 + ...).
Use case: predicting house prices using size, location, and number of bedrooms together.
Advantages: captures more real-world complexity than simple linear regression; still interpretable.
Limitations: vulnerable to multicollinearity (when predictors are correlated with each other), and adding too many variables can cause overfitting.

## Polynomial Regression

How it works: models nonlinear relationships by adding polynomial terms (x², x³, etc.) to the regression equation, allowing a curved line/fit instead of a straight one.
Use case: modeling the growth rate of a population or the dose-response curve of a drug, where the relationship isn't a straight line.
Advantages: can capture curved/non-linear patterns that linear models miss.
Limitations: high-degree polynomials easily overfit the data and become unstable outside the training range.

# \* Regression Metrics

MAE (Mean Absolute Error): average of the absolute differences between predicted and actual values. Measures average error magnitude in the same units as the target.
MSE (Mean Squared Error): average of the squared differences between predicted and actual values. Penalizes larger errors more heavily.
RMSE (Root Mean Squared Error): square root of MSE, bringing the error back into the original units while still penalizing large errors.
R² (Coefficient of Determination): proportion of variance in the target variable explained by the model, ranging roughly from 0 to 1 (closer to 1 = better fit).

![1782830903616](image/paper/1782830903616.png)

## \* Underfitting and Overfitting

Underfitting: the model is too simple to capture the underlying pattern, leading to poor performance on both training and test data (e.g., fitting a straight line to clearly curved data).
Overfitting: the model is too complex and learns noise/random fluctuations in the training data rather than the true pattern, performing great on training data but poorly on new data.
Cause in polynomial regression: using a very high-degree polynomial makes the curve bend excessively to fit every training point, including noise, which fails to generalize.

Ways to prevent overfitting:

Use regularization techniques (Ridge or Lasso regression) to penalize overly complex models.
Use cross-validation to test model performance on unseen data and choose an appropriate polynomial degree.
Collect more training data or simplify the model (fewer features/lower degree).

## Real-World Case Study

- A health insurance company applied linear regression to predict future healthcare costs for policyholders, using historical claims data, treatment types, and patient demographics as inputs to forecast costs and adjust premiums. Medium

Goal: improve the accuracy of cost predictions to manage financial risk and set fairer premiums.
Data used: past insurance claims, types of treatments received, and patient demographic information.
Type of regression: multiple linear regression (multiple input features predicting one continuous cost value).
Key results: the regression model improved cost prediction accuracy by 15%, helping the company better manage financial risk and offer more competitive premiums, while also enabling more dynamic, data-driven pricing strategies. Medium

This example shows how a relatively simple, interpretable regression model can produce measurable business value when applied to well-structured real-world data.
