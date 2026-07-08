# Reflection Paper

## Assignment Four – Regression

### 1. What did you implement?

In this assignment, I implemented two regression models to predict car prices using the cleaned dataset from Assignment Three. First, I loaded the dataset and prepared the features (X) and the target variable (y). The target variable was **Price**, while all other columns except **Price** and **LogPrice** were used as input features.

Next, I split the dataset into 80% training data and 20% testing data using `random_state=42`. I then trained two machine learning models: Linear Regression and Random Forest Regressor. After training, I used both models to predict car prices on the test dataset. Finally, I evaluated their performance using R², MAE, MSE, and RMSE.

---

## 2. Comparison of Models

During the sanity check, both models predicted values that were reasonably close to the actual car price. However, the predictions were not exactly the same because the two models learn differently.

Linear Regression predicts using a linear relationship between the features and the target value. Random Forest predicts by combining the results of many decision trees. Because of this, Random Forest usually produces predictions that are closer to the actual prices, especially when the relationship between features and price is more complex.

Based on the evaluation metrics, the model with the higher R² score and lower error values provides more realistic predictions.

---

## 3. Understanding Random Forest

Random Forest is an ensemble machine learning algorithm that combines many decision trees to make predictions. Instead of depending on only one tree, it builds multiple trees using different samples of the training data.

Each tree predicts a value, and the final prediction is calculated by averaging the predictions from all the trees. This approach usually improves accuracy and reduces the effect of individual prediction errors.

---

## 4. Metrics Discussion

The evaluation metrics helped compare the performance of the two regression models.

* **R²** measures how well the model explains the variation in car prices.
* **MAE** shows the average prediction error.
* **MSE** gives a larger penalty to large prediction errors.
* **RMSE** measures prediction error in the same units as the car prices.

The model with the higher R² score and lower MAE and RMSE values performed better because its predictions were closer to the actual prices.

---

## 5. My Findings

From this assignment, I learned how regression models can be used to predict continuous numerical values such as car prices. I also learned that different regression algorithms can produce different prediction accuracy depending on the dataset.

Personally, I prefer the Random Forest model for price prediction because it can capture more complex relationships between the features and the target variable. Although Linear Regression is simple, fast, and easy to understand, Random Forest often provides better prediction accuracy when the data contains non-linear patterns.

Overall, this assignment improved my understanding of regression, model evaluation, and practical machine learning using Python and Scikit-learn.
