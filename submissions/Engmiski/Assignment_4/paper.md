# Assignment Four – Part A: Regression Theory

## 1. Introduction to Regression

Regression is a supervised machine learning technique used to predict continuous numerical values based on one or more input variables. The main objective of regression is to learn the relationship between independent variables (features) and a dependent variable (target). Once the model is trained, it can estimate future or unknown values from new data. Regression is widely used in many fields, including finance, healthcare, transportation, agriculture, and business.

Regression differs from classification because regression predicts numerical values, while classification predicts categories or labels. For example, regression can estimate the price of a used car, whereas classification can determine whether an email is spam or not spam. Although both are supervised learning techniques, they solve different types of prediction problems.

A real-life example of regression is predicting house prices based on the size, location, and number of bedrooms. A real-life example of classification is predicting whether a bank customer will default on a loan (Yes or No).

---

## 2. Types of Regression

### Linear Regression

Linear Regression is the simplest regression algorithm. It assumes that there is a straight-line relationship between the input variables and the target variable. The model fits the best possible line that minimizes prediction errors.

**Real-world use case:** Predicting house prices based on house size.

**Advantages**

* Easy to understand and interpret.
* Fast to train.
* Works well for linear relationships.

**Limitations**

* Cannot model complex relationships.
* Sensitive to outliers.
* Performance decreases when data is not linear.

### Multiple Linear Regression

Multiple Linear Regression extends Linear Regression by using two or more independent variables to predict one target variable. Instead of using only one feature, it combines several features to improve prediction accuracy.

**Real-world use case:** Predicting car prices using mileage, year, number of doors, accident history, and location.

**Advantages**

* Uses multiple factors for prediction.
* Often produces more accurate results than simple linear regression.
* Easy to interpret.

**Limitations**

* Requires careful feature selection.
* Can suffer from multicollinearity.
* Assumes a linear relationship.

### Polynomial Regression

Polynomial Regression is an extension of Linear Regression that models non-linear relationships by adding polynomial terms to the features. It creates a curved line instead of a straight line, allowing it to fit more complex patterns.

**Real-world use case:** Predicting population growth or product demand over time.

**Advantages**

* Captures non-linear relationships.
* More flexible than linear regression.
* Can improve prediction accuracy for curved data.

**Limitations**

* Can easily overfit the training data.
* More difficult to interpret.
* Choosing the correct polynomial degree is important.

---

## 3. Regression Metrics

Regression models are evaluated using performance metrics that measure prediction accuracy.

### Mean Absolute Error (MAE)

MAE is the average absolute difference between the predicted values and the actual values. Lower MAE indicates better performance because predictions are closer to the true values.

### Mean Squared Error (MSE)

MSE calculates the average squared difference between predictions and actual values. Squaring gives more weight to large errors, making MSE sensitive to outliers.

### Root Mean Squared Error (RMSE)

RMSE is the square root of MSE. It has the same unit as the target variable, making it easier to interpret while still penalizing large prediction errors.

### R² (Coefficient of Determination)

R² measures how well the regression model explains the variation in the target variable. An R² value closer to 1 indicates better model performance, while a value closer to 0 indicates poor performance.

### Comparison of Regression Metrics

| Metric | Unit           | Sensitive to Large Errors | Meaning                                       |
| ------ | -------------- | ------------------------- | --------------------------------------------- |
| MAE    | Same as target | Low                       | Average prediction error                      |
| MSE    | Squared unit   | High                      | Average squared error                         |
| RMSE   | Same as target | High                      | Square root of MSE, easier to interpret       |
| R²     | No unit        | No                        | Percentage of variance explained by the model |

---

## 4. Underfitting and Overfitting

Underfitting occurs when a regression model is too simple to learn the relationship in the data. As a result, it performs poorly on both training and testing datasets.

Overfitting occurs when a model learns not only the true relationship but also the noise in the training data. Such models achieve excellent training performance but poor testing performance because they cannot generalize to new data.

Polynomial Regression is especially prone to overfitting when a very high polynomial degree is selected. The model becomes too complex and fits every small fluctuation in the training data.

Methods to prevent overfitting include:

* Using simpler models.
* Applying cross-validation.
* Reducing unnecessary features.
* Collecting more training data.
* Applying regularization techniques.

---

## 5. Real-World Case Study

A common real-world application of regression is car price prediction in the automotive industry. Companies and online marketplaces use historical vehicle data to estimate the market value of used cars.

The goal is to predict the selling price of a car using features such as manufacturing year, mileage, accident history, number of doors, and location. A Multiple Linear Regression model can be used because several independent variables influence the final price.

The results of these models help buyers determine fair prices, assist sellers in pricing vehicles competitively, and enable dealerships to automate price estimation. Accurate regression models improve pricing decisions and reduce uncertainty in the used-car market.

---

## References

* Aurélien Géron. *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow*. O'Reilly Media.
* Gareth James, Daniela Witten, Trevor Hastie, and Robert Tibshirani. *An Introduction to Statistical Learning*. Springer.
* Ian Goodfellow, Yoshua Bengio, and Aaron Courville. *Deep Learning*. MIT Press.
