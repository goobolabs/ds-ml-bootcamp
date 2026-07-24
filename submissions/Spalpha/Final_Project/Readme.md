# Bank Loan Approval & Creditworthiness Predictor 🏦📊

## 🔗 Repo Link
https://github.com/Spalpha/ds-ml-bootcamp.git


---
An automated End-to-End Machine Learning workflow designed to assess the creditworthiness of loan applicants. This system predicts whether a loan application should be **Approved** or **Rejected** based on financial and asset attributes, helping financial institutions mitigate risks and speed up processing times.

---

## 📁 Folder Contents
This repository/folder contains the complete capstone project setup:
* **project-proposal.md** – The approved project plan, detailing the problem statement, dataset, algorithms, and evaluation metrics.
* **README.md** – This file, providing a short summary, technical overview, and implementation steps.

---

## 📁 Repository Structure

```text
bank-loan-predictor/
├── dataset/
│   ├── loan_approval_dataset.csv       # Raw data from Kaggle (4,269 rows)
│   └── clean_loan_dataset.csv          # Preprocessed data ready for ML
├── notebooks/
│   └── exploratory_analysis.ipynb      # EDA and Data Visualization
├── src/
│   ├── preprocess.py                   # Data cleaning, scaling, and encoding
│   └── train.py                        # Model training and evaluation script
├── api/
│   └── app.py                          # FastAPI application implementation
├── models/
│   └── best_loan_model.pkl             # Serialized best performing model
├── README.md                           # Project documentation (This file)
└── project_paper.md                    # Detailed project report
```