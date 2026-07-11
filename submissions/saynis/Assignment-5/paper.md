# Part A — Classification Theory

## Introduction to Classification

Classification is a supervised machine learning task where the model learns from labeled examples and predicts a category for new data. In a loan approval problem, the model studies previous loan applications and learns patterns from features such as income, credit score, loan amount, collateral, employment years, and previous defaults. The target is usually a category such as `Approved` or `Rejected`.

Classification is different from regression because regression predicts a continuous number, while classification predicts a class label. For example, predicting the price of a house is a regression task because the output is a number such as 350,000 dollars. Predicting whether a loan should be approved or rejected is a classification task because the output is a category.

A real-life classification example is email spam detection, where the model predicts whether an email is `Spam` or `Not Spam`. A real-life regression example is predicting the monthly rent of an apartment based on its location, size, and number of rooms.

## Classification Algorithms

### Logistic Regression

Logistic Regression is a simple and widely used classification algorithm. Even though the name contains the word “regression,” it is commonly used for classification. It estimates the probability that an observation belongs to a class. For example, in loan approval, it may estimate that an applicant has an 82% chance of being approved. If the probability is above a chosen threshold, such as 0.5, the model predicts `Approved`; otherwise, it predicts `Rejected`.

A useful real-world case for Logistic Regression is predicting whether a customer will leave a service. Its main advantage is that it is simple, fast, and easy to interpret. It can show how features such as income or credit score influence the probability of approval. Its limitation is that it may not perform well when the relationship between features is complex or highly non-linear.

### Decision Tree

A Decision Tree makes predictions by asking a sequence of feature-based questions. In a loan approval problem, it may ask questions such as: Is the credit score greater than 650? Is the income high enough? Does the applicant have previous defaults? Each answer moves the data through a branch until the model reaches a final decision.

A real-world use case for Decision Trees is medical screening, where the model may use symptoms and test results to classify a patient as high risk or low risk. The main advantage of a Decision Tree is that it is easy to understand and explain. Its limitation is that a single tree can overfit the training data, meaning it may memorize the training examples instead of learning general rules.

### Random Forest

Random Forest is an ensemble algorithm made of many Decision Trees. Instead of trusting one tree, it trains many trees on different random parts of the data and features. For classification, each tree gives a vote, and the class with the majority vote becomes the final prediction. For example, if 72 trees predict `Approved` and 28 trees predict `Rejected`, the final prediction is `Approved`.

A real-world use case for Random Forest is fraud detection, where the model predicts whether a transaction is legitimate or fraudulent. Its main advantage is that it is usually more stable and accurate than a single Decision Tree. It can handle complex patterns and reduce overfitting. Its limitation is that it is less interpretable because many trees are involved in the final decision.

## Classification Metrics

Classification models should not be evaluated using Accuracy alone, especially when the dataset is imbalanced. A confusion matrix gives the full picture by showing four values: True Positive, False Positive, False Negative, and True Negative.

In this loan approval project, the positive class is `Approved = 1`. A True Positive means the applicant was actually approved and the model predicted approved. A False Positive means the applicant was actually rejected but the model predicted approved. A False Negative means the applicant was actually approved but the model predicted rejected. A True Negative means the applicant was actually rejected and the model predicted rejected.

| Metric | What it measures | Sensitive to imbalance? |
|---|---|---|
| Accuracy | The percentage of all predictions that are correct | Yes |
| Precision | Of the applications predicted as approved, how many were actually approved | Less sensitive than Accuracy |
| Recall | Of the actually approved applications, how many the model correctly found | Less sensitive than Accuracy |
| F1-Score | A balanced score between Precision and Recall | Useful for imbalanced data |
| Confusion Matrix | The full count of TP, FP, FN, and TN | Shows the full picture |

Accuracy measures overall correctness. Precision focuses on the quality of positive predictions. Recall focuses on how many real positive cases the model found. F1-Score is useful when both Precision and Recall matter because it combines them into one balanced score.

## Class Imbalance

Class imbalance happens when one class is much more common than another. For example, if 95% of loan applications are approved and only 5% are rejected, a model could predict `Approved` for every applicant and still get 95% Accuracy. However, this model would be weak because it would fail to identify rejected or risky applications.

In loan approval, Precision should be prioritized when false positives are costly. A false positive means the model approved someone who should have been rejected. This can be dangerous for a bank because the applicant may fail to repay the loan.

Recall should be prioritized when false negatives are costly. A false negative means the model rejected someone who should have been approved. This can hurt the business because the bank may lose a good customer. Therefore, the best metric depends on the business goal. If avoiding risky approvals is the main goal, Precision is more important. If finding as many good applicants as possible is the main goal, Recall is more important.

## Real-World Case Study: Breast Cancer Classification

A real-world example of classification is breast cancer diagnosis using the Wisconsin Diagnostic Breast Cancer dataset. The goal of this type of project is to classify tumors as malignant or benign using measurements computed from images of fine needle aspirate samples. The dataset contains 569 samples and 30 numeric features.

Researchers have applied classification algorithms such as Support Vector Machine, Neural Networks, Logistic Regression, and other models to this dataset. One study by Agarap compared several machine learning algorithms on the Wisconsin Diagnostic Breast Cancer dataset and reported that the tested models achieved strong classification performance, with all models exceeding 90% test accuracy and a Multilayer Perceptron reaching about 99.04% test accuracy.

This case study shows how classification can support decision-making in healthcare. However, it also shows why metrics beyond Accuracy matter. In medical screening, missing a real disease case can be very costly, so Recall is especially important. The same idea applies to other fields such as finance and education, where the cost of different mistakes must be carefully considered.

## Conclusion

Classification is useful when the goal is to predict a category, such as approved or rejected, pass or fail, fraud or not fraud, and risk or not risk. Logistic Regression is simple and interpretable, Decision Trees are easy to explain, and Random Forests are stronger and more stable because they combine many trees. Evaluation should include Accuracy, Precision, Recall, F1-Score, and the Confusion Matrix because each metric explains a different part of model performance.

## References

- Scikit-learn. (n.d.). LogisticRegression documentation. https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
- Scikit-learn. (n.d.). DecisionTreeClassifier documentation. https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
- Scikit-learn. (n.d.). RandomForestClassifier documentation. https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
- UCI Machine Learning Repository. (n.d.). Breast Cancer Wisconsin Diagnostic dataset. https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
- Agarap, A. F. (2017). On Breast Cancer Detection: An Application of Machine Learning Algorithms on the Wisconsin Diagnostic Dataset. arXiv. https://arxiv.org/abs/1711.07831
