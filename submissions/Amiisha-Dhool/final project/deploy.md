Student Performance Prediction Using Machine Learning

 1. Abstract

Education data contains valuable information that can help institutions understand student performance and provide early support to learners. This project focuses on developing a machine learning model to predict whether a student will pass or fail based on academic, behavioral, and learning-related factors.

The project uses supervised machine learning classification techniques to build a predictive system. Different classification algorithms were trained and evaluated, and the best-performing model was selected for deployment.

The final selected model is a Random Forest Classifier, which was saved and deployed using a Flask API to provide student performance predictions.



 2. Introduction

Student academic performance is influenced by many factors including study habits, attendance, motivation, learning resources, and educational support. Identifying students who may fail at an early stage can help educators provide appropriate interventions.

Machine learning provides techniques that allow computers to learn patterns from historical data and make predictions on new data.

This project applies machine learning classification methods to predict student outcomes as either:

- Pass
- Fail



3. Problem Statement

The objective of this project is to develop a machine learning model that can predict student performance outcomes.

The system takes student information as input and predicts the final class:

- Pass
- Fail

This is considered a binary classification problem because the output contains only two possible categories.



4. Dataset Description

The dataset used in this project is:

student_performance.csv


The dataset contains information related to student academic performance and learning behavior.

The available features include:

- StudyHours
- Attendance
- Resources
- Extracurricular
- Motivation
- Internet
- Gender
- Age
- LearningStyle
- OnlineCourses
- Discussions
- AssignmentCompletion
- ExamScore
- EduTech
- StressLevel
- FinalGrade

The target variable used for prediction is:

Pass_Fail


5. Problem Type

This project uses:

Supervised Machine Learning - Binary Classification

The model learns from labeled training data where each student has a known outcome.

The prediction classes are:
0 - Fail
1 - Pass

 6. Data Preprocessing

Before training the machine learning models, the dataset was prepared through several preprocessing steps.

The preprocessing process included:

 Data Loading

The dataset was loaded using Pandas.

_ Feature and Target Separation

The dataset was divided into:

Input features (X):

Student-related attributes

Target variable (y):


Pass_Fail


Handling Categorical Data

Categorical features were converted into numerical format so that machine learning algorithms could process them.

 Dataset Splitting

The dataset was divided into:

- Training data
- Testing data

The training data was used for model learning, while the testing data was used for evaluation.



 7. Machine Learning Models

Four classification algorithms were trained and compared.

 1. Logistic Regression

Logistic Regression was used as a baseline classification algorithm to understand the relationship between student features and the final outcome.



2. Decision Tree Classifier

Decision Tree was trained because it can learn decision rules from student performance patterns.

 3. Random Forest Classifier

Random Forest combines multiple decision trees to improve prediction accuracy and reduce overfitting.

It was selected as the final model because it achieved the strongest overall performance among the evaluated models.



 4. Support Vector Machine (SVM)

Support Vector Machine was used as another classification approach to compare performance with other algorithms.



 8. Model Evaluation

The trained models were evaluated using different classification metrics:

 _Accuracy

Measures the percentage of correct predictions made by the model.

 _Precision

Measures how many predicted positive cases were actually positive.

 _Recall

Measures how many actual positive cases were correctly identified.

_F1-Score

Provides a balance between Precision and Recall.

_Confusion Matrix

Used to analyze the number of correct and incorrect predictions for Pass and Fail categories.


9. Final Model Selection

After comparing the performance of all trained models, the Random Forest Classifier was selected as the final model.

Reasons for selecting Random Forest:

- Strong predictive performance
- Good handling of different feature types
- Better generalization compared with other tested models

The trained model was saved as:

models/random_forest.pkl


The model was stored using Joblib and loaded later for prediction.


 10. Model Deployment

The final model was deployed using Flask.

The API loads the trained model:


random_forest.pkl


and provides predictions through an endpoint:


POST /predict


The API receives student information and returns the predicted result.

Example response:

json
{
    "prediction": "Pass"
}




 11. Project Structure


student-performance-prediction/

├── dataset/
│   └── student_performance.csv
│
├── notebooks/
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


12. Technologies Used

The following technologies were used:

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Flask
- Flask-CORS
- Matplotlib
- Seaborn
- Postman


 13. Conclusion

This project demonstrates how machine learning can be applied to predict student academic outcomes.

Different classification models were trained and evaluated. Among the tested algorithms, Random Forest Classifier was selected as the final model due to its reliable performance.

The trained model was successfully saved and deployed through a Flask API, allowing users to provide student information and receive predictions of Pass or Fail.

Machine learning-based prediction systems like this can support educational decision-making and help identify students who may require additional academic support.


14. References

- Scikit-learn Documentation  
https://scikit-learn.org/

- Flask Documentation  
https://flask.palletsprojects.com/

- Pandas Documentation  
https://pandas.pydata.org/



final project link:_ https://github.com/Amiisha-Dhool/student-perfomence-pridaction