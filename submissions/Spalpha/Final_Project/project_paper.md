# Bank Loan Approval and Creditworthiness Predictor — Project Paper

**Author:** Suhayb Hassan Mohammoud

## 1. Problem Statement
Manual loan-application review is slow, inconsistent, and prone to human
bias. This project builds a binary classification model that predicts
whether a loan application should be **Approved (1)** or **Rejected (0)**
based on the applicant's financial and credit profile.

## 2. Dataset
- Source: Kaggle "Loan Approval Prediction Dataset"
- 4,269 rows, 12 raw features + target (`loan_status`)
- Target distribution after cleaning: ~62% Approved / ~38% Rejected — moderately
  imbalanced, which is why F1-Score (not raw Accuracy) was used to pick the
  final model.

## 3. Preprocessing (`src/preprocess.py`)
- Stripped whitespace from string columns (raw CSV headers/values contain
  leading spaces).
- Dropped the `loan_id` identifier column.
- Filled missing numeric values with the column median.
- Binary-encoded `education` (Graduate=1 / Not Graduate=0) and
  `self_employed` (Yes=1 / No=0).
- **Feature engineering:** added `total_asset_value`, the sum of
  `residential_assets_value + commercial_assets_value + luxury_assets_value +
  bank_asset_value`, as a single measure of overall applicant wealth.

## 4. Models Trained (`src/train.py`)
| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Logistic Regression | 0.913 | 0.921 | 0.942 | 0.931 |
| Random Forest | 0.982 | 0.981 | 0.991 | **0.986** |
| SVM (RBF kernel) | 0.943 | 0.958 | 0.949 | 0.954 |

**Selected model: Random Forest** (highest F1-Score).

Logistic Regression and SVM were trained on `StandardScaler`-scaled features
(fit on the training split only, to avoid data leakage); Random Forest does
not require scaling.

## 5. Caveat on Result Quality
The F1-Score of ~0.986 is unusually high for a real-world credit-risk task.
Exploratory analysis shows `cibil_score` alone is a near-deterministic
predictor of `loan_status` in this specific dataset. This should be reported
as a **limitation of the dataset**, not evidence that the model would
perform this well on live bank data — a production deployment would need
validation against a more representative, noisier dataset before being
trusted for real lending decisions.

## 6. Deployment
A FastAPI service (`api/app.py`) exposes a `POST /predict` endpoint that
accepts the raw applicant fields, reconstructs the same engineered features
used at training time, applies the saved scaler if required by the winning
model, and returns the predicted label, human-readable status, and approval
probability.

## 7. Future Work
- Validate on an external/held-out dataset to test generalization beyond
  this specific Kaggle sample.
- Add SHAP or permutation feature-importance analysis to make the model's
  decisions explainable to loan officers and applicants.
- Add fairness/bias auditing across demographic proxies (e.g. dependents,
  employment status) before any real deployment.
