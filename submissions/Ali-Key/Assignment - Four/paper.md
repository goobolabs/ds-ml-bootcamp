# Reflection Paper — Assignment Four: Regression

**Author:** Ali Omar Abdi
**Course:** DS-ML Bootcamp
**Due:** Tuesday, June 30, 2026 — 12:00 PM (Africa/Mogadishu / EAT)

---

## 1. What Did I Implement?

I trained two regression models on the cleaned car dataset from Assignment Three to predict car prices. The dataset went through a full preprocessing pipeline before this step, including imputation, outlier capping, one-hot encoding of the Location column, and feature engineering that added HouseAge, PricePerSqft, BedroomRatio, and Is_Urban. LogPrice was excluded from the features to avoid target leakage.

The features fed into both models were the same: scaled continuous columns (Size_sqft, Bedrooms, Bathrooms, YearBuilt, HouseAge, PricePerSqft, BedroomRatio) alongside binary dummies (Location_City, Location_Rural, Location_Suburb, Is_Urban).

The data was split 80/20 with random_state=42, giving 112 rows for training and 28 for testing. I trained a LinearRegression model first as a baseline, then a RandomForestRegressor with n_estimators=100 and the same random seed for reproducibility.

---

## 2. Comparison of Models

The results were somewhat unexpected. Linear Regression scored R² = 0.434, while Random Forest scored R² = 0.266. On this dataset, the simpler model outperformed the ensemble.

In the sanity check (row index 3 of the test set), the actual price was $7,009. Linear Regression predicted $5,685, an error of about $1,324. Random Forest predicted $6,951, which was closer to the actual value by about $58, even though its overall R² was lower.

This shows that a single-row comparison can give a misleading picture. One row where the forest happened to predict well does not mean the forest is more accurate across the full test set. The aggregate metrics (R², MAE, RMSE over all 28 test rows) are more reliable than any individual prediction.

The forest's lower R² on this dataset is probably explained by the small sample size. Random Forest is a high-variance model that needs enough data to average out noise across its trees. With only 112 training rows, it may have overfit to the training split while the linear model's simpler structure generalized better.

---

## 3. Understanding Random Forest

Random Forest is an ensemble method built from many decision trees, each trained on a randomly sampled subset of the training data and a random subset of the features. At prediction time, each tree produces its own estimate, and the forest averages them.

The key idea is that individual trees can overfit badly (high variance), but if the trees are different enough from each other, their errors tend to cancel out when averaged. The randomness introduced in both data sampling (bagging) and feature selection at each split creates enough variety between trees to make averaging useful.

Random Forest is often described as one of the most reliable off-the-shelf machine learning algorithms because it handles non-linear relationships, does not require feature scaling, and is not very sensitive to its hyperparameters. Its main weaknesses are that it is harder to interpret than a single linear model and that it needs a reasonable amount of data to benefit from the ensemble mechanism.

---

## 4. Metrics Discussion

| Metric | Linear Regression | Random Forest |
|---|---|---|
| R² | 0.434 | 0.266 |
| MAE | 1,427 | 1,192 |
| MSE | 3,770,383 | 4,887,988 |
| RMSE | 1,942 | 2,211 |

Linear Regression had the better R², MSE, and RMSE. Random Forest had the better MAE, which means its individual errors were smaller on average, but it had more large outlier errors that pushed MSE and RMSE higher (both metrics penalize large errors more than MAE does).

An R² of 0.43 for Linear Regression means the model explains about 43% of the variance in price. That is a modest result. In practice, a house price or car price predictor used in production would need R² much closer to 0.85 or higher. The limited dataset size (99 clean rows, 112 after imputation, 28 for testing) is the most likely explanation for both models performing modestly.

The gap between MAE and RMSE for Random Forest (1,192 vs 2,211) is larger than for Linear Regression (1,427 vs 1,942), which confirms that the forest made a few predictions that were far off the mark, even though its typical error was smaller. This is consistent with overfitting on a small dataset.

---

## 5. My Findings

Both models produced reasonable predictions for most test rows, but neither achieved the kind of R² score I would consider reliable for real-world price prediction. The dataset is intentionally small and messy, so this is expected.

For this specific dataset, Linear Regression is the better choice. It explains more overall variance and its error distribution is more consistent. The Random Forest's lower MAE is encouraging, but the higher RMSE suggests it made a handful of notably wrong predictions that offset the advantage.

If I had access to more data (several thousand rows rather than under a hundred), I would expect Random Forest to outperform Linear Regression. The ensemble's strength comes from averaging across many trees, and with only 112 training rows, there simply are not enough examples for that mechanism to work well. I would also experiment with cross-validation rather than a single 80/20 split, since with a dataset this small the split itself has a large effect on the results.

The most important thing I took from this exercise is that model choice matters less than data quality and quantity. Both models struggled here because the underlying dataset is small. Collecting more data, or engineering more informative features, would improve both models more than switching algorithms.

---

*Submitted for DS-ML Bootcamp — Assignment Four*
*Due: Tuesday, June 30, 2026*