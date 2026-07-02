# Assignment Five: Classification — Theory and Practice

**Due:** Sunday, July 5, 2026 — 12:00 PM (Africa/Mogadishu / EAT)

**Goal:** Demonstrate understanding of classification concepts in Machine Learning. Reproduce the **Lesson 5** preprocessing and modeling pipeline in Jupyter notebooks, then research and implement **one additional classifier** — for a total of three models (Logistic Regression, Random Forest, and your chosen algorithm) on the loan approval dataset.

---

## Part A — Theory

Write your answers in English using a clear academic style (headings, paragraphs, and references). Length: 2–3 pages. Use your own words — no copy-paste. You may use AI for clarification, but must understand and verify everything you write.

1. **Introduction to Classification**

   - What is classification in Machine Learning?
   - How is it different from regression?
   - Give one real-life example of classification and one of regression.

2. **Classification Algorithms**

   - Describe and compare the following:
     - Logistic Regression
     - Decision Trees
     - Random Forest
   - For each type, explain: how it works (basic idea), one real-world use case, and its main advantages and limitations.

3. **Classification Metrics**

   - Define and explain what each metric measures:
     - Accuracy
     - Precision
     - Recall
     - F1-Score
     - Confusion Matrix
   - Include a comparison table showing their differences (what each measures, sensitivity to class imbalance).

4. **Class Imbalance**

   - Why can Accuracy be misleading when classes are imbalanced?
   - When would you prioritize Precision over Recall, and when would you prioritize Recall over Precision? Use loan approval as an example.

5. **Real-World Case Study**

   - Research a real-world project or study that used classification in any field such as business, healthcare, finance, or education.
   - Summarize: the goal, the data used, the type of classifier applied, and the key results or insights.

---

## Part B — Practical

Part B mirrors the **Lesson 5** coding session. **B1** reproduces the preprocessing pipeline; **B2** reproduces the Logistic Regression and Random Forest models, then adds a third classifier you research yourself.

### B1 — Loan Data Processing

**Dataset:** `dataset/raw_loan_dataset.csv`

Create a Jupyter Notebook named `loan_data_processing.ipynb` and implement the following steps. Include a brief print checkpoint after each major step.

> Follow the **Preprocessing for Classification** section in **Lesson 5** and [`code/loan-data-processing.py`](../code/loan-data-processing.py). Implement the same pipeline in your own notebook — typed by you, with output cells visible. **Exception:** in step 10, research and choose your own scaler instead of copying `StandardScaler` from the class script.

1. **Load & Inspect**

   - Load the CSV with pandas and show head, info, and missing counts.
   - Note the key issues you find — look for `$` signs in numeric columns, mixed Yes/No spellings, and rows where `Approved` is not exactly "Yes" or "No".

2. **Clean Currency Formatting**

   - Remove currency symbols and commas from `Income` and `LoanAmount`; ensure both columns are numeric.

3. **Fix Category Errors before Imputation**

   - Normalize typos in `HasCollateral`, `PreviousDefaults`, and `Approved`.
   - Map variants (e.g., yes/no, y/n, approved/rejected) to consistent Yes/No values.
   - Do this **before** filling missing values. Check `value_counts()` after each column to confirm.

4. **Impute Missing Values**

   - Median for numeric columns; mode for categorical columns.
   - Confirm post-imputation missing counts with `isnull().sum()` — there should be zero missing when done.

5. **Remove Duplicates**

   - Drop duplicate rows and report the row count before and after.

6. **Outliers (IQR capping)**

   - Compute IQR bounds (`k=1.5`) and clip `Income`, `CreditScore`, `LoanAmount`, and `EmploymentYears`.
   - Cap extreme values with `.clip()` — do not delete rows.

7. **Label Encoding**

   - Map Yes/No columns to `1` and `0`: `Approved`, `HasCollateral`, and `PreviousDefaults`.
   - For `Approved`, print class distribution with `value_counts()`.

8. **Class Balance Check**

   - Print approved vs rejected counts and proportions (`value_counts(normalize=True)`).
   - Note whether the dataset is balanced enough for Accuracy to be a reliable metric.

9. **Feature Engineering (no leakage)**

    - Add `DebtToIncome` and `IncomePerYearEmployed`.
    - Build these from **features only** — never use `Approved` in the formula.

10. **Feature Scaling (Research & Choose)**

    - The class script uses `StandardScaler`. For this assignment, **research and choose a different scaler** from `sklearn.preprocessing` (e.g., `MinMaxScaler`, `RobustScaler`, `MaxAbsScaler`).
    - Apply your chosen scaler to **numeric features only**.
    - Do **not** scale label-encoded columns (`Approved`, `HasCollateral`, `PreviousDefaults`).
    - In a short markdown cell, explain:

      - Which scaler you chose and why it fits this loan dataset.
      - One source you used for your research (documentation, tutorial, or article).

