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

Regression is a supervised machine learning method for predicting a number. The model trains on labeled examples, where each input comes paired with a known numeric answer, and learns a function that maps inputs to outputs. After training, it estimates answers for inputs it has never seen.

The word comes from statistics. Francis Galton used it in 1886 to describe how children's heights tended back toward the population average rather than the extremes of their parents (Galton, 1886). Modern machine learning regression keeps the same core idea: given enough examples, find the pattern that connects inputs to a numeric target.

Practical uses include predicting house prices from size and location, estimating tomorrow's temperature from today's weather readings, and forecasting next month's sales from transaction history.

### Regression vs Classification

Both are supervised learning tasks. The difference is what the model predicts.

Regression predicts a number on a continuous scale. The output can be any value in a range, for example $342,000 or 23.7 degrees. Classification predicts a category from a fixed list of options, for example "spam" or "not spam."

| | Regression | Classification |
|---|---|---|
| Output type | Continuous number | Category from a fixed set |
| Example output | $342,000 | "Spam" |
| Question it answers | How much? How many? | Which category? |
| Example metric | MAE, RMSE, R² | Accuracy, F1-score |

A useful check: if the answer can fall anywhere on a number line, it is regression. If the answer must be one item from a list, it is classification.

### Real-Life Examples

**Regression:** Estimating the resale price of a used car given its age, mileage, brand, and condition. The output is a dollar amount that can be anywhere on a continuous scale.

**Classification:** Deciding whether a bank transaction is fraudulent or legitimate. The output is one of exactly two categories. There is nothing in between.

---

## 2. Types of Regression

### Linear Regression

Linear Regression fits a straight line through a dataset to describe the relationship between one input feature and a numeric target. It assumes that a fixed increase in the input always produces the same fixed increase in the output, regardless of the starting point.

The algorithm finds the line y = mx + b that minimises the total squared distance between the line and the data points. This is called Ordinary Least Squares (OLS).

**Real-world use case:** Predicting fuel consumption from engine size. Larger engines generally use more fuel in a roughly proportional way, which is a relationship a straight line captures well.

**Advantages:** Fast to train, simple to interpret, and coefficients directly show how much each feature contributes to the prediction.

**Limitations:** One input only, which is too restrictive for most real problems. It also assumes a perfectly straight relationship, which breaks down when the data curves or levels off.

### Multiple Linear Regression

Multiple Linear Regression extends the single-input version to handle several features at once. Instead of a line through a two-dimensional scatter plot, it fits a plane through multi-dimensional space. The model learns a weight for each feature: y = b0 + b1x1 + b2x2 + ... + bnxn. Each weight shows how much a one-unit increase in that feature moves the prediction, assuming all other features stay fixed.

**Real-world use case:** Predicting a house price using size, number of bedrooms, location, and year built together. No single feature tells the whole story, so the model uses all of them at once.

**Advantages:** More realistic than simple linear regression for problems that depend on several factors. Still interpretable because each coefficient has a clear meaning.

**Limitations:** Still assumes a linear relationship between each feature and the target. It also struggles when input features are correlated with each other, a problem called multicollinearity.

### Polynomial Regression

Polynomial Regression fits a curve rather than a straight line by adding powers of a feature (x², x³) as new input columns. Despite producing a curved output, it is still a linear model mathematically, because the algorithm is linear in its coefficients, not in the original feature values.

A degree-2 polynomial adds x² as a new feature, which allows the line to bend once. A degree-3 polynomial can bend twice, producing an S-shape.

**Real-world use case:** Modelling the relationship between advertising spend and revenue. Returns tend to grow quickly at first and then level off as audiences saturate, a curve that a straight line cannot capture.

**Advantages:** Captures non-linear patterns using the same OLS fitting procedure as linear regression. Interpretable at low degrees.

**Limitations:** High-degree polynomials overfit badly. The curve starts chasing noise in the training data instead of the real underlying pattern. Extrapolating outside the training range also produces unreliable results.

### Comparison Table

| | Linear Regression | Multiple Linear Regression | Polynomial Regression |
|---|---|---|---|
| Number of inputs | 1 | 2 or more | 1 or more |
| Shape of fit | Straight line | Flat plane / hyperplane | Curve |
| Handles non-linearity | No | No | Yes |
| Risk of overfitting | Low | Low to moderate | High at high degrees |
| Best use case | One-factor linear trends | Multi-factor linear problems | Curved, non-linear patterns |

---

## 3. Regression Metrics

After training, we need to measure how close predictions are to the actual values. Four metrics are standard for regression problems.

### Mean Absolute Error (MAE)

MAE takes the average of the absolute prediction errors. Absolute value means negative and positive errors do not cancel each other out before averaging.

An MAE of 5,000 means predictions are off by 5,000 units on average. It is easy to explain: the number lives in the same units as the target.

MAE treats all errors equally. A prediction that is off by 100 contributes 100 times more than one that is off by 1.

### Mean Squared Error (MSE)

MSE squares each error before averaging. Squaring does two things: it removes negative signs, and it makes large errors disproportionately expensive. A prediction off by 10 contributes 100 to MSE. A prediction off by 100 contributes 10,000.

The units are squared (dollars², for example), which makes MSE hard to read directly. It is mainly used as a training loss function rather than a reporting metric.

### Root Mean Squared Error (RMSE)

RMSE takes the square root of MSE, which brings the units back to the original scale.

An RMSE of 5,000 means predictions are typically off by 5,000 units, but with more weight on the largest errors. If RMSE is much higher than MAE for the same model, the model has a few predictions that are very wrong even though most are reasonable.

