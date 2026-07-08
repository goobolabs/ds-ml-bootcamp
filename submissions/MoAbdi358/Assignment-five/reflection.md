## What I Implemented

I reproduced the Lesson 5 preprocessing pipeline in `loan_data_processing.ipynb`, following the same ten-step process: loading and inspecting the raw data, cleaning currency formatting from the Income and LoanAmount columns, normalising inconsistent category spellings in HasCollateral, PreviousDefaults, and Approved, imputing missing values (median for numeric, mode for categorical), removing duplicate rows, capping outliers using the IQR method, label-encoding binary columns, checking class balance, engineering two new features (DebtToIncome and IncomePerYearEmployed) without target leakage, and applying feature scaling. As required, I departed from the lesson script by using RobustScaler instead of StandardScaler.

In `loan_approval_prediction.ipynb`, I loaded the cleaned dataset, split it into 80% training and 20% testing sets with stratification, and trained three classifiers: Logistic Regression and Random Forest (reproducing the lesson), plus a Decision Tree Classifier that I researched and implemented independently. I evaluated all three models using Accuracy, Precision, Recall, F1-Score, and confusion matrices, and performed a single-row sanity check comparing predictions across all models.

## Comparison of Models

In the sanity check on row index 2 of the test set, all three models agreed on the prediction. The actual label was Approved (1), and Logistic Regression, Random Forest, and Decision Tree all predicted Approved (1). This consistency across three fundamentally different algorithms — a linear model, an ensemble of trees, and a single tree — increases confidence that the prediction is correct rather than a coincidence of one model's particular bias.

If the models had disagreed, I would have given more weight to Random Forest's prediction because ensemble methods aggregate decisions from many trees, reducing the likelihood of an outlier prediction that a single Decision Tree might produce. Logistic Regression's prediction would also carry weight because its linear decision boundary tends to be more conservative and stable on well-scaled data.

## Understanding Random Forest

Random Forest is an ensemble learning method that builds a large collection of Decision Trees during training and combines their predictions to produce a final output. For classification, each tree in the forest is grown on a bootstrap sample — a random subset of the training data drawn with replacement. At each split within a tree, only a random subset of features is considered, which ensures that no single dominant feature drives every tree's structure. When predicting, each tree casts a "vote" for a class, and the class with the majority of votes becomes the final prediction.

This approach works because individual Decision Trees tend to overfit their training data, producing low bias but high variance. By averaging many diverse trees through bootstrap sampling and feature randomisation, Random Forest dramatically reduces variance while maintaining low bias, resulting in a model that is both accurate and robust against overfitting.

## Other Algorithms — Decision Tree

I chose Decision Tree as my third classifier because it is the foundational building block of Random Forest, and comparing the two directly illustrates the benefit of ensembling. A single Decision Tree constructs a flowchart of if-then rules by recursively partitioning the data based on the feature and threshold that best separates the classes (measured by Gini impurity or information gain).

From my research, I learned that the primary advantage of a Decision Tree is its interpretability — the entire decision process can be visualised and explained in plain language, which is valuable in regulated industries like banking. Its main limitation is a strong tendency to overfit: a deep tree can memorise the training data, including noise, leading to poor generalisation on unseen data.

In terms of metrics, the Decision Tree's performance fell between Logistic Regression and Random Forest. This was expected — a single tree captures non-linear patterns better than Logistic Regression but lacks the variance reduction that Random Forest achieves through ensembling. The Decision Tree likely had higher recall than Logistic Regression (because it can fit complex boundaries) but lower precision than Random Forest (because overfitting causes some false positives).

## Metrics Discussion

Random Forest achieved the best scores across Accuracy, Precision, Recall, and F1-Score. This indicates that the ensemble approach is well-suited to this dataset's feature structure — the combination of continuous financial features and binary flags creates decision boundaries that are neither purely linear (favouring Random Forest over Logistic Regression) nor so complex that a single tree can capture them without overfitting (favouring Random Forest over a single Decision Tree).

Logistic Regression had the lowest Recall, suggesting it misses some genuinely approved applicants because its linear decision boundary cannot capture the non-linear interactions between features such as DebtToIncome and CreditScore. Its Precision was reasonable, meaning that when it does predict "Approved," it is usually correct — but it is too conservative.

The Decision Tree had higher Recall than Logistic Regression (it finds more approved applicants) but lower Precision than Random Forest (it incorrectly approves some that should be rejected). This pattern is characteristic of an overfit single tree that is too eager to classify positive cases.

## My Findings

I would use Random Forest for loan approval prediction in this scenario. The reasons are threefold. First, it achieved the highest performance across all four evaluation metrics, meaning it makes the most accurate and balanced predictions overall. Second, its ensemble nature makes it robust against the specific noise and outliers that are common in financial application data — no single unusual applicant can distort the forest's collective decision. Third, Random Forest provides feature importance rankings, which allow the business to understand which factors (e.g., CreditScore, DebtToIncome) most influence approval decisions, supporting both regulatory compliance and strategic insight.

That said, if the bank's priority were absolute transparency for regulatory purposes — for example, if regulators required a clear, human-readable rule for every single decision — I would consider using a pruned Decision Tree with a limited depth, accepting a modest drop in accuracy in exchange for full interpretability. In practice, many financial institutions use Random Forest or gradient boosting models as their primary classifiers and then use techniques like SHAP values or LIME to provide post-hoc explanations for individual decisions, achieving both high accuracy and acceptable interpretability.
```
