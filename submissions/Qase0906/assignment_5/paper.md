# Part A — Theory

## 1. Introduction to Classification

### What is classification in Machine Learning?

Classification is a type of supervised learning in machine learning where the goal is to predict a category or label based on input data. The model learns from labeled examples and then assigns new data into predefined classes such as “Yes” or “No”, “Spam” or “Not Spam”, or “Approved” or “Rejected”. In classification, the output is discrete, meaning it belongs to a specific group rather than a continuous value.

### How is it different from regression?

Classification and regression are both supervised learning techniques, but they differ in their output. Classification predicts categories or classes, while regression predicts continuous numerical values. For example, classification might predict whether a loan is approved or not, while regression might predict the exact loan amount a customer should receive.

### Real-life examples
- Classification example: Email spam detection, where emails are classified as “Spam” or “Not Spam”.
- Regression example: Predicting house prices based on features like size, location, and number of rooms.


## 2. Classification Algorithms

### 2.1 Logistic Regression

Logistic Regression is a statistical model used for binary classification problems. It works by estimating probabilities using a sigmoid function and then classifying outputs based on a threshold (usually 0.5).

- How it works: It calculates a weighted sum of input features and applies a sigmoid function to produce a probability between 0 and 1.
- Use case: Loan approval prediction, medical diagnosis (disease vs no disease).
- Advantages: Simple, fast, and easy to interpret.
- Limitations: Assumes linear relationships between features and target, and may not perform well on complex data.


### 2.2 Decision Trees

Decision Trees are models that split data into branches based on feature conditions until a final decision is reached.

- How it works: The model repeatedly splits data using conditions (e.g., Income > 50,000) until it reaches a leaf node representing a class.
- Use case: Credit scoring, customer segmentation, fraud detection.
- Advantages: Easy to understand, handles both numerical and categorical data, no need for scaling.
- Limitations: Can overfit the training data and become unstable with small changes in data.


### 2.3 Random Forest

Random Forest is an ensemble learning method that combines multiple decision trees to improve performance.

- How it works: It builds many decision trees using random subsets of data and features. Each tree makes a prediction, and the final output is based on majority voting.
- Use case: Financial risk prediction, disease classification, loan approval systems.
- Advantages: High accuracy, reduces overfitting, works well with large datasets.
- Limitations: Less interpretable than a single decision tree and computationally more expensive.



## 3. Classification Metrics

Definitions
- Accuracy: Measures the proportion of correct predictions out of all predictions.
- Precision: Measures how many predicted positive cases are actually positive.
- Recall: Measures how many actual positive cases are correctly identified.
- F1-Score: Harmonic mean of precision and recall, balances both metrics.
- Confusion Matrix: A table that shows correct and incorrect predictions in four categories (TP, TN, FP, FN).


## Comparison of Classification Metrics

| Metric        | What it Measures                                  | Sensitive to Class Imbalance |
|--------------|---------------------------------------------------|------------------------------|
| Accuracy      | Overall correctness of predictions               | Yes (can be misleading)      |
| Precision     | How many predicted positives are actually correct | Less sensitive               |
| Recall        | How many actual positives are correctly detected  | Very important               |
| F1-Score      | Balance between Precision and Recall              | Moderately sensitive         |
| Confusion Matrix | Full breakdown of TP, TN, FP, FN               | Not a single metric         |



## 4. Class Imbalance

Accuracy can be misleading when classes are imbalanced because a model may predict the majority class most of the time and still achieve high accuracy. For example, if 90% of loan applications are “Approved”, a model that always predicts “Approved” will achieve 90% accuracy but will fail to detect rejected cases.

In loan approval systems, Recall is important when we want to identify all good applicants, even if some incorrect approvals happen. However, Precision is important when we want to avoid approving risky applicants. Therefore, if a bank wants to reduce financial risk, it should prioritize Precision. If it wants to approve as many good customers as possible, it should prioritize Recall.

## 5. Real-World Case Study

A real-world example of classification is credit card fraud detection in banking systems. The goal of this system is to identify fraudulent transactions and prevent financial loss.

The dataset used typically includes transaction amount, location, time, and user behavior patterns. Machine learning models such as Logistic Regression, Decision Trees, and Random Forest are commonly used for classification.

In many studies, Random Forest performs well because it handles complex patterns and reduces overfitting. The main challenge in this problem is class imbalance, as fraud cases are very rare compared to normal transactions. Therefore, metrics like Recall and F1-score are more important than Accuracy. The key insight from such systems is that machine learning can significantly reduce financial fraud by automatically detecting suspicious transactions in real time.

References
- Scikit-learn Documentation: https://scikit-learn.org
- James, G. et al. (2021). An Introduction to Statistical Learning
- IBM Machine Learning Concepts: https://www.ibm.com/cloud/learn/machine-learning
- Khan Academy: Machine Learning Basics






