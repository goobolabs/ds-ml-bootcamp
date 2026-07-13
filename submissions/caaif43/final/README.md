# Student Academic Performance Prediction System

## Project Overview

The **Student Academic Performance Prediction System** is a machine learning project that predicts whether a student is likely to **Pass** or **Fail** based on academic, demographic, and personal information.

The project demonstrates the complete machine learning workflow, including data preprocessing, model training, evaluation, comparison of multiple algorithms, and deployment using **FastAPI**.

---

# Objectives

* Predict student academic performance.
* Compare multiple machine learning algorithms.
* Select the best-performing model.
* Deploy the final model as a REST API.
* Demonstrate an end-to-end machine learning project.

---

# Dataset

**Source:** Kaggle – Student Performance Dataset

**Dataset Size:**

* More than 1,000 records
* Numerical and categorical features

### Features

* Age
* Gender
* Study Hours
* Attendance
* Previous Grades
* Internet Access
* Family Support
* Parent Education
* School Type
* Extra Classes

### Target

* **Pass**
* **Fail**

---

# Data Preprocessing

The preprocessing pipeline includes:

* Exploratory Data Analysis (EDA)
* Removing duplicate records
* Handling missing values
* Encoding categorical variables
* Scaling numerical features
* Detecting and handling outliers
* Feature selection
* Train/Test split

---

# Machine Learning Algorithms

The following classification algorithms are trained and compared:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier

The best-performing model is selected based on the highest **F1-Score**.

---

# Evaluation Metrics

The models are evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

Three sanity checks are also performed on the best model.

---

# Project Structure

```text
student-performance-prediction/
│
├── dataset/
├── notebooks/
├── src/
├── api/
├── models/
├── README.md
├── project_paper.md
├── requirements.txt
└── .gitignore
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/your-username/student-performance-prediction.git
```

Move into the project directory:

```bash
cd student-performance-prediction
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

# Training the Model

Run the training script:

```bash
python src/train.py
```

---

# Running the API

Start the FastAPI server:

```bash
uvicorn api.app:app --reload
```

Open the API documentation:

```
http://127.0.0.1:8000/docs
```

---

# Example API Request

### POST `/predict`

Example JSON request:

```json
{
  "age": 18,
  "gender": "Male",
  "study_hours": 4,
  "attendance": 92,
  "previous_grade": 78,
  "internet_access": "Yes",
  "family_support": "Yes"
}
```

Example JSON response:

```json
{
  "prediction": "Pass",
  "probability": 0.94
}
```

---

# Results Summary

Three machine learning algorithms were trained and evaluated using the same dataset and train/test split. The model with the highest F1-Score was selected as the final model and deployed using FastAPI.

The project demonstrates how machine learning can assist educational institutions in identifying students who may require additional academic support before final examinations.

---

# Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* FastAPI
* Uvicorn
* Joblib
* Jupyter Notebook

---

# Author

**Abdullahi Hassan Shire**

Goobo Labs Data Science & Machine Learning Bootcamp

July 2026
