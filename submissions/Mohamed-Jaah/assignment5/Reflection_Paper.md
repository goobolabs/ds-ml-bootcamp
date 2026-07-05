# Reflection Paper: Loan Approval Classification Project

## 1. What Did I Implement?

For this project, I reproduced the Lesson 5 preprocessing pipeline on a raw loan approval dataset and then trained three classifiers to predict whether a loan application should be approved.

The pipeline (`Loan_Data_Processing.py`) took the raw dataset through ten steps: loading and inspecting the data, stripping currency symbols from `Income` and `LoanAmount`, normalizing inconsistent category spellings (e.g., "Yes", "yes", "yEs", "Y", "1", "Approved" all mapped to a clean "Yes"), imputing missing numeric values with the column average and missing categorical values with the most frequent category (mode), removing duplicate rows, capping outliers using the interquartile range (IQR) method, label-encoding the Yes/No columns to 1/0, and finally engineering two new features — `DebtToIncome` and `IncomePerYearEmployed` — built only from existing features so there was no leakage from the target variable. The result was a fully clean dataset (`Cleaned_Loan_Dataset.csv`) with zero missing values and no duplicate rows.

On top of this cleaned dataset, I trained three classifiers in `Loan_Approval_Prediction.py`: **Logistic Regression** and **Random Forest** (the two models introduced in class), plus a **Decision Tree Classifier** as my additional, independently researched algorithm. 

Crucially, rather than using a standard scaler, I implemented **`RobustScaler`** to scale the feature data before training. Because loan datasets inherently contain extreme outliers—such as applicants with exceptionally high annual incomes or massive loan requests—`RobustScaler` is the ideal choice. Unlike `StandardScaler`, which uses the mean and variance and gets heavily distorted by outliers, `RobustScaler` scales the data using the median and the Interquartile Range (IQR), ensuring that extreme values do not compromise the learning process of the models.

All three models were trained on an 80/20 stratified train/test split so that the proportion of approved versus rejected loans stayed consistent between the two sets, and then evaluated on Accuracy, Precision, Recall, F1-score, and a confusion matrix.

## 2. Comparison of Models

As a sanity check, I picked a single test-set applicant and compared what each model predicted against the true outcome. In this particular case, the applicant was actually approved (`Approved = 1`). Interestingly, the models diverged on this individual instance: both **Logistic Regression** and **Random Forest** correctly predicted approval (`1`), whereas the single **Decision Tree** incorrectly predicted rejection (`0`). This single-row test perfectly highlights how different algorithms interpret the exact same scaled feature space.

Looking at the results across the whole test set, clear performance differences emerged. **Logistic Regression** achieved the highest overall performance with an Accuracy of 0.70, a Precision of 0.733, a Recall of 0.846, and an F1-score of 0.786. It successfully captured 11 out of 13 true approvals while minimizing false positives.

**Random Forest** and **Decision Tree** both lagged slightly behind with an identical Accuracy of 0.65. However, their underlying behavior was quite different. Random Forest achieved a higher Precision (0.714) but lower Recall (0.769), meaning it was more cautious and conservative about approving loans. The Decision Tree, on the other hand, matched Logistic Regression's high Recall (0.846) but suffered from the lowest Precision (0.688), meaning it was overly generous, catching many true approvals but letting a higher number of bad loans slip through.

## 3. Understanding Random Forest

In my own words, a Random Forest is essentially a "committee" of decision trees rather than a single tree. Instead of building one tree that sees the entire training set and every feature, a Random Forest builds many trees, and each individual tree only sees a random sample of the rows (with replacement) and a random subset of the features when deciding how to split. Because every tree is trained slightly differently, each one makes somewhat different mistakes.

When it's time to classify a new loan applicant, every tree in the forest casts a "vote" for Approved or Rejected, and the forest's final prediction is simply whichever class gets the most votes (majority vote). This averaging-out effect is the key idea: a single decision tree can overfit and be thrown off by noise in the training data, but by combining many different, somewhat-random trees, the mistakes of individual trees tend to cancel out, and the forest as a whole becomes more accurate and more stable than any one tree on its own.

## 4. Other Algorithms (My Third Classifier)

I chose the **Decision Tree Classifier** as my third algorithm. I picked it partly because it is the natural "building block" that Random Forest is made of, which made it a useful point of comparison — it let me see directly what a single tree does on its own versus what happens once many trees are combined into a forest.

From my research (scikit-learn's official documentation, linked in the notebook), a Decision Tree works by repeatedly splitting the data based on the feature and threshold that best separates the classes at each step (for example, "Is CreditScore above 620?"), continuing until it reaches a stopping point or the data in a branch is mostly one class. One clear advantage is interpretability: it is easy to trace exactly why the model reached a particular decision, since you can literally follow the path of questions down the tree. Its main limitation is that a single tree can overfit fairly easily — it can end up memorizing quirks of the training data rather than learning patterns that generalize, especially on a dataset as small as this one.

This limitation was visibly demonstrated in the sanity check, where the Decision Tree was the only model to incorrectly predict `0` for an actually approved applicant. Because a single tree creates rigid, axis-aligned decision boundaries, it is highly sensitive to small variations in the data, leading to a lower Precision (0.688) and a lower overall Accuracy (0.65) compared to the linear baseline of Logistic Regression.

## 5. Metrics Discussion

The metrics across the three models tell a compelling story about the trade-offs in machine learning:

* **Logistic Regression:** Accuracy: 0.70 | Precision: 0.733 | Recall: 0.846 | F1: 0.786
* **Random Forest:** Accuracy: 0.65 | Precision: 0.714 | Recall: 0.769 | F1: 0.741
* **Decision Tree:** Accuracy: 0.65 | Precision: 0.688 | Recall: 0.846 | F1: 0.759

In this specific run, **Logistic Regression** emerged as the strongest model across all metrics. It provided the best balance, achieving the highest Precision while matching the highest Recall. 

However, the comparison between Random Forest and Decision Tree highlights the classic Precision-Recall tug-of-war. Random Forest favored **Precision** (0.714), meaning that when it approved a loan, it was highly reliable, but it missed a few good applicants (Recall of 0.769). The Decision Tree favored **Recall** (0.846), meaning it caught almost all good applicants but at the expense of approving too many risky ones (Precision of 0.688). In a banking context, approving a bad loan (a false positive) is often much more expensive than rejecting a good applicant (a false negative), making Random Forest's conservative stance arguably safer than the Decision Tree's leniency.

## 6. My Findings

If I had to pick one model for deployment based strictly on these current test results, **Logistic Regression** technically performed the best. Its linear boundaries, combined with the robust scaling provided by `RobustScaler`, allowed it to generalize exceptionally well on this small test set, yielding a superior 0.70 accuracy.

However, for a long-term real-world loan approval system, I would still lean toward developing the **Random Forest** further. While it tied with the Decision Tree on accuracy (0.65) in this specific run, ensemble models like Random Forest inherently scale better as data grows. They naturally capture complex, non-linear feature interactions—such as how a high `DebtToIncome` ratio might be acceptable only if the applicant's credit history is flawless—without suffering from the catastrophic overfitting risks of a lone Decision Tree. 

That said, given the tiny size of this dataset (20 rows in the test set), these metrics represent a single snapshot. A minor shuffle in the train/test split could significantly alter the percentages. In a production environment, a financial institution would require a much larger dataset, extensive cross-validation, and a strict business definition regarding the cost of false positives versus false negatives before locking in a final model.