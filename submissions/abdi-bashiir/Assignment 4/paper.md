# Regression in Machine Learning

**Assignment Four – Part A (Theory)**

## 1. Introduction to Regression

### What is Regression in Machine Learning?

Regression is a supervised machine learning technique used to predict continuous numerical values. Instead of predicting categories, regression predicts numbers on a continuous scale. The main objective of regression is to learn the relationship between the input features (X) and the target variable (y). Once this relationship is learned, the model can predict values for new, unseen data.

Regression is widely used in many real-world applications where numerical prediction is required. Examples include predicting house prices, estimating sales revenue, forecasting stock prices, and predicting weather temperatures.

### Difference Between Regression and Classification

Although both regression and classification are supervised learning methods, they solve different types of problems.

Regression predicts numerical values, while classification predicts categories or classes.

For example:

* Predicting the selling price of a car is a regression problem because the output is a number.
* Predicting whether an email is spam or not spam is a classification problem because the output belongs to one of two categories.

In simple terms, regression answers the question **"How much?"**, whereas classification answers the question **"Which class?"**

### Real-Life Examples

**Regression Example**

A real estate company predicts the selling price of houses based on features such as house size, number of bedrooms, location, and year built.

**Classification Example**

An email service predicts whether a received email is spam or not spam.

---

# 2. Types of Regression

Regression models can be designed in different ways depending on the relationship between the input features and the target value.

## Linear Regression

Linear Regression is the simplest regression model. It predicts a continuous value by finding a straight-line relationship between one input feature and one output variable.

For example, a house with a larger size generally has a higher selling price. Linear Regression learns this trend and draws the best-fitting straight line through the data.

### Real-World Use Case

Predicting house prices using only the size of the house.

### Advantages

* Easy to understand and implement.
* Fast to train.
* Provides a clear relationship between variables.
* Works well when the relationship is approximately linear.

### Limitations

* Uses only one main feature.
* Assumes the relationship is a straight line.
* Cannot accurately model complex real-world relationships.

---

## Multiple Linear Regression

Multiple Linear Regression extends Linear Regression by using several input features instead of only one. Since many real-world problems depend on multiple factors, this model usually provides more accurate predictions.

For example, predicting house prices may require information about house size, number of bedrooms, location, and year built. The model combines all these features to estimate the final price.

### Real-World Use Case

Predicting house prices using size, bedrooms, location, and construction year.

### Advantages

* Produces more realistic predictions.
* Considers several important factors simultaneously.
* Usually performs better than simple Linear Regression.

### Limitations

* Requires more data.
* Can become difficult to interpret when many features are included.
* Performance decreases if irrelevant features are added.

---

## Polynomial Regression

Not all relationships follow a straight line. Polynomial Regression extends Linear Regression by creating additional features such as x², x³, and higher powers. These additional features allow the model to fit curved relationships instead of straight lines.

For example, increasing the size of a house from 1,000 to 1,500 square feet may increase its price significantly, while increasing the size from 2,800 to 3,300 square feet may produce a much smaller increase. Polynomial Regression captures this changing relationship more effectively than Linear Regression.

### Real-World Use Case

Predicting house prices when the relationship between house size and price is not perfectly linear.

### Advantages

* Models non-linear relationships.
* Produces better predictions when the data follows a curved pattern.
* More flexible than Linear Regression.

### Limitations

* More likely to overfit if the polynomial degree becomes too high.
* More complex than Linear Regression.
* Choosing the correct polynomial degree can be difficult.

---

# Comparison of Regression Types

| Feature            | Linear Regression    | Multiple Linear Regression   | Polynomial Regression                |
| ------------------ | -------------------- | ---------------------------- | ------------------------------------ |
| Number of Features | One                  | Multiple                     | One or more with polynomial features |
| Relationship       | Straight line        | Linear with multiple inputs  | Curved                               |
| Complexity         | Low                  | Medium                       | Higher                               |
| Best Used For      | Simple relationships | Multiple influencing factors | Non-linear relationships             |

---

# 3. Regression Metrics

