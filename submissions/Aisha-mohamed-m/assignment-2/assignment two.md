# Loan Approval Prediction Dataset Report

## 1. Introduction

This project focuses on predicting whether a loan application will be approved or rejected using Machine Learning techniques. A dataset was created to represent loan applicants and their financial information. The goal is to identify the factors that influence loan approval decisions and build a predictive model.


## 2. Dataset Description

The dataset contains 50 records (samples) and 5 features (attributes). Each record represents a loan applicant.

### Features

 Feature           Description   
 Monthly_Income    Applicant's monthly income in USD                      
 Employment_Years  Number of years the applicant has been employed        
 Credit_Score      Creditworthiness score of the applicant                
 Existing_Loans    Number of active loans currently held by the applicant 
 Loan_Amount       Amount of money requested as a loan                    

### Label
 Label          Description                                                    

 Loan_Approved |Indicates whether the loan was approved (Yes) or rejected (No) 

---

## 3. Data Collection Method|

The dataset was collected using a questionnaire distributed to individuals who had previously applied for loans. The questionnaire gathered information regarding income, employment history, credit score, existing loans, loan amount requested, and loan approval status.

The collected responses were organized into a structured dataset suitable for Machine Learning analysis.



## 4. Dataset Characteristics

 Total Samples: 50
 Total Features: 5
 Label: Loan_Approved
 Learning Type: Supervised Learning

The dataset is balanced, containing an equal number of approved and rejected loan applications. This balance helps prevent bias during model training and improves prediction performance.



## 5. Importance of Features

### Monthly Income

Monthly income reflects the applicant's ability to repay a loan. Applicants with higher incomes are generally more likely to receive loan approval.

### Employment Years

Employment history indicates financial stability. Individuals with longer employment records are often considered lower-risk borrowers.

### Credit Score

Credit score measures the applicant's creditworthiness. A higher credit score increases the probability of loan approval.

### Existing Loans

This feature shows the number of active loans already held by the applicant. Applicants with many existing loans may be considered higher risk.

### Loan Amount

The requested loan amount influences approval decisions. Larger loan requests may require stronger financial qualifications.

---

## 6. Data Quality Issues

Several data quality issues may occur in real-world datasets:

1. Missing Values

   .Some applicants may not provide complete information.

2. Duplicate Records

    The same applicant may appear multiple times.

3. Incorrect Values

    Negative income values or unrealistic credit scores.

4. Outliers

    Extremely high loan amounts or incomes compared to the rest of the dataset.

These issues should be addressed during the data cleaning stage.





The trained model can assist banks and financial institutions in making faster and more consistent loan approval decisions.

---

## 8. Conclusion

The Loan Approval Prediction dataset is a structured and balanced dataset designed for supervised learning tasks. By analyzing financial and employment-related information, Machine Learning models can predict loan approval outcomes and support decision-making processes in the banking sector.











 
