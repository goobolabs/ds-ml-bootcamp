# E-Wallet Service Satisfaction and Recommendation Dataset

**Course:** Data Foundations for Machine Learning  
**Assignment:** Practical Assignment – Lessons 1–3  
**Student:** Abdurahman Aden  
**Date:** June 2026

---

## 1. Title & Collection Method

**Dataset:** User satisfaction and recommendation behavior for E-Wallet services used in Jijiga, Ethiopia.

The dataset focuses on understanding how users perceive different digital financial service platforms such as Telebirr, CBE Birr, E-Birr/Kaafi, and other mobile payment applications. The goal is to identify the factors that influence whether a user recommends an E-Wallet service to others.

Since no publicly available dataset exists that captures local user experiences with these platforms in Jijiga, the data was collected directly through a survey.

### How I Collected the Data

* **Google Forms:** Designed and distributed a structured questionnaire.
* **Social Media Distribution:** Shared the survey through WhatsApp and Telegram groups.
* **Direct Responses:** Collected responses from local users of digital payment services.
* **Manual Verification:** Checked responses for completeness and consistency before cleaning.

Final Dataset Size:

* **Rows:** 50
* **Columns:** 7

---

## 2. Features & Labels

| Feature | Type | Description | Role |
|----------|----------|----------|----------|
| App_Category | Categorical | Type of E-Wallet application used | Feature X |
| Frequency_of_Use | Numeric | Number of times the service is used | Feature X |
| Ease_of_Use | Numeric | User rating (1–5) for usability | Feature X |
| Trans_Speed | Numeric | User rating (1–5) for transaction speed | Feature X |
| Net_Dependency | Numeric | User rating (1–5) for network dependence | Feature X |
| Service_Charges | Numeric | User rating (1–5) for service affordability | Feature X |
| Recommendation | Binary | Whether the user recommends the service (0 = No, 1 = Yes) | Label y |

## Target Variable

`Recommendation`

The machine learning objective is to predict whether a user is likely to recommend an E-Wallet service based on their experience.

---

## 3. Dataset Structure

### Dataset Summary

* Rows: 51
* Columns: 7
* Target Variable: Recommendation
* Problem Type: Classification

---

## 4. Quality Issues

* Missing Values
* Category Inconsistency
* Outliers
* Data Type Issues
* Class Imbalance

---

## 5. Learning Type

### Supervised Learning (Classification)

Predict whether a user will recommend the service.

Possible algorithms:

* Logistic Regression
* Decision Tree
* Random Forest
* Support Vector Machine (SVM)

### Unsupervised Learning

If Recommendation is removed, users can be grouped using:

* K-Means
* Hierarchical Clustering

---

## 6. Use Case & Data Science Lifecycle

### Business Use Cases

* Customer Satisfaction Analysis
* Service Improvement
* Customer Retention
* Market Research

### Data Science Lifecycle

| Stage | Status |
|---------|---------|
| Business Understanding | Understanding drivers of E-Wallet recommendations |
| Data Collection | Completed through survey |
| Data Cleaning | Completed |
| Data Preparation | Encoding and scaling required |
| Exploratory Data Analysis (EDA) | Next Stage |
| Feature Engineering | Create Satisfaction Score and Loyalty Score |
| Modeling | Classification Models |
| Evaluation | Accuracy, Precision, Recall, F1-Score |
| Deployment | Recommendation Prediction System |

---

## Feature Engineering Opportunities

### Satisfaction Score

```text
(Ease_of_Use + Trans_Speed + Service_Charges) / 3
```

### Loyalty Score

```text
Frequency_of_Use × Satisfaction Score
```

### Technical Dependency Score

```text
Net_Dependency
```

---

## Files

```text
cleaned_survey_Respones.csv
assignment.md
```

---

## Notes

The dataset was collected from users of E-Wallet services in Jijiga, Ethiopia. Because the dataset contains only 50 observations, the results should be interpreted as exploratory rather than representative of all users in Ethiopia.
