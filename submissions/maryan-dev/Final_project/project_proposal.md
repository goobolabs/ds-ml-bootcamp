# Project Proposal


**Date:** July 2026

---

# 1. Certificate Name

**Maryan Mohamed Adam**

---

# 2. Project Title and Description

## Title

**Machine Learning-Based Problematic Internet Use Prediction and User Behavior Clustering**

Problematic Internet Use (PIU) has become an increasing concern among children and adolescents because excessive internet use can negatively affect mental health, sleep quality, physical activity, and academic performance. This project aims to build a machine learning model that predicts the severity of problematic internet use using demographic, behavioral, and psychological assessment data. In addition to prediction, clustering techniques will be used to discover hidden groups of users with similar internet usage behaviors. The final deliverable will be a REST API that accepts user information as JSON and returns the predicted PIU severity with a confidence score.

---

# 3. Problem Type

This project combines both **Classification** and **Clustering**.

## Classification (Supervised Learning)

The target column is **`sii`**, which represents the severity of Problematic Internet Use with four classes:

* None
* Mild
* Moderate
* Severe

## Clustering (Unsupervised Learning)

Clustering will be used to identify hidden groups of children with similar internet usage behaviors without using the target label.

---

# 4. Dataset

* **Source:** Kaggle – Child Mind Institute: Problematic Internet Use

  https://www.kaggle.com/datasets/akirahoimancheng/child-mind-institute-problematic-internet-use

* **Dataset Size:** Approximately **3,960 training records** with more than **80 features**.

* **Target Column:** `sii` – Severity level of Problematic Internet Use.

* **Main Features**

  * Age
  * Sex
  * BMI
  * Sleep Duration
  * Physical Activity
  * Screen Time
  * Internet Usage
  * CGAS Score
  * PCIAT Assessment Scores

## Preprocessing Plan

* Handle missing values using appropriate imputation techniques.
* Remove unnecessary columns.
* Encode categorical variables.
* Scale numerical features.

---

# Algorithms I Plan to Train

| # | Algorithm                     | Type         | Why it fits                                                                         |
| - | ----------------------------- | ------------ | ----------------------------------------------------------------------------------- |
| 1 | **Logistic Regression**       | Supervised   | A simple and interpretable baseline model for multiclass classification.            |
| 2 | **K-Nearest Neighbors (KNN)** | Supervised   | A distance-based algorithm that classifies samples using their nearest neighbors.   |
| 3 | **Decision Tree**             | Supervised   | Captures nonlinear relationships and produces easy-to-understand decision rules.    |
| 4 | **Random Forest**             | Supervised   | Improves prediction accuracy, reduces overfitting, and provides feature importance. |
| 5 | **XGBoost**                   | Supervised   | A powerful boosting algorithm that performs well on structured tabular datasets.    |
| 6 | **K-Means Clustering**        | Unsupervised | Discovers hidden groups of users with similar internet usage behaviors.             |
| 7 | **Hierarchical Clustering**   | Unsupervised | Provides an alternative clustering approach for comparing user segments.            |

The project will compare multiple supervised learning algorithms to identify the best classification model for predicting Problematic Internet Use (PIU). In addition, two unsupervised learning algorithms will be used to discover hidden behavioral groups and compare clustering performance.

---

# 6. Evaluation Plan

## Classification Metrics

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

The best classification model will be selected using the **F1-Score** because the dataset contains multiple target classes with an imbalanced distribution.

## Clustering Metrics

* Silhouette Score
* Davies–Bouldin Index

The best clustering model will be selected using the highest **Silhouette Score** and the lowest **Davies–Bouldin Index**.

---

# 7. Deployment Sketch

* **Framework:** FastAPI
* **Endpoint:** `POST /predict`

## Input JSON Example

```json
{
  "Age": 13,
  "Sex": "Male",
  "BMI": 20.8,
  "Sleep_Duration": 8,
  "Physical_Activity": 4,
  "Screen_Time": 5,
  "Internet_Usage": 6,
  "CGAS_Score": 72
}
```

## Output JSON Example

```json
{
  "prediction": "Moderate",
  "probability": 0.91
}
```

The API will load the trained model from `models/best_model.pkl`, apply the same preprocessing pipeline used during training, and return the predicted PIU severity with its confidence score.

---

# 8. Repository Plan

```text
child-mind-piu-prediction/
├── dataset/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_supervised.ipynb
│   └── 04_unsupervised.ipynb
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   └── clustering.py
├── api/
│   └── app.py
├── models/
│   ├── best_model.pkl
│   └── scaler.pkl
├── README.md
├── requirements.txt
└── project_paper.md
```

## Planned Commands

```bash
python src/train.py

uvicorn api.app:app --reload
```

---

# Expected Outcome

The final project will develop a machine learning application capable of predicting the severity of Problematic Internet Use while also identifying hidden behavioral groups through clustering. Multiple supervised learning algorithms will be compared to select the best predictive model, while clustering algorithms will provide additional insights into children's internet usage patterns. The final solution will be deployed as a FastAPI REST API capable of returning prediction results and confidence scores from user-provided data.
