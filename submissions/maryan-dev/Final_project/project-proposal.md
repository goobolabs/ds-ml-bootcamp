# 📊 Final Project Proposal

---

# 1. Certificate Name

> **Maryan Mohamed Adam**

---

# 2. Project Title and Description

**Title:** **Machine Learning-Based Employment Status Prediction Using Somali Labour Force Data**

Employment is one of the most pressing socioeconomic challenges in Somalia, with many young people and women facing unemployment or remaining outside the labour force entirely.

This project builds a machine learning model that predicts an individual's employment status (**Employed, Unemployed, or Not in Labour Force**) from demographic and household characteristics.

The tool is intended for use by government agencies, NGOs, and development organizations who need fast, data-driven insight into labour market patterns to design and target employment interventions, rather than waiting on slow manual survey analysis.

---

# 3. Problem Type

🏷️ **Classification**

The target column, **`employment_status`**, has three categories:

- **Employed**
- **Unemployed**
- **Not in Labour Force**

Therefore, this is a **multiclass classification problem**.

---

# 4. Dataset

| **Item** | **Description** |
|:---------|:----------------|
| **Source** | `lfs_somalia_synthetic_2000.csv` — a synthetic Somali labour force dataset modeled on the structure of the Somali Labour Force Survey (SLFS 2019, Somalia National Bureau of Statistics / ILO). |
| **Size** | **2,000 rows, 10 columns** — meets the **1,000-row minimum requirement**. |
| **Target Column** | `employment_status` |

### 📈 Target Distribution

| **Employment Status** | **Number of Rows** |
|:----------------------|------------------:|
| Employed | 1,104 |
| Unemployed | 541 |
| Not in Labour Force | 355 |

The dataset contains **class imbalance**, which will be addressed during model training using techniques such as:

- Class weighting
- Stratified sampling

---

## 📌 Main Features

### `age`

Respondent's age in years.

### `gender`

Male / Female.

### `region`

One of **7 Somali regions**, including:

- Banadir
- Puntland
- Somaliland

### `education`

Education level:

- Primary
- Secondary
- Tertiary
- Vocational

Missing education values (**~25%**) will be handled through:

- Imputation
- Missing-value indicators

### `marital_status`

Categories:

- Single
- Married
- Widowed
- Divorced

### `sector`

Industry sector of work.

**Examples:**

- Trade
- Agriculture
- Fishing

This feature is mostly missing for non-workers, so it will be treated carefully and used only as a **secondary/derived feature**.

---

## 🚫 Excluded Features

The following features will **not** be used as model inputs:

- `hours_worked`
- `monthly_wage_usd`

These features create **data leakage** because:

- `hours_worked = 0` for every non-employed person.
- The value directly reveals the employment status.

Including these variables would make the model learn the answer directly instead of discovering real employment patterns.

---

# 5. Algorithms  Plan to Train

### 1. Logistic Regression *(Bootcamp)*

- Simple and interpretable multiclass baseline.
- Provides a strong reference point before testing more advanced models.

### 2. Decision Tree *(Bootcamp)*

- Produces clear and interpretable decision rules.
- Shows how features such as age, education, and region contribute to predictions.
- Serves as a comparison with the ensemble-based Random Forest model.

### 3. Random Forest *(Bootcamp)*

- Handles both categorical and numerical features effectively.
- Captures nonlinear relationships between variables.
- Reduces overfitting compared with a single Decision Tree.

### 4. XGBoost *(Self-Researched)*

- Gradient boosting algorithm known for high predictive performance.
- Well suited for structured/tabular datasets.
- Includes built-in techniques for handling class imbalance.

---

## 🔍 Optional Exploratory Step (Unsupervised)

Before training the classification models, **K-Means Clustering** will be applied using the following features:

- `age`
- `education`
- `region`
- `gender`
- `marital_status`

The purpose is to explore natural demographic groups within the Somali labour force dataset, such as populations with similar education levels, ages, and employment characteristics.

Because K-Means does **not** use the target variable (`employment_status`) during training, it will **not** be compared with the classification models using Accuracy, Precision, Recall, or Macro F1-Score.

Instead, it will be evaluated separately using the **Silhouette Score** and will be used only to support exploratory data analysis (EDA) and feature engineering.

---

# 6. Evaluation Plan

## 📊 Evaluation Metrics

The following metrics will be calculated for each classification model:

- Accuracy
- Precision
- Recall
- Macro F1-Score
- Confusion Matrix

### 🏆 Model Selection

The final model will be selected based on the **Macro F1-Score** because:

- The dataset contains imbalanced classes.
- Macro F1 gives equal importance to all employment categories.
- It prevents the majority class (**Employed**) from dominating the evaluation.

---

# 7. Deployment Sketch

### ⚙️ Framework

**FastAPI**

### 🌐 API Endpoint

```http
POST /predict
```

### 📥 Input (JSON)

```json
{
  "age": 28,
  "gender": "Female",
  "region": "Banadir",
  "education": "Secondary",
  "marital_status": "Single"
}
```

### 📤 Output (JSON)

```json
{
  "predicted_status": "Unemployed",
  "probabilities": {
    "Employed": 0.22,
    "Unemployed": 0.61,
    "Not in Labour Force": 0.17
  },
  "model_used": "XGBoost"
}
```

---

# 8. Repository Plan

```text
maryan-dev-final-project/
│
├── dataset/
│   └── lfs_somalia_synthetic_2000.csv
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── evaluate.py
│
├── api/
│   └── app.py
│
├── models/
│   └── best_model.pkl
│
├── README.md
│
└── project_paper.md
```

---

## ✅ Summary

- **Problem Type:** Multiclass Classification
- **Dataset Size:** 2,000 rows × 10 columns
- **Target Variable:** `employment_status`

- **Bootcamp Algorithms:** Logistic Regression, Decision Tree, Random Forest
- **Self-Researched Algorithm:** XGBoost
- **Optional Unsupervised Analysis:** K-Means Clustering
- **Evaluation Metric:**  F1-Score
- **Deployment Framework:** FastAPI
- **API Endpoint:** `POST /predict`