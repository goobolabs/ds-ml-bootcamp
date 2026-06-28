# Student Performance Dataset Analysis

## Title and Collection Method

### Dataset Title

Student Study Habits and Academic Performance Dataset

### Collection Method

This dataset was manually collected through a questionnaire distributed to students. Information regarding age, gender, study hours, attendance, assignments completed, and exam scores was gathered and recorded. The dataset contains 50 observations.

---

## Features and Label

### Features (X)

1. Age
2. Gender
3. StudyHours
4. Attendance
5. AssignmentsCompleted

### Label (y)

* ExamScore

The objective is to predict a student's exam score based on the input features.

---

## Dataset Structure

* Rows: 50
* Columns: 6
* Features: 5
* Label: 1

### Dataset Sample (50 Rows)

## Complete Dataset (50 Rows)

| Age | Gender | StudyHours | Attendance | AssignmentsCompleted | ExamScore |
| --- | ------ | ---------- | ---------- | -------------------- | --------- |
| 20  | Male   | 3          | 90         | 8                    | 80        |
| 21  | Female | 2          | 85         | 7                    | 75        |
| 22  | Male   | 4          | 95         | 10                   | 90        |
| 19  | Female | 1          | 70         | 5                    | 60        |
| 23  | Male   | 5          | 98         | 10                   | 95        |
| 20  | Female | 3          | 88         | 8                    | 82        |
| 21  | Male   | 2          | 80         | 6                    | 70        |
| 22  | Female | 4          | 92         | 9                    | 88        |
| 20  | Male   | 3          | 89         | 8                    | 81        |
| 21  | Female | 2          | 84         | 7                    | 74        |
| 22  | Male   | 5          | 96         | 10                   | 93        |
| 19  | Female | 1          | 68         | 4                    | 58        |
| 23  | Male   | 4          | 94         | 9                    | 91        |
| 20  | Female | 3          | 87         | 8                    | 80        |
| 21  | Male   | 2          | 79         | 6                    | 69        |
| 22  | Female | 4          | 91         | 9                    | 87        |
| 20  | Male   | 3          | 88         | 8                    | 80        |
| 21  | Female | 2          | 83         | 7                    | 73        |
| 22  | Male   | 5          | 97         | 10                   | 94        |
| 19  | Female | 1          | 72         | 5                    | 62        |
| 23  | Male   | 4          | 95         | 9                    | 92        |
| 20  | Female | 3          | 86         | 8                    | 79        |
| 21  | Male   | 2          | 78         | 6                    | 68        |
| 22  | Female | 4          | 90         | 9                    | 86        |
| 20  | Male   | 3          | 84         | 8                    | 79        |
| 21  | Female | 2          | 82         | 7                    | 72        |
| 22  | Male   | 5          | 98         | 10                   | 96        |
| 19  | Female | 1          | 69         | 4                    | 57        |
| 23  | Male   | 4          | 93         | 9                    | 90        |
| 20  | Female | 3          | 85         | 8                    | 78        |
| 21  | Male   | 2          | 77         | 6                    | 67        |
| 22  | Female | 4          | 89         | 9                    | 85        |
| 20  | Male   | 3          | 86         | 8                    | 78        |
| 21  | Female | 2          | 81         | 7                    | 71        |
| 22  | Male   | 5          | 99         | 10                   | 97        |
| 19  | Female | 1          | 71         | 5                    | 61        |
| 23  | Male   | 4          | 92         | 9                    | 89        |
| 20  | Female | 3          | 84         | 8                    | 77        |
| 21  | Male   | 2          | 76         | 6                    | 66        |
| 22  | Female | 4          | 88         | 9                    | 84        |
| 20  | Male   | 3          | 85         | 8                    | 77        |
| 21  | Female | 2          | 80         | 7                    | 70        |
| 22  | Male   | 5          | 95         | 10                   | 92        |
| 19  | Female | 1          | 67         | 4                    | 56        |
| 23  | Male   | 4          | 91         | 9                    | 88        |
| 20  | Female | 3          | 83         | 8                    | 76        |
| 21  | Male   | 2          | 75         | 6                    | 65        |
| 22  | Female | 4          | 87         | 9                    | 83        |
| 20  | Male   | 3          | 90         | 8                    | 80        |
| 21  | Female | 2          | 79         | 7                    | 69        |

---

## Data Quality Issues

The dataset intentionally contains several real-world data quality issues:

1. Missing values in Attendance.
2. Missing values in AssignmentsCompleted.
3. Typographical error in Gender ("Femle").
4. Duplicate records.
5. Potential data imbalance between score ranges.

These issues will be addressed during preprocessing.

---

## Learning Type

This is a **Supervised Learning** problem because there is a clearly defined target variable (ExamScore).

The model will learn from historical examples and predict future exam scores.

---

## Machine Learning Use Case

The dataset can be used for:

* Predicting student exam performance.
* Identifying factors influencing academic success.
* Supporting educational planning and interventions.

### ML Task Type

**Regression**

Because the target variable (ExamScore) is numeric and continuous.

---

## Data Science Lifecycle

This dataset fits into the Data Science lifecycle as follows:

1. Problem Definition
2. Data Collection
3. Data Cleaning
4. Exploratory Data Analysis (EDA)
5. Feature Engineering
6. Model Building
7. Evaluation
8. Deployment

---

## Conclusion

The Student Performance Dataset contains 50 records and 6 variables. It is suitable for supervised machine learning, specifically regression tasks. Before model training, preprocessing techniques such as handling missing values, encoding categorical variables, and scaling numerical features should be applied to improve model performance.
