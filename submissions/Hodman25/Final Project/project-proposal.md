# 1. Certificate Name:
**Hodan Maxamed Ibraahim**

# 2. Project Title and Description

## Project Title

**Water Quality and Potability Prediction System**

## Description

Access to clean and safe drinking water is essential for public health. However, determining whether water is safe to drink often requires laboratory testing, which can be costly and time-consuming. This project aims to develop a machine learning classification model that predicts whether a water sample is potable (safe to drink) or not potable based on its physical and chemical properties. The system can help environmental agencies, water treatment facilities, researchers, and communities make faster and more informed decisions about water quality.



# 3. Problem Type

## Classification

This project is a **classification** problem because the model predicts one of two categories:

- **1 = Potable (Safe to Drink)**
- **0 = Not Potable (Unsafe to Drink)**

The final model will classify each water sample into one of these two classes.



# 4. Dataset

## Dataset Source

- **Source:** Kaggle
- **Dataset:** Water Potability Dataset
- **Link:** https://www.kaggle.com/datasets/uom190346a/water-quality-and-potability
## Dataset Size

- **Rows:** 3,276
- **Columns:** 10 (9 features + 1 target)

## Target Column

**Potability**

- **1:** Water is safe to drink.
- **0:** Water is not safe to drink.

## Main Features

| Feature | Description |
|----------|-------------|
| pH | The pH level of the water. |
| Hardness | Water hardness, a measure of mineral content. |
| Solids |Total dissolved solids in the water. |
| Chloramines | Chloramines concentration in the water. |
| Sulfate |Sulfate concentration in the water. |
| Conductivity | Electrical conductivity of the water |
| Organic_carbon | Organic carbon content in the water.|
| Trihalomethanes | Trihalomethanes concentration in the water. |
| Turbidity | Turbidity level, a measure of water clarity. |



# 5. Algorithms You Plan to Train

## 1. Logistic Regression

Logistic Regression will serve as a baseline classification model because it is simple, fast, and performs well for binary classification problems.

## 2. Support Vector Machine (SVM)

 SVM plots water parameters in a multi-dimensional space and finds the optimum boundary that separates potable from non-potable water samples. It is highly effective when working with well-defined, continuous variables.

## 3. Random Forest Classifier

Random Forest combines multiple decision trees to improve prediction accuracy, reduce overfitting, and generally provides strong performance on structured datasets.

## XGBoost Classifier
A boosting algorithm that improves prediction performance by learning complex patterns from multiple decision trees.

# 6. Evaluation Plan

The following evaluation metrics will be used to compare all models:

- Accuracy
- Precision
- Recall
- F1-Score

## Best Model Selection

The final model will be selected based on the **F1-Score** because the dataset is slightly imbalanced. F1-Score balances precision and recall, making it a better overall measure than accuracy alone for this classification problem.


# 7. Deployment Sketch

## Framework

**FastAPI**

## `/predict` Endpoint

The API will accept a JSON request like the following:

```json
{
  "ph": 7.2,
  "Hardness": 205.5,
  "Solids": 18000,
  "Chloramines": 7.1,
  "Sulfate": 330.0,
  "Conductivity": 420.5,
  "Organic_carbon": 14.5,
  "Trihalomethanes": 68.2,
  "Turbidity": 3.8
}
```

### Response

```json
{
  "prediction": "Potable",
  "probability": 0.94
}
```

The API will return the predicted class (Potable or Not Potable) together with the prediction probability.

---

## 8. Repository Plan

```text
water-quality-potability-prediction/
│
├── data/
│   ├── raw/                      # Original dataset (water_potability.csv)
│   └── processed/                # Cleaned, scaled, and split datasets
│
├── notebooks/                    # Exploratory Data Analysis (EDA) and experiments
│   ├── 01_EDA_and_Preprocessing.ipynb
│   └── 02_Model_Training.ipynb
│
├── src/                          # Machine Learning source code
│   ├── data_processing.py        # Data cleaning, imputation, scaling, encoding
│   ├── train.py                  # Train machine learning models
│   ├── evaluate.py               # Model evaluation and metrics
│   └── utils.py                  # Helper functions
│
├── api/                          # FastAPI backend
│   ├── app.py                    # Main FastAPI application
│   ├── routes.py                 # API endpoints
│   ├── schemas.py                # Request and response models
│   └── requirements.txt          # Backend dependencies
│
├── frontend/                     # React + Vite frontend
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/             # API calls to FastAPI
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   ├── vite.config.js
│   └── README.md
│
├── models/                       # Trained models (.pkl)
│   └── best_model.pkl
│
├── README.md                     # Project overview and setup guide
├── requirements.txt              # Python dependencies
└── project_paper.md              # Final project report
```
