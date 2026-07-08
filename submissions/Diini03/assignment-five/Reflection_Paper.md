# Reflection Paper — Loan Approval Classification

---

## 1. What I Implemented

I reproduced the Lesson 5 preprocessing pipeline on the raw loan dataset — cleaning currency formatting, fixing category typos, imputing missing values, removing duplicates, capping outliers, label encoding, and feature engineering. For scaling I chose RobustScaler instead of StandardScaler because it handles skewed distributions better by using median and IQR instead of mean and standard deviation.

For the classification part I trained three models on the cleaned dataset: Logistic Regression and Random Forest from the lesson, plus KNN as the additional classifier I researched myself.

---

## 2. Comparison of Models

In the sanity check all three models predicted the same label for the selected row, which suggests they agree on clear-cut cases. The differences showed up more in the metrics — Random Forest had the strongest overall numbers, Logistic Regression was close, and KNN was slightly behind on recall.

Random Forest gave the most consistent predictions across both approved and rejected applicants. Logistic Regression was reliable but occasionally missed borderline cases where the relationship between features and approval wasn't linear.

---

## 3. Understanding Random Forest for Classification

Random Forest builds many decision trees during training, each on a random sample of the data and a random subset of features. For classification, every tree casts a vote and the majority vote becomes the final prediction.

The reason it works well is that individual trees overfit easily, but when you combine hundreds of imperfect trees their errors don't all go in the same direction — they cancel out. The result is a model that generalizes much better than any single tree.

---

## 4. My Third Classifier — KNN

I chose K-Nearest Neighbors because it works differently from both Logistic Regression and Random Forest. Instead of learning a model during training, KNN just stores the training data. When a new application comes in, it finds the K closest examples in the training set and predicts the majority label.

**Advantage:** Simple, no assumptions about the data distribution, works well on small clean datasets.

**Limitation:** Slow on large datasets because it has to compute distance to every training point for each prediction. Also sensitive to irrelevant features and unscaled data — which is why RobustScaler mattered here.

KNN performed reasonably well but had lower recall than Random Forest, meaning it missed more approved applicants than the other two models.

---

## 5. Metrics Discussion

Random Forest had the best Accuracy, Precision, Recall, and F1-Score across all three models. Logistic Regression was competitive on precision but weaker on recall. KNN sat in the middle overall but struggled the most with recall on the minority class.

High recall matters more in loan approval when the cost of rejecting a qualified applicant is the bigger concern. From that angle Random Forest is the clear winner — it caught more true approvals while keeping false positives reasonable.

---

## 6. My Findings

Random Forest is the model I would use for loan approval prediction. The metrics are strongest, it handles the mix of numeric and binary features well, and it doesn't assume a linear boundary between approved and rejected applicants — which is more realistic for real loan data where multiple factors interact in complex ways.

KNN was a useful addition to compare against, but it would not be my production choice. On a small dataset like this it performs acceptably, but it would not scale well to thousands of applications and its recall was the weakest of the three.
