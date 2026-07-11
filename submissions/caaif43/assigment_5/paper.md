# Assignment Five – Part A: Classification Theory

# Classification in Machine Learning

## Introduction

Machine Learning is a branch of Artificial Intelligence (AI) that enables computers to learn patterns from data and make predictions without being explicitly programmed. One of the most common supervised learning tasks is **classification**, where the goal is to predict a category or class rather than a numerical value. Classification is widely used in many industries, including healthcare, banking, education, cybersecurity, and e-commerce. This paper explains the concept of classification, compares common classification algorithms, discusses evaluation metrics, explains class imbalance, and presents a real-world case study.

---

# 1. Introduction to Classification

## What is Classification?

Classification is a supervised machine learning technique used to predict the category or class of an object based on its features. The model learns from labeled training data and then predicts the correct label for new data.

For example, in a loan approval system, a machine learning model predicts whether a loan application should be **Approved** or **Rejected** based on information such as income, credit score, employment history, and loan amount.

## Difference Between Classification and Regression

Although both classification and regression belong to supervised learning, they solve different types of problems.

| Classification             | Regression                |
| -------------------------- | ------------------------- |
| Predicts categories        | Predicts numerical values |
| Output is discrete         | Output is continuous      |
| Example: Approved/Rejected | Example: House Price      |

### Real-Life Examples

**Classification Example**

A bank predicts whether a customer should receive a loan.

**Regression Example**

A real estate company predicts the selling price of a house.

---

# 2. Classification Algorithms

## Logistic Regression

### Basic Idea

Logistic Regression estimates the probability that a data point belongs to a particular class using a sigmoid function. The probability is then converted into a final prediction.

### Real-World Use

* Loan approval
* Email spam detection
* Medical diagnosis

### Advantages

* Simple and easy to understand.
* Fast to train.
* Produces probability values.
* Works well for binary classification.

### Limitations

* Performs poorly on highly complex data.
* Assumes a relatively simple relationship between features and the target.

---

## Decision Tree

### Basic Idea

A Decision Tree makes predictions by asking a sequence of questions about the data. Each question splits the data into smaller groups until a final decision is reached.

### Real-World Use

* Customer segmentation
* Medical diagnosis
* Credit approval

### Advantages

* Easy to understand and visualize.
* Handles both numerical and categorical data.
* Requires little data preparation.

### Limitations

* Can easily overfit the training data.
* Small changes in data may produce a different tree.

---

## Random Forest

### Basic Idea

Random Forest combines many Decision Trees. Each tree makes its own prediction, and the final prediction is determined by majority voting.

### Real-World Use

* Fraud detection
* Loan approval
* Disease prediction
* Customer churn prediction

### Advantages

* High accuracy.
* Reduces overfitting.
* Handles complex relationships.
* Works well on large datasets.

### Limitations

* More computationally expensive.
* Harder to interpret than a single Decision Tree.

---

## Algorithm Comparison

| Feature                 | Logistic Regression | Decision Tree | Random Forest |
| ----------------------- | ------------------- | ------------- | ------------- |
| Easy to Interpret       | High                | High          | Medium        |
| Accuracy                | Medium              | Medium        | High          |
| Handles Non-linear Data | Limited             | Yes           | Yes           |
| Overfitting Risk        | Low                 | High          | Low           |
| Training Speed          | Fast                | Fast          | Moderate      |

---

# 3. Classification Metrics

Machine learning models must be evaluated using performance metrics.

## Accuracy

Accuracy measures the percentage of correct predictions among all predictions.

**Formula**

Accuracy = Correct Predictions / Total Predictions

Best used when classes are balanced.

---

## Precision

Precision measures how many predicted positive cases are actually positive.

High precision is important when false positives are expensive.

Example: Loan approval.

---

## Recall

Recall measures how many actual positive cases are correctly identified.

High recall is important when missing positive cases is costly.

---

## F1-Score

The F1-Score combines Precision and Recall into a single measurement.

It is especially useful when datasets are imbalanced.

---

## Confusion Matrix

A Confusion Matrix summarizes prediction results using four values:

* True Positive (TP)
* False Positive (FP)
* False Negative (FN)
* True Negative (TN)

It provides a detailed picture of model performance.

---

## Metrics Comparison

| Metric           | Measures                             | Suitable for Imbalanced Data |
| ---------------- | ------------------------------------ | ---------------------------- |
| Accuracy         | Overall correctness                  | No                           |
| Precision        | Quality of positive predictions      | Yes                          |
| Recall           | Ability to find positive cases       | Yes                          |
| F1-Score         | Balance between Precision and Recall | Yes                          |
| Confusion Matrix | Complete prediction breakdown        | Yes                          |

---

# 4. Class Imbalance

Class imbalance occurs when one class contains significantly more examples than another.

For example, suppose 95% of loan applications are approved and only 5% are rejected. A model that predicts "Approved" for every application would achieve 95% accuracy while completely failing to identify risky applicants. Therefore, accuracy alone can be misleading.

### When to Prioritize Precision

Precision should be prioritized when approving an unqualified applicant would result in financial loss. Banks should avoid approving customers who are likely to default on their loans.

### When to Prioritize Recall

Recall should be prioritized when the bank wants to identify as many qualified applicants as possible. A low recall may incorrectly reject customers who are capable of repaying their loans.

---

# 5. Real-World Case Study

## Loan Approval Prediction

Banks receive thousands of loan applications every day. Reviewing each application manually is time-consuming and expensive.

Machine learning classification models analyze customer information such as income, credit score, employment history, collateral, and previous loan defaults to predict whether an applicant should be approved.

Random Forest is commonly used because it provides high accuracy and can capture complex relationships among variables.

The main benefit is faster decision-making, reduced financial risk, and more consistent loan approval decisions.

