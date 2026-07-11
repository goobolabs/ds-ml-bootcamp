# Assignment Five: Classification — Theory and Practice

## Part A: Theory

### 1. Introduction to Classification

Classification is one of the main tasks in Machine Learning. It is a supervised learning technique that predicts the category or class of new data based on patterns learned from labeled training data. The output of a classification model is a discrete label, such as "Yes" or "No," "Approved" or "Rejected," or "Spam" or "Not Spam."

Regression is another supervised learning technique, but instead of predicting categories, it predicts continuous numerical values. The main difference is that classification produces class labels, while regression predicts numbers.

A real-life example of classification is loan approval prediction, where a bank decides whether to approve or reject a customer's loan application. A real-life example of regression is predicting the price of a house based on its size, location, and number of rooms.

---

## 2. Classification Algorithms

### Logistic Regression

Logistic Regression is a statistical classification algorithm used for binary classification problems. It estimates the probability that an observation belongs to a particular class by using the logistic (sigmoid) function.

**Real-world application:** Loan approval prediction.

**Advantages**

* Simple and easy to interpret.
* Fast to train.
* Works well for linearly separable data.

**Limitations**

* Cannot model complex nonlinear relationships.
* Performance decreases when classes are not linearly separable.

---

### Decision Tree

A Decision Tree is a machine learning algorithm that splits data into smaller groups based on feature values. Each internal node represents a decision, and each leaf node represents a predicted class.

**Real-world application:** Medical diagnosis.

**Advantages**

* Easy to understand and visualize.
* Handles both numerical and categorical data.
* Requires little data preparation.

**Limitations**

* Can easily overfit training data.
* Small changes in the data may produce different trees.

---

### Random Forest

Random Forest is an ensemble learning algorithm that combines many Decision Trees. Each tree makes its own prediction, and the final prediction is determined by majority voting.

**Real-world application:** Credit risk assessment in banks.

**Advantages**

* High prediction accuracy.
* Reduces overfitting compared to a single Decision Tree.
* Handles large datasets effectively.

**Limitations**

* More computationally expensive.
* Harder to interpret than a single Decision Tree.

---

### Comparison of Algorithms

| Algorithm           | Basic Idea                                       | Strength                     | Limitation                   |
| ------------------- | ------------------------------------------------ | ---------------------------- | ---------------------------- |
| Logistic Regression | Uses a sigmoid function to predict probabilities | Simple and interpretable     | Assumes linear relationships |
| Decision Tree       | Splits data into branches based on rules         | Easy to visualize            | Can overfit                  |
| Random Forest       | Combines many Decision Trees                     | High accuracy and robustness | Less interpretable           |

---

## 3. Classification Metrics

### Accuracy

Accuracy measures the proportion of correctly classified observations among all observations.

**Formula**

Accuracy = (TP + TN) / (TP + TN + FP + FN)

---

### Precision

Precision measures how many of the predicted positive cases are actually positive.

High precision means the model produces fewer false positive predictions.

---

### Recall

Recall measures how many actual positive cases are correctly identified by the model.

High recall means the model misses fewer positive cases.

---

### F1-Score

The F1-Score is the harmonic mean of Precision and Recall. It provides a balanced measure when both metrics are important.

---

### Confusion Matrix

A Confusion Matrix is a table that summarizes prediction results.

It contains:

* True Positive (TP)
* True Negative (TN)
* False Positive (FP)
* False Negative (FN)

The confusion matrix helps identify the types of prediction errors made by the classifier.

---

### Comparison of Evaluation Metrics

| Metric           | Measures                             | Sensitive to Class Imbalance |
| ---------------- | ------------------------------------ | ---------------------------- |
| Accuracy         | Overall correctness                  | Yes                          |
| Precision        | Correctness of positive predictions  | No                           |
| Recall           | Ability to detect positive cases     | No                           |
| F1-Score         | Balance between Precision and Recall | No                           |
| Confusion Matrix | Detailed prediction outcomes         | No                           |

---

## 4. Class Imbalance

Class imbalance occurs when one class contains significantly more samples than another. In such situations, Accuracy can be misleading because a model may predict only the majority class and still achieve a high accuracy score.

For example, if 95% of loan applications are approved, a model that predicts every application as approved will achieve 95% accuracy but completely fail to identify rejected applications.

Precision should be prioritized when approving a risky customer has a high financial cost. A bank wants to ensure that customers predicted as approved are truly reliable.

Recall should be prioritized when missing qualified applicants is more costly than approving additional applications. A bank may want to identify as many eligible customers as possible, even if some additional reviews are required.

---

## 5. Real-World Case Study

A common real-world application of classification is credit risk assessment in the banking sector.

The goal is to determine whether a loan applicant should be approved or rejected based on financial information such as income, credit score, employment history, collateral, and previous loan defaults.

Banks typically use classification algorithms such as Logistic Regression, Decision Trees, and Random Forest to predict loan approval decisions. These models analyze historical loan data to identify patterns associated with successful repayments.

Studies have shown that Random Forest often achieves higher prediction accuracy than individual Decision Trees because it combines the predictions of multiple trees, reducing overfitting and improving generalization. As a result, many financial institutions use Random Forest and other ensemble methods to support loan approval decisions and reduce financial risk.

---

# References

1. Géron, A. (2023). *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* (3rd Edition). O'Reilly Media.

2. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning* (2nd Edition). Springer.

3. Scikit-learn Developers. *Scikit-learn User Guide*. https://scikit-learn.org/stable/

4. Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
