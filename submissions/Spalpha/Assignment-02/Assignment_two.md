# Evaluating Islamic Banking Financing and Youth Employment Outcomes in Hargeisa

This repository contains the dataset and documentation evaluating the impact of Sharia-compliant financing structures on youth entrepreneurship and employment outcomes across district hubs in Hargeisa, Somaliland.

---

## 1. Title & Collection Method

### Title
Evaluating the Impact of Sharia-Compliant Financing on Youth Entrepreneurship and Employment in Hargeisa

### Collection Method
The data was collected through a structured field survey targeting young entrepreneurs and unemployed youth aged 18 to 35 within Hargeisa. The primary sampling framework leveraged institutional records from local microfinance institutions (MFIs), commercial banks, and community youth centers. Responses were gathered electronically to monitor demographic profiles, capital injections, operational timelines, and final venture status.

---

## 2. Description of Features & Labels

The dataset maps predictive features ($X$) against a primary employment classification target ($y$).

### Feature Space (Predictive Variables $X$)
* [cite_start]**ID**: Unique identifier assigned to each participant (to be dropped during model training).
* [cite_start]**Age**: Continuous numeric variable representing the participant's age (18 to 35).
* [cite_start]**Education_Level**: Categorical variable indicating academic attainment (e.g., High School, Diploma, Bachelor, Master).
* **Financing_Product**: Categorical variable representing the sharia-compliant contract deployed (e.g., Murabahah, Mudarabah, Musharakah, Qard al-Hasan).
* **Funding_Amount_USD**: Continuous numeric variable denoting the total capital facility allocated in US Dollars.
* [cite_start]**Business_Duration_Months**: Continuous numeric variable capturing the operational lifetime of the venture.
* [cite_start]**Training_Received**: Categorical flag detailing if the applicant received supplementary business development or financial literacy training.

### Target Variable (Label $y$)
* [cite_start]**Employment_Status**: Categorical label indicating the final economic outcome: either **Sustained Startup** (the venture succeeded and maintained employment) or **Unemployed**.

---

## 3. Dataset Structure

[cite_start]The dataset contains **54 rows** and **8 columns**.

### Data Sample (Rows 1–10)
| ID | Age | Education_Level | Financing_Product | Funding_Amount_USD | Business_Duration_Months | Training_Received | Employment_Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 24 | Bachelor | Murabahah | 3500.0 | 14.0 | Yes | Sustained Startup |
| 2 | 19 | High School | *[Null]* | 0.0 | 0.0 | No | Unemployed |
| 3 | 28 | Master | Mudarabah | 12000.0 | 24.0 | Yes | Sustained Startup |
| 4 | 22 | Diploma | Qard al-Hasan | 1500.0 | 8.0 | No | Sustained Startup |
| 5 | 31 | Bachelor | Murabahah | *[Null]* | 18.0 | Yes | Sustained Startup |
| 6 | 26 | Bachelor | Murabahah | 4500.0 | 3.0 | No | Unemployed |
| 7 | 23 | Bacehlor | Mudarabah | 5000.0 | 11.0 | Missing | Sustained Startup |
| 8 | 20 | Diploma | *[Null]* | 0.0 | 0.0 | No | Unemployed |
| 9 | 35 | Master | Murabahah | 15000.0 | 36.0 | Yes | Sustained Startup |
| 10 | 25 | Bachelor | Murbaha | 4000.0 | 12.0 | Yes | Sustained Startup |

---

## 4. Data Quality Issues

An inspection of the raw dataset reveals several anomalies requiring preprocessing:
* [cite_start]**Structural Typographical Errors (Typos)**: `Education_Level` contains the typo `"Bacehlor"` (e.g., ID 7, 21), and `Financing_Product` contains `"Murbaha"` (e.g., ID 10, 31), which need standardization.
* **Missing System Values**: Structural blanks exist in `Financing_Product` for individuals who did not receive funding (e.g., ID 2, 8).
* **Numerical Data Gaps**: Continuous variables contain empty fields; [cite_start]`Funding_Amount_USD` is missing for IDs 5 and 28, while `Business_Duration_Months` is missing for IDs 18 and 46.
* [cite_start]**Placeholder String Errors**: The `Training_Received` feature contains string literals labeled `"Missing"` instead of structural nulls or standard binary markers (e.g., ID 7, 19).

---

## 5. Learning Type & Use Case

### Learning Type
[cite_start]This dataset requires a **supervised learning** approach because it contains a explicitly defined, predetermined target label (`Employment_Status`) to guide algorithmic optimization.

### Machine Learning Use Case
* [cite_start]**Task Type**: Binary Classification.
* **Objective**: Predict whether a youth financing applicant will achieve a **Sustained Startup** or remain **Unemployed** based on their demographic profile, educational baseline, and proposed financing structure.
* **Data Science Lifecycle Fit**: Currently in the **Data Cleaning & Preprocessing** stage. [cite_start]Addressing the quality defects (imputing missing entries, correcting structural typos, and encoding categorical strings) is the direct prerequisite before shifting into Exploratory Data Analysis (EDA) and Model Training.