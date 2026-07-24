# Automated Healthcare Insurance Cost Estimation Using Machine Learning

**Authors:** ML Engineering & Research Team  
**Date:** July 2026  
**Document Version:** 1.0  
**Target Domain:** Applied Predictive Healthcare Analytics & Web Deployment  

---

## Executive Summary

Medical insurance pricing traditionally relies on general statistical tables that often struggle to capture how different health factors interact with each other. This project presents an automated machine learning system built to predict annual individual medical insurance costs based on personal attributes like age, health index, and smoking habits.

We built and compared three different models:
1. **Multiple Linear Regression** (Standard Statistical Baseline)
2. **Random Forest Regressor** (Decision Tree Ensemble)
3. **XGBoost Regressor** (Advanced Gradient Boosting)

The complete project includes automatic data preparation, continuous model training, a lightweight prediction web server built with **FastAPI**, and a simple interactive web dashboard created with **React.js** and **Tailwind CSS**.

---

## 1. Introduction

Accurate prediction of individual medical costs helps both insurance providers and patients plan financially. Unplanned medical expenses are a leading cause of individual financial stress. By analyzing historical medical bills, machine learning models can identify complex patterns—such as how smoking combined with a high Body Mass Index (BMI) drastically increases medical costs—far better than simple traditional calculators.

### 1.1 Key Goals
* Build an automated data pipeline that prepares raw data for prediction without human errors.
* Train and compare three machine learning models under identical test conditions.
* Save the winning trained model so it can be used instantly by web applications.
* Create a fast web API using FastAPI to handle incoming user requests.
* Build a clear, user-friendly React dashboard where anyone can type in their details and get a cost estimate.

---

## 2. Dataset Overview

The system runs on a healthcare dataset containing 1,338 individual records with 7 key details:

| Field Name | Description | Type | Examples / Range |
|---|---|---|---|
| `age` | Age of the primary beneficiary | Number | 18 to 64 years |
| `sex` | Gender of the policyholder | Category | Female, Male |
| `bmi` | Body Mass Index (weight to height ratio) | Number | 15.9 to 53.1 |
| `children` | Number of dependent children covered | Number | 0 to 5 children |
| `smoker` | Regular tobacco user status | Category | Yes, No |
| `region` | Residential location in the United States | Category | Southwest, Southeast, Northwest, Northeast |
| `charges` | **Annual medical cost billed (Target)** | Number | $1,121 to $63,770 |

---

## 3. How Data Preparation Works

Before feeding information to machine learning models, raw data must be cleaned and converted into numbers the computer can understand.

```text
                  Raw User Input Data
                          │
         ┌────────────────┴────────────────┐
         ▼                                 ▼
   Numeric Values                  Categorical Text
['age', 'bmi', 'children']    ['sex', 'smoker', 'region']
         │                                 │
         ▼                                 ▼
 Scaled to Standard Range     Converted to Binary Flags (0s & 1s)
         │                                 │
         └────────────────┬────────────────┘
                          ▼
            Final Cleaned Data Matrix
```

### 3.1 Plain Language Data Steps
1. **Number Standardization:** Numbers like `age` (18–64) and `bmi` (15–53) are measured on different scales. Standardizing rescales all numbers so large values don't overwhelm smaller ones during learning.
2. **Category Encoding:** Machine learning models cannot directly process words like `"yes"`, `"female"`, or `"southwest"`. These are converted into binary flags (0s and 1s). For instance, a smoker becomes `1` and a non-smoker becomes `0`.
3. **Train-Test Split:** $80\%$ of the data is used to train the models, while $20\%$ is hidden away as a final test to ensure the models aren't just memorizing answers.

---

## 4. Comparing the Machine Learning Models

Three models were trained on the exact same dataset and evaluated on how close their dollar predictions were to real insurance bills.

### 4.1 Evaluation Metrics Explained
* **Average Dollar Error (MAE):** The average difference in dollars between the model's prediction and the real medical bill. **Lower is better.**
* **Large Error Penalty (RMSE):** Measures overall error while punishing big individual mistakes extra heavily. **Lower is better.**
* **Accuracy Percentage ($R^2$ Score):** Shows what percentage of the price variations the model successfully explains. **Higher is better (1.0 is 100%).**

### 4.2 Model Performance Summary

| Model Tested | Average Dollar Error (MAE) | Large Error Score (RMSE) | Accuracy Score ($R^2$) | Winner Status |
|---|---|---|---|---|
| **Linear Regression** | $\$4,181.19$ | $\$5,796.28$ | $78.3\%$ | Baseline Model |
| **Random Forest** | $\$2,534.20$ | $\$4,582.10$ | $86.4\%$ | Second Place |
| **XGBoost Regressor** | **$\$2,412.35$** | **$\$4,320.15$** | **$87.9\%$** | **SELECTED WINNER** |

### 4.3 Main Insights
* **Smoking is the Largest Cost Driver:** Smoking habits had by far the biggest impact on total cost. When combined with a high BMI, insurance estimates increased drastically by $\$15,000$ to $\$30,000$ per year.
* **XGBoost Won:** XGBoost came out on top with the lowest average error ($\$2,412.35$) and highest overall accuracy ($87.9\%$). It outperformed basic linear regression by over $42\%$ because it naturally detects complex real-world health conditions.

---

## 5. System Design & Web Architecture

The full application is divided into two separate, connected parts: a backend API and a frontend dashboard.

```text
┌────────────────────────────────────────────────────────┐
│                   React Dashboard                      │
│      User fills form and clicks "Estimate Cost"        │
└───────────────────────────┬────────────────────────────┘
                            │ HTTP Request
                            ▼
┌────────────────────────────────────────────────────────┐
│                   FastAPI Server                       │
│    Receives input, checks fields, formats data         │
└───────────────────────────┬────────────────────────────┘
                            │ Processed Data
                            ▼
┌────────────────────────────────────────────────────────┐
│                  XGBoost Model Pipeline                │
│    Transforms features & calculates dollar estimate    │
└───────────────────────────┬────────────────────────────┘
                            │ Prediction Result
                            ▼
┌────────────────────────────────────────────────────────┐
│         User sees estimated premium on screen          │
└────────────────────────────────────────────────────────┘
```

---

## 6. Frontend Web Dashboard Features

The web client provides an intuitive form for entering patient information:

* **Simple Inputs:** Easy controls for Age, BMI, Dependents, Gender, Smoker status, and US Region.
* **Instant Calculation:** Displays formatted prediction results (e.g., `$4,150.25`) immediately upon form submission.
* **Clear Feedback:** Displays clear, helpful messages if the web server is offline or unreachable.

---

## 7. How to Run the Project

### 7.1 Run the Backend API
1. Open your terminal in the project folder.
2. Install Python packages:
   ```bash
   pip install pandas numpy scikit-learn xgboost joblib fastapi uvicorn pydantic
   ```
3. Train the model:
   ```bash
   python src/train.py
   ```
4. Start the backend server:
   ```bash
   python api/app.py
   ```

### 7.2 Run the React Web App
1. Open a second terminal window in the `frontend` folder.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the dashboard:
   ```bash
   npm run dev
   ```
4. Open `http://localhost:5173` in your web browser.

---

## 8. Conclusion

This project successfully turns raw medical data into an automated prediction tool. By replacing static statistical formulas with an **XGBoost** model connected to a **FastAPI** backend and **React** frontend, users get quick, accurate, and easy-to-understand health insurance estimates.
