## 1.0 what is classification in ML

Classification is a type of Supervised Machine Learning where the goal is to predict a category (class) rather than a number.

## 1.1 How is it different from regression?

Regression = predicting **how much** . Classification = predicting **which class** .

## 1.3 Give one real-life example of classification and one of regression.

| Hours Studied | Attendance | Result |
| ------------- | ---------- | ------ |
| 2             | 60%        | Fail   |
| 5             | 85%        | Pass   |
| 6             | 95%        | pass   |
| 3             | 70%        | Fail   |

Input

- Hours studied
- Attendance

while **output** will be catagory **pass** or **fail**

| House Size (sq ft) | Bedrooms | House Age (Years) | Price (USD)_(Target)_ |
| ------------------ | -------- | ----------------- | --------------------: |
| 900                | 2        | 15                |               120,000 |
| 1,200              | 3        | 10                |               165,000 |
| 1,500              | 3        | 8                 |               210,000 |
| 1,800              | 4        | 5                 |               275,000 |
| 2,100              | 4        | 3                 |               340,000 |
| 2,500              | 5        | 2                 |               420,000 |

**Features (X): House Size Bedrooms House Age.**

**Target (y): House Price (continuous numeric value)**

## **2\*\***Classification Algorithms\*\*

### \* 2.0 Logistic Regression

**Despite its name, Logistic Regression is a classification algorithm, not a regression algorithm. It predicts the probability that an input belongs to a particular class, then converts that probability into a class label**

#### How it works (Basic Idea)

**Instead of predicting a continuous value, Logistic Regression calculates the probability of belonging to a class using the sigmoid (logistic) function , which produces values between 0 and 1.**

**For example:**

- Probability = 0.90 → Predict **Positive**
- Probability = 0.30 → Predict **Negative**

A threshold (usually **0.5** ) determines the final class.

| Hours Studied | Predicted Probability | Prediction |
| ------------- | --------------------- | ---------- |
| 2             | 0.15                  | Fail       |
| 4             | 0.48                  | Fail       |
| 5             | 0.72                  | Pass       |
| 8             | 0.97                  | Pass       |

## Real-world Use Case

**Email Spam Detection**

Input features may include:

- Number of suspicious words
- Number of links
- Sender reputation

Output:

- Spam
- Not Spam

## Advantages

- Easy to understand and implement.
- Fast to train and predict.
- Produces probabilities, making predictions interpretable.
- Performs well when the relationship between features and the target is approximately linear.
- Works well on small and medium-sized datasets.

## Limitations

- Cannot model very complex decision boundaries.
- Sensitive to outliers and highly correlated features.
- Performance decreases when the data are highly nonlinear.# 2.1 Decision Trees

# 2.1 Decision Trees

A **Decision Tree** predicts a class by asking a series of questions about the input data. Each answer leads to another question until a final prediction (leaf node) is reached.

## How it works (Basic Idea)

The algorithm repeatedly selects the feature that best separates the data into different classes.

Example:

Age > 18?
/
No Yes
Reject Income > $3000?
/
No Yes
Reject Approve

## Advantages

- Easy to understand and visualize.
- No feature scaling is required.
- Can handle both numerical and categorical data.
- Captures nonlinear relationships.
- Predictions are easy to explain.

## Limitations

- Can easily overfit the training data.
- Small changes in the data may produce a very different tree.
- Often less accurate than ensemble methods such as Random Forest.
- Deep trees can become complex and difficult to generalize.

# 2.2 Random Forest

A **Random Forest** is an **ensemble learning** algorithm that combines many Decision Trees to make a final prediction.

## How it works (Basic Idea)

Suppose 100 trees are trained.

For a new customer:

| Tree     | Prediction |
| -------- | ---------- |
| Tree 1   | Approve    |
| Tree 2   | Reject     |
| Tree 3   | Approve    |
| ...      | ...        |
| Tree 100 | Approve    |

**Results:**

- **Approve = 76 votes**
- **Reject = 24 votes**

**Final prediction: Approve**

## Advantages

- High predictive accuracy.
- Reduces overfitting compared with a single Decision Tree.
- Handles large datasets and many features well.
- Works with numerical and categorical data.
- Robust to noise and missing values.
- Can estimate feature importance.

## Limitations

- More computationally expensive than a single Decision Tree.
- Slower to train and predict.
- Harder to interpret because many trees contribute to the final decision.
- Requires more memory.

| Feature                         | Logistic Regression                                     | Decision Tree                                          | Random Forest                                                       |
| ------------------------------- | ------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------- |
| Basic Idea                      | Predicts class probabilities using the sigmoid function | Makes predictions through a sequence of decision rules | Combines predictions from many Decision Trees using majority voting |
| Handles Nonlinear Relationships | Limited                                                 | Yes                                                    | Yes                                                                 |
| Interpretability                | High                                                    | Very High                                              | Low to Moderate                                                     |
| Risk of Overfitting             | Low to Moderate                                         | High                                                   | Low                                                                 |
| Training Speed                  | Fast                                                    | Fast                                                   | Slower                                                              |
| Prediction Accuracy             | Good for simple problems                                | Good                                                   | Usually the highest of the three                                    |
| Feature Scaling Needed          | Often helpful                                           | Not required                                           | Not required                                                        |
| Real-world Example              | Spam detection                                          | Loan approval                                          | Fraud detection                                                     |

