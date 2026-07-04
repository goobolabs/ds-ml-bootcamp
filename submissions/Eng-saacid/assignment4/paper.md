# Assignment Four – Regression Theory and Practice

##                                                Theory

# Regression in Machine Learning

## 1. Introduction to Regression

### What is Regression?

Regression is a supervised machine learning technique used to predict continuous numerical values based on one or more input features. The objective of regression is to identify the relationship between independent variables (features) and a dependent variable (target). Once the relationship is learned from historical data, the model can predict values for new data.

Regression is widely used because many real-world problems involve predicting numbers rather than categories. Examples include predicting house prices, vehicle prices, salaries, temperatures, and stock values.

### Difference Between Regression and Classification

Although both regression and classification are supervised learning methods, they solve different types of problems.

Regression predicts continuous numerical values, while classification predicts discrete categories or class labels. For example, a regression model may predict that a car costs $15,500, whereas a classification model may predict whether an email is spam or not spam.

| Regression                   | Classification                |
| ---------------------------- | ----------------------------- |
| Predicts numerical values    | Predicts categories or labels |
| Output is continuous         | Output is discrete            |
| Example: Predict house price | Example: Detect spam emails   |

### Real-Life Examples

**Regression Example**

A car dealership uses historical information such as mileage, engine size, fuel type, and manufacturing year to predict the selling price of used cars.

**Classification Example**

A bank predicts whether a customer will default on a loan by classifying them into either "Default" or "No Default."

---

# 2. Types of Regression

## Linear Regression

Linear Regression is the simplest regression algorithm. It assumes that there is a straight-line relationship between the input variables and the target variable. The model fits the best possible line through the data by minimizing prediction errors.

### Real-World Use

Predicting employee salary based on years of work experience.

### Advantages

* Simple and easy to understand.
* Fast to train.
* Easy to interpret.
* Performs well when relationships are approximately linear.

### Limitations

* Cannot model complex nonlinear relationships.
* Sensitive to outliers.
* Assumes linearity between variables.

---

## Multiple Linear Regression

Multiple Linear Regression extends Linear Regression by using two or more independent variables to predict a single target variable.

Instead of relying on one feature, it combines several predictors to improve accuracy.

### Real-World Use

Predicting house prices using features such as location, size, number of bedrooms, age, and distance from the city center.

### Advantages

* Uses multiple features simultaneously.
* Produces more accurate predictions than simple linear regression when relevant variables are included.
* Easy to interpret the influence of each feature.

### Limitations

* Can suffer from multicollinearity.
* Assumes a linear relationship.
* May become less effective when irrelevant variables are included.

---

## Polynomial Regression

Polynomial Regression is an extension of Linear Regression that models nonlinear relationships by adding polynomial terms of the input variables.

Instead of fitting a straight line, it fits a curved line that better captures complex patterns in the data.

### Real-World Use

Predicting crop production based on rainfall and fertilizer usage when the relationship is nonlinear.

### Advantages

* Models nonlinear relationships effectively.
* Can improve prediction accuracy for curved data patterns.

### Limitations

* Easily overfits when the polynomial degree is too high.
* More computationally expensive.
* Harder to interpret than linear models.

---

# 3. Regression Metrics

Regression models are evaluated using error metrics that measure how close predictions are to the actual values.

## Mean Absolute Error (MAE)

MAE is the average of the absolute differences between predicted values and actual values. It treats every error equally and is easy to understand.

Lower MAE values indicate better model performance.

---

## Mean Squared Error (MSE)

MSE calculates the average squared difference between predicted and actual values. Because errors are squared, large prediction errors receive much greater penalties.

Lower MSE values indicate better performance.

---

## Root Mean Squared Error (RMSE)

RMSE is the square root of MSE. It is measured in the same unit as the target variable, making it easier to interpret.

Like MSE, RMSE penalizes large prediction errors.

---

## Coefficient of Determination (R²)

R² measures how well the regression model explains the variation in the target variable.

Its values typically range from 0 to 1.

* R² = 1 means perfect prediction.
* R² = 0 means the model explains none of the variance.

Higher R² values indicate better model performance.

---

### Comparison of Regression Metrics

| Metric | Measures               | Unit           | Sensitive to Large Errors | Better Value |
| ------ | ---------------------- | -------------- | ------------------------- | ------------ |
| MAE    | Average absolute error | Same as target | No                        | Lower        |
| MSE    | Average squared error  | Squared unit   | Yes                       | Lower        |
| RMSE   | Square root of MSE     | Same as target | Yes                       | Lower        |
| R²     | Explained variance     | No unit        | No                        | Higher       |

---

# 4. Underfitting and Overfitting

## Underfitting

Underfitting occurs when a model is too simple to capture the relationship between input variables and the target. As a result, the model performs poorly on both training and testing data.

Common causes include:

* Using an overly simple model.
* Too few features.
* Insufficient training.

---

## Overfitting

Overfitting occurs when a model learns not only the true patterns in the training data but also random noise. Consequently, the model performs very well on training data but poorly on unseen testing data.

Polynomial Regression is especially vulnerable when the polynomial degree is too high, allowing the model to fit every small fluctuation in the training dataset.

### Methods to Prevent Overfitting

Several techniques can reduce overfitting:

* Use cross-validation to evaluate model performance.
* Reduce model complexity by selecting an appropriate polynomial degree.
* Increase the size of the training dataset.
* Remove unnecessary features.
* Apply regularization methods such as Ridge or Lasso Regression.

---

# 5. Real-World Case Study

## Car Price Prediction Using Regression

Regression is widely used in the automotive industry to estimate the market value of used vehicles.

### Goal

The objective is to predict the selling price of used cars so that buyers and sellers can make informed decisions.

### Data Used

The dataset typically includes:

* Manufacturing year
* Mileage
* Fuel type
* Transmission
* Engine size
* Brand
* Vehicle condition

### Regression Method

Multiple Linear Regression is commonly used because several vehicle characteristics influence price simultaneously.

### Results

Regression models help dealerships estimate fair market prices with reasonable accuracy. Important factors such as mileage, vehicle age, and engine capacity significantly affect the predicted price. These models improve pricing consistency and support better business decisions.

---

# Conclusion

Regression is one of the most important techniques in machine learning because it enables the prediction of continuous numerical values. Different regression methods are suitable for different types of problems. Linear Regression is simple and interpretable, Multiple Linear Regression incorporates several predictors, and Polynomial Regression models nonlinear relationships. Evaluating models using metrics such as MAE, MSE, RMSE, and R² helps determine prediction quality. Understanding underfitting and overfitting is also essential for building accurate and reliable machine learning models.

# References

Géron, A. (2023). Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow (3rd ed.). O'Reilly Media. https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/

James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). An Introduction to Statistical Learning (2nd ed.). Springer. https://link.springer.com/book/10.1007/978-1-0716-1418-1

Bishop, C. M. (2006). Pattern Recognition and Machine Learning. Springer. https://link.springer.com/book/10.1007/978-0-387-45528-0

Pedregosa, F., et al. (2011). Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, 12, 2825–2830. https://jmlr.org/papers/v12/pedregosa11a.html
