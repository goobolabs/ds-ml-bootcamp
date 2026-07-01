# Assignment 4 – Reflection Paper

## 1. What did you implement?

In this assignment, I built two machine learning regression models to predict car prices using the cleaned dataset from Assignment Three (`clean_car_dataset.csv`). First, I loaded the dataset with Pandas and selected **Price** as the target variable (`y`). The remaining columns, except `Price` and `LogPrice` (when available), were used as the input features (`X`).

Next, I split the dataset into **80% training data** and **20% testing data** using `train_test_split` with `random_state=42`. I trained two regression models: **Linear Regression** and **Random Forest Regressor** with `n_estimators=100` and `random_state=42`. After training, I evaluated both models using R², MAE, MSE, and RMSE, and compared their predictions on one sample from the test dataset.

## 2. Comparison of Models

In the sanity check, the actual car price was **4379.0**.

* **Linear Regression Prediction:** 6203.41
* **Random Forest Prediction:** 4259.64

The Random Forest prediction was much closer to the actual price than the Linear Regression prediction. This indicates that the Random Forest model produced more realistic and accurate results. It was able to capture complex relationships in the data that Linear Regression could not.

## 3. Understanding Random Forest

Random Forest is a machine learning algorithm that combines many decision trees to make predictions. Instead of relying on a single decision tree, it builds multiple trees using different random samples of the training data. Each tree makes its own prediction, and the final prediction is calculated by averaging the predictions of all the trees.

This ensemble approach reduces overfitting and usually provides more accurate and stable predictions than using a single decision tree.

## 4. Metrics Discussion

The evaluation results were:

### Linear Regression

* **R²:** 0.8752
* **MAE:** 978.43
* **RMSE:** 1378.43

### Random Forest

* **R²:** 0.9922
* **MAE:** 123.61
* **RMSE:** 344.14

Random Forest achieved a much higher R² score and much lower error values (MAE and RMSE). This means it explained more of the variation in car prices while making smaller prediction errors.

Linear Regression is simple, fast, and easy to understand, but it assumes a linear relationship between the features and the target. Random Forest is more flexible because it can model complex and non-linear relationships, although it requires more computational resources.

## 5. My Findings

Based on the results of this assignment, I prefer the **Random Forest Regressor** for car price prediction. It consistently produced more accurate predictions and achieved significantly better evaluation metrics than Linear Regression. The sanity check also showed that its prediction was very close to the actual car price.

Overall, this assignment helped me understand that choosing the right machine learning model is very important. While Linear Regression is useful as a simple baseline model, Random Forest performed much better for this dataset because it can learn more complex patterns and provide more reliable predictions.
