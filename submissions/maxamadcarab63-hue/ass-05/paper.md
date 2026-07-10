# **Introduction to Classification in Machine Learning**

## Introduction

Machine Learning (ML) is a branch of artificial intelligence that enables computers to learn patterns from data and make predictions or decisions without being explicitly programmed. One of the most common supervised learning tasks is **classification**, where the goal is to assign data into predefined categories or classes. Classification techniques are widely used in healthcare, finance, education, business, cybersecurity, and many other fields to solve real-world problems.

---

# 1. What is Classification in Machine Learning?

Classification is a supervised machine learning technique that predicts the category or class of a data point based on previously labeled training data. During training, the model learns the relationship between input features and their corresponding class labels. Once trained, it can classify new, unseen data into one of the predefined classes.

Examples of classification include:

* Email Spam vs. Not Spam
* Fraudulent vs. Legitimate Transactions
* Disease Positive vs. Disease Negative
* Student Pass vs. Fail

## Difference Between Classification and Regression

Although both classification and regression belong to supervised learning, they solve different types of problems.

* **Classification** predicts **categorical outputs**, such as "Yes" or "No," "Approved" or "Rejected."
* **Regression** predicts **continuous numerical values**, such as price, temperature, or salary.

### Examples

**Classification Example:**
A bank predicts whether a loan application should be **approved** or **rejected** based on the applicant's financial information.

**Regression Example:**
A real estate company predicts the **selling price** of a house based on its size, location, and number of rooms.

---

# 2. Classification Algorithms

## Logistic Regression

### Basic Idea

Despite its name, Logistic Regression is a classification algorithm. It uses a mathematical function called the **sigmoid function** to estimate the probability that an observation belongs to a particular class. The output probability ranges from 0 to 1, and a threshold (commonly 0.5) determines the predicted class.

### Real-World Use Case

Banks use Logistic Regression to predict whether a customer is likely to **default on a loan**.

### Advantages

* Simple and easy to understand.
* Fast to train.
* Produces probability estimates.
* Performs well on linearly separable data.

### Limitations

* Assumes a linear relationship between variables.
* Performs poorly with complex non-linear data.
* Sensitive to outliers.

---

## Decision Trees

### Basic Idea

A Decision Tree classifies data by asking a series of questions. It repeatedly splits the dataset into smaller groups based on the feature that best separates the classes until reaching a final decision at a leaf node.

### Real-World Use Case

Hospitals use Decision Trees to assist doctors in diagnosing diseases based on patient symptoms and medical test results.

### Advantages

* Easy to visualize and interpret.
* Handles both numerical and categorical data.
* Requires little data preparation.

### Limitations

* Can easily overfit the training data.
* Sensitive to small changes in data.
* Less accurate than ensemble methods.

---

## Random Forest

### Basic Idea

Random Forest is an ensemble learning algorithm that builds many Decision Trees using different random samples of the training data. Each tree makes its own prediction, and the final prediction is determined by majority voting.

### Real-World Use Case

Credit card companies use Random Forest to detect fraudulent transactions.

### Advantages

* High prediction accuracy.
* Reduces overfitting.
* Handles missing values and large datasets effectively.
* Works well with complex relationships.

### Limitations

* More computationally expensive.
* Less interpretable than a single Decision Tree.
* Requires more memory.

---

## Comparison of Classification Algorithms

| Algorithm           | Basic Idea                                     | Common Use              | Advantages                  | Limitations              |
| ------------------- | ---------------------------------------------- | ----------------------- | --------------------------- | ------------------------ |
| Logistic Regression | Uses probability to classify data              | Loan default prediction | Simple, fast, interpretable | Poor for non-linear data |
| Decision Tree       | Splits data into branches using decision rules | Medical diagnosis       | Easy to understand          | Can overfit              |
| Random Forest       | Combines many decision trees                   | Fraud detection         | High accuracy, robust       | More complex and slower  |

---

