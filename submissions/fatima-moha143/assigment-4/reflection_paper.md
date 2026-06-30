# Car Price Prediction Using Linear Regression and Random Forest

## What I Implemented

In this assignment, I developed a machine learning project to predict car prices using a cleaned car dataset. The target variable was **Price**, while all remaining columns except **Price** and **LogPrice** were used as input features. The dataset was divided into training and testing sets using an 80/20 split with `random_state=42` to ensure reproducibility.

Two regression models were trained: **Linear Regression** and **Random Forest Regressor**. The Linear Regression model was trained to learn a linear relationship between the input features and car prices. The Random Forest model was trained using 100 decision trees and combined their predictions to generate a final price estimate.

## Comparison of Models

To compare the models, I performed a sanity check by selecting one sample from the test set and generating predictions from both models. The predicted prices were compared with the actual car price.

The Linear Regression model produced a prediction that was reasonably close to the actual value, but it sometimes underestimated or overestimated prices because it assumes a linear relationship between variables. The Random Forest model generally produced predictions that were closer to the actual price because it can capture more complex patterns in the data.

Based on the sanity check, the Random Forest model provided more realistic results. This is because car prices are influenced by many factors that often interact in non-linear ways, which Random Forest can model more effectively than Linear Regression.

## Understanding Random Forest

Random Forest is an ensemble machine learning algorithm that combines many decision trees to make predictions. Instead of relying on a single decision tree, the algorithm creates multiple trees using different samples of the training data.

For regression tasks, each tree predicts a value, and the final prediction is calculated by averaging the predictions from all trees. This approach reduces overfitting and improves prediction accuracy. Because it combines the knowledge of many trees, Random Forest is often more robust and reliable than a single model.

## Metrics Discussion

The performance of both models was evaluated using R², Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE).

The Random Forest model achieved a higher R² score and lower error values compared to Linear Regression. A higher R² indicates that the model explains more of the variation in car prices, while lower MAE and RMSE values indicate that prediction errors are smaller.

These results suggest that Linear Regression is simple, fast, and easy to interpret, but it may struggle when relationships between variables are complex. In contrast, Random Forest is better at capturing non-linear relationships and interactions between features, leading to more accurate predictions.

## Findings

Based on the evaluation results, I prefer the Random Forest model for car price prediction. The model consistently achieved better performance metrics and produced predictions that were closer to actual car prices. Its ability to learn complex patterns makes it well suited for real-world datasets where relationships between variables are not strictly linear.

Although Linear Regression is easier to understand and computationally efficient, its assumptions can limit predictive performance. Random Forest provides a better balance between accuracy and reliability, making it the preferred choice for this car price prediction task.
