# Part A — Theory: Understanding Classification in Machine Learning

## 1. Introduction to Classification

### 1.1 What is Classification in Machine Learning?

Classification is a type of supervised learning in which a model learns to assign a data point to one of a set of predefined categories, called classes or labels. The model is trained on data where the correct answer (the label) is already known, and it learns the patterns that connect the input features to that label. Once trained, the model can predict the class of new, unseen data.

For example, a classification model can look at a loan applicant's income, credit history, and loan amount, and decide whether the application should be **Approved** or **Rejected**. The output is always one of a limited number of categories, not a number on a continuous scale.

### 1.2 How is Classification Different from Regression?

Both classification and regression are supervised learning tasks, but they differ in the type of output they produce:

- **Classification** predicts a discrete category or class (e.g., "spam" or "not spam", "approved" or "rejected").
- **Regression** predicts a continuous numeric value (e.g., a price, a temperature, or a probability of rainfall in millimeters).

In simple terms, classification answers the question "which group does this belong to?", while regression answers "how much?" or "how many?".

### 1.3 Real-Life Examples

- **Classification example:** Email spam detection. A model reads the content of an email and classifies it as "spam" or "not spam" based on words, sender information, and formatting patterns.
- **Regression example:** House price prediction. A model uses features such as square footage, number of bedrooms, and location to predict the actual sale price of a house, which is a continuous number.

---

## 2. Classification Algorithms

### 2.1 Logistic Regression

**How it works:** Despite its name, logistic regression is used for classification, not regression. It calculates a weighted sum of the input features and passes this sum through a sigmoid (S-shaped) function, which converts the result into a probability between 0 and 1. If the probability is above a chosen threshold (commonly 0.5), the model predicts one class; otherwise, it predicts the other.

**Real-world use case:** Predicting whether a bank customer will default on a credit card payment, based on features like income, existing debt, and payment history.

**Advantages:** Simple to understand and implement, fast to train, and produces easily interpretable results (the model shows how much each feature increases or decreases the probability of a class). It also works well when the relationship between features and the outcome is roughly linear.

**Limitations:** It struggles with complex, non-linear relationships between features and the target, and its performance can suffer when features are highly correlated with each other (multicollinearity).

### 2.2 Decision Trees

**How it works:** A decision tree splits the data step by step, asking a series of yes/no questions about the features (for example, "Is income greater than $50,000?"). Each split creates a branch, and the process continues until the data in each final branch (leaf) is mostly of one class. The tree structure resembles an upside-down tree, with the root at the top and the final decisions (leaves) at the bottom.

**Real-world use case:** Medical diagnosis systems that decide whether a patient is at risk of a disease based on a sequence of symptoms and test results.

**Advantages:** Easy to visualize and explain to non-technical audiences, requires little data preparation (no need to scale features), and can capture non-linear relationships.

**Limitations:** Prone to overfitting, meaning it can memorize the training data too closely and perform poorly on new data. Small changes in the data can also lead to a very different tree structure, making single trees somewhat unstable.

### 2.3 Random Forest

**How it works:** A random forest is an ensemble method, meaning it combines many decision trees to make a more reliable prediction. Each tree is trained on a random subset of the data and a random subset of features. When making a prediction, every tree "votes" for a class, and the forest picks the class with the most votes. This process, called bagging, reduces the risk of overfitting that a single decision tree has.

**Real-world use case:** Fraud detection in banking, where the model examines many transaction features simultaneously to flag suspicious activity.

**Advantages:** More accurate and stable than a single decision tree, resistant to overfitting, and able to handle large datasets with many features. It also provides a measure of feature importance, showing which variables matter most for the prediction.

**Limitations:** Slower to train and less interpretable than a single decision tree or logistic regression, since it relies on combining many trees ("black box" behavior). It also requires more memory and computing power.

### 2.4 Comparison Summary

| Model | Basic Idea | Interpretability | Handles Non-Linearity | Overfitting Risk |
|---|---|---|---|---|
| Logistic Regression | Weighted sum + probability via sigmoid | High | Low | Low |
| Decision Tree | Sequential feature-based splits | High | High | High |
| Random Forest | Ensemble of many decision trees (voting) | Medium | High | Low (compared to single tree) |

---

## 3. Classification Metrics

When evaluating a classification model, accuracy alone is often not enough. The following metrics give a fuller picture of performance.

- **Accuracy:** The proportion of total predictions that were correct. It answers "out of all predictions, how many were right?"
- **Precision:** Of all the cases the model predicted as positive (e.g., "approved"), how many were actually positive. Precision answers "when the model says yes, how often is it correct?"
- **Recall (Sensitivity):** Of all the actual positive cases, how many did the model correctly identify. Recall answers "out of all the true positives, how many did the model catch?"
- **F1-Score:** The harmonic mean of precision and recall, combining both into a single number. It is useful when we want a balance between precision and recall, especially with imbalanced classes.
- **Confusion Matrix:** A table that shows the counts of true positives, true negatives, false positives, and false negatives. It gives a complete breakdown of correct and incorrect predictions for each class, and is the basis from which accuracy, precision, recall, and F1-score are calculated.

