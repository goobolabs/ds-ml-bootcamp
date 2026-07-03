# Assignment Five – Classification Theory and Practice (Part A)

## Classification in Machine Learning

### Student Name:

Nimco Nuur

---

# Introduction to Classification

Classification is one of the most important supervised learning techniques in Machine Learning. It is used to predict the category or class of an object based on previously labeled data. A classification model learns patterns from historical data and then predicts which predefined class a new observation belongs to.

The main objective of classification is to assign data into discrete categories. The model is trained using labeled examples, where both the input features and the correct output labels are known. After training, the model can predict the class of new unseen data.

Classification is widely used in many industries such as healthcare, banking, education, cybersecurity, and e-commerce. Common applications include disease diagnosis, spam email detection, fraud detection, loan approval prediction, customer churn prediction, and image recognition.

For this assignment, classification is used to predict whether a loan application should be **Approved** or **Rejected** based on applicant information such as income, credit score, employment years, previous loan defaults, collateral, and requested loan amount.

---

# Classification vs Regression

Although both classification and regression are supervised learning techniques, they solve different types of problems.

Classification predicts categorical values, while regression predicts continuous numerical values.

For example, a bank may want to predict whether a customer will be approved for a loan. The possible outputs are **Approved** or **Rejected**, making this a classification problem.

On the other hand, predicting the exact selling price of a house is a regression problem because the output is a continuous numerical value such as $150,000 or $250,000.

| Classification                     | Regression                      |
| ---------------------------------- | ------------------------------- |
| Predicts categories                | Predicts numerical values       |
| Output is discrete                 | Output is continuous            |
| Example: Loan Approved or Rejected | Example: House Price Prediction |
| Uses classification algorithms     | Uses regression algorithms      |

---

# Classification Algorithms

Several algorithms can perform classification tasks. This paper discusses Logistic Regression, Decision Tree, and Random Forest.

---

## Logistic Regression

### Basic Idea

Logistic Regression is a supervised learning algorithm used for binary classification problems. Instead of predicting continuous values, it estimates the probability that an observation belongs to a particular class.

The algorithm uses the sigmoid function to convert predictions into probabilities between 0 and 1. If the probability is greater than a chosen threshold (usually 0.5), the model predicts the positive class.

### Real-World Use Case

Banks use Logistic Regression to predict whether a customer is likely to repay a loan or default.

### Advantages

* Simple and easy to understand.
* Fast to train.
* Works well for binary classification.
* Produces interpretable results.

### Limitations

* Assumes a linear relationship between features and the target.
* May perform poorly on complex datasets.
* Sensitive to outliers if data is not properly preprocessed.

---

## Decision Tree

### Basic Idea

A Decision Tree is a supervised learning algorithm that makes predictions by splitting data into branches based on feature values. Each internal node represents a decision, each branch represents an outcome, and each leaf node represents the final prediction.

The model continues splitting until it reaches a stopping criterion or pure leaf nodes.

### Real-World Use Case

Banks use Decision Trees to evaluate loan applications by considering income, employment history, collateral, and credit score.

### Advantages

* Easy to visualize and interpret.
* Handles numerical and categorical data.
* Requires little data preprocessing.
* Captures non-linear relationships.

### Limitations

* Can easily overfit training data.
* Small data changes may produce different trees.
* Usually less accurate than ensemble methods.

---

## Random Forest

### Basic Idea

Random Forest is an ensemble learning algorithm that combines multiple Decision Trees. Each tree is trained using a random subset of the data and features. The final prediction is determined by majority voting among all trees.

Because many trees work together, Random Forest generally provides better accuracy and reduces overfitting.

### Real-World Use Case

Financial institutions use Random Forest to predict loan approvals, detect fraud, and evaluate credit risk.

### Advantages

* High prediction accuracy.
* Reduces overfitting.
* Handles large datasets effectively.
* Works well with missing and noisy data.

### Limitations

* More computationally expensive.
* Harder to interpret than a single Decision Tree.
* Training time increases with more trees.

---

# Classification Metrics

Classification models are evaluated using several performance metrics.

## Accuracy

Accuracy measures the proportion of correctly classified observations among all predictions.

Accuracy is useful when the classes are balanced.

---

## Precision

Precision measures how many predicted positive cases are actually positive.

High precision means the model produces few false positive predictions.

---

## Recall

Recall measures how many actual positive cases are correctly identified.

A high recall indicates that the model misses very few positive cases.

---

## F1-Score

The F1-Score is the harmonic mean of Precision and Recall.

It provides a balanced measure when both false positives and false negatives are important.

---

## Confusion Matrix

A Confusion Matrix summarizes prediction results into four categories:

* True Positive (TP)
* True Negative (TN)
* False Positive (FP)
* False Negative (FN)

It helps understand where the model makes mistakes.

---

# Comparison of Classification Metrics

| Metric           | Measures                        | Best Used When             | Sensitive to Class Imbalance |
| ---------------- | ------------------------------- | -------------------------- | ---------------------------- |
| Accuracy         | Overall correct predictions     | Balanced datasets          | Yes                          |
| Precision        | Correct positive predictions    | False positives are costly | No                           |
| Recall           | Correct detection of positives  | False negatives are costly | No                           |
| F1-Score         | Balance of Precision and Recall | Imbalanced datasets        | No                           |
| Confusion Matrix | Detailed prediction results     | Any classification task    | No                           |

---

# Class Imbalance

Class imbalance occurs when one class contains significantly more observations than another.

In such cases, Accuracy can be misleading. For example, if 95% of loan applications are approved and only 5% are rejected, a model that predicts every application as approved would achieve 95% Accuracy while completely failing to identify rejected applications.

Therefore, relying only on Accuracy may hide poor model performance.

For loan approval prediction, Precision should be prioritized when the bank wants to avoid approving risky customers who may fail to repay loans.

Recall should be prioritized when the bank wants to identify as many eligible customers as possible, ensuring that qualified applicants are not rejected unnecessarily.

Using Precision, Recall, and F1-Score together provides a more complete evaluation than Accuracy alone.

---

# Real-World Case Study

One practical application of classification is loan approval prediction in the banking industry.

The goal is to determine whether a loan applicant should be approved based on historical customer information. Typical features include income, employment history, credit score, collateral, previous loan defaults, and requested loan amount.

Machine learning algorithms such as Logistic Regression, Decision Tree, and Random Forest are commonly used for this task.

Among these algorithms, Random Forest often provides the highest prediction accuracy because it combines multiple Decision Trees and reduces overfitting.

Banks use these predictions to reduce financial risk, improve decision-making, speed up loan processing, and increase customer satisfaction.

---

# Conclusion

Classification is an essential machine learning technique used to predict categorical outcomes. Compared to regression, classification focuses on assigning observations to predefined classes instead of predicting continuous values.

Algorithms such as Logistic Regression, Decision Tree, and Random Forest each have strengths and weaknesses. Logistic Regression is simple and interpretable, Decision Tree is easy to understand, while Random Forest generally provides the highest accuracy by combining many trees.

Evaluating models using Accuracy, Precision, Recall, F1-Score, and Confusion Matrix provides a comprehensive understanding of model performance.

In loan approval prediction, selecting the appropriate classification algorithm helps financial institutions make accurate, fair, and efficient lending decisions.

