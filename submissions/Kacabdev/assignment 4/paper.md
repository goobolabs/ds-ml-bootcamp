# Assignment Four – Part A: Regression, Theory and Practice

**Name:** Abdurahman aden (Kacabdev)
**Course:** DS AND ML – Lesson 4, Regression

---

## 1. Introduction to Regression

When I first heard the word "regression" in this course, it sounded scarier than it actually is. In simple terms, regression is a type of supervised learning where the model tries to predict a **number**, not a category. We give it examples of inputs (features) together with the correct numeric answer (label), and the model learns the relationship between them so it can guess the number for new, unseen inputs.

The main thing that separates regression from classification is the *type of output*. Classification answers a question like "which group does this belong to?" — spam or not spam, cat or dog, pass or fail. Regression answers "how much?" or "how many?" — a price, a temperature, a score. Both are supervised learning (they both learn from labeled data), but the shape of the answer is completely different.

**Example of regression:** predicting the rent of an apartment based on its size, number of rooms, and neighborhood. The output is a continuous number, e.g. $450, $610, $1,200.

**Example of classification:** predicting whether an email is spam or not. The output is one of two fixed categories, not a number.

A simple way I remember it: *regression predicts a value on a scale, classification predicts a label from a list.*

---

## 2. Types of Regression

### 2.1 Linear Regression

Linear Regression is the simplest form. It tries to draw one straight line through the data that best represents the relationship between a single input feature and the output. For example, using only the size of a house (in square feet) to predict its price — as the size increases, the price tends to increase too, and Linear Regression tries to capture that trend with a straight line.

- **How it works (basic idea):** it finds the line `y = mx + b` that minimizes the distance between the line and the actual data points.
- **Real-world use case:** predicting a student's exam score based on the number of hours they studied.
- **Advantages:** very easy to understand, fast to train, and the results are easy to explain to someone who isn't technical.
- **Limitations:** it assumes the relationship is a straight line and that only one factor matters, which is rarely true in real life. Most outcomes depend on more than one variable.

### 2.2 Multiple Linear Regression

Multiple Linear Regression is basically the same idea as Linear Regression, except now the model looks at **several input features at the same time** instead of just one. Instead of a single line, imagine it as a flat plane (when there are two features) or a higher-dimensional surface (when there are more).

- **How it works (basic idea):** the model learns a weight (coefficient) for each feature, and combines them together to make the final prediction — for example, price depends a bit on size, a bit on number of bedrooms, a bit on location, and so on, all added together.
- **Real-world use case:** predicting a used car's price based on mileage, age, number of accidents, and location — which is exactly what we do in Part B of this assignment.
- **Advantages:** more realistic than simple Linear Regression because it accounts for multiple factors that actually influence the outcome.
- **Limitations:** it can struggle if the features are strongly correlated with each other (multicollinearity), and it still assumes the underlying relationship is linear, which may not always be true.

### 2.3 Polynomial Regression

Polynomial Regression is used when the relationship between the input and output is **curved** rather than a straight line. It works by adding new features that are powers of the original one, like `size²` or `size³`, so the model is technically still "linear" in terms of the coefficients, but the line it draws can bend.

- **How it works (basic idea):** it transforms one feature into several (x, x², x³, …) and then fits a regression on top of those, which allows the fitted line to curve instead of staying straight.
- **Real-world use case:** modeling how a car's value drops over time — depreciation is usually fast in the first couple of years and then slows down, which is a curve, not a straight line.
- **Advantages:** captures non-linear patterns that a plain straight line would miss, while still being relatively simple and interpretable compared to more advanced models.
- **Limitations:** if the degree of the polynomial is too high, the curve can start bending to fit every little bump in the training data, which leads to overfitting (explained more in section 4).

### 2.4 Comparison

| Aspect | Linear Regression | Multiple Linear Regression | Polynomial Regression |
|---|---|---|---|
| Number of inputs | One | Several | One or more, but raised to powers |
| Shape of relationship | Straight line | Flat plane / hyperplane | Curve |
| Complexity | Lowest | Medium | Can get high depending on degree |
| Risk of overfitting | Low | Low–Medium | Higher, especially at high degrees |

---

## 3. Regression Metrics

Once a model makes predictions, we need a way to measure how good those predictions actually are. This is where metrics come in — they turn "the model looks okay" into an actual number we can compare.

- **MAE (Mean Absolute Error):** the average of the absolute difference between predicted and actual values. It tells us, on average, how far off our predictions are, in the same unit as the target (e.g., dollars). It treats every mistake equally, whether it's small or huge.

