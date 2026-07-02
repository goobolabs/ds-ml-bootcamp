# Reflection Paper – Car Price Prediction

## 1. What did you implement?

In this assignment, I built two regression models to predict car prices using the cleaned dataset from Assignment Three. First, I loaded the cleaned dataset and prepared the features and target variable. Then, I split the data into training and testing sets using an 80/20 ratio. After that, I trained a Linear Regression model and a Random Forest Regressor. Finally, I evaluated both models using R², MAE, MSE, and RMSE metrics and performed a sanity check by comparing predictions with the actual car price.

---

## 2. Comparison of Models

The predictions from the two models were different. Linear Regression produced predictions based on a linear relationship between the features and the target, while Random Forest captured more complex patterns in the data. During the sanity check, the Random Forest prediction was closer to the actual car price, making it more realistic.

---

## 3. Understanding Random Forest

Random Forest is an ensemble machine learning algorithm that combines many decision trees. Each tree makes its own prediction, and the final prediction is the average of all trees. This approach reduces overfitting and usually provides more accurate and stable predictions than a single decision tree.

---

## 4. Metrics Discussion

After evaluating both models, Random Forest achieved a higher R² score and lower MAE and RMSE values than Linear Regression. This indicates that Random Forest predicted car prices more accurately and made smaller errors. Linear Regression is simple and easy to understand, but it may not perform well when the relationship between variables is not purely linear.

---

## 5. My Findings

I prefer the Random Forest model for car price prediction because it provides better accuracy and handles complex relationships between features. Although Linear Regression is faster and easier to interpret, Random Forest produced more reliable predictions on this dataset. This assignment helped me understand the importance of comparing multiple models before selecting the best one for a machine learning problem.