11. **Final Checks & Save**

    - Show final info, missing counts, and head — confirm no missing values remain and `Approved` is still 0/1.
    - Save the result to `clean_loan_dataset.csv` (Part B2 will load this file).

---

### B2 — Loan Approval Classification

**Dataset:** Use the cleaned loan dataset you produced in Part B1 (`clean_loan_dataset.csv`).

Create a Jupyter Notebook named `loan_approval_prediction.ipynb` and implement the following steps:

1. **Load Dataset**

   - Load `clean_loan_dataset.csv`.

2. **Prepare Features & Target**

   - Target (`y`) = `Approved`
   - Features (`X`) = all columns except `Approved`

3. **Split Data**

   - Split into 80% training and 20% testing.
   - Use `stratify=y` and `random_state=42`.

4. **Train Models (Reproduce Lesson)**

   - Train a `LogisticRegression` model with `max_iter=1000` and `random_state=42`.
   - Train a `RandomForestClassifier` with `n_estimators=100` and `random_state=42`.

   These two models match [`code/loan-approval-classifier.py`](../code/loan-approval-classifier.py) from the **Lesson 5** coding session.

5. **Research & Train a Third Classifier**

   - The lesson covers preprocessing plus **Logistic Regression** and **Random Forest**. Your assignment adds **one additional classification algorithm** you research and implement yourself.
   - Choose a classifier you did **not** use in the lesson script (e.g., Decision Tree, KNN, Naive Bayes, SVM — or another suitable algorithm from your Part A research).
   - In a short markdown cell in the notebook, explain:

     - Which algorithm you chose and why it fits loan approval prediction.
     - One source you used for your research (article, documentation, or tutorial).

   - Train your third model on the same `X_train` / `y_train` split using sensible default hyperparameters and `random_state=42` where applicable.

6. **Evaluate Performance**

   - Write a helper function to print Accuracy, Precision, Recall, and F1-Score (positive class = Approved = 1).
   - Call it for **all three models**.
   - Print a confusion matrix for each model.
   - Expected output format (exact numbers will vary):

     ```
     Logistic Regression Performance:
       Accuracy : 0.850
       Precision: 0.820  (positive = Approved=1)
       Recall   : 0.880  (positive = Approved=1)
       F1-Score : 0.849  (positive = Approved=1)

     Random Forest Performance:
       Accuracy : 0.900
       Precision: 0.870  (positive = Approved=1)
       Recall   : 0.910  (positive = Approved=1)
       F1-Score : 0.889  (positive = Approved=1)

     [Your Third Algorithm] Performance:
       Accuracy : 0.870
       Precision: 0.840  (positive = Approved=1)
       Recall   : 0.890  (positive = Approved=1)
       F1-Score : 0.864  (positive = Approved=1)
     ```

7. **Sanity Check**

   - Pick one row from the test set (`X_test.iloc[[i]]`) and compare the actual label with predictions from **all three models**.

> **Lesson 5** walks through preprocessing and two classifiers (Logistic Regression and Random Forest). Your assignment reproduces both pipelines in notebooks and adds **one third classifier** you research yourself. Submit your own notebooks with all output cells visible.

---

## Part C — Reflection Paper

Write a short paper (1–2 pages, Markdown or PDF) answering the following:

1. **What did you implement?**

   - Briefly describe how you reproduced the **Lesson 5** preprocessing pipeline and trained **three classifiers** — Logistic Regression and Random Forest from class, plus your additional algorithm — to predict loan approval.

2. **Comparison of Models**

   - How did predictions differ in your sanity check across all three models?
   - Which model gave more realistic results? Why?

3. **Understanding Random Forest**

   - In your own words: what is Random Forest and how does it work for classification (ensemble of decision trees, majority vote)?

4. **Other Algorithms (Your Third Classifier)**

   - Which additional algorithm did you choose, and why?
   - Summarize what you learned from your research (how it works, one advantage, one limitation).
   - How did its metrics compare to Logistic Regression and Random Forest?

5. **Metrics Discussion**

   - Which model had the best Accuracy, Precision, Recall, and F1-Score?
   - What does that tell you about the strengths and weaknesses of each model?

6. **Your Findings**

   - In 1–2 paragraphs, explain which model you would use for loan approval prediction and why.

---

## Deliverables

Submit these four files:

- `paper.md` or `paper.pdf` — Part A theory answers.
- `loan_data_processing.ipynb` — Part B1 notebook with all code and output cells visible.
- `loan_approval_prediction.ipynb` — Part B2 notebook with all code and output cells visible.
- `reflection_paper.md` or `reflection_paper.pdf` — Part C reflection.

Also produce `clean_loan_dataset.csv` (used by Part B2; same pattern as Assignment Three's cleaned CSV).

---
