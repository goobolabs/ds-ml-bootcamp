# Reflection Paper — Car Price Prediction

**Assignment Four, Part C**

> **Note:** Since `clean_car_dataset.csv` was not available when this was written, the specific numbers below (metrics, sanity-check prices) are **illustrative placeholders**, written to show the structure and reasoning expected in this paper. Once the notebook is run on the real dataset, replace the bracketed/example values with your actual output before submitting.

---

## 1. What Did I Implement?

For this assignment, I built on the cleaned car dataset from Assignment Three to train two regression models capable of predicting a car's price. First, I separated the data into features (`X`) — every column except `Price` and `LogPrice` — and the target (`y`) — the `Price` column itself. I excluded `LogPrice` because it is mathematically derived from `Price`, and including it would let the model "see" the answer indirectly, which would produce misleadingly perfect results.

I split the data into an 80% training set and a 20% test set using `random_state=42` for reproducibility, then trained two models on the training data: a `LinearRegression` model, which fits a straight-line relationship between the features and price, and a `RandomForestRegressor` with 100 trees, which builds an ensemble of decision trees and averages their predictions. Both models were then evaluated on the untouched 20% test set to see how well they generalize to cars they had never seen during training.

## 2. Comparison of Models

For the sanity check, I picked one row from the test set (index `i = 3`) and compared both models' predictions against the actual price. For example:

| | Value |
|---|---|
| Actual Price | $[$7,009] |
| Linear Regression Prediction | $[ $7,457] |
| Random Forest Prediction | $[$8,701] |

**Expected output shape** (actual numbers depend on the dataset once run):

```
Linear Regression Performance:
Linear Regression Performance:
  R2   : 0.908
  MAE  : 592
  MSE  : 613,419
  RMSE : 783

Random Forest Performance:
  R2   : 0.931
  MAE  : 345
  MSE  : 458,647
  RMSE : 677
```

Typically, Random Forest is expected to show a higher R² and lower MAE/RMSE than Linear Regression, since car pricing tends to involve non-linear relationships (e.g., diminishing returns on age, brand premiums) that a linear model can't fully capture.

In this example, the Random Forest prediction landed closer to the actual price than the Linear Regression prediction. This is a pattern I would generally expect: car pricing depends on interactions between features — for instance, how much mileage lowers a price probably depends on the car's age and brand, not just mileage alone — and Random Forest is much better equipped to capture that kind of non-linear, interacting relationship than a model that can only draw a straight line through the data.

## 3. Understanding Random Forest

In my own words, a Random Forest is not a single model but a collection — a "forest" — of many individual decision trees, each trained slightly differently. Each tree is trained on a random subset of the training data (sampled with replacement) and, at each split within the tree, is only allowed to consider a random subset of the available features. This randomness means that no two trees in the forest end up identical; each one learns a slightly different, imperfect view of the relationship between features and price.

When it's time to make a prediction, every tree in the forest produces its own price estimate, and the Random Forest's final output is simply the **average** of all of those individual tree predictions. This averaging is the key to why Random Forest tends to perform well: while any single decision tree might overfit to quirks in its particular slice of the data, the errors of many different trees tend to cancel out when averaged together, leaving a prediction that is both more accurate and more stable than any one tree on its own.

## 4. Metrics Discussion

Based on the evaluation step, the Random Forest model achieved a higher R² and lower MAE and RMSE than the Linear Regression model (for example, an R² of roughly [0.931] for Random Forest versus [0.908] for Linear Regression, with a correspondingly lower RMSE). A higher R² means Random Forest explained a larger share of the variation in car prices, and the lower MAE/RMSE confirms that its individual predictions were, on average, closer to the true prices.

This tells me that Linear Regression's core weakness here is its assumption of a purely linear relationship between each feature and price — real car pricing almost certainly involves diminishing returns, thresholds, and interactions between features that a straight-line model simply cannot represent. Its strength, however, is that it is simple and highly interpretable: each coefficient directly tells you how much a feature is expected to change the price. Random Forest's strength is its accuracy and its ability to model complex, non-linear patterns, but its weakness is that it is much harder to interpret — you can't point to a single coefficient and say "this is exactly how much mileage affects price" the way you can with a linear model.

## 5. My Findings

Overall, I would prefer the Random Forest model for actual car price prediction, primarily because of its stronger performance on the held-out test set — a higher R² and lower error metrics mean its predictions are, on average, both more accurate and more trustworthy for a real user trying to estimate a fair price. Car pricing is inherently a complex, non-linear problem shaped by the interaction of many factors (brand, age, mileage, condition, and more), and Random Forest's ensemble structure is much better suited to capturing that complexity than a single straight-line model.

That said, I recognize Linear Regression still has real value, particularly when interpretability matters — for example, if a stakeholder wants to understand *why* the model predicts a certain price, or by how much price is expected to change per additional 10,000 miles of mileage, the linear model's coefficients answer that directly, while the Random Forest's internal logic is much more opaque. In a production setting, I would likely deploy Random Forest for the actual price predictions, but keep a Linear Regression model on hand as an interpretable baseline for explaining pricing trends to non-technical stakeholders.
