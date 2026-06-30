# Reflection Paper

## 1. What did I implement?
 The models used were Linear Regression and Random Forest Regression. The dataset contained several features such as house size, number of rooms, location, house prices and other.
---
## 2. Comparison of Models
From the test results and sanity check, the predictions from both models were not the same.

Linear Regression gives straight-line predictions, so it sometimes misses complex patterns.

Random Forest gave predictions closer to the actual price in most cases because it can handle more complex relationships.

Random Forest produced more realistic results on this training. 
---
## 3. Understanding Random Forest

Random Forest is a machine learning algorithm based on an ensemble learning method. It builds multiple decision trees during training and combines their predictions to produce a final result.

Instead of relying on a single decision tree, Random Forest creates many trees using different subsets of the training data. Each tree learns patterns independently. When making a prediction, each tree provides a predicted value, and the final prediction is calculated by averaging all these outputs.

This method helps reduce overfitting and improves the accuracy and stability of predictions. Because of this, Random Forest is often more powerful than a single decision tree or simple linear models.
---
## 4. Metrics Discussion
I used these metrics:
  R² → shows how well the model explains the data  
  MAE → average error  
  RMSE → error size in real units  
The better model is the one with:
  Higher R²  
  Lower MAE and RMSE  
Random Forest performed better based on these metrics.
---

## 5. Final Findings
Random Forest is better for this task because house prices depend on many factors and are not purely linear.

However, Linear Regression still has some advantages. It is simpler, faster to train, and easier to interpret. This makes it useful for understanding the basic relationship between features and house prices.

Overall, for this project I would prefer using Random Forest for price prediction models, because it provides better predictive performance and handles complex data patterns more effectively.
