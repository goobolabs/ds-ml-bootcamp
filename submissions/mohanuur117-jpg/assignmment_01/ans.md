# DATA SCIENCE & MACHINE LEARNING: A RESEARCH-ORIENTED STUDY

## 1. Data Science and Machine Learning: Definitions and Relationship

**Data Science** is an interdisciplinary field that combines statistics, computer science, domain expertise, and data engineering to extract meaningful insights and knowledge from structured and unstructured data.

**Machine Learning (ML)** is a sub-discipline of artificial intelligence in which algorithms are trained on data to learn patterns and make predictions or decisions without being explicitly programmed for each task.

### Relationship

Machine Learning is one of the most powerful tools within Data Science. Data Science provides the broader framework—problem definition, data gathering, preprocessing, and communication of results—while ML is applied at the modeling and prediction stage.

### Real-Life Example: Netflix Recommendation System

Netflix collects massive amounts of user interaction data such as viewing history, ratings, and watch time. Data scientists prepare and process this data, while machine learning models predict what users are likely to watch next.

---

## 2. The Data Science Lifecycle

1. **Problem Definition**
2. **Data Collection**
3. **Data Cleaning & Preprocessing**
4. **Exploratory Data Analysis (EDA)**
5. **Modeling (Machine Learning)**
6. **Evaluation**
7. **Deployment**
8. **Monitoring**

### Where Does ML Fit?

Machine Learning primarily fits in the **Modeling** stage, while also influencing Evaluation, Deployment, and Monitoring.

---

## 3. Supervised Learning vs. Unsupervised Learning

| Feature    | Supervised Learning    | Unsupervised Learning |
| ---------- | ---------------------- | --------------------- |
| Labels     | Required               | Not Required          |
| Goal       | Predict Outputs        | Discover Patterns     |
| Examples   | Spam Detection         | Customer Segmentation |
| Algorithms | Linear Regression, SVM | K-Means, PCA          |

---

## 4. Overfitting: Causes and Prevention

### Causes

* Complex models
* Small datasets
* Excessive training
* Noisy data

### Prevention

* Cross-validation
* Regularization (L1/L2)
* Dropout
* Early stopping
* More training data
* Pruning

---

## 5. Training Data and Test Data Split

* **Training Set (70–80%)**
* **Validation Set (10–15%)**
* **Test Set (20–30%)**

The test set provides an unbiased estimate of model performance on unseen data.

---

## 6. Case Study: Early Detection of Diabetic Retinopathy

Researchers trained a deep learning model using retinal images to detect diabetic retinopathy.

### Results

* Sensitivity: 97.5%
* Specificity: 93.4%

This demonstrates how machine learning can support healthcare professionals and improve early disease detection.

---

# References

* Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*.
* Donoho, D. (2017). *50 Years of Data Science*.
* Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*.
* Mitchell, T. M. (1997). *Machine Learning*.
* Provost, F., & Fawcett, T. (2013). *Data Science for Business*.
