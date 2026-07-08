# Regression — Theory and Practice

**Assignment Four, Part A: Theory**

---

## 1. Introduction to Regression

Regression is a category of supervised machine learning in which a model learns to predict a **continuous numerical value** from one or more input features. Given a training set of examples where the correct output is already known, a regression algorithm learns the relationship between the inputs (independent variables) and the output (dependent variable), so that it can estimate the output for new, unseen inputs. Common examples include predicting house prices, forecasting sales, or estimating a person's age from a photograph.

Regression differs from **classification** in the nature of the output it predicts. Regression outputs a continuous quantity — a number that can take any value within a range (e.g., $18,500 or $21,340.75) — whereas classification outputs a **discrete category or label** (e.g., "spam" or "not spam", "cat" or "dog"). The choice between the two depends entirely on the type of question being asked: "how much" or "how many" points toward regression, while "which category" points toward classification. The two also tend to use different evaluation metrics — regression uses error-based metrics such as MAE and RMSE, while classification uses metrics such as accuracy, precision, and recall.

- **Regression example:** Predicting the resale price of a used car based on its mileage, age, brand, and condition.
- **Classification example:** Predicting whether a bank loan applicant will default or not default on a loan.

---

## 2. Types of Regression

### 2.1 Linear Regression

Linear regression models the relationship between a single input feature and the output as a straight line: `y = w·x + b`. The algorithm learns the weight `w` and bias `b` that minimize the difference between predicted and actual values, typically using an approach called least squares, which minimizes the sum of squared errors between predictions and true values.

- **Use case:** Predicting a student's exam score based on the number of hours studied.
- **Advantages:** Simple to implement, fast to train, and highly interpretable — the weight tells you exactly how much the output changes per unit change in the input.
- **Limitations:** Only captures a straight-line relationship, so it performs poorly when the true relationship between input and output is curved or complex. It is also sensitive to outliers.

### 2.2 Multiple Linear Regression

Multiple linear regression extends simple linear regression to more than one input feature: `y = w1·x1 + w2·x2 + ... + wn·xn + b`. Each feature gets its own weight, and the model learns how all the features jointly contribute to the output.

- **Use case:** Predicting a house's sale price based on square footage, number of bedrooms, location, and age of the building simultaneously.
- **Advantages:** Captures the combined effect of several factors at once, giving a more realistic and often more accurate model than single-variable regression. Still relatively interpretable, since each coefficient shows the contribution of its feature.
- **Limitations:** Assumes the relationship between each feature and the output is still linear. Performance can degrade when features are highly correlated with each other (multicollinearity), which makes the individual weights unstable and harder to interpret.

### 2.3 Polynomial Regression

Polynomial regression fits a curved line to the data by adding higher-degree terms of the input feature(s), such as `y = w1·x + w2·x² + w3·x³ + ... + b`. Although the relationship between x and y is now curved, the model is still considered "linear" in terms of the weights, so it can be fit using the same underlying techniques as linear regression.

- **Use case:** Modeling the growth rate of a population or the trajectory of a projectile, where the relationship clearly bends rather than following a straight line.
- **Advantages:** Can fit non-linear patterns that plain linear regression cannot, often producing a much better fit to curved data.
- **Limitations:** Choosing a high polynomial degree makes the model extremely flexible, which can cause it to fit the noise in the training data rather than the underlying trend — a problem known as overfitting (discussed further in Section 4). Polynomial regression is also more sensitive to outliers and can behave unpredictably outside the range of the training data.

---

## 3. Regression Metrics

Once a regression model has been trained, its quality is evaluated by measuring how far its predictions are from the actual values.

