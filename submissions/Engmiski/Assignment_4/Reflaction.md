# Assignment Four – Part C: Reflection Paper

## 1. What Did You Implement?

In this assignment, I built two machine learning regression models to predict car prices using the cleaned dataset created in Assignment Three. I first loaded the dataset and selected **Price** as the target variable while using the remaining features, except **LogPrice**, as input variables. The dataset was then divided into training and testing sets using an 80/20 split. Finally, I trained both a Linear Regression model and a Random Forest Regressor to learn the relationship between the car features and their prices.

## 2. Comparison of Models

During the sanity check, both models produced predictions that were close to the actual car price. However, the Random Forest model generally produced predictions that were closer to the true value than the Linear Regression model. This happened because Random Forest can capture more complex relationships in the data, while Linear Regression assumes a simple linear relationship.

## 3. Understanding Random Forest

Random Forest is an ensemble machine learning algorithm that combines many decision trees to make predictions. Each tree is trained using a different random sample of the training data. For regression problems, every tree predicts a value, and the final prediction is calculated by averaging the predictions from all trees. This approach improves prediction accuracy and reduces overfitting compared to using a single decision tree.

## 4. Metrics Discussion

The Random Forest model achieved a higher R² score and lower MAE and RMSE values than the Linear Regression model. A higher R² indicates that the model explains more of the variation in car prices, while lower error values show that its predictions are closer to the actual prices. Linear Regression performed well but was less accurate because it cannot model complex patterns as effectively as Random Forest.

## 5. My Findings

Based on the results of this assignment, I believe that Random Forest is the better model for car price prediction. It produced more accurate predictions and achieved better evaluation metrics than Linear Regression. Its ability to model non-linear relationships makes it suitable for real-world datasets where many factors influence prices.

Overall, this assignment helped me understand how regression models are trained, evaluated, and compared. I also learned the importance of evaluation metrics such as R², MAE, MSE, and RMSE when selecting the best model for a prediction task.
