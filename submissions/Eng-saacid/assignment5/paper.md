# Assignment Five – Part A: Classification Theory

## 1. Introduction to Classification

### What is Classification in Machine Learning?

Classification is a supervised machine learning technique used to predict categorical outcomes. The model learns patterns from labeled training data and assigns new observations to predefined classes. Unlike regression, which predicts continuous numerical values, classification predicts discrete labels such as "Yes" or "No", "Approved" or "Rejected", or "Spam" and "Not Spam".

Classification algorithms are widely used in many industries because they help automate decision-making. For example, banks use classification models to determine whether a loan application should be approved, while hospitals use them to predict whether a patient has a particular disease.

### Difference Between Classification and Regression

Although both are supervised learning methods, they solve different types of problems.

* **Classification** predicts categories or labels.
* **Regression** predicts continuous numerical values.

For example, a bank deciding whether to approve a loan is a classification problem because the output is either "Approved" or "Rejected." Predicting the exact price of a house is a regression problem because the output is a numerical value.

**Examples**

* **Classification:** Predict whether a customer will be approved for a loan (Approved or Rejected).
* **Regression:** Predict the selling price of a house based on its features.

---

# 2. Classification Algorithms

## Logistic Regression

### How it Works

Despite its name, Logistic Regression is a classification algorithm. It calculates the probability that an observation belongs to a particular class using the logistic (sigmoid) function. If the probability exceeds a chosen threshold, such as 0.5, the observation is assigned to the positive class.

### Real-World Use Case

Banks use Logistic Regression to predict whether a loan applicant is likely to repay a loan.

### Advantages

* Simple and easy to interpret.
* Fast to train.
* Works well for binary classification.
* Produces probability estimates.

### Limitations

* Assumes a linear relationship between features and the outcome.
* Performance decreases when relationships are highly complex.

---

## Decision Tree

### How it Works

A Decision Tree divides the data into smaller groups by repeatedly selecting the feature that best separates the classes. Each internal node represents a decision, while each leaf node represents the final predicted class.

### Real-World Use Case

Hospitals use Decision Trees to help diagnose diseases based on symptoms and medical test results.

### Advantages

* Easy to understand and visualize.
* Can handle both numerical and categorical data.
* Requires little data preparation.

### Limitations

* Can easily overfit the training data.
* Small changes in data may produce a different tree.

---

## Random Forest

### How it Works

Random Forest is an ensemble learning algorithm that combines many Decision Trees. Each tree is trained using a random sample of the data and features. The final prediction is determined by majority voting among all trees.

### Real-World Use Case

Financial institutions use Random Forest to detect fraudulent transactions and evaluate loan applications.

### Advantages

* High prediction accuracy.
* Reduces overfitting.
* Handles large datasets and many features effectively.
* More robust than a single Decision Tree.

### Limitations

* More computationally expensive.
* Harder to interpret than individual Decision Trees.

---

### Comparison of Classification Algorithms

| Algorithm           | Basic Idea                                                | Advantages                            | Limitations                  |
| ------------------- | --------------------------------------------------------- | ------------------------------------- | ---------------------------- |
| Logistic Regression | Uses the sigmoid function to estimate class probabilities | Fast, simple, interpretable           | Assumes linear relationships |
| Decision Tree       | Splits data into decision rules                           | Easy to visualize and understand      | Can overfit the data         |
| Random Forest       | Combines multiple Decision Trees using majority voting    | Accurate, robust, reduces overfitting | More complex and slower      |

---

# 3. Classification Metrics

## Accuracy

Accuracy measures the proportion of all predictions that are correct.

**Formula**

Accuracy = (TP + TN) / (TP + TN + FP + FN)

Accuracy works well when the dataset is balanced but can be misleading when one class is much larger than the other.

---

## Precision

Precision measures how many predicted positive cases are actually positive.

High precision means the model makes very few false positive predictions.

---

## Recall

Recall measures how many actual positive cases are correctly identified by the model.

A high recall indicates that the model successfully finds most positive cases.

---

## F1-Score

The F1-Score is the harmonic mean of Precision and Recall. It provides a balanced measure when both false positives and false negatives are important.

---

## Confusion Matrix

A Confusion Matrix summarizes prediction results using four values:

* True Positive (TP)
* True Negative (TN)
* False Positive (FP)
* False Negative (FN)

It provides detailed insight into the types of errors made by the model.

### Comparison of Classification Metrics

| Metric           | What it Measures                          | Sensitive to Class Imbalance?              |
| ---------------- | ----------------------------------------- | ------------------------------------------ |
| Accuracy         | Overall percentage of correct predictions | Yes                                        |
| Precision        | Correctness of positive predictions       | No                                         |
| Recall           | Ability to identify actual positive cases | No                                         |
| F1-Score         | Balance between Precision and Recall      | No                                         |
| Confusion Matrix | Counts of TP, FP, TN, and FN              | Shows imbalance rather than being a metric |

---

# 4. Class Imbalance

When one class has many more samples than another, the dataset is imbalanced. In such situations, Accuracy may give a misleading impression of model performance.

For example, imagine that 95% of loan applications are approved and only 5% are rejected. A model that predicts every application as "Approved" would achieve 95% accuracy, even though it completely fails to identify rejected applications.

In loan approval prediction, **Precision** should be prioritized when the bank wants to avoid approving risky applicants. High precision reduces false approvals.

On the other hand, **Recall** should be prioritized when the bank wants to identify as many qualified applicants as possible. High recall reduces the number of good applicants who are mistakenly rejected.

---

# 5. Real-World Case Study

A practical example of classification can be found in peer-to-peer lending platforms such as LendingClub. Researchers developed machine learning models to classify loan applications according to their likelihood of repayment.

The dataset included applicant information such as income, employment history, loan amount, debt ratio, and credit history. Various classification algorithms, including Logistic Regression and Random Forest, were evaluated to predict whether applicants represented low or high credit risk.

The study showed that ensemble methods such as Random Forest generally produced higher prediction accuracy because they combined the predictions of multiple decision trees. These models helped financial institutions improve loan approval decisions, reduce financial risk, and automate the credit evaluation process.

---

# References

Geron, A. (2023). *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* (3rd ed.). O'Reilly Media.

Pedregosa, F., et al. (2011). Scikit-learn: Machine Learning in Python. *Journal of Machine Learning Research*, 12, 2825–2830.

Scikit-learn Developers. (2026). *Scikit-learn User Guide*. https://scikit-learn.org/stable/

Bazarbash, M. (2019). *FinTech in Financial Inclusion: Machine Learning Applications in Lending*. International Monetary Fund.
