# Reflection Paper

## 1. What did I implement?
 Before training the models, I loaded the cleaned dataset, selected the input features and the target variable (car price), and divided the data into training and testing sets.

I trained the Linear Regression model to learn the relationship between the car features and the selling price using a linear equation. I also trained the Random Forest Regression model, which combines many decision trees to improve prediction accuracy. After training both models, I evaluated their performance using standard regression metrics and performed a sanity check by predicting the prices of a few sample cars.
---
## 2. Comparison of Models
During the sanity check, both models produced reasonable predictions, but there were noticeable differences. The Linear Regression model tended to predict prices based on a simple linear relationship between the features and the target. Because of this, some predictions were either slightly higher or lower than the expected values.

The Random Forest model produced predictions that were generally closer to the actual car prices. Since it can capture more complex patterns in the data, it handled variations in car features better than Linear Regression. Overall, the Random Forest predictions appeared more realistic because they were less affected by assumptions of a linear relationship.

Random Forest produced more realistic results on this training. 
---
## 3. Understanding Random Forest

Random Forest is an ensemble Machine Learning algorithm that combines the predictions of many decision trees instead of relying on a single tree. Each decision tree is trained using a random sample of the training data and a random subset of features. This creates diversity among the trees.

When making a prediction for a regression problem, every decision tree predicts a value, and the Random Forest calculates the average of all these predictions. Averaging the predictions reduces errors, improves accuracy, and helps prevent overfitting. This makes Random Forest more reliable for datasets that contain complex relationships between variables.
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
I prefer the Random Forest Regression model for predicting car prices. It consistently produced more accurate predictions during the sanity check and achieved better evaluation metrics than Linear Regression. The ability to combine many decision trees allowed it to capture complex relationships within the dataset.

Overall, for this project I would prefer using Random Forest for price prediction models, because it provides better predictive performance and handles complex data patterns more effectively.
