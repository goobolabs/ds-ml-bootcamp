# Project Proposal — Stroke Risk Prediction API

## 1. Certificate Name
Iqra Dahir
## 2. Project Title and Description

**Title:** Stroke Risk Prediction API

*Hospitals and clinics screen large numbers of patients for stroke risk factors, but early warning signs are often missed until it's too late. This project builds a machine learning model that predicts whether a patient is at risk of stroke based on health and demographic data (age, glucose level, BMI, hypertension, heart disease, smoking status, etc.).*
---
## 3. Problem Type

**Classification** — binary output: `Stroke` or `No Stroke`.

Target column: `stroke` (1 = had stroke, 0 = did not). Supervised learning, trained on historical patient records with known outcomes.

**Note:** This dataset is heavily imbalanced (~5% positive class) — accuracy alone will be misleading, so recall, F1, and ROC-AUC matter more.
---
## 4. Dataset

- **Source:** [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset) (Kaggle)
- **Size:** ~5,110 rows, 12 columns (can subsample to ~2,000 if scope requires)
- **Target:** `stroke` — 1 or 0
- **Main features:**
  - `age`, `avg_glucose_level`, `bmi` — numeric (`bmi` has missing values)
  - `hypertension`, `heart_disease` — binary numeric
  - `gender`, `ever_married`, `work_type`, `Residence_type`, `smoking_status` — categorical

**Preprocessing plan:** impute missing `bmi` (median or KNN imputer), IQR capping on outliers, one-hot encode categoricals, StandardScaler on numerics, stratified 80/20 train/test split.

---

## 5. Algorithms I Plan to Train

| # | Algorithm | Why it fits |
| --- | --- | --- |
| 1 | **Logistic Regression** | Baseline; interpretable coefficients show which risk factors matter most. |
| 2 | **Decision Tree** | Bootcamp model; simple, interpretable, captures non-linear splits (e.g. age/glucose thresholds). |
| 3 | **Random Forest** | Ensemble method, handles mixed feature types and non-linear relationships well; reduces overfitting vs a single tree. |
| 4 | **SVM (RBF kernel)** | Researched — effective on smaller, well-scaled feature sets; good comparison point against tree-based models. |
| 5 | **XGBoost** | Researched — gradient boosting typically outperforms Random Forest on structured/tabular health data. Candidate for best model. |

Three algorithms (Logistic Regression, Random Forest) are bootcamp standard. SVM,Decision Tree and XGBoost are researched additions.

**Handling class imbalance:** since the dataset is ~95/5 imbalanced, this is treated as a *preprocessing/training technique* applied consistently across models (via `class_weight='balanced'` where supported, and `scale_pos_weight` for XGBoost) rather than as separate algorithm entries — keeping the comparison table clean while still addressing the imbalance problem head-on.

## 6. Evaluation Plan

**Metrics for all models (on the same held-out test set):**

- Accuracy (reported but not used to rank — misleading with imbalance)
- Precision, Recall, F1-Score
- ROC-AUC and Precision-Recall AUC (more informative than ROC-AUC alone under imbalance)
- Confusion Matrix

**Best-model rule:** Rank by **Recall** first (missing an actual stroke case is the costlier error), tie-break with **F1-Score**. Comparison table with one row per algorithm; save/deploy only the winner.

**Cool extra:** Use **SHAP (SHapley Additive exPlanations)** on the winning model to show which features drove each individual prediction — this powers the "explanation" field in the API response below.
---
## 7. Deployment Sketch

- **Framework:** FastAPI
- **Endpoint:** `POST /predict`
- **Input JSON example:**

```json
{
  "gender": "Female",
  "age": 67,
  "hypertension": 0,
  "heart_disease": 1,
  "ever_married": "Yes",
  "work_type": "Private",
  "Residence_type": "Urban",
  "avg_glucose_level": 228.69,
  "bmi": 36.6,
  "smoking_status": "formerly smoked"
}
```

- **Output JSON example:**

```json
{
  "prediction": "Stroke Risk",
  "probability": 0.74,
  "top_risk_factors": [
    {"feature": "age", "impact": "+0.21"},
    {"feature": "avg_glucose_level", "impact": "+0.15"},
    {"feature": "heart_disease", "impact": "+0.09"}
  ]
}
```

The API loads the best saved model (`models/best_model.pkl`), preprocessing artifacts (scaler, encoders, imputer), and a SHAP explainer object.

---

## 8. Repository Plan

```
stroke-prediction-api/
├── dataset/
│   └── raw_stroke_data.csv
├── src/
│   ├── preprocess.py      # imputation, IQR capping, encoding, scaling, split
│   ├── train.py           # train all 5 models, compare, save best
│   └── explain.py         # SHAP explainer setup
├── api/
│   └── app.py             # FastAPI app with /predict
├── models/
│   ├── best_model.pkl
│   ├── scaler.pkl
│   └── shap_explainer.pkl
├── notebooks/
│   └── exploration.ipynb
├── README.md
├── requirements.txt
└── project_paper.md
```

**Run commands (planned):**

```bash
python src/train.py
uvicorn api.app:app --reload
```
