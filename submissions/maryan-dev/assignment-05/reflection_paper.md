# Reflection Paper: Loan Approval Classification

## 1. What Did I Implement?

I reproduced the Lesson 5 preprocessing pipeline using the already-cleaned and
scaled dataset (`clean_loan_dataset.csv`, 100 rows, 8 numeric/binary features
plus the `Approved` target). I separated the target (`y = Approved`) from the
features (`X` = the remaining 8 columns) and split the data into an 80/20
train/test split using `stratify=y` and `random_state=42` so that the class
balance (66 approved vs. 34 denied) was preserved in both sets.

On this split I trained the two models from class — `LogisticRegression`
(`max_iter=1000`, `random_state=42`) and `RandomForestClassifier`
(`n_estimators=100`, `random_state=42`) — and then trained a third model I
researched myself, `KNeighborsClassifier` (`n_neighbors=5`), all three fit on
the identical `X_train`/`y_train`. I then wrote a single evaluation helper
that computes Accuracy, Precision, Recall, and F1-Score (treating
`Approved = 1` as the positive class) and a confusion matrix for each model,
and ran a sanity check comparing all three models' predictions against the
actual label for individual test rows.

## 2. Comparison of Models

In the single-row sanity check (`X_test.iloc[[0]]`), the actual label was
`Approved = 1`, but **all three models predicted 0** — none of them got that
particular applicant right. Looking at the full test-set comparison table,
Logistic Regression and Random Forest agreed with each other on almost every
row, with only a couple of exceptions (e.g., one row where Random Forest
predicted 0 while Logistic Regression and KNN both predicted 1). KNN
diverged slightly more often, occasionally predicting 1 where the other two
predicted 0.

Given the metrics (below), Logistic Regression gave the most realistic
results on this dataset: it had the highest accuracy and the best balance
between precision and recall. Random Forest, despite being a more complex
model, actually performed slightly worse here — likely because the training
set is very small (only 80 rows), and Random Forest's flexibility makes it
prone to overfitting on small datasets.

## 3. Understanding Random Forest

In my own words, a Random Forest is an ensemble method that trains many
individual decision trees and combines their outputs to make a final
prediction. Each tree is trained on a random subset of the training rows
(with replacement, a technique called bagging) and considers only a random
subset of features at each split. This randomness means the individual
trees end up somewhat different from one another and make different
mistakes. For classification, each tree "votes" for a class, and the forest
outputs whichever class gets the majority of the votes. Because the errors
of individual trees tend to be uncorrelated, averaging over many trees
usually reduces variance and produces a more stable prediction than any
single decision tree would give on its own — though, as seen above, this
benefit is less pronounced when there isn't much data to build diverse trees
from in the first place.

## 4. Other Algorithms (My Third Classifier)

I chose **K-Nearest Neighbors (KNN)**. KNN classifies a new applicant by
looking at the "k" most similar applicants in the training data (by
distance in feature space) and taking a majority vote of their labels. It
fits this problem well because the dataset was already cleaned and scaled
in Part B1 — KNN is a distance-based algorithm, so having standardized
features is important for it to work correctly, and that preprocessing was
already done for us.

From my research (scikit-learn's documentation on `KNeighborsClassifier`),
I learned that KNN is a "lazy learner": it does not build an internal model
during training, it just stores the training data and does all its work at
prediction time by computing distances to every stored point. One advantage
is that it is simple and intuitive to explain to a non-technical audience
(e.g., a loan officer can be told "this applicant resembles 5 previous
applicants, most of whom were approved"). One limitation is that it can
become slow and less accurate as the dataset grows large or has many
features, since it needs to search through all training points for every
single prediction (the "curse of dimensionality").

On this dataset, KNN's metrics (Accuracy 0.650, Precision 0.688, Recall
0.846, F1 0.759) landed between the other two models: its recall matched
Logistic Regression's (both correctly identified the most actual approvals),
but its precision was the lowest of the three, meaning it also mislabeled
more denied applicants as approved.

## 5. Metrics Discussion

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Logistic Regression | **0.700** | **0.733** | 0.846 | **0.786** |
| Random Forest | 0.650 | 0.714 | 0.769 | 0.741 |
| K-Nearest Neighbors | 0.650 | 0.688 | **0.846** | 0.759 |

Logistic Regression had the best Accuracy, Precision, and F1-Score.
Logistic Regression and KNN tied for the best Recall. This tells me that on
this particular (small, already well-scaled) dataset, a simple linear model
was able to separate approved from denied applicants about as well as, or
better than, the more complex models. Random Forest's weaker showing
suggests it may be overfitting patterns in the small training set that
don't generalize to the test set. KNN's strong recall but weak precision
suggests it is a bit too willing to predict "approved," catching most true
approvals but also incorrectly approving more applicants who should have
been denied — a meaningful risk in a loan-approval context.

## 6. My Findings

For this specific dataset, I would use **Logistic Regression** for loan
approval prediction. It produced the best overall balance of accuracy,
precision, and F1-score, meaning it not only correctly identifies most
approvable applicants but also does the best job of avoiding false
approvals — an important property when the cost of wrongly approving a
risky loan is high. It's also the simplest and most interpretable of the
three models, which matters in a regulated domain like lending, where
being able to explain *why* an application was denied is often a
requirement, not just a nice-to-have.

That said, I would treat this conclusion as provisional rather than final.
With only 100 total rows and a 20-row test set, all of these metrics have a
lot of variance — a single misclassified applicant changes the accuracy by
5 percentage points. If more data became available, I would want to
re-evaluate all three models (and Random Forest in particular, since
ensemble methods typically need more data to show their advantage) before
committing to one model for production use.
