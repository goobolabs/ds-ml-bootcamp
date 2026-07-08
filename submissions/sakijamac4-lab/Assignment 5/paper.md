# Part A  Theory


## 1. Introduction to Classification

### What is Classification in Machine Learning?

Classification is a type of Machine Learning, specifically supervised learning, that predicts a category or class based on the input data provided. Instead of producing a numeric value, a classification model assigns the data to predefined categories, such as "Approved" or "Rejected", "Spam" or "Not Spam", and "Positive" or "Negative".

### How is Classification Different from Regression?

The main difference between Classification and Regression is the type of output they produce. Classification predicts a category or class, such as "Approved" or "Rejected", while Regression predicts a continuous numeric value, such as the price of a house.

### Real-Life Examples

**Classification example:** Customer Churn Prediction  a telecommunications or internet service company uses classification to predict whether a customer will leave the service (Will Leave) or continue using it (Will Stay).

**Regression example:** Estimating the price of a house based on its size, location, and number of rooms.

---

## 2. Classification Algorithms

### Logistic Regression

**How it works:** Logistic Regression is a Supervised Machine Learning algorithm used for Classification. Although its name contains the word "Regression", it is not used to predict continuous numeric values; instead, it is used to predict a category or class, such as Approved/Rejected, Yes/No, or Positive/Negative. It is most commonly used for Binary Classification. Logistic Regression first calculates the probability that a data point belongs to a particular category. To obtain this probability, it uses the Sigmoid Function, which transforms the output into a value between 0 and 1, representing a probability between 0% and 100%.

**Real-world use case:** A bank can use Logistic Regression to determine whether a customer's loan application should be approved or rejected.

**Advantages:**
- It is easy to understand and implement  one of the simplest classification algorithms available.
- It works well for Binary Classification problems with two classes, such as Approved/Rejected or Yes/No.

**Limitations:**
- It performs best when the relationship between the features and the target is simple and linear.
- Its performance can be lower than more advanced algorithms on complex data.

---

### Decision Trees

**How it works:** A Decision Tree is a supervised machine learning algorithm used for both classification and regression. In the context of classification, it predicts a category or class, such as Approved/Rejected or Yes/No. It is called a Decision Tree because it resembles a tree with many branches. Each branch represents a question or decision, until a final outcome is reached. A Decision Tree splits the data by asking a series of questions. For example, in loan approval:
- Income > $50,000? → Yes: ask another question / No: Rejected
- Credit Score > 700? → Yes: Approved / No: Rejected

The model continues splitting the data until it reaches a final decision.

**Real-world use case:** A hospital can use a Decision Tree to determine whether a patient has diabetes or not, based on their symptoms and test results.

**Advantages:**
- Easy to understand and interpret  the decisions it makes can be followed step by step.
- Does not require feature scaling  the data does not need to be standardized or normalized.

**Limitations:**
- It can easily overfit, especially if the tree grows too large.
- A small change in the data can significantly change the structure of the tree.

---

### Random Forest

**How it works:** Random Forest is a classification algorithm made up of many decision trees. Instead of using a single tree, it creates many trees, and each tree independently makes its own prediction. It is called a "Forest" because it consists of many Decision Trees, like a forest made up of many trees. Random Forest creates many trees (for example, 100 or 200 Decision Trees). Each tree makes its own prediction  for example:
- Tree 1 → Approved
- Tree 2 → Approved
- Tree 3 → Rejected
- Tree 4 → Approved
- Tree 5 → Approved

Random Forest then conducts a vote (Voting). If the majority of trees say Approved, the final result is Approved. If the majority say Rejected, the result is Rejected. Therefore, Random Forest does not rely on a single tree  it follows the opinion of the majority (majority vote).

**Real-world use case:** A bank uses Random Forest to predict whether a loan application should be approved or rejected.

**Advantages:**
- Provides higher accuracy compared to a single Decision Tree.
- Reduces overfitting because it uses many trees instead of just one.

**Limitations:**
- Slower than Logistic Regression because it trains many trees.
- Uses more memory and computational resources.

---

### Algorithm Comparison Table

| Feature | Logistic Regression | Decision Tree | Random Forest |
|---|---|---|---|
| How it works | Sigmoid probability curve | Series of yes/no questions | Many trees voting together |
| Interpretability | High | High | Lower |
| Overfitting risk | Low | High | Low (ensemble reduces it) |
| Speed | Fast | Fast | Slower |
| Best used when | Simple binary problems | Small, interpretable tasks | Complex, large datasets |

---

## 3. Classification Metrics

### Accuracy

Accuracy is the proportion of correct predictions made by the model out of all predictions. It answers: "Overall, how often is the model correct?"

**Formula:** (TP + TN) / (TP + FP + FN + TN)

**Example:** If the model makes 100 predictions and 80 are correct → Accuracy = 80%

### Precision

Precision measures how many of the predicted positive cases are actually correct. It answers: "Of all predicted positives, how many were truly positive?"

