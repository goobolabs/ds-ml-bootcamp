# Lesson 5 – Classification

> In **Lesson 4**, we built regression models to predict house prices — continuous numbers. Now we switch to **Classification**: predicting which *category* something belongs to. Our project this lesson: **loan approval**.

---

## What You'll Learn

By the end of this lesson, students will be able to:

- Explain what Classification is and when to use it instead of Regression.
- Preprocess a loan dataset for classification (label encoding, class balance, scaling).
- Distinguish between Logistic Regression and Random Forest for classification tasks.
- Evaluate classification models using Accuracy, Precision, Recall, F1-Score, and the Confusion Matrix.

---

## What is Classification?

Instead of predicting a number, we predict a **label** — a category or yes/no answer. Our running example: should a bank **approve or reject** a loan application based on the applicant's profile?

### Definition

- **Classification** is a type of supervised learning where the target variable is **categorical** (e.g., Approved/Rejected, Yes/No, Pass/Fail).
- The model learns from labeled data and predicts which class a new observation belongs to.

### Real-World Examples

- 🏦 **Loan Approval:** Predict whether a loan application should be approved or rejected.
- 📱 **Customer Churn:** Predict whether a customer will leave a service or stay.
- 🏥 **Medical Screening:** Predict whether a patient has a condition or is healthy.
- 🛒 **Fraud Detection:** Predict whether a transaction is legitimate or fraudulent.

### Contrast with Regression

- **Regression:** Output is a **number** (e.g., \$350,000 house price, 25°C).
- **Classification:** Output is a **category** (e.g., Approved vs Rejected).

Quick check:

- Predicting whether a loan is approved or rejected → **Classification**
- Predicting the rent price of an apartment → **Regression**

> Regression = predicting **how much**. Classification = predicting **which class**.

---

## Classification Algorithms

### Logistic Regression

- Despite the name, Logistic Regression is used for **classification**, not regression.
- It estimates the **probability** that an input belongs to a class, then picks the most likely class.
- Internally, it uses the **sigmoid function** to squash outputs into a range between 0 and 1.

#### Example (Loan Approval)

- **Inputs (features):** Income, credit score, employment years, loan amount.
- **Output (label):** Approved (1) or Rejected (0).

The model might learn: higher income + better credit score → higher probability of approval.

#### Visual Intuition

- Imagine plotting one feature (credit score) against approve/reject outcomes.
- Instead of fitting a straight regression line, Logistic Regression fits an **S-shaped curve**.
- Points near the middle of the curve are uncertain; points at the top or bottom are confident predictions.

#### Why It's Useful

- Simple and fast — a strong **baseline** for binary classification.
- Outputs **probabilities**, not just hard labels (e.g., "82% chance of approval").
- Easy to interpret: you can see which features push the prediction toward approval or rejection.

> Logistic Regression = a simple classifier that turns features into **class probabilities** using an S-shaped curve.

### Random Forest

- A Random Forest is an **ensemble** of many decision trees trained on random subsets of the data and features.
- Each tree votes; the **majority vote** wins as the final prediction.
- Averaging many trees reduces overfitting and usually gives stronger results than a single model.

#### Example (Loan Approval)

- **Inputs (features):** Income, credit score, loan amount, collateral, employment years.
- **Output (label):** Approved (1) or Rejected (0).

One tree might overfit on a few unusual applicants, but 100 trees voting together produce a more stable approve/reject decision.

#### Visual Intuition

- Imagine 100 different trees, each trained on a slightly different slice of loan applications.
- For a new applicant, each tree casts a vote: Approve or Reject.
- If 72 trees say Approve and 28 say Reject, the prediction is **Approved**.

#### Why It's Useful

- Usually **more accurate** than Logistic Regression on complex patterns.
- Handles non-linear relationships without heavy feature engineering.
- Less interpretable than Logistic Regression — you trade clarity for performance.

> Random Forest = many trees voting together; stronger and more stable than a single classifier.

#### Algorithm Comparison

| Feature             | Logistic Regression | Random Forest              |
| ------------------- | ------------------- | -------------------------- |
| Output              | Class probabilities | Hard class label (vote)    |
| Interpretability    | High                | Lower                      |
| Non-linear patterns | Limited             | Yes                        |
| Overfitting risk    | Low                 | Lower (ensemble averaging) |
| Best as             | Simple baseline     | Strong general-purpose model |

### Beyond These Two Algorithms

Classification is **not limited** to Logistic Regression and Random Forest. Other common classifiers include Decision Trees, KNN, Naive Bayes, and SVM.

In class we walk through the full loan pipeline — preprocessing plus **Logistic Regression** and **Random Forest**. In **Assignment 5**, you reproduce that pipeline in notebooks and **research one additional algorithm** to implement as a third classifier.

---

## Classification Metrics

When we build a classification model, accuracy alone is not always enough — especially when classes are **imbalanced** (e.g., 95% approved, 5% rejected). **Metrics** tell us exactly where the model succeeds and where it fails.

