# Final Project Proposal — Customer Personality Analysis API

**Date:** July 2026

---

## 1. Certificate Name

**Ahmed Ali Abdi**

---

## 2. Project Title and Description

**Title:** Customer Personality Analysis: Customer Segmentation and Purchase Prediction API

Businesses collect large amounts of customer data but often struggle to understand customer behavior and identify the customers most likely to respond to marketing campaigns. This project builds a machine learning system that analyzes customer characteristics and purchasing behavior to create customer segments and predict whether a customer will accept a marketing campaign. The final deliverable will be a REST API that accepts customer information as JSON and returns a prediction with a probability score. This system can help businesses improve marketing decisions, personalize offers, and increase customer engagement.

---

## 3. Problem Type

**Classification** — binary output: `Accepted` or `Not Accepted`.

The target column is **`Response`**.

* `1` = Customer accepted the marketing campaign.
* `0` = Customer did not accept the marketing campaign.

This is a supervised learning problem. In addition, clustering will be used to discover different customer groups based on purchasing patterns.

---

## 4. Dataset

* **Source:** Customer Personality Analysis Dataset (Kaggle)
  https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis

* **Size:** 2,240 rows and 29 columns.

* **Target:** `Response` — represents whether a customer accepted the marketing campaign.

### Main Features:

* `Income` — customer annual income.
* `Year_Birth` — customer birth year.
* `Education` — education level.
* `Marital_Status` — customer marital status.
* `Recency` — number of days since the last purchase.
* `NumWebPurchases` — number of online purchases.
* `NumStorePurchases` — number of store purchases.
* `NumCatalogPurchases` — number of catalog purchases.
* `NumWebVisitsMonth` — monthly website visits.
* `MntWines` — money spent on wine products.
* `MntFruits` — money spent on fruit products.
* `MntMeatProducts` — money spent on meat products.

**Preprocessing plan:**
I will handle missing values, remove duplicates, encode categorical variables, scale numerical features, perform feature engineering, and split the dataset into training and testing sets.

---

## 5. Algorithms I Plan to Train

| # | Algorithm               | Why it fits                                                                                                |
| - | ----------------------- | ---------------------------------------------------------------------------------------------------------- |
| 1 | **Logistic Regression** | A baseline classification algorithm that is fast and provides interpretable results for binary prediction. |
| 2 | **Random Forest**       | An ensemble learning algorithm that handles complex customer behavior patterns and reduces overfitting.    |
| 3 | **XGBoost**             | An advanced boosting algorithm that often performs well on structured customer datasets.                   |
| 4 | **K-Means Clustering**  | Used to group customers into meaningful segments such as VIP, regular, and budget customers.               |

This project uses Logistic Regression, Random Forest, and K-Means from machine learning fundamentals, while XGBoost will be researched and implemented as an additional algorithm.

---

## 6. Evaluation Plan

### Classification Metrics:

All classification models will be compared using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* ROC-AUC

**Best-model rule:**
The final model will be selected based on the highest **F1-Score** because it balances Precision and Recall and provides a better measure when predicting customer responses.

### Clustering Metrics:

For customer segmentation, I will use:

* Silhouette Score

The clustering model with the highest Silhouette Score will be selected.

---

## 7. Deployment Sketch

* **Framework:** FastAPI

* **Endpoint:** `POST /predict`

### Input JSON Example:

```json
{
  "Income": 50000,
  "Age": 35,
  "Education": "Graduate",
  "Marital_Status": "Single",
  "Recency": 15,
  "NumWebPurchases": 5,
  "NumStorePurchases": 4,
  "NumCatalogPurchases": 2
}
```

### Output JSON Example:

```json
{
  "prediction": "Accepted",
  "probability": 0.89
}
```

The API will load the best trained model and preprocessing files, then return the predicted customer response and probability.

---

## 8. Repository Plan

```
customer-personality-analysis-api/
├── dataset/
│   └── marketing_campaign.csv
├── src/
│   ├── preprocess.py
│   ├── clustering.py
│   ├── train.py
│   └── evaluate.py
├── api/
│   └── app.py
├── models/
│   ├── best_model.pkl
│   └── scaler.pkl
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
