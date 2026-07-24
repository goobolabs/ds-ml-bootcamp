# Socioeconomic Class Prediction via Machine Learning: Evaluating Supervised Classification Algorithms on Adult Census Income Data

**Author:** Rahma Mohamud Abdi  
**Date:** July 2026  
**Project Repository:** `census_adult_income/`

---

## Abstract

Predicting individual income tiers using demographic, socio-economic, and employment characteristics is a foundational problem in applied machine learning and social data science. This paper evaluates three distinct supervised machine learning algorithms—Logistic Regression, Random Forest, and XGBoost—on the 1994 Adult Census Income dataset containing 48,842 instances. We implement an end-to-end preprocessing pipeline incorporating median numeric imputation, standard scaling, and one-hot encoding for categorical variables. Due to substantial class imbalance (approximately 75.9% earning $50,000 or less versus 24.1% earning more than $50,000), models were optimized and evaluated using the macro and class-specific F1-Score alongside Accuracy, Precision, and Recall. The XGBoost Classifier achieved superior overall performance with an Accuracy of 87.12% and an F1-Score of 0.7066 on the holdout test set. The winning pipeline was containerized and served as an asynchronous microservice REST API using FastAPI.

---

## 1. Introduction & Motivation

Understanding the structural drivers of income inequality and socio-economic classification is critical for public policy design, targeted social welfare distribution, and credit risk assessment. Microfinance institutions and non-governmental organizations (NGOs) often rely on demographic attributes to infer creditworthiness or target community assistance programs when verified financial documentation is unavailable.

The primary objective of this study is to formulate a binary classification model that accurately predicts whether an individual earns more than $50,000 annually based on census data.

### Research Questions
1. How do linear baseline models perform relative to non-linear tree ensembles on high-dimensional demographic tabular datasets?
2. How effectively does feature preprocessing (scaling, imputation, and categorical encoding) mitigate data leakage and handle class imbalance?
3. Can a complex ensemble model be deployed efficiently via a microservice architecture for real-time inference?

---

## 2. Dataset Profile & Preprocessing Strategy

### 2.1 Dataset Description
The model was constructed using the Adult Census Income Dataset sourced from the UCI Machine Learning Repository and Kaggle. The dataset consists of 48,842 records combining training and evaluation partitions.

* **Target Variable:** Income status (Categorical: Greater than 50K or Less than or equal to 50K).
* **Feature Space:** 14 demographic and financial attributes:
  * *Continuous (5):* Age, education level number, capital gain, capital loss, and weekly working hours.
  * *Categorical (8):* Workclass, education degree, marital status, occupation, relationship, race, sex, and native country.
  * *Excluded (1):* Final sampling weight (`fnlwgt`), which was removed due to a lack of predictive relevance across general demographic sub-populations.

### 2.2 Data Sanitization & Cleaning
1. **Token Standardization:** Replaced missing structural string tokens (question mark symbols) with explicit null values.
2. **Whitespace Stripping:** Trimmed leading and trailing whitespaces across all textual data columns.
3. **Column Normalization:** Standardized column naming conventions into lowercase format using underscores to ensure seamless compatibility with API request payloads.

### 2.3 Feature Transformation Pipeline
To ensure strict isolation between training and test sets and eliminate data leakage, all transformations were encapsulated within a automated feature pipeline:

* **Numeric Sub-Pipeline:** Missing continuous values were filled using median imputation to resist extreme skewness, followed by standard z-score normalization.
* **Categorical Sub-Pipeline:** Missing categorical labels were imputed using the most frequent category (mode), then transformed into sparse binary vectors through One-Hot Encoding.

---

## 3. Algorithm Methodology

Three distinct machine learning paradigms were trained and evaluated on an identical 80/20 stratified train-test split (39,073 training samples and 9,769 testing samples).

### 3.1 Logistic Regression (Linear Baseline)
Logistic Regression models the probability of an outcome using a linear combination of input features mapped through a logistic function.
* **Rationale:** Provides a fast, interpretable benchmark for high-dimensional one-hot encoded input spaces.
* **Configuration:** Configured with a maximum iteration limit of 1,000 using L-BFGS optimization.

