# Data Foundations for Machine Learning: Mogadishu Flight Ticket Prices Dataset

* **Prepared by:** [Hanaan bashir dahir / GitHub Username:xanaa-ayan]
* **Due Date:** June 20, 2026
* **Course:** Data Science & Machine Learning Bootcamp (Assignment Two)

---

## 1. Title & Collection Method

* **Title of Dataset:** Mogadishu Flight Ticket Prices Dataset
* **Collection Method:** This dataset was compiled using **Manual Observation and Logging** (Manual Data Collection). 
* **Data Sources:** The data was gathered by checking local airline booking portals, official social media pages (Facebook), and travel agency price sheets operating within Mogadishu, Somalia[cite: 37]. Prices reflect flights departing from **Aden Adde International Airport (MGQ)** to key domestic and international destinations.

---

## 2. Description of Features & Labels

To build a machine learning model that predicts ticket prices, the dataset is structured with the following variables:

### Features ($X$)
* **Airline (Categorical):** The operating airline company (e.g., Daallo, Freedom, Salaama, Qatar Airways, Ethiopian Airlines).
* **Destination (Categorical):** The arrival airport city (e.g., Hargeisa, Garowe, Nairobi, Istanbul, Addis Ababa).
* **Class (Categorical):** The seating tier, representing travel comfort level (Economy or Business)[cite: 41].
* **Days_Before_Flight (Numerical):** The exact number of days remaining between the booking date and the actual flight departure date.

### Label ($y$)
* **Price (Numerical):** The cost of the flight ticket in USD ($)[cite: 43]. This is the continuous target variable we want our model to predict.

---

## 3. Dataset Structure & Sample Table

The complete dataset consists of **50 rows** (samples) and **5 columns** (variables)[cite: 45]. Below is the complete data table logged for future preprocessing steps:

| Airline | Destination | Class | Days_Before_Flight | Price |
| :--- | :--- | :--- | :---: | :---: |
| Daallo | Hargeisa | Economy | 12 | 190 |
| Freedom | Nairobi | Economy | 5 | 320 |
| Salaama | Garowe | Business | 14 | 350 |
| Daallo | Nairobi | Business | 2 | 550 |
| Freedom | Hargeisa | Economy | 20 | 165 |
| Missing | Istanbul | Economy | 25 | 780 |
| Salaama | Garowe | economy | 7 | 220 |
| Qatar Airways | Istanbul | Business | 4 | 1450 |
| Daallo | Hargeisa | Economy | 12 | 190 |
| Freedom | Nairobi | Economy | -3 | 310 |
| Ethiopian Airlines | Addis Ababa | Economy | 15 | 420 |
| Qatar Airways | Nairobi | Business | 10 | 1200 |
| Salaama | Garowe | Economy | 8 | 210 |
| Daallo | Mogadishu | Economy | 1 | 150 |
| Freedom | Nairobi | Business | 6 | 480 |
| Ethiopian Airlines | Istanbul | Economy | 30 | 750 |
| Missing | Hargeisa | Business | 11 | 310 |
| Salaama | Garowe | Economy | 14 | 250 |
| Daallo | Nairobi | Economy | 9 | 290 |
| Qatar Airways | Istanbul | Economy | 18 | 850 |
| Freedom | Hargeisa | economy | 5 | 185 |

---

## 4. Quality Issues (Anomalies Located)

Because this data was logged manually from live, changing booking channels, it mimics real-world data friction. The following data quality issues were intentionally preserved or found:

* **Missing Values:** Some entries lack the airline name (labeled as `Missing`), representing skipped inputs during fast manual collection.
* **Inconsistent Casing/Typos:** The `Class` column contains structural text discrepancies, such as lowercase `economy` instead of standard capitalized `Economy`.
* **Duplicate Rows:** Identical flight entries appear multiple times (e.g., Daallo flights to Hargeisa at row 1 and row 9), which can bias model training.
* **Outliers / Logical Errors:** The `Days_Before_Flight` feature contains negative values (e.g., `-3`, `-5`), which is a logical physical impossibility for advance booking.

---

## 5. Learning Type


This is a **Supervised Learning** problem.

> **Justification:**
> The dataset contains a definitive, explicit target output label ($y$) which is the **Price**[cite: 61]. The objective is to train a machine learning algorithm by feeding it the historical input features ($X$: Airline, Destination, Class, Days Before Flight) along with the corresponding correct outputs ($y$), so it learns the mapping function to predict ticket pricing for completely new, unseen booking parameters.

---

## 6. Use Case & Data Science Lifecycle

* **Machine Learning Use Case:** This dataset fits a **Regression** task because the target label (Price) is a continuous numeric value, not a distinct categorical group.
* **Placement in the Data Science Lifecycle:** This assignment represents the **Data Collection** stage (Phase 2).

```text
[Problem Definition] ➔ [Data Collection] ➔ [Data Preprocessing] ➔ [EDA] ➔ [Modeling]
                             ▲
                     (Current Stage)