### 3.1 Comparison Table

| Metric | What It Measures | Sensitivity to Class Imbalance |
|---|---|---|
| Accuracy | Overall proportion of correct predictions | High — can be misleading with imbalanced data |
| Precision | Correctness of positive predictions | Moderate — affected by number of false positives |
| Recall | Ability to find all actual positives | Moderate — affected by number of false negatives |
| F1-Score | Balance between precision and recall | Low — more robust than accuracy alone |
| Confusion Matrix | Full breakdown of prediction outcomes | Not a single score, but reveals imbalance directly |

---

## 4. Class Imbalance

### 4.1 Why Can Accuracy Be Misleading?

Class imbalance happens when one class is much more common than another. For example, if 95% of loan applications in a dataset are approved and only 5% are rejected, a model that simply predicts "approved" for every applicant would achieve 95% accuracy — despite being completely useless at identifying the rejected cases. This shows that accuracy alone does not reveal how well a model performs on the minority class, which is often the class of greatest interest.

### 4.2 Precision vs. Recall: Loan Approval Example

The choice between prioritizing precision or recall depends on the cost of different types of mistakes.

- **Prioritize Precision when false positives are costly.** In loan approval, a false positive means approving a loan for someone who will not repay it. If the bank wants to minimize the risk of bad loans (defaults), it should prioritize precision, accepting that it may reject some good applicants (false negatives) in order to be more cautious.
- **Prioritize Recall when false negatives are costly.** If the bank's priority is to make sure that as many creditworthy applicants as possible are approved (to grow its loan business and avoid losing good customers), it should prioritize recall for identifying the "approved" class, even if this means occasionally approving some risky applicants.

In practice, banks often try to balance both using the F1-score, or by adjusting the decision threshold based on business priorities.

---

## 5. Real-World Case Study

**Topic:** Comparative machine learning models for loan approval and credit risk prediction.

A comparative study on credit risk analysis in loan approval used survey data from 1,991 individuals, combining a loan approval dataset with additional mental health-related information as input features. <cite index="1-1">The study noted that loan requests represent a multi-billion-dollar business worldwide, and in 2022 over 20 million Americans had open loans totaling 178 billion US dollars in debt, although over 20% of loan applications were rejected.</cite>

**Goal:** To evaluate whether machine learning techniques could better predict loan and credit risk outcomes than traditional statistical methods, and to compare the performance of multiple classification algorithms on the same task.

**Data used:** A combined dataset drawing on loan application records and survey-based personal information, used as input features for predicting loan approval or risk outcomes.

**Classifiers applied:** <cite index="1-1">The study compared several algorithms, including Gaussian Naive Bayes, Random Forest Classifier, Decision Tree Classifier, AdaBoost Classifier, Gradient Boosting Classifier, and XGBoost Classifier.</cite> <cite index="1-1">The researchers accounted for practical challenges such as imbalanced datasets, using stratified sampling and a fixed random seed to ensure reproducible results.</cite>

**Key results and insights:** <cite index="1-1">Performance was evaluated using accuracy, F1-score, precision, recall, and the confusion matrix, giving a detailed view of each algorithm's effectiveness rather than relying on a single metric.</cite> This mirrors a broader pattern seen across similar financial studies: in a separate comparison of loan default prediction models, <cite index="5-1">Gradient Boosting achieved the highest overall performance among the models tested, with an accuracy of about 0.89, an F1-score of about 0.81, and a recall of about 0.80, making it the most effective model in that particular study for identifying defaults.</cite> Similarly, in a related comparison of loan default prediction techniques, <cite index="2-1">Random Forest was found to outperform logistic regression and decision tree models in both accuracy and area under the curve.</cite>

**Insight for this project:** These findings support the choice of Random Forest as a strong ensemble baseline and confirm that no single algorithm is universally best — model performance depends on the dataset, the degree of class imbalance, and the chosen evaluation metrics. This reinforces the importance of comparing multiple classifiers (as done in this assignment with Logistic Regression, Random Forest, and a third chosen algorithm) rather than relying on just one model.

---

## References

- Comparative study on credit risk analysis integrating mental health data with loan approval prediction models. Available at: https://www.mdpi.com/2504-4990/6/1/4
- Bank Loan Prediction Using Machine Learning Techniques. Available at: https://arxiv.org/pdf/2410.08886
- Data-Driven Loan Default Prediction: A Machine Learning Approach for Enhancing Business Process Management. Available at: https://www.mdpi.com/2079-8954/13/7/581
- Credit Risk Prediction Using Machine Learning and Deep Learning: A Study on Credit Card Customers. Available at: https://www.mdpi.com/2227-9091/12/11/174
