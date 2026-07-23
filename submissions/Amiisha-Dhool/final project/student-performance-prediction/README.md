# Student Performance Prediction

## Project Overview

Student Performance Prediction is a Machine Learning project that predicts whether a student will pass or fail based on academic, behavioral, and learning-related factors.

The main goal of this project is to build a classification model that can analyze student information and predict the final outcome (`Pass` or `Fail`).

This project uses supervised machine learning techniques and deploys the selected model through a Flask API.


# Problem Type

This project is a:

**Binary Classification Problem**

The model predicts two possible classes:

- Pass
- Fail

The target variable is:

Pass_Fail


# Dataset

Dataset file:

dataset/student_performance.csv


The dataset contains student-related information including:

- Study habits
- Attendance
- Learning resources
- Motivation
- Internet access
- Educational technology usage
- Assignment completion
- Exam performance
- Final grade



# Features Used

The model was trained using the following features:

StudyHours
Attendance
Resources
Extracurricular
Motivation
Internet
Gender
Age
LearningStyle
OnlineCourses
Discussions
AssignmentCompletion
EduTech
StressLevel
FinalGrade


# Data Preparation

The following preprocessing steps were applied:

1. Loading the dataset using Pandas

2. Creating the target variable:

```
Pass_Fail
```

from:

```
FinalGrade
```

3. Separating:

- Features (X)
- Target (y)

4. Encoding categorical variables into numerical values.

5. Splitting the dataset into:

- Training data
- Testing data

using:

```
train_test_split()
```


# Machine Learning Models

Different classification algorithms were trained and evaluated.

The models were compared using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

After evaluation, the best performing model was selected.


# Final Model

The selected model is:

## Random Forest Classifier

Random Forest was chosen because it achieved strong performance and provided reliable classification results.

The trained model was saved as:

```
models/random_forest.pkl
```

The model is loaded using:

```
joblib.load()
```

and used for prediction.


# Project Structure

student-performance-prediction/

│
├── dataset/
│   └── student_performance.csv
│
├── notebooks/
│   └── student_perfomance_prediction.ipynb
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── evaluate.py
│
├── api/
│   └── app.py
│
├── models/
│   └── random_forest.pkl
│
├── results/
│
├── README.md
│
├── requirements.txt
│
└── project_paper.md


# Model Deployment

The trained Random Forest model was deployed using Flask.

The API provides a prediction endpoint:


POST /predict

Example input:

json
{
    "StudyHours": 5,
    "Attendance": 85,
    "Resources": "High",
    "Extracurricular": "Yes",
    "Motivation": "High",
    "Internet": "Yes",
    "Gender": "Male",
    "Age": 20,
    "LearningStyle": "Visual",
    "OnlineCourses": "Yes",
    "Discussions": "Yes",
    "AssignmentCompletion": 90,
    "EduTech": "Yes",
    "StressLevel": "Low",
    "FinalGrade": 80
}
```

Example output:

json
{
    "prediction": "Pass"
}


# Running the API

Navigate to the API folder:

bash
cd api

Run Flask:

bash
python app.py


The API will run on:


http://127.0.0.1:5000




# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Random Forest Classifier
- Flask
- Joblib
- Postman


# Conclusion

This project demonstrates how machine learning can be used to predict student academic outcomes.

The Random Forest model successfully learned patterns from student data and can classify students into Pass or Fail categories.

The deployed Flask API allows users to provide student information and receive predictions from the trained model.