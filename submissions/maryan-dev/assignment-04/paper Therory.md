# Part A — Theory: Regression in Machine Learning
## 1. Introduction to Regression
### 1.1 What is Regression in Machine Learning?

Regression is a category of supervised learning algorithms used to predict a **continuous numerical value** based on one or more input variables. In a regression problem, the model is trained on historical data where both the inputs (features) and the correct numerical output (label) are known. The algorithm learns the underlying relationship between the inputs and the output so that it can later predict the output for new, unseen inputs.

For example, a regression model could learn the relationship between a house's size, location, and age in order to predict its price — a number that can take on virtually any value within a range.

### 1.2 How is Regression Different from Classification?

Although both regression and classification are supervised learning tasks, they differ in the **type of output** they predict:

- **Regression** predicts a continuous, numeric quantity (e.g., 245,000 dollars, 36.7 degrees Celsius, 5.2 years).
- **Classification** predicts a discrete category or class label (e.g., "spam" vs. "not spam", "approved" vs. "rejected").

Because the output types differ, the two tasks also use different evaluation metrics. Regression models are typically evaluated using error-based metrics such as MAE, MSE, and RMSE, while classification models are evaluated using metrics such as accuracy, precision, recall, and F1-score.

### 1.3 Real-Life Examples

- **Regression example:** Predicting the price of a used car based on its mileage, age, brand, and engine size. The output (price) is a continuous number.
- **Classification example:** Determining whether an email is "spam" or "not spam" based on its content and sender. The output is one of two discrete categories.

---

## 2. Types of Regression

### 2.1 Linear Regression

**Basic idea:** Linear regression models the relationship between a single independent variable (X) and a dependent variable (Y) by fitting a straight line through the data points. The line is defined by the equation:

Y = b0 + b1·X

where *b0* is the intercept and *b1* is the slope, representing how much Y changes for a one-unit change in X. The algorithm finds the values of *b0* and *b1* that minimize the overall prediction error, usually using a method called Ordinary Least Squares.

**Real-world use case:** Predicting a student's final exam score based solely on the number of hours they studied.

**Advantages:**
- Simple to understand, implement, and interpret.
- Computationally inexpensive, even on large datasets.
- Coefficients clearly show the direction and strength of the relationship.

**Limitations:**
- Only models a relationship with one input variable.
- Assumes the relationship between X and Y is linear, which is often unrealistic.
- Sensitive to outliers, which can heavily distort the fitted line.

### 2.2 Multiple Linear Regression

**Basic idea:** Multiple linear regression extends simple linear regression by allowing more than one independent variable to predict the dependent variable:

Y = b0 + b1·X1 + b2·X2 + ... + bn·Xn

Each coefficient represents the effect of its corresponding variable on Y, holding all other variables constant. This allows the model to capture more complex, real-world situations where an outcome depends on several factors simultaneously.

**Real-world use case:** Predicting house prices based on multiple factors at once, such as square footage, number of bedrooms, location, and age of the property.

**Advantages:**
- Captures the combined effect of multiple factors, making predictions more realistic.
- Still relatively interpretable — each coefficient has a clear meaning.
- Often more accurate than simple linear regression for real-world data.

**Limitations:**
- Assumes a linear relationship between each input and the output.
- Performance can degrade if the input variables are highly correlated with each other (multicollinearity).
- Requires careful feature selection; irrelevant variables can reduce model quality.

### 2.3 Polynomial Regression

**Basic idea:** Polynomial regression is used when the relationship between the independent and dependent variables is curved rather than a straight line. It extends linear regression by adding powers of the independent variable as new terms:

Y = b0 + b1·X + b2·X² + b3·X³ + ... + bn·Xⁿ

Although the relationship between X and Y is nonlinear, the model is still considered a form of *linear* regression because it is linear in terms of the coefficients (b0, b1, b2, …).

**Real-world use case:** Modelling the growth rate of a population or the spread of a disease over time, where growth accelerates and then slows down in a curved pattern rather than a straight line.

**Advantages:**
- Can model curved, nonlinear relationships that simple or multiple linear regression cannot capture.
- More flexible and can fit complex patterns in the data.

**Limitations:**
- Choosing too high a polynomial degree leads to overfitting (see Section 4).
- Becomes difficult to interpret as the degree increases.
- More sensitive to outliers, especially near the edges of the data range.

### 2.4 Comparison Summary

| Aspect | Linear Regression | Multiple Linear Regression | Polynomial Regression |
|---|---|---|---|
| Number of inputs | One | Two or more | One or more, with powers |
| Shape of relationship | Straight line | Flat plane / hyperplane | Curve |
| Interpretability | Very high | High | Moderate to low |
| Risk of overfitting | Low | Moderate | High (especially at high degrees) |

---

## 3. Regression Metrics

Once a regression model makes predictions, its performance must be measured by comparing the predicted values to the actual values. The following four metrics are the most commonly used.

### 3.1 MAE (Mean Absolute Error)

MAE measures the average size of the errors, ignoring their direction (positive or negative). It is calculated by taking the absolute difference between each predicted value and the actual value, then averaging these differences across all data points. Because it does not square the errors, MAE treats all mistakes proportionally and is less influenced by a few very large errors.

### 3.2 MSE (Mean Squared Error)

MSE measures the average of the *squared* differences between predicted and actual values. Squaring the errors means that larger mistakes are penalized much more heavily than smaller ones. This makes MSE useful when large errors are particularly undesirable, but it also makes the metric harder to interpret directly since its units are squared (e.g., dollars², not dollars).

### 3.3 RMSE (Root Mean Squared Error)

