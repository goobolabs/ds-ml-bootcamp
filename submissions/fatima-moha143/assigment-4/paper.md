# Introduction to Regression

## What is Regression in Machine Learning?

Regression is a supervised machine learning technique used to predict continuous numerical values. The goal of regression is to find the relationship between one or more input variables (features) and a target variable. By learning patterns from historical data, regression models can estimate future or unknown values.

For example, a regression model can predict house prices based on factors such as size, location, and number of bedrooms. The output is a number rather than a category.

## Difference Between Regression and Classification

Although both regression and classification are supervised learning methods, they solve different types of problems.

Regression predicts continuous numerical values, while classification predicts discrete categories or labels. For instance, predicting the price of a house is a regression problem because the output can be any numerical value. In contrast, determining whether an email is spam or not spam is a classification problem because the output belongs to a specific category.

### Examples

**Regression Example:** Predicting the monthly sales revenue of a business.

**Classification Example:** Determining whether a customer will buy a product (Yes/No).

---

# Types of Regression

## 1. Linear Regression

### How It Works

Linear Regression models the relationship between a single independent variable and a dependent variable using a straight line. The model attempts to find the best-fitting line that minimizes prediction errors.

The general equation is:

**y = mx + b**

Where:

* y = predicted value
* x = input feature
* m = slope of the line
* b = intercept

### Real-World Use Case

A real estate company may use linear regression to predict house prices based solely on house size.

### Advantages

* Simple and easy to understand.
* Fast to train and interpret.
* Works well when relationships are approximately linear.

### Limitations

* Cannot accurately model complex nonlinear relationships.
* Sensitive to outliers.
* Assumes a linear relationship between variables.

---

## 2. Multiple Linear Regression

### How It Works

Multiple Linear Regression extends linear regression by using two or more independent variables to predict a target value.

The equation is:

**y = b₀ + b₁x₁ + b₂x₂ + ... + bₙxₙ**

This approach allows the model to consider multiple factors simultaneously.

### Real-World Use Case

Predicting house prices using size, number of bedrooms, age of the property, and location.

### Advantages

* More realistic than simple linear regression.
* Can capture the influence of several variables.
* Useful for understanding the impact of different factors.

### Limitations

* Requires more data.
* Can suffer from multicollinearity when predictors are highly correlated.
* Interpretation becomes more complex as variables increase.

---

## 3. Polynomial Regression

### How It Works

Polynomial Regression is used when the relationship between variables is nonlinear. Instead of fitting a straight line, it fits a curve by adding polynomial terms such as x², x³, and higher powers.

Example equation:

**y = b₀ + b₁x + b₂x²**

Although the curve is nonlinear, the model is still trained using regression techniques.

### Real-World Use Case

Predicting vehicle fuel consumption at different speeds, where the relationship is not perfectly linear.

### Advantages

* Captures nonlinear relationships effectively.
* Often achieves better accuracy than linear models when data follows a curved pattern.
* Flexible and adaptable.

### Limitations

* More likely to overfit the training data.
* Becomes complex with high-degree polynomials.
* Harder to interpret than linear regression.

---

## Comparison of Regression Types

| Feature             | Linear Regression | Multiple Linear Regression | Polynomial Regression |
| ------------------- | ----------------- | -------------------------- | --------------------- |
| Number of Features  | One               | Multiple                   | One or more           |
| Relationship Type   | Linear            | Linear                     | Nonlinear             |
| Complexity          | Low               | Medium                     | High                  |
| Interpretability    | High              | Medium                     | Low                   |
| Risk of Overfitting | Low               | Medium                     | High                  |

---

# Regression Metrics

Regression metrics evaluate how well a model predicts numerical values.

## MAE (Mean Absolute Error)

MAE measures the average absolute difference between predicted values and actual values.

Formula:

**MAE = Σ|Actual − Predicted| / n**

### What It Measures

It shows the average prediction error without considering direction.

### Interpretation

A lower MAE indicates better model performance.

---

## MSE (Mean Squared Error)

MSE calculates the average of squared prediction errors.

Formula:

**MSE = Σ(Actual − Predicted)² / n**

### What It Measures

It penalizes larger errors more heavily because errors are squared.

### Interpretation

Lower MSE values indicate better predictions.

---

## RMSE (Root Mean Squared Error)

RMSE is the square root of MSE.

Formula:

**RMSE = √MSE**

### What It Measures

It represents the average prediction error while maintaining the original unit of measurement.

### Interpretation

Smaller RMSE values indicate higher model accuracy.

---

## R² (Coefficient of Determination)

R² measures the proportion of variance in the target variable explained by the model.

Formula:

**R² = 1 − (Residual Sum of Squares / Total Sum of Squares)**

### What It Measures

It indicates how well the model explains the data.

### Interpretation

* R² = 1 → Perfect prediction
* R² = 0 → No explanatory power
* Higher values indicate better model fit

---

## Comparison of Regression Metrics

| Metric | Units                   | Sensitive to Large Errors | Meaning                          |
| ------ | ----------------------- | ------------------------- | -------------------------------- |
| MAE    | Same as target variable | Low                       | Average absolute error           |
| MSE    | Squared units           | Very High                 | Average squared error            |
| RMSE   | Same as target variable | High                      | Average prediction error         |
| R²     | No units                | Indirectly                | Percentage of variance explained |

---

# Underfitting and Overfitting

## Underfitting

Underfitting occurs when a model is too simple to capture the underlying patterns in the data. As a result, it performs poorly on both training and testing datasets.

### Example

Using a straight-line model to predict a strongly curved relationship.

---

## Overfitting

Overfitting occurs when a model learns not only the true patterns but also random noise in the training data. The model performs extremely well on training data but poorly on new, unseen data.

### Causes of Overfitting

In polynomial regression, overfitting often occurs when a very high-degree polynomial is used. The model becomes excessively flexible and fits every small variation in the training data, including noise.

Other causes include:

* Insufficient training data.
* Too many features.
* Complex models relative to dataset size.

---

## Methods to Prevent Overfitting

### 1. Use Simpler Models

Choose lower-degree polynomial functions when possible.

### 2. Cross-Validation

Evaluate the model on multiple data subsets to ensure good generalization.

### 3. Regularization

Techniques such as Ridge and Lasso Regression penalize overly complex models and reduce overfitting.

---

# Real-World Case Study

## Predicting House Prices Using Multiple Linear Regression

### Goal

One of the most common real-world applications of regression is predicting house prices. Real estate companies and researchers use regression models to estimate property values based on multiple characteristics.

### Data Used

The dataset typically includes:

* House size (square feet)
* Number of bedrooms
* Number of bathrooms
* Property age
* Location
* Lot size

### Type of Regression Applied

Researchers commonly use **Multiple Linear Regression** because house prices depend on several factors simultaneously.

### Key Results and Insights

Studies have shown that house size and location are often the strongest predictors of price. Multiple linear regression allows analysts to quantify how much each feature contributes to the final property value.

The model helps:

* Buyers estimate fair market prices.
* Sellers set competitive prices.
* Real estate agencies make informed decisions.
* Banks assess property values for mortgage approval.

This application demonstrates how regression transforms historical data into actionable insights and supports data-driven decision-making.

---

# References

1. Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O’Reilly Media.

2. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning* (2nd ed.). Springer.

3. Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.

4. Hastie, T., Tibshirani, R., & Friedman, J. (2017). *The Elements of Statistical Learning*. Springer.

5. IBM. (2024). Machine Learning and Regression Analysis Documentation.
