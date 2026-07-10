# Reflection Paper: Loan Approval Classification Using Machine Learning

## Introduction

In this project, I implemented a machine learning pipeline to predict whether a loan application would be approved or rejected. I used Python together with the **pandas** and **scikit-learn** libraries to load a cleaned loan dataset, split the data into training and testing sets, train classification models, and evaluate their performance using several classification metrics. The project helped me understand how different classification algorithms perform on the same dataset and how evaluation metrics are used to compare their effectiveness.

---

# What I Implemented

I reproduced the preprocessing pipeline by loading the cleaned loan dataset (`clean_loan_dataset.csv`) into a pandas DataFrame. The target variable was **Approved**, while the remaining columns were used as input features. I then divided the dataset into training and testing sets using an 80/20 split with stratified sampling to preserve the proportion of approved and rejected loans.

Next, I trained two classification algorithms:

- **Logistic Regression**
- **Random Forest**

In addition, I selected **Decision Tree** as my third classification algorithm because it is easy to understand and commonly used for classification problems. After training the models, I evaluated them using Accuracy, Precision, Recall, F1-Score, and the Confusion Matrix. Finally, I performed a sanity check by testing one loan application and comparing the predictions produced by each classifier.

---

# Comparison of Models

During the sanity check, each model predicted whether the selected loan application should be approved or rejected. In many cases, Logistic Regression and Random Forest produced the same prediction, while the Decision Tree occasionally produced a different result because it relies on a single tree rather than multiple trees or probability estimates.

Among the three models, **Random Forest produced the most realistic predictions**. Since it combines the predictions of many decision trees through majority voting, it reduces the risk of overfitting and generally provides better generalization to unseen data. Logistic Regression performed well when relationships between variables were relatively simple, while the Decision Tree was easier to interpret but more likely to overfit the training data.

---

# Understanding Random Forest

Random Forest is an **ensemble learning algorithm** used for both classification and regression tasks. Instead of building only one decision tree, it creates many decision trees using random samples of the training data and random subsets of features.

For classification, every decision tree predicts a class label independently. The final prediction is determined by **majority voting**, meaning the class that receives the highest number of votes becomes the final prediction.

This approach improves prediction accuracy because errors made by individual trees are often corrected by the other trees. As a result, Random Forest is generally more robust and less prone to overfitting than a single Decision Tree.

---

# Additional Algorithm

The additional algorithm I selected was **Decision Tree**.

A Decision Tree classifies data by repeatedly splitting it into smaller groups based on the feature that best separates the classes. Each internal node represents a decision, and each leaf node represents the final classification.

One major advantage of Decision Trees is that they are **easy to interpret and visualize**, making them useful for explaining predictions to non-technical users.

One limitation is that Decision Trees can **overfit the training data**, especially when the tree becomes very deep.

Compared with Logistic Regression and Random Forest, the Decision Tree generally achieved lower evaluation metrics because it relied on a single model instead of combining multiple learners. However, it remained valuable because of its simplicity and interpretability.

---

# Metrics Discussion

The evaluation metrics provided different insights into model performance.

- **Accuracy** measured the overall percentage of correctly classified loan applications.
- **Precision** measured how many approved loans predicted by the model were actually approved.
- **Recall** measured how many truly approved loans were successfully identified.
- **F1-Score** balanced Precision and Recall into a single metric.

Among the three models, **Random Forest achieved the highest Accuracy, Precision, Recall, and F1-Score**. This indicates that it correctly classified more loan applications while making fewer false predictions.

Logistic Regression produced competitive results and was computationally efficient, but it assumed a linear relationship between the features and the target variable.

The Decision Tree was easy to understand and explain but was generally less stable and more likely to overfit, resulting in slightly lower performance.

---

# My Findings

Based on the experimental results, I would choose **Random Forest** for loan approval prediction. It consistently achieved the strongest overall performance across Accuracy, Precision, Recall, and F1-Score while producing realistic predictions during the sanity check. Its ensemble learning approach reduces overfitting and improves the model's ability to generalize to new loan applications.

Although Logistic Regression is simpler and easier to interpret, and the Decision Tree provides clear decision rules, Random Forest offers the best balance between predictive accuracy and reliability. For real-world banking systems where correct loan approval decisions are critical, Random Forest would be the preferred model because it minimizes prediction errors while maintaining strong overall performance.

