# Assignment Five — Part A: Theory

## 1. Introduction to Classification

Classification is a supervised learning technique in Machine Learning where the goal is to predict a category or class label based on input features. The model learns patterns from labeled training data and uses them to classify new unseen data.

Classification differs from regression in that classification predicts discrete outputs (e.g., Yes/No, Approved/Rejected), while regression predicts continuous numerical values (e.g., price, salary).

Examples:
- Classification: Loan Approved or Not Approved
- Regression: Predicting house price

## 2. Classification Algorithms

### Logistic Regression
Logistic Regression is a linear classification algorithm that uses the sigmoid function to estimate probabilities between 0 and 1.

Advantages:
- Fast and efficient
- Easy to interpret
- Works well for linear data

Limitations:
- Poor with complex patterns

### Decision Tree
A Decision Tree splits data using if-else rules until a decision is made.

Advantages:
- Easy to interpret
- Handles non-linear relationships

Limitations:
- Overfitting risk

### Random Forest
Random Forest combines multiple decision trees and uses majority voting.

Advantages:
- High accuracy
- Reduces overfitting

Limitations:
- Computationally expensive

## 3. Classification Metrics

- Accuracy: Overall correctness
- Precision: Correct positive predictions
- Recall: Ability to find actual positives
- F1-Score: Balance between precision and recall
- Confusion Matrix: TP, FP, TN, FN

## 4. Class Imbalance

Accuracy can be misleading when classes are imbalanced because a model can predict only the majority class.

Loan example:
- False Negative: Rejecting good customer
- False Positive: Approving risky customer

## 5. Real-World Case Study

Banks use classification models to predict loan approval using data such as income, credit score, and employment history. Random Forest often performs best in such tasks.
