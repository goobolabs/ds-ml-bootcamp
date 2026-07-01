# Assignment Four — Part A: Regression Theory

**Author:** Ali Omar Abdi
**Course:** DS-ML Bootcamp
**Due:** Tuesday, June 30, 2026 — 12:00 PM (Africa/Mogadishu / EAT)

---

## Table of Contents

1. [Introduction to Regression](#1-introduction-to-regression)
2. [Types of Regression](#2-types-of-regression)
3. [Regression Metrics](#3-regression-metrics)
4. [Underfitting and Overfitting](#4-underfitting-and-overfitting)
5. [Real-World Case Study](#5-real-world-case-study)
6. [References](#references)

---

## 1. Introduction to Regression

### What Is Regression?

Regression is a type of supervised machine learning used to predict a continuous numeric output. The model learns from labeled training data — pairs of input features (X) and known numeric outputs (y) — and builds a mathematical function that maps inputs to outputs. After training, it can estimate the output for inputs it has never seen.

The word "regression" comes from statistics. Francis Galton used it in 1886 to describe how children's heights tended to "regress" toward the population average rather than extremes (Galton, 1886). Modern ML regression extends that idea to any problem where the goal is to predict a quantity on a continuous scale.

Common examples include predicting house prices from size and location, estimating tomorrow's temperature from today's weather readings, and forecasting next month's sales from historical data.

### How Is Regression Different from Classification?

Both regression and classification are supervised learning tasks. The difference comes down to what the model predicts.

- **Regression** predicts a number on a continuous scale. The output can take any value in a range — for example, $342,000 or $341,999.
- **Classification** predicts a category from a fixed set of options — for example, "spam" or "not spam," "pass" or "fail."

| | Regression | Classification |
|---|---|---|
| Output type | Continuous number | Discrete category |
| Example output | $342,000 | "Spam" |
| Evaluation metric | MAE, RMSE, R² | Accuracy, F1-score |
| Algorithm example | Linear Regression | Logistic Regression, SVM |

A useful rule of thumb: if you can meaningfully ask "how much?" or "how many?", the problem is regression. If you ask "which category?", it is classification.

### Real-Life Examples

**Regression:** Estimating the selling price of a used car given its age, mileage, brand, and condition. The prediction is a specific dollar amount anywhere on a continuous scale.

**Classification:** Deciding whether a bank transaction is fraudulent or legitimate. The prediction is one of two fixed categories: fraud or not fraud.

---

## 2. Types of Regression

### Linear Regression

Linear Regression fits a straight line through a dataset to describe the relationship between one input feature and a numeric target. It assumes the relationship is linear — that a fixed increase in the input produces a fixed increase in the output, regardless of where on the scale you are.

**How it works:** The algorithm finds the line y = mx + b that minimizes the total squared distance between the line and all data points. This process is called Ordinary Least Squares (OLS).

**Real-world use case:** Predicting fuel consumption from engine size. A larger engine generally uses more fuel in a roughly proportional way.

**Advantages:**
- Fast to train and simple to interpret
- Coefficients directly show the size of each feature's effect
- Works well when the true relationship is close to linear

**Limitations:**
- Assumes a perfectly straight relationship, which many real problems do not have
- One input only — most real problems depend on multiple factors
- Sensitive to outliers, which can pull the line in the wrong direction

### Multiple Linear Regression

Multiple Linear Regression extends linear regression to handle several input features at once. Instead of fitting a line through a 2D scatter plot, it fits a plane (or a hyperplane in higher dimensions) through a multi-dimensional space.

**How it works:** The model learns a weight for each feature: y = b0 + b1x1 + b2x2 + ... + bnxn. Each weight tells the model how much a one-unit increase in that feature affects the target, holding all other features constant.

**Real-world use case:** Predicting a house price using size, number of bedrooms, location, and year built together. No single feature tells the full story; the combination is more informative than any one of them.

**Advantages:**
- More realistic than simple linear regression for most problems
- Still interpretable — each coefficient has a clear meaning
- Computationally cheap, even with many features

**Limitations:**
- Still assumes linear relationships between each feature and the target
- Sensitive to multicollinearity (when input features are correlated with each other)
- Performs poorly when the true relationship has bends or curves

### Polynomial Regression

Polynomial Regression fits a curve rather than a straight line by adding powers of a feature (x², x³) as new input columns. Despite the curve in the output, it is still mathematically a linear model — linear in its coefficients, not in the original feature.

**How it works:** A degree-2 polynomial adds x² as a new feature: y = b0 + b1x + b2x². The extra term lets the line bend once. A degree-3 polynomial can bend twice, and so on.

**Real-world use case:** Modelling the relationship between advertising spend and revenue. Returns often increase quickly at first, then level off as saturation sets in — a curved relationship that a straight line cannot capture.

**Advantages:**
- Can model non-linear patterns with relatively simple mathematics
- Interpretable at low degrees (quadratic, cubic)
- Still uses the same OLS fitting procedure as linear regression

**Limitations:**
- High-degree polynomials overfit badly — the curve chases noise instead of the true pattern
- Extrapolation outside the training data range is unreliable
- Feature space grows quickly, which can cause numerical instability

### Comparison Table

| Feature | Linear Regression | Multiple Linear Regression | Polynomial Regression |
|---|---|---|---|
| Number of inputs | 1 | 2 or more | 1 or more |
| Shape of fit | Straight line | Flat plane / hyperplane | Curve |
| Handles non-linearity | No | No | Yes |
| Risk of overfitting | Low | Low-moderate | High at high degrees |
| Best use case | One-factor linear relationships | Multi-factor linear problems | Curved, non-linear patterns |

---

## 3. Regression Metrics

After training a model, we need to measure how close its predictions are to the actual values. Four metrics are widely used for regression.

### Mean Absolute Error (MAE)

MAE calculates the average size of the prediction errors without caring about direction. Each error is taken as an absolute value (so negative and positive errors do not cancel out), and the results are averaged.

**Interpretation:** An MAE of 5,000 means predictions are off by 5,000 units on average. It is easy to explain to a non-technical audience.

**Sensitivity to large errors:** Low. One very wrong prediction does not push MAE up disproportionately.

### Mean Squared Error (MSE)

MSE squares each error before averaging. Squaring has two effects: it removes negative signs, and it makes large errors much more expensive than small ones.

**Interpretation:** The units are squared (e.g., dollars²), which makes MSE hard to interpret directly. It is primarily used as a loss function during model training.

**Sensitivity to large errors:** High. Squaring means a prediction that is off by 10 contributes 100 to MSE, while one off by 100 contributes 10,000.

### Root Mean Squared Error (RMSE)

RMSE is the square root of MSE. Taking the root brings the units back to the original scale, making it directly comparable to MAE.

**Interpretation:** An RMSE of 5,000 means predictions are typically off by 5,000 units, but large individual errors are weighted more heavily than in MAE.

**Sensitivity to large errors:** High (inherited from MSE). If the difference between RMSE and MAE is large, the model has a few very bad predictions pulling the score down.

### R² Score (Coefficient of Determination)

R² measures how much of the variation in the target variable is explained by the model, expressed as a proportion between 0 and 1. An R² of 0.85 means the model explains 85% of the variance in the output.

- R² = 1.0: perfect predictions
- R² = 0.0: the model does no better than always predicting the mean
- R² < 0: the model performs worse than the mean baseline

**Interpretation:** R² gives a sense of overall fit quality. It does not indicate the size of errors in original units.

### Comparison Table

| Metric | Formula idea | Units | Sensitive to large errors? | Interpretation |
|---|---|---|---|---|
| MAE | Average of absolute errors | Same as target | No | Average prediction gap |
| MSE | Average of squared errors | Target squared | Yes | Used mainly in training |
| RMSE | Square root of MSE | Same as target | Yes | Like MAE but punishes outliers |
| R² | 1 minus ratio of residual variance | 0 to 1 (unitless) | No | % of variation explained |

---

## 4. Underfitting and Overfitting

### Underfitting

Underfitting happens when a model is too simple to capture the real patterns in the data. A linear regression on data with a curved relationship is a classic example. The model's assumptions do not match reality, so it performs poorly on both training data and new data.

Signs of underfitting: low R², high MAE and RMSE on training data, errors that are systematic rather than random.

Causes: choosing a model that is too simple for the problem, using too few features, not training long enough.

### Overfitting

Overfitting happens when a model learns the training data too closely, including its noise and random fluctuations. The model memorizes rather than generalizing, so it scores very well on training data but performs badly on new data.

In regression, overfitting is especially common in polynomial regression at high degrees. A degree-10 polynomial on 20 data points can pass through every training point exactly while making wildly wrong predictions between them.

Signs of overfitting: R² close to 1.0 on training data but much lower on test data, very low MAE on training but high MAE on test.

**Causes of overfitting in polynomial regression:**
- High degree polynomials create very flexible curves that chase noise
- Too many parameters relative to the number of training samples
- No regularization to constrain coefficient sizes

### Prevention Methods

**1. Use a simpler model.** If a linear model achieves similar test performance to a degree-5 polynomial, use the linear model. Unnecessary complexity invites overfitting.

**2. Regularization.** Ridge regression (L2) and Lasso regression (L1) add a penalty to the loss function that discourages large coefficient values. This limits how tightly the model can fit the training data. James et al. (2013) describe regularization as one of the most reliable tools for controlling variance in linear models.

**3. Cross-validation.** Rather than evaluating on a single test set, k-fold cross-validation trains and tests on multiple data splits and reports the average performance. A model that overfits will show a large gap between its training score and its cross-validation score, making the problem visible before deployment.

**4. More training data.** More examples make it harder to memorize individual cases and force the model toward general patterns. This is not always available, but it is the most direct remedy.

---

## 5. Real-World Case Study

### Regression in Healthcare: Predicting Hospital Length of Stay

**Source:** Turgeman, L., May, J. H., & Sciulli, R. (2017). Insights from a machine learning model for predicting the hospital Length of Stay (LOS) at the time of admission. *Expert Systems with Applications*, 78, 376–385. https://doi.org/10.1016/j.eswa.2017.02.023

**Goal:** Hospitals need to plan bed capacity and staffing. If a patient's length of stay can be estimated at the time of admission, hospital managers can allocate resources more effectively. This study built machine learning models to predict how many days each patient would stay in hospital based on information available at admission.

**Data used:** The dataset came from a large hospital in the United States and included several thousand patient records. Features included patient age, admission type (emergency vs. scheduled), primary diagnosis code, number of prior admissions, insurance type, and hospital department.

**Type of regression applied:** The study compared several approaches including Multiple Linear Regression, Poisson Regression (suited to count outcomes), and gradient boosted trees. Multiple Linear Regression served as the baseline, with each feature contributing a weighted coefficient to the predicted stay length.

**Key results:** Multiple Linear Regression achieved an R² of approximately 0.28, meaning it explained about 28% of the variation in length of stay. The tree-based ensemble models performed better, reaching R² values above 0.40. The study found that admission type, primary diagnosis, and number of prior admissions were the most important predictors across all models.

**Data Science lifecycle coverage:** This study covers the full CRISP-DM cycle. Business understanding established the need for capacity planning. Data preparation involved cleaning patient records and encoding diagnosis codes. Modeling compared multiple regression approaches. Evaluation compared R² and MAE across models. The authors discussed deployment implications for hospital information systems.

**Why this matters:** This is a good example of multiple regression used in a real healthcare context where the output (days) is a continuous number and the relationship between predictors and outcome is not purely linear. The study also illustrates a common real-world pattern: simple linear models provide a useful baseline, but ensemble methods often outperform them on complex tabular data.

---

## References

Galton, F. (1886). Regression towards mediocrity in hereditary stature. *Journal of the Anthropological Institute of Great Britain and Ireland*, 15, 246–263. https://doi.org/10.2307/2841583

James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). *An Introduction to Statistical Learning: With Applications in R*. Springer. https://doi.org/10.1007/978-1-4614-7138-7

Turgeman, L., May, J. H., & Sciulli, R. (2017). Insights from a machine learning model for predicting the hospital Length of Stay (LOS) at the time of admission. *Expert Systems with Applications*, 78, 376–385. https://doi.org/10.1016/j.eswa.2017.02.023

Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.

Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning: Data Mining, Inference, and Prediction* (2nd ed.). Springer. https://doi.org/10.1007/978-0-387-84858-7

---

*Submitted for DS-ML Bootcamp — Assignment Four*
*Due: Tuesday, June 30, 2026*