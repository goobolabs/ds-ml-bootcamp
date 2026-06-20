# Research Assignment: Introduction to Machine Learning
clear
1. What is Machine Learning? (Definition + Real-Life Example)

Machine Learning (ML) is a branch of Artificial Intelligence that enables computers to learn patterns from data and make predictions or decisions without being explicitly programmed.

Real-life example:

Email Spam Detection

You mark some emails as Spam and others as Not Spam.

The system learns patterns (words, sender, links).

Over time, it automatically classifies new emails correctly.

2. Supervised Learning vs Unsupervised Learning
Supervised Learning

Definition:
Learning from labeled data (data with correct answers).

Example:

Predicting house prices using:

Inputs: size, location, rooms

Output (label): price
Algorithms learn the relationship between inputs and known outputs.

Common algorithms:

Linear Regression

Decision Trees

Support Vector Machines (SVM)

Unsupervised Learning

Definition:
Learning from unlabeled data (no predefined answers).

Example:
Customer segmentation:

Grouping customers based on buying behavior

No labels like “high spender” or “low spender”
Algorithms discover hidden patterns or groups.

Common algorithms:

K-Means Clustering

Hierarchical Clustering

Association Rules

Comparison Table
Feature	Supervised Learning	Unsupervised Learning
Data	Labeled	Unlabeled
Goal	Prediction	Pattern discovery

Example:	Spam detection	Customer clustering
Output	Known categories	Groups/relationships
3. What Causes Overfitting? How Can It Be Prevented?
Overfitting

Overfitting happens when a model learns the training data too well, including noise, but performs poorly on new data.

Causes:

Too complex model

Small training dataset

Too many features

Training for too many iterations

Prevention methods:

Use more data

Apply regularization (L1, L2)

Use cross-validation

Simplify the model

Early stopping

Feature selection

4. Training Data vs Test Data (Split & Importance)
Data Splitting

Typically, data is divided as:

70–80% Training Data

20–30% Test Data

Why split data?

Training data: teaches the model

Test data: checks how well the model performs on unseen data

Example:
If you train and test on the same data, the accuracy will look high—but it will fail in real life.
5. Case Study: Application of Machine Learning in Business
Title

“Predicting Customer Churn Using Machine Learning in the Telecommunications Industry”

Problem

Telecommunication companies lose millions of dollars every year due to customer churn (customers leaving for competitors).
Traditional methods could not accurately predict which customers were likely to leave.

Machine Learning Application

Type of Learning: Supervised Learning

Algorithms Used:

Logistic Regression

Random Forest

Decision Trees

Data Used:

Customer usage patterns

Billing history

Call duration

Customer complaints

Contract type

Each customer record was labeled as:

Churn = Yes

Churn = No

Process

Data collected from thousands of customers

Data split into:

Training data (used to train the model)

Test data (used to evaluate performance)

Model trained to recognize patterns linked to customer churn

Best-performing model selected based on accuracy

Findings

Machine Learning models predicted customer churn with 85–90% accuracy

Random Forest performed better than traditional statistical methods

Key churn indicators identified:

High number of customer complaints

Short contract duration

High monthly charges

Business Impact

Companies were able to:

Identify high-risk customers early

Offer targeted promotions and discounts

Improve customer retention

Resulted in:

Reduced customer loss

Increased revenue

Better customer satisfaction

Conclusion

This case study shows that Machine Learning helps businesses make data-driven decisions, reduce costs, and increase profits by predicting customer behavior accurately.