# Data Science and Machine Learning – Assignment

---


## 1. Data Science and Machine Learning

**Data Science** is the process of collecting, cleaning, and analyzing data to help make decisions.

**Machine Learning (ML)** is a part of Data Science that allows computers to learn from data and make predictions.

### Relationship
Machine Learning is one tool used inside Data Science to build predictive models.

### Example  
A supermarket in Mogadishu collects sales data to understand which products sell most during Ramadan.  
Then a Machine Learning system predicts what customers will likely buy next year.

---

## 2. Data Science Lifecycle

- **Problem Definition** – Identify the problem to solve (e.g., predict bus passengers).
- **Data Collection** – Gather data (sales, users, passengers).
- **Data Preparation** – Clean and organize data.
- **Modeling** – Apply Machine Learning to learn patterns.
- **Evaluation** – Test how accurate the model is.
- **Deployment** – Use the model in real life.

### Where Machine Learning is used
Machine Learning is mainly used in the **Modeling stage**, because this is where the system learns patterns and makes predictions.

---

## 3. Supervised vs Unsupervised Learning

### Supervised Learning
- Uses labeled data (input + correct answer)

### Example:
- **Disease diagnosis:**  
  A model learns from patient records labeled as **“Diseased” or “Healthy”** and predicts whether a new patient has a disease based on symptoms, age, and test results.

---

### Unsupervised Learning
- Uses unlabeled data (no correct answer given)

### Example:
- Grouping mobile users based on usage patterns.

---

## 4. Overfitting

Overfitting happens when a model learns the training data too well, including noise, and performs poorly on new data.

### Example
A model learns last year’s weather patterns exactly (including unusual storms).  
When new weather data comes, it fails to predict correctly because it memorized old patterns too closely.

### Causes
- Small dataset
- Too complex model
- Too much training

### Prevention
- Use more data
- Simplify model
- Use test data
- Apply regularization

---

## 5. Training Data vs Test Data

- **Training Data:** Used to teach the model (e.g., 80%)
- **Test Data:** Used to check performance (e.g., 20%)

### Why split data?
To make sure the model can work well on new unseen data, not just memorized data.

### Example
A system is built to predict whether it will rain in Mogadishu.

Out of 1000 weather records:
- 800 records (Training Data): The model learns patterns like temperature, humidity, and wind.
- 200 records (Test Data): The model is tested on new weather data it has never seen before.

---

## 6. Case Study: Diabetes Prediction Using Machine Learning

A research study used Machine Learning to predict diabetes risk based on patient health data.

### Data Used:
- Age  
- BMI  
- Blood sugar level  
- Blood pressure  

### What Was Done:
- Data collected and cleaned  
- Machine Learning models trained  
- Models tested for accuracy  

### Results:
- ML models can predict diabetes early  
- Helps doctors identify high-risk patients faster  

### Lifecycle Stages Used:
- Problem Definition  
- Data Collection  
- Data Preparation  
- Modeling  
- Evaluation  

---

## References

- Kopitar, L. et al. (2020).  
  *Early detection of type 2 diabetes mellitus using machine learning-based prediction models*  
  https://www.nature.com/articles/s41598-020-68771-z  

- Rizwan, M. et al. (2021).
Rainfall Prediction Using Machine Learning Techniques
This study applies machine learning models to predict rainfall based on weather variables such as temperature, humidity, and atmospheric pressure. It shows how ML can improve short-term weather forecasting accuracy.

🔗 https://arxiv.org/abs/2105.04547 

- Patro, K. K. et al. (2023).  
  *Diabetes prediction using machine learning approaches*  
  https://link.springer.com/article/10.1186/s12859-023-05488-6  
