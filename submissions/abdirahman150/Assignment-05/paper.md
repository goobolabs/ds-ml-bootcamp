
# Part A — Theory

## Introduction to ClassificationWhat 
Classification in Machine Learning: Classification is a supervised learning task where the model learns to predict a categorical class label for a given input. The goal is to map input variables (X) to discrete output variables (y), assigning data points into predefined categories.

1. How is it Different from Regression?
- Classification Predicts a discrete category (e.g., predicting if an email is Spam or Safe).
- Regression Predicts a continuous numerical value (e.g., predicting the exact price of a house).

## Classification Algorithms
1. Logistic Regression
- Basic Idea: A simple linear model that calculates the probability (0 to 1) of an item belonging to a specific class.
- Use Case: Predicting if a customer will cancel a subscription.
- Advantages: Simple to implement, computationally efficient, and highly interpretable (outputs clear probabilities).
- Limitations: Assumes a linear relationship between features and target; performs poorly on highly complex, non-linear data.

2. Decision Trees
- Basic Idea: Breaks down data by asking a series of if-else questions, creating a tree-like structure of rules.
- Use Case: Diagnosing a disease based on medical symptoms.
- Advantages: Easy to understand and visualize; requires very little data preprocessing (no feature scaling needed).
- Limitations: Highly prone to overfitting, meaning it captures noise in the training data and generalizes poorly to new data.

3. Random Forest
- Basic Idea: An ensemble learning method that builds a "forest" of multiple independent Decision Trees and combines their predictions (usually by majority vote) to produce a more robust model.

- Real-World Use Case: Credit card fraud detection.

- Advantages: Reduces the risk of overfitting, handles large datasets with high dimensionality effectively, and is highly accurate.

- Limitations: Slow to train and predict compared to simpler models; acts as a "black box" making it harder to interpret.


## Classification Metrics
- Accuracy: Overall percentage of correct predictions.

- Precision: Out of all examples the model predicted as positive, how many were actually positive? (Minimizes False Positives).

- Recall: Out of all actual positive examples, how many did the model manage to find? (Minimizes False Negatives).

- F1-Score: The perfect balance/average between Precision and Recall.

- Confusion Matrix: A table that displays the exact counts of True Positives, True Negatives, False Positives, and False Negatives.

|Metric|Measures|Balanced Data|
|------|--------|-------------|
|Accuracy|Correctness|No|
|Precision|Positive Guesses|Yes|
|Recall|find all positive cases|Yes|
|F1-Score|Balanced B/W Precision and Recall|Yes|

## Class Imbalance
If 99% of your dataset consists of legitimate transactions and only 1% is fraud, a dumb model that guesses "No Fraud" every single time will achieve 99% accuracy, despite completely failing to find any actual fraud.

1. Precision vs. Recall (Loan Approval)
- Prioritize Precision: When a False Positive costs too much. In loans, a False Positive means approving a risky customer who defaults on their debt. To avoid losing money, the bank needs to be absolutely precise about who it approves.

- Prioritize Recall: When a False Negative costs too much. If a bank is running a marketing campaign to give special loans to VIP clients, a False Negative means missing out on an excellent customer. Here, the bank wants a high Recall to catch every potential VIP client.

## Case Study: Credit Risk Assessment
- Project Title: Automated Loan Underwriting and Credit Risk Prediction Using Random Forest and SMOTE.

- Goal: A bank automated its loan approval process to predict if an applicant would default on a loan within 2 years.
- Data: Customer profiles containing financial features (income, age, debt-to-income ratio, and past late payments).
- Classifier: A Random Forest Classifier optimized with SMOTE to handle the severe class imbalance of defaulting customers.
- Results: The bank instantly automated 70% of loan approvals, reduced processing time from days to minutes, maintained an F1-Score of 0.84, and decreased overall bad-debt defaults by 12%.

### References 
Financial Journal (MDPI): * Credit Risk Prediction Using Machine Learning: A Study on Credit Card Customers. * URL: Read Article on MDPI.
