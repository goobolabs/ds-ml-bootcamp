
#  StockSense AI

## Intelligent Inventory Management and Stockout Prediction System

**StockSense AI** is a full-stack machine learning application developed as the final capstone project for the Goobo Labs Data Science & Machine Learning Bootcamp.

The system helps businesses manage inventory more efficiently by combining **K-Means Clustering** and **Machine Learning Classification** to categorize inventory and predict stockout risks before they occur.

---

## Project Overview

StockSense AI performs two main tasks:

###  Inventory Categorization

The system uses **K-Means Clustering** to automatically classify inventory into:

-  Fast Moving
-  Medium Moving
-  Slow Moving

This helps businesses understand product movement patterns and improve inventory planning.

---

###  Stockout Prediction

The system predicts whether a product is at risk of running out of stock using multiple machine learning algorithms.

Algorithms trained:

- Logistic Regression
- Random Forest
- XGBoost

The best-performing model is saved as **best_model.pkl** and used during prediction.

---

##  Dataset

- **Dataset:** Custom Supply Chain Inventory Dataset
- **Rows:** 5,000+
- **Target Variable:** Stockout_Flag

Main Features:

- Inventory_Level
- Units_Sold
- Supplier_Lead_Time_Days
- Reorder_Point
- Order_Quantity
- Unit_Price
- Demand_Forecast

---

## Model Evaluation

### K-Means Clustering

| Metric | Result |
|---------|--------|
| Silhouette Score | **0.4768** |
| Davies-Bouldin Score | **0.8682** |

### Classification Models

| Model | Accuracy |
|--------|----------|
| Logistic Regression | **81.3%** |
| Random Forest | **81.3%** |
| XGBoost | **80.1%** |

---

## Technologies Used

### Backend

- Python
- Django
- Django REST Framework
- MySQL
- Joblib

### Frontend

- React
- Tailwind CSS
- Axios
- Recharts
- Framer Motion

### Machine Learning

- Scikit-learn
- XGBoost
- Pandas
- NumPy

---

##  Features

- Inventory Dashboard
- CSV Upload
- Inventory Categorization
- Stockout Prediction
- Prediction History
- Analytics Dashboard
- Interactive Charts
- JWT Authentication
- Responsive Design

---

##  Project Structure

```text
stocksense-ai/
│
├── backend/
├── frontend/
├── dataset/
├── models/
├── src/
├── requirements.txt
└── README.md
```

---

## ▶️ Run the Project

### Backend

```bash
python manage.py runserver
```

### Frontend

```bash
npm install

npm run dev
```

---

## 📌 GitHub Repository

**Repository Link:**

https://github.com/nimco-nuur/stocksense-ai/tree/main/final_project_ds-ml-main


---

## Developer

**Name:**  Nimco Nor gesey

Goobo Labs Data Science & Machine Learning Bootcamp

Final Capstone Project

July 2026
````





