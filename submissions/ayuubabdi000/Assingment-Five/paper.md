# Introduction to Classification

## What is Classification in Machine Learning?

Classification is a supervised machine learning technique used to predict a category .
**Example:** Predicting whether a loan application will be **Approved** or **Rejected**.

## How is it Different from Regression?

| Classification | Regression |
|---------------|------------|
| Predicts categories or labels. | Predicts continuous numerical values. |
| Output is discrete (e.g., Yes/No). | Output is a number (e.g., price). |
| Example: Spam or Not Spam. | Example: House price prediction. |

### Real-Life Examples

- **Classification:** Predicting whether an email is **Spam** or **Not Spam**.
- **Regression:** Predicting the **price of a house** based on its features.

---

# Classification Algorithms

## Logistic Regression

**Definition:**  
Logistic Regression is a classification algorithm that predicts the probability that an input belongs to a particular class.

**How it Works**
- Calculates the probability of each class.
- Uses a sigmoid function to produce values between 0 and 1.
- Classifies based on a probability threshold (usually 0.5).

**Real-World Use Case**
- Loan approval prediction.

**Advantages**
- Simple and easy to interpret.
- Fast to train.
- Works well for binary classification.

**Limitations**
- Assumes a linear relationship.
- Cannot model complex patterns well.

---

## Decision Trees

**Definition:**  
A Decision Tree classifies data by asking a series of decision questions and splitting the data into branches.

**How it Works**
- Splits data based on the best feature.
- Creates branches until reaching a final decision (leaf node).

**Real-World Use Case**
- Customer churn prediction.

**Advantages**
- Easy to understand and visualize.
- Handles numerical and categorical data.
- Captures non-linear relationships.

**Limitations**
- Can overfit the training data.
- Sensitive to small changes in data.

---

## Random Forest

**Definition:**  
Random Forest is an ensemble learning algorithm that combines many decision trees to improve prediction accuracy.

**How it Works**
- Builds multiple decision trees using random subsets of data.
- Combines their predictions using majority voting.

**Real-World Use Case**
- Credit risk assessment.

**Advantages**
- High accuracy.
- Reduces overfitting.
- Works well with large datasets.

**Limitations**
- Slower than a single decision tree.
- Harder to interpret.

---

## Comparison of Algorithms

| Algorithm | Basic Idea | Use Case | Advantages | Limitations |
|-----------|------------|----------|------------|-------------|
| Logistic Regression | Predicts probability using a sigmoid function | Loan approval | Simple, fast, interpretable | Assumes linear relationship |
| Decision Tree | Splits data into branches | Customer churn | Easy to understand | Can overfit |
| Random Forest | Combines many decision trees | Credit risk prediction | Accurate, reduces overfitting | Less interpretable, slower |

---

# Classification Metrics

## Accuracy

**Definition:**  
Accuracy measures the percentage of correct predictions out of all predictions.

**Formula**

```
Accuracy = (Correct Predictions) / (Total Predictions)
```

---

## Precision

**Definition:**  
Precision measures how many predicted positive cases are actually positive.

**Formula**

```
Precision = TP / (TP + FP)
```

---

## Recall

**Definition:**  
Recall measures how many actual positive cases are correctly identified.

**Formula**

```
Recall = TP / (TP + FN)
```

---

## F1-Score

**Definition:**  
F1-Score combines Precision and Recall into a single metric.

**Formula**

```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

---

## Confusion Matrix

**Definition:**  
A Confusion Matrix is a table that compares actual values with predicted values.

| | Predicted Positive | Predicted Negative |
|---|---|---|
| Actual Positive | True Positive (TP) | False Negative (FN) |
| Actual Negative | False Positive (FP) | True Negative (TN) |

---

## Comparison of Metrics

| Metric | What it Measures | Sensitive to Class Imbalance |
|--------|------------------|------------------------------|
| Accuracy | Overall correctness | Yes |
| Precision | Correctness of positive predictions | No |
| Recall | Ability to find actual positives | No |
| F1-Score | Balance between Precision and Recall | Less sensitive |
| Confusion Matrix | Counts TP, FP, TN, FN | Helps analyze imbalance |

---

# Class Imbalance

## Why Can Accuracy Be Misleading?

When one class appears much more often than another, a model can achieve high accuracy simply by always predicting the majority class while failing to identify the minority class.

**Example:**  
If 95% of loan applications are approved, predicting **Approved** for every application gives 95% accuracy but completely misses rejected loans.

---

## When to Prioritize Precision or Recall

### Prioritize Precision

Use Precision when approving a risky loan would be costly.

**Loan Example:**  
If a model predicts a loan should be approved, you want to be highly confident that the applicant is actually eligible.

### Prioritize Recall

Use Recall when it is important to identify as many qualified applicants as possible.

**Loan Example:**  
A high Recall ensures that most eligible applicants are approved, reducing the chance of rejecting good customers.

---

# Real-World Case Study

## Loan Approval Prediction

### Goal

Predict whether a loan application should be approved based on applicant information.

### Data Used

- Applicant income
- Credit score
- Employment history
- Loan amount
- Previous loan defaults
- Collateral information

### Classifier Used

**Random Forest Classifier**

### Key Results

- Achieved high prediction accuracy.
- Reduced overfitting compared to a single decision tree.
- Identified credit score, income, and previous defaults as the most important features for loan approval decisions.

### Insights

Classification models help financial institutions make faster and more consistent loan approval decisions while reducing lending risk.