# 3. Classification Metrics

Evaluating a classification model requires appropriate performance metrics.

## Accuracy

Accuracy measures the proportion of correctly classified observations.

**Formula:**

Accuracy = (Correct Predictions) ÷ (Total Predictions)

It is useful when the dataset has balanced classes.

---

## Precision

Precision measures how many predicted positive cases are actually positive.

**Formula:**

Precision = True Positives ÷ (True Positives + False Positives)

High precision means there are few false positive predictions.

---

## Recall

Recall measures how many actual positive cases are correctly identified.

**Formula:**

Recall = True Positives ÷ (True Positives + False Negatives)

High recall means the model misses very few positive cases.

---

## F1-Score

The F1-Score combines Precision and Recall into a single metric using their harmonic mean.

**Formula:**

F1 = 2 × (Precision × Recall) ÷ (Precision + Recall)

It is useful when both false positives and false negatives are important.

---

## Confusion Matrix

A Confusion Matrix summarizes classification results using four outcomes:

* **True Positive (TP):** Correct positive prediction.
* **True Negative (TN):** Correct negative prediction.
* **False Positive (FP):** Incorrect positive prediction.
* **False Negative (FN):** Incorrect negative prediction.

These values help calculate Accuracy, Precision, Recall, and F1-Score.

---

## Comparison of Classification Metrics

| Metric           | What It Measures                        | Sensitive to Class Imbalance? |
| ---------------- | --------------------------------------- | ----------------------------- |
| Accuracy         | Overall correctness                     | Yes (can be misleading)       |
| Precision        | Correctness of positive predictions     | Less sensitive                |
| Recall           | Ability to identify actual positives    | Less sensitive                |
| F1-Score         | Balance between Precision and Recall    | Suitable for imbalanced data  |
| Confusion Matrix | Complete summary of prediction outcomes | Helps analyze imbalance       |

---

# 4. Class Imbalance

Class imbalance occurs when one class contains significantly more observations than another.

For example, in loan approval, 95% of applicants may repay their loans while only 5% default.

## Why Accuracy Can Be Misleading

Suppose a dataset contains:

* 950 good borrowers
* 50 bad borrowers

If a model predicts **every applicant as a good borrower**, it achieves:

Accuracy = 950 / 1000 = **95%**

Although the accuracy appears excellent, the model fails to identify any risky borrowers, making it practically useless.

Therefore, Precision, Recall, and F1-Score are often better evaluation metrics for imbalanced datasets.

---

## Precision vs. Recall in Loan Approval

### When Precision Is More Important

Precision should be prioritized when the bank wants to avoid **incorrectly rejecting trustworthy applicants**.

A high precision model ensures that applicants predicted as risky are truly risky.

### When Recall Is More Important

Recall should be prioritized when the bank wants to identify **as many risky borrowers as possible**.

Missing a borrower who will default may result in substantial financial losses.

In practice, banks often seek a balance between Precision and Recall depending on their risk management strategy.

---

# 5. Real-World Case Study

## Credit Card Fraud Detection Using Random Forest

### Goal

A major financial institution aimed to automatically identify fraudulent credit card transactions in real time while minimizing financial losses.

### Data Used

The project used a large dataset containing thousands of credit card transactions. Features included:

* Transaction amount
* Transaction time
* Merchant information
* Customer spending behavior
* Historical transaction patterns

Because fraudulent transactions represented only a very small percentage of all transactions, the dataset was highly imbalanced.

### Classification Algorithm

Researchers applied the **Random Forest classifier**, which combines multiple Decision Trees to improve prediction accuracy and reduce overfitting.

### Key Results

The Random Forest model successfully detected fraudulent transactions with high Precision and Recall, outperforming several traditional classification methods. It significantly reduced false alarms while accurately identifying suspicious transactions. The study demonstrated that ensemble learning techniques are highly effective for fraud detection, especially when dealing with large and imbalanced datasets.

