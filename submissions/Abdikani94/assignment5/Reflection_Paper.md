# Reflection Paper

## 1. The Process

Notebook B1 cleaned the raw loan data: fixed currency text, fixed Yes/No typos, filled missing values, dropped duplicates (103 → 100 rows), capped outliers with IQR, encoded Yes/No to 0/1, added two new features (DebtToIncome, IncomePerYearEmployed), scaled the numeric columns, and saved `clean_loan_dataset.csv`.

I used RobustScaler instead of StandardScaler. Income and LoanAmount still had some skew even after IQR capping, and RobustScaler uses median/IQR instead of mean/std, so it stays consistent with the capping step and isn't thrown off by the outliers that remain.

Notebook B2 loaded that file, split 80/20 (stratify=y, random_state=42), then trained three models: Logistic Regression, Random Forest, and Decision Tree (my third pick). I checked each with Accuracy, Precision, Recall, F1, a confusion matrix, and one sanity-check row.

One thing I had to fix along the way: I was originally fitting the scaler on the full dataset before splitting into train/test. That let the test set leak into the scaling statistics. I moved the split before the scaling step, fitting RobustScaler only on the training data and using `.transform()` (not `.fit_transform()`) on the test data.

## 2. Comparison of Models

On the sanity-check row, all three models predicted Approved (1), but the actual label was Rejected (0). All three got that single case wrong — a reminder that even models with decent overall metrics can miss individual applications, especially with a small, imbalanced training set (66 Approved vs. 34 Rejected).

Across the full 20-row test set, the models did not perform the same:

| Model | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| Logistic Regression | 0.700 | 0.733 | 0.846 | 0.786 |
| Random Forest | 0.650 | 0.714 | 0.769 | 0.741 |
| Decision Tree | 0.700 | 0.706 | 0.923 | 0.800 |

Logistic Regression and Decision Tree tied on accuracy, but Random Forest actually scored lowest here. Decision Tree caught the most real approvals (highest recall) but also let in more risky ones (lowest precision). With only 100 rows total, this small a test set (20 rows) can easily be tipped by a couple of individual predictions — not enough data to fully trust these differences.

## 3. Understanding Random Forest

In my own words: Random Forest trains many decision trees, each on a random slice of rows and features. Each tree votes, and the majority wins. One tree overfits easily. Many different trees averaged together cancel out each other's mistakes, so the forest usually generalizes better than a single tree — though on this dataset, with so few rows, that advantage didn't show up in the numbers.

## 4. Third Classifier: Decision Tree

I picked Decision Tree because it's the base building block of Random Forest, so comparing the two shows what the ensemble actually adds. It also fits loan approval well — features like credit score, employment years, and collateral split naturally into yes/no rules, similar to how a loan officer thinks through an application.

From scikit-learn's documentation: at each step, the tree picks the feature and cutoff that best separates the data (default: Gini impurity). Good: fully readable, you can trace the exact path to a decision. Bad: unstable — a small change in the data can produce a very different tree, and it overfits easily without limits like max depth.

Its metrics turned out the strongest here: highest Recall (0.923) and highest F1 (0.800) of the three models, but the lowest Precision (0.706) — it approved more borderline cases than the others.

## 5. Metrics Discussion

Decision Tree had the best Recall and F1. Logistic Regression had the best Precision. Random Forest was lowest across the board on this run.

That doesn't mean Random Forest is a bad algorithm — it means 100 rows isn't enough data for an ensemble to show its usual advantage. Logistic Regression's simplicity worked in its favor here since the patterns in this small dataset are close to linear. Decision Tree's willingness to approve more cases pushed its recall up but cost it some precision.

## 6. My Findings

For this specific dataset, I'd lean toward Logistic Regression or Decision Tree over Random Forest, since Random Forest didn't earn its extra complexity here. If catching every good applicant matters most (avoiding lost business), Decision Tree's high recall makes the strongest case. If avoiding bad loans matters most, Logistic Regression's higher precision is safer.

Main takeaway: 100 rows is too small to fully trust any of these results. The real test would be running this same pipeline on a much larger loan dataset, where Random Forest's averaging effect would have room to actually help.
