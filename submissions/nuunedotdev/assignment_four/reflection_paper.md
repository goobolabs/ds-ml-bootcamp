# PART C - Reflection Paper

## Q1 - 

The dataset was prepared and then divided into two parts: one for training the model and another for testing its performance.Usually, 80% of the data was used for training and 20% for testing. After preparing and converting the necessary categorical variables, a Linear Regression model was built using the training data to understand how car features like year, mileage, engine size, fuel type, and transmission relate to the car's price. The model that had been trained was then used to forecast prices for the test data.
A Random Forest Regressor was trained using the same preprocessed training and testing datasets. This model creates many decision trees using different parts of the training data and then combines the results by taking the average of all the predictions. Random Forest is good at finding complicated, curved connections between car features and their prices, which makes it stronger than a basic straight-line model.


## Q2 -

During the sanity check, both models gave somewhat reasonable price predictions, but there were some clear differences.

The predictions showed a straightforward connection where the price changed in a straight line based on the input features. The model worked okay, but it sometimes gave prices that were too high or too low, especially for pricey or unique cars. This is because Linear Regression assumes that the connection between the features and the price is straight-line shaped.
The predictions using Random Forest Regression were mostly close to what was expected based on market prices. The model dealt with how different factors like mileage, age, engine size, and fuel type affect each other, which helped make the predictions more accurate and reliable. It was also less influenced by the tricky patterns in the data.

More realistic model:
The Random Forest Regression model provided more realistic results because car prices are affected by complicated, non-linear factors that a simple linear model can't fully explain. By using predictions from many decision trees, Random Forest lowers prediction errors and handles different types of data better, which makes its price estimates more trustworthy compared to Linear Regression.

## Q3 - 

Random Forest is a machine learning method that uses a group of decision trees together to create a more accurate prediction. Instead of using just one decision tree, it creates many trees by using different groups of data and different sets of features each time. This is why it's called a forest of decision trees.


## Q4 - 

| Metric       | Linear Regression    | Random Forest    | Better Model      |
|--------------|------------------    |----------------- |-----------------  |
| MAE          |  1,428.05            |  1,204.81        | Random Forest     |
| RMSE         | 1,937.86             |  2,198.01        | Linear Regression |
| R² Score     |  43.58%              |  27.42%          | Linear Regression |


Linear Regression

Strengths:
    Achieved the highest R² Score (43.58%), explaining more variation in car prices.
    Produced the lowest RMSE (1,937.86), meaning it made fewer large prediction errors.
    Performed better overall on this dataset.
Weaknesses:
    Had a higher MAE than Random Forest, meaning its average prediction error was slightly larger.

Random Forest Regression

Strengths:
    Achieved the lowest MAE (1,204.81), meaning its predictions were closer to the actual prices on average.
Weaknesses:
    Had a lower R² Score (27.42%), indicating it explained less variation in the data.
    Had the highest RMSE (2,198.01), showing that it made some large prediction errors that negatively affected its overall performance.


## Q5 - 

Overall, the results suggest that Linear Regression is more suitable for this cleaned dataset because it provides a better overall fit and more consistent predictions. While Random Forest generally performs well on complex datasets, its lower R² score (27.42%) and higher RMSE (2,198.01) indicate that it struggled with some observations in this case. Therefore, I would choose Linear Regression as the preferred model for predicting car prices because it produced more reliable and stable predictions on this dataset.


```bash
ABDULKADIR HASSAN
```