# Assignment Four: Regression — Theory and Practice
## Part A — Theory

## 1. Introduction to Regression

Regression is a type of Supervised Machine Learning used to predict a numeric (continuous) value. The model is trained on historical data made up of inputs (X), also called features, and an output (y), called the label, so that it learns the relationship between them. When it receives new data, it uses what it has learned to estimate a numeric outcome, such as the price of a car or the price of a house.

Regression predicts a continuous numeric value, for example: the price of a car. Classification predicts a category or class, for example: spam or not spam. In short: Regression = predicting how much. Classification = predicting which class.

**Regression example:** Estimating the price of a house based on its size, location, and number of rooms.

**Classification example:** Email spam detection — sorting an email as "Spam" or "Not Spam."

## 2. Types of Regression

### Linear Regression
**How it works:** Linear regression looks for a straight-line relationship between one input (X) and one output (y).

**Real-world example:** Estimating a house's price based on its size.

**Advantages:** Simple and easy to understand; fast to compute; works well when the data follows a straight-line trend.

**Limitations:** Only captures a linear relationship; sensitive to outliers; cannot capture complex or non-linear relationships.

### Multiple Linear Regression
**How it works:** The same as Linear Regression, but using more than one input (X1, X2, X3...).

**Real-world example:** Predicting a house's price while considering size, location, number of rooms, and the age of the house.

**Advantages:** More accurate than simple linear regression; uses several factors at once; still relatively easy to interpret.

**Limitations:** Still assumes a linear relationship; can suffer from multicollinearity when features are correlated with each other; not well-suited for very complex data.

### Polynomial Regression
**How it works:** Captures non-linear relationships by using powers of the input (squares, cubes).

**Real-world example:** Predicting bacterial growth over time; the relationship between a car's speed and its fuel consumption.

**Advantages:** Captures complex, curved relationships; more flexible than linear models.

**Limitations:** Easily overfits; harder to interpret; sensitive to noise in the data.

## 3. Regression Metrics

**MAE (Mean Absolute Error)** is a metric used to evaluate how accurate a machine learning model is. It measures the average difference between the actual values and the values predicted by the model, without considering the sign (positive or negative) of the difference. MAE shows, on average, how much error the model makes in its predictions.

**MSE (Mean Squared Error)** is a metric used to evaluate the accuracy of a machine learning model. It calculates the average of the differences between the actual values and the predicted values, but each error is squared before averaging. This makes large errors stand out much more than small ones. By squaring the errors, MSE highlights the bigger mistakes, which helps the model learn from its errors better and improve its predictions.

**RMSE (Root Mean Squared Error)** is a metric used to evaluate the accuracy of a model. It squares the errors, then averages them (MSE), and finally takes the square root so that the result is back in the same units as the original data. RMSE highlights large errors more strongly, and it helps in understanding how much the model typically deviates from its predictions, on average.

**R² (Coefficient of Determination)** is a metric that measures how well a model can explain the variation in the target variable. Unlike MAE, MSE, and RMSE, R² does not measure error directly; instead, it shows the percentage of the data's variation that the model can accurately explain.

- R² = 1.0 → The model is a perfect fit and explains the data completely.
- R² = 0.0 → The model is no better than simply using the average to make predictions.
- R² < 0 (e.g., -0.2) → The model performs worse than simply using the average, indicating poor predictions.

**Example:** If R² = 0.85, it means the model can explain 85% of the variation in the data, while the remaining 15% is due to other factors or error.

| Metric | Meaning | Sensitive to Big Errors? | Units |
|--------|---------|---------------------------|-------|
| MAE | Average absolute error | No | Same as data |
| MSE | Average squared error | Yes | Squared units |
| RMSE | Root of MSE | Yes | Same as data |
| R² | % of pattern explained | No | 0 to 1 |

## 4. Underfitting and Overfitting

Underfitting occurs when a model fails to learn the data well. It becomes too simple and only understands a small part of the data, ignoring the rest. As a result, it makes errors even on the data it has already seen (the training data).

Overfitting occurs when a model learns the training data excessively, essentially memorizing it. As a result, it performs very well on the data it was trained on, but fails when given new data, because it did not understand the general pattern — it only memorized the specifics.

Overfitting, particularly in polynomial regression, occurs when the model becomes too complex (a high degree) and starts learning even the noise and minor fluctuations in the training data, instead of learning the true underlying pattern. This causes it to perform very well on the data it was trained on, but to fail on new data.

**Methods to prevent overfitting:**

- **More training data:** Using more data helps the model learn the true underlying pattern instead of memorizing a small amount of data.
- **Simplify the model:** Use a simpler model (for example, a lower polynomial degree) so that it does not become too complex and memorize the data.
- **Regularization (L1 / L2):** This reduces the size of large weights in the model, helping it learn the general pattern instead of memorizing noise.
- **Cross-validation:** Used to test the model on different portions of the data to confirm that it performs well overall, not just on the training data.

## 5. Real-World Case Study: Predicting House Prices (Real Estate Industry)

**Goal:** The purpose of this project was to predict house prices so that buyers and real estate companies could accurately understand market values.

**Data Used:** The data used included the size of the house (in square meters), the number of bedrooms, the location/neighborhood, the age of the house, and facilities such as parking or a garden.

**Type of Regression Applied:** Multiple Linear Regression was used, because a house's price depends on more than one factor (multiple features).

**Key Results / Insights:**

- House size was the factor with the greatest impact on price.
- Houses in prime locations had higher prices even when they were smaller.
- The model predicted house prices well, achieving a good R² score.
- It was found that combining multiple features produced more accurate results than using a single feature alone.
