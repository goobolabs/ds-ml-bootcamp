# Car Price Prediction Using Linear Regression and Random Forest

## What I Implemented

In this project, I developed two machine learning regression models to predict car prices using my cleaned Assignment Three dataset. Before training the models, I performed data preprocessing and feature engineering to improve prediction performance.

The target variable was **Price**, while the input features included the car's manufacturing year, odometer reading, number of doors, accident history, location, and several engineered features. The engineered features included **Car_age**, **Km_Per_Year**, **Age_x_Odometer**, **Km_Per_Accident**, and **Heavy_Use**.

The dataset was divided into training and testing sets using an 80/20 split. I trained both a **Linear Regression** model and a **Random Forest Regressor** using the training data and evaluated their performance on the testing data.

---

# Comparison of Models

To verify that the models were working correctly, I performed a sanity check by comparing their predictions with the actual car prices. Both models produced reasonable predictions, but their accuracy differed.

Initially, Random Forest outperformed Linear Regression on the test dataset. After experimenting with feature engineering, Linear Regression improved considerably, while Random Forest showed a slight decrease in performance. This demonstrates that feature engineering does not always improve every machine learning algorithm.

Overall, **Random Forest produced the most realistic predictions** because it achieved the highest R² score and the lowest prediction errors. Unlike Linear Regression, Random Forest can model complex and non-linear relationships between features, making it more suitable for predicting car prices.

---

# Understanding Random Forest

Random Forest is an ensemble machine learning algorithm that combines many decision trees to make predictions. Instead of relying on a single decision tree, Random Forest creates multiple trees using different random samples of the training data and different subsets of features.

Each decision tree predicts a car price independently. For regression problems, the final prediction is obtained by averaging the predictions from all decision trees. This averaging process reduces variance, improves stability, and generally produces more accurate predictions than a single decision tree.

Because Random Forest can automatically learn complex relationships and interactions between variables, it usually requires less manual feature engineering than Linear Regression.

---

# Metrics Discussion

The final evaluation results were:

| Model             |    R² |  MAE | RMSE |
| ----------------- | ----: | ---: | ---: |
| Linear Regression | 0.265 | 1583 | 2211 |
| Random Forest     | 0.321 | 1189 | 2126 |

Random Forest achieved the highest R² score and the lowest MAE and RMSE values, making it the best-performing model overall.

The higher R² score indicates that Random Forest explained more variation in car prices than Linear Regression. The lower MAE and RMSE values show that its predictions were closer to the actual prices on average.

However, the training and testing scores also revealed that Random Forest experienced some overfitting because its training R² was much higher than its testing R². This is likely due to the relatively small dataset (140 records), which makes it easier for the model to memorize the training data.

Linear Regression had lower predictive performance but benefited more from feature engineering. After adding the engineered features, its R² score improved substantially, demonstrating that Linear Regression relies more heavily on meaningful feature engineering.

Overall, this project showed that Random Forest is the stronger model for predicting car prices on this dataset, while Linear Regression remains a useful baseline model that can be improved through carefully designed features. It also demonstrated the importance of evaluating models with multiple metrics and understanding the trade-offs between model complexity, feature engineering, and generalization.
