# Assignment2

**Dataset:** Student Transportation and School Arrival Dataset

---

## Title and Collection Method

### Dataset Title

Student Transportation and School Arrival Dataset

### How I Collected method

For this project, I created a survey to collect information about how students travel to school and whether they arrive on time. The survey included questions about age, gender, distance from home to school, transportation type, travel time, transportation cost, traffic conditions, weather conditions, and overall satisfaction with transportation.

The survey was distributed to students, and I collected responses from 50 participants. The purpose of the dataset is to understand how transportation-related factors affect students' arrival times at school.

---

## Features and Label

### Features (X)

| Feature            | Description                              |
| ------------------ | ---------------------------------------- |
| Age                | Age of the student                       |
| Gender             | Gender of the student                    |
| DistanceToSchool   | Distance between home and school         |
| TransportationType | Main transportation used by the student  |
| TravelTime         | Time taken to reach school               |
| TransportationCost | Daily transportation cost                |
| TrafficImpact      | Whether traffic affects travel time      |
| WeatherImpact      | Whether weather affects the journey      |
| SatisfactionLevel  | Student satisfaction with transportation |

### Label (y)

| Label         | Description                                 |
| ------------- | ------------------------------------------- |
| ArrivalStatus | Whether the student arrives On Time or Late |

The goal is to predict whether a student will arrive at school on time based on transportation and travel-related factors.

---

## Dataset Structure

The dataset contains 50 rows and 10 columns. It consists of 9 features and 1 label.

### Sample Data

| Age | Gender | DistanceToSchool | TransportationType | TravelTime | ArrivalStatus |
| --- | ------ | ---------------- | ------------------ | ---------- | ------------- |
| 20  | Female | 2 km             | Walking            | 20 min     | On Time       |
| 21  | Male   | 5 km             | Bus                | 35 min     | On Time       |
| 19  | Female | 8 km             | Taxi               | 50 min     | Late          |
| 22  | Male   | 3 km             | Bajaj              | 15 min     | On Time       |
| 20  | Female | 10 km            | Bus                | 60 min     | Late          |

Each row represents one student, while each column represents a specific feature or label.

---

## Quality Issues

Like many real-world datasets, this dataset may contain several quality issues that need to be addressed before training a machine learning model.

* Some students may skip questions, resulting in missing values.
* There may be spelling mistakes in transportation types or other text fields.
* Some students might submit the survey more than once, creating duplicate records.
* Different students may enter data using different formats.
* Traffic and weather information may be based on personal opinions rather than exact measurements.
* There may be more "On Time" responses than "Late" responses, causing class imbalance.

These issues can be solved during the data cleaning and preprocessing stage.

---

## Learning Type

**Supervised Learning**.

The reason is that every record contains a known target value called **ArrivalStatus**. T

Because the correct answer already exists in the dataset, this problem is supervised rather than unsupervised learning.

---

## Machine Learning Problem

This is a **Classification Problem**.

The label has two possible categories:

* On Time
* Late

The model will classify each student into one of these two groups based on the provided features.

---

## Use Case

This dataset can be useful in several ways:

* Understanding the factors that influence student punctuality.
* Identifying transportation challenges faced by students.
* Helping schools understand why students arrive late.
* Supporting decisions related to transportation planning.
* Building a machine learning model that predicts whether a student is likely to arrive on time or late.

---

## Data Science Lifecycle

This project follows the main stages of the Data Science lifecycle:

1. Problem Definition – Understanding student transportation challenges.
2. Data Collection – Gathering survey responses from students.
3. Data Cleaning – Handling missing values, duplicates, and formatting issues.
4. Exploratory Data Analysis (EDA) – Exploring patterns and relationships in the data.
5. Feature Engineering – Transforming useful variables for modeling.
6. Model Building – Training a classification model.
7. Evaluation – Measuring model accuracy and performance.
8. Deployment – Using the model to predict future student arrival status.

---

## Conclusion

This dataset focuses on student transportation habits and school arrival behavior. Information was collected from 50 students through a survey designed specifically for this project.

The dataset includes transportation-related features and a clear label called ArrivalStatus. Since the dataset contains labeled examples, it is suitable for supervised learning. Furthermore, because the target variable consists of two categories (On Time and Late), the appropriate machine learning task is classification.

After cleaning and preprocessing the data, this dataset can be used to build a machine learning model that predicts whether a student is likely to arrive on time or arrive late based on transportation conditions and travel patterns.



## References

1. Scikit-Learn Documentation
2. Google Forms Documentation
3. Course Notes: Data Foundations for Machine Learning
4. Microsoft Learn – Machine Learning Fundamentals