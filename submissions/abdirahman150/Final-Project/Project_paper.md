# Real-Time Credit Card Fraud Detection API

## Author: 
Abdirahman Khadar Muxumed

**Date:** July 2026

---

## 1. Problem Statement and Motivation
Credit card fraud costs financial institutions and cardholders billions of dollars every year, and the damage is worsened by how thin the signal is: legitimate financial institutions process thousands of transactions per second, while genuinely fraudulent ones make up a tiny fraction of that volume. A human review process cannot scale to this speed, so banks need an automated system that can look at a transaction the instant it happens and decide, in milliseconds, whether it is safe to approve or whether it should be flagged for review or rejected outright.

This project addresses that problem directly: build a supervised machine learning model that classifies an incoming credit card transaction as legitimate or fraudulent based on its attributes, and deploy that model as a real-time REST API. The goal is not just an accurate model on paper, but a working service that mirrors how such a model would actually sit inside a payment-processing pipeline accepting a transaction as JSON and returning a decision and a risk score in the same request/response cycle.

This matters because the cost of getting it wrong is asymmetric in both directions: missing fraud (a false negative) is a direct financial loss, while wrongly blocking a legitimate transaction (a false positive) damages customer trust and generates support costs. A useful fraud model has to be judged on how it balances both of these failure modes, not on raw accuracy.

---

## 2. Dataset and Preprocessing
### 2.1 Source and Size
The dataset used is the Credit Card Fraud Detection Dataset, a Kaggle mirror of anonymized transactions made by European cardholders (https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud). It contains 284,807 transactions across 31 columns. After removing exact duplicate rows in preprocessing, 283,726 rows remain.
### 2.2 Features
- Time — seconds elapsed between the given transaction and the first transaction in the dataset.
- Amount — the transaction amount.
- V1 through V28 — twenty-eight anonymized features produced via Principal Component Analysis (PCA) on the original transaction attributes.
- Class — the target label: 0 for legitimate, 1 for confirmed fraud.

The dataset is severely imbalanced: only 473 of 283,726 transactions (~0.17%) are labeled as fraud.

### 2.3 Cleaning and Outlier Analysis
Implemented in utility/preprocess.py:

1. Duplicate removal — exact duplicate rows dropped.
2. Outlier analysis on Amount — IQR-based upper bound computed; fraud cases fall meaningfully into that range, so outliers are kept rather than dropped, to avoid discarding scarce fraud examples.

### 2.4 Scaling and Splitting
Implemented in utility/train.py:
- Time and Amount scaled with RobustScaler (chosen over StandardScaler for its resistance to the retained outliers).
- Stratified 80/20 train/test split (random_state=42) to preserve the fraud ratio in both sets.

--- 

## 3. Algorithms
|Algorithm| Type| Why chosen|
|-----|-----|-----|
|Logistic Regressio| Linear| 	Fast, interpretable baseline; class_weight='balanced'|
|Random Forest| Ensemble of trees| Robust to overfitting and skewed features; class_weight='balanced'|
|XGBoost| Gradient-boosted trees| Best-in-class for tabular data; scale_pos_weight tuned for imbalance|

---

## 4. Results and Discussion
### 4.1 Comparison Table (test set: 56,746 transactions, 95 fraud)
|Algorithm| Precision|Recall|F1-Score|ROC-AUC|
|-----|-----|-----|-----|-----|
|Logistic Regression|0.0564|0.8737|0.1059|0.9246|
|Random Forest|0.9710|0.7053|0.8171|0.8526|
|XGBoost|0.9375|0.7895|0.8571|0.8947|

- Selection rule: highest F1-score — accuracy is meaningless here since predicting "legitimate" every time would score >99% while catching zero fraud. XGBoost wins.

### 4.2 Why XGBoost Won
- Logistic Regression: highest recall but only 5.6% precision — unusable false-alarm rate.
- Random Forest: highest precision but lowest recall — misses more fraud.
- XGBoost: best balance of both, highest F1.

### 4.3 Confusion Matrix (XGBoost, Test Set)
|Predicted Legit|Predicted Fraud|
|-----|-----|-----|
|Actual Legit|56,646|5|
|Actual Fraud|20|75|

- 75/95 fraud cases caught (78.9% recall), only 5/56,651 false alarms (0.009% false-positive rate). Accuracy: 99.96% (reported for completeness only).

### 4.4 Sanity Checks
|Check| Amount|True Class|Predicted|Fraud Probability|
|1|	$149.62|Legitimate|Legitimate|0.0000|
|2|	$378.66|Legitimate|Legitimate|0.0000|
|3|	$0.00|Fraud|Fraudulent|1.0000|

---

## 5. Deployment Notes
models/best_model.pkl bundles the model, RobustScaler, and feature order together, so inference always matches training-time preprocessing.

*FastAPI exposes:*

- GET / — health check
- POST /predict — accepts Time, Amount, V1–V28, returns:
```json
{
  "prediction": 0,
  "fraud_probability": 0.0142,
  "status": "Legitimate"
}
```

*Run locally:*
- uvicorn api.app:app --reload

---

## 6. Lessons Learned
- Class imbalance dominates every decision — from the stratified split to class_weight/scale_pos_weight to the F1-based selection rule.
- Precision and recall trade off — the "best" model depends on which error costs more; a single high metric (like Logistic Regression's recall) can hide an unusable model.
- Keeping outliers can be the right call — dropping them would have removed real fraud examples.

*What I'd improve with more time:*

- Systematic hyperparameter search for XGBoost
- Precision-recall curve analysis and explicit threshold tuning
- Pin dependency versions to avoid scikit-learn version-mismatch warnings
- Compare against SMOTE/resampling as an alternative to weighted loss

---

## 7. Conclusion

This project delivered a complete, working fraud-detection pipeline: cleaned and properly split data, three fairly compared algorithms, a metric-driven model selection, and a deployed API matching training-time preprocessing exactly. XGBoost was selected with an F1-score of 0.8571, catching 78.9% of fraud while keeping the false-positive rate at 0.009%.