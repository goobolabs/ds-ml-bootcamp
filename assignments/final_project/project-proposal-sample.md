# Sample Project Proposal — Loan Approval Prediction API

> This is an **instructor example** showing what a complete proposal looks like. Do not copy this project — choose your own problem, dataset, and algorithms.

**Date:** July 2026

---

## 1. Certificate Name

**Ahmed Hassan Mohamed**

*(Example — submit your own legal/full name as you want it on your certificate.)*

---

## 2. Project Title and Description

**Title:** Loan Approval Prediction API

A bank receives hundreds of loan applications each week. Loan officers need a fast, consistent first screening tool. This project builds a machine learning model that predicts whether a loan application is likely to be approved based on applicant details (income, credit history, loan amount, etc.). The final deliverable is a REST API that accepts applicant data as JSON and returns an approval prediction with a probability score — useful for demo dashboards or internal triage tools.

---

## 3. Problem Type

**Classification** — binary output: `Approved` or `Rejected`.

The target column is `Loan_Status`. This is supervised learning: we train on historical applications where the outcome is already known.

---

## 4. Dataset

- **Source:** [Loan Approval Prediction Dataset](https://www.kaggle.com/datasets/wordsforthewise/lending-club) (Kaggle mirror of a standard loan-approval tabular dataset; alternative: UCI Credit Approval dataset).
- **Size:** ~1,500 rows, 12+ columns.
- **Target:** `Loan_Status` — whether the loan was approved (`Y`) or rejected (`N`).
- **Main features:**
  - `ApplicantIncome` — monthly income (numeric)
  - `CoapplicantIncome` — co-applicant income (numeric)
  - `LoanAmount` — requested loan amount (numeric)
  - `Loan_Amount_Term` — repayment term in months (numeric)
  - `Credit_History` — 1 = good credit history, 0 = poor (numeric/binary)
  - `Gender`, `Married`, `Dependents`, `Education`, `Self_Employed`, `Property_Area` — categorical columns to encode

**Preprocessing plan:** impute missing values, encode categoricals (one-hot or label encoding), scale numeric features, stratified train/test split (80/20).

---

## 5. Algorithms I Plan to Train

| # | Algorithm | Why it fits |
| --- | --- | --- |
| 1 | **Logistic Regression** | Bootcamp baseline for binary classification; fast, interpretable coefficients. |
| 2 | **Random Forest** | Bootcamp ensemble; reduces overfitting vs a single tree, handles mixed feature types well. |
| 3 | **Gradient Boosting (sklearn)** | Researched — often strong on structured/tabular data; good candidate for best model. |

This meets the **minimum of three** algorithms. Two (Logistic Regression, Random Forest) come from Lessons 4–5. Gradient Boosting I will research via scikit-learn documentation and one tutorial. I may add more algorithms (e.g. Decision Tree, SVM) if time allows.

---

## 6. Evaluation Plan

**Metrics for all models (on the same held-out test set):**

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

**Best-model rule:** Rank all trained models by **F1-Score** on the test set. F1 balances Precision and Recall — important here because false approvals (bad loans) and false rejections (lost good customers) both matter. If two models tie on F1, break the tie with higher **Recall** (catch more actual approvals).

I will print a comparison table with one row per algorithm and save/deploy only the winner.

---

## 7. Deployment Sketch

- **Framework:** FastAPI (simple, modern, auto-generates API docs at `/docs`).
- **Endpoint:** `POST /predict`
- **Input JSON example:**

```json
{
  "ApplicantIncome": 5000,
  "CoapplicantIncome": 1500,
  "LoanAmount": 120,
  "Loan_Amount_Term": 360,
  "Credit_History": 1,
  "Gender": "Male",
  "Married": "Yes",
  "Dependents": "1",
  "Education": "Graduate",
  "Self_Employed": "No",
  "Property_Area": "Urban"
}
```

- **Output JSON example:**

```json
{
  "prediction": "Approved",
  "probability": 0.87
}
```

The API loads the best saved model from `models/best_model.pkl` plus any preprocessing artifacts (scaler, encoders).

---

## 8. Repository Plan

```
loan-approval-api/
├── dataset/
│   └── raw_loans.csv
├── src/
│   ├── preprocess.py      # cleaning, encoding, scaling, train/test split
│   └── train.py           # train all models, compare, save best
├── api/
│   └── app.py             # FastAPI app with /predict
├── models/
│   ├── best_model.pkl
│   └── scaler.pkl
├── notebooks/
│   └── exploration.ipynb  # optional EDA
├── README.md
├── requirements.txt
└── project_paper.md
```

**Run commands (planned):**

```bash
python src/train.py        # trains models, prints comparison table, saves best
uvicorn api.app:app --reload   # starts API locally
```

---

*Sample proposal — for reference only. Submit your own original project idea.*
