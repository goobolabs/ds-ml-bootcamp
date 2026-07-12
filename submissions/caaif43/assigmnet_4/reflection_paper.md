

# Introduction

This assignment gave me practical experience in applying regression algorithms to predict car prices using machine learning. I trained two different regression models, evaluated their performance, and compared their prediction accuracy using several evaluation metrics.

---

# 1. What Did You Implement?

I implemented two machine learning regression models: Linear Regression and Random Forest Regressor. I used the cleaned car dataset from Assignment Three. First, I loaded the dataset, selected the Price column as the target variable, and used the remaining columns as input features.

Then, I split the dataset into training and testing sets using an 80%–20% ratio. After training both models, I evaluated them using R², MAE, MSE, and RMSE. Finally, I performed a sanity check by comparing the actual price of one car with the predictions from both models.

---

# 2. Comparison of Models

The two models produced different prediction values. Linear Regression predicted prices based on a linear relationship between the variables, while Random Forest captured more complex patterns by combining many decision trees.

The Random Forest model produced more realistic predictions because it can learn nonlinear relationships and reduce prediction errors.

---

# 3. Understanding Random Forest

Random Forest is an ensemble learning algorithm that combines many decision trees to make predictions. Each tree is trained using a different random sample of the data. The final prediction is obtained by averaging the predictions from all the trees.

This method improves prediction accuracy and reduces overfitting compared to using a single decision tree.

---

# 4. Metrics Discussion

The Random Forest model achieved better evaluation results than Linear Regression. It had a higher R² value and lower MAE, MSE, and RMSE values.

A higher R² means that the model explains more variation in car prices, while lower error values indicate more accurate predictions. These results show that Random Forest is more effective for predicting car prices.

---

# 5. My Findings

Based on the results, I prefer the Random Forest model because it provides more accurate and reliable predictions. Car prices depend on many factors, including mileage, age, accident history, and location. Random Forest can model these complex relationships better than Linear Regression.

This assignment improved my understanding of regression, model evaluation, and machine learning workflows. I also learned the importance of selecting the appropriate algorithm based on the characteristics of the data.

---
