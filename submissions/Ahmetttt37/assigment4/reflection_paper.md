# Reflection Paper – Car Price Prediction

## 1. What Did You Implement?

In this assignment, I built two machine learning regression models to predict car prices using the cleaned dataset that I prepared in Assignment Three. I first loaded the dataset into Python using Pandas and separated the target variable (`Price`) from the input features. Since machine learning models require numerical data, categorical variables were encoded before training. The dataset was then divided into training data (80%) and testing data (20%) using `train_test_split` with `random_state=42` to ensure reproducible results.

After preparing the data, I trained two different regression models: Linear Regression and Random Forest Regression. Linear Regression learned a linear relationship between the features and the car price, while Random Forest Regression used many decision trees to model more complex relationships. After training both models, I evaluated their performance using R², MAE, MSE, and RMSE. Finally, I performed a sanity check by selecting one test sample and comparing the actual car price with the predictions from both models.

## 2. Comparison of Models

During the sanity check, both models predicted a price that was reasonably close to the actual value, but the Random Forest model produced a prediction that was closer to the real price. The Linear Regression model sometimes overestimated or underestimated the price because it assumes a linear relationship between the features and the target.

The Random Forest model gave more realistic predictions because it can capture complex patterns and interactions between variables such as vehicle age, mileage, engine size, and brand. Since car prices are influenced by many factors that do not always have a simple linear relationship, Random Forest was better able to represent the data.

## 3. Understanding Random Forest

Random Forest is an ensemble machine learning algorithm that combines many decision trees to make predictions. Instead of relying on a single decision tree, the algorithm builds multiple trees using different random samples of the training data and different subsets of features.

For regression problems, each decision tree predicts a numerical value, and the Random Forest model calculates the final prediction by averaging the outputs of all the trees. This approach reduces overfitting, improves prediction accuracy, and makes the model more stable than a single decision tree.

## 4. Metrics Discussion

The Random Forest model achieved a higher R² score and lower MAE and RMSE values than the Linear Regression model. A higher R² indicates that the model explains more of the variation in car prices, while lower MAE and RMSE values indicate smaller prediction errors.

These results show that Linear Regression is simple, fast, and easy to interpret, but it may not perform well when the relationship between variables is not purely linear. In contrast, Random Forest can learn more complex patterns and generally provides more accurate predictions, although it requires more computation and is less interpretable than Linear Regression.

## 5. My Findings

Based on the results of this assignment, I prefer the Random Forest model for car price prediction. It consistently produced more accurate predictions and achieved better evaluation metrics than Linear Regression. Because car prices depend on many interacting factors, a model that can capture nonlinear relationships is more suitable for this problem.

However, I also learned that Linear Regression remains an important baseline model. It is easy to implement, trains quickly, and provides interpretable results. In practice, I would use Linear Regression as a starting point and then compare it with more advanced models such as Random Forest. Overall, this assignment improved my understanding of regression, model evaluation, and the importance of selecting an appropriate algorithm for a real-world prediction task.
