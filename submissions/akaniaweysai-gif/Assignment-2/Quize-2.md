Practical Assignment: Data Foundations for Machine Learning
Title

Student Daily Study Habits and Academic Performance Dataset

1. Collection Method

This dataset was collected using a simple questionnaire distributed to university students. The survey asked students about their study habits, attendance, sleep duration, and assignment completion. Their latest exam result was also recorded.

The data were collected manually from students over several days.

2. Description of Features and Label
2. Description of Features and Label
Features (X)
Feature	Description	Data Type
Age	Student's age	Numerical
Gender	Male/Female	Categorical
Study Hours	Average study hours per day	Numerical
Attendance (%)	Class attendance percentage	Numerical
Sleep Hours	Average sleep per night	Numerical
Assignment Completed	Yes/No	Categorical
Label (y)
Label	Description
Pass	Whether the student passed the exam (Yes/No)

This is the variable the machine learning model will predict.

3. Dataset Structure
Number of Rows: 50
Number of Columns: 7
Features: 6
Label: 1

Age	Gender	Study Hours	Attendance	Sleep Hours	Assignment Completed	Pass
19	Male	1	55	5	No	No
20	Female	2	58	6	Yes	No
21	Male	3	61	7	Yes	No
22	Female	4	64	8	No	No
23	Male	5	67	5	Yes	No
24	Female	1	70	6	Yes	No
19	Male	2	73	7	No	No
20	Female	3	76	8	Yes	Yes
21	Male	4	79	5	Yes	Yes
22	Female	5	82	6	No	No
23	Male	1	85	7	Yes	No
24	Female	2	88	8	Yes	No
19	Male	3	91	5	No	No
20	Female	4	94	6	Yes	Yes
21	Male	5	56	7	Yes	No
22	Female	1	59	8	No	No
23	Male	2	62	5	Yes	No
24	Female	3	65	6	Yes	No
19	Male	4	68	7	No	No
20	Female	5	71	8	Yes	Yes
21	Male	1	74	5	Yes	No
22	Female	2	77	6	No	No
23	Male	3	80	7	Yes	Yes
24	Female	4	83	8	Yes	Yes
19	Male	5	86	5	No	No
20	Female	1	89	6	Yes	No
21	Male	2	92	7	Yes	No
22	Female	3	95	8	No	No
23	Male	4	57	5	Yes	No
24	Female	5	60	6	Yes	No
19	Male	1	63	7	No	No
20	Female	2	66	8	Yes	No
21	Male	3	69	5	Yes	No
22	Female	4	72	6	No	No
23	Male	5	75	7	Yes	Yes
24	Female	1	78	8	Yes	No
19	Male	2	81	5	No	No
20	Female	3	84	6	Yes	Yes
21	Male	4	87	7	Yes	Yes
22	Female	5	90	8	No	No
23	Male	1	93	5	Yes	No
24	Female	2	55	6	Yes	No
19	Male	3	58	7	No	No
20	Female	4	61	8	Yes	No
21	Male	5	64	5	Yes	No
22	Female	1	67	6	No	No
23	Male	2	70	7	Yes	No
24	Female	3	73	8	Yes	Yes
19	Male	4	76	5	No	No
20	Female	5	79	6	Yes	Yes

4. Quality Issues

The dataset may contain several real-world data quality problems, including:

Missing values if some students skipped questions.
Typographical errors in gender or assignment status.
Duplicate records if a student completed the survey twice.
Different formats (e.g., "Yes", "yes", "YES").
Imbalanced classes if most students passed and only a few failed.

5. Learning Type

This is a Supervised Machine Learning problem because the dataset includes a known target variable (Pass).

The model learns from the input features to predict whether a student will pass or fail.

6. Machine Learning Use Case

Possible machine learning applications include:

Classification

Predict whether a student is likely to pass or fail before the exam.

Possible algorithms include:
Decision Tree
Logistic Regression
Random Forest
Support Vector Machine (SVM)

7. Role in the Data Science Lifecycle

This dataset fits into the Data Science lifecycle as follows:

Problem Definition
Predict student academic performance.
Data Collection
Survey students and record responses.
Data Cleaning
Remove duplicates, handle missing values, and standardize data.
Exploratory Data Analysis
Analyze relationships between study habits and exam performance.
Model Building
Train a classification model.
Model Evaluation
Measure accuracy, precision, recall, and F1-score.
Deployment
Use the model to identify students who may need academic support.
