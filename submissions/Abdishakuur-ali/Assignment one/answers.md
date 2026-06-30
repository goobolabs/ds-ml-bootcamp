# Research Assignment: Introduction to Data Science and Machine Learning

**Student Name:** Abdishakuur ali daaahir

**Course:** data science and machine learning

**Submission Date:** 16/6/2026

---

# 1. Definition of Data Science and Machine Learning

## What is Data Science?

Data Science is an interdisciplinary field that combines statistics, computer science, mathematics, and domain knowledge to extract useful insights and knowledge from data. It involves collecting, cleaning, analyzing, and interpreting data to support decision-making and solve real-world problems.

## What is Machine Learning?

Machine Learning (ML) is a branch of Artificial Intelligence (AI) that enables computers to learn patterns from data and make predictions or decisions without being explicitly programmed for every task.

## Relationship Between Data Science and Machine Learning

Machine Learning is a subset of Data Science. Data Science covers the entire process of working with data, while Machine Learning focuses on building models that learn from data and make predictions.

## Real-Life Example

An online shopping platform such as Amazon uses Data Science to collect and analyze customer behavior data. Machine Learning algorithms then use this data to recommend products that customers are likely to purchase. Data Science provides the data and analysis, while Machine Learning provides predictive capabilities.

---

# 2. Data Science Lifecycle

The Data Science lifecycle consists of several stages:

| Stage | Description |
|---------|------------|
| Problem Definition | Identify the business or research problem to be solved. |
| Data Collection | Gather relevant data from various sources. |
| Data Cleaning and Preparation | Remove errors, duplicates, and missing values. |
| Exploratory Data Analysis (EDA) | Analyze data patterns and relationships. |
| Model Building | Develop predictive or analytical models. |
| Evaluation | Assess model performance using metrics. |
| Deployment | Implement the model in a real-world environment. |
| Monitoring and Maintenance | Continuously monitor and improve the model. |

## Where Does Machine Learning Fit?

Machine Learning typically fits during the **Model Building** and **Evaluation** stages. At this point, prepared data is used to train algorithms that learn patterns and generate predictions. The model is then evaluated to determine whether it performs effectively on unseen data.

---

# 3. Supervised Learning vs. Unsupervised Learning

## Supervised Learning

Supervised Learning uses labeled data, meaning the correct outputs are already known during training. The algorithm learns the relationship between inputs and outputs.

**Example:** Predicting house prices using historical housing data.

## Unsupervised Learning

Unsupervised Learning uses unlabeled data. The algorithm identifies hidden patterns or structures without predefined outcomes.

**Example:** Customer segmentation in marketing, where customers are grouped according to purchasing behavior.

## Comparison Table

| Feature | Supervised Learning | Unsupervised Learning |
|-----------|-------------------|---------------------|
| Data Type | Labeled Data | Unlabeled Data |
| Goal | Prediction | Pattern Discovery |
| Examples | House Price Prediction, Spam Detection | Customer Segmentation, Market Basket Analysis |
| Output | Known Categories or Values | Hidden Groups or Patterns |

---

# 4. What Causes Overfitting and How Can It Be Prevented?

## Causes of Overfitting

Overfitting occurs when a model learns the training data too well, including noise and random variations, rather than learning general patterns.

Common causes include:

- Using a highly complex model.
- Having too many features.
- Insufficient training data.
- Training the model for too many iterations.
- Lack of regularization.

## Consequences

An overfitted model performs extremely well on training data but poorly on new, unseen data.

## Prevention Methods

### 1. Use More Training Data

Larger datasets help models learn general patterns rather than memorizing specific examples.

### 2. Cross-Validation

Cross-validation evaluates model performance across multiple data splits and improves reliability.

### 3. Regularization Techniques

Methods such as L1 and L2 regularization reduce model complexity and prevent overfitting.

### 4. Feature Selection

Removing irrelevant variables helps the model focus on meaningful patterns.

### 5. Use Simpler Models

Simpler models often generalize better than highly complex ones.

### 6. Early Stopping

Training can be stopped when validation performance starts decreasing.

---

# 5. Training Data and Test Data Split

## What is a Data Split?

Before training a Machine Learning model, data is divided into separate datasets:

- **Training Data:** Used to teach the model.
- **Test Data:** Used to evaluate the model on unseen data.

A common split ratio is:

- 80% Training Data
- 20% Test Data

## Why is Data Splitting Necessary?

Without a test set, it is impossible to determine whether the model has learned useful patterns or simply memorized the training data.

Benefits include:

- Measuring generalization ability.
- Detecting overfitting.
- Providing unbiased performance evaluation.
- Improving model reliability.

## Example

If a dataset contains 10,000 records:

- 8,000 records are used for training.
- 2,000 records are used for testing.

The model is evaluated using the 2,000 unseen records to determine how well it performs in real-world situations.

---

# 6. Case Study: Machine Learning in Healthcare

## Study Title

**Predicting Diabetes Using Machine Learning Algorithms**

## Background

Researchers have applied Machine Learning techniques to healthcare data to predict diabetes at an early stage. One widely cited example uses the Pima Indians Diabetes Dataset.

## Method

Researchers collected patient information such as:

- Age
- Blood glucose level
- Blood pressure
- Body Mass Index (BMI)

Several Machine Learning models, including Logistic Regression and Decision Trees, were trained using this data.

## Findings

The study found that Machine Learning models could successfully identify patients at high risk of developing diabetes with relatively high accuracy. Early prediction enables healthcare professionals to provide preventive treatment and improve patient outcomes.

## Data Science Lifecycle Stages Covered

1. **Problem Definition** – Predict diabetes risk.
2. **Data Collection** – Gather patient health records.
3. **Data Preparation** – Clean and organize medical data.
4. **Model Building** – Train prediction models.
5. **Evaluation** – Measure prediction accuracy.
6. **Deployment** – Use the model in healthcare systems.

## Impact

This application demonstrates how Data Science and Machine Learning can support medical decision-making, reduce healthcare costs, and improve patient care.

---

# References

1. Han, J., Kamber, M., & Pei, J. (2022). *Data Mining: Concepts and Techniques*. Morgan Kaufmann.
2. Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*. O'Reilly Media.
3. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning*. Springer.
4. Provost, F., & Fawcett, T. (2013). *Data Science for Business*. O'Reilly Media.
5. World Health Organization (WHO). Health Data and Digital Health Reports.
6. UCI Machine Learning Repository – Pima Indians Diabetes Dataset.

---