RMSE is simply the square root of MSE. Taking the square root brings the value back into the same unit as the original target variable (e.g., dollars instead of dollars²), which makes it easier to interpret than MSE while still penalizing large errors more than MAE does.

### 3.4 R² (Coefficient of Determination)

R² measures the proportion of the variation in the dependent variable that the model is able to explain using the independent variable(s). It produces a value typically between 0 and 1 (it can occasionally be negative for a very poor model), where a value closer to 1 indicates that the model explains most of the variability in the data, and a value closer to 0 indicates that the model explains very little.

### 3.5 Comparison Table

| Metric | Unit | Sensitivity to Large Errors | What It Tells Us |
|---|---|---|---|
| MAE | Same as target variable | Low — treats all errors equally | Average magnitude of error, in plain terms |
| MSE | Squared units of target variable | High — squares amplify large errors | Penalizes big mistakes heavily; harder to interpret |
| RMSE | Same as target variable | High — same sensitivity as MSE, but readable units | Typical size of error, in original units |
| R² | Unitless (ratio/percentage) | Indirect — reflects how well variance is explained | Proportion of outcome variability explained by the model |

---

## 4. Underfitting and Overfitting

### 4.1 What Do They Mean?

**Underfitting** occurs when a regression model is too simple to capture the true pattern in the data. It performs poorly on both the training data and new data because it has not learned enough about the underlying relationship. For example, fitting a straight line to data that clearly follows a curve would result in underfitting.

**Overfitting** occurs when a model is too complex and learns not only the true underlying pattern but also the random noise and minor fluctuations specific to the training data. An overfit model performs very well on training data but performs poorly on new, unseen data because it has essentially "memorized" the training set rather than learning a generalizable pattern.

### 4.2 Causes of Overfitting in Polynomial Regression

Polynomial regression is especially prone to overfitting because increasing the polynomial degree gives the model more flexibility to bend and twist the fitted curve so that it passes very close to every single training point. The main causes include:

- **Choosing too high a polynomial degree**, which gives the model excessive flexibility relative to the amount of data available.
- **Having too little training data**, since a flexible curve can easily "thread the needle" through a small number of points.
- **Noisy data**, where the model fits the random fluctuations in the data rather than the true trend.

### 4.3 Methods to Prevent Overfitting

1. **Cross-validation:** Splitting the data into multiple training and validation folds helps detect overfitting early, since an overfit model will perform well on training folds but poorly on validation folds.
2. **Regularization (e.g., Ridge or Lasso regression):** Adding a penalty term to the model's cost function discourages excessively large coefficients, which keeps the fitted curve smoother and less reactive to noise.
3. **Reducing model complexity / choosing a lower polynomial degree:** Selecting the simplest model that still fits the underlying pattern reasonably well, often guided by validation performance, helps balance fit and generalization.

---

## 5. Real-World Case Study: Predicting Life Expectancy with Regression

### 5.1 Goal

A 2024 academic study set out to predict national **life expectancy** using machine learning, with the aim of supporting public health policy decisions. Rather than relying purely on traditional demographic life-table methods, the researchers wanted to see whether modern regression-based techniques could better capture the complex interplay of health, environmental, and socioeconomic factors that influence how long people live in a given country.

### 5.2 Data Used

The study used a real-world, multidimensional dataset compiled from the World Health Organization (WHO) and United Nations (UN), covering multiple countries and time periods. The dataset included variables such as vaccination coverage, geographic and demographic information, mortality indicators, and socioeconomic factors. Before modelling, the researchers carried out extensive preprocessing to handle missing values and inconsistencies in the raw data, which is a common and necessary step in real-world regression projects.

### 5.3 Type of Regression Applied

The researchers compared **three models**: Linear Regression, a Regression Decision Tree, and Random Forest. Linear Regression served as the interpretable baseline model — essentially a form of multiple linear regression, since life expectancy was predicted from several combined demographic and health variables at once, rather than from a single input.

### 5.4 Key Results and Insights

To evaluate the models fairly, the team measured performance using R², Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE) — the very same metrics discussed in Section 3 of this report. This is a good real-world illustration of why these metrics matter: they allowed the researchers to directly compare a simple, interpretable model (Linear Regression) against more complex, "black-box" models (Decision Tree and Random Forest) on equal footing.

The key insight from this kind of study is one of the central trade-offs in applied machine learning: simpler regression models like Linear Regression are easy to interpret — policymakers can directly see how, for instance, vaccination coverage relates to life expectancy — while more complex models may capture nonlinear patterns slightly better but are harder to explain to non-technical decision-makers. This trade-off between **interpretability and predictive accuracy** is exactly why organizations such as the WHO and national health ministries often still rely on regression-based models for policy work, even when more complex alternatives exist: the ability to explain *why* a prediction was made can be just as important as the prediction itself.

### 5.5 Why This Example Is Relevant

This case study is a particularly fitting real-life example because it touches on nearly every theoretical concept covered in this report: it uses multiple linear regression on real socioeconomic and health data, it relies on the exact metrics (R², MAE, RMSE) explained above, and it highlights the practical importance of model interpretability — a consideration that becomes especially relevant when discussing the complexity trade-offs of polynomial regression versus simpler linear approaches.

---

## References

- Dolgopolyi, R., Amaslidou, I., & Margaritou, A. (2024). *Interpretable Machine Learning for Life Expectancy Prediction: A Comparative Study of Linear Regression, Decision Tree, and Random Forest.* Retrieved from arXiv.
- World Health Organization (WHO) and United Nations (UN) open health and demographic datasets, as used in the above study.