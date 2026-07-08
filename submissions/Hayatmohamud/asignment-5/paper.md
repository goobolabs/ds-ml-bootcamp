# Classification in Machine Learning

**Name:** Hayat Mohamud Hassan

---

# Classification in Machine Learning

## Introduction to Classification

### What is Classification in Machine Learning?

Classification is a supervised machine learning technique that predicts a category or class label for new data based on patterns learned from labeled training data. During training, the algorithm learns the relationship between input features and their corresponding class labels. Once trained, it can classify unseen data into one of the predefined categories.

Classification is widely used in many industries because many real-world problems involve making decisions between different classes rather than predicting numerical values.

### How is Classification Different from Regression?

Although both classification and regression are supervised learning techniques, they solve different types of problems.

Classification predicts **categorical outputs**, such as whether an email is spam or not spam, while regression predicts **continuous numerical values**, such as the price of a house or the temperature tomorrow.

For example:

* **Classification:** Predicting whether a loan application should be approved or rejected.
* **Regression:** Predicting the selling price of a used car.

---

## Classification Algorithms

### Logistic Regression

#### How It Works

Logistic Regression estimates the probability that a data point belongs to a particular class using the logistic (sigmoid) function. The output is a probability between 0 and 1. If the probability is above a selected threshold (commonly 0.5), the model assigns the positive class; otherwise, it assigns the negative class.

#### Real-World Use Case

Banks use Logistic Regression to determine whether a customer is likely to repay a loan or default.

#### Advantages

* Easy to understand and implement.
* Fast to train.
* Produces probability estimates.
* Performs well on linearly separable data.

#### Limitations

* Cannot model complex non-linear relationships.
* Performance decreases when classes overlap significantly.
* Sensitive to irrelevant features.

---

### Decision Trees

#### How It Works

A Decision Tree divides the dataset into smaller groups by selecting the best feature at each step. Each decision creates a branch until the final prediction is reached at a leaf node.

#### Real-World Use Case

Hospitals use Decision Trees to assist doctors in diagnosing diseases based on symptoms and medical test results.

#### Advantages

* Easy to visualize and interpret.
* Handles both numerical and categorical data.
* Requires little data preparation.

#### Limitations

* Can easily overfit the training data.
* Small changes in the data may produce a different tree.
* Less accurate than ensemble methods.

---

### Random Forest

#### How It Works

Random Forest combines many Decision Trees. Each tree is trained using a random subset of the data and features. The final prediction is determined by majority voting among all trees.

#### Real-World Use Case

Financial institutions use Random Forest models to detect fraudulent credit card transactions.

#### Advantages

* High prediction accuracy.
* Reduces overfitting.
* Works well with large datasets.
* Handles missing values better than a single Decision Tree.

#### Limitations

* More computationally expensive.
* Harder to interpret.
* Requires more memory.

---

## Comparison of Classification Algorithms

| Algorithm           | Basic Idea                            | Main Advantage     | Main Limitation                    | Example Application |
| ------------------- | ------------------------------------- | ------------------ | ---------------------------------- | ------------------- |
| Logistic Regression | Uses probability to classify data     | Simple and fast    | Cannot model complex relationships | Loan approval       |
| Decision Tree       | Makes decisions through tree branches | Easy to understand | Can overfit                        | Medical diagnosis   |
| Random Forest       | Combines multiple decision trees      | High accuracy      | Less interpretable                 | Fraud detection     |

---

# Classification Metrics

## Accuracy

Accuracy measures the percentage of predictions that are correct.

**Formula**

Accuracy = (Correct Predictions) ÷ (Total Predictions)

Accuracy works well when all classes contain similar numbers of samples.

---

## Precision

Precision measures how many predicted positive cases are actually positive.

A high precision means the model makes very few false positive predictions.

This metric is important when false positives are costly.

---

## Recall

Recall measures how many actual positive cases are successfully identified.

A high recall means the model misses very few positive cases.

Recall is important when missing positive cases could have serious consequences.

---

## F1-Score

The F1-Score combines Precision and Recall into a single metric by calculating their harmonic mean.

It is useful when the dataset is imbalanced because it balances both false positives and false negatives.

---

## Confusion Matrix

A Confusion Matrix summarizes a classifier's predictions by showing:

* True Positives (TP)
* True Negatives (TN)
* False Positives (FP)
* False Negatives (FN)

It provides detailed information about model performance beyond overall accuracy.

---

## Comparison of Classification Metrics

| Metric           | What It Measures                     | Sensitive to Class Imbalance? |
| ---------------- | ------------------------------------ | ----------------------------- |
| Accuracy         | Overall correctness                  | Yes                           |
| Precision        | Correctness of positive predictions  | No                            |
| Recall           | Ability to detect positive cases     | No                            |
| F1-Score         | Balance between Precision and Recall | No                            |
| Confusion Matrix | Counts all prediction outcomes       | Helps analyze imbalance       |

---

# Class Imbalance

Class imbalance occurs when one class contains significantly more examples than another.

For example, suppose a loan dataset contains:

* 990 approved loans
* 10 rejected loans

A model that predicts every application as approved would achieve 99% accuracy, even though it completely fails to identify rejected loans.

Therefore, relying only on accuracy can give a false impression of good performance.

### When Should Precision Be Prioritized?

Precision should be prioritized when false positives are expensive.

**Loan Approval Example**

If a bank approves a loan for someone who is unlikely to repay it, the bank may lose money. Therefore, the bank should focus on high precision to reduce incorrect approvals.

### When Should Recall Be Prioritized?

Recall should be prioritized when missing positive cases is more harmful than making extra positive predictions.

For example, if the goal is to identify customers who are likely to default on loans, missing a risky customer could result in significant financial losses. In this case, high recall is more important.

---

# Real-World Case Study

## Credit Card Fraud Detection

### Goal

A financial institution wanted to detect fraudulent credit card transactions as quickly as possible to reduce financial losses and protect customers.

### Data Used

The dataset contained transaction information such as:

* Transaction amount
* Transaction time
* Customer behavior
* Merchant information
* Historical fraud labels

Because fraudulent transactions are rare, the dataset was highly imbalanced.

### Classification Algorithm

The researchers applied the Random Forest classifier because it performs well on complex datasets and handles imbalanced data effectively.

### Results

The Random Forest model achieved high fraud detection performance while maintaining a low false positive rate. Compared with a single Decision Tree, it produced more accurate predictions and generalized better to unseen transactions.

This case demonstrates how classification models can improve security, reduce financial losses, and support real-time decision-making in the banking industry.

---

# References

1. Géron, A. (2023). *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* (3rd ed.). O'Reilly Media.
2. Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
3. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.
4. Scikit-learn Documentation. https://scikit-learn.org
5. IBM Machine Learning Documentation. https://www.ibm.com/topics/machine-learning