### R² Score (Coefficient of Determination)

R² measures what fraction of the variation in the target the model explains.

- R² = 1.0: perfect predictions
- R² = 0.0: the model does no better than always predicting the mean
- R² below 0: worse than the mean baseline

An R² of 0.85 means the model accounts for 85% of why prices vary across the dataset. The remaining 15% is variation the model cannot explain from the available features.

### Comparison Table

| Metric | Units | Sensitive to large errors | Interpretation |
|---|---|---|---|
| MAE | Same as target | No | Average size of prediction errors |
| MSE | Target squared | Yes | Used mainly during model training |
| RMSE | Same as target | Yes | Like MAE but penalises outlier predictions more |
| R² | Unitless (0 to 1) | No | Proportion of variance the model explains |

---

## 4. Underfitting and Overfitting

### Underfitting

Underfitting happens when a model is too simple to capture the real pattern in the data. Fitting a straight line to data that curves is a clear example. The model's assumptions do not match reality, so it makes systematic errors on both training data and new data.

Signs of underfitting: high error on training data, errors that follow a visible pattern rather than looking random, low R².

Typical causes: choosing an algorithm that is too simple, using too few features, or stopping training before the model has converged.

### Overfitting

Overfitting happens when a model learns the training data too closely, including its noise and random fluctuations. It memorises rather than generalises, which produces strong scores on training data and poor scores on data it has not seen.

Polynomial regression at high degrees is a textbook case. A degree-10 polynomial on 20 data points can pass exactly through every training point while producing wildly wrong predictions between them.

**What causes overfitting in polynomial regression specifically:**

- High-degree polynomials create very flexible curves with many parameters to fit
- With enough degrees, the model can fit any training set perfectly, including the noise
- The more parameters a model has relative to training samples, the more room it has to overfit

### Prevention

**Simpler model.** If a linear model achieves similar test performance to a degree-5 polynomial, use the linear model. Complexity that is not justified by the data will overfit.

**Regularization.** Ridge regression (L2) and Lasso regression (L1) add a penalty to the loss function that discourages large coefficient values. This limits how tightly the model can fit the training data, reducing variance. James et al. (2013) describe regularization as one of the most reliable tools for controlling this kind of overfitting in linear models.

**Cross-validation.** K-fold cross-validation trains and tests on multiple splits of the data and reports average performance. A model that overfits shows a large gap between training score and cross-validation score, making the problem visible before deployment.

---

## 5. Real-World Case Study

### Predicting Hospital Length of Stay with Multiple Linear Regression

**Source:** Turgeman, L., May, J. H., and Sciulli, R. (2017). Insights from a machine learning model for predicting the hospital Length of Stay (LOS) at the time of admission. *Expert Systems with Applications*, 78, 376-385. https://doi.org/10.1016/j.eswa.2017.02.023

**Goal:** Hospitals need to plan bed capacity and staffing. If the number of days a patient will stay can be estimated at admission, managers can allocate resources more effectively and reduce bottlenecks. This study built models to make that prediction from information available on the day the patient arrives.

**Data used:** Several thousand patient records from a large hospital in the United States. Features included patient age, admission type (emergency vs. scheduled), primary diagnosis code, number of prior admissions, insurance type, and hospital department.

**Regression type applied:** The study tested Multiple Linear Regression as a baseline alongside Poisson Regression and gradient boosted trees. Multiple Linear Regression worked by assigning a coefficient to each patient feature, then summing them to produce a predicted stay length in days.

**Key results:** Multiple Linear Regression achieved R² around 0.28, meaning it explained about 28% of the variation in stay length. The tree-based ensemble models reached above 0.40. Admission type, primary diagnosis, and prior admissions were the strongest predictors across all models.

**Why this is relevant:** Length of stay is a continuous number (days), which makes it a regression problem rather than classification. The study also shows a pattern common in real-world healthcare data: simple linear models provide a useful starting point, but the relationship between patient characteristics and outcomes is not fully linear. Ensemble methods improved on the baseline, but the linear model was still useful for understanding which features mattered most, because its coefficients are directly interpretable.

The study maps to the full CRISP-DM lifecycle: the business need drove the feature selection (data understanding), patient records required cleaning and diagnosis code encoding (data preparation), multiple algorithms were compared (modeling), R² and MAE guided final model selection (evaluation), and the authors discussed integration into hospital information systems (deployment).

---

## References

Galton, F. (1886). Regression towards mediocrity in hereditary stature. *Journal of the Anthropological Institute of Great Britain and Ireland*, 15, 246-263. https://doi.org/10.2307/2841583

James, G., Witten, D., Hastie, T., and Tibshirani, R. (2013). *An Introduction to Statistical Learning: With Applications in R*. Springer. https://doi.org/10.1007/978-1-4614-7138-7

Turgeman, L., May, J. H., and Sciulli, R. (2017). Insights from a machine learning model for predicting the hospital Length of Stay (LOS) at the time of admission. *Expert Systems with Applications*, 78, 376-385. https://doi.org/10.1016/j.eswa.2017.02.023

Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.

Hastie, T., Tibshirani, R., and Friedman, J. (2009). *The Elements of Statistical Learning: Data Mining, Inference, and Prediction* (2nd ed.). Springer. https://doi.org/10.1007/978-0-387-84858-7

---

*Submitted for DS-ML Bootcamp — Assignment Four*
*Due: Tuesday, June 30, 2026*