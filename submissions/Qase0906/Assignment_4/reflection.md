# Part C — Reflection Paper

## 1. What did I implement?

In this assignment, I implemented two machine learning models to predict car prices using a cleaned dataset from Assignment Three. The dataset was preprocessed to handle missing values, incorrect entries, and categorical encoding.

I trained two regression models:

- Linear Regression
- Random Forest Regressor

The dataset was split into training and testing sets. The models were trained using X_train and y_train, and predictions were generated using X_test. Finally, I evaluated the models using performance metrics such as R², MAE, MSE, and RMSE to measure accuracy and error levels.


## 2. Comparison of Models

During the sanity check (individual prediction comparison), the models produced different results:

- Actual price: $7,009
- Linear Regression prediction: $5,476
- Random Forest prediction: $6,138

The Random Forest model produced a value closer to the actual price compared to Linear Regression in this case. This suggests that Random Forest captured the patterns in the dataset slightly better for individual predictions.

However, both models still underestimated the actual value, indicating that the dataset may have complex relationships or missing influential features that are not fully captured by the models.


## 3. Understanding Random Forest

Random Forest is an ensemble machine learning algorithm that combines multiple decision trees to make predictions.

Instead of relying on a single decision tree, Random Forest:

- Builds many decision trees using different subsets of the training data
- Each tree makes its own prediction
- The final output is calculated by averaging all predictions (for regression)

This method improves accuracy and reduces overfitting because it combines the strength of multiple models rather than depending on a single one. As a result, Random Forest is more flexible and can capture non-linear relationships in data.


## 4. Metrics Discussion

The performance results were:

Linear Regression:
- R²   : 0.4064
- MAE  : 1,444.09
- MSE  : 3,950,658.98
- RMSE : 1,987.63

Random Forest:
- R²   : 0.3285
- MAE  : 1,177.43
- MSE  : 4,469,150.33
- RMSE : 2,114.04

Linear Regression achieved a higher R² score, meaning it explained more variance in the dataset. It also had a lower RMSE, indicating better performance in handling large prediction errors.

However, Random Forest had a lower MAE, meaning it made smaller average errors in general predictions. This shows that Random Forest performs better in average accuracy, while Linear Regression is more consistent in explaining overall patterns.


## 5. Findings

Based on the results, I would prefer Linear Regression as the primary model for this dataset because it achieved a higher R² score and lower RMSE, meaning it better explains the relationship between features and car prices overall.

However, Random Forest is still valuable because it produced closer predictions in some individual cases and has the ability to capture non-linear relationships. With further tuning and feature engineering, Random Forest could potentially outperform Linear Regression.