- **MSE (Mean Squared Error):** similar to MAE, but the errors are squared before averaging. Squaring makes big mistakes count a lot more than small ones, so a model with a few very wrong predictions will get punished harder under MSE. The downside is that its unit is "squared dollars," which isn't very intuitive.

- **RMSE (Root Mean Squared Error):** just the square root of MSE. This brings the error back into the original unit (dollars, degrees, etc.), so it's easier to interpret than MSE, while still being more sensitive to big mistakes than MAE.

- **R² (Coefficient of Determination):** instead of measuring error directly, R² tells us what proportion of the variation in the target the model is able to explain. An R² of 1.0 means a perfect fit, 0.0 means the model is no better than just guessing the average value every time, and a negative R² means the model is actually worse than that.

### Comparison Table

| Metric | Meaning | Units | Sensitive to Large Errors? |
|---|---|---|---|
| MAE | Average absolute error | Same as target | No |
| MSE | Average squared error | Squared units | Yes |
| RMSE | Square root of MSE | Same as target | Yes |
| R² | Proportion of variance explained | 0–1 (can go negative) | No |

In practice, I like to look at RMSE and R² together: RMSE gives me a concrete number I can explain to a non-technical person ("we're off by about $2,000 on average"), while R² tells me how much of the overall pattern the model is actually capturing.

---

## 4. Underfitting and Overfitting

**Underfitting** happens when a model is too simple to capture the real pattern in the data. It performs poorly on both the training data and new data, because it hasn't actually learned the relationship — it's just making rough, generic guesses. A straight line trying to fit a clearly curved relationship (like car depreciation) is a good example of underfitting.

**Overfitting** is the opposite problem: the model learns the training data *too well*, including the noise and random quirks that don't generalize. It performs great on the data it was trained on but poorly on new, unseen data, because it basically "memorized" instead of "learned."

Polynomial Regression is especially prone to overfitting because increasing the degree gives the model more and more freedom to bend the curve. With a high enough degree, the curve can twist itself to pass almost exactly through every single training point — which looks perfect on paper but fails badly the moment it sees new data, because it's fitting noise, not the actual trend.

**Ways to prevent overfitting:**

1. **Keep the model reasonably simple** — for polynomial regression, don't use a higher degree than necessary; test a few degrees and pick the one that generalizes best, not just the one with the lowest training error.
2. **Use train/test splits or cross-validation** — evaluate the model on data it hasn't seen, so you can catch overfitting before deploying the model.
3. **Use regularization (e.g., Ridge or Lasso regression)** — these techniques penalize overly complex models, discouraging the model from relying too heavily on any single feature or extreme coefficient.
4. **Get more training data** — with more examples, it becomes harder for the model to simply memorize noise, so it's pushed to learn the actual underlying pattern instead.

---

## 5. Real-World Case Study

For this section I looked at a recent study that used regression to predict **life expectancy** using data from the World Health Organization (WHO) and the United Nations (UN).

- **Goal:** estimate a country's life expectancy using demographic, health, and socioeconomic indicators, and compare how well different regression-style models could do it.
- **Data used:** a real-world, multidimensional dataset compiled from WHO and UN sources, covering vaccination coverage, geographic and demographic data, mortality indicators, and socioeconomic variables across many countries and time periods. Specifically, it covered 193 countries between the years 2000 and 2015, with 22 columns and close to 2,938 rows of data.
- **Type of regression applied:** the researchers compared several models of different complexity — Linear Regression as a baseline, along with tree-based models like Decision Tree and Random Forest — to see how they handled the relationship between health/economic factors and life expectancy.
- **Key results/insights:** the researchers noted that traditional demographic models based only on historical mortality data often fail to capture the complex, non-linear relationships between health, environmental, and socioeconomic factors, especially as global conditions change quickly. This matches exactly what we learned in Lesson 4 — a plain straight-line model can miss important patterns that a more flexible model (or added polynomial terms) can pick up. It also connects to what I found in my own Part B experiment below: more flexible models don't automatically win, especially on small datasets — the right model really depends on the size and shape of the data you have.

I picked this study because it isn't just "regression worked, the end" — it actually shows why researchers compare multiple regression approaches (simple vs. more complex) instead of assuming one is always better, which is the same lesson I learned first-hand while comparing Linear Regression and Random Forest on my own car price dataset.

---

*This content is an AI written, but the exact Aim or understanding is inside my mind that means I understood it.*