### 3.2 Random Forest Classifier (Bagging Ensemble)
Random Forest builds an ensemble of multiple independent decision trees trained on bootstrap samples of the training data, aggregating individual predictions through majority voting.
* **Rationale:** Highly effective at handling non-linear interactions and heavily skewed continuous features (such as capital gain) without requiring complex transformations.
* **Configuration:** Built using 100 decision trees running in parallel.

### 3.3 XGBoost Classifier (Gradient Boosting)
XGBoost constructs decision trees sequentially, where each new tree focuses on correcting the prediction errors made by the prior trees.
* **Rationale:** Optimized gradient tree-boosting consistently delivers high predictive accuracy on tabular data through fine-grained error correction and built-in regularization against overfitting.
* **Configuration:** Configured with 100 boosting iterations, a learning rate of 0.1, a maximum depth of 6 splits per tree, and log-loss evaluation tracking.

---

## 4. Empirical Results & Model Selection

### 4.1 Comparative Metric Analysis
Models were evaluated across four standard classification metrics on the holdout test set:

| Model Architecture | Accuracy | Precision | Recall | F1-Score |
| :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression** | 84.21% | 70.11% | 60.23% | 0.6479 |
| **Random Forest** | 85.41% | 72.91% | 61.90% | 0.6696 |
| **XGBoost (Champion)** | **87.12%** | **76.14%** | **65.91%** | **0.7066** |

### 4.2 Decision Rule Justification
The **F1-Score** was designated as the primary selection metric prior to evaluation. Because the dataset exhibits significant class imbalance (approximately three-quarters of the population earns $50,000 or less), a simple majority-class model would achieve over 75% accuracy while failing entirely to identify high-income individuals.

XGBoost achieved the highest F1-score (0.7066), outperforming Random Forest by 3.70% and Logistic Regression by 5.87%.

### 4.3 Operational Sanity Checks
Validation checks were executed on three unseen test profiles using the serialized champion model to confirm real-world performance:

* **Profile #1 (High Capital Gain):** Age 38, Bachelor's degree level, Executive-Managerial role, Capital Gain of $15,024  
  $\rightarrow$ **Prediction:** Greater than $50K (94.2% confidence) | **Match:** Correct
* **Profile #2 (Entry-Level Worker):** Age 21, High School level, Service role, Zero Capital Gain  
  $\rightarrow$ **Prediction:** Less than or equal to $50K (97.9% confidence) | **Match:** Correct
* **Profile #3 (Mid-Career Specialist):** Age 45, Master's degree level, Professional Specialist role, Zero Capital Gain  
  $\rightarrow$ **Prediction:** Greater than $50K (68.5% confidence) | **Match:** Correct

---

## 5. Deployment Architecture

The winning XGBoost pipeline (including preprocessing transformers and trained model parameters) was serialized into a unified binary artifact.

```text
[ React Client UI ]
        │
        │ HTTP POST (JSON Payload)
        ▼
[ FastAPI Backend ] ──> Loads Model Artifact
        │
        ├── Step 1: Preprocess Features (Impute + Scale + One-Hot)
        ├── Step 2: XGBoost Probability Calculation
        ▼
[ JSON Prediction Response ]
```



## 6. Lessons Learned & Future Work

### 6.1 Key Insights
* **Pipeline Encapsulation:** Combining preprocessing transformers and estimators into a single, unified pipeline prevents data leakage during training and eliminates input format mismatch errors during live API inference.
* **Feature Impact:** Financial markers (capital gain and capital loss) alongside marital status proved to be the strongest overall indicators of earning over $50,000 annually.

### 6.2 Limitations & Future Improvements
* **Class Imbalance Mitigation:** Future iterations will explore synthetic oversampling techniques or custom class-weight adjustments to further boost detection of high-income individuals.
* **Automated Tuning:** Automated hyperparameter optimization frameworks could yield incremental performance gains for the gradient-boosted model.

---

## 7. Conclusion

This project successfully developed, evaluated, and deployed an end-to-end machine learning solution for adult income classification. XGBoost proved to be the superior algorithm, achieving an F1-Score of **0.7066** and an Accuracy of **87.12%**. The deployed FastAPI microservice and React frontend demonstrate a production-ready application suitable for real-world socio-economic analysis.



## URL REPO

https://github.com/rahma-88/census_adult_income