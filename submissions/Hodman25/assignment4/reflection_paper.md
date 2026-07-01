# 1. What I Implemented

In this assignment, I implemented two machine learning models—Linear Regression and Random Forest Regressor—to predict car prices using a cleaned dataset from Assignment Three.

After preprocessing the dataset (handling missing values, encoding categorical features, and scaling where necessary), I split the data into training and testing sets. I then trained:
- Linear Regression model using ***sklearn.linear_model.LinearRegression***
- Random Forest model using ***sklearn.ensemble.RandomForestRegressor***

Both models were trained on the same features to ensure a fair comparison. After training, I evaluated them using test data and performed a sanity check by comparing predicted prices with actual values for selected samples.

# 2. Comparison of Models
To perform a sanity check, I selected one row from the testing dataset and compared the actual price with the predictions from both models.

| Value                        |      Price |
| ---------------------------- | ---------: |
| Actual Price                 | **$3,622** |
| Linear Regression Prediction | **$4,614** |
| Random Forest Prediction     | **$3,630** |

The Linear Regression model overestimated the price by almost $1,000, while the Random Forest prediction was only $8 away from the actual value.

Although Random Forest produced a much more realistic prediction for this individual example, Linear Regression performed better overall across the entire testing dataset according to the evaluation metrics.

# 3. Understanding Random Forest

Random Forest is an ensemble learning algorithm that combines many decision trees to make predictions.

Instead of relying on one decision tree, Random Forest builds many trees using different random samples of the training data. Each tree predicts a value independently, and the final prediction is obtained by averaging the predictions from all trees.

Because it combines many trees, Random Forest usually reduces overfitting and can model complex, non-linear relationships that Linear Regression cannot capture. This often leads to more realistic predictions for individual observations.

# 4.  Metrics Discussion

| Metric   | Linear Regression | Random Forest |
| -------- | ----------------: | ------------: |
| **R²**   |         **0.436** |         0.274 |
| **MAE**  |             1,428 |     **1,205** |
| **RMSE** |         **1,938** |         2,198 |


### R² (Coefficient of Determination):

Linear Regression achieved the higher R² value ***(0.436)****, meaning it explained more of the variation in car prices.
Random Forest explained less of the overall variance ***(0.274)***.

### MAE (Mean Absolute Error):

Random Forest had the lower MAE (1,205), meaning its average prediction error was smaller.

### RMSE (Root Mean Squared Error):

Linear Regression had the lower RMSE (1,938), indicating it handled large prediction errors better than Random Forest.

Overall, Linear Regression produced better overall performance according to R² and RMSE, while Random Forest produced a smaller average error (MAE) and gave a more accurate prediction in the sanity check.

# Findings
Based on the evaluation results, Linear Regression is the stronger model overall for this dataset because it achieved the highest R² score and the lowest RMSE. These metrics indicate that it explains more of the variation in car prices and makes more consistent predictions across the testing data.

However, the Random Forest model produced a much more accurate prediction in the sanity check, predicting $3,630 compared to the actual price of $3,622. This suggests that Random Forest can capture complex patterns that Linear Regression may miss when predicting individual cars.

Overall, I would choose Linear Regression as the preferred model for this assignment because it demonstrated better overall performance across the entire dataset. At the same time, the Random Forest results show that ensemble learning can produce highly realistic predictions for certain cases and may perform better if further tuning of its hyperparameters is performed.
