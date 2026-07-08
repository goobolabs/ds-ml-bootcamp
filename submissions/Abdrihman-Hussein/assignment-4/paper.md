# Regression: Theory and Practice

## Abstract

Regression is a fundamental supervised machine learning technique used to predict continuous numerical values. This paper explores regression fundamentals, various regression models, evaluation metrics, and real-world applications. Understanding regression is essential for data science and machine learning practitioners.

---

# 1. Introduction to Regression

Regression is a supervised learning method that predicts continuous numerical outcomes based on input features. Unlike classification (which predicts categories), regression estimates real-valued outputs.

## Key Differences: Regression vs Classification

| Aspect | Regression | Classification |
|--------|-----------|-----------------|
| **Output** | Continuous values | Discrete categories |
| **Example** | Predicting house price | Predicting if email is spam |
| **Use Case** | Price, temperature, salary | Email classification, disease diagnosis |

## Real-World Applications

- **Finance**: Stock price prediction, loan default prediction
- **Healthcare**: Patient cost estimation, disease progression
- **Real Estate**: Property price prediction
- **Transportation**: Car price prediction, fuel consumption
- **Weather**: Temperature and rainfall forecasting

---

# 2. Types of Regression Models

## 2.1 Linear Regression

Linear Regression models the relationship between variables using a linear equation: **y = mx + b**

### Advantages
- Simple and fast to train
- Highly interpretable
- Works well for linear relationships
- Low computational cost

### Limitations
- Cannot capture non-linear patterns
- Sensitive to outliers
- Assumes linear relationships between variables

### Use Case
Predicting used car prices based on mileage and age.

---

## 2.2 Multiple Linear Regression

Extends linear regression to multiple independent variables.

**Formula**: y = b₀ + b₁x₁ + b₂x₂ + ... + bₙxₙ

### Advantages
- Uses multiple features for better predictions
- More flexible than simple linear regression
- Identifies feature importance

### Limitations
- Multicollinearity issues
- Still assumes linear relationships
- More complex interpretation

### Use Case
Predicting house prices using size, location, age, and number of bedrooms.

---

## 2.3 Polynomial Regression

Adds polynomial terms to capture non-linear relationships.

**Formula**: y = b₀ + b₁x + b₂x² + b₃x³ + ...

### Advantages
- Captures curved relationships
- More flexible than linear models
- Better for complex data

### Limitations
- Risk of overfitting
- Difficult to interpret
- Computationally expensive

### Use Case
Modeling population growth or scientific measurements with curved trends.

---

## 2.4 Random Forest Regression

Ensemble method combining multiple decision trees for predictions.

### How It Works
1. Creates multiple random decision trees
2. Each tree makes independent predictions
3. Final prediction is the average of all tree predictions
4. Reduces overfitting compared to single tree

### Advantages
- Captures non-linear relationships
- Reduces overfitting
- Handles missing values well
- Feature importance available

### Limitations
- Less interpretable than linear models
- Computationally expensive
- Requires more data

---

# 3. Regression Evaluation Metrics

## 3.1 Mean Absolute Error (MAE)

**Formula**: MAE = (1/n) Σ|yᵢ - ŷᵢ|

**Interpretation**: Average absolute difference between predicted and actual values

**Pros**: Easy to interpret, robust to outliers
**Cons**: Doesn't penalize large errors heavily

---

## 3.2 Mean Squared Error (MSE)

**Formula**: MSE = (1/n) Σ(yᵢ - ŷᵢ)²

**Interpretation**: Average squared prediction error

**Pros**: Penalizes large errors, commonly used
**Cons**: Not in original units, hard to interpret

---

## 3.3 Root Mean Squared Error (RMSE)

**Formula**: RMSE = √MSE

**Interpretation**: Typical prediction error magnitude in original units

**Pros**: Same units as target, penalizes large errors
**Cons**: Sensitive to outliers

---

## 3.4 R² Score (Coefficient of Determination)

**Formula**: R² = 1 - (SS_res / SS_tot)

**Interpretation**: Proportion of variance explained by the model

**Range**: 0 to 1 (higher is better)
- R² = 1: Perfect predictions
- R² = 0.5: Model explains 50% of variance
- R² = 0: Model no better than mean

**Pros**: Interpretable, standardized
**Cons**: Can be misleading with few samples

---

# 4. Underfitting and Overfitting

## 4.1 Underfitting

**Definition**: Model is too simple to capture data patterns

**Characteristics**:
- Poor training performance
- Poor testing performance
- High bias, low variance

**Causes**:
- Model too simple
- Insufficient features
- Too much regularization

**Solutions**:
- Use more complex model
- Add more features
- Reduce regularization
- Collect more data

---

## 4.2 Overfitting

**Definition**: Model learns noise instead of true patterns

**Characteristics**:
- Excellent training performance
- Poor testing performance
- Low bias, high variance

**Causes**:
- Model too complex
- Too many features
- Not enough data
- Too little regularization

**Solutions**:
- Simplify model
- Use fewer features
- Cross-validation
- Regularization (Ridge, Lasso)
- Collect more data

---

# 5. Model Selection and Evaluation

## Choosing the Right Model

| Scenario | Recommended Model |
|----------|------------------|
| Linear relationships | Linear Regression |
| Multiple predictors | Multiple Linear Regression |
| Curved relationships | Polynomial Regression |
| Complex non-linear | Random Forest, Gradient Boosting |
| Small dataset | Linear/Polynomial Regression |
| Large dataset | Random Forest, Neural Networks |

## Cross-Validation

**Purpose**: Estimate model performance on unseen data

**k-Fold Cross-Validation**:
1. Split data into k equal parts
2. Train on k-1 parts, test on 1 part
3. Repeat k times
4. Average results

**Typical k values**: 5, 10

---

# 6. Real-World Case Study: Car Price Prediction

## Problem Statement
Predict used car prices based on features like mileage, age, accidents, and location.

## Dataset Features
- Odometer reading (km)
- Number of doors
- Accident history
- Vehicle year
- Location (city, rural, suburb)
- Car age
- Km per year

## Models Implemented
1. **Linear Regression**: Simple baseline model
2. **Random Forest**: Ensemble model for complexity

## Expected Performance
- R² Score: 0.3-0.5 (moderate predictive power)
- RMSE: $1,500-2,500
- MAE: $1,200-1,500

## Insights
- Car age and mileage are strong price predictors
- Location affects price significantly
- Accident history impacts value
- Random Forest typically outperforms Linear Regression

---

# 7. Conclusion

Regression is a versatile machine learning technique for predicting continuous values. Selecting the appropriate model depends on data characteristics, complexity, and business requirements. Proper evaluation using multiple metrics and cross-validation ensures reliable predictions. This assignment demonstrates implementing and comparing regression models for real-world car price prediction.

---

