# 📄 Project Paper — Stroke Risk Prediction API (NeuroGuard)

**Author:** Iqra Dahir  
**GitHub Repository:** [github.com/Iqra027/stroke-prediction-api](https://github.com/Iqra027/stroke-prediction-api)  
**Dataset:** [Kaggle Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)  

---

## 1. Executive Summary & Problem Description

Stroke is one of the leading causes of disability and mortality worldwide. While hospitals and clinics screen large numbers of patients for stroke risk factors, early warning signs are often missed until acute symptoms appear.

The **NeuroGuard Stroke Risk Prediction API** solves this problem by building an end-to-end Machine Learning inference pipeline that predicts whether a patient is at risk of stroke based on clinical and demographic data (age, average glucose level, BMI, hypertension, heart disease, smoking status, etc.). It serves as an early clinical warning system powered by a FastAPI backend.

---

## 2. Project Architecture & Directory Structure

The project has been modularized into standard production folders (`clients/`, `Dataset/`, `docs/`, `models/`, and `src/`) to ensure clean separation of concerns across the frontend UI, dataset storage, serialized models, documentation, and backend application code:

```text
STROK/
├── 📂 clients/                            # Web dashboard UI files
│   ├── index.html
│   ├── script.js
│   └── style.css
├── 📂 Dataset/                            # Training datasets
│   ├── clean_stroke_dataset.csv
│   └── healthcare-dataset-stroke-data.csv
├── 📂 docs/                               # Project reports & papers
│   ├── NeuroGuard_Resolution_Report.pdf
│   ├── model_comparison.md
│   └── project_paper.md
├── 📂 models/                             # Serialized joblib artifacts & scaler
│   ├── model_decision_tree.joblib
│   ├── model_features.joblib
│   ├── model_logistic_regression.joblib
│   ├── model_random_forest.joblib
│   ├── model_svm.joblib
│   ├── model_xgboost.joblib
│   └── scaler.pkl
├── 📂 src/                                # Core Python scripts (Backend & Training)
│   ├── main.py                            # FastAPI app & prediction endpoint
│   ├── preprocess.py                      # Data cleaning & pipeline transformations
│   └── train.py                           # Model training & regularization script
└── README.md                              # Repository overview & setup guide
```

---

## 3. Dataset & Preprocessing Pipeline

* **Dataset Source:** [Stroke Prediction Dataset (Kaggle)](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
* **Dataset Structure:** 5,110 patient records across 12 feature columns.
* **Target Variable:** `stroke` (Binary Classification: `1` = Stroke Risk, `0` = No Stroke Risk).
* **Class Imbalance:** The dataset is heavily imbalanced with approximately **~95% negative cases (no stroke)** and **~5% positive cases (stroke)**.

### Preprocessing Applied:
1. **Missing Value Imputation:** Missing `bmi` values were imputed using median statistical values in `src/preprocess.py`.
2. **Feature Scaling:** `StandardScaler` was applied to continuous numeric features (`age`, `avg_glucose_level`, `bmi`).
3. **Categorical Encoding:** One-Hot Encoding was applied to categorical variables (`gender`, `ever_married`, `work_type`, `Residence_type`, `smoking_status`).
4. **Data Splitting:** Stratified 80/20 train/test split to preserve target distribution ratio.

---

## 4. Algorithm Training & Comparative Evaluation

Five distinct machine learning models were trained and benchmarked on the same held-out test set:

| # | Algorithm | Model Role / Tuning Strategy | Recall Score | Healthy Baseline Risk % | Evaluation Status |
|---|---|---|---|---|---|
| **1** | **Support Vector Machine (SVM)** | RBF Kernel (Best Recall Performance) | **34.0%** 🏆 | **1.5%** | **SELECTED BEST MODEL** |
| **2** | **Logistic Regression** | Linear Baseline | 31.0% | 4.2% | Validated |
| **3** | **Random Forest Classifier** | Ensemble (`max_depth=5`) | 28.5% | 8.8% | Regularized |
| **4** | **XGBoost Classifier** | Gradient Boosting (`scale_pos_weight=4`) | 26.0% | 0.4% | Regularized |
| **5** | **Decision Tree Classifier** | Single Tree (`max_depth=4`, `min_samples_leaf=15`) | 22.0% | 0.0% | Pruned |

### 🏆 Best Model Selection Rule:
Because missing a stroke case is significantly costlier than triggering a false warning in clinical screenings, **Recall** was designated as the primary selection metric. **Support Vector Machine (SVM with RBF Kernel)** emerged as the **best-performing model**, achieving the highest recall rate (34.0%) while providing smooth, calibrated risk probabilities (1.5% on healthy test profiles).

---

## 5. Technical Challenges & Overfitting Mitigation

During system testing, an anomaly occurred where unconstrained tree models (Decision Tree & XGBoost) predicted **99.9% to 100% stroke risk** for healthy 30-year-old patient profiles (Age 30, BMI 22, Glucose 100).

### Root Causes & Fixes Applied:
1. **Deep Leaf Memorization:** Unconstrained tree depth isolated minority stroke cases into isolated leaf nodes.
   * *Fix:* Applied hyperparameter depth constraints (`max_depth=4` for Decision Trees, `max_depth=5` for Random Forest) and minimum leaf sample sizes (`min_samples_leaf=15`) inside `src/train.py`.
2. **Categorical Vector Misalignment:** Defaulting unselected categorical features to all zeros created unseen pathways.
   * *Fix:* Implemented realistic baseline health encodings (`smoking_status_never smoked = 1`, `work_type_Private = 1`) in `src/main.py` and serialized explicit column schemas (`models/model_features.joblib`).

---

## 6. Overall Lessons Learned & Key Insights

1. **Accuracy is Misleading in Imbalanced Medical Data:** In a dataset where 95% of patients do not have a stroke, a naive model that predicts "No Stroke" 100% of the time gets 95% accuracy but is clinically useless. Prioritizing **Recall** and **F1-Score** is crucial for clinical safety.
2. **Regularization is Required for Tree Ensembles:** Tree models (XGBoost & Decision Trees) easily memorize noise when dealing with imbalanced minority classes. Hyperparameter tuning (`max_depth`, `min_samples_leaf`) is essential to prevent false-positive alarms.
3. **Seamless Deployment Requires Schema Persistence:** Exporting feature schemas (`models/model_features.joblib`) during training guarantees that API request transformations in `src/main.py` always match the exact feature dimensions expected by the trained model binaries.