### Accuracy

- **Idea:** Of all predictions made, how many were correct?
- **Example:** Model scored 100 loan applications — 90 decisions were correct → **Accuracy = 90%**.

> Use Accuracy when classes are **roughly balanced**. It can be misleading when one class dominates (e.g., 99% approved → a model that always says "approved" gets 99% accuracy but rejects every risky applicant).

### Precision

- **Idea:** Of all cases the model **predicted as approved**, how many were **actually approved**?
- **Example:** Model approved 10 applications → 7 were truly creditworthy → **Precision = 7/10 = 70%**.

> Use Precision when **false positives are costly** — e.g., approving a loan to someone who will default, or wrongly flagging a legitimate transaction as fraud.

### Recall (Sensitivity)

- **Idea:** Of all **actually approvable** applications, how many did the model **correctly approve**?
- **Example:** There are 10 applications that should be approved → model approved 7 → **Recall = 7/10 = 70%**.

> Use Recall when **false negatives are costly** — e.g., rejecting a good applicant who would have repaid, or missing a risky borrower the bank wanted to catch.

### F1-Score

- **Idea:** A single score that **balances** Precision and Recall — if either drops sharply, F1 drops too.
- **Example:** Precision = 0.7, Recall = 0.7 → **F1 = 0.7**.

> Use F1 when classes are **imbalanced** and you care about both catching approvals and avoiding bad approvals.

### Confusion Matrix

- **Idea:** A table showing the **full breakdown** of correct and incorrect predictions.

|                     | **Predicted Approved** | **Predicted Rejected** |
| ------------------- | ---------------------- | ---------------------- |
| **Actually Approved** | True Positive (TP) ✅   | False Negative (FN) ❌  |
| **Actually Rejected** | False Positive (FP) ❌  | True Negative (TN) ✅   |

- Every other metric (Accuracy, Precision, Recall, F1) can be calculated from these four counts.
- Reading the matrix shows **exactly what kind of mistakes** the model makes — wrong approvals vs missed good applicants.

### Summary Table

| Metric           | Question it answers                                       | Sensitive to imbalance? |
| ---------------- | --------------------------------------------------------- | ----------------------- |
| Accuracy         | How many predictions are correct overall?                 | ✅ Yes                   |
| Precision        | Of predicted approvals, how many were actually approvable? | ❌ No                    |
| Recall           | Of actual approvals, how many did the model catch?          | ❌ No                    |
| F1-Score         | How well do Precision and Recall balance?                   | ❌ No                    |
| Confusion Matrix | What are the counts of TP, FP, FN, TN?                     | Shows full picture      |

---

## Coding Session

Theory done — now we go hands-on. Run both scripts in order:

**Step 1 — Preprocessing**

[`code/loan-data-processing.py`](../code/loan-data-processing.py)

```bash
python code/loan-data-processing.py
```

This applies the 11 steps above and saves `dataset/clean_loan_dataset.csv`.

**Step 2 — Classification**

[`code/loan-approval-classifier.py`](../code/loan-approval-classifier.py)

```bash
python code/loan-approval-classifier.py
```

This script loads the cleaned dataset, splits with a **stratified** 80/20 train/test split, trains **Logistic Regression** and **Random Forest**, prints Accuracy, Precision, Recall, F1-Score, and the Confusion Matrix for each model, then runs a single-row sanity check.

In **Assignment 5**, you reproduce both pipelines in Jupyter notebooks and add a **third classifier** you research yourself.

---

## Summary

- **Classification:** A supervised learning method used to **predict categories** — our project predicts **approved vs rejected** loan applications.
- **Preprocessing:** Clean currency, fix Yes/No typos, impute, cap outliers, label-encode, check class balance, engineer features, scale numerics — save `clean_loan_dataset.csv`.
- **Logistic Regression:** Maps features to **class probabilities** using a sigmoid curve — simple, fast baseline.
- **Random Forest:** An **ensemble of trees** that vote — usually more accurate and robust than Logistic Regression alone.
- **Coding session:** Run [`loan-data-processing.py`](../code/loan-data-processing.py) then [`loan-approval-classifier.py`](../code/loan-approval-classifier.py).
- **Assignment 5:** Reproduce the in-class pipeline in notebooks and research **one additional classifier** beyond Logistic Regression and Random Forest.
- **Key Difference from Regression:**

  - Regression → predicts **numbers**.
  - Classification → predicts **classes**.

- **Metrics to Evaluate Models:**

  - **Accuracy:** Overall correctness — best when classes are balanced.
  - **Precision:** Quality of approval predictions — avoid wrong approvals.
  - **Recall:** Coverage of actual approvals — avoid rejecting good applicants.
  - **F1-Score:** Balanced measure of Precision and Recall.
  - **Confusion Matrix:** Full table of TP, FP, FN, TN — the foundation for all other metrics.

---

*End of Lesson 5*
