# Regression in Machine Learning

## Introduction

Regression is one of the most important supervised learning techniques in Machine Learning. It is used to predict continuous numerical values based on the relationship between input variables (features) and an output variable (target). Regression models help researchers, businesses, and organizations make accurate predictions from historical data. Common applications include predicting house prices, sales revenue, medical costs, and weather conditions.

Understanding regression is essential because it provides valuable insights into how different variables influence an outcome. This report explains the concept of regression, its main types, evaluation metrics, common challenges such as overfitting and underfitting, and a real-world application.

---

# 1. Introduction to Regression

## What is Regression in Machine Learning?

Regression is a supervised Machine Learning algorithm used to predict continuous numerical values. During training, the model learns the relationship between independent variables (features) and a dependent variable (target). Once trained, it can estimate future numerical outcomes for new data.

For example, a regression model can predict a student's final score, the selling price of a house, or tomorrow's temperature.

## Difference Between Regression and Classification

Although both regression and classification are supervised learning methods, they solve different types of problems.

* **Regression** predicts continuous numerical values.
* **Classification** predicts discrete categories or labels.

For example:

* **Regression Example:** Predicting the monthly electricity bill based on electricity usage.
* **Classification Example:** Predicting whether an email is **Spam** or **Not Spam**.

---

# 2. Types of Regression

## 2.1 Linear Regression

### Basic Idea

Linear Regression assumes there is a straight-line relationship between the independent variable and the dependent variable. The model fits the best possible line that minimizes prediction errors.

Equation:

**Y = a + bX**

where:

* Y = predicted value
* X = input variable
* a = intercept
* b = slope

### Real-World Use Case

Predicting house prices based on the size of the house.

### Advantages

* Easy to understand and implement.
* Fast training process.
* Highly interpretable.
* Works well when relationships are approximately linear.

### Limitations

* Cannot model complex nonlinear relationships.
* Sensitive to outliers.
* Performance decreases when assumptions are violated.

---

## 2.2 Multiple Linear Regression

### Basic Idea

Multiple Linear Regression extends Linear Regression by using two or more independent variables to predict one target variable.

Equation:

**Y = a + b₁X₁ + b₂X₂ + ... + bₙXₙ**

### Real-World Use Case

Predicting employee salary using:

* Education level
* Years of experience
* Age
* Job position

### Advantages

* Uses several variables to improve prediction accuracy.
* Captures more realistic relationships.
* Useful for business and economic forecasting.

### Limitations

* Sensitive to multicollinearity among variables.
* Requires larger datasets.
* Interpretation becomes more difficult as variables increase.

---

## 2.3 Polynomial Regression

### Basic Idea

Polynomial Regression models nonlinear relationships by adding polynomial terms such as X², X³, and higher powers.

Instead of fitting a straight line, it fits a curve that better represents complex patterns.

### Real-World Use Case

Predicting crop yield based on rainfall and temperature when the relationship is curved rather than linear.

### Advantages

* Models nonlinear relationships effectively.
* Higher prediction accuracy for curved data.
* More flexible than Linear Regression.

### Limitations

* Can easily overfit training data.
* Selecting the correct polynomial degree is challenging.
* More computationally expensive than Linear Regression.

---

# 3. Regression Metrics

Regression models are evaluated using several performance metrics.

## Mean Absolute Error (MAE)

MAE measures the average absolute difference between predicted values and actual values.

Lower MAE indicates better prediction accuracy.

## Mean Squared Error (MSE)

MSE measures the average squared difference between predictions and actual values.

Because errors are squared, large mistakes receive greater penalties.

## Root Mean Squared Error (RMSE)

RMSE is the square root of MSE.

It is easier to interpret because it has the same unit as the target variable.

## R² (Coefficient of Determination)

R² measures how well the regression model explains the variation in the data.

* R² = 1 means perfect prediction.
* R² = 0 means the model explains none of the variation.

---

## Comparison of Regression Metrics

| Metric | Measures                         Unit                                Sensitive to Large Errors Interpretation                                    

 MAE     Average absolute error           Same as target  Low                        Lower values indicate better accuracy             
 MSE     Average squared error            Squared units   Very High                  Penalizes large prediction errors                 
 RMSE    Square root of MSE               Same as target  High                       Indicates average prediction error magnitude      
| R²      Variance explained by the model  No unit         Not directly               Higher values (closer to 1) indicate a better fit 



# 4. Underfitting and Overfitting

## Underfitting

Underfitting occurs when a model is too simple to capture the underlying relationship in the data.

Characteristics:

 High training error
 High testing error
 Poor prediction performance

Example:
Using a simple straight line to model highly curved data.


## Overfitting

Overfitting occurs when a model learns both the real patterns and the random noise in the training data.

Characteristics:

 Very low training error
 High testing error
*Poor performance on new data

### Causes of Overfitting (Especially in Polynomial Regression)

 Using a polynomial degree that is too high.
 Small training datasets.
 Too many unnecessary features.
 Noise in the dataset.

### Methods to Prevent Overfitting

1. Use a simpler model with a lower polynomial degree.
2. Apply regularization techniques such as Ridge Regression or Lasso Regression.
3. Increase the amount of training data or use cross-validation to improve generalization.

---

# 5. Real-World Case Study

## Healthcare: Predicting Medical Insurance Charges

### Goal

Researchers developed a Multiple Linear Regression model to predict individual medical insurance costs. Accurate predictions help insurance companies estimate healthcare expenses and set fair insurance premiums.

### Data Used

The dataset included:

 Age
 Body Mass Index (BMI)
 Smoking status
 Number of children
Gender
 Geographic region

### Type of Regression

Multiple Linear Regression

### Key Results

The study found that smoking status and age were among the strongest predictors of insurance charges. Individuals who smoked generally had much higher predicted medical costs than non-smokers. The model also showed that BMI contributed to increased healthcare expenses. These findings help insurance providers improve pricing strategies and assist policymakers in understanding factors associated with healthcare costs.

---

# Conclusion

Regression is a powerful Machine Learning technique used to predict continuous numerical values. Unlike classification, which predicts categories, regression estimates quantities such as prices, costs, and temperatures. Linear Regression works well for simple linear relationships, Multiple Linear Regression handles multiple influencing variables, and Polynomial Regression models nonlinear patterns. Model performance is commonly evaluated using MAE, MSE, RMSE, and R². Understanding underfitting and overfitting is essential for building accurate and reliable models. Regression continues to play an important role in business, healthcare, education, transportation, and many other industries by supporting data-driven decision-making.

# References

1. Aurélien Géron. *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow*. O'Reilly Media, 3rd Edition, 2022.

2. Gareth James, Daniela Witten, Trevor Hastie, and Robert Tibshirani. *An Introduction to Statistical Learning*. Springer, 2nd Edition, 2021.

3. Ian Goodfellow, Yoshua Bengio, and Aaron Courville. *Deep Learning*. MIT Press, 2016.

4. Scikit-learn Developers. *Scikit-learn User Guide: Linear Models and Regression*. https://scikit-learn.org/stable/user_guide.html
