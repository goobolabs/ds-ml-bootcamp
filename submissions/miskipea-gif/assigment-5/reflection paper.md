 Assignment Five, Part C: Reflection Paper

1. What did I implement?

I reproduced the Lesson 5 preprocessing pipeline in `loan_data_processing.ipynb`, cleaning the raw loan dataset by fixing currency formatting, normalizing inconsistent Yes/No spellings, imputing missing values, removing duplicates, capping outliers with the IQR method, label-encoding categorical columns, engineering two new features (`DebtToIncome` and `IncomePerYearEmployed`), and scaling the numeric features with `RobustScaler`. The cleaned output was saved to `clean_loan_dataset.csv`.

In `loan_approval_prediction.ipynb`, I loaded that cleaned dataset, split it 80/20 with stratification, and trained three classifiers: Logistic Regression and Random Forest (reproducing the lesson), plus K-Nearest Neighbors (KNN) as my own additional algorithm. I evaluated all three with Accuracy, Precision, Recall, F1-Score, and a confusion matrix, then ran a sanity check comparing all three models' predictions against one actual test-set label.

 2. Comparison of Models

In the sanity check, all three models agreed with each other but disagreed with the actual label: the true value for the sampled applicant was `Approved = 1`, but Logistic Regression, Random Forest, and KNN all predicted `0`. This shows the models converged on a similar (in this case incorrect) decision boundary for that particular applicant, which is not surprising since all three were trained on the same small dataset and the same features. None of the three models gave a "more realistic" individual prediction on this one row — the more meaningful comparison is across the full test set using the aggregate metrics below, since a single row can easily be an edge case that any model gets wrong.

3. Understanding Random Forest

Random Forest is an ensemble learning method built from many individual Decision Trees. Each tree in the "forest" is trained on a randomly sampled subset of the training data (with replacement, known as bootstrapping) and considers only a random subset of features at each split. Because each tree sees slightly different data and features, the trees end up different from one another rather than all making the same mistakes. When it comes time to classify a new example, every tree in the forest makes its own prediction, and the forest's final output is decided by majority vote across all the trees. This averaging effect is what makes Random Forest more stable and less prone to overfitting than any single Decision Tree on its own.

 4. Other Algorithms (My Third Classifier)

I chose **K-Nearest Neighbors (KNN)**. KNN classifies a new applicant by finding the `k` most similar applicants already in the training data (based on distance across the scaled numeric features) and taking a majority vote of their labels. I chose it because loan approval feels intuitively similar to a "find comparable cases" problem — applicants with similar income, credit score, and debt ratios often receive similar decisions in practice, which is exactly the assumption KNN relies on.

From my research, KNN's main **advantage** is its simplicity: there is no real training phase, since it simply memorizes the data, and it can capture non-linear patterns without needing an explicit model structure like Logistic Regression does. Its main **limitation** is that it depends heavily on feature scaling and on choosing a good value of `k`, and it can become slow and less reliable as the dataset grows, since every prediction requires comparing against many stored points.

On my run, KNN's metrics (Accuracy 0.650, Precision 0.688, Recall 0.846, F1 0.759) landed between Logistic Regression and Random Forest overall — its Recall matched Logistic Regression's (both 0.846), but its Precision was the lowest of the three models, meaning it produced more false positives (predicting "Approved" for applicants who were actually rejected) than the other two.

 5. Metrics Discussion

On this test split:

- **Best Accuracy:** Logistic Regression (0.700)
- **Best Precision:** Logistic Regression (0.733)
- **Best Recall:** Logistic Regression and KNN, tied (0.846)
- **Best F1-Score:** Logistic Regression (0.786)

Logistic Regression came out ahead on every metric in this particular run, which was a bit surprising given that Random Forest is usually the stronger model in theory. This is likely explained by the very small dataset (only 100 rows after cleaning, with just 20 in the test set) — Random Forest and KNN both tend to need more data to show their advantages, and with so few test examples, a handful of different predictions can swing every metric noticeably. Random Forest had the lowest Recall (0.769), meaning it missed the highest proportion of actual approvals, while KNN had the lowest Precision (0.688), meaning it was the most likely to falsely approve an applicant who should have been rejected.

6. My Findings

Based purely on these numbers, I would lean toward **Logistic Regression** for this dataset, since it had the best Accuracy, Precision, and F1-Score, and tied for the best Recall, all while being the simplest and most interpretable of the three models — which matters in a loan approval context where a bank may need to explain to an applicant why they were rejected. That said, I would not treat this as a final conclusion: the dataset here is very small (100 rows), so these results could easily shift with more data, different train/test splits, or hyperparameter tuning (for example, trying a different `k` for KNN or tuning Random Forest's tree depth and number of estimators). In a real deployment, I would want to test on a much larger, more representative dataset and use cross-validation rather than a single 80/20 split before trusting any one model's metrics as a reliable measure of which approach is actually best.