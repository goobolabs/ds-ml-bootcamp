# Reflection Paper: Loan Approval Classification

## What I Implemented

In this assignment, I reproduced the Lesson 5 preprocessing pipeline for the loan approval dataset. The preprocessing steps included handling missing values, encoding categorical variables, scaling numerical features where appropriate, and splitting the dataset into training and testing sets.

After preprocessing, I trained three machine learning classification models to predict whether a loan application should be approved or rejected. The models were **Logistic Regression**, **Random Forest**, and **Decision Tree**. Finally, I evaluated their performance using Accuracy, Precision, Recall, and F1-Score.

## Comparison of Models

During the sanity check, all three models produced similar predictions for many loan applications, but there were some differences. Logistic Regression made predictions based on linear relationships between the features and the target variable. Decision Tree captured more complex decision rules but occasionally produced inconsistent predictions because it can overfit the training data. Random Forest generated more stable predictions because it combined the results of many decision trees.

Among the three models, Random Forest produced the most realistic and reliable predictions. Its ensemble approach reduced overfitting and improved generalization, making it better suited for loan approval prediction.

## Understanding Random Forest

Random Forest is an ensemble machine learning algorithm that combines multiple decision trees to perform classification. Each tree is trained on a different random sample of the data and considers a random subset of features when making splits. For a classification problem, each tree votes for a class, and the class receiving the majority of votes becomes the final prediction.

This approach improves prediction accuracy and reduces the risk of overfitting compared to using a single decision tree.

## Other Algorithm: Decision Tree

The additional algorithm I selected was Decision Tree because it is simple to understand and provides clear decision rules that can easily be interpreted.

A Decision Tree works by repeatedly splitting the data into smaller groups based on the feature that best separates the classes. The process continues until a final prediction is reached.

One advantage of Decision Tree is that it is easy to interpret and visualize. One limitation is that it can overfit the training data, resulting in lower performance on unseen data.

Compared with Logistic Regression and Random Forest, the Decision Tree achieved reasonable performance but generally produced lower Accuracy and F1-Score than Random Forest.

## Metrics Discussion

Among the three models, Random Forest achieved the highest Accuracy, Precision, Recall, and F1-Score. Logistic Regression performed well and produced consistent results but was limited by its assumption of linear relationships. Decision Tree performed adequately but was more prone to overfitting, leading to lower overall performance.

These results suggest that Random Forest provides the best balance between correctly identifying approved loans while minimizing incorrect predictions.

## My Findings

Based on the results, I would choose Random Forest for loan approval prediction. It consistently achieved the strongest performance across all evaluation metrics and produced more stable predictions than the other models. Its ability to combine multiple decision trees helps reduce overfitting while improving classification accuracy.

Although Logistic Regression is faster and easier to interpret, and Decision Tree provides clear decision rules, Random Forest offers the best overall balance between accuracy, reliability, and robustness. For real-world banking and financial applications, where prediction quality is very important, Random Forest would be my preferred model.
