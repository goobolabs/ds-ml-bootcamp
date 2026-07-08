# Part A — Theory: Regression in Machine Learning


## 1.  Introduction to Regression

    Regression is a method in machine learning used to predict continuous numbers. It helps us understand the relationship between input data (features) and an output value (target).

For example, regression can be used to predict:

- House price based on size and location
- Temperature based on weather conditions

### Regression vs Classification

Regression predicts numbers, while classification predicts categories.

- Regression example: Predicting the price of a house
- Classification example: Predicting if a student will pass or fail

So, regression gives a value, and classification gives a label.


## 2. Types of Regression

### 2.1 Linear Regression
    Linear regression is the simplest type. It draws a straight line between input and output.

How it works:
    It finds the best straight line to fit the data:
    y = mx + c

Example:
Predicting salary based on years of experience.

Advantages:
- Easy to understand
- Fast to train
- Works well for simple problems

Limitations:
- Only works well for straight-line relationships
- Not good for complex data


### 2.2 Multiple Linear Regression

    This is an extension of linear regression. It uses more than one input variable.

How it works:
It uses several features:
y = b0 + b1x1 + b2x2 + ...

Example:
Predicting house price using size, location, and number of rooms.

Advantages:
- More realistic for real problems
- More accurate than simple linear regression

Limitations:
- Can become complex
- Features may affect each other (multicollinearity)


### 2.3 Polynomial Regression

    Polynomial regression is used when data is not straight. It fits a curved line.

How it works:
It adds powers of x (x², x³, etc.) to create a curve.

Example:
Predicting growth of a business over time.

Advantages:
- Works well with non-linear data
- More flexible

Limitations:
- Can easily overfit
- Too complex if degree is high



## 3. Regression Metrics

    To know how good a model is, we use error metrics.

#### MAE (Mean Absolute Error)

It shows the average difference between real and predicted values.

#### MSE (Mean Squared Error)

It squares errors, so big mistakes are punished more.

#### RMSE (Root Mean Squared Error)

Same as MSE but in original units, so it is easier to understand.

#### R² (R-squared)

It shows how well the model explains the data.
- 1 = perfect prediction
- 0 = poor model



#### Regression Metrics Comparison

| Metric | Meaning | Units | Big Error Impact |
|--------|--------|------|------------------|
| MAE | Average error | Same as data | Low |
| MSE | Squared error | Squared units | High |
| RMSE | Average error (clear scale) | Same as data | High |
| R² | Model accuracy | None | Medium |


## 4. Underfitting and Overfitting

### Underfitting

    Underfitting happens when the model is too simple. It cannot learn the pattern in the data, so it performs poorly.

### Overfitting

    Overfitting happens when the model learns the training data too well, including noise. It works well on training data but poorly on new data.

#### Why Overfitting Happens

In polynomial regression, overfitting happens when the curve becomes too complex and follows every small change in the data.

How to Prevent Overfitting
- Use simpler models
- Use more data
- Apply regularization (L1 or L2)



## 5. Real-World Case Study

#### House Price Prediction
A real example of regression is predicting house prices in real estate.

#### Goal:
To estimate house prices based on features like size, rooms, and location.

#### Data Used:
- House size
- Number of rooms
- Location
- Age of house
- Past prices

#### Model Used:
Multiple linear regression is commonly used because many factors affect house price.

#### Results:
- Bigger houses cost more
- Location strongly affects price
- Age of house can reduce price

    This model helps real estate companies estimate prices quickly and make better decisions.


### References
- James et al. (2021). Introduction to Statistical Learning
- Géron (2022). Hands-On Machine Learning
- IBM Machine Learning Guide (2024)



