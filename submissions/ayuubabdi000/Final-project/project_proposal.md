# AI Student Success Prediction and Learning Analytics System

## 1. Certificate Name

**Ayuub A/risaak Jaama**

---

## 2. Project Title and Description

**Title:** AI Student Success Prediction and Learning Analytics System

Online learning platforms generate large amounts of student activity data every day. However, instructors often struggle to identify students who are at risk of failing or dropping out before it is too late. This project aims to build an AI-powered educational analytics system that predicts student performance and provides meaningful learning insights.

The system combines multiple machine learning models to analyze student demographic information, learning behavior, course engagement, and academic performance. It predicts whether a student will complete a course and groups students into different learning behavior categories.

The final application will consist of a React dashboard connected to a FastAPI backend and MongoDB database. Users will be able to submit student information, receive AI predictions, view learning analytics, compare machine learning models, and review previous prediction history through a clean web interface.

The goal of the project is to demonstrate practical machine learning deployment while helping educators better understand student performance and identify students who may require additional academic support.

---

## 3. Problem Type

This project combines two machine learning problem types.

### Classification

Predict whether a student will successfully complete a course.

Output:

- Completed
- Not Completed

Target column:

```
Completed
```

---

### Clustering

Group students based on learning behavior without predefined labels.

Example clusters:

- High Performers
- Active Learners
- At-Risk Students
- Inactive Students

The classification model is the primary prediction model, while clustering provides additional learning analytics.

---

## 4. Dataset

**Source**

Student Course Completion Dataset (Kaggle)

**Expected Size**

- Approximately 10,000 student records
- More than 40 features

**Target**

```
Completed
```

### Main Features

#### Student Information


- Education_Level
- Employment_Status

#### Learning Environment

- Device_Type
- Internet_Connection_Quality

#### Course Information

- Course_Level
- Course_Duration_Days
- Instructor_Rating

#### Learning Behaviour

- Login_Frequency
- Average_Session_Duration_Min
- Video_Completion_Rate
- Discussion_Participation
- Time_Spent_Hours
- Days_Since_Last_Login

#### Academic Performance

- Assignments_Submitted
- Assignments_Missed
- Quiz_Score_Avg
- Progress_Percentage

### Preprocessing Plan

- Remove unnecessary columns
- Handle missing values
- Encode categorical variables
- Scale numerical features when required
- Split dataset into 80% training and 20% testing

---

## 5. Algorithms I Plan to Train

### Classification

| Algorithm | Reason |
|-----------|--------|
| Logistic Regression | Baseline classification model |
| Random Forest Classifier | Handles mixed feature types and reduces overfitting |
| XGBoost Classifier | Strong performance on structured educational datasets |

---

### Clustering

| Algorithm | Reason |
|-----------|--------|
| K-Means | Student segmentation |
| Hierarchical Clustering | Understand relationships between groups |
| DBSCAN | Detect unusual learning behaviors |

The best-performing model from each task will be selected for deployment.

---

## 6. Evaluation Plan

### Classification

Metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- Confusion Matrix

The final classification model will be selected using **F1-Score** because it balances Precision and Recall when identifying students at risk.

---

### Clustering

Metrics:

- Silhouette Score
- Elbow Method
- Cluster Visualization

---

## 7. Deployment Sketch

### Backend

FastAPI

### Frontend

React + Tailwind CSS

### Database

MongoDB

### REST API

```text
GET  /api/v1/dashboard

POST /api/v1/predict

GET  /api/v1/evaluation

GET  /api/v1/history

GET  /api/v1/health
```

### Input Example

```json
{
  "Age": 20,
  "Education_Level": "Bachelor",
  "Login_Frequency": 5,
  "Video_Completion_Rate": 85,
  "Quiz_Score_Avg": 90,
  "Assignments_Submitted": 10,
  "Progress_Percentage": 80
}
```

### Output Example

```json
{
  "completion_prediction": "Completed",
  "completion_probability": 0.91,
  "risk_level": "Low",
  "cluster": "High Performer",
  "recommendations": [
    "Maintain quiz performance",
    "Increase discussion participation"
  ]
}
```

---

## 8. Repository Plan

```text
student-success-ai/

student-success-ai/
│
├── frontend/
│   ├── public/
│   │
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── layouts/
│   │   ├── services/
│   │   ├── hooks/
│   │   ├── types/
│   │   ├── utils/
│   │   ├── App.tsx
│   │   └── main.tsx
│   │
│   ├── package.json
│   └── vite.config.ts
│
├── backend/
│   │
│   ├── dataset/
│   │   └── students.csv
│   │
│   ├── src/
│   │   ├── preprocess.py
│   │   ├── train.py
│   │   ├── evaluate.py
│   │   └── predict.py
│   │
│   ├── api/
│   │   └── app.py
│   │
│   ├── models/
│   │   ├── classifier.pkl
│   │   ├── cluster.pkl
│   │   ├── scaler.pkl
│   │   └── encoder.pkl
│   │
│   ├── notebooks/
│   │   └── exploration.ipynb
│   │
│   ├── requirements.txt
│   └── README.md
│
├── project_paper.md
└── README.md
```

### Planned Commands

```bash
python backend/train.py

uvicorn backend.app.main:app --reload

npm run dev
```

---

## Final Deliverable

The completed project will be a full-stack AI-powered educational analytics platform that combines:

- Student Course Completion Prediction
- Student Learning Behaviour Clustering
- Learning Analytics Dashboard
- Machine Learning Model Evaluation
- FastAPI REST API
- React Frontend
- MongoDB Database

The system will provide educators with an easy-to-use web application for predicting student outcomes, analyzing learning behavior, and supporting data-driven educational decisions.