## Introduction to Classification

### What is Classification in Machine Learning?

Classification is a supervised learning task in which the goal is to assign input data to one of several predefined categories or classes. A classification model learns a mapping function from a set of input features (independent variables) to a discrete target variable (dependent variable) during a training phase. Once trained, the model can predict the class label for new, previously unseen data points. The number of possible output classes defines whether the problem is binary (two classes, such as "Approved" or "Rejected") or multiclass (more than two, such as classifying emails into "Spam," "Promotions," or "Primary").

### How is Classification Different from Regression?

Although both classification and regression fall under supervised learning, they differ fundamentally in the nature of their output. Classification predicts a discrete categorical label, whereas regression predicts a continuous numerical value. In classification, the model's output is a class membership; in regression, the output is a quantity on a real-valued scale. This distinction also affects the choice of evaluation metrics: classification uses measures such as accuracy and F1-score, while regression relies on mean squared error or mean absolute error.

### Real-Life Examples

A real-life example of **classification** is an email spam filter, which categorises each incoming email as either "Spam" or "Not Spam." A real-life example of **regression** is predicting the market price of a house based on its size, number of bedrooms, location, and age — the output is a continuous dollar amount rather than a category.

## Classification Algorithms

### Logistic Regression

**How it works:** Despite its name, Logistic Regression is a classification algorithm. It models the probability that a given input belongs to a particular class by applying the logistic (sigmoid) function to a linear combination of the input features. The sigmoid function squashes the output to a value between 0 and 1, which is then interpreted as a probability. A threshold (typically 0.5) is applied to convert the probability into a class label.

**Real-world use case:** Logistic Regression is widely used in medical research to predict the presence or absence of a disease based on patient risk factors such as age, blood pressure, and cholesterol levels.

**Advantages:** It is computationally efficient, easy to implement, and provides interpretable coefficients that indicate the direction and magnitude of each feature's influence. It also outputs well-calibrated probabilities.

**Limitations:** It assumes a linear relationship between the features and the log-odds of the target, which may not hold for complex, non-linear patterns. It also struggles with highly correlated features and may underperform on datasets with intricate feature interactions.

### Decision Trees

**How it works:** A Decision Tree constructs a tree-like model of decisions. At each internal node, the algorithm selects the feature and threshold that best splits the data according to a criterion such as Gini impurity or information gain. This process repeats recursively until a stopping condition is met (e.g., maximum depth or minimum samples per leaf). Each leaf node represents a class label.

**Real-world use case:** Decision Trees are commonly used in customer segmentation to classify customers into high-value, medium-value, and low-value groups based on purchasing behaviour and demographics.

**Advantages:** Decision Trees are highly intuitive and their decisions can be visualised as a flowchart, making them easy for non-technical stakeholders to understand. They require little data preprocessing — they handle both numerical and categorical features and are unaffected by feature scaling.

**Limitations:** Single Decision Trees are prone to overfitting, especially when grown deep without pruning. They are also sensitive to small variations in the training data, which can lead to entirely different tree structures (high variance).

### Random Forest

**How it works:** Random Forest is an ensemble method that constructs a large number of Decision Trees during training. Each tree is built on a bootstrapped sample of the training data, and at each split, only a random subset of features is considered. For classification, the final prediction is determined by majority vote across all trees. This combination of bagging (bootstrap aggregating) and feature randomness reduces the variance that plagues individual Decision Trees.

**Real-world use case:** Random Forest is extensively used in credit scoring to predict whether a loan applicant will default, leveraging diverse features such as income, credit history, and employment status.

**Advantages:** Random Forest typically achieves higher accuracy than a single Decision Tree and is robust against overfitting. It handles high-dimensional data well and provides feature importance rankings, aiding interpretability.

**Limitations:** It is less interpretable than a single Decision Tree because the prediction results from aggregating hundreds of trees. It is also computationally more expensive, both in training time and memory usage, particularly as the number of trees increases.

## Classification Metrics

### Accuracy

Accuracy measures the proportion of all predictions that are correct — that is, the number of true positives plus true negatives divided by the total number of predictions. While intuitive, it can be misleading when classes are imbalanced because a model that always predicts the majority class can still achieve high accuracy.

### Precision

