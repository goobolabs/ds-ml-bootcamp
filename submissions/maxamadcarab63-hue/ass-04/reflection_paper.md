# Car Price Prediction Using Linear Regression and Random Forest

## What I Implemented

In this project, I implemented two machine learning regression models, **Linear Regression** and **Random Forest Regressor**, to predict car prices using a cleaned car dataset. I first loaded the dataset using Pandas and separated the features (independent variables) from the target variable (`Price`). I removed the `Price` and `LogPrice` columns from the feature set and used `Price` as the prediction target.

Next, I divided the dataset into training and testing sets using an 80/20 train-test split. This allowed me to train the models on one portion of the data and evaluate their performance on unseen data.

For the first model, I trained a **Linear Regression** model using Scikit-learn's `LinearRegression` class. After fitting the model to the training data, I used it to predict car prices on the test set.

For the second model, I trained a **Random Forest Regressor** with 100 decision trees (`n_estimators=100`). After training, I also generated predictions for the test data. Finally, I evaluated both models using several performance metrics including R² Score, Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE). I also performed a single-row prediction (sanity check) to compare each model's prediction with the actual car price.

---

# Comparison of Models

The sanity check compared the predicted price from both models with the actual price of one car from the test dataset. The predictions from Linear Regression and Random Forest were different because each model learns patterns in a different way.

Linear Regression assumes a linear relationship between the input features and the target price. Because of this assumption, its predictions may be less accurate when the relationship between variables is more complex.

Random Forest usually produced more realistic predictions because it can capture non-linear relationships and interactions between multiple features. Instead of relying on one mathematical equation, it combines predictions from many decision trees, making it more flexible and accurate for real-world datasets such as car prices.

---

# Understanding Random Forest

Random Forest is an ensemble machine learning algorithm that combines many decision trees to make a prediction. Instead of building only one tree, it creates multiple trees using different random samples of the training data.

Each decision tree predicts a car price independently. For regression problems like car price prediction, the Random Forest model calculates the average prediction from all the trees. Averaging many trees reduces errors caused by individual trees and helps prevent overfitting.

Because every tree sees slightly different data and different subsets of features, the final prediction is usually more accurate and stable than using a single decision tree.

---

# Metrics Discussion

To evaluate both models, I used four common regression metrics:

- **R² Score** measures how well the model explains the variation in car prices. Higher values (closer to 1) indicate better performance.
- **Mean Absolute Error (MAE)** measures the average prediction error in dollars. Lower values are better.
- **Mean Squared Error (MSE)** gives more weight to large prediction errors. Lower values indicate better performance.
- **Root Mean Squared Error (RMSE)** is the square root of MSE and represents the average prediction error in the original price units. Lower values indicate higher accuracy.

Based on the evaluation results, the model with the **higher R² score** and **lower MAE and RMSE** performed better. In most car price prediction problems, Random Forest typically achieves a higher R² and lower error values because it can model complex relationships between vehicle characteristics and prices.

Linear Regression is simpler, easier to interpret, and faster to train, but its performance decreases when the relationship between features and price is not purely linear.

---

# My Findings

Based on the results of this project, I prefer the **Random Forest Regressor** for predicting car prices. Its predictions were more realistic during the sanity check, and it generally achieved better evaluation metrics than Linear Regression. Since car prices depend on many interacting factors such as age, mileage, brand, engine size, and condition, Random Forest is better suited to capture these complex relationships.

Although Linear Regression is easier to understand and computationally efficient, it cannot model complex patterns as effectively as Random Forest. For practical car price prediction, Random Forest provides higher accuracy and more reliable predictions, making it the better choice for this dataset. However, Linear Regression remains useful as a simple baseline model and for understanding the general relationship between the input features and the target variable.