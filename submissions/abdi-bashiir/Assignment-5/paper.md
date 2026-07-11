# Introduction to Classification in Machine Learning

## What is Classification?

Classification is a supervised machine learning technique used to predict a **categorical label (class)**. The output is a discrete value such as *Yes/No*, *Spam/Not Spam*, or *Approve/Reject*. The model learns from labeled data and then assigns new inputs into predefined categories.

---

## How is Classification Different from Regression?

The main difference lies in the output type:

- **Classification** → Predicts **categories (discrete values)**
- **Regression** → Predicts **continuous values (real numbers)**

### Example:
- Classification: Predict whether a customer will **stay or leave**
- Regression: Predict the **price of a house**

---

## Real-Life Examples

| Type            | Example |
|-----------------|--------|
| Classification  | **:contentReference[oaicite:0]{index=0}** – Predict whether a customer will stay or leave |
| Regression      | **:contentReference[oaicite:1]{index=1} Real Estate** – Predict house price |

---

# Classification Algorithms

## 1. Logistic Regression

### How it works
Logistic Regression is used for binary classification. It applies a **sigmoid function** to convert outputs into probabilities between 0 and 1.

### Use Case
- **:contentReference[oaicite:2]{index=2}** – Predict whether a customer will renew an internet package

### Advantages
- Simple and fast
- Outputs probabilities
- Works well for linearly separable data

### Limitations
- Poor performance on complex patterns
- Sensitive to outliers
- Assumes linear relationships

---

## 2. Decision Trees

### How it works
Decision Trees split data using **if-else rules** until a decision is made.

### Use Case
- **Hayat Market** – Predict whether a customer will buy a promotional product

### Advantages
- Easy to interpret
- Works with numerical and categorical data
- Requires little preprocessing

### Limitations
- Prone to overfitting
- Can be unstable

---

## 3. Random Forest

### How it works
Random Forest combines multiple decision trees and takes a majority vote for prediction.

### Use Case
- **:contentReference[oaicite:4]{index=4}** – Detect fraudulent transactions  
- **:contentReference[oaicite:5]{index=5}** – Fraud detection systems

### Advantages
- High accuracy
- Reduces overfitting
- Works well with large datasets

### Limitations
- Less interpretable
- Computationally expensive

---

# Classification Metrics

## Definitions

- **Accuracy** → Overall correctness of predictions  
- **Precision** → How many predicted positives are correct  
- **Recall** → How many actual positives are detected  
- **F1-Score** → Balance between precision and recall  
- **Confusion Matrix** → Table showing prediction outcomes

---

## Comparison Table

| Metric | Meaning | Sensitivity to Imbalance |
|--------|--------|--------------------------|
| Accuracy | Overall correctness | High (can be misleading) |
| Precision | Correctness of positive predictions | Medium |
| Recall | Detection of actual positives | High importance |
| F1-Score | Balance of precision & recall | Balanced |
| Confusion Matrix | TP, TN, FP, FN breakdown | Analysis tool |

---

## Real-Life Meaning

- **Precision (Email Spam Filter):** Avoid marking real emails as spam  
- **Recall (Hospital):** Detect all sick patients  
- **Accuracy (School):** Predict pass/fail  
- **Confusion Matrix (Security System):** Authorized vs unauthorized detection  

---

# Class Imbalance

## Why Accuracy Can Be Misleading

Accuracy fails when one class dominates the dataset. For example, in fraud detection, 99% of transactions are normal and only 1% are fraud. A model predicting “no fraud” always would still get 99% accuracy but is useless.

Example:
- **:contentReference[oaicite:6]{index=6}**
- **:contentReference[oaicite:7]{index=7}**
- **:contentReference[oaicite:8]{index=8}**

---

## Precision vs Recall (Loan Approval Example)

- **Precision Priority:** When approving bad loans is costly  
  → Bank wants to avoid risky customers

- **Recall Priority:** When missing good customers is costly  
  → Bank wants to approve all eligible applicants

---

# Real-World Case Study: Fraud Detection in Banking

## Goal
Detect fraudulent transactions automatically.

## Data Used
- Transaction amount  
- Time  
- Location  
- Customer history  
- Device information  

## Model Used
Random Forest and ensemble models are commonly used.

## Example Institutions
- **:contentReference[oaicite:9]{index=9}**
- **:contentReference[oaicite:10]{index=10}**

## Key Insights
- Fraud data is highly imbalanced  
- Accuracy is not enough  
- Precision and recall are more important  
- Feature engineering improves performance  

---

# Conclusion

Classification is a core machine learning technique used in finance, healthcare, telecom, and education. Algorithms like Logistic Regression, Decision Trees, and Random Forest solve different types of problems. However, evaluating models requires more than accuracy—metrics like precision, recall, and F1-score are essential, especially in imbalanced datasets such as fraud detection systems.