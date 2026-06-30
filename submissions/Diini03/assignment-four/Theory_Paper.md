# Assignment Four — Regression: Theory and Practice

## 1. Introduction to Regression

Regression is a type of supervised learning where the model predicts a continuous number as output. You give it input features and it learns the relationship between those features and a numeric target — like price, temperature, or score.

The difference between regression and classification is the output type. Regression predicts a number. Classification predicts a category.

**Regression example:** Predicting a football player's market value based on age, goals scored, assists, and minutes played. The output is a number — say $24 million.

**Classification example:** Predicting whether a team will win or lose their next match. The output is a category — Win or Loss.

---

## 2. Types of Regression

### Linear Regression

Linear Regression assumes a straight-line relationship between one input feature and the target. The model finds the best-fit line through the data.

**How it works:** It learns two things — a slope and an intercept — and draws a line that minimizes the gap between predicted and actual values.

**Use case:** Predicting a player's goals next season based only on their shots on target per game.

**Advantage:** Simple, fast, and easy to interpret.

**Limitation:** Only works well when the relationship between the feature and target is actually linear. Real data is rarely that clean.

---

### Multiple Linear Regression

Same idea as linear regression but with more than one input feature. Instead of one line, the model fits a plane (or hyperplane) across multiple dimensions.

**How it works:** Each feature gets its own weight. The model adds them all up to produce a prediction.

**Use case:** Predicting a player's market value using age, goals, assists, position, and league — all at once.

**Advantage:** More realistic than simple linear regression because most outcomes depend on multiple factors.

**Limitation:** Assumes all features have a linear relationship with the target, which is often not true.

---

### Polynomial Regression

Polynomial Regression handles curved relationships. Instead of fitting a straight line, it fits a curve by adding powers of the input feature (x², x³, etc.).

**How it works:** It transforms the original feature into multiple features (x, x², x³...) and then runs linear regression on them.

**Use case:** Modeling how a footballer's performance changes with age — it goes up in early career, peaks around 26–28, then declines. That's a curve, not a line.

**Advantage:** Can capture non-linear patterns that linear regression misses.

**Limitation:** Easy to overfit. A high-degree polynomial can memorize the training data and perform poorly on new data.

---

## 3. Regression Metrics

### MAE — Mean Absolute Error

The average of the absolute differences between predicted and actual values. It tells you on average how far off your predictions are, in the same units as the target.

### MSE — Mean Squared Error

Same as MAE but it squares the errors before averaging. This means large errors are punished more heavily than small ones.

### RMSE — Root Mean Squared Error

The square root of MSE. It brings the error back to the same units as the target, making it easier to interpret than MSE while still being sensitive to large errors.

### R² — Coefficient of Determination

Measures how much of the variance in the target the model explains. R² = 1.0 means perfect predictions. R² = 0 means the model is no better than just predicting the average every time.

---

### Comparison Table

| Metric | Units             | Sensitive to Large Errors | Meaning                     |
| ------ | ----------------- | ------------------------- | --------------------------- |
| MAE    | Same as target    | No                        | Average absolute error      |
| MSE    | Squared units     | Yes                       | Penalizes large errors more |
| RMSE   | Same as target    | Yes                       | Like MSE but interpretable  |
| R²     | No units (0 to 1) | No                        | % of variance explained     |

---

## 4. Underfitting and Overfitting

**Underfitting** happens when the model is too simple to capture the pattern in the data. It performs poorly on both training and test data. A linear model trying to fit a curved relationship is a classic example.

**Overfitting** happens when the model learns the training data too well — including its noise. It performs great on training data but fails on new data.

In polynomial regression, overfitting is common when the degree is too high. A degree-10 polynomial on a small dataset will bend and twist to hit every training point perfectly but will make wild predictions on anything it hasn't seen.

**Ways to prevent overfitting:**

1. **Reduce model complexity** — use a lower polynomial degree or fewer features
2. **Regularization** — techniques like Ridge or Lasso add a penalty for large coefficients, keeping the model simpler
3. **More training data** — the more examples the model sees, the harder it is to memorize them

---

## 5. Real-World Case Study — Predicting Player Market Value in Football

**Source:** Singh, A. & Bhattacharya, S. (2019). _Predicting football player market value using machine learning._ International Journal of Computer Applications, 182(50), 1–6.

**Goal:** Build a regression model that predicts the transfer market value of professional football players based on their performance statistics and personal attributes.

**Data used:** Player data from FIFA datasets and Transfermarkt — including age, overall rating, potential, goals, assists, position, nationality, and contract length. Over 10,000 player records were used.

**Type of regression:** Multiple Linear Regression was used as the baseline, alongside more advanced ensemble methods for comparison.

**Key results:** The model showed that overall rating, age, and potential were the strongest predictors of market value. Younger players with high potential were consistently valued higher even if their current stats were average. The linear regression model achieved reasonable accuracy but struggled with top-tier players whose valuations are influenced by factors the data doesn't capture — like social media following or club branding.

**Where it fits in the DS lifecycle:** This project covers the full pipeline — problem definition, data collection from Transfermarkt, cleaning and feature engineering, modeling, and evaluation. It is a practical example of how regression sits inside the broader Data Science workflow.
