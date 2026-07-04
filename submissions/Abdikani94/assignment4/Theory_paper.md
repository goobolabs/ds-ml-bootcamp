# Assignment Four  Part A: Regression Theory

## 1. Introduction to Regression

Regression is a type of machine learning where the model predicts a number, Classification is the opposite: it predicts a label or group.

Example of regression: predicting a car's price.
Example of classification: deciding if a car passed or failed inspection.

## 2. Types of Regression

**Linear Regression** uses one feature to draw a straight line through the data and predict the target. Simple example: predicting house price from size alone. It's easy to understand but only works well if the relationship is actually a straight line.

**Multiple Linear Regression** is the same idea but with several features at once, like mileage, age, and accidents together. It gives a better picture than one feature alone, but breaks down if the features are strongly related to each other.

**Polynomial Regression** bends the line into a curve so it can fit data that isn't straight, like how a car loses value fast at first and then slows down. The problem is it can curve too much and overfit if you're not careful.

## 3. Regression Metrics

| Metric | Meaning | Same Unit as Target? | Punishes Big Errors |
|---|---|---|---|
| MAE | Average size of the error | Yes | No |
| MSE | Average of squared errors | No (squared) | Yes |
| RMSE | Square root of MSE | Yes | Yes |
| R² | How much of the variation the model explains (0 to 1) | No | No |

Basically: MAE is the easy-to-read average mistake. MSE and RMSE punish big mistakes harder. R² tells you how well the model fits overall.

## 4. Underfitting and Overfitting

Underfitting is when the model is too simple and gets things wrong even on the training data. Overfitting is when the model memorizes the training data, including its noise, and then fails on new data. Polynomial regression overfits easily because a high-degree curve can twist itself to match every training point.

Ways to avoid overfitting:
- Use cross-validation instead of trusting one train/test split
- Use regularization (Ridge/Lasso)
- Don't make the model more complex than the data needs

## 5. Real-World Case Study

A good example is Zillow's home price estimator ("Zestimate"). It uses regression models, including linear regression and tree-based models like Random Forest, trained on past home sales, square footage, location, and number of rooms.

Goal: estimate a fair price for a house.
Data: historical sales and property details.
Model type: multiple linear regression and ensemble (tree-based) regression.
Result: tree-based models usually do better because house prices depend on features that interact in non-linear ways, location especially. This matches what I saw in my own car price project — simple linear models are a good starting point, but more flexible models can pick up patterns linear regression misses.
