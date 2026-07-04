
# Part A 


### ) 1
## What is Regression in Machine Learning?

Regression  is a type of supervised learning that predicts continuous outputs (numbers on a scale).
based on one or more input features. Unlike algorithms that classify data into categories, regression estimates a quantity such as price, temperature, salary, or sales.

A regression model learns the relationship between independent variables (features) and a dependent variable (target). After learning this relationship from historical data, it can predict values for new unseen data.

Regression is widely used because many real-world problems involve predicting numbers rather than categories.

---

## Difference Between Regression and Classification

Although both regression and classification belong to supervised learning, they solve different kinds of problems.

Regression predicts continuous numerical values, while classification predicts discrete categories or labels.

For example:

- Predicting the selling price of a used car is a regression problem because the output is a number.
- Predicting whether an email is spam or not spam is a classification problem because the output belongs to predefined classes.

| Regression | Classification |
|------------|---------------|
| Predicts numerical values | Predicts categories |
| Output is continuous | Output is discrete |
| Example: House price prediction | Example: Disease detection |
| Metrics: MAE, MSE, RMSE, R² | Metrics: Accuracy, Precision, Recall |

---

## Real-Life Examples

### Regression Example

A used car dealership wants to estimate the selling price of cars using information such as:

- Manufacturing year
- Mileage
- Number of accidents
- Number of doors


The model predicts the expected selling price.

### Classification Example

A bank wants to determine whether a customer is likely to default on a loan.

Possible outputs are:

- Default
- Not Default

---

### ) 2

# Types of Regression

Regression has several forms depending on the relationship between variables.

---

## 1. Linear Regression

### Basic Idea

Linear Regression models the relationship between one independent variable and one dependent variable using a straight line.

The model attempts to find the best-fitting line that minimizes prediction errors.

General equation:

**Y = β₀ + β₁X + ε**

Where:

- Y = predicted value
- β₀ = intercept
- β₁ = slope
- X = feature
- ε = error

### Real-World Use Case

Predicting house prices using only house size.

### Advantages

- Very easy to understand.
- Fast to train.
- Highly interpretable.
- Works well when relationships are approximately linear.

### Limitations

- Cannot model complex nonlinear relationships.
- Sensitive to outliers.
- Performance decreases when assumptions are violated.

---

## 2. Multiple Linear Regression

### Basic Idea

Multiple Linear Regression extends Linear Regression by using multiple input variables.

Equation:

**Y = β₀ + β₁X₁ + β₂X₂ + ... + βₙXₙ + ε**

Instead of one feature, the model considers many features simultaneously.

### Real-World Use Case

Predicting used car prices using:

- Mileage
- Year
- Location
- Number of doors
- Accident history

### Advantages

- More realistic because many real-world problems depend on multiple variables.
- Usually provides better predictions than simple linear regression.

### Limitations

- Multicollinearity between features may reduce performance.
- Interpretation becomes more difficult as features increase.
- Still assumes a linear relationship.

---

## 3. Polynomial Regression

### Basic Idea

Polynomial Regression models nonlinear relationships by adding polynomial terms such as:

- X²
- X³
- X⁴

Instead of fitting a straight line, it fits a curved relationship.

Example equation:

**Y = β₀ + β₁X + β₂X² + ε**

### Real-World Use Case

Predicting fuel consumption as vehicle speed changes, where the relationship is curved rather than linear.

### Advantages

- Can model nonlinear patterns.
- Often produces better predictions than simple linear regression.

### Limitations

- Easily overfits training data.
- Choosing the correct polynomial degree is challenging.
- Harder to interpret.

---

### ) 3
# Regression Metrics

Regression models are evaluated using numerical error metrics.

---

## Mean Absolute Error (MAE)

MAE measures the average absolute difference between actual and predicted values.

Formula:

**MAE = (1/n) Σ |Actual − Predicted|**

Characteristics:

- Easy to interpret
- Uses the same unit as the target variable
- Less sensitive to large errors

---

## Mean Squared Error (MSE)

MSE calculates the average squared prediction error.

Formula:

**MSE = (1/n) Σ (Actual − Predicted)²**

Characteristics:

- Penalizes large errors heavily.
- Useful during model optimization.

---

## Root Mean Squared Error (RMSE)

RMSE is the square root of MSE.

Formula:

**RMSE = √MSE**

Characteristics:

- Same unit as target variable.
- Easier to interpret than MSE.
- Still sensitive to large errors.

---

## R² (Coefficient of Determination)

R² measures how much of the variation in the target variable is explained by the model.

Formula:

**R² = 1 − (Residual Sum of Squares / Total Sum of Squares)**

Interpretation:

- 1.0 = Perfect prediction
- 0 = No improvement over predicting the mean
- Negative = Worse than predicting the mean

Higher R² indicates better model performance.

---

# Comparison of Regression Metrics

| Metric | Unit | Sensitive to Large Errors | Meaning |
|---------|------|--------------------------|---------|
| MAE | Same as target | Low | Average absolute prediction error |
| MSE | Squared unit | Very High | Average squared prediction error |
| RMSE | Same as target | High | Square root of MSE |
| R² | No unit | Not directly | Percentage of variance explained |

---

### ) 4

# Underfitting and Overfitting

## Underfitting

Underfitting occurs when a model is too simple to learn the underlying patterns in the data.

Characteristics:

- Poor training performance
- Poor testing performance
- High bias

Example:

Using a straight line to model a highly curved relationship.

---

## Overfitting

Overfitting occurs when a model learns both the true patterns and the noise in the training data.

Characteristics:

- Excellent training accuracy
- Poor performance on new data
- High variance

---

## Why Polynomial Regression Can Overfit

High-degree polynomial regression creates very flexible curves.

Instead of capturing the true relationship, it begins fitting random noise.

As polynomial degree increases:

- Complexity increases.
- Variance increases.
- Generalization decreases.

---

## Methods to Prevent Overfitting

### 1. Cross Validation

Evaluate the model on multiple validation sets to estimate its generalization performance.

### 2. Reduce Model Complexity

Choose a lower polynomial degree or use simpler models.

### 3. Regularization

Apply techniques such as Ridge Regression or Lasso Regression to reduce excessively large coefficients.

---

### ) 5

# Real-World Case Study

## Used Car Price Prediction Using Multiple Linear Regression

One practical application of regression is predicting the market value of used cars.

### Goal

Estimate fair selling prices based on vehicle characteristics.

### Data Used

Typical features include:

- Manufacturing year
- Mileage
- Engine size
- Fuel type
- Transmission
- Accident history
- Vehicle condition

The target variable is the selling price.

### Regression Technique

Researchers commonly use Multiple Linear Regression as a baseline model because it is simple and interpretable.

More advanced studies compare it with Random Forest and Gradient Boosting models.

### Key Results

The study found that:

- Vehicle age and mileage were among the strongest predictors of price.
- Multiple Linear Regression provided understandable relationships between features and price.
- Tree-based models such as Random Forest generally achieved lower prediction errors because they captured nonlinear relationships.

These findings help dealerships estimate prices more accurately and assist customers in making informed purchasing decisions.

---

# Conclusion

Regression is one of the most important techniques in supervised machine learning because it predicts continuous numerical values. Different regression methods are suitable for different types of relationships. Linear Regression is simple and interpretable, Multiple Linear Regression handles multiple features, while Polynomial Regression models nonlinear patterns.

Model evaluation metrics such as MAE, MSE, RMSE, and R² provide different perspectives on prediction quality. Understanding underfitting and overfitting is essential for building models that generalize well to new data. In practical applications such as used car price prediction, regression helps businesses make accurate, data-driven decisions.



