
Reflection Paper : Car Price Prediction

1. What was implemented

In this assignment, two main regression approaches were built to predict car prices using a cleaned dataset: Linear Regression (including Ridge Regression) and Random Forest Regressor.

The workflow started by loading the dataset (car_cleaned_ready.csv) and performing a quick inspection using info() and describe(). The target variable was transformed into LogPrice to reduce skewness and improve model stability, while the feature set was prepared by dropping Price and LogPrice, followed by one-hot encoding for categorical variables.

The dataset was then split into training and testing sets (80/20 split). To ensure more reliable evaluation, 5-fold cross-validation (KFold) was used during training.

Three models were trained:

Linear Regression as a baseline linear model
Ridge Regression as a regularized version of linear regression to reduce overfitting
Random Forest Regressor as a non-linear ensemble model

Each model was evaluated using:

R² (explained variance)
MAE (Mean Absolute Error)
RMSE (Root Mean Squared Error)

A sanity check was also performed by comparing predictions on individual samples.

2. Comparison of Models

From the cross-validation results:

Linear Regression R² ≈ 0.54
Ridge Regression R² ≈ 0.54
Random Forest R² ≈ 0.71

On training/cross-validation performance, Random Forest clearly looked stronger, capturing more variance in the data.

However, the test set results told a different story:

Linear Regression R² ≈ 0.541
Ridge Regression R² ≈ 0.542
Random Forest R² ≈ 0.479

This mismatch is important. While Random Forest performed better during cross-validation, it dropped significantly on unseen test data.

Sanity Check Differences

In individual predictions, Random Forest often produced values that were more “flexible” but less consistent with actual prices. Linear and Ridge models gave more stable, smoother predictions. This suggests that Random Forest may have learned patterns too specific to the training folds (mild overfitting or instability on this small dataset).

3. Understanding Random Forest

Random Forest is an ensemble learning method made up of many decision trees. Instead of relying on a single tree, it builds multiple trees using random subsets of the data and features.

Each tree makes its own prediction, and the final output is the average of all tree predictions (for regression problems).

Key idea:

One tree = high variance, unstable
Many trees combined = more stable and robust prediction

Randomness is introduced in two ways:

Bootstrapping (random samples of data)
Random feature selection at each split

This helps reduce overfitting compared to a single decision tree, but it can still struggle on small datasets or when the signal is weak.

4. Metrics Discussion

From the final evaluation:

Linear Regression

R² ≈ 0.541
MAE ≈ 0.361
RMSE ≈ 0.466

Ridge Regression

R² ≈ 0.542
MAE ≈ 0.360
RMSE ≈ 0.466

Random Forest

R² ≈ 0.479
MAE ≈ 0.257
RMSE ≈ 0.497
Interpretation
R² (best: Linear/Ridge)
Linear and Ridge explain slightly more variance on the test set compared to Random Forest. This indicates more consistent generalization.
MAE (best: Random Forest)
Random Forest had lower MAE, meaning it was closer on average to actual values, even if variance explanation was weaker.
RMSE (worst: Random Forest)
Higher RMSE suggests Random Forest made some larger errors that heavily affected performance.
What this means
Linear and Ridge models are stable and consistent, especially for structured datasets.
Random Forest is more flexible, but in this case it did not generalize well to unseen data.

The dataset size (around 140 rows) is likely a key limitation. Tree-based models like Random Forest usually perform better with more data.

5. Final Findings and Preferred Model

Based on the results, the most reliable model for this dataset is Ridge Regression.

Although its performance is almost identical to Linear Regression, Ridge is slightly more robust because it applies regularization, reducing the risk of overfitting and handling multicollinearity better.

Random Forest showed strong cross-validation performance but failed to maintain that strength on the test set. This inconsistency makes it less reliable for deployment in this case.

In summary:

Ridge Regression is the best balance between stability and accuracy.
Linear Regression performs similarly but is less robust.
Random Forest is powerful in theory, but underperforms here due to dataset size and possible overfitting.

For this dataset, simpler linear models outperform more complex ones because the relationships between features and price appear mostly linear rather than highly non-linear.