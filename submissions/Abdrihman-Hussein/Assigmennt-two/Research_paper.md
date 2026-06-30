# Predicting Customer Payment Status Using Invoice Data

## Project Overview

This project applies Machine Learning concepts to predict customer payment behavior based on invoice data. The goal is to determine whether a customer will pay an invoice **on time** or **delay the payment** using historical business transaction data.

This is a **Supervised Machine Learning classification problem**.

---

## Problem Statement

Businesses often face delays in customer payments, which affects cash flow and planning.
This project aims to build a model that can predict payment status using invoice-related features.

---

## Dataset Description

* **Total Samples:** 50 invoices
* **Features:** 5
* **Label:** 1

Each row represents one invoice transaction.

### Features (X)

* Customer Type
* Amount ($)
* Payment Term
* Month
* Number of Items

### Label (y)

* Payment Status

  * Paid On-Time
  * Delayed

> Invoice ID is used only as an identifier and not as a model feature.

---

## Sample Data

| Invoice ID | Customer Type | Amount ($) | Payment Term   | Month | Number of Items | Payment Status |
| ---------- | ------------- | ---------- | -------------- | ----- | --------------- | -------------- |
| INV-001    | Wholesale     | 500        | Net 30         | Jan   | 8               | Paid On-Time   |
| INV-002    | Retail        | 60         | Due on Receipt | Jan   | 2               | Paid On-Time   |
| INV-003    | Wholesale     | 1200       | Net 30         | Jan   | 15              | Delayed        |

---

## Machine Learning Type

* **Type:** Supervised Learning
* **Task:** Classification

The model learns from labeled data and predicts whether a new invoice will be paid on time or delayed.

---

## Data Quality Notes

The dataset is generally clean but may include:

* Minor inconsistencies in categorical formatting
* Different feature scales (requires scaling)
* Encoding required for categorical variables

These issues will be handled during preprocessing.

---

## Use Case

This model can be used to:

* Predict late payments
* Improve cash flow management
* Identify risky customers
* Support business decision-making

---

## Data Science Workflow

1. Problem Definition
2. Data Collection
3. Data Understanding
4. Data Preprocessing
5. Feature Engineering
6. Model Training
7. Model Evaluation
8. Deployment 

---

## Conclusion

This project demonstrates how invoice data can be used to predict customer payment behavior using Machine Learning. The dataset contains 50 samples and is suitable for a supervised classification problem.

Future work includes data preprocessing and model building.
