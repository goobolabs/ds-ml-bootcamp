# Data Science & Machine Learning – Assignment Answers

## Q1. Define Data Science and Machine Learning. What is the relationship between them?

### 1.1 What is Data Science?

Data Science is an interdisciplinary field that combines statistics, mathematics, computer science, and domain knowledge to extract meaningful insights and knowledge from structured and unstructured data. It covers the entire data workflow, including data collection, cleaning, analysis, visualization, and decision-making.

### 1.2 What is Machine Learning?

Machine Learning (ML) is a branch of Artificial Intelligence (AI) that enables computers to learn patterns from data and make predictions or decisions without being explicitly programmed for every task. ML algorithms improve automatically through experience.

### 1.3 Relationship Between Data Science and Machine Learning

Machine Learning is a tool used within Data Science. Data Science is the broader field, while ML is one of its most powerful techniques. Not all Data Science projects require Machine Learning, but Machine Learning relies on Data Science processes such as data cleaning, feature engineering, and evaluation.

| Data Science                         | Machine Learning                           |
| ------------------------------------ | ------------------------------------------ |
| Collects and cleans data             | Trains models on clean data                |
| Explores data using statistics       | Learns patterns automatically              |
| Visualizes and communicates findings | Makes predictions on new data              |
| Uses SQL, Python, and BI tools       | Uses Scikit-learn, TensorFlow, and PyTorch |

### 1.4 Real-Life Example: Netflix Recommendation System

Netflix collects millions of data points daily, including viewing history, watch time, ratings, and browsing behavior.

* **Data Collection (DS):** Gather user interaction data.
* **Data Cleaning (DS):** Remove duplicates and incomplete records.
* **Feature Engineering (DS):** Create variables such as genre preference and watch time.
* **Model Training (ML):** Train recommendation models using collaborative filtering.
* **Prediction (ML):** Recommend shows users are likely to enjoy.
* **Evaluation (DS):** Measure recommendation effectiveness through A/B testing.

---

## Q2. Describe the Data Science Lifecycle. Where does Machine Learning fit in?

### 1. Problem Definition

Identify the business problem and define success metrics.

### 2. Data Collection

Gather data from databases, APIs, surveys, sensors, or web scraping.

### 3. Data Cleaning and Preparation

Handle missing values, remove duplicates, correct inconsistencies, and transform variables.

### 4. Exploratory Data Analysis (EDA)

Analyze data using statistics and visualizations to identify patterns, trends, and outliers.

### 5. Modeling (Machine Learning)

Train and tune machine learning models using prepared data. Common algorithms include regression, decision trees, and neural networks.

### 6. Model Evaluation

Measure model performance using metrics such as Accuracy, F1-Score, RMSE, and AUC-ROC.

### 7. Deployment

Deploy the model into production environments and continuously monitor performance.

### Why Does Machine Learning Fit in Stage 5?

Machine Learning belongs in Stage 5 because the data has already been collected, cleaned, and analyzed. ML models require high-quality input data and clearly defined targets to produce reliable results.

---

## Q3. Compare Supervised Learning and Unsupervised Learning, with One Example Each

| Aspect          | Supervised Learning                   | Unsupervised Learning                |
| --------------- | ------------------------------------- | ------------------------------------ |
| Definition      | Learns from labeled data              | Learns from unlabeled data           |
| Labels Required | Yes                                   | No                                   |
| Goal            | Predict known outputs                 | Discover hidden patterns             |
| Types           | Classification, Regression            | Clustering, Dimensionality Reduction |
| Evaluation      | Accuracy, RMSE, F1-Score              | Silhouette Score, Inertia            |
| Algorithms      | Random Forest, SVM, Linear Regression | K-Means, PCA, DBSCAN                 |
| Example         | Email Spam Detection                  | Customer Segmentation                |

### Supervised Learning Example: Email Spam Detection

A model is trained on emails labeled as "spam" or "not spam." It learns patterns such as keyword frequency, sender reputation, and link count. When a new email arrives, the model predicts whether it is spam.

