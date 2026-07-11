# Assignment: Classification in Machine Learning

## 1. Introduction to Classification

Classification means teaching a model to sort inputs into fixed categories, using labeled data. Regression is different: it predicts a number, not a category.

Example of classification: predict if a loan is Approved or Rejected.
Example of regression: predict a car's price.

## 2. Classification Algorithms

**Logistic Regression**
Turns input features into a probability (0 to 1) using a sigmoid function. Above 0.5, predict positive class.
Use case: credit scoring.
Good: fast, easy to read, works well on simple patterns.
Bad: weak on non-linear data, sensitive to outliers.

**Decision Trees**
Splits data step by step (e.g. "CreditScore > 600?") until it reaches a decision.
Use case: medical triage rules.
Good: easy to explain, handles non-linear patterns.
Bad: overfits fast, unstable — small data change, different tree.

**Random Forest**
Many decision trees, each trained on random rows/features. Final answer = majority vote.
Use case: fraud detection.
Good: more accurate and stable than one tree.
Bad: harder to explain, slower to run.

## 3. Classification Metrics

- **Accuracy** – % of correct predictions. Misleading on imbalanced data.
- **Precision** – of predicted positives, how many were right. Matters when false positives are costly.
- **Recall** – of actual positives, how many were caught. Matters when false negatives are costly.
- **F1-Score** – balance of precision and recall.
- **Confusion Matrix** – table of correct/wrong predictions by type.

| Metric | Measures | Imbalance-sensitive? |
|---|---|---|
| Accuracy | Overall correctness | Yes |
| Precision | Correct positive predictions | Some |
| Recall | Coverage of real positives | Some |
| F1-Score | Balance of both | Less than accuracy |
| Confusion Matrix | Full breakdown | No, shows raw counts |

## 4. Class Imbalance

If 90% of loans are Approved, a model that always says "Approved" gets 90% accuracy — but it's useless.

For loan approval:
- Prioritize **Precision** if approving a bad loan (default) is costly.
- Prioritize **Recall** if rejecting good applicants is costly.

## 5. Real-World Case Study

A 2025 study built a machine learning pipeline to predict loan defaults, comparing Gradient Boosting, Random Forest, XGBoost, and LightGBM. The pipeline covered preprocessing, class-imbalance handling with SMOTE, training, tuning, and evaluation using accuracy, F1, ROC AUC, and confusion matrices. Gradient Boosting performed best, at about 88.9% accuracy and an F1 score around 0.81.

Same idea as this assignment: real finance data, same metrics, tree-based models. Lesson: ensembles usually beat single models, and imbalance needs direct handling, not just accuracy.

**Source:** *Data-Driven Loan Default Prediction: A Machine Learning Approach for Enhancing Business Process Management*, MDPI, 2025.
