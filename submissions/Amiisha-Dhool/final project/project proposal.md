 Final Project Proposal

1. Certificate Name

Amina Abdirahmaan mohamed 


2. Project Title and Description

Project title

**Student Performance Prediction Using Machine Learning**

Description

This project aims to predict whether a student will **Pass** or **Fail** based on academic, personal, and lifestyle factors such as study hours, attendance, previous scores, sleep hours, and tutoring sessions. The goal is to help schools and educators identify students who may be at academic risk so that they can provide early support and improve student success.


3. Problem Type

**Classification**

This is a binary classification problem where the model predicts whether a student will **Pass** or **Fail** based on different student-related features.

Problem Type:  Classification
Learning Type:  Supervised Learning

 4. Dataset

Source: zenodo

Dataset Link: https://zenodo.org/records/16459132/files/merged_dataset.csv?utm_

**Expected Size:** Approximately 15,000 rows

Target Column:

 **Pass_Fail** – Indicates whether a student passes or fails the exam.

**Main Features:

* Hours_Studied – Number of study hours.
* Attendance – Student attendance percentage.
* Previous_Scores – Previous academic performance.
* Sleep_Hours – Average sleeping hours.
* Tutoring_Sessions – Number of tutoring sessions attended.
* Motivation_Level – Student motivation level.
* Internet_Access – Availability of internet access.
* Extracurricular_Activities – Participation in extracurricular activities.
* Parental_Involvement – Level of parental support.



5. Algorithms You Plan to Train

1. Logistic Regression

Used as a baseline classification model because it is simple, efficient, and performs well on binary classification problems.

 2. Decision Tree

Useful for learning decision rules and providing interpretable predictions.

 3. Random Forest

Improves prediction accuracy by combining multiple decision trees and reducing overfitting.

4. K-Nearest Neighbors (KNN)

Classifies students based on similarities with nearby data points.

5. Support Vector Machine (SVM)

Effective for classification tasks and capable of finding the optimal decision boundary between classes.


 6. Evaluation Plan

The models will be evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

**Best Model Selection:**
The final model will be selected based on the **F1-Score**, as it provides a balanced evaluation of both Precision and Recall for binary classification.



7. Deployment Sketch

**Framework:** Flask

predict Endpoint

**Input (JSON):**

* Hours_Studied
* Attendance
* Previous_Scores
* Sleep_Hours
* Tutoring_Sessions
* Motivation_Level
* Internet_Access
* Extracurricular_Activities
* Parental_Involvement

**Output (JSON):**

* Prediction (Pass or Fail)
* Prediction Probability



8. Repository Plan

student-performance-prediction/
│
├── dataset/
├── notebooks/
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│
├── api/
│   └── app.py
│
├── models/
├── results/
├── README.md
├── requirements.txt
└── project_paper.md


