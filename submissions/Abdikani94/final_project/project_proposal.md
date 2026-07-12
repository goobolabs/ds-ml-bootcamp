# Final Project Proposal

**Date:** July 2026

---

# 1. Certificate Name

**Abdi Kani Mohamed Hassan**

---

# 2. Project Title and Description

## Title

**Bank Customer Intelligence System: An End-to-End Machine Learning Web Application Using Supervised and Unsupervised Learning**

## Description

Banks contact many customers during marketing campaigns to promote term deposit accounts. However, contacting every customer is expensive, and many customers are not interested. This project aims to develop a machine learning system that predicts whether a customer will subscribe to a term deposit and groups customers into similar segments based on their demographic and financial characteristics. The system will help banks improve marketing decisions, better understand customer behavior, and reduce campaign costs.

The machine learning models will be deployed using **FastAPI**, while a simple **React web dashboard** will provide an interactive interface for users. The dashboard will allow users to enter customer information, receive prediction results, view customer segments, and explore model performance through charts and statistics.

---

# 3. Problem Type

This project combines two machine learning tasks.

## Classification (Supervised Learning)

Predict whether a customer will subscribe to a term deposit account.

**Output**

- Yes
- No

## Clustering (Unsupervised Learning)

Group customers into similar customer segments based on their demographic and financial information.

---

# 4. Dataset

## Source

**Bank Marketing Dataset (Kaggle)**

https://www.kaggle.com/datasets/mdnaimislam165436/bank-marketing-dataset-uci

## Dataset Size

- 45,211 rows
- 17 columns

## Target Column

`y`

- **Yes** – Customer subscribed to a term deposit.
- **No** – Customer did not subscribe.

## Main Features

- Age
- Job
- Marital Status
- Education
- Default
- Balance
- Housing Loan
- Personal Loan
- Contact Type
- Campaign
- Previous Campaign Information

## Preprocessing Plan

- Perform Exploratory Data Analysis (EDA)
- Remove duplicate records
- Check for missing values
- Remove the `duration` feature to prevent data leakage
- Encode categorical variables
- Scale numerical features
- Detect and handle outliers
- Perform feature selection
- Split the dataset into training and testing sets for classification

---

# 5. Algorithms I Plan to Train

## Classification (Supervised Learning)

### Logistic Regression

A simple and interpretable baseline model for binary classification.

### Random Forest

An ensemble learning algorithm that handles mixed feature types and provides strong prediction performance.

### XGBoost

A powerful boosting algorithm that often achieves high accuracy on structured datasets.

## Clustering (Unsupervised Learning)

### K-Means Clustering

The primary clustering algorithm used to group customers with similar characteristics.

### Agglomerative Clustering

A hierarchical clustering algorithm used to compare clustering quality with K-Means.

### DBSCAN

A density-based clustering algorithm used to identify customer groups and detect outliers automatically.

---

# 6. Evaluation Plan

## Classification Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

The best classification model will be selected using the **F1-Score** because it provides a good balance between Precision and Recall.

## Clustering Metrics

- Silhouette Score
- Davies-Bouldin Index
- Elbow Method (for K-Means)

The best clustering model will be selected using the **highest Silhouette Score** and the **lowest Davies-Bouldin Index**.

---

# 7. Deployment Sketch

## Frontend

- React
- Responsive dashboard
- Customer prediction form
- Customer segmentation page
- Charts and statistics

## Backend

- FastAPI
- REST API
- Swagger API documentation (`/docs`)

## API Endpoints

### Prediction Endpoint

```http
POST /predict
```

### Input

```json
{
  "age": 35,
  "job": "technician",
  "marital": "married",
  "education": "secondary",
  "balance": 2500,
  "housing": "no",
  "loan": "no",
  "campaign": 2
}
```

### Output

```json
{
  "prediction": "Yes",
  "probability": 0.87
}
```

---

### Customer Segmentation Endpoint

```http
POST /cluster
```

### Input

```json
{
  "age": 35,
  "job": "technician",
  "marital": "married",
  "education": "secondary",
  "balance": 2500,
  "housing": "no",
  "loan": "no",
  "campaign": 2
}
```

### Output

```json
{
  "cluster": 2,
  "description": "Customers with stable income and high probability of subscribing."
}
```

The React dashboard will communicate with the FastAPI backend through these APIs. The backend will preprocess customer data, load the trained machine learning models, generate predictions or customer segments, and return the results in JSON format.

---

# 8. Repository Plan

```text
bank-customer-intelligence-system/
│
├── dataset/
│   └── bank-full.csv
│
├── notebooks/
│   ├── eda.ipynb
│   ├── classification.ipynb
│   └── clustering.ipynb
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.jsx
│   └── package.json
│
├── backend/
│   ├── api/
│   │   ├── app.py
│   │   ├── predict.py
│   │   └── cluster.py
│   │
│   ├── src/
│   │   ├── preprocess.py
│   │   ├── feature_engineering.py
│   │   ├── train_classification.py
│   │   ├── train_clustering.py
│   │   ├── evaluation.py
│   │   └── utils.py
│   │
│   └── models/
│       ├── classification_model.pkl
│       ├── clustering_model.pkl
│       └── preprocessing_pipeline.pkl
│
├── requirements.txt
├── README.md
└── project_paper.md
```

## Planned Commands

```bash
python backend/src/train_classification.py

python backend/src/train_clustering.py

uvicorn backend.api.app:app --reload
```