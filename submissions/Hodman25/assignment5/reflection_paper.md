# Loan Approval Classification Project

## What Did I Implement?

In this assignment, I reproduced the Lesson 5 preprocessing pipeline and trained three classification models to predict loan approval outcomes.

The preprocessing pipeline included:

- Handling missing values
- Encoding categorical variables
- Splitting the dataset into training and testing sets (80% training, 20% testing)
- Training and evaluating classification models

The three classifiers used were:

1. Logistic Regression
2. Random Forest
3. Decision Tree (additional classifier)

The goal was to predict whether a loan application would be **Approved (1)** or **Rejected (0)**.

---

# Comparison of Models

## Sanity Check Results

For a single test application, the actual label was:

**Rejected (0)**

Predictions from the three models were:

| Model | Prediction |
|---------|-----------|
| Logistic Regression | Approved (1) |
| Random Forest | Approved (1) |
| Decision Tree | Approved (1) |

All three models predicted **Approved**, while the true label was **Rejected**. This indicates that this particular application was difficult for all models to classify correctly.

## Which Model Gave More Realistic Results?

Based on the evaluation metrics, **Logistic Regression** provided the most realistic and reliable results because it achieved the highest overall performance.

| Model | Accuracy | Precision | Recall | F1-Score |
|---------|---------|---------|---------|---------|
| Logistic Regression | **0.750** | **0.750** | **0.923** | **0.828** |
| Random Forest | 0.650 | 0.714 | 0.769 | 0.741 |
| Decision Tree | 0.700 | 0.706 | 0.923 | 0.800 |

Logistic Regression achieved the best balance between correctly identifying approved loans and minimizing incorrect predictions.

---

# Understanding Random Forest

Random Forest is an ensemble machine learning algorithm that combines many Decision Trees to make a final prediction.

### How It Works

1. Multiple Decision Trees are created using random samples of the training data.
2. Each tree learns different patterns from the data.
3. Every tree makes its own prediction.
4. The final classification is determined using **majority voting**.

Example:

- Tree 1 → Approved
- Tree 2 → Approved
- Tree 3 → Rejected
- Tree 4 → Approved

Final Prediction → **Approved**

### Advantage

- Reduces overfitting compared to a single Decision Tree.
- Usually produces more stable predictions.

### Limitation

- More difficult to interpret than a single Decision Tree.
- Requires more computational resources.

---

# Other Algorithm: Decision Tree

I selected **Decision Tree** as my additional classifier because it is simple, easy to understand, and commonly used for classification tasks.

## How It Works

A Decision Tree repeatedly splits data into smaller groups based on feature values. These splits continue until the model reaches a final decision represented by a leaf node.

### Advantage

- Easy to visualize and interpret.

### Limitation

- Can overfit the training data if not properly controlled.

## Performance Comparison

| Model | Accuracy | Precision | Recall | F1-Score |
|---------|---------|---------|---------|---------|
| Logistic Regression | **0.750** | **0.750** | **0.923** | **0.828** |
| Decision Tree | 0.700 | 0.706 | **0.923** | 0.800 |
| Random Forest | 0.650 | 0.714 | 0.769 | 0.741 |

Decision Tree performed better than Random Forest on this dataset but did not outperform Logistic Regression overall.

---

# Metrics Discussion

## Best Accuracy

**Logistic Regression (0.750)**

This means it produced the highest percentage of correct predictions overall.

## Best Precision

**Logistic Regression (0.750)**

This indicates that when the model predicted loan approval, it was correct more often than the other models.

## Best Recall

**Logistic Regression and Decision Tree (0.923)**

These models successfully identified most approved loans.

## Best F1-Score

**Logistic Regression (0.828)**

This shows it achieved the best balance between Precision and Recall.

### Strengths and Weaknesses

| Model | Strength | Weakness |
|---------|---------|---------|
| Logistic Regression | Best overall performance | Assumes linear relationships |
| Random Forest | Ensemble method reduces overfitting | Lower performance on this dataset |
| Decision Tree | Easy to interpret | Can overfit training data |

---

# Findings

Based on the evaluation results, I would choose **Logistic Regression** for loan approval prediction. It achieved the highest Accuracy, Precision, and F1-Score while also maintaining excellent Recall. These results suggest that it provides the most reliable overall performance for this dataset.

Although Random Forest is generally a powerful ensemble method, it did not outperform Logistic Regression in this experiment. The Decision Tree achieved strong Recall but lower overall Accuracy and F1-Score. Therefore, Logistic Regression offers the best balance between identifying approved loans and avoiding incorrect approvals, making it the most suitable model for this loan approval classification task.