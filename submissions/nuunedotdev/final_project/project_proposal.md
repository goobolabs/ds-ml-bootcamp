# Project Proposal: Predictive Modeling for Medical Insurance Costs

## 0. Certificate Name

- **ABDULKADIR HASSAN IBRAHIM**

## 1. Project Title and Description

**Project Title:** Healthcare Premium Forecasting: Leveraging Patient Demographics and Habits for Insurance Cost Prediction

This project aims to solve the problem of unpredictable and opaque pricing in health insurance premiums. By analyzing historical patient demographic and behavioral profiles, the predictive model uncovers exactly how individual factors like age, smoking habits, and Body Mass Index (BMI) impact financial risk. The primary beneficiaries of this system are health insurance providers, who can automate and standardize their actuarial pricing pipelines, and individual consumers, who gain transparency into how their personal lifestyle choices directly influence their healthcare costs.

---

## 2. Problem Type

**Problem Type:** Regression

The objective of this project is to predict a continuous, real-valued numeric variable: the annual medical insurance cost (`charges`) billed to an individual patient. Because we are estimating a numeric financial amount rather than partitioning users into discrete categories or unlabelled cohorts, this is a supervised machine learning regression task.

---

## 3. Dataset

- **Source:** Kaggle (Medical Cost Personal Datasets)  
  _URL:_ [https://www.kaggle.com/datasets/mirichoi0218/insurance](https://www.kaggle.com/datasets/mirichoi0218/insurance)
- **Size:** 1,338 rows (exceeds the 1,000-row baseline requirement) and 7 distinct features.
- **Target Column:** `charges` — A continuous numeric variable representing the individual medical costs billed by health insurance per annum (measured in USD).

### Main Features:

1.  `age`: Age of the primary beneficiary (Numeric / Integer).
2.  `sex`: Insurance contractor gender, `female` or `male` (Categorical / Nominal).
3.  `bmi`: Body Mass Index, providing an objective index of body weight relative to height ($kg/m^2$), ideally between 18.5 and 24.9 (Numeric / Continuous).
4.  `children`: Number of dependents/children covered by the health insurance plan (Numeric / Integer).
5.  `smoker`: Smoking status of the beneficiary, `yes` or `no` (Categorical / Binary).
6.  `region`: The beneficiary's residential area in the US, divided into four geographic zones: `northeast`, `southeast`, `southwest`, `northwest` (Categorical / Nominal).

---

## 4. Algorithms You Plan to Train

To identify the most accurate and generalizable predictive engine, the following three distinct algorithms will be trained and rigorously benchmarked:

1.  **Multiple Linear Regression (Baseline Model):** This foundational bootcamp algorithm fits a linear equation to the data, serving as an interpretable baseline to measure linear feature relationships against insurance costs.
2.  **Random Forest Regressor:** This ensemble-based bootcamp algorithm constructs multiple decision trees to capture non-linear interactions (such as the combined compounding effect of high BMI paired with a positive smoking status) without overfitting.
3.  **Gradient Boosting Regressor (XGBoost / LightGBM):** This advanced, sequentially trained boosting algorithm will be researched and implemented to optimize prediction errors through gradient descent, handling outliers and structural boundaries within behavioral features efficiently.

---

## 5. Evaluation Plan

To assess and compare model performance, three evaluation metrics will be tracked across validation datasets:

- **Mean Absolute Error (MAE)**
- **Root Mean Squared Error (RMSE)**
- **Coefficient of Determination ($R^2$ Score)**

### Single Definitive Metric:

The best model will be selected based on the **lowest Mean Absolute Error (MAE)**. MAE is chosen because it expresses prediction error directly in the original target currency (USD), making the performance easily interpretable for business stakeholders (e.g., _"On average, our model's premium predictions are off by \$450"_). Unlike RMSE, MAE will not disproportionately penalize rare, unusually high medical bills, ensuring a robust representation of typical premium pricing behavior.

---

## 6. Deployment Sketch

- **Framework:** FastAPI will be utilized due to its native asynchronous support, automatic interactive OpenAPI (`/docs`) documentation generation, and rapid execution speeds.
- **Endpoint:** `/predict` via an HTTP `POST` request.

### Input Format (Accepts JSON Fields):

```json
{
  "age": 28,
  "sex": "male",
  "bmi": 24.5,
  "children": 0,
  "smoker": "no",
  "region": "northwest"
}
```

### Output Format (Returns JSON):

```json
{
  "status": "success",
  "estimated_charges_usd": 4250.75,
  "model_version": "1.0.0"
}
```
