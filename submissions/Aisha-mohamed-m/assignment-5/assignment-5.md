1. What is Classification in Machine Learning?

Classification is a supervised learning technique that predicts the category or class of new observations.

Examples

Spam or Not Spam
Loan Approved or Rejected
Disease or No Disease

2. Classification vs Regression
Classification	Regression
Predicts categories	Predicts continuous values
Example: Approved/Rejected	Example: House Price
Metrics: Accuracy, Precision, Recall	Metrics: MAE, RMSE

3. Classification Algorithms
Logistic Regression

Basic Idea

Uses the sigmoid function to estimate the probability of belonging to a class.

 Use Case: Loan Approval

 Advantages

Simple
Fast
Easy to interpret

 Limitations

Cannot model complex relationships
Decision Tree

Basic Idea

Makes predictions using a series of decision rules.

Income > $50,000

       Yes
      /    \
Credit Good?
   /      \
Approve  Reject

 Use Case

Medical Diagnosis

Advantages

Easy to understand
Visual model

Limitations

Can overfit


Random Forest

Basic Idea

Combines multiple Decision Trees to improve prediction accuracy.

✔ Use Case

Fraud Detection

✔ Advantages

High accuracy
Less overfitting

✔ Limitations

Harder to interpret


4. Classification Metrics
Metric	    Measures
Accuracy	Overall correctness
Precision	Correct positive predictions
Recall   	Finds actual positives
F1-score	Balance between Precision and Recall
Confusion Matrix	Prediction summary

5. Class Imbalance

Example:

Approved = 950

Rejected = 50

A model predicting every applicant as Approved achieves 95% Accuracy, but fails to detect rejected applicants.

Therefore, Accuracy alone can be misleading.

6. Real-World Case Study
Loan Approval Prediction Using Random Forest

Goal

Predict whether applicants should receive a loan.

Dataset

Income
Credit History
Employment
Loan Amount

Classifier

Random Forest

Results

Higher accuracy than Decision Tree
Credit history was the most important feature
Faster and more reliable loan decisions

Conclusion

Classification helps computers predict categories rather than numbers. It is widely used in finance, healthcare, education, and business. Algorithms such as Logistic Regression, Decision Trees, and Random Forest each have unique strengths, while metrics like Precision, Recall, and F1-score provide a better evaluation than Accuracy alone for imbalanced datasets.