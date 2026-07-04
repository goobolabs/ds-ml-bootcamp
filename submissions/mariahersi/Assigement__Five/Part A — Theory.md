# Introduction to Classification in Machine Learning

## Introduction

Machine Learning (ML) is a branch of Artificial Intelligence (AI) that
enables computers to learn patterns from data and make predictions
without being explicitly programmed. One of the most common supervised
learning tasks is **classification**, where the goal is to assign data
into predefined categories. Classification is widely used in healthcare,
finance, education, cybersecurity, and business to support better
decision-making.

## 1. What is Classification in Machine Learning?

Classification is a supervised machine learning technique that predicts
the category or class of an input based on previously labeled training
data. The model learns patterns from historical examples and uses them
to classify new, unseen data.

For example, an email can be classified as **spam** or **not spam**, or
a bank transaction can be classified as **fraudulent** or
**legitimate**.

### Difference Between Classification and Regression

-   **Classification** predicts **categorical values** (labels or
    classes).
-   **Regression** predicts **continuous numerical values**.

**Classification Example:** Predicting whether a customer will repay a
loan (**Approved** or **Rejected**).

**Regression Example:** Predicting the price of a house based on its
size, location, and number of rooms.

## 2. Classification Algorithms

### Logistic Regression

**How it Works:** Logistic Regression estimates the probability that an
observation belongs to a particular class using the sigmoid function.

**Real-World Use Case:** Loan approval prediction.

**Advantages:** Simple, fast, interpretable, and provides probability
estimates.

**Limitations:** Cannot model complex non-linear relationships.

### Decision Trees

**How it Works:** Decision Trees split data into smaller groups using
decision rules until a final prediction is reached.

**Real-World Use Case:** Medical diagnosis.

**Advantages:** Easy to understand and works with numerical and
categorical data.

**Limitations:** Can overfit the training data.

### Random Forest

**How it Works:** Random Forest combines many Decision Trees and
predicts using majority voting.

**Real-World Use Case:** Credit card fraud detection.

**Advantages:** High accuracy, reduces overfitting, handles large
datasets.

**Limitations:** More computationally expensive and less interpretable.

  ----------------------------------------------------------------------------
  Algorithm    Basic Idea      Common Use Case   Advantages    Limitations
  ------------ --------------- ----------------- ------------- ---------------
  Logistic     Uses            Loan approval     Simple and    Limited for
  Regression   probabilities                     fast          complex
                                                               patterns

  Decision     Tree-based      Medical diagnosis Easy to       Overfitting
  Tree         rules                             interpret     

  Random       Ensemble of     Fraud detection   High accuracy Less
  Forest       trees                                           interpretable
  ----------------------------------------------------------------------------

## 3. Classification Metrics

-   **Accuracy:** Percentage of correct predictions.
-   **Precision:** Correctness of positive predictions.
-   **Recall:** Ability to identify actual positive cases.
-   **F1-Score:** Harmonic mean of Precision and Recall.
-   **Confusion Matrix:** Shows TP, TN, FP, and FN.

  Metric             What It Measures                  Sensitive to Class Imbalance?
  ------------------ --------------------------------- -------------------------------
  Accuracy           Overall correctness               Yes
  Precision          Positive prediction quality       Less
  Recall             Positive detection rate           Less
  F1-Score           Balance of Precision and Recall   No
  Confusion Matrix   Prediction breakdown              No

## 4. Class Imbalance

When one class has many more examples than another, accuracy may be
misleading. For example, if 95% of loan applications are approved,
predicting "Approved" for every applicant gives 95% accuracy while
failing to identify rejected applicants.

-   **Prioritize Precision:** When approving risky loans would be
    costly.
-   **Prioritize Recall:** When identifying as many risky applicants as
    possible is the goal.

## 5. Real-World Case Study

### Credit Card Fraud Detection Using Random Forest

**Goal:** Detect fraudulent transactions.

**Data Used:** Transaction amount, time, customer behavior, device
information, location, and historical transaction data.

**Classifier:** Random Forest.

**Results:** High fraud detection accuracy with strong Precision and
Recall, helping reduce financial losses.

## Conclusion

Classification is a fundamental supervised learning technique used to
predict categories. Logistic Regression, Decision Trees, and Random
Forest each have different strengths. Evaluating models with Accuracy,
Precision, Recall, F1-Score, and the Confusion Matrix provides a more
complete understanding of model performance, especially when datasets
are imbalanced.

## References

1.  Géron, A. (2023). *Hands-On Machine Learning with Scikit-Learn,
    Keras & TensorFlow* (3rd ed.).
2.  Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*.
3.  James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An
    Introduction to Statistical Learning* (2nd ed.).
4.  Fawcett, T. (2006). *An Introduction to ROC Analysis*.
5.  European Credit Card Fraud Detection Dataset (Kaggle).
