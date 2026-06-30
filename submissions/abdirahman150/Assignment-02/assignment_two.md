# Practical Assignment: Data Foundations for Machine Learning

## Title: Student Performance Dataset for Machine Learning Analysis

### prepared By:
Name : Abdirahman Khadar Mohamed

## 1: Data Collection
This dataset focuses on student academic performance and the factors influencing examination results. The purpose of collecting this dataset is to understand how different student habits and behaviors affect academic performance. The dataset was collected manually through surveys and questionnaires distributed to students. A total of 50 students participated in this data collection process.

The data collection process included asking students questions about: 
Age 
Gender 
Daily Study Hours 
Attendance Percentage 
Average Sleep Hours 
Final Exam Score

This dataset was created specifically for this assignment and was not taken from Kaggle, UCI, or any public repository.

## 2:  Description of Features & Labels
In Machine Learning, data is divided into Features (X) and Label (y).

### Features (X):
1. Age – Student age in years. 
2. Gender – Male or Female. 
3. Study Hours – Number of hours studied per day. 
4. Attendance – Percentage of class attendance. 
5. Sleep Hours – Average number of sleeping hours per day.

### Label (y): 
Exam Score – Student final examination score in percentage.
The features are used as input variables to predict the label.

## 3: Dataset Structure
The complete dataset contains:
 • 50 Rows (Samples) 
 • 8 Columns (Variables)
### Sample Records
Student_ID,Student_Name,Age,Gender,Study_Hours,Attendance,Sleep_Hours,Exam_Score
1,Ahmed ,20,Male,4,85,7,78
2,Amina ,22,Female,6,90,8,88
3,Mohamed ,19,Male,2,70,6,60
4,Hodan ,21,Female,5,92,7,91
5,Abdirahman ,23,Male,3,75,5,65
6,Faiza ,20,Female,4,88,7,80

## 4: Quality Issues
Real-world datasets usually contain problems that need preprocessing before machine learning.

Missing Values
duplicates
imbalance
Typos
Invalid Value
Outlier

## 5: Learning Type

This dataset belongs to Supervised Learning. The reason is that the dataset contains a clear output variable (Label y), which is Exam Score. The model will learn patterns from the features and predict student exam scores. 

Input Features (X): Age, Gender, Study Hours, Attendance, Sleep Hours 
Output Label (y): Exam Score

## 6: Use Case
This dataset can be used in different Machine Learning applications. 
Regression: Used to predict exact exam scores such as 75%, 82%, or 91%. 
Classification: Exam scores can be converted into categories such as Pass/Fail or Good/Average/Poor. 
Clustering: Students can be grouped based on similar study behaviors and performance levels.

## 7. Data Science Lifecycle 
This dataset fits into the Data Science lifecycle as follows:
1. Problem Definition – Understand factors affecting student performance. 
2. Data Collection – Gather data from surveys and questionnaires. 
3. Data Cleaning – Handle missing values, duplicates, and errors. 
4. Modeling – Train machine learning models. 
5. Evaluation – Measure model performance and accuracy. 
6. Deployment – Apply the model in real-world educational systems.

## Conclusion 
The Student Performance Dataset is valuable for analyzing academic performance and identifying factors that influence student success. Machine Learning can help predict exam scores, identify struggling students, and improve educational decision-making. This dataset provides a strong foundation for future preprocessing and machine learning tasks.