Precision measures the proportion of positive predictions that are actually correct. It is calculated as true positives divided by true positives plus false positives. Precision answers the question: "Of all the cases the model predicted as positive, how many were truly positive?" High precision is important when the cost of a false positive is high.

### Recall

Recall (also called sensitivity or true positive rate) measures the proportion of actual positive cases that the model correctly identified. It is calculated as true positives divided by true positives plus false negatives. Recall answers the question: "Of all the actual positive cases, how many did the model find?" High recall is important when the cost of a false negative is high.

### F1-Score

The F1-Score is the harmonic mean of Precision and Recall, providing a single metric that balances both concerns. It ranges from 0 to 1, with 1 indicating perfect precision and recall. The F1-Score is particularly useful when dealing with imbalanced datasets because it does not inflate when one metric is high and the other is low.

### Confusion Matrix

A Confusion Matrix is a table that summarises the performance of a classification model by displaying the counts of true positives, true negatives, false positives, and false negatives. Each row represents the actual class, and each column represents the predicted class. It provides a comprehensive view of where the model is making correct and incorrect predictions.

### Comparison Table

| Metric           | What It Measures                                      | Sensitive to Class Imbalance |
|------------------|-------------------------------------------------------|------------------------------|
| Accuracy         | Overall proportion of correct predictions             | Yes — can be misleading      |
| Precision        | Correctness among positive predictions                | Partially — focuses on preds |
| Recall           | Completeness of detecting actual positives            | Partially — focuses on actuals |
| F1-Score         | Balance between Precision and Recall                  | No — robust to imbalance     |
| Confusion Matrix | Full breakdown of TP, TN, FP, FN counts              | No — shows raw counts        |

## Class Imbalance

### Why Accuracy Can Be Misleading

When classes are imbalanced (e.g., 95% of loan applications are approved and only 5% are rejected), a model that simply predicts "Approved" for every single application would achieve 95% accuracy despite being completely useless at identifying rejections. Accuracy in such cases masks the model's inability to detect the minority class, which is often the class of greatest interest.

### Precision vs. Recall in Loan Approval

In the loan approval context, a **false positive** means approving a loan that should have been rejected (the applicant is likely to default), while a **false negative** means rejecting a loan that should have been approved (the applicant is creditworthy but denied).

When a bank wants to **minimise financial losses from defaults**, it would prioritise **Precision** — ensuring that among all applicants approved, as few as possible are actually bad borrowers. A high-precision model reduces the cost of bad loans.

When a bank wants to **maximise business opportunity and customer satisfaction**, it would prioritise **Recall** — ensuring that most creditworthy applicants are approved, even if a few risky ones slip through. A high-recall model reduces missed revenue from wrongly rejected good customers.

In practice, the choice depends on the institution's risk appetite and regulatory environment. A conservative bank in a volatile economy would lean toward Precision, while a growth-oriented fintech in a stable market might lean toward Recall.

## Real-World Case Study

### Breast Cancer Classification Using Machine Learning

A well-documented application of classification is the Wisconsin Breast Cancer Diagnostic study, which is widely available through the UCI Machine Learning Repository and scikit-learn's built-in datasets. The goal of the project was to classify breast tissue samples as malignant (cancerous) or benign (non-cancerous) based on 30 numerical features computed from digitised images of fine needle aspirates. These features include radius, texture, perimeter, area, smoothness, and concavity of the cell nuclei.

Researchers and practitioners have applied multiple classifiers to this dataset, including Logistic Regression, Decision Trees, Random Forest, and Support Vector Machines (SVM). In a typical benchmark, Random Forest and SVM consistently achieve accuracy above 96%, with SVM occasionally reaching 98%. The key insight from these studies is that ensemble methods and kernel-based classifiers outperform simpler models on this dataset because the decision boundary between malignant and benign samples is non-linear. Another important finding is that feature selection — reducing the 30 features to the 10 most informative ones — maintains nearly identical accuracy while improving model interpretability, which is critical in medical settings where clinicians need to understand why a particular diagnosis was made.

**Reference:** Street, W.N., Wolberg, W.H., and Mangasarian, O.L. (1993). Nuclear feature extraction for breast tumor diagnosis. *IS&T/SPIE's Symposium on Electronic Imaging: Science and Technology*. Dataset available at: https://scikit-learn.org/stable/datasets/toy_dataset.html#breast-cancer-dataset
```