Regression models are evaluated by comparing predicted values with actual values. Several evaluation metrics are commonly used.

## Mean Absolute Error (MAE)

Mean Absolute Error measures the average absolute difference between predicted values and actual values.

A lower MAE indicates that the model's predictions are closer to the true values.

---

## Mean Squared Error (MSE)

Mean Squared Error calculates the average squared difference between predicted values and actual values.

Because the errors are squared, larger prediction errors receive much heavier penalties than smaller ones.

---

## Root Mean Squared Error (RMSE)

Root Mean Squared Error is the square root of the Mean Squared Error.

Unlike MSE, RMSE is expressed in the same units as the original target variable, making it easier to interpret. RMSE is also sensitive to large prediction errors.

---

## R² (Coefficient of Determination)

R² measures how much of the variation in the target variable is explained by the regression model.

* R² = 1.0 indicates a perfect model.
* R² = 0 indicates that the model performs no better than predicting the average.
* A negative R² indicates that the model performs worse than simply predicting the average.

A higher R² generally indicates better model performance.

### Comparison of Regression Metrics

| Metric | What It Measures                  | Units          | Sensitive to Large Errors |
| ------ | --------------------------------- | -------------- | ------------------------- |
| MAE    | Average absolute prediction error | Same as target | No                        |
| MSE    | Average squared prediction error  | Squared units  | Yes                       |
| RMSE   | Square root of MSE                | Same as target | Yes                       |
| R²     | Percentage of variation explained | No units (0–1) | No                        |

# 4. Underfitting and Overfitting

## Underfitting

Underfitting occurs when a regression model is too simple to learn the relationship between the input features and the target variable. As a result, the model performs poorly on both the training data and new unseen data because it cannot capture the important patterns in the dataset.

For example, using a simple Linear Regression model to predict a complex non-linear relationship may result in underfitting because a straight line cannot represent the true pattern of the data.

### Causes of Underfitting

* Using a model that is too simple.
* Using too few relevant features.
* Insufficient training of the model.

---

## Overfitting

Overfitting occurs when a model learns the training data too well, including its noise and random variations. Although the model performs very well on the training data, it usually performs poorly on new unseen data because it has memorized the training examples instead of learning the general relationship.

Polynomial Regression can easily overfit when the polynomial degree is too high. A highly complex curve may pass through almost every training point, but it may fail to make accurate predictions on new data.

### Causes of Overfitting

* Using a polynomial degree that is too high.
* Training a very complex model on a small dataset.
* Including unnecessary or noisy features.

### Methods to Prevent Overfitting

Several techniques can reduce overfitting:

1. Use a simpler model whenever possible.
2. Increase the amount of training data.
3. Select only the most relevant features and remove unnecessary ones.

These techniques help the model learn the general patterns in the data rather than memorizing the training examples.

---

# 5. Real-World Case Study

## House Price Prediction Using Multiple Linear Regression

A common real-world application of regression is house price prediction. Real estate companies and researchers use Multiple Linear Regression to estimate house prices based on several property characteristics.

### Goal

The objective is to predict the selling price of a house before it is placed on the market. Accurate predictions help buyers, sellers, and real estate agencies make better financial decisions.

### Data Used

The dataset typically includes several features, such as:

* House size (square feet)
* Number of bedrooms
* Number of bathrooms
* House location
* Year built

The target variable is the selling price of the house.

### Type of Regression

Multiple Linear Regression is commonly used because house prices depend on several different factors rather than a single feature.

### Results and Insights

The regression model learns the relationship between the property features and the selling price. After training, the model can estimate the price of new houses that were not included in the training dataset.

The study demonstrates that using multiple features generally produces more accurate predictions than using only one feature. It also shows that important factors such as house size and location have a significant influence on the final price.

---

# References

1. Aurélien Géron. *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow*. O'Reilly Media.

2. Gareth James, Daniela Witten, Trevor Hastie, and Robert Tibshirani. *An Introduction to Statistical Learning*. Springer.

3. Scikit-learn Developers. *Scikit-learn User Guide – Supervised Learning and Regression*. https://scikit-learn.org/
