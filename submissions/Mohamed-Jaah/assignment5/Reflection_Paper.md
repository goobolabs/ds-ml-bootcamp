# Reflection Paper: Loan Approval Classification Project

## 1. What Did I Implement?

For this project, I reproduced the Lesson 5 preprocessing pipeline on a raw loan approval dataset and then trained three classifiers to predict whether a loan application should be approved.

The pipeline (`Loan_Data_Processing.py`) took the raw dataset through ten steps: loading and inspecting the data, stripping currency symbols from `Income` and `LoanAmount`, normalizing inconsistent category spellings (e.g., "Yes", "yes", "yEs", "Y", "1", "Approved" all mapped to a clean "Yes"), imputing missing numeric values with the column average and missing categorical values with the most frequent category (mode), removing duplicate rows, capping outliers using the interquartile range (IQR) method, label-encoding the Yes/No columns to 1/0, and finally engineering two new features — `DebtToIncome` and `IncomePerYearEmployed` — built only from existing features so there was no leakage from the target variable. The result was a fully clean dataset (`Cleaned_Loan_Dataset.csv`) with zero missing values and no duplicate rows.

On top of this cleaned dataset, I trained three classifiers in `Loan_Approval_Prediction.py`: **Logistic Regression** and **Random Forest** (the two models introduced in class), plus a **Decision Tree Classifier** as my additional, independently researched algorithm. All three models were trained on an 80/20 stratified train/test split so that the proportion of approved versus rejected loans stayed consistent between the two sets, and then evaluated on Accuracy, Precision, Recall, F1-score, and a confusion matrix.

## 2. Comparison of Models

As a sanity check, I picked a single test-set applicant and compared what each model predicted against the true outcome. In this particular case, the applicant was actually approved (`Approved = 1`), and all three models — Logistic Regression, Random Forest, and Decision Tree — correctly predicted approval. So, on this one example, the three models agreed with each other and with reality.

Looking at the results across the whole test set rather than a single row, though, small differences appear. Logistic Regression and Random Forest produced identical scores in this run (Accuracy 0.65, Precision 0.714, Recall 0.769, F1 0.741), while the Decision Tree leaned slightly more toward approving applicants — it caught more of the true approvals (Recall 0.846) but at the cost of a few more false approvals (Precision 0.688). I would consider Logistic Regression and Random Forest to have given the more "realistic" or trustworthy results here, mainly because a single Decision Tree is more prone to overfitting the specific quirks of a small training set, while Logistic Regression's simplicity and Random Forest's use of many averaged trees make their predictions less sensitive to any one unusual row in the data.

## 3. Understanding Random Forest

In my own words, a Random Forest is essentially a "committee" of decision trees rather than a single tree. Instead of building one tree that sees the entire training set and every feature, a Random Forest builds many trees, and each individual tree only sees a random sample of the rows (with replacement) and a random subset of the features when deciding how to split. Because every tree is trained slightly differently, each one makes somewhat different mistakes.

When it's time to classify a new loan applicant, every tree in the forest casts a "vote" for Approved or Rejected, and the forest's final prediction is simply whichever class gets the most votes (majority vote). This averaging-out effect is the key idea: a single decision tree can overfit and be thrown off by noise in the training data, but by combining many different, somewhat-random trees, the mistakes of individual trees tend to cancel out, and the forest as a whole becomes more accurate and more stable than any one tree on its own.

## 4. Other Algorithms (My Third Classifier)

I chose the **Decision Tree Classifier** as my third algorithm. I picked it partly because it is the natural "building block" that Random Forest is made of, which made it a useful point of comparison — it let me see directly what a single tree does on its own versus what happens once many trees are combined into a forest.

From my research (scikit-learn's official documentation, linked in the notebook), a Decision Tree works by repeatedly splitting the data based on the feature and threshold that best separates the classes at each step (for example, "Is CreditScore above 620?"), continuing until it reaches a stopping point or the data in a branch is mostly one class. One clear advantage is interpretability: it is easy to trace exactly why the model reached a particular decision, since you can literally follow the path of questions down the tree. Its main limitation is that a single tree can overfit fairly easily — it can end up memorizing quirks of the training data rather than learning patterns that generalize, especially on a dataset as small as this one (100 rows).

In terms of metrics, the Decision Tree's Accuracy (0.65) matched Logistic Regression and Random Forest exactly, but its Precision was slightly lower (0.688 vs. 0.714) and its Recall was noticeably higher (0.846 vs. 0.769), giving it the highest F1-score of the three (0.759 vs. 0.741). In other words, the Decision Tree was a bit more willing to approve borderline applicants, catching more of the true approvals but also letting through a few more applicants who should have been rejected.

## 5. Metrics Discussion

Across the three models, Accuracy was tied at 0.65 for all three, so it did not help distinguish between them. Logistic Regression and Random Forest tied for the best Precision (0.714), while the Decision Tree had the best Recall (0.846) and, as a result, the best F1-score (0.759).

This tells an important story: no single model was best on every metric. Logistic Regression and Random Forest were more "cautious" — when they predicted approval, they were right slightly more often (higher precision), but they also missed a few applicants who should have been approved (lower recall). The Decision Tree was more "generous" — it caught more of the true approvals but let a few more risky applicants slip through as false approvals. Because Precision and Recall pull in opposite directions here, which model looks "best" really depends on which mistake is more costly: approving a bad loan (a false positive, where Precision matters most) or rejecting a good applicant (a false negative, where Recall matters most).

## 6. My Findings

If I had to pick one model for real loan approval prediction, I would lean toward **Random Forest**. Its metrics were identical to Logistic Regression's in this run, but Random Forest tends to be more robust as a dataset grows or shifts over time, since it is built from many trees rather than a single linear equation or a single tree that can be unstable on small samples. It also naturally captures non-linear relationships between features (like the engineered `DebtToIncome` ratio) that Logistic Regression cannot represent as directly, without suffering from the overfitting risk of a lone Decision Tree.

That said, with only 100 rows in this dataset and just 20 rows in the test set, none of these results should be treated as final. A handful of different rows landing in the test set could easily shift Accuracy, Precision, or Recall by several percentage points, and the fact that Accuracy was identical across all three models is itself a sign that this test set is too small to reliably separate them. In a real deployment, a bank would likely want a much larger and more diverse dataset, cross-validation instead of a single train/test split, and a clear business decision about whether approving bad loans (favoring Precision) or rejecting good applicants (favoring Recall) is the more costly mistake, before committing to one model over another.
