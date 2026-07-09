# Assignment 5 – Part A: Theory

## 1. What is Supervised Learning?

Supervised learning is a machine learning approach where a model learns from labeled data. The dataset contains input features and corresponding target outputs. The goal is to learn patterns from historical data and use them to make predictions on unseen data.

### Example
A bank can use past loan application records to predict whether a new loan applicant should be approved or rejected.

---

## 2. What is Classification?

Classification is a supervised learning task where the target variable belongs to predefined categories or classes.

### Example
Loan approval prediction:
- Approved = 1
- Not Approved = 0

The model learns from previous examples and predicts which class a new observation belongs to.

---

## 3. What is Logistic Regression?

Logistic Regression is a classification algorithm used to predict the probability of a binary outcome. It estimates the relationship between input variables and a categorical target variable.

### Advantages
- Simple and easy to interpret
- Fast to train
- Works well for binary classification problems

### Example
Predicting whether a loan application will be approved or rejected.

---

## 4. What is a Decision Tree?

A Decision Tree is a machine learning algorithm that makes predictions using a tree-like structure of decisions and rules.

### Advantages
- Easy to understand
- Easy to visualize
- Handles both numerical and categorical data

### Example
A bank may first check credit score, then income level, and finally loan amount before making a loan approval decision.

---

## 5. What is Random Forest?

Random Forest is an ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

### Advantages
- High predictive performance
- Reduces overfitting
- Works well on complex datasets

### Example
Instead of relying on one decision tree, the bank uses many decision trees and combines their predictions to make a final decision.

---

## 6. What is Train-Test Split?

Train-test split is the process of dividing data into two parts:

- Training Set (used to train the model)
- Testing Set (used to evaluate model performance)

In this assignment:
- Training Data = 80%
- Testing Data = 20%

This helps evaluate how well the model performs on unseen data.

---

## 7. What is Accuracy?

Accuracy measures the percentage of correct predictions made by a model.

Formula:

Accuracy = Correct Predictions / Total Predictions

### Example
If a model correctly predicts 70 out of 100 loan applications:

Accuracy = 70%

---

## 8. What is Precision?

Precision measures how many positive predictions were actually correct.

Formula:

Precision = True Positives / (True Positives + False Positives)

### Example
If a bank approves 100 loans and 90 are truly eligible:

Precision = 90%

---

## 9. What is Recall?

Recall measures how many actual positive cases were correctly identified.

Formula:

Recall = True Positives / (True Positives + False Negatives)

### Example
If 100 eligible customers exist and the model identifies 92 of them:

Recall = 92%

---

## 10. What is F1-Score?

F1-Score is the harmonic mean of Precision and Recall.

It is useful when both Precision and Recall are important.

### Example
Loan approval systems often require a balance between approving qualified applicants and avoiding risky approvals.

---

## 11. What is a Confusion Matrix?

A Confusion Matrix is a table used to evaluate classification models.

It contains:

- True Positives (TP)
- True Negatives (TN)
- False Positives (FP)
- False Negatives (FN)

It helps understand the types of prediction errors made by a model.

---

## Conclusion

Supervised machine learning techniques such as Logistic Regression, Decision Tree, and Random Forest can be used to predict loan approval outcomes. Evaluation metrics such as Accuracy, Precision, Recall, F1-Score, and Confusion Matrix help determine which model performs best.