- **MAE (Mean Absolute Error):** The average of the absolute differences between predicted and actual values. It treats all errors equally regardless of size, so a $500 error contributes exactly $500 to the average, whether it is one of many small errors or a rare large one.
- **MSE (Mean Squared Error):** The average of the *squared* differences between predicted and actual values. Squaring the errors means large errors are penalized much more heavily than small ones, making MSE very sensitive to outliers.
- **RMSE (Root Mean Squared Error):** The square root of MSE. Taking the square root brings the metric back into the same units as the original target (e.g., dollars instead of dollars-squared), which makes it easier to interpret than raw MSE while still penalizing large errors more than MAE does.
- **R² (Coefficient of Determination):** A measure of how much of the variation in the target variable is explained by the model, expressed as a value typically between 0 and 1 (it can be negative for a very poor model). An R² of 0.90 means the model explains 90% of the variability in the data; it does not describe error size directly, but rather the model's overall explanatory power.

**Comparison Table**

| Metric | Units | Sensitivity to Large Errors | What It Tells You |
|--------|-------|------------------------------|--------------------|
| MAE | Same as target variable | Low — treats all errors equally | Average magnitude of typical prediction error |
| MSE | Squared units of target | High — squaring amplifies large errors | Penalizes big mistakes heavily; harder to interpret directly |
| RMSE | Same as target variable | High — inherits MSE's sensitivity, but in interpretable units | "Typical" error size, weighted toward large mistakes |
| R² | Unitless (proportion, 0–1) | Indirect — reflects overall fit, not individual errors | How well the model explains the variance in the data |

---

## 4. Underfitting and Overfitting

**Underfitting** occurs when a model is too simple to capture the true pattern in the data. An underfit model performs poorly on both the training data and new/unseen data, because it hasn't learned enough about the underlying relationship — for example, using plain linear regression to model data that is clearly curved.

**Overfitting** occurs when a model is too complex relative to the amount or noise level of the training data. An overfit model performs very well on the training data — sometimes almost perfectly — but performs poorly on new, unseen data because it has essentially memorized the noise and quirks of the training set rather than the true underlying trend.

In polynomial regression specifically, overfitting is caused by choosing a **degree that is too high** for the available data. A high-degree polynomial has enough flexibility to bend and twist itself to pass through nearly every training point, including the random noise in those points, which produces a curve that looks excellent on the training set but generalizes badly.

**Methods to prevent overfitting:**

1. **Cross-validation** — Evaluate the model on multiple different train/validation splits rather than a single split, to get a more reliable estimate of how well it generalizes and to detect overfitting early.
2. **Regularization** (e.g., Ridge or Lasso regression) — Add a penalty term to the loss function that discourages excessively large weights, keeping the model simpler and less prone to fitting noise.
3. **Simplify the model / reduce polynomial degree, or gather more training data** — Lowering model complexity (e.g., choosing a lower polynomial degree) or increasing the size and diversity of the training set both reduce the model's tendency to memorize noise.

---

## 5. Real-World Case Study

A widely cited application of regression in transportation and urban planning is the use of multiple linear regression models by ride-hailing and logistics companies to predict trip fares and estimated arrival times. For example, ride-hailing platforms use regression models that take inputs such as distance, expected trip duration, time of day, and current demand levels to estimate a price or arrival time before a customer confirms a ride.

- **Goal:** Estimate a fair, competitive trip price or arrival time in real time so that customers can see a reliable estimate before booking.
- **Data used:** Historical trip records including pickup/drop-off locations, distance traveled, time of day, day of week, traffic conditions, and actual fares or durations from past trips.
- **Type of regression applied:** Multiple linear regression (and in more advanced deployments, ensemble regression models such as gradient boosting or random forests) trained on these historical features.
- **Key results/insights:** Regression-based estimation allows the platform to give near-real-time price and time predictions that adjust automatically as conditions such as traffic or demand change, and the accuracy of these models directly affects customer trust and the company's ability to balance supply and demand ("surge pricing") efficiently. This illustrates how even relatively simple regression techniques, when combined with rich real-world data, can power large-scale operational decision-making.

---

## References

- James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning*. Springer.
- Géron, A. (2019). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*. O'Reilly Media.
- Scikit-learn Developers. *Linear Models and Ensemble Methods Documentation*. https://scikit-learn.org/stable/
