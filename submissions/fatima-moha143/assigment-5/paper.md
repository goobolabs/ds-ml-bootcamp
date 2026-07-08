## Introduction to Classification

### What is Classification in Machine Learning?

Classification is a supervised machine learning technique used to predict a categorical label or class for new data. In classification problems, the target variable belongs to a predefined category rather than a continuous numerical value. The model learns patterns from historical labeled data and then assigns new observations to one of the available classes.

The primary goal of classification is to determine which category an input belongs to based on its features. Classification is widely used in many industries, including healthcare, finance, marketing, cybersecurity, and education.

Examples of classification tasks include:

* Determining whether an email is spam or not spam.
* Predicting whether a customer will buy a product or not.
* Identifying whether a medical image indicates the presence of a disease.
* Classifying a loan application as approved or rejected.

---

### How is Classification Different from Regression?

Although both classification and regression are supervised learning techniques, they solve different types of problems.

| Feature            | Classification                                     | Regression                          |
| ------------------ | -------------------------------------------------- | ----------------------------------- |
| Output Type        | Categorical values                                 | Continuous numerical values         |
| Goal               | Predict a class or category                        | Predict a quantity or number        |
| Example            | Spam or Not Spam                                   | House Price Prediction              |
| Common Algorithms  | Logistic Regression, Decision Trees, Random Forest | Linear Regression, Ridge Regression |
| Evaluation Metrics | Accuracy, Precision, Recall, F1-Score              | MAE, MSE, RMSE, R²                  |

Classification predicts categories, while regression predicts numerical values.

---

### Real-Life Examples

#### Classification Example

A bank wants to predict whether a customer will default on a loan.

Possible outputs:

* Default
* No Default

Since the output belongs to categories, this is a classification problem.

#### Regression Example

A real estate company wants to predict house prices.

Possible outputs:

* $150,000
* $320,000
* $500,000

Since the output is a continuous numerical value, this is a regression problem.

---

# Classification Algorithms

## 1. Logistic Regression

### Basic Idea

Despite its name, Logistic Regression is a classification algorithm. It estimates the probability that an observation belongs to a particular class using the logistic (sigmoid) function.

The sigmoid function converts any input into a value between 0 and 1, which represents probability.

For example:

* Probability = 0.85 → Class = Yes
* Probability = 0.20 → Class = No

The model draws a decision boundary to separate different classes.

### Real-World Use Case

**Loan Approval Prediction**

Banks use Logistic Regression to predict whether an applicant should be approved or rejected based on:

* Income
* Credit score
* Employment history
* Existing debt

### Advantages

* Easy to understand and interpret.
* Fast training and prediction.
* Works well on linearly separable data.
* Produces probability scores.

### Limitations

* Assumes a linear relationship between variables.
* Performs poorly on complex non-linear datasets.
* Sensitive to outliers.

---

## 2. Decision Trees

### Basic Idea

A Decision Tree makes decisions by repeatedly splitting data into smaller groups based on feature values.

The model creates a tree-like structure consisting of:

* Root node
* Internal decision nodes
* Leaf nodes

Each split aims to separate classes as clearly as possible.

For example:

```
Credit Score > 700?
    Yes → Approve Loan
    No → Check Income
          High → Approve
          Low → Reject
```

### Real-World Use Case

**Customer Churn Prediction**

Telecommunication companies use Decision Trees to identify customers who are likely to cancel their subscriptions.

### Advantages

* Easy to visualize and explain.
* Handles numerical and categorical data.
* Captures non-linear relationships.
* Requires little data preparation.

### Limitations

* Can overfit training data.
* Small changes in data may create different trees.
* Lower accuracy compared to ensemble methods.

---

## 3. Random Forest

### Basic Idea

Random Forest is an ensemble learning algorithm that combines multiple Decision Trees.

Instead of relying on a single tree, it:

1. Creates many Decision Trees.
2. Trains each tree on a random sample of data.
3. Allows trees to vote on the final prediction.
4. Chooses the class receiving the most votes.

This process improves accuracy and reduces overfitting.

### Real-World Use Case

**Fraud Detection**

Banks use Random Forest to identify suspicious credit card transactions.

The model analyzes:

* Transaction amount
* Location
* Frequency
* User behavior

and predicts whether a transaction is fraudulent.

### Advantages

* High prediction accuracy.
* Reduces overfitting.
* Handles large datasets effectively.
* Works well with complex relationships.

### Limitations

* More computationally expensive.
* Harder to interpret than a single Decision Tree.
* Requires more memory.

---

## Comparison of Classification Algorithms

| Feature               | Logistic Regression | Decision Tree  | Random Forest   |
| --------------------- | ------------------- | -------------- | --------------- |
| Complexity            | Low                 | Medium         | High            |
| Interpretability      | High                | High           | Low             |
| Handles Non-Linearity | No                  | Yes            | Yes             |
| Risk of Overfitting   | Low                 | High           | Low             |
| Training Speed        | Fast                | Medium         | Slower          |
| Accuracy              | Good                | Good           | Usually Best    |
| Real-World Example    | Loan Approval       | Customer Churn | Fraud Detection |

---

# Classification Metrics

Machine learning models must be evaluated to determine how well they classify data.

---

## 1. Accuracy

### Definition

Accuracy measures the proportion of correctly classified observations out of all observations.

### Formula

[
Accuracy = \frac{TP + TN}{TP + TN + FP + FN}
]

