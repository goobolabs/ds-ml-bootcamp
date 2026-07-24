
# Final Project Proposal – StockSense AI

**Date:** July 2026

---

# 1. Certificate Name

**Nimco Nor Gesey*



---

# 2. Project Title and Description

## Title

**StockSense AI – Intelligent Inventory Management and Stockout Prediction System**

## Description

Inventory management is one of the most important challenges for businesses because running out of stock can lead to lost sales and customer dissatisfaction, while overstocking increases storage costs. This project develops an intelligent inventory management system that combines machine learning and a modern web application to help businesses classify inventory and predict stockout risks.

The system first uses **K-Means Clustering** to group inventory into **Fast Moving**, **Medium Moving**, and **Slow Moving** categories. It then trains multiple classification algorithms to predict whether a product is at risk of stockout. The best-performing model is deployed as a web application using **Django REST Framework**, **React**, and **MySQL**

---

# 3. Problem Type

This project combines **Unsupervised Learning** and **Supervised Learning**.

### Unsupervised Learning

**Algorithm:** K-Means Clustering

Purpose:

* Group inventory into Fast Moving, Medium Moving, and Slow Moving categories.

Output:

* Inventory Category
* Cluster Number

### Supervised Learning

**Problem Type:** Binary Classification

Target Variable:

`Stockout_Flag`

Output Classes:

* Stockout Risk
* No Stockout Risk

---

# 4. Dataset

**Source:** Custom Supply Chain Inventory Dataset

**Size:** Approximately **5,000 inventory records**.

**Target Variable:**

`Stockout_Flag`

### Main Features

* Inventory_Level
* Units_Sold
* Supplier_Lead_Time_Days
* Reorder_Point
* Order_Quantity
* Unit_Price
* Demand_Forecast
* Stockout_Flag

### Preprocessing Plan

* Validate dataset
* Handle missing values
* Scale numerical features using StandardScaler
* Perform train/test split (80/20)
* Generate inventory clusters using K-Means

---

# 5. Algorithms Trained

| # | Algorithm           | Purpose                  |
| - | ------------------- | ------------------------ |
| 1 | K-Means Clustering  | Inventory Categorization |
| 2 | Logistic Regression | Stockout Prediction      |
| 3 | Random Forest       | Stockout Prediction      |
| 4 | XGBoost             | Stockout Prediction      |

The project trains multiple classification models and compares their performance. The best-performing model is saved as `best_model.pkl` for deployment.

---

# 6. Evaluation Plan and Results

## K-Means Clustering Metrics

| Metric               | Result     |
| -------------------- | ---------- |
| Silhouette Score     | **0.4768** |
| Davies-Bouldin Score | **0.8682** |

### Cluster Distribution

| Inventory Category | Products |
| ------------------ | -------- |
| Fast Moving        | 1666     |
| Medium Moving      | 1667     |
| Slow Moving        | 1667     |

---

## Classification Metrics

The following models were evaluated on the same test dataset.

| Model               |  Accuracy | Precision |    Recall |  F1-Score |   ROC AUC |
| ------------------- | --------: | --------: | --------: | --------: | --------: |
| Logistic Regression | **0.813** | **0.979** |     0.640 | **0.774** |     0.807 |
| Random Forest       | **0.813** | **0.979** |     0.640 | **0.774** | **0.810** |
| XGBoost             |     0.801 |     0.919 | **0.660** |     0.768 |     0.805 |

The best-performing model is selected and saved as **best_model.pkl** for deployment.

---

# 7. Deployment Plan

### Backend

* Django
* Django REST Framework
* JWT Authentication
* MySQL
* Joblib

### Frontend

* React
* Tailwind CSS
* Axios
* Recharts
* Framer Motion

### Machine Learning Models

The application loads the following trained models:

* scaler.pkl
* kmeans_model.pkl
* logistic_regression.pkl
* random_forest.pkl
* xgboost.pkl
* best_model.pkl

The models are used only for inference and are never retrained during deployment.

### Main API Endpoints

| Endpoint              | Description                 |
| --------------------- | --------------------------- | |
| POST /api/run-kmeans/ | Run inventory clustering    |
| POST /api/predict/    | Predict stockout risk       |
| GET /api/dashboard/   | Display analytics dashboard |

### Prediction Input Example

```json
{
  "Inventory_Level": 120,
  "Units_Sold": 45,
  "Supplier_Lead_Time_Days": 5,
  "Reorder_Point": 30,
  "Order_Quantity": 60,
  "Unit_Price": 15,
  "Demand_Forecast": 55
}
```

### Prediction Output Example

```json
{
  "prediction": "Stockout Risk",
  "confidence": 94.3,
  "cluster": 2,
  "inventory_category": "Fast Moving",
  "recommendation": "Reorder immediately. High demand is expected."
}
```

---

# 8. Repository Plan

```text
stocksense-ai/

├── dataset/
│   ├── inventory_dataset.csv
│   ├── clean_inventory_dataset.csv
│   └── clustered_inventory_dataset.csv
│
├── models/
│   ├── scaler.pkl
│   ├── kmeans_model.pkl
│   ├── logistic_regression.pkl
│   ├── random_forest.pkl
│   ├── xgboost.pkl
│   └── best_model.pkl
│
├── src/
│   ├── 01_data_preprocessing.py
│   ├── 02_kmeans_clustering.py
│   └── 03_stockout_prediction.py
│
├── backend/
│
├── frontend/
│
├── requirements.txt
├── README.md
└── project_paper.md
```

### Planned Commands

```bash
python src/01_data_preprocessing.py

python src/02_kmeans_clustering.py

python src/03_stockout_prediction.py

python manage.py runserver

npm install

npm run dev
```



