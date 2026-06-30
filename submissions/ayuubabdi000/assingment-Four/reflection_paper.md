# Reflection – Paper (Car Price Prediction)


In this assignment, I built a machine learning system to predict car prices using the cleaned dataset from Assignment 3. I split the dataset into training and testing sets (80% training, 20% testing). Then I trained two models: **Linear Regression** and **Random Forest Regressor**. After training, I used both models to predict car prices on the test data and evaluated them using MAE, MSE, RMSE, and R². I also performed a single-row sanity check to compare predicted values with the actual price.

---

## Comparison of Models
In the sanity check, the results were:

- Actual Price: **$7,009**
- Linear Regression: **$7,406**
- Random Forest: **$7,612**

Linear Regression was slightly closer to the real value in this example. Random Forest predicted a higher value, which shows it may have overestimated in this case.

---

## Understanding Random Forest
Random Forest is an ensemble machine learning model made of many decision trees. Each tree makes a prediction, and the final output is the **average of all tree predictions**. This method improves stability and reduces overfitting compared to a single decision tree. It is usually strong for complex datasets because it can learn non-linear relationships.

---

## Metrics Discussion

### Linear Regression
- R²: -0.012  
- MAE: 7330  
- RMSE: 24724  

### Random Forest
- R²: -0.097  
- MAE: 7258  
- RMSE: 25747  

From these results:
- Random Forest had slightly lower MAE (better average error)
- Linear Regression had better R² and RMSE
- Both models had negative R², meaning they performed worse than predicting the average value

This shows that both models struggled to capture strong patterns in the dataset.

---

##  Findings
In this assignment, I found that neither model performed very well overall, as shown by the negative R² values. This indicates that the dataset is difficult to model or that important features may still be missing. However, Linear Regression performed slightly better in terms of R², RMSE, and the sanity check prediction.

Even though Random Forest is usually a stronger model, it did not perform better in this case. This may be due to noise in the data or limited useful features. Overall, Linear Regression gave more stable results for this dataset, but both models need better feature engineering or more data to improve performance.