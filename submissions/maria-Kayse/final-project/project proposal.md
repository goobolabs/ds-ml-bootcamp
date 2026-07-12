# Project Proposal — Hotel Booking Cancellation Prediction Using Machine Learning

**Date:** July 2026  

## 1. Certificate Name

**Maryan Ahmed Warsame**

---

# 2. Project Title and Description

## Title:
**Hotel Booking Cancellation Prediction Using Machine Learning**

## Description:

Hotels receive thousands of booking requests every year, and a significant number of reservations are canceled. These cancellations can negatively affect hotel revenue, resource planning, and customer management.

This project aims to develop a machine learning system that predicts whether a hotel booking will be canceled or not based on customer information, booking details, and reservation characteristics.

The project will apply **supervised machine learning algorithms** to predict booking cancellations and **unsupervised learning techniques** to discover customer booking behavior patterns.

---

# 3. Problem Type

This project includes both supervised and unsupervised learning approaches.

| Learning Type | Problem Type | Goal |
|---|---|---|
| Supervised Learning | Binary Classification | Predict whether a booking will be canceled or not |
| Unsupervised Learning | Clustering | Discover groups of customers with similar booking behaviors |

## Target Column:

**Target Variable:** `is_canceled`

| Value | Meaning |
|---|---|
| 0 | Not Canceled |
| 1 | Canceled |

---

# 4. Dataset

## Dataset Information

**Dataset Name:** Hotel Booking Demand Dataset  

**Source:** Kaggle  

Dataset Link:  
https://www.kaggle.com/datasets/pattae/hotel-booking-demand-datasets

| Information | Details |
|---|---|
| Number of Rows | 119,390 |
| Number of Columns | 32 |
| Data Type | Structured Tabular Data |
| Target Variable | is_canceled |

---

# Main Features

The dataset contains different types of information:

| Category | Examples |
|---|---|
| Customer Details | adults, children, country, customer type |
| Booking Details | lead_time, stay duration, arrival information |
| Hotel Details | hotel, meal, reserved_room_type |
| Previous History | previous_cancellations, previous_bookings_not_canceled |
| Financial Information | adr, deposit_type |

---

# 5. Data Preprocessing Plan

Before training machine learning models, the dataset will be cleaned and prepared through the following steps:

| Step | Description |
|---|---|
| Data Inspection | Analyze dataset structure, columns, and data types |
| Missing Values Handling | Identify and handle missing values |
| Duplicate Removal | Remove duplicated records to improve data quality |
| Outlier Handling | Detect and manage extreme values |
| Feature Selection | Select the 15 most important features to reduce complexity and improve model performance |
| Encoding | Convert categorical variables into numerical format using One-Hot Encoding |
| Scaling | Normalize numerical features before model training |

## Encoding Method

**One-Hot Encoding** will be used because most categorical variables in the dataset do not have a natural order.

---

# 6. Machine Learning Algorithms

## Classification Models

The following supervised learning algorithms will be trained and compared:

| Algorithm | Reason for Selection |
|---|---|
| Logistic Regression | Provides a baseline model for binary classification and is easy to interpret |
| Random Forest Classifier | Handles complex relationships, reduces overfitting, and works well with structured data |
| XGBoost Classifier | A powerful boosting algorithm that provides high accuracy and handles complex patterns efficiently |

---

## Clustering Models

Unsupervised learning will also be applied to analyze customer booking behaviors.

| Algorithm | Purpose |
|---|---|
| K-Means Clustering | Groups customers based on similarities in booking patterns |
| Agglomerative Clustering | Creates hierarchical customer groups |

---

# 7. Evaluation Plan

## Classification Evaluation Metrics

The classification models will be evaluated using:

| Metric | Purpose |
|---|---|
| Accuracy | Measures overall prediction performance |
| Precision | Measures correct cancellation predictions |
| Recall | Measures how well the model detects actual cancellations |
| F1-Score | Provides balance between precision and recall |
| Confusion Matrix | Shows correct and incorrect predictions |
| ROC-AUC | Measures the model's ability to distinguish between classes |

**The best classification model will be selected based on the F1-score because detecting cancellations correctly is the main objective.**

---

## Clustering Evaluation Metrics

The clustering models will be evaluated using:

- Elbow Method
- Silhouette Score

---

# 8. Deployment Plan

The best-performing model can be deployed using **FastAPI**.

The API will receive booking information as input and return:

- Cancellation prediction
- Prediction probability

## Example Input:

```json
{
  "hotel": "City Hotel",
  "lead_time": 120,
  "adults": 2,
  "adr": 150
}
```
## Example Output

The API will return the prediction result together with the probability score.

```json
{
  "prediction": "Canceled",
  "probability": 0.82
}
```

The API will load the best trained model from `models/best_model.pkl` and use the saved preprocessing pipeline to transform new booking information before making predictions.

---

# 9. Repository Plan

```text
hotel-booking-ml-project/
├── dataset/
│   └── hotel_bookings.csv
├── notebooks/
│   ├── 01_data_cleaning_eda.ipynb
│   └── 02_model_training.ipynb
├── src/
│   ├── preprocess.py
│   └── train.py
├── api/
│   └── app.py
├── models/
│   └── best_model.pkl
├── reports/
│   └── project_report.pdf
├── README.md
├── project_proposal.md
└── requirements.txt
```

---

# Run Commands (Planned)

Train the machine learning models, compare their performance, and save the best model.

```bash
python src/train.py
```

Start the FastAPI application locally.

```bash
uvicorn api.app:app --reload
```



