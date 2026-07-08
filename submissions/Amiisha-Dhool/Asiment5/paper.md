 Machine Learning Classification: Theory Paper

Course: Data Foundations for Machine Learning
Assignment: Lesson 5 – Classification




Part A – Theory

 1. What is Classification in Machine Learning?

Classification is a supervised machine learning technique used to predict a categorical label or class for new data based on previously labeled examples. During training, the algorithm learns patterns from input features and their corresponding class labels. After learning these patterns, it can classify unseen data into one of the predefined categories.

Classification problems are common in many industries, including healthcare, banking, education, and cybersecurity. For example, a machine learning model can determine whether a loan application should be approved or rejected based on customer information.

 Difference Between Classification and Regression

Although both classification and regression are supervised learning methods, they solve different types of problems.

Classification predicts discrete categories or labels, while regression predicts continuous numerical values.

For example:

* Classification predicts whether a customer will repay a loan (Yes or No).
* Regression predicts the exact amount of money a customer is expected to borrow.

 Real-Life Examples

**Classification Example**

A bank uses customer information such as income, credit score, employment history, and previous loan defaults to predict whether a loan should be approved or rejected.

**Regression Example**

A real estate company predicts the selling price of a house using factors such as location, number of bedrooms, size, and age of the property.



 2. Classification Algorithms

 Logistic Regression

How it Works

Logistic Regression estimates the probability that an observation belongs to a particular class using the logistic (sigmoid) function. The output probability is converted into a class label using a threshold, commonly 0.5.

 Real-World Use Case

Banks use Logistic Regression to predict whether customers are likely to repay loans.

 Advantages

* Simple and easy to interpret.
* Fast to train.
* Performs well on linearly separable data.
* Produces probability estimates.

 Limitations

* Assumes a linear relationship.
* Performs poorly with highly complex datasets.
* Sensitive to multicollinearity.



 Decision Tree

How it Works

A Decision Tree splits the dataset into smaller groups by selecting the best feature at each node. The process continues until a final prediction is reached at a leaf node.

 Real-World Use Case

Hospitals use Decision Trees to help diagnose diseases based on symptoms and medical test results.

 Advantages

* Easy to understand.
* Can handle numerical and categorical data.
* Requires little data preparation.

 Limitations

* Easily overfits training data.
* Small changes in data may produce different trees.
* Less stable than ensemble methods.



 Random Forest

 How it Works

Random Forest combines many Decision Trees. Each tree makes its own prediction, and the final class is determined by majority voting.

 Real-World Use Case

Financial institutions use Random Forest to detect fraudulent transactions and assess credit risk.

 Advantages

* High prediction accuracy.
* Reduces overfitting.
* Handles large datasets well.
* Works with both numerical and categorical features.

Limitations

* Slower than a single Decision Tree.
* Harder to interpret.
* Requires more computational resources.



 3. Classification Metrics

 Accuracy

Accuracy measures the percentage of predictions that are correct.

**Formula**

Accuracy = (Correct Predictions) / (Total Predictions)

Accuracy is useful when the dataset is balanced.



 Precision

Precision measures how many predicted positive cases are actually positive.

High precision means there are few false positives.

This metric is important when false approvals are costly.



 Recall

Recall measures how many actual positive cases are correctly identified.

High recall means there are few false negatives.

Recall is important when missing a positive case is expensive.



 F1-Score

The F1-Score combines Precision and Recall into a single metric using their harmonic mean.

It is especially useful when classes are imbalanced.



 Confusion Matrix

A Confusion Matrix summarizes model predictions using four values:

* True Positive (TP)
* True Negative (TN)
* False Positive (FP)
* False Negative (FN)

It provides a detailed view of model performance beyond overall accuracy.



 Comparison of Classification Metrics

| Metric           | What It Measures                     | Sensitive to Class Imbalance         |
| ---------------- | ------------------------------------ | ------------------------------------ |
| Accuracy         | Overall correctness                  | Yes                                  |
| Precision        | Correctness of positive predictions  | No (more robust than Accuracy)       |
| Recall           | Ability to identify positive cases   | No (more robust than Accuracy)       |
| F1-Score         | Balance between Precision and Recall | No (recommended for imbalanced data) |
| Confusion Matrix | Complete prediction outcomes         | No (shows all prediction types)      |



4. Class Imbalance

 Why Accuracy Can Be Misleading

Accuracy can be misleading when one class is much larger than the other.

For example, suppose a loan dataset contains:

* 95% Approved
* 5% Rejected

If a model predicts every application as Approved, it achieves 95% accuracy but completely fails to identify rejected applications.

Therefore, Precision, Recall, and F1-Score provide a more reliable evaluation for imbalanced datasets.



 Precision vs Recall in Loan Approval

 When Precision Should Be Prioritized

A bank should prioritize Precision when approving loans because approving risky applicants may result in financial losses.

High Precision means that most approved applicants are actually reliable borrowers.

 When Recall Should Be Prioritized

Recall should be prioritized when the bank wants to identify as many qualified applicants as possible.

High Recall reduces the number of eligible customers who are incorrectly rejected.



 5. Real-World Case Study

 Loan Approval Prediction Using Machine Learning

 Goal

The objective of the project was to predict whether loan applications should be approved based on customer financial information.

 Data Used

The dataset included features such as:

* Applicant income
* Credit score
* Employment years
* Loan amount
* Previous loan defaults
* Collateral information

 Classifier Used

Random Forest Classifier was applied because it provides strong predictive performance and reduces overfitting compared with a single Decision Tree.

 Results

The Random Forest model achieved higher prediction accuracy than Logistic Regression and Decision Tree models. It also produced better Precision and Recall, making it suitable for real-world loan approval systems.

The study concluded that ensemble learning methods can significantly improve decision-making in financial institutions.



References

Géron, A. (2023). *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* (3rd ed.). O'Reilly Media.

Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.

Pedregosa, F., Varoquaux, G., Gramfort, A., et al. (2011). Scikit-learn: Machine Learning in Python. *Journal of Machine Learning Research*, 12, 2825–2830.


