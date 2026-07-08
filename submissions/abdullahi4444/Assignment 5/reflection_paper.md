# Reflection Paper: Loan Approval Classification

## 1. What did you implement?

In this assignment, I reproduced the full **Lesson 5** pipeline in Jupyter notebooks, starting from the raw loan dataset and ending with trained and evaluated classification models. In Part B1 (`loan_data_processing.ipynb`), I implemented all eleven preprocessing steps: loading and inspecting the data, stripping currency symbols from `Income` and `LoanAmount`, normalizing typos and abbreviations in `HasCollateral`, `PreviousDefaults`, and `Approved` before imputation, filling missing values with medians (numeric) and modes (categorical), removing duplicate rows, capping outliers with IQR fencing, label-encoding binary columns, checking class balance, engineering two new features (`DebtToIncome` and `IncomePerYearEmployed`), and applying **RobustScaler** to all continuous numeric columns before saving `clean_loan_dataset.csv`.

In Part B2 (`loan_approval_prediction.ipynb`), I loaded the cleaned data, split it 80/20 with stratification, and trained three classifiers: **Logistic Regression** (max\_iter=1000), **Random Forest** (100 trees), and a **Support Vector Machine** (RBF kernel) as my third algorithm. I then evaluated all three models using Accuracy, Precision, Recall, F1-Score, and the Confusion Matrix, and performed a sanity check on a single test row.

---

## 2. Comparison of Models

For the sanity check on test row index 5, the actual label was **Approved (1)**. All three models predicted **Rejected (0)** for this particular sample. This unanimous miss makes sense given the small test set size (only 20 rows) — individual rows close to the decision boundary are inherently uncertain and more likely to be misclassified. It is not an indictment of any one model; it highlights that decisions at the class boundary are the hardest to get right, and that confidence in predictions grows with more training data.

---

## 3. Understanding Random Forest

A Random Forest is an ensemble machine learning algorithm built from a large collection of individual Decision Trees. During training, two sources of randomness are injected to ensure diversity among the trees: first, each tree is trained on a random bootstrap sample of the training data (sampling with replacement); second, at each split point within a tree, only a random subset of features is considered as candidates. This means each tree "sees" a slightly different slice of the data and learns a slightly different decision boundary.

When making a prediction on a new observation, the Random Forest asks every tree in the ensemble to vote — each tree predicts a class (Approved or Rejected) independently. The final output is the class that receives the most votes (majority rule). Because individual trees may overfit to their own random subset of data, their individual errors tend to be different and uncorrelated. When many such trees vote together, the errors cancel out and the majority vote is much more stable and accurate than any single tree. This process — called **ensemble averaging** — is why Random Forest consistently outperforms lone decision trees in practice.

---

## 4. Other Algorithms (Third Classifier — SVM)

I chose **Support Vector Machine (SVC)** with an RBF kernel as my third classifier, for the following reasons: after applying `RobustScaler` in preprocessing, all continuous features are on a comparable scale — a key requirement for SVM to function correctly, since it relies on distances in the feature space. Loan approval decisions can involve non-linear interactions between features (e.g., a moderate income combined with a very high credit score may justify approval in ways a linear model cannot capture), and the RBF kernel is well-suited for learning such curved decision boundaries.

From my research I learned that SVM works by finding the **maximum-margin hyperplane** — the decision boundary that is as far as possible from the nearest training points of each class (the "support vectors"). The RBF kernel implicitly maps the data into a higher-dimensional space where non-linear boundaries become linear, making SVM powerful without explicitly computing that transformation.

**One advantage:** SVM generalizes well on small datasets because it uses only the support vectors (the boundary points) to define the decision, ignoring the bulk of interior training examples. This makes it robust to noise in data-dense regions.

**One limitation:** Training time scales poorly with dataset size (O(n²) to O(n³)), and tuning the `C` (regularization) and `gamma` hyperparameters requires careful cross-validation.

**Metric comparison (positive class = Approved = 1):**

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Logistic Regression | 0.700 | 0.733 | 0.846 | 0.786 |
| Random Forest | 0.650 | 0.714 | 0.769 | 0.741 |
| SVM (RBF) | 0.650 | 0.688 | 0.846 | 0.759 |

SVM achieved the same Recall as Logistic Regression (0.846), outperforming Random Forest in that regard, but had the lowest Precision of the three, resulting in an F1 midway between Logistic Regression and Random Forest.

---

## 5. Metrics Discussion

**Best Accuracy:** Logistic Regression at 0.700, meaning it correctly predicted 14 out of 20 test cases.

**Best Precision:** Logistic Regression at 0.733 — of all the applicants it labeled "Approved," 73.3% were genuinely creditworthy. This matters if the bank wants to avoid bad loans.

**Best Recall (tied):** Logistic Regression and SVM at 0.846 — both caught 11 of the 13 truly approvable applicants in the test set. High recall means fewer good borrowers are wrongly turned away.

**Best F1-Score:** Logistic Regression at 0.786 — the best balance of Precision and Recall.

**What this tells us about each model:**
- **Logistic Regression** is the strongest performer across all four metrics on this particular dataset. Its linear decision boundary, coupled with the feature scaling applied during preprocessing, is well-matched to this relatively small and clean dataset.
- **Random Forest** had slightly lower metrics overall, which is somewhat unexpected — Random Forest typically outperforms Logistic Regression on complex data. The likely explanation is the very small training set (only 80 rows). Ensemble methods generally benefit from more data to diversify their trees, and with only 80 training samples, the individual trees may be noisy and underfit.
- **SVM** matched Logistic Regression on Recall but fell short on Precision and F1, suggesting it is slightly more aggressive about predicting approvals (fewer false negatives but more false positives) compared to Logistic Regression.

---

## 6. Your Findings

For this loan approval prediction task — particularly with the current dataset size — I would choose **Logistic Regression** as my production model. It outperformed both Random Forest and SVM on Accuracy, Precision, and F1-Score, and matched SVM on Recall. Its coefficients are fully interpretable: a bank's compliance team can examine exactly which features (income, credit score, collateral) push the model toward approval or rejection, which is essential for regulatory accountability in lending.

In a real-world deployment, I would also carefully consider the business objective before locking in a final model. If the bank's primary concern is avoiding bad loans (minimizing defaults), I would tune the Logistic Regression threshold upward to prioritize Precision, even at the cost of rejecting some genuinely creditworthy applicants. If the bank is trying to grow its loan book and wants to maximize reach, I would lower the threshold to boost Recall, accepting a slightly higher default rate in exchange for serving more qualified customers. The Confusion Matrix is the best tool for making that tradeoff visible and deliberate.

With a larger dataset, I would expect Random Forest and SVM to close the gap with — or potentially surpass — Logistic Regression, since their ability to model non-linear feature interactions becomes increasingly valuable as data volume grows. Future work should include cross-validation to ensure these findings are stable and not artifacts of the specific 80/20 split.

---

*Models trained on: `clean_loan_dataset.csv` (100 rows, 9 features after preprocessing)*  
*Evaluation: 80/20 stratified split, random_state=42, positive class = Approved (1)*
