---

# Part C — Reflection Paper: Loan Approval Classification

## 1. What I Implemented

In this project, I successfully replicated the Lesson 5 preprocessing pipeline on a tabular loan dataset containing 100 applications. The preprocessing pipeline began by mapping binary columns (`HasCollateral`, `PreviousDefaults`) into numerical values (`1` or `0`). Following this, feature engineering was performed to create two new custom attributes: `DebtToIncome` and `IncomePerYearEmployed`.

To prepare the data for training, a train-test split was performed (80 rows for training, 20 rows for testing). While initially experimenting with `MinMaxScaler`, I pivoted to **`RobustScaler`** to standardize the numerical features. This switch was critical because it scales features like `Income` and `LoanAmount` using the median and interquartile range (IQR), effectively preventing extreme outliers from squashing the remaining data points into a compressed cluster.

Using this scaled data, I trained three distinct classification models to predict loan approval (`Approved = 1`):

1. **Logistic Regression** (from class)
2. **Random Forest** (from class)
3. **Support Vector Machine (SVM)** (additional algorithm)

---

## 2. Comparison of Models

### Metrics & Confusion Matrix Summary

Following the preprocessing adjustments and applying `class_weight='balanced'` to handle the dataset's target imbalance, the models yielded the following test results:

- **Logistic Regression & Random Forest:** Achieved identical results with **70.0% Accuracy**, **0.733 Precision**, and **0.846 Recall**. Their confusion matrices were identical: 11 True Positives (TP), 3 True Negatives (TN), 4 False Positives (FP), and 2 False Negatives (FN).
- **Support Vector Machine (SVM):** Achieved **65.0% Accuracy**, **0.750 Precision**, and **0.692 Recall**. Its confusion matrix recorded: 9 True Positives (TP), 4 True Negatives (TN), 3 False Positives (FP), and 4 False Negatives (FN).

### Sanity Check and Realism Analysis

During the single-row sanity check (evaluating index `2` of the test set), all three models were fully aligned, correctly predicting **"Approved (1)"** matching the actual label.

Despite Logistic Regression and Random Forest sharing a higher overall accuracy (70%), the **Support Vector Machine (SVM) provided a more realistic and practically safer result for a bank deployment**.

- **Why?** In loan classification, a **False Positive** (approving a risky applicant who will default) is vastly more expensive to a bank than a **False Negative** (accidentally rejecting a good applicant).
- The SVM model behaved more cautiously; it successfully caught **4 rejections** (TN) compared to the 3 caught by the other models and dropped False Positives from 4 down to 3. It achieved the highest Precision (75.0%), meaning that when the SVM asserts an applicant is safe to approve, it has the highest level of certainty.

---

## 3. Understanding Random Forest

In my own words, a **Random Forest** is an "ensemble" machine learning algorithm, which means it combines the power of multiple smaller models to make a single, highly accurate decision. Instead of relying on just one complex decision tree—which can easily overfit and misinterpret data patterns—Random Forest constructs hundreds of unique, independent decision trees during training.

To ensure diversity among the trees, the algorithm uses two types of randomness: it feeds each tree a random subset of the training rows (bootstrapping) and allows each split point to choose from only a random subset of features. When a new loan application needs a prediction, every single tree in the forest inspects the features and casts a single "vote" (either Approved or Rejected). The algorithm counts the votes, and the **majority vote** determines the final output.

---

## 4. Other Algorithms (The Third Classifier)

### Choice and Rationale

For my third classifier, I chose the **Support Vector Machine (SVM / SVC)** using a linear kernel. I chose SVM because it is mathematically optimized for small datasets ($N=100$). Rather than evaluating data distributions globally, SVM establishes its boundary using only the data points resting closest to the class thresholds.

### Research Summary

- **How it works:** SVM plots data points in an $N$-dimensional space and searches for an optimal separating hyperplane (boundary line). It seeks to maximize the physical width of the empty space—known as the **margin**—between the closest opposing data classes (the Support Vectors), creating a maximum-margin separator.
- **Advantage:** It is highly effective in high-dimensional spaces and is remarkably memory efficient because it only retains the support vector data points in memory to hold the boundary line.
- **Limitation:** It does not naturally provide probability estimates under the hood (like Logistic Regression does) and requires careful feature scaling to function properly.

### Metric Comparison

When compared directly to Logistic Regression and Random Forest, the SVM broke the architectural tie. While Logistic Regression and Random Forest aggressively pursued approvals (yielding higher Recall at 84.6%), SVM prioritized a clean boundary corridor. This conservative approach resulted in a lower overall accuracy (65% vs 70%) and lower Recall (69.2%), but granted the highest **Precision (75.0%)**, making it the superior algorithm for strict risk avoidance.