## **3 Classification Metrics**

**3.0** **Accuracy** **measures the proportion of all predictions that are correct.**

**It tells us how often the classifier is correct overall .**

**Accuracy**=**TP+TN/**TP+TN+FP+FN\*\*\*\*

### Example

**Suppose:**

- TP = 45
- TN = 42
- FP = 8
- FN = 5

**Total predictions = 100**

**Accuracy = (45 + 42) / 100 = 87%**

##### 3.1Precision measures how many of the predicted positive cases are actually positive

It answers the question:

> **"When the model predicts Positive, how often is it correct?**

**Precision**=**TP/TP+FP**

### Example

**Suppose:**

- **TP = 90**
- **FP = 10**

Precision = 90 / (90 + 10)

= **90%**

###### **3.2 Recall** measures how many actual positive cases the model correctly identifies.

It answers the question:

\***\*"Out of all actual positive cases, how many did the model find?"\*
Recall=**TP/TR+FN\*\*\***\*\*\***

**Example**

**Suppose:**

- TP = 90
- FN = 10

**Recall = 90 / (90 + 10)**

**= 90%**
**3.3 The F1-Score combines Precision and Recall into a single metric.**

### What it Measures

**It provides a balanced measure of Precision and Recall.**

### What it Measures

**It provides a balanced measure of Precision and Recall.**

| **Metric**           | **What It Measures**                      | **Formula**                                     | **Best Used When**                              | **Sensitivity to Class Imbalance**                                                  |
| -------------------- | ----------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Confusion Matrix** | Counts TP, TN, FP, and FN                 | Not a formula                                   | Understanding prediction outcomes               | Not affected directly; provides the counts used by other metrics                    |
| **Accuracy**         | Overall proportion of correct predictions | (TP + TN) / Total                               | Classes are balanced                            | **High**– can be misleading on imbalanced datasets                                  |
| **Precision**        | Correctness of positive predictions       | TP / (TP + FP)                                  | False positives are costly                      | **Moderate**– more informative than accuracy for imbalanced data                    |
| **Recall**           | Ability to detect actual positive cases   | TP / (TP + FN)                                  | False negatives are costly                      | **Moderate**– useful for imbalanced datasets where finding positives matters        |
| **F1-Score**         | Balance between Precision and Recall      | 2 × (Precision × Recall) / (Precision + Recall) | Both false positives and false negatives matter | **Low**– preferred for imbalanced datasets because it balances precision and recall |

# Class Imbalance

## What is Class Imbalance?

**Class imbalance** occurs when one class has significantly more examples than another class in a dataset.

For example, in a loan approval dataset:

| Loan Status | Number of Applications |
| ----------- | ---------------------: |
| Approved    |                    950 |
| Rejected    |                     50 |

Here, the dataset is **imbalanced** because there are many more approved loans than rejected loans.

---

# Why Can Accuracy Be Misleading When Classes Are Imbalanced?

**Accuracy** measures the percentage of correct predictions out of all predictions.

[
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
]

When one class is much larger than the other, a model can achieve a **high accuracy simply by predicting the majority class**, even if it completely fails to identify the minority class.

### Example

Suppose a bank has **1,000** loan applications.

| Actual Status | Number |
| ------------- | -----: |
| Approved      |    950 |
| Rejected      |     50 |

Imagine the model predicts **Approved** for every application.

| Actual / Predicted | Approved | Rejected |
| ------------------ | -------- | -------- |
| Approved           | 950      | 0        |
| Rejected           | 50       | 0        |

Accuracy:

[
\frac{950}{1000}=95%
]

The model has **95% accuracy**, which appears excellent.

However, it **failed to identify all 50 rejected applications**, making it unreliable for helping the bank manage lending risk.

**Conclusion:** In imbalanced datasets, a high accuracy does not necessarily mean the model performs well. Metrics such as **Precision**, **Recall**, and **F1-Score** provide a more complete evaluation.

---

# When Should You Prioritize Precision?

You should prioritize **Precision** when **false positives are more costly than false negatives**.

Precision answers the question:

> **"When the model predicts Positive, how often is it correct?"**

### Loan Approval Example

Suppose the bank defines the **positive class** as **Approved**.

A **false positive** means:

- The model approves a loan for someone who should actually be rejected.

This can lead to:

- Financial losses
- Higher default rates
- Increased lending risk

In this case, the bank wants to ensure that **approved loans are truly good candidates**, so **high Precision** is more important.

### Example

| Prediction | Actual Result                |
| ---------- | ---------------------------- |
| Approved   | Approved ✅                  |
| Approved   | Rejected ❌ (False Positive) |

The bank wants to minimize these incorrect approvals.

**Priority:** Precision

---

# When Should You Prioritize Recall?

You should prioritize **Recall** when **false negatives are more costly than false positives**.

Recall answers the question:

> **"Out of all actual positive cases, how many did the model correctly identify?"**

### Loan Approval Example

Suppose the bank wants to identify **all customers who truly qualify for a loan**.

A **false negative** means:

- The model rejects an applicant who actually deserves approval.

Consequences include:

- Losing good customers
- Reduced revenue
- Lower customer satisfaction

If attracting and retaining qualified borrowers is the bank's main goal, the bank should prioritize **Recall** to ensure that most eligible applicants are identified.

### Example

| Prediction | Actual Result                |
| ---------- | ---------------------------- |
| Rejected   | Approved ❌ (False Negative) |
| Approved   | Approved ✅                  |

The bank wants to reduce these missed opportunities.

**Priority:** Recall

---

# Precision vs. Recall in Loan Approval

| Situation                            | Priority      | Reason                                          |
| ------------------------------------ | ------------- | ----------------------------------------------- |
| Avoid approving risky applicants     | **Precision** | Reduces false positives (incorrect approvals).  |
| Avoid rejecting qualified applicants | **Recall**    | Reduces false negatives (incorrect rejections). |

---

# Summary

- **Class imbalance** occurs when one class has many more examples than another.
- **Accuracy** can be misleading because predicting only the majority class can still produce a high accuracy while ignoring the minority class.
- **Precision** should be prioritized when the cost of **incorrectly approving** a loan (false positive) is high.
- **Recall** should be prioritized when the cost of **incorrectly rejecting** a qualified applicant (false negative) is high.
- In practice, banks often seek a balance between Precision and Recall, depending on their lending policies and risk tolerance.

# Real-World Case Study: Using Machine Learning to Detect Diabetes

## Project Title

**Exploratory Study on Classification of Diabetes Mellitus Through a Combined Random Forest Classifier** (published in _BMC Medical Informatics and Decision Making_, 2021). ([Springer][1])

---

## Goal of the Study

The primary goal of the study was to **identify individuals at high risk of diabetes mellitus (DM)** as early as possible using machine learning classification techniques.

Early detection enables healthcare providers to:

- Diagnose diabetes sooner.
- Begin treatment earlier.
- Reduce the risk of serious complications such as heart disease, kidney failure, and blindness. ([Springer][1])

---

## Data Used

The researchers used **medical survey data** containing health information from individuals. The dataset included demographic, lifestyle, and clinical features such as:

- Age
- Body Mass Index (BMI)
- Blood pressure
- Heart rate
- History of hypertension
- History of hyperlipidemia
- Geographic region

Because the dataset was **imbalanced** (fewer diabetic cases than non-diabetic cases), the researchers applied **SVM-SMOTE**, a resampling technique, to balance the classes before training the models. ([Springer][1])

---

## Type of Classifier Applied

The study compared several supervised classification algorithms, including:

- Logistic Regression
- Decision Tree
- Random Forest
- Other machine learning classifiers

After comparing their performance, the **Random Forest classifier** combined with **LASSO feature selection** and **SVM-SMOTE** produced the best results. ([Springer][1])

---

## Key Results and Insights

The Random Forest model achieved the strongest performance:

- **Accuracy:** 89.0%
- **Precision:** 86.9%
- **Recall:** 91.9%
- **F1-Score:** 89.3%
- **AUC:** 94.8% ([Springer][1])

The study also found that the most important factors for predicting diabetes included:

- Age
- Body Mass Index (BMI)
- Hypertension
- Hyperlipidemia
- Heart rate
- Geographic region ([Springer][1])

The researchers concluded that Random Forest is an effective tool for identifying people at high risk of diabetes and can support healthcare professionals in early screening and preventive care. ([Springer][1])

---

# Summary Table

| Aspect              | Description                                                                                                                                                                                     |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Field**           | Healthcare                                                                                                                                                                                      |
| **Problem**         | Early detection of diabetes mellitus                                                                                                                                                            |
| **Goal**            | Classify individuals as high-risk or low-risk for diabetes                                                                                                                                      |
| **Data Used**       | Demographic, clinical, and lifestyle information (e.g., age, BMI, blood pressure, heart rate, hypertension, hyperlipidemia)                                                                     |
| **Classifier Used** | Random Forest (compared with Logistic Regression, Decision Tree, and others)                                                                                                                    |
| **Performance**     | Accuracy = 89.0%, Precision = 86.9%, Recall = 91.9%, F1-Score = 89.3%, AUC = 94.8%                                                                                                              |
| **Key Insight**     | Random Forest provided the best overall performance and showed that age, BMI, hypertension, hyperlipidemia, heart rate, and region were among the most influential predictors of diabetes risk. |

### Conclusion

This case study demonstrates how **classification algorithms** can solve real-world healthcare problems. By applying a **Random Forest classifier** to patient data, researchers were able to accurately identify individuals at high risk of diabetes. Such models can help doctors make earlier diagnoses, improve treatment planning, and reduce the long-term impact of chronic diseases through timely intervention.

[1]: https://link.springer.com/article/10.1186/s12911-021-01471-4?utm_source=chatgpt.com
