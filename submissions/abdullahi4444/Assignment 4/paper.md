# Assignment Four: Regression — Theory and Practice

## Part A — Theory

### Introduction to Regression

**1. What is regression in Machine Learning?**
Regression is a type of supervised learning algorithm used to predict a continuous numerical output. The goal of regression is to find the underlying relationship between the input features (independent variables) and the numeric target (dependent variable).

**2. How is it different from classification?**
Regression predicts a continuous quantity (e.g., predicting a price or a temperature), meaning the output is a number on a continuous scale. Classification, on the other hand, predicts a discrete category or class label (e.g., predicting whether an email is "Spam" or "Not Spam"). Regression answers "how much", while classification answers "which class".

**3. Real-life examples**
- **Regression:** Predicting the future price of a stock based on historical market data and economic indicators.
- **Classification:** Predicting whether a patient has a specific disease (Yes/No) based on their medical test results.

---

### Types of Regression

**1. Linear Regression**
- **How it works:** It models the relationship between a single input feature and a target variable by fitting the best straight line through the data points.
- **Real-world use case:** Estimating a car's fuel efficiency (MPG) based solely on its weight.
- **Advantages:** Very simple to implement, fast to train, and highly interpretable.
- **Limitations:** Only works well when the relationship is actually linear and relies on only one feature, which is rarely sufficient for complex real-world problems.

**2. Multiple Linear Regression**
- **How it works:** It extends linear regression by using multiple input features to predict a single target variable, fitting a multidimensional plane rather than a single line.
- **Real-world use case:** Predicting a house's price based on its size, number of bedrooms, age, and zip code.
- **Advantages:** More realistic than simple linear regression as it accounts for multiple factors simultaneously.
- **Limitations:** Still assumes a linear relationship between each feature and the target.

**3. Polynomial Regression**
- **How it works:** It captures non-linear relationships by adding polynomial terms (features raised to powers like squared or cubed) into a linear regression model, allowing the model to fit a curved line to the data.
- **Real-world use case:** Predicting the spread rate of a virus over time, which typically follows an exponential or curved trajectory rather than a straight line.
- **Advantages:** Can model complex, non-linear patterns where the effect of a feature changes over time or scale.
- **Limitations:** Highly susceptible to overfitting if the degree of the polynomial is set too high.

---

### Regression Metrics

| Metric | Meaning | Units | Sensitive to Big Errors? |
| --- | --- | --- | --- |
| **MAE (Mean Absolute Error)** | The average of the absolute differences between predicted and actual values. | Same as target data | No |
| **MSE (Mean Squared Error)** | The average of the squared differences between predicted and actual values. | Squared units of target | Yes |
| **RMSE (Root Mean Squared Error)**| The square root of the MSE, bringing the error back to original units. | Same as target data | Yes |
| **R² (Coefficient of Determination)**| The proportion of the variance in the target variable that is explained by the model. | 0 to 1 (unitless) | No |

---

### Underfitting and Overfitting

**1. Explain underfitting and overfitting:**
- **Underfitting:** Occurs when a model is too simple to capture the underlying pattern of the data. It performs poorly on both training and unseen testing data.
- **Overfitting:** Occurs when a model is too complex and learns the random noise in the training data rather than the actual signal. It performs exceptionally well on training data but poorly on unseen testing data.

**2. What causes overfitting, especially in polynomial regression?**
Overfitting in polynomial regression is typically caused by using an excessively high degree polynomial. When the degree is high, the model's curve bends sharply to pass exactly through every training data point (including outliers and noise), resulting in a wild, erratic curve that fails to generalize to new data.

**3. Methods to prevent overfitting:**
- **Use simpler models:** Reduce the complexity (e.g., lower the degree of the polynomial).
- **More training data:** Providing more diverse data helps the model generalize better.
- **Regularization:** Techniques like Ridge or Lasso regression penalize overly complex models by shrinking large coefficients.

---

### Real-World Case Study

**Goal:** Forecast the daily demand for ride-sharing services (like Uber or Lyft) in a major city.
**Data Used:** Historical ride requests, weather conditions (temperature, precipitation), time of day, day of the week, and occurrence of local events.
**Type of Regression Applied:** Multiple Linear Regression (and sometimes non-linear ensemble variations).
**Key Results:** The model revealed that time of day and specific weather conditions (like heavy rain) were the most significant predictors of ride demand. This allowed the company to dynamically allocate drivers to high-demand areas before the surge happened, improving customer satisfaction and driver earnings.
