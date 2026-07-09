# Part A – Theory

## Classification in Machine Learning

### Introduction

Machine Learning is a branch of Artificial Intelligence (AI) that enables computers to learn patterns from data and make predictions without being explicitly programmed. One of the most common supervised learning tasks is **classification**, where the goal is to predict the category or class of an input based on previously labeled data. Classification is widely used in finance, healthcare, education, cybersecurity, and many other industries to support decision-making.

---

# 1. Introduction to Classification

## What is Classification in Machine Learning?

Classification is a supervised machine learning technique used to predict a predefined category or class. The model learns from labeled training data and then assigns new data to one of the known classes.

For example, a bank can use a classification model to determine whether a loan application should be **Approved** or **Rejected** based on information such as income, employment status, and credit history.

---

## Difference Between Classification and Regression

Although both classification and regression belong to supervised learning, they solve different types of problems.

Classification predicts categories or labels, while regression predicts continuous numerical values.

Examples include:

- Classification: Predicting whether an email is Spam or Not Spam.
- Regression: Predicting the selling price of a house.

### Comparison

| Classification | Regression |
|---------------|------------|
| Predicts categories | Predicts numerical values |
| Output is a class label | Output is a continuous number |
| Example: Loan Approved/Rejected | Example: House Price Prediction |

---

## Real-Life Examples

### Classification Example

A bank predicts whether a customer is eligible for a loan.

Possible outputs:
- Approved
- Rejected

### Regression Example

A real estate company predicts the market price of a house based on its size, location, and number of rooms.

---

# 2. Classification Algorithms

## Logistic Regression

### Basic Idea

Logistic Regression is a classification algorithm that estimates the probability that an observation belongs to a particular class. It uses the sigmoid function to produce probability values between 0 and 1.

### Real-World Use Case

Banks use Logistic Regression to predict loan approval decisions.

### Advantages

- Simple to implement
- Fast training
- Easy to interpret
- Works well for binary classification

### Limitations

- Performs poorly on complex non-linear relationships
- Sensitive to irrelevant features

---

## Decision Tree

### Basic Idea

A Decision Tree predicts outcomes by asking a sequence of questions about the data. Each question creates a branch until a final decision (leaf node) is reached.

### Real-World Use Case

Hospitals use Decision Trees to help diagnose diseases based on patient symptoms.

### Advantages

- Easy to understand and visualize
- Works with numerical and categorical data
- Requires little data preparation

### Limitations

- Can easily overfit training data
- Small data changes may produce a different tree

---

## Random Forest

### Basic Idea

Random Forest is an ensemble learning algorithm that combines many Decision Trees. Each tree makes a prediction, and the final result is determined by majority voting.

### Real-World Use Case

Financial institutions use Random Forest to detect loan fraud and assess credit risk.

### Advantages

- High prediction accuracy
- Reduces overfitting
- Handles large datasets effectively
- Robust against noisy data

### Limitations

- More computationally expensive
- Harder to interpret than a single Decision Tree

---

## Comparison of Algorithms

| Algorithm | How it Works | Advantages | Limitations |
|------------|-------------|------------|-------------|
| Logistic Regression | Uses probability to classify data | Fast and simple | Cannot model complex relationships well |
| Decision Tree | Makes decisions through a series of questions | Easy to understand | Can overfit |
| Random Forest | Combines multiple decision trees | High accuracy and robust | More complex and slower |

---

# 3. Classification Metrics

Machine learning models are evaluated using different performance metrics.

## Accuracy

Accuracy measures the percentage of correct predictions made by the model.

Formula:

Accuracy = Correct Predictions / Total Predictions

---

## Precision

Precision measures how many predicted positive cases are actually positive.

High precision means there are few false positive predictions.

---

## Recall

Recall measures how many actual positive cases are correctly identified.

High recall means there are few false negatives.

---

## F1-Score

F1-Score combines Precision and Recall into one metric.

It is especially useful when the dataset is imbalanced.

---

## Confusion Matrix

A Confusion Matrix summarizes prediction results.

It contains:

- True Positive (TP)
- True Negative (TN)
- False Positive (FP)
- False Negative (FN)

It helps identify which types of prediction errors the model makes.

---

## Comparison of Evaluation Metrics

| Metric | Measures | Sensitive to Class Imbalance |
|---------|----------|-----------------------------|
| Accuracy | Overall correctness | Yes |
| Precision | Correct positive predictions | Less sensitive |
| Recall | Ability to detect actual positives | Less sensitive |
| F1-Score | Balance between Precision and Recall | No |
| Confusion Matrix | Detailed prediction results | No |

---

# 4. Class Imbalance

Class imbalance occurs when one class has significantly more samples than another.

For example, if 95 loan applications are approved and only 5 are rejected, a model that predicts every application as approved will achieve 95% accuracy but completely fail to identify rejected applications.

Therefore, relying only on Accuracy can be misleading.

### When to Prioritize Precision

Precision should be prioritized when false positive predictions are costly.

Loan Approval Example:

If a bank approves a loan for someone who is actually likely to default, the bank may lose money.

Therefore, high Precision is important.

### When to Prioritize Recall

Recall should be prioritized when missing positive cases is more harmful.

Loan Approval Example:

If the bank wants to ensure that every qualified applicant is identified, Recall becomes more important because it reduces false negatives.

---

# 5. Real-World Case Study

## Loan Approval Prediction Using Machine Learning

### Goal

The objective of the project was to predict whether a loan application should be approved based on applicant information.

### Data Used

The dataset included features such as:

- Gender
- Marital Status
- Education
- Applicant Income
- Co-applicant Income
- Loan Amount
- Credit History
- Property Area

### Classification Algorithm

The study applied Logistic Regression, Decision Tree, and Random Forest classifiers.

### Results

Random Forest achieved the highest prediction accuracy because it combines multiple decision trees and reduces overfitting.

Logistic Regression provided a simple and interpretable baseline model.

Decision Tree was easy to understand but showed a higher risk of overfitting.

The results demonstrated that ensemble methods such as Random Forest often provide more reliable predictions for loan approval problems.

---

# Conclusion

Classification is one of the most important techniques in supervised machine learning. It is widely used to solve real-world problems involving category prediction. Logistic Regression, Decision Tree, and Random Forest each have different strengths and weaknesses. Choosing the appropriate algorithm depends on the dataset, the problem being solved, and the desired balance between accuracy, interpretability, and computational cost.

---

# References

1. Aurélien Géron. *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow*. O'Reilly Media, 2019.

2. Christopher M. Bishop. *Pattern Recognition and Machine Learning*. Springer, 2006.

3. Ian Goodfellow, Yoshua Bengio, and Aaron Courville. *Deep Learning*. MIT Press, 2016.

4. Scikit-learn Developers. *Scikit-learn Documentation*. https://scikit-learn.org

5. Han, Kamber, and Pei. *Data Mining: Concepts and Techniques*. Morgan Kaufmann.