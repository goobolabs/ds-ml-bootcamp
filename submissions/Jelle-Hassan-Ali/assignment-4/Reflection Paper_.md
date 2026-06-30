Reflection Paper : Car Price Prediction 

1. What was implemented ?

In this assignment, multiple regression models were implemented to predict car prices using a cleaned dataset (car_cleaned_ready.csv). The main goal was to compare linear and non-linear approaches and evaluate their predictive performance.

The workflow started with loading the dataset and performing basic inspection using info() and describe() to understand structure and data types. The target variable was transformed into LogPrice, which helps reduce skewness and improves model performance.

The feature set was prepared by dropping the original Price and LogPrice columns, followed by one-hot encoding for categorical variables.

The dataset was split into training and testing sets using an 80/20 split.

Three models were implemented:

Linear Regression (baseline model)
Ridge Regression (regularized linear model)
Random Forest Regressor (non-linear ensemble model)

Model evaluation was done using:

R² (variance explained)
MAE (Mean Absolute Error)
RMSE (Root Mean Squared Error)

A sanity check was also performed by comparing individual predictions against actual values.

Additional Experiment: Ridge Regression & Cross-Validation

An additional experiment was introduced using Ridge Regression combined with 5-fold cross-validation (KFold).

Although this was not explicitly required in the assignment guide, it was added to improve model stability and obtain a more reliable estimate of performance.

Ridge Regression was selected because it applies L2 regularization, which reduces overfitting by penalizing large coefficient values. This is particularly useful when dealing with multiple encoded features.

In addition, KFold cross-validation (5 splits) was used to ensure the model was evaluated across different subsets of the dataset instead of relying on a single train-test split. This provides a more robust and realistic performance measure.

2. Comparison of Models

From cross-validation results:

Linear Regression: R² ≈ 0.537
Ridge Regression: R² ≈ 0.539
Random Forest: R² ≈ 0.707

During cross-validation, Random Forest showed the strongest performance, capturing more complex patterns in the data.

However, on the test set:

Linear Regression: R² ≈ 0.541
Ridge Regression: R² ≈ 0.542
Random Forest: R² ≈ 0.479

This shows a clear difference between validation and final test performance. While Random Forest performed well during training folds, it did not generalize as effectively to unseen data in this case.

Sanity Check Observations

In individual predictions, Linear and Ridge models produced smoother and more consistent results. Random Forest predictions were more variable and sometimes deviated further from actual values.

This suggests that the model may have captured patterns that are specific to training subsets rather than general relationships.

3. Understanding Random Forest

Random Forest is an ensemble learning method that builds multiple decision trees and combines their outputs.

Instead of relying on one model, it:

Trains many decision trees on different random samples of data
Selects random subsets of features at each split
Averages all predictions to produce the final output

This approach reduces variance and improves stability compared to a single decision tree.

The key idea is that while individual trees may overfit, combining many trees results in a more robust and generalized model.

4. Metrics Discussion
Linear Regression
R²: 0.541
MAE: 0.361
RMSE: 0.466

Ridge Regression
R²: 0.542
MAE: 0.360
RMSE: 0.466
Random Forest

R²: 0.479
MAE: 0.257
RMSE: 0.497

Interpretation

R² (best: Linear & Ridge)
Linear-based models explain slightly more variance on unseen data compared to Random Forest.
MAE (best: Random Forest)
Random Forest has lower average error, meaning predictions are closer on average, even if variance explanation is weaker.
RMSE (worst: Random Forest)
Higher RMSE indicates occasional large prediction errors.
Key Insight

Linear and Ridge models are more stable and consistent for this dataset, while Random Forest is more flexible but less reliable here, likely due to the small dataset size.

5. Final Findings 

Based on the results, Ridge Regression is the preferred model for this dataset.

Although Linear Regression performs almost the same, Ridge is slightly more robust due to its regularization, which helps control overfitting and improves generalization.

Random Forest, despite showing strong cross-validation performance, does not generalize as well on the test data. This inconsistency makes it less reliable for final prediction in this case.

Overall, simpler linear models performed better because the relationships in the dataset appear mostly linear rather than highly complex or non-linear.