Where:

* TP = True Positive
* TN = True Negative
* FP = False Positive
* FN = False Negative

### What It Measures

Overall correctness of the model.

### Example

If a model correctly predicts 950 out of 1000 cases:

```
Accuracy = 950 / 1000 = 95%
```

---

## 2. Precision

### Definition

Precision measures how many predicted positive cases are actually positive.

### Formula

[
Precision = \frac{TP}{TP + FP}
]

### What It Measures

Reliability of positive predictions.

### Example

Out of 100 loans predicted as safe:

* 90 were truly safe
* 10 were not

```
Precision = 90 / (90 + 10)
          = 90%
```

---

## 3. Recall

### Definition

Recall measures how many actual positive cases are correctly identified.

### Formula

[
Recall = \frac{TP}{TP + FN}
]

### What It Measures

Ability to find all positive cases.

### Example

Out of 100 actual safe borrowers:

* 90 identified correctly
* 10 missed

```
Recall = 90 / (90 + 10)
       = 90%
```

---

## 4. F1-Score

### Definition

F1-Score combines Precision and Recall into a single metric.

### Formula

[
F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}
]

### What It Measures

Balance between Precision and Recall.

### Example

If:

* Precision = 80%
* Recall = 90%

Then:

```
F1 ≈ 84.7%
```

---

## 5. Confusion Matrix

### Definition

A Confusion Matrix is a table showing correct and incorrect predictions.

|                 | Predicted Positive | Predicted Negative |
| --------------- | ------------------ | ------------------ |
| Actual Positive | TP                 | FN                 |
| Actual Negative | FP                 | TN                 |

### What It Measures

Detailed understanding of model performance and types of errors.

---

# Comparison of Classification Metrics

| Metric           | What It Measures                    | Formula       | Sensitive to Class Imbalance? |
| ---------------- | ----------------------------------- | ------------- | ----------------------------- |
| Accuracy         | Overall correctness                 | (TP+TN)/Total | Yes                           |
| Precision        | Correctness of positive predictions | TP/(TP+FP)    | Less sensitive                |
| Recall           | Ability to detect positives         | TP/(TP+FN)    | Less sensitive                |
| F1-Score         | Balance of Precision and Recall     | Harmonic Mean | No                            |
| Confusion Matrix | Complete error breakdown            | Table         | No                            |

---

# Class Imbalance

## Why Can Accuracy Be Misleading?

Class imbalance occurs when one class is much larger than another.

Example:

A loan dataset contains:

* 990 approved loans
* 10 rejected loans

A model predicts every application as approved.

Results:

* Correct predictions = 990
* Total predictions = 1000

```
Accuracy = 99%
```

Although accuracy is extremely high, the model completely fails to identify rejected loans.

Therefore, Accuracy alone can be misleading in imbalanced datasets.

Metrics such as Precision, Recall, and F1-Score provide a more realistic evaluation.

---

## Precision vs Recall in Loan Approval

### When to Prioritize Precision

Choose Precision when false approvals are very costly.

Example:

A bank wants to ensure that approved applicants are truly reliable borrowers.

High Precision means:

* Few risky customers receive loans.
* Lower risk of financial loss.

### When to Prioritize Recall

Choose Recall when missing qualified applicants is more harmful.

Example:

A bank wants to identify all customers who deserve a loan.

High Recall means:

* More eligible customers receive consideration.
* Fewer good applicants are rejected.

### Summary

| Situation                           | Priority  |
| ----------------------------------- | --------- |
| Avoid approving risky borrowers     | Precision |
| Avoid rejecting qualified borrowers | Recall    |
| Need balance between both           | F1-Score  |

---

# Real-World Case Study

## Breast Cancer Classification Using Machine Learning

### Goal

Researchers and healthcare organizations use machine learning to classify tumors as:

* Benign (non-cancerous)
* Malignant (cancerous)

The objective is to support doctors in making faster and more accurate diagnoses.

---

### Data Used

One of the most widely used datasets is the Breast Cancer Wisconsin Dataset.

Features include:

* Radius of tumor cells
* Texture
* Perimeter
* Area
* Smoothness
* Compactness

The target variable has two classes:

* Benign
* Malignant

---

### Classifier Applied

Researchers frequently apply Random Forest classifiers because they:

* Handle complex medical data well.
* Achieve high accuracy.
* Reduce overfitting through ensemble learning.

---

### Key Results and Insights

Studies using Random Forest on this dataset often achieve accuracy above 95%.

Key findings include:

* Random Forest successfully distinguishes malignant tumors from benign tumors.
* Early detection becomes more reliable.
* False diagnoses are reduced.
* Medical professionals receive decision-support tools that improve patient outcomes.

---

# Conclusion

Classification is a fundamental machine learning technique used to predict categorical outcomes. Unlike regression, which predicts numerical values, classification predicts class labels such as approved/rejected, spam/not spam, or benign/malignant. Popular classification algorithms include Logistic Regression, Decision Trees, and Random Forest, each with unique strengths and weaknesses. Model performance is evaluated using metrics such as Accuracy, Precision, Recall, F1-Score, and Confusion Matrix. In real-world applications, especially when dealing with imbalanced data, relying solely on Accuracy can be misleading. Classification models play a critical role in healthcare, finance, cybersecurity, marketing, and many other fields, helping organizations make accurate and data-driven decisions.
