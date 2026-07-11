# Assignment Five — Part C: Reflection Paper

**Author:** Ali Omar Abdi     
**Course:** DS-ML Bootcamp.  
**Due:** Sunday, July 5, 2026 — 12:00 PM (Africa/Mogadishu / EAT)
---

## Table of Contents

1. [What Did I Implement?](#1-what-did-i-implement)
2. [Comparison of Models](#2-comparison-of-models)
3. [Understanding Random Forest](#3-understanding-random-forest)
4. [Other Algorithms (My Third Classifier)](#4-other-algorithms-my-third-classifier)
5. [Metrics Discussion](#5-metrics-discussion)
6. [My Findings](#6-my-findings)
7. [References](#references)

---

## 1. What Did I Implement?

For Part B1, I reproduced the Lesson 5 preprocessing pipeline in `loan_data_processing.ipynb`. This involved cleaning currency-formatted columns, normalizing inconsistent Yes/No/typo values, imputing missing values with median/mode, removing duplicates, capping outliers with IQR-based clipping, label-encoding the target and binary features, engineering two new features (`DebtToIncome` and `IncomePerYearEmployed`), and scaling the numeric columns. The one deliberate change from the class example was swapping `StandardScaler` for `RobustScaler`, since it uses the median and IQR rather than the mean and standard deviation, which made it a better fit for the skewed, outlier-prone `Income` and `LoanAmount` columns.

For Part B2, I loaded the cleaned dataset in `loan_approval_prediction.ipynb`, split it 80/20 with `stratify=y` and `random_state=42`, and trained three classifiers on the same training data: Logistic Regression (`max_iter=1000`), Random Forest (`n_estimators=100`), and K-Nearest Neighbors (`n_neighbors=5`) as my researched third algorithm. I evaluated all three with a shared helper function that prints Accuracy, Precision, Recall, and F1-Score, plus a labeled confusion matrix for each model, and finished with a single-row sanity check comparing all three models' predictions against the true label.

## 2. Comparison of Models

On the sanity-check row, all three models agreed with each other and with the actual label. Looking across the full 20-row test set, however, the picture is more interesting: Logistic Regression and Random Forest produced the exact same prediction on every single test row, while KNN differed on one row — a case where the true label was Rejected but KNN alone predicted Approved.

At first this looked like a bug, so I double-checked it by comparing predictions row by row instead of trusting the summary metrics alone. It turned out to be a genuine result rather than an error: Logistic Regression and Random Forest gave different underlying predicted probabilities for several rows, but those probabilities happened to land on the same side of the 0.5 decision threshold every time. With only 20 test rows, there simply weren't enough close-to-50/50 borderline cases to separate the two models' final class predictions.

| | Logistic Regression | Random Forest | KNN (k=5) |
|---|---|---|---|
| Sanity-check row | Matched actual | Matched actual | Matched actual |
| Agreement with actual (20 rows) | 14/20 | 14/20 | 13/20 |
| Disagreed with the other two models | No | No | Yes (1 row) |

Between the three, Random Forest gave the more realistic-feeling results, since it is an ensemble average of many decision trees and is less likely to be swayed by one unusual training pattern the way a single KNN neighborhood vote can be. That said, since Random Forest and Logistic Regression tied exactly on this test set, I cannot claim Random Forest was empirically better here — only that it is the more robust choice in general, and KNN's one miss (falsely approving an applicant who should have been rejected) is the more costly type of error in a loan-approval context.

## 3. Understanding Random Forest

Random Forest is an ensemble learning method built from many individual decision trees. Instead of training one tree on the full dataset, it trains a large number of trees, each on a random bootstrap sample of the training rows and a random subset of the features at each split. This randomness means each tree ends up slightly different and makes slightly different mistakes. For classification, every tree in the forest "votes" for a predicted class, and the forest's final prediction is simply the majority vote across all trees.

The benefit of this approach is that it reduces overfitting compared to a single decision tree: one tree can memorize noise in the training data, but averaging many differently-biased trees smooths that out. It also tends to handle non-linear relationships and feature interactions well without needing manual feature engineering, which fits loan data where features like income, credit score, and debt-to-income ratio likely interact in non-obvious ways.

## 4. Other Algorithms (My Third Classifier)

I chose K-Nearest Neighbors (KNN) as my third classifier, using `n_neighbors=5`. I chose it because it is conceptually simple and intuitive for a loan approval use case: it predicts an applicant's outcome by finding the five most similar past applicants by feature distance and taking a majority vote among them. That mirrors how a human loan officer might informally reason — "this applicant looks like these other five, and most of them were approved or rejected." I researched the algorithm using the scikit-learn documentation for `sklearn.neighbors.KNeighborsClassifier`.

**What I learned:** KNN is a "lazy learner" — it does not build an explicit model during training; it simply stores the training data and does all of its work at prediction time by computing distances. Because of this, it depends heavily on feature scaling, which is why the Part B1 `RobustScaler` step mattered specifically for this model, unlike for the tree-based Random Forest, which is scale-invariant.

**Advantage:** It is simple to understand and requires no assumptions about the underlying data distribution, unlike Logistic Regression, which assumes a roughly linear relationship between features and the log-odds of approval.

**Limitation:** It can be sensitive to irrelevant or noisy features and to the choice of `k`, and it scales poorly to large datasets since every prediction requires comparing against the entire training set.

**Metrics comparison:** KNN scored slightly lower than both Logistic Regression and Random Forest on this test set — 0.650 accuracy versus 0.700 for the other two — driven by the one false-approval case described above.

## 5. Metrics Discussion

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Logistic Regression | 0.700 | 0.733 | 0.846 | 0.786 |
| Random Forest | 0.700 | 0.733 | 0.846 | 0.786 |
| KNN (k=5) | 0.650 | 0.688 | 0.846 | 0.759 |

Logistic Regression and Random Forest tied for the best Accuracy, Precision, and F1-Score, while all three models had identical Recall. KNN trailed slightly on every metric except Recall.

The tied Recall (0.846) across all three models shows they are all similarly good at catching true approvals — they miss the same proportion of applicants who should have been approved. The gap instead shows up in Precision: KNN's lower precision (0.688 vs. 0.733) means it is more likely to approve an applicant who should have been rejected, which is the more costly error type for a lender. This lines up with the one row where KNN diverged from the other two models. Overall, the metrics suggest Logistic Regression and Random Forest behave very similarly on this dataset, while a simple distance-based method like KNN is somewhat more exposed to individual "unusual neighbor" cases.

## 6. My Findings

For loan approval prediction specifically, I would use Random Forest. It matched Logistic Regression's performance on this test set, but ensembling across many trees makes it more robust to noise and unusual applicant profiles than a single model like KNN. Unlike Logistic Regression, it also does not assume a linear relationship between features and approval odds, which matters here since features like debt-to-income ratio and credit score likely interact in non-linear ways. It additionally does not require feature scaling to work correctly, which makes the overall pipeline less fragile.

That said, this small 20-row test set is not large enough to strongly separate Logistic Regression from Random Forest, since they produced identical predictions on every row. In a real deployment rather than a class assignment, I would want a much larger test set before choosing one model over the other with confidence, since a handful of close-call predictions can make two genuinely different algorithms look statistically identical purely by chance.

---

## References

Pedregosa, F., et al. (2011). Scikit-learn: Machine Learning in Python. *Journal of Machine Learning Research*, 12, 2825-2830. https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html

Breiman, L. (2001). Random Forests. *Machine Learning*, 45(1), 5-32. https://doi.org/10.1023/A:1010933404324

---

*Submitted for DS-ML Bootcamp — Assignment Five*     
**Due:** Sunday, July 5, 2026*