# 📊 Empirical Research Paper: Used Car Price Prediction Modeling

---

## 1. Abstract & Introduction (What Was Implemented)

In this research project, we developed a machine learning framework using Python’s `scikit-learn` library to predict used car prices based on a cleaned vehicle dataset. The predictive pipeline evaluated three distinct algorithms:

- Ordinary Least Squares (OLS) Linear Regression  
- Random Forest Regressor  
- Gradient Boosting Regressor  

The dataset includes features such as:

- Odometer_km  
- CarAge  
- Km_per_year  
- Doors  
- Accidents  
- Location variables (Location_City, Location_Rural, Location_Suburb, Is_Urban)

To stabilize variance and address non-linear distribution in car prices, the target variable `Price` was transformed into `LogPrice` using:

\[
y = \ln(\text{Price})
\]

The dataset contains **138 rows**, split into:

- Train set: 110 rows (80%)
- Test set: 28 rows (20%)

A fixed seed (`random_state=42`) was used for reproducibility.

---

## 2. Comparison of Models (Sanity Check Observations)

During validation testing, predictions showed noticeable differences between models, especially at extreme price ranges.

### 🔹 Low-Price Example
- Actual: **$1,501**
- Linear Regression: **$2,677**
- Random Forest: **$3,184**

### 🔹 High-Price Example
- Actual: **$8,871**
- Linear Regression: **$6,375**
- Random Forest: **$5,734**

---

### 📌 Key Insight

Linear Regression produced more stable and realistic predictions compared to ensemble models.

This is largely due to a structural issue in the dataset:

> A strict price floor at **$1,500** exists across multiple entries.

This creates conflicting patterns where identical target values correspond to very different feature combinations.

Linear Regression handles this by fitting a global trend, while tree-based models struggle with repeated identical outputs.

---

## 3. Understanding Random Forest

A Random Forest is an ensemble learning method that combines multiple decision trees to improve predictive accuracy.

### 🔧 How it works:

#### 1. Bootstrap Sampling (Bagging)
- Each tree is trained on a random sample of the dataset (with replacement).

#### 2. Feature Randomness
- At each split, only a subset of features is considered.

#### 3. Aggregation
- Each tree makes a prediction.
- Final output is the **average of all tree predictions**.

---

### 📌 Benefit
- Reduces variance
- Prevents overfitting (in large datasets)

### 📌 Limitation
- Poor extrapolation outside training distribution
- Sensitive to small datasets

---

## 4. Metrics Discussion & Analytical Findings

| Model               | Train R² | Test R² | MAE   | RMSE  |
|--------------------|----------|---------|-------|-------|
| Linear Regression  | 0.607    | **0.550** | 1427  | **2079** |
| Gradient Boosting  | 0.987    | 0.486   | **1260** | 2110  |
| Random Forest      | 0.825    | 0.508   | 1490  | 2202  |

---

### 📌 Interpretation

#### 🔹 Linear Regression
- Best generalization performance
- Stable train-test balance
- Limited non-linear modeling ability

#### 🔹 Random Forest
- Moderate performance
- Struggles with extrapolation
- Affected by duplicated target values

#### 🔹 Gradient Boosting
- Very high training accuracy (overfitting)
- Weak test performance due to small dataset

---

## 5. Research Conclusion & Recommendations

Based on experimental results, **Linear Regression is the most reliable model** for this dataset.

### 📌 Reason:
- Small dataset (138 samples)
- Artificial price floor ($1500 cap)
- High noise and duplicate target values

Ensemble models (Random Forest & Gradient Boosting) typically require larger datasets to perform effectively.

---

## 🚀 Future Improvements

To improve model performance:

- Increase dataset size (500+ rows recommended)
- Remove artificial price constraints
- Apply cross-validation (k-fold)
- Test advanced models:
  - Ridge Regression
  - Lasso Regression
  - XGBoost

---

## 📌 Final Conclusion

Simple models can outperform complex models when:

- Data is limited
- Patterns are noisy
- Target distribution is artificially constrained

In this case, Linear Regression provides the best balance between accuracy and generalization.