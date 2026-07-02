# Introduction to Regression

## What is Regression in Machine Learning?

Regression is a supervised machine learning technique used to predict **continuous numerical values** based on input features. The goal of regression is to learn the relationship between one or more independent variables (features) and a dependent variable (target). Once the model learns this relationship from historical data, it can predict future numerical values.

For example, regression can predict a house price, a student's exam score, a company's sales revenue, or the price of a used car.

---

## How is Regression Different from Classification?

Although both regression and classification are supervised learning techniques, they solve different types of problems.

| Regression | Classification |
|------------|----------------|
| Predicts continuous numerical values | Predicts discrete categories or classes |
| Output is a number | Output is a label |
| Example: Predicting house price | Example: Predicting whether an email is spam |

### Examples

**Regression Example**

Predicting the selling price of a used car based on features such as age, mileage, engine size, and brand.

**Classification Example**

Predicting whether a customer will buy a product (Yes or No) based on age, income, and purchasing history.

---

# Types of Regression

## 1. Linear Regression

### Basic Idea

Linear Regression assumes a straight-line relationship between the input variable and the output variable.

The equation is:

**Y = β₀ + β₁X**

Where:

- Y = predicted value
- X = input feature
- β₀ = intercept
- β₁ = slope

The algorithm finds the best-fitting line by minimizing prediction errors.

### Real-World Use Case

Predicting house prices using house size.

### Advantages

- Easy to understand
- Fast to train
- Highly interpretable
- Works well for linear relationships

### Limitations

- Cannot model complex relationships
- Sensitive to outliers
- Assumes a linear relationship

---

## 2. Multiple Linear Regression

### Basic Idea

Multiple Linear Regression extends Linear Regression by using multiple input variables.

Equation:

**Y = β₀ + β₁X₁ + β₂X₂ + ... + βₙXₙ**

Instead of using only one feature, it combines several features to improve prediction.

### Real-World Use Case

Predicting car prices using:

- Mileage
- Brand
- Engine size
- Fuel type
- Manufacturing year

### Advantages

- More accurate than simple linear regression
- Uses multiple sources of information
- Easy to interpret

### Limitations

- Assumes linear relationships
- Sensitive to multicollinearity
- Can become unstable if features are highly correlated

---

## 3. Polynomial Regression

### Basic Idea

Polynomial Regression models curved relationships by adding powers of the input variable.

Example:

**Y = β₀ + β₁X + β₂X² + β₃X³**

Although it is called polynomial regression, it is still a type of linear model because it is linear in the coefficients.

### Real-World Use Case

Predicting crop yield based on fertilizer amount, where the relationship is curved rather than linear.

### Advantages

- Captures nonlinear relationships
- More flexible than linear regression
- Better fit for curved data

### Limitations

- Can easily overfit
- More difficult to interpret
- Higher-degree polynomials become unstable

---

# Regression Metrics

Regression metrics evaluate how accurately a model predicts numerical values.

---

## Mean Absolute Error (MAE)

### Definition

MAE is the average absolute difference between actual and predicted values.

Formula:

**MAE = (1/n) Σ |Actual − Predicted|**

### What it Measures

Average prediction error.

### Interpretation

Smaller MAE means better predictions.

---

## Mean Squared Error (MSE)

### Definition

MSE is the average squared difference between actual and predicted values.

Formula:

**MSE = (1/n) Σ (Actual − Predicted)²**

### What it Measures

Average squared prediction error.

Large errors receive much larger penalties.

### Interpretation

Lower MSE indicates better performance.

---

## Root Mean Squared Error (RMSE)

### Definition

RMSE is the square root of MSE.

Formula:

**RMSE = √MSE**

### What it Measures

Average prediction error expressed in the original units.

### Interpretation

Lower RMSE indicates more accurate predictions.

---

## R² (Coefficient of Determination)

### Definition

R² measures how much of the variation in the target variable is explained by the regression model.

Formula:

**R² = 1 − (Residual Sum of Squares / Total Sum of Squares)**

### Interpretation

- R² = 1 → Perfect prediction
- R² = 0 → Model performs no better than predicting the mean
- R² < 0 → Model performs worse than predicting the mean

Higher R² values indicate better model performance.

---

# Comparison of Regression Metrics

| Metric | Unit | Sensitive to Large Errors? | Meaning |
|---------|------|---------------------------|---------|
| MAE | Same as target | No | Average absolute prediction error |
| MSE | Squared units | Yes | Average squared prediction error |
| RMSE | Same as target | Yes | Average prediction error with stronger penalty for large errors |
| R² | No unit | No | Percentage of variance explained by the model |

---

# Underfitting and Overfitting

## Underfitting

Underfitting occurs when a model is too simple to capture the patterns in the data.

Characteristics:

- Poor training accuracy
- Poor testing accuracy
- High bias

Example:

Using a straight line to fit highly curved data.

---

## Overfitting

Overfitting occurs when a model learns not only the true patterns but also the noise in the training data.

Characteristics:

- Very high training accuracy
- Poor testing accuracy
- High variance

The model performs well on training data but fails to generalize to new data.

---

## Causes of Overfitting (Especially in Polynomial Regression)

Polynomial regression can overfit when:

- The polynomial degree is too high.
- The model becomes overly complex.
- It starts fitting random noise instead of meaningful patterns.
- The training dataset is too small.

---

## Methods to Prevent Overfitting

### 1. Use Simpler Models

Choose a lower polynomial degree or a simpler regression model.

### 2. Cross-Validation

Evaluate the model using different subsets of the data to ensure it generalizes well.

### 3. Regularization

Use techniques such as Ridge Regression or Lasso Regression to penalize overly complex models.

---

# Real-World Case Study

## Predicting House Prices Using Multiple Linear Regression

### Goal

Researchers and real estate companies use Multiple Linear Regression to estimate house prices based on property characteristics. Accurate price prediction helps buyers, sellers, and real estate agents make informed decisions.

### Data Used

Typical features include:

- House size (square feet)
- Number of bedrooms
- Number of bathrooms
- Age of the house
- Location
- Distance to schools and public transportation

The target variable is the selling price of the house.

### Type of Regression Applied

Multiple Linear Regression.

### Key Results and Insights

The regression model showed that house size and location were the strongest predictors of selling price. Houses located in desirable neighborhoods with larger living areas generally had significantly higher prices. The model enabled real estate professionals to estimate market values, identify overpriced or underpriced properties, and support pricing decisions with data-driven insights. This demonstrates how regression analysis can improve decision-making in the real estate industry.