**Formula:** TP / (TP + FP)

**Example:** If the model predicts 10 people as "Approved" and 7 are truly creditworthy → Precision = 70%

### Recall (Sensitivity)

Recall measures how many of the actual positive cases were correctly identified by the model. It answers: "Of all real positive cases, how many did the model catch?"

**Formula:** TP / (TP + FN)

**Example:** If there are 10 truly good applicants and the model identifies 7 → Recall = 70%

### F1-Score

F1-Score is the harmonic mean of Precision and Recall, balancing both metrics. It answers: "How well does the model balance Precision and Recall?"

**Formula:** 2 × (Precision × Recall) / (Precision + Recall)

**Key idea:** If either Precision or Recall is low, the F1-Score will also be low.

### Confusion Matrix

A Confusion Matrix is a table that shows all correct and incorrect predictions made by the model. It includes:
- **TP (True Positive):** Correct positive prediction
- **FP (False Positive):** Incorrect positive prediction
- **FN (False Negative):** Missed positive case
- **TN (True Negative):** Correct negative prediction

| | Predicted Positive | Predicted Negative |
|---|---|---|
| Actual Positive | TP ✅ | FN ❌ |
| Actual Negative | FP ❌ | TN ✅ |

### Metrics Comparison Table

| Metric | What it measures | When to use | Sensitivity to Class Imbalance |
|---|---|---|---|
| Accuracy | Overall correctness of the model | When classes are balanced | High (can be misleading) |
| Precision | Correctness of positive predictions | When False Positives are costly | Low |
| Recall | Ability to find all positive cases | When False Negatives are costly | Low |
| F1-Score | Balance between Precision and Recall | When dataset is imbalanced | Medium |
| Confusion Matrix | Full breakdown of TP, FP, FN, TN | For detailed model analysis | None |

---

## 4. Class Imbalance

### Why Can Accuracy Be Misleading When Classes Are Imbalanced?

Accuracy can be misleading when classes are imbalanced because it only looks at the overall number of correct predictions, without giving proper attention to the minority class. When one class is much larger than the other, a model can achieve a high accuracy even if it fails to correctly identify the important class. For example, in loan approval, if 95% of applicants are "Approved" and only 5% are "Rejected", a model that predicts "Approved" for everyone would achieve 95% accuracy, but would completely miss all the high-risk applicants (Rejected). Therefore, accuracy alone does not reflect the true performance of the model when the data is not balanced. For this reason, other metrics such as Precision, Recall, and F1-Score become essential to truly understand how the model is performing, especially when it is important to catch critical mistakes.

### When to Prioritize Precision vs. Recall

**Prioritizing Precision over Recall:**
Precision is prioritized when you want to minimize the number of people who are incorrectly approved (False Positives). This means the model must be very cautious before predicting "Approved."

Loan approval example: The bank does not want to give a loan to someone who will not repay it (a risky borrower). If the model incorrectly approves a bad applicant, the bank loses money. Therefore, the bank prioritizes high Precision to ensure that those who are approved are truly creditworthy applicants.

**Prioritizing Recall over Precision:**
Recall is prioritized when you want to capture all the important cases (True Positives), even if some incorrect cases are included.

Loan approval example: If the bank does not want to lose good customers, it focuses on identifying all applicants who can repay the loan. If the model incorrectly rejects a good applicant (False Negative), the bank loses potential profit. Therefore, the bank prioritizes high Recall to avoid missing good applicants.

**Summary:**
- Precision is important → when the cost of "approving a bad applicant" is high.
- Recall is important → when the cost of "missing a good applicant" is harmful.

---

## 5. Real-World Case Study: Healthcare Insurance Fraud Detection (Saudi Arabia, 2023)

**Goal:** The aim of this study was to detect fraud in healthcare insurance claims. The objective was to distinguish between legitimate and fraudulent claims in order to reduce the financial losses faced by insurance companies. Insurance companies encounter a significant challenge: individuals or hospitals sometimes submit false or exaggerated claims for medical services that were never provided or were misrepresented.

**Data Used:** The data was collected from healthcare insurance claims submitted by three hospitals in Saudi Arabia. The dataset included information such as: the type of medical service provided, the cost of treatment, patient information, the history of previous claims, and indicators that may suggest fraudulent activity.

**Classifiers Used:** Three classification models were tested in this study: Random Forest Classifier, Logistic Regression, and Artificial Neural Networks (ANN). These models classified each claim as either "Fraud" or "Not Fraud."

**Key Results and Insights:** The results showed that Random Forest was the best-performing model, successfully identifying fraudulent cases, particularly from the minority class. Logistic Regression and ANN also performed well, but did not reach the accuracy level of Random Forest. It was also found that the dataset suffered from class imbalance, which made metrics such as Recall and F1-Score more important than Accuracy alone.

**Source:** Nabrawi, E. and Alanazi, A. (2023). Fraud detection in healthcare insurance claims using machine learning. *Risks*, 11(9):160.