### Unsupervised Learning Example: Customer Segmentation

A retailer uses customer purchase data without labels. A K-Means clustering algorithm groups customers based on spending habits and preferences, identifying segments such as budget shoppers and premium buyers.

---

## Q4. What Causes Overfitting? How Can It Be Prevented?

### 4.1 What is Overfitting?

Overfitting occurs when a model learns the training data too closely, including noise and random variations. As a result, it performs well on training data but poorly on unseen data.

### 4.2 Causes of Overfitting

* Model is too complex.
* Training dataset is too small.
* Too many irrelevant features.
* Excessive training iterations.
* Lack of regularization.

### 4.3 Prevention Techniques

1. Cross-Validation
2. Regularization (L1/Lasso, L2/Ridge)
3. Decision Tree Pruning
4. Dropout (Neural Networks)
5. Early Stopping
6. More Training Data
7. Feature Selection
8. Using Simpler Models

---

## Q5. Explain How Training and Test Data Are Split and Why This Process Is Necessary

### 5.1 Concept

The dataset is divided into separate subsets. The model learns from the training set and is evaluated using the test set, which contains unseen data.

### 5.2 Common Split Ratios

* **80% Training / 20% Testing**
* **70% Training / 30% Testing**
* **60% Training / 20% Validation / 20% Testing**
* **K-Fold Cross-Validation**

### 5.3 Example of an 80/20 Split

**Training Set (80%)**

* Used for learning patterns and training the model.

**Test Set (20%)**

* Used only for evaluating performance.

### 5.4 Why Is This Necessary?

* Prevents data leakage.
* Detects overfitting.
* Simulates real-world performance.
* Enables fair comparison of models.
* Supports proper hyperparameter tuning.

**Important Rule:** The test set must never be used during training or hyperparameter tuning.

---

## Q6. Case Study: Machine Learning Applied in Healthcare

### 6.1 Source

**Title:** A Roadmap to Implementing Machine Learning in Healthcare: From Concept to Practice

**Institution:** SickKids Hospital, Toronto, Canada – PREDICT Program

**Published:** Frontiers in Digital Health / PubMed Central (PMC), 2025

### 6.2 Background

Healthcare organizations face challenges such as data privacy regulations, integration of Electronic Health Records (EHRs), regulatory approval requirements, and the need for explainable AI systems.

### 6.3 The PREDICT Program

The PREDICT (Pediatric Real-world Evaluative Data Sciences for Clinical Transformation) program was launched in 2023 to develop, deploy, evaluate, and maintain machine learning models for pediatric healthcare.

### 6.4 Key Findings and Contributions

#### Data Infrastructure

Created a secure and standardized pipeline for extracting and preprocessing EHR data.

#### MLOps Framework

Implemented automated model retraining, version control, and monitoring.

#### Clinical Integration

Integrated ML models directly into clinical workflows through decision-support systems.

#### Model Examples

Developed models for:

* Sepsis prediction
* Patient deterioration risk prediction
* Medication dosing optimization

#### Evaluation Results

Improved early warning detection and reduced delays in clinical intervention.

### 6.5 Data Science Lifecycle Stages Covered

| Stage              | Covered? | Description                                         |
| ------------------ | -------- | --------------------------------------------------- |
| Problem Definition | Yes      | Identified healthcare problems suitable for ML      |
| Data Collection    | Yes      | Collected EHR data including vitals and lab results |
| Data Cleaning      | Yes      | Standardized and cleaned healthcare data            |
| EDA                | Yes      | Analyzed patterns and predictive features           |
| Modeling           | Yes      | Trained prediction and classification models        |
| Evaluation         | Yes      | Assessed model effectiveness                        |
| Deployment         | Yes      | Integrated models into live clinical systems        |

### Key Takeaway

The PREDICT case study demonstrates the complete Data Science lifecycle in a real healthcare environment. It highlights that successful Machine Learning requires not only accurate models but also strong data infrastructure, workflow integration, continuous monitoring, and a clear problem-focused 825A-3A99