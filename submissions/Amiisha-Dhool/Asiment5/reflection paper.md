 Loan Approval Prediction – Reflection Paper

1. Introduction

In this assignment, I implemented a machine learning project to predict whether a loan application will be approved or rejected based on applicant financial and personal data. The goal was to reproduce the Lesson 5 preprocessing pipeline and build classification models to analyze loan approval decisions.

-
 2. What I Implemented

I completed the full machine learning workflow in two main parts:

Part B1 – Data Preprocessing
- Loaded the raw dataset (`raw_loan_dataset.csv`)
- Cleaned inconsistent data (e.g., currency symbols like $, commas, and mixed text values)
- Standardized categorical values (Yes/No, y/n, approved/rejected variations)
- Handled missing values using:
  - Median for numerical columns
  - Mode for categorical columns
- Removed duplicate rows
- Handled outliers using IQR capping
- Encoded categorical variables into numerical format (0 and 1)
- Created new features:
  - DebtToIncome
  - IncomePerYearEmployed
- Applied feature scaling using **RobustScaler**
- Saved cleaned dataset as `clean_loan_dataset.csv`



 Part B2 – Model Training and Prediction

I used the cleaned dataset to build and evaluate three classification models:

 3. Models Used

 1. Logistic Regression
- A linear classification model that uses probability to predict outcomes.
- Used as a baseline model for comparison.
- Parameters: `max_iter=1000, random_state=42`


2. Random Forest Classifier
- An ensemble learning method that builds multiple decision trees.
- Final prediction is made using majority voting.
- Parameters: `n_estimators=100, random_state=42`
- Usually performs better on complex datasets.



 3. K-Nearest Neighbors (KNN)
- A distance-based algorithm that classifies data based on the closest neighbors.
- Parameter: `n_neighbors=5`
- Used as the third model for comparison.



 4. Model Evaluation

All models were evaluated using the following metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

These metrics helped measure how well each model predicts loan approval correctly.



5. Sanity Check

A single test sample from the dataset was used to compare predictions from all three models against the actual label. This helped understand how each model behaves on real examples.



 6. Key Learnings

From this assignment, I learned:

- Data preprocessing is the most important step in machine learning
- Real-world data is often messy and requires cleaning before modeling
- Feature engineering improves model performance
- Different models give different results depending on the data structure
- Random Forest is generally more accurate for this type of dataset compared to Logistic Regression and KNN



 7. Conclusion

This project helped me understand the full machine learning pipeline from raw data to prediction. I successfully implemented preprocessing, trained multiple models, and evaluated their performance. Random Forest performed the best overall in this case, but each model provided useful insights. 