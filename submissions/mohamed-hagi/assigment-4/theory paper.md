# Part A – Theory: Regression in Machine Learning

Regression is a supervised machine learning technique used to predict continuous numerical values based on input data. The goal of a regression model is to identify the relationship between one or more independent variables (features) and a dependent variable (target). By learning patterns from historical data, the model can estimate numerical outcomes for new observations.

### Difference Between Regression and Classification

Although both regression and classification are supervised learning methods, they solve different types of problems.

Regression predicts continuous numerical values, while classification predicts categories or class labels. For example, regression may predict the selling price of a car, whereas classification determines whether a loan application should be approved or rejected.

**Examples**

* **Regression:** Predicting the selling price of a used car based on its age, mileage, engine size, and brand.
* **Classification:** Predicting whether a customer will default on a loan (Default or No Default).

---

# Types of Regression

## 1. Linear Regression

Linear Regression models the relationship between one independent variable and one dependent variable using a straight-line equation. It assumes that changes in the independent variable result in proportional changes in the dependent variable.

### Real-World Use Case

A company can use Linear Regression to predict monthly sales based on advertising expenditure.

### Advantages

* Simple and easy to understand.
* Fast to train and interpret.
* Performs well when the relationship is approximately linear.

### Limitations

* Assumes a linear relationship between variables.
* Sensitive to outliers.
* Cannot accurately model complex nonlinear patterns.

---

## 2. Multiple Linear Regression

### Basic Idea

Multiple Linear Regression extends Linear Regression by using two or more independent variables to predict a single numerical target. It estimates how each feature contributes to the final prediction.

### Real-World Use Case

Predicting house prices using features such as location, number of bedrooms, house size, age, and nearby facilities.

### Advantages

* Uses multiple factors for more accurate predictions.
* Helps identify the influence of each feature.
* Suitable for many practical business applications.

### Limitations

* Sensitive to multicollinearity among features.
* Assumes linear relationships.
* Performance decreases if irrelevant variables are included.

---

## 3. Polynomial Regression

Polynomial Regression models nonlinear relationships by adding polynomial terms (such as squared or cubic values) to the regression equation. This allows the model to fit curved patterns in the data.

### Real-World Use Case

Predicting vehicle fuel consumption where the relationship between engine speed and fuel usage is nonlinear.

### Advantages

* Captures complex nonlinear relationships.
* Can significantly improve prediction accuracy when data follows a curved pattern.

### Limitations

* Higher risk of overfitting.
* More difficult to interpret.
* Choosing the correct polynomial degree can be challenging.

# Regression Metrics

Regression models are evaluated using several performance metrics.

## Mean Absolute Error (MAE)

MAE measures the average absolute difference between predicted values and actual values. It treats every error equally and is easy to interpret.

A lower MAE indicates better model performance.

---

## Mean Squared Error (MSE)

MSE calculates the average of the squared prediction errors. Squaring the errors gives greater importance to larger mistakes.

A lower MSE indicates better performance.

---

## Root Mean Squared Error (RMSE)

RMSE is the square root of MSE. Because it is expressed in the same unit as the target variable, it is easier to interpret than MSE.

Lower RMSE values indicate more accurate predictions.

---

## R² (Coefficient of Determination)

R² measures how well the regression model explains the variation in the target variable.

Its value ranges from 0 to 1.

* **R² = 1** means perfect prediction.
* **R² = 0** means the model explains none of the variation.

Higher R² values indicate a better-fitting model.

---

## Comparison of Regression Metrics

| Metric | What It Measures                  | Units          | Sensitive to Large Errors | Interpretation   |
| ------ | --------------------------------- | -------------- | ------------------------- | ---------------- |
| MAE    | Average absolute prediction error | Same as target | Low                       | Lower is better  |
| MSE    | Average squared prediction error  | Squared units  | High                      | Lower is better  |
| RMSE   | Square root of MSE                | Same as target | High                      | Lower is better  |
| R²     | Proportion of variance explained  | Unitless       | No                        | Higher is better |

---

# Underfitting and Overfitting

## Underfitting

Underfitting occurs when a regression model is too simple to capture the underlying patterns in the data. As a result, the model performs poorly on both training and testing datasets.

## Overfitting

Overfitting occurs when a model learns not only the true relationships in the training data but also random noise. Although it performs very well on training data, its performance decreases significantly on new, unseen data.

### Why Polynomial Regression Can Overfit

Polynomial Regression may overfit when a polynomial of very high degree is used. A highly flexible curve can fit nearly every training point, including random noise, reducing the model's ability to generalize.

### Methods to Prevent Overfitting

Several techniques can reduce overfitting:

* Use a simpler model or lower polynomial degree.
* Apply cross-validation to evaluate model performance.
* Use regularization techniques such as Ridge or Lasso Regression.
* Increase the size and quality of the training dataset.

---

# Real-World Case Study

## Predicting House Prices Using Multiple Linear Regression

One common real-world application of regression is house price prediction. Real estate companies and online property platforms use Multiple Linear Regression to estimate the market value of homes.

### Goal

The objective is to predict house prices accurately to help buyers, sellers, and real estate agencies make informed decisions.

### Data Used

Typical features include:

* House size
* Number of bedrooms
* Number of bathrooms
* Property age
* Neighborhood
* Distance to schools and public transportation

### Type of Regression

Multiple Linear Regression is commonly applied because house prices depend on several independent variables.

### Key Results

The study demonstrated that using multiple property characteristics significantly improved prediction accuracy compared with relying on a single feature. The model helped estimate property values more consistently and supported pricing decisions in the real estate market.

---

# Conclusion

Regression is an essential machine learning technique for predicting continuous numerical values. Different regression methods are suitable for different types of problems. Linear Regression is simple and interpretable, Multiple Linear Regression incorporates several predictive features, and Polynomial Regression captures nonlinear relationships. Evaluating models with metrics such as MAE, MSE, RMSE, and R² helps determine prediction quality. Understanding underfitting and overfitting is also important for building reliable models that generalize well to new data.

# References

* Aurélien Géron. (2023). *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* (3rd ed.). O'Reilly Media.
* Christopher M. Bishop. (2006). *Pattern Recognition and Machine Learning*. Springer.
* Gareth James, Daniela Witten, Trevor Hastie, & Robert Tibshirani. (2021). *An Introduction to Statistical Learning* (2nd ed.). Springer.
* Ian Goodfellow, Yoshua Bengio, & Aaron Courville. (2016). *Deep Learning*. MIT Press.
