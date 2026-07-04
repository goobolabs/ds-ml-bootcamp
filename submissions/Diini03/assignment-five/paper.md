# Assignment Five — Classification: Theory and Practice

---

## 1. Introduction to Classification

Classification is a type of supervised learning where the model predicts which category an input belongs to. You give it labeled examples and it learns the boundary between classes — then uses that to label new, unseen data.

The difference from regression is simple: regression predicts a number, classification predicts a category. Both are supervised — both need labeled training data.

**Classification example:** Predicting whether a loan application gets approved or rejected. The output is one of two categories.

**Regression example:** Predicting how much money a player will be worth in the transfer market next season. The output is a number.

---

## 2. Classification Algorithms

### Logistic Regression

Despite the name, Logistic Regression is a classification algorithm. It calculates the probability that an input belongs to a class, then uses a threshold (usually 0.5) to make the final decision.

**How it works:** It applies a sigmoid function to a linear combination of the input features, squashing the output to a value between 0 and 1. If the probability is above 0.5, it predicts class 1.

**Use case:** Predicting whether a bank customer will default on a loan based on income, credit score, and employment history.

**Advantage:** Simple, fast, and easy to interpret. You can see exactly how each feature influences the prediction.

**Limitation:** Assumes a linear boundary between classes. Struggles when the relationship between features and the label is complex or non-linear.

---

### Decision Trees

A Decision Tree splits the data step by step using the feature that best separates the classes at each point. The result looks like a flowchart — each node is a question, each branch is an answer, and each leaf is a prediction.

**How it works:** It picks the feature that gives the best split (measured by Gini impurity or entropy), divides the data, then repeats on each branch until the data is pure or a stopping condition is met.

**Use case:** Deciding whether to approve a loan — the tree might first ask "Is credit score above 650?", then "Does the applicant have collateral?", and so on.

**Advantage:** Very easy to visualize and explain. No need to scale features.

**Limitation:** Prone to overfitting. A deep tree memorizes the training data and generalizes poorly.

---

### Random Forest

Random Forest builds many decision trees, each trained on a random subset of the data and features. For classification, each tree votes and the majority vote wins.

**How it works:** It uses a technique called bagging — sampling the training data with replacement for each tree. Combined with random feature selection at each split, this makes the trees diverse. Averaging many imperfect trees produces a strong, stable model.

**Use case:** Fraud detection in banking — detecting whether a transaction is legitimate or fraudulent based on amount, location, time, and history.

**Advantage:** Much more accurate than a single tree. Handles missing values and mixed feature types well. Resistant to overfitting.

**Limitation:** Harder to interpret than a single Decision Tree. Slower to train when using many trees.

---

## 3. Classification Metrics

### Accuracy

The percentage of all predictions that were correct. Simple but can be misleading when one class is much more common than the other.

### Precision

Of all the cases the model predicted as positive, how many actually were positive. High precision means few false alarms.

### Recall

Of all the actual positive cases, how many did the model catch. High recall means fewer missed positives.

### F1-Score

The harmonic mean of Precision and Recall. Useful when you need to balance both — especially with imbalanced classes.

### Confusion Matrix

A table showing the four possible outcomes: True Positives, True Negatives, False Positives, and False Negatives. It gives the full picture of where the model is getting things right and wrong.

---

### Comparison Table

| Metric           | What It Measures                          | Sensitive to Imbalance                 |
| ---------------- | ----------------------------------------- | -------------------------------------- |
| Accuracy         | Overall correct predictions               | Yes — misleading if classes are skewed |
| Precision        | How reliable positive predictions are     | Partly                                 |
| Recall           | How many positives were caught            | Partly                                 |
| F1-Score         | Balance between Precision and Recall      | No — better for imbalanced data        |
| Confusion Matrix | Full breakdown of all prediction outcomes | No — shows everything                  |

---

## 4. Class Imbalance

Accuracy becomes misleading when one class dominates the dataset. If 90% of loan applications are rejected, a model that always predicts "Rejected" achieves 90% accuracy — without learning anything useful. It will miss every legitimate approval.

**When to prioritize Precision:** When false positives are costly. In loan approval, approving a bad applicant costs the bank money. If that's the bigger concern, prioritize Precision — make sure approvals are reliable.

**When to prioritize Recall:** When false negatives are costly. If the bigger concern is rejecting good applicants and losing business, prioritize Recall — make sure the model catches as many qualified applicants as possible.

In practice, F1-Score is the better default metric for loan approval because both mistakes carry real cost.

---

## 5. Real-World Case Study — Predicting Match Outcomes in Football

**Source:** Bunker, R. P., & Thabtah, F. (2019). A machine learning framework for sport result prediction. _Applied Computing and Informatics_, 15(1), 27–33.

**Goal:** Predict the outcome of football matches — win, draw, or loss — using pre-match statistics and historical performance data.

**Data used:** Match records from several professional leagues including the English Premier League. Features included home/away advantage, recent form (last 5 matches), goals scored, goals conceded, shots on target, and head-to-head history.

**Type of classifier:** The study tested multiple classifiers including Logistic Regression, Decision Trees, and Random Forest. Random Forest consistently outperformed the others.

**Key results:** Random Forest achieved the highest accuracy across most leagues, with home advantage and recent form being the strongest predictors of match outcome. The study also found that draw prediction was the hardest class to get right — draws are inherently unpredictable and underrepresented compared to wins and losses, which is a real-world class imbalance problem.

This case study is a strong example of why Accuracy alone is not enough — the model looked good overall but struggled on draws. F1-Score per class gave a much clearer picture of actual performance.
