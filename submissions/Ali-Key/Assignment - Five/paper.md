# Assignment Five — Part A: Classification Theory

**Author:** Ali Omar Abdi  
**Course:** DS-ML Bootcamp.       
**Due:** Sunday, July 5, 2026 — 12:00 PM (Africa/Mogadishu / EAT)

---

# 1. Introduction to Classification

Classification is a type of supervised machine learning where the goal is to predict a category or label. The model learns from labeled training data and then uses that knowledge to classify new data into the correct group.

Classification is different from regression because it predicts categories instead of numbers. For example, classification predicts outcomes such as **Approved** or **Rejected**, while regression predicts continuous values like house prices or salaries.

A real-world example of classification is a bank deciding whether to approve a loan based on a customer's income, employment history, and credit score. A real-world example of regression is predicting the selling price of a house using features such as its size, location, and age.

---

# 2. Classification Algorithms

## Logistic Regression

Logistic Regression is a classification algorithm that estimates the probability that a record belongs to a particular class. If the probability is above a chosen threshold, the model assigns that class as the prediction.

A common use case is customer churn prediction, where companies predict whether a customer is likely to leave their service.

### Advantages
- Easy to understand and explain.
- Fast to train.
- Works well on simple datasets.

### Limitations
- Does not perform well with complex non-linear relationships.
- May require feature engineering to improve performance.

---

## Decision Trees

Decision Trees classify data by splitting it into smaller groups using a series of decision rules. Each split is based on the feature that best separates the classes.

Decision Trees are commonly used in healthcare to help diagnose diseases based on symptoms and medical test results.

### Advantages
- Easy to visualize and interpret.
- Works with both numerical and categorical data.
- Requires little data preparation.

### Limitations
- Can easily overfit the training data.
- Small changes in the data can produce different tree structures.

---

## Random Forest

Random Forest is an ensemble learning algorithm that combines many Decision Trees. Each tree makes its own prediction, and the final result is determined by majority voting.

It is widely used in finance for tasks such as loan approval, credit scoring, and fraud detection because it generally provides high prediction accuracy.

### Advantages
- High accuracy.
- Less likely to overfit than a single Decision Tree.
- Handles complex relationships well.

### Limitations
- Harder to interpret.
- Slower to train and predict than simpler models.

---

# 3. Classification Metrics

Classification models are evaluated using different performance metrics.

- **Accuracy** measures the percentage of predictions that are correct.
- **Precision** measures how many predicted positive cases are actually positive.
- **Recall** measures how many actual positive cases are correctly identified.
- **F1-Score** combines Precision and Recall into one balanced score.
- **Confusion Matrix** provides a detailed summary of correct and incorrect predictions.

| Metric | What It Measures | Sensitivity to Class Imbalance |
|---------|------------------|-------------------------------|
| Accuracy | Overall percentage of correct predictions | High – can be misleading when classes are imbalanced |
| Precision | Correctness of positive predictions | Useful when false positives are costly |
| Recall | Ability to find all positive cases | Useful when false negatives are costly |
| F1-Score | Balance between Precision and Recall | Better for imbalanced datasets |
| Confusion Matrix | Shows TP, FP, TN, and FN | Clearly reveals prediction errors |

---

# 4. Class Imbalance

Class imbalance happens when one class appears much more often than another. In this situation, Accuracy can give a misleading result.

For example, if 95% of loan applications are approved, a model that approves every applicant would still achieve 95% Accuracy even though it fails to identify risky borrowers.

In loan approval, **Precision** is more important when the bank wants to avoid approving applicants who may fail to repay their loans. **Recall** becomes more important when the bank wants to avoid rejecting qualified applicants who are likely to repay. The choice depends on which type of error has the greater financial impact.

---

# 5. Real-World Case Study

A well-known application of classification is **loan default prediction** in the financial industry.

Researchers used the LendingClub loan dataset to predict whether borrowers would repay or default on their loans. The dataset included information such as income, employment history, loan amount, debt ratio, and credit history.

Before training the models, the data was cleaned and techniques such as **SMOTE** were used to reduce class imbalance.

Among the models tested, **Random Forest** achieved the best overall performance because it captured complex patterns in the data better than Logistic Regression and Decision Trees. The study concluded that Random Forest is an effective model for loan default prediction, although it is more difficult to interpret than simpler algorithms.

---

# References

1. Zhu, L., et al. (2019). *A Study on Predicting Loan Default Based on the Random Forest Algorithm.* Procedia Computer Science, 162, 503–513.

2. *Loan Prediction Literature Review.* (2024). arXiv:2410.08886.

3. Wang, Y., et al. (2021). *Machine Learning Methods for Peer-to-Peer Loan Default Prediction.* PMC8455619.

4. *Loan Default Prediction Using Machine Learning.* (2023). arXiv:2301.08702.

*Submitted for DS-ML Bootcamp — Assignment Five*        
*Due: Sunday, July 5, 2026*