## Classification

Classification is a supervised machine learning task where the model learns from labeled data and predicts the category (class) of new data.

Classification and regression are both supervised machine learning techniques, but they solve different types of problems.

## Difference Between Classification and Regression

| Feature | Classification | Regression |
|----------|---------------|------------|
| **Predicts** | Category (Class/Label) | Continuous Number |
| **Output** | Yes, No, Cat, Dog | 150, 25.5, \$3000 |
| **Goal** | Identify which group an item belongs to | Estimate a numeric value |
| **Example** | Spam or Not Spam | House Price Prediction |
| **Target Variable** | Categorical | Continuous |

## Example of Classification and regration

### Example 1: Email Spam Detection

**Input**

Email

**Output**

- Spam
- Not Spam

## Real-Life Example of Regression

### House Price Prediction

**Input**

- Bedrooms
- Bathrooms
- Location
- Square Feet

**Output**

$235,600

## Classification Algorithms

### 1. Logistic Regression

logistic regration It is mainly used for binary classification problems, where the output has only two possible classes.Instead of predicting a continuous number, Logistic Regression predicts the **probability** that a data point belongs to a particular class, also learns the relationship between the input features (hours studied) and the target (pass/fail).

Examples:

- Yes / No
- Spam / Not Spam
- Fraud / Not Fraud
- Pass / Fail

### Real-World Use Cases

- Email spam detection
- Disease diagnosis
- Loan approval prediction
- Customer churn prediction
- Credit card fraud detection

### Advantages

- Simple and easy to understand.
- Fast to train.
- Works well on linearly separable data.
- Produces probabilities.

### Limitations

- Cannot model complex relationships.
- Performs poorly when classes overlap heavily.
- Sensitive to outliers.

### 2. Decision Tree

A Decision Tree is a supervised learning algorithm that makes predictions by asking **if-else questions**.

It resembles a flowchart where:

- Internal nodes represent decisions.
- Branches represent possible outcomes.
- Leaf nodes represent the final prediction.


#### Basic Idea (How It Works)

Suppose a bank wants to approve loans.

The Decision Tree may ask:

Is Income > $40,000?
        │
     Yes      No
      │        │
 Owns House?   Reject
   │
Yes     No
 │        │
approve   reject

#### Real-World Use Cases

- Loan approval
- Medical diagnosis
- Employee recruitment
- Customer segmentation
- Risk assessment

#### Advantages

- Very easy to understand and visualize.
- Handles numerical and categorical data.
- Requires little data preprocessing.
- Can model nonlinear relationships.
- Feature scaling is usually unnecessary.

### 3. Random Forest

Random Forest is an **ensemble learning algorithm** that combines many Decision Trees to make a more accurate prediction.

Instead of relying on one tree, Random Forest builds **hundreds of trees** and combines their predictions.

Think of it as asking many experts instead of just one.

#### Basic Idea (How It Works)

Imagine we have 100 Decision Trees.

Each tree predicts whether an email is spam.

Example
Tree 1 → Spam
Tree 2 → Spam
Tree 3 → Not Spam
Tree 4 → Spam

#### Real-World Use Cases

- Disease prediction
- Credit risk analysis
- Fraud detection
- Stock market trend prediction
- Customer behavior prediction
- Recommendation systems

#### Advantages

- High prediction accuracy.
- Reduces overfitting.
- Handles missing values reasonably well.
- Works with large datasets.
- Can model complex relationships.
- Provides feature importance scores.

#### Limitations

- Slower than Logistic Regression and Decision Trees.
- Requires more memory.
- Harder to interpret.
- Training can be computationally expensive.

## Classification Metric

A classification metric is a measurement used to determine how accurately a classification model predicts the correct class labels.

- Accuracy → How many predictions are correct overall?
- Precision → When the model predicts "Positive," how often is it correct?
- Recall → Out of all the actual positive cases, how many did the model correctly identify?
- F1-Score → How well does the model balance Precision and Recall?
- Confusion Matrix → How do the model's predictions compare with the actual outcomes?

### Comparison of All Metrics

| **Metric** | **What It Measures** | **Best Used When** | **Sensitive to Class Imbalance?** |
|-------------|----------------------|--------------------|-----------------------------------|
| **Accuracy** | Overall percentage of correct predictions | Classes are balanced | ✅ Yes (can be misleading) |
| **Precision** | Correctness of positive predictions | False Positives are costly | ⚠️ Less sensitive |
| **Recall** | Ability to find all actual positives | False Negatives are costly | ⚠️ Less sensitive |
| **F1-Score** | Balance between Precision and Recall | Imbalanced datasets | ❌ No (preferred) |
| **Confusion Matrix** | Complete breakdown of TP, TN, FP, and FN | Understanding model errors | ❌ No |

## Class Imbalance

Class imbalance occurs when one class has significantly more samples than the other class(es) in a dataset.
For example, in a loan approval dataset:

- for example

| Loan Status | Number of Applications |
|-------------|-----------------------:|
| Approved | 9,500 |
| Rejected | 500 |

### Prioritize Precision Over Recall

I prioritize Precision when False Positives are more costly than False Negatives.

- Loan Approval Example

Suppose the bank wants to approve loans only to applicants who are highly likely to repay them.

A False Positive:

The model predicts Approved.
The applicant should actually have been Rejected.

This could result in:

- Financial losses
- Increased business risk

Therefore, the bank wants every approved loan to be as trustworthy as possible.

### Prioritize Recall Over Precision

I prioritize Recall when False Negatives are more costly than False Positives.

Loan Approval Example

Suppose the bank's goal is to identify every qualified applicant.

A False Negative:

The applicant actually deserves approval.
The model incorrectly rejects the application.

This could result in:

- Losing good customers
- Reduced business opportunities
- Lower customer satisfaction

Recall is more important than Precision.

## Real-World Case Study: Breast Cancer Diagnosis Using Machine Learning Classification

### Project Goal

The goal of this project was to develop a machine learning model that could accurately classify breast tumors as either:

- **Malignant (Cancerous)**
- **Benign (Non-cancerous)**

Early and accurate diagnosis is extremely important because it allows doctors to begin treatment sooner, improving patient outcomes while reducing unnecessary medical procedures.

### Data Used

The study used the **Breast Cancer Wisconsin (Diagnostic) Dataset (WDBC)** from the **UCI Machine Learning Repository**.

### Dataset Information

| Feature | Description |
|---------|-------------|
| Dataset Name | Breast Cancer Wisconsin (Diagnostic) Dataset |
| Total Samples | 569 patients |
| Classes | Malignant, Benign |
| Number of Features | 30 numerical features |
| Feature Source | Measurements extracted from digitized fine-needle aspiration (FNA) images of breast cell nuclei |

### Type of Classifier Applied

The researchers used **Logistic Regression**, a supervised machine learning algorithm designed for **binary classification**.


# Key Results

The Logistic Regression model achieved excellent performance.

| Metric | Result |
|---------|--------|
| Accuracy | **98.25%** |
| Sensitivity (Recall) | **97.62%** |
| Specificity | **98.61%** |
| ROC-AUC | **0.9954** |
| Misclassified Cases | Only **2** test samples |


