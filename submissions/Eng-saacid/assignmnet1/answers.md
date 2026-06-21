# Research Assignment: Introduction to Data Science and Machine Learning

---

## 1. Data Science and Machine Learning

### Data Science

Data Science is the process of collecting, analyzing, and interpreting data to gain useful insights.

> **Analogy:** Data Science is like managing an entire hospital. It involves collecting patient information, organizing medical records, analyzing health data, and supporting healthcare decisions.

### Machine Learning

Machine Learning (ML) is a branch of AI that allows computers to learn from data and make predictions.

> **Analogy:** Machine Learning is like a doctor who learns from previous patient cases and uses that knowledge to predict diseases or recommend treatments.

### Relationship Between Data Science and Machine Learning

|       | Data Science               | Machine Learning      |
| ----- | -------------------------- | --------------------- |
| Scope | Broad field                | Part of Data Science  |
| Goal  | Understand data            | Make predictions      |
| Uses  | Analysis and visualization | Algorithms and models |

> **Analogy:** If Data Science is the entire hospital, Machine Learning is one department within the hospital that specializes in making predictions.

### Real-Life Example – Healthcare

| Step                 | Who Does It      | What Happens                               |
| -------------------- | ---------------- | ------------------------------------------ |
| Collect patient data | Data Science     | Gather patient records and medical history |
| Prepare data         | Data Science     | Clean and organize healthcare data         |
| Train model          | Machine Learning | Learn patterns from patient information    |
| Predict disease risk | Machine Learning | Estimate the likelihood of diseases        |
| Check results        | Data Science     | Measure prediction accuracy                |

---

## 2. Data Science Lifecycle

Machine Learning is mainly used in **Step 6**.

1. Define the Problem
2. Collect Data
3. Clean Data
4. Analyze Data
5. Prepare Features
6. Build ML Model
7. Evaluate Model
8. Deploy Solution
9. Monitor Results

### Why ML Fits Here

* Data must be prepared first.
* ML learns from clean data.
* Results are evaluated after training.

> **Analogy:** Building an ML model is like diagnosing a patient. Before making a diagnosis, doctors must first collect and examine medical information.

> ML is one stage within the Data Science process.

---

## 3. Supervised vs Unsupervised Learning

### Supervised Learning

Uses labeled data.

**Example:**
Predicting whether a patient has a disease based on previous medical records.

> **Analogy:** A doctor learns from past patient cases that already have confirmed diagnoses.

### Unsupervised Learning

Uses unlabeled data.

**Example:**
Grouping patients based on similar symptoms or health conditions.

> **Analogy:** Researchers analyze patient data and naturally identify groups with similar characteristics without predefined labels.

### Comparison

|         | Supervised Learning | Unsupervised Learning |
| ------- | ------------------- | --------------------- |
| Labels  | Yes                 | No                    |
| Goal    | Predict outcomes    | Find patterns         |
| Data    | Labeled             | Unlabeled             |
| Example | Disease Prediction  | Patient Grouping      |

> Supervised learning predicts, while unsupervised learning discovers patterns.

---

## 4. Overfitting

### What is Overfitting?

Overfitting happens when a model performs well on training data but poorly on new data.

> **Analogy:** A student memorizes answers from past exams instead of understanding the subject. The student scores well on familiar questions but struggles with new ones.

### Causes

* Small datasets
* Complex models
* Too much training

### Prevention Methods

* Use more data
* Simplify the model
* Apply cross-validation

### Summary

| Problem     | Result                       |
| ----------- | ---------------------------- |
| Overfitting | Poor performance on new data |

> A good model should work well on unseen data.

---

## 5. Training Data and Test Data

Data is usually divided into two parts.

| Dataset       | Purpose         | Split |
| ------------- | --------------- | ----- |
| Training Data | Train the model | 80%   |
| Test Data     | Test the model  | 20%   |

### Why Split Data?

* Check model performance
* Detect overfitting
* Ensure fair evaluation

### Example

For 1,000 records:

* Training Data = 800
* Test Data = 200

> **Analogy:** Training data is like study material used before an exam, while test data is the final exam used to measure actual understanding.

> Training data teaches the model, while test data evaluates it.

---

## 6. Case Study – Machine Learning in Healthcare

### Title

Disease Prediction Using Machine Learning

### Objective

Predict diseases using historical patient data and medical records.

### What They Did

* Collected patient health records
* Cleaned the data
* Applied machine learning algorithms
* Evaluated prediction accuracy

### Findings

* Models predicted diseases effectively
* Healthcare providers could identify high-risk patients earlier
* Hospitals could improve medical decision-making

### Lifecycle Coverage

| Lifecycle Stage    | Covered               |
| ------------------ | --------------------- |
| Problem Definition | Yes                   |
| Data Collection    | Yes                   |
| Data Cleaning      | Yes                   |
| Data Exploration   | Yes                   |
| Model Building     | Yes                   |
| Model Evaluation   | Yes                   |
| Deployment         | Possible in hospitals |

> This case study shows how ML can support healthcare and medical decision-making.

---

## References

1. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning* (2nd ed.). Springer. Available at: https://www.statlearning.com/

2. UCI Machine Learning Repository. (n.d.). *Machine Learning Datasets*. University of California, Irvine. Available at: https://archive.ics.uci.edu/

3. Scikit-learn Developers. (n.d.). *Scikit-learn Documentation*. Available at: https://scikit-learn.org/stable/

4. TensorFlow Team. (n.d.). *TensorFlow Documentation*. Available at: https://www.tensorflow.org/

5. The Hospital for Sick Children. (2025). *A Roadmap to Implementing Machine Learning in Healthcare: From Concept to Practice*. *Frontiers in Digital Health*. Available at: https://pmc.ncbi.nlm.nih.gov/articles/PMC11788154/
