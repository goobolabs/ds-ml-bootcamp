# Machine Learning Classification

**Part A – Theory**

**Student:** Mohamed Abdirahman

---

# Introduction to Classification

## What is Classification in Machine Learning?

Classification is a type of supervised machine learning used to predict categories or class labels instead of numerical values. A classification model learns patterns from labeled training data and predicts which class a new observation belongs to.

Classification is commonly used when the target variable has two or more categories, such as **Yes/No**, **Approved/Rejected**, or **Spam/Not Spam**. After learning from historical data, the model can classify new data based on the relationships it has learned.

## Difference Between Classification and Regression

Although both classification and regression are supervised learning techniques, they solve different problems.

Classification predicts **categories**, while regression predicts **continuous numerical values**.

For example:

- Predicting whether a bank should approve or reject a loan application is a **classification** problem because the output is either **Approved** or **Rejected**.
- Predicting the selling price of a used car is a **regression** problem because the output is a **numeric value**.

**In simple terms:**

- **Classification:** "Which class?"
- **Regression:** "How much?"

## Real-Life Examples

### Classification Example

A bank predicts whether a loan application should be **Approved** or **Rejected** using information such as income, credit score, employment history, and collateral.

### Regression Example

A car dealership predicts the selling price of a used vehicle using mileage, manufacturing year, accident history, and location.

---

# Classification Algorithms

## Logistic Regression

### Basic Idea

Despite its name, Logistic Regression is a classification algorithm. It estimates the probability that a data point belongs to a particular class using the **sigmoid function**. The predicted probability is then converted into a class label.

### Real-World Use Case

Banks use Logistic Regression to estimate the probability that a customer qualifies for a loan.

### Advantages

- Simple and fast
- Easy to understand and interpret
- Produces prediction probabilities

### Limitations

- Assumes a mostly linear relationship between features and the target
- May perform poorly on highly complex datasets

---

## Decision Tree

### Basic Idea

A Decision Tree classifies data by asking a series of questions about the input features. Each question creates a branch, and the final branch leads to a prediction.

For example, a loan approval model may first check income, then credit score, and finally whether the applicant has collateral before making a decision.

### Real-World Use Case

Insurance companies use Decision Trees to determine whether an applicant is eligible for a specific insurance policy.

### Advantages

- Easy to visualize and understand
- Handles both numerical and categorical data
- Does not require complex preprocessing

### Limitations

- Can easily overfit the training data
- Small changes in the data may produce a different tree

---

## Random Forest

### Basic Idea

Random Forest is an ensemble learning algorithm that combines many Decision Trees. Each tree is trained using a different random sample of the training data, and every tree makes its own prediction. The final prediction is determined by majority voting.

### Real-World Use Case

Financial institutions use Random Forest to detect fraudulent transactions and evaluate loan applications.

### Advantages

- Usually produces higher accuracy
- Handles complex relationships well
- Reduces overfitting compared to a single Decision Tree

### Limitations

- More difficult to interpret
- Requires more computation than Logistic Regression

---

# Comparison of Classification Algorithms

| Algorithm | Basic Idea | Advantages | Limitations |
|-----------|------------|------------|-------------|
| **Logistic Regression** | Predicts class probabilities using the sigmoid function | Simple, fast, interpretable | Limited for complex relationships |
| **Decision Tree** | Uses decision rules to split the data into classes | Easy to understand and visualize | Can overfit the data |
| **Random Forest** | Combines many Decision Trees using majority voting | High accuracy and robustness | Less interpretable and slower |

---

# Classification Metrics

Classification metrics evaluate how well a classification model predicts the correct class.

## Accuracy

Accuracy measures the proportion of correctly classified observations out of all predictions.

It is useful when the dataset contains approximately equal numbers of each class.

---

## Precision

Precision measures how many positive predictions made by the model were actually correct.

Precision is important when false positive predictions are costly.

---

## Recall

Recall measures how many actual positive cases were correctly identified by the model.

Recall is important when missing positive cases would have serious consequences.

---

## F1-Score

The F1-Score combines Precision and Recall into a single value.

It is especially useful when the classes are imbalanced because it balances both measures.

---

## Confusion Matrix

A Confusion Matrix summarizes the model's predictions by showing:

- True Positives (TP)
- False Positives (FP)
- True Negatives (TN)
- False Negatives (FN)

It helps identify the types of mistakes made by the model.

---

# Comparison of Classification Metrics

| Metric | What It Measures | Sensitive to Class Imbalance? |
|--------|-------------------|-------------------------------|
| **Accuracy** | Overall percentage of correct predictions | Yes |
| **Precision** | Correct positive predictions among predicted positives | No |
| **Recall** | Correct positive predictions among actual positives | No |
| **F1-Score** | Balance between Precision and Recall | No |
| **Confusion Matrix** | Counts TP, FP, FN, and TN | Shows the complete picture |

---

# Class Imbalance

Class imbalance occurs when one class contains significantly more samples than another. In this situation, Accuracy can be misleading because a model may achieve a high accuracy simply by predicting the majority class.

For example, imagine that **95%** of loan applications are approved and only **5%** are rejected. A model that always predicts **Approved** would achieve **95% accuracy** but would completely fail to identify rejected applications.

In loan approval prediction, **Precision** should be prioritized when the bank wants to avoid approving applicants who are likely to default on their loans. False approvals can lead to financial losses.

On the other hand, **Recall** should be prioritized when the bank wants to identify as many qualified applicants as possible. A higher Recall reduces the number of good applicants who are incorrectly rejected.

---

# Real-World Case Study

## Loan Approval Prediction Using Classification

### Goal

A financial institution developed a machine learning model to predict whether loan applications should be approved or rejected. The goal was to improve decision-making, reduce financial risk, and speed up the loan approval process.

### Data Used

The dataset included applicant information such as:

- Annual income
- Credit score
- Employment history
- Loan amount
- Previous loan defaults
- Collateral information

The target variable was **Loan Approval**, classified as **Approved** or **Rejected**.

### Classification Algorithm

The project applied **Random Forest Classification** because it can model complex relationships among applicant characteristics and usually provides higher prediction accuracy than a single decision tree.

### Key Results

The study found that **credit score, income, and previous loan defaults** were the most important factors affecting loan approval decisions. Random Forest achieved high classification accuracy while reducing incorrect loan approvals.

The results demonstrated that machine learning can support faster and more consistent loan approval decisions.

---

# Conclusion

Classification is an important supervised learning technique used to predict categories instead of numerical values. Logistic Regression provides a simple and interpretable baseline model, Decision Trees create easy-to-understand decision rules, and Random Forest improves prediction accuracy by combining many decision trees.

Classification metrics such as Accuracy, Precision, Recall, F1-Score, and the Confusion Matrix help evaluate model performance from different perspectives. Understanding these concepts is essential for solving practical classification problems such as loan approval, fraud detection, medical diagnosis, and customer churn prediction.

---

# References

1. Géron, A. (2019). *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* (2nd ed.). O'Reilly Media.
2. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning* (2nd ed.). Springer.
3. Scikit-learn Developers. *Classification Algorithms and Metrics*. https://scikit-learn.org/stable/
4. Breiman, L. (2001). *Random Forests*. *Machine Learning, 45*(1), 5–32.
