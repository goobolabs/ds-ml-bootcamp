# Final Project Proposal

**Date:** July 2026

---

# 1. Certificate Name

**Nimco NOR Geesey**

---

# 2. Project Title and Description

## Title

**StockSense AI: Smart Inventory Segmentation and Stockout Prediction System**

## Description

Efficient inventory management is essential for retail stores, supermarkets, pharmacies, and warehouses. Many businesses lose revenue because products become out of stock unexpectedly, while other products remain in storage for too long, increasing holding costs and reducing profits. The goal of this project is to build an intelligent inventory management system that combines unsupervised and supervised machine learning techniques. First, K-Means clustering will group products into meaningful inventory behavior segments. Then, classification algorithms will predict whether a product is likely to experience a stockout event. The final system will be deployed using Django REST Framework and will provide predictions through a REST API that can later be integrated with a React dashboard.

---

# 3. Problem Type

This project combines **Unsupervised Learning** and **Supervised Learning**.

* **Unsupervised Learning:** K-Means Clustering will group products into inventory behavior segments such as Fast Moving, Medium Moving, and Slow Moving products.
* **Supervised Learning:** Classification algorithms will predict whether a product is likely to experience a stockout event.

The deployed API will assign a product segment and return the stockout prediction.

---

# 4. Dataset

## Source

Kaggle – High-Dimensional Supply Chain Inventory Dataset

## Dataset Link
https://www.kaggle.com/datasets/ziya07/high-dimensional-supply-chain-inventory-dataset?.com

## Dataset Size

More than 1,000 records.

## Target Column

**Stockout Events** – Indicates whether a product experienced a stockout.

## Main Features

* Inventory Levels – Current inventory available.
* Units Sold – Number of units sold.
* Supplier Lead Times – Number of days suppliers need to deliver products.
* Reorder Points – Inventory level that triggers reordering.
* Reorder Quantities – Number of products reordered.
* Selling Price – Product selling price.
*
## Preprocessing Plan

* Remove duplicate records.
* Handle missing values.
* Encode categorical variables.
* Scale numerical features.
* Perform feature selection.
* Split the dataset into training and testing sets using an 80/20 ratio.

---

# 5. Algorithms I Plan to Train

| Algorithm               | Why it fits                                                                                                       |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **K-Means Clustering**  | Groups products with similar inventory behavior without requiring labels.                                         |
| **Logistic Regression** | Provides a simple and interpretable baseline model for binary classification.                                     |
| **Random Forest**       | Improves prediction accuracy by combining multiple decision trees.                                                |
| **XGBoost**             | A powerful gradient boosting algorithm that often achieves excellent performance on structured business datasets. |

These algorithms satisfy the project requirement of training and comparing at least three different machine learning algorithms.

---

# 6. Evaluation Plan

## Clustering Evaluation

* Silhouette Score
* Davies–Bouldin Index

## Classification Evaluation

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

### Best Model Selection

The best supervised model will be selected using the **highest F1-Score** because it balances Precision and Recall and provides a reliable evaluation for stockout prediction.

---

# 7. Deployment Sketch

## Backend Framework

Django REST Framework

## Prediction Endpoint

**POST /api/predict/**

### Example Input

```json
{
  "inventory_level": 150,
  "units_sold": 60,
  "supplier_lead_time": 5,
  "reorder_point": 100,
  "forecasted_demand": 75
}
```

### Example Output

```json
{
  "cluster": "Fast Moving",
  "prediction": "Stockout",
  "probability": 0.94
}
```

The API will first assign the inventory segment using the trained K-Means model and then use the best-performing classification model to predict stockout events.

---

# 8. Repository Plan

```text
stocksense-ai/
├── dataset/
│   └── inventory.csv
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
├── api/
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── models.py
├── ml_models/
│   ├── kmeans.pkl
│   ├── best_model.pkl
│   └── scaler.pkl
├── frontend/
├── notebooks/
├── README.md
├── requirements.txt
└── project_paper.md
```

This repository structure separates data preprocessing, model training, evaluation, deployment, and documentation, making the project organized and easy to maintain.
