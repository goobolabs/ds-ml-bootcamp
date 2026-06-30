# Reflection Paper: Car Price Prediction

## What did you implement?
In this assignment, I implemented two machine learning models, Linear Regression and Random Forest Regressor, to predict the price of a car based on features such as its age, odometer reading, doors, and location. I used the cleaned dataset from Assignment Three (`clean_car_dataset.csv`). I split the data into 80% training and 20% testing sets using a random state of 42 to ensure reproducibility. I trained both models using Scikit-Learn and evaluated their performance using standard regression metrics.

## Comparison of Models
During my sanity check, the predictions differed slightly between the two models on a specific test sample:
- **Actual Price:** $4,379.00
- **Linear Regression Prediction:** $5,035.77
- **Random Forest Prediction:** $4,507.84

For this particular instance, the **Random Forest** model gave more realistic results because its prediction was closer to the actual price. It was able to better capture the underlying patterns for this specific car without overshooting as much as the linear model.

## Understanding Random Forest
A Random Forest is an ensemble machine learning algorithm. It works by creating a "forest" made up of many individual Decision Trees during the training phase. Each tree is trained on a random subset of the data and a random subset of the features. When making a prediction, the Random Forest asks all of its individual trees for their prediction and then averages those predictions to output a final result. This averaging process makes the model much more robust and less prone to overfitting compared to a single decision tree.

## Metrics Discussion
Based on the metrics obtained from evaluating both models on the test set:
- **Linear Regression:** R²: 0.4357, MAE: 1,423, RMSE: 1,938
- **Random Forest:** R²: 0.2717, MAE: 1,202, RMSE: 2,202

The models presented an interesting split in performance metrics. The Random Forest had a lower Mean Absolute Error (MAE), indicating that its median, typical predictions were closer to the actual values on average. However, Linear Regression had a better R² and a lower Root Mean Squared Error (RMSE). 

This tells us about the strengths and weaknesses of each model:
- The Random Forest is better at getting most typical predictions close (hence the better MAE), but it struggles with large outliers, which heavily penalize the RMSE and drag down its overall R² score.
- The Linear Regression is more stable globally across the dataset. While its typical error is slightly higher, it avoids massive errors that would otherwise inflate the RMSE.

## Your Findings
Given the metrics, I prefer the **Linear Regression** model for predicting car prices in this specific dataset. Even though Random Forest performed better on the single sanity check and had a lower absolute average error (MAE), the higher R² and lower RMSE of Linear Regression indicate that it explains more of the variance in the data and is less severely impacted by large errors. In a real-world scenario like predicting car prices, massive outliers (like vastly mispricing an expensive car) can be very costly, so a model with a lower RMSE and higher stability is generally preferable.
