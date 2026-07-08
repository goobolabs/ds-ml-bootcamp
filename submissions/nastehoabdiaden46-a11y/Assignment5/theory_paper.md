Assignment Five – Part A: Theory

Classification in Machine Learning

Introduction to Classification

Classification is a supervised Machine Learning technique used to predict or assign data into predefined categories or classes. In classification tasks, the model learns patterns from labeled historical data and uses those patterns to classify new unseen data. The primary goal of classification is to determine which category an observation belongs to.

Classification differs from regression because classification predicts categorical outputs while regression predicts continuous numerical values. Classification outputs labels such as "Approved" or "Rejected," whereas regression outputs numerical values such as house prices or sales amounts.

Real-life examples:

Classification Example:
Loan approval prediction where a bank determines whether a customer should be approved or rejected for a loan.

Regression Example:
Predicting the price of a house based on features such as location, size, and number of bedrooms.

---

Classification Algorithms

Logistic Regression

Logistic Regression is a classification algorithm that predicts probabilities and converts them into categories using a sigmoid function. The model calculates the probability of an observation belonging to a particular class.

Real-world use case:
Loan default prediction.

Advantages:

- Easy to understand and implement
- Fast training process
- Works well for linearly separable data

Limitations:

- Poor performance with complex relationships
- Sensitive to outliers
- Assumes linear relationships between variables

---

Decision Trees

Decision Trees classify data by splitting it into branches according to feature values. The model creates decision nodes that continue branching until reaching a final prediction.

Real-world use case:
Medical diagnosis systems.

Advantages:

- Easy to visualize and interpret
- Handles both categorical and numerical data
- Requires minimal preprocessing

Limitations:

- Can overfit training data
- Sensitive to small changes in data
- Lower generalization ability

---

Random Forest

Random Forest is an ensemble learning algorithm that combines many decision trees. The final prediction is determined using majority voting among all trees.

Real-world use case:
Financial fraud detection.

Advantages:

- High prediction accuracy
- Reduces overfitting
- Performs well on large datasets

Limitations:

- Computationally expensive
- Harder to interpret
- Longer training time

---

Classification Metrics

Classification metrics are used to evaluate model performance.

Accuracy

Accuracy measures the proportion of correctly predicted observations among all predictions.

Formula:

Accuracy = Correct Predictions / Total Predictions

Precision

Precision measures how many predicted positive cases are actually positive.

Formula:

Precision = TP / (TP + FP)

Recall

Recall measures how many actual positive cases were correctly identified.

Formula:

Recall = TP / (TP + FN)

F1-Score

F1-Score combines Precision and Recall into one balanced metric.

Formula:

F1 = 2 × ((Precision × Recall) / (Precision + Recall))

Confusion Matrix

A Confusion Matrix displays model predictions using:

- True Positive (TP)
- True Negative (TN)
- False Positive (FP)
- False Negative (FN)

Comparison Table

Metric| What it Measures| Sensitivity to Class Imbalance
Accuracy| Overall correctness| High
Precision| Correct positive predictions| Medium
Recall| Ability to identify positives| Medium
F1-Score| Balance of precision and recall| Low
Confusion Matrix| Complete prediction details| Low

---

Class Imbalance

Class imbalance occurs when one class contains significantly more observations than another class. Accuracy can become misleading because a model can predict the majority class frequently and still produce high accuracy.

For example, in a loan approval dataset, if 95% of applicants are approved and only 5% are rejected, a model that predicts every applicant as approved could achieve 95% accuracy while performing poorly in reality.

Precision should be prioritized when:
False positives are expensive. In loan approval prediction, banks want to avoid approving risky applicants who may not repay loans.

Recall should be prioritized when:
Missing positive cases is expensive. In loan approval prediction, banks want to identify all applicants who truly deserve loan approval.

---

Real-World Case Study

A real-world application of classification exists in healthcare through breast cancer prediction systems.

The goal of these systems is to classify tumors as malignant or benign using patient medical information. Data often includes measurements such as cell size, texture, and shape.

Random Forest and Logistic Regression are commonly used classification algorithms because they provide reliable prediction performance.

Research studies have shown that classification systems can achieve high prediction accuracy and support doctors in making earlier diagnoses. Early detection improves treatment outcomes and patient care.

---

References

1. Scikit-learn Documentation
2. IBM Machine Learning Documentation
3. Han, J., Kamber, M., & Pei, J. Data Mining: Concepts and Techniques
4. Breast Cancer Wisconsin Dataset Research Studies