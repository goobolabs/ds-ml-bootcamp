Assignment Five: Classification — Theory and Practice

Part A — Theory

1. Introduction to Classification

What is Classification in Machine Learning?

Classification is a supervised machine learning technique used to predict or assign data into predefined categories or classes. A classification model learns patterns from labeled training data and uses those patterns to classify new, unseen observations into one of the known classes.

Classification is widely used in many real-world applications such as loan approval, medical diagnosis, spam email detection, fraud detection, customer churn prediction, and image recognition.

Difference Between Classification and Regression

Although both classification and regression are supervised learning methods, they solve different types of prediction problems.

Classification predicts categorical outcomes, while regression predicts continuous numerical values. For example, a classification model may predict whether a loan application will be approved or rejected, whereas a regression model predicts the selling price of a car.

Classification models are commonly evaluated using Accuracy, Precision, Recall, F1-Score, and Confusion Matrix. Regression models are evaluated using MAE, MSE, RMSE, and R².

Real-Life Examples

Classification Example: Predicting whether a customer will qualify for a bank loan (Approved or Rejected).

Regression Example: Predicting the market price of a used vehicle based on its features.

---

2. Classification Algorithms

Logistic Regression

How It Works

Logistic Regression is a supervised learning algorithm used for binary classification problems. Instead of predicting continuous values, it estimates the probability that an observation belongs to a particular class using the logistic (sigmoid) function. The probability is then converted into a class label, typically using a threshold of 0.5.

Real-World Use Case

Banks use Logistic Regression to predict whether a customer is likely to repay a loan or default.

Advantages

- Simple and easy to interpret.
- Fast to train and predict.
- Works well for binary classification.
- Produces probability estimates.

Limitations

- Assumes a linear relationship between features and the log-odds.
- Cannot easily model highly complex relationships.
- Sensitive to multicollinearity.

---

Decision Tree

How It Works

A Decision Tree divides the dataset into smaller subsets using a sequence of decision rules. Each internal node represents a condition based on one feature, while each leaf node represents the predicted class.

Real-World Use Case

Hospitals use Decision Trees to assist doctors in diagnosing diseases based on patient symptoms and medical test results.

Advantages

- Easy to understand and visualize.
- Handles both numerical and categorical data.
- Requires little data preparation.
- Can model nonlinear relationships.

Limitations

- Can easily overfit the training data.
- Sensitive to small changes in the dataset.
- Individual trees may have lower predictive accuracy than ensemble methods.

---

Random Forest

How It Works

Random Forest is an ensemble learning algorithm that combines many Decision Trees. Each tree is trained using a random sample of the training data and a random subset of features. For classification, each tree votes for a class, and the majority vote becomes the final prediction.

Real-World Use Case

Financial institutions use Random Forest to detect fraudulent transactions and evaluate loan applications.

Advantages

- High prediction accuracy.
- Reduces overfitting compared to a single Decision Tree.
- Handles large datasets effectively.
- Works well with nonlinear relationships.

Limitations

- More computationally expensive than Logistic Regression.
- Less interpretable than a single Decision Tree.
- Training may take longer on very large datasets.

---

3. Classification Metrics

Accuracy

Accuracy measures the proportion of correctly classified observations among all predictions. It provides an overall measure of model performance but may be misleading when the classes are imbalanced.

---

Precision

Precision measures how many of the instances predicted as positive are actually positive. High precision indicates a low number of false positive predictions.

---

Recall

Recall measures how many of the actual positive cases are correctly identified by the model. High recall means fewer false negatives.

---

F1-Score

The F1-Score is the harmonic mean of Precision and Recall. It provides a balanced measure when both false positives and false negatives are important.

---

Confusion Matrix

A Confusion Matrix summarizes classification performance by showing the numbers of True Positives (TP), True Negatives (TN), False Positives (FP), and False Negatives (FN). It helps identify the types of prediction errors made by the model.

---

Comparison of Classification Metrics

Metric| What It Measures| Sensitive to Class Imbalance
Accuracy| Overall percentage of correct predictions| Yes
Precision| Correctness of positive predictions| Less sensitive
Recall| Ability to identify actual positive cases| Less sensitive
F1-Score| Balance between Precision and Recall| Good for imbalanced datasets
Confusion Matrix| Counts of TP, TN, FP, and FN| Shows detailed error distribution

---

4. Class Imbalance

Class imbalance occurs when one class contains significantly more observations than another. In such situations, Accuracy can be misleading because a model may achieve high accuracy simply by predicting the majority class.

For example, suppose 95% of loan applications are approved and only 5% are rejected. A model that predicts every application as approved would achieve 95% accuracy while completely failing to identify rejected applicants.

In loan approval prediction, Precision is more important when the bank wants to minimize approving risky applicants. High precision means that most approved loans are likely to be safe.

On the other hand, Recall becomes more important when the bank wants to ensure that most eligible applicants are correctly approved. High recall reduces the number of qualified applicants who are mistakenly rejected.

The choice between Precision and Recall depends on the business objective and the cost of different prediction errors.

---

5. Real-World Case Study

Loan Approval Prediction Using Random Forest

Many banks use machine learning to automate the loan approval process. Historical loan application data containing applicant income, employment history, credit score, collateral information, and previous loan defaults are used to train classification models.

Random Forest has become a popular algorithm for this task because it can model complex relationships between applicant characteristics while reducing overfitting. Each decision tree independently predicts whether a loan should be approved, and the final decision is based on the majority vote of all trees.

Studies have shown that Random Forest often achieves higher predictive accuracy than simpler models such as Logistic Regression because it captures nonlinear relationships and interactions among variables. As a result, financial institutions can make faster, more consistent, and more accurate lending decisions while reducing financial risk.

---

References

Géron, A. (2023). Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow (3rd ed.). O'Reilly Media.

James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). An Introduction to Statistical Learning (2nd ed.). Springer.

Pedregosa, F., Varoquaux, G., Gramfort, A., et al. (2011). Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, 12, 2825–2830.

Scikit-learn Developers. (2025). Scikit-learn User Guide. https://scikit-learn.org/stable/user_guide.html