Data Foundations for Machine Learning

Practical Assignment: Mobile Phone Usage and Battery Life Dataset

Student Information

Name: Nasteho Abdi Aadan

Course: Data Foundations for Machine Learning

Submission Date: June 20, 2026

---

1. Introduction

This project focuses on collecting and documenting a dataset related to mobile phone usage and battery performance. The purpose of the dataset is to understand how different phone usage habits affect battery performance.

The dataset was collected through manual data collection and observation. Information such as screen time, charging frequency, and battery capacity was recorded and organized into a structured dataset.

This project demonstrates the data collection stage of the Data Science lifecycle and prepares the dataset for future preprocessing and machine learning tasks.

---

2. Dataset Collection Method

The dataset was created manually by recording information about smartphone usage patterns and battery characteristics.

The collected information includes:

- User age
- Phone brand
- Daily screen time
- Number of applications used daily
- Charging frequency
- Battery capacity
- Battery performance category

A total of 50 samples were collected.

---

3. Features and Label

Features (X)

Feature| Description
Age| Age of the phone user
Phone_Brand| Smartphone manufacturer
Screen_Time_Hours| Average screen usage per day
Apps_Used_Daily| Number of apps used daily
Charging_Frequency| Number of charges per day
Battery_Capacity_mAh| Battery size in mAh

Label (y)

Label| Description
Battery_Performance| Battery condition categorized as Good, Average, or Poor

The label represents the target variable that a machine learning model would attempt to predict.

---

4. Dataset Structure

- Total Rows: 50
- Total Columns: 7
- Features: 6
- Label: 1

Sample Data

Age| Phone Brand| Screen Time| Apps Used| Charging Frequency| Battery Capacity| Performance
20| Samsung| 4| 12| 1| 5000| Good
22| Huawei| 7| 20| 2| 4200| Average
19| Infinix| 9| 25| 3| 5000| Poor
21| Tecno| 5| 15| 1| 6000| Good
23| Xiaomi| 8| 22| 2| 4500| Average

---

5. Data Quality Issues

Like many real-world datasets, this dataset may contain several quality issues:

- Missing values in some records
- Duplicate rows
- Typographical errors in phone brand names
- Inconsistent formatting
- Imbalanced distribution between battery performance categories

These issues will be addressed during the data preprocessing stage.

---

6. Learning Type

This dataset is suitable for Supervised Machine Learning because it contains a clearly defined target variable (Battery_Performance).

The machine learning model can learn patterns from the input features and predict the battery performance category for new observations.

---

7. Use Case

This dataset can be used for:

- Battery performance prediction
- Smartphone usage analysis
- User behavior analysis
- Classification machine learning projects

Possible machine learning task:

Classification

The model predicts whether battery performance is:

- Good
- Average
- Poor

---

8. Data Science Lifecycle

This dataset fits into the following stages of the Data Science lifecycle:

1. Data Collection
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis
4. Machine Learning Model Training
5. Model Evaluation
6. Deployment and Monitoring

For this assignment, the focus is primarily on the Data Collection stage.

---

9. Conclusion

The Mobile Phone Usage and Battery Life dataset was created to explore the relationship between smartphone usage habits and battery performance. The dataset contains 50 samples and 6 input features with one target label.

The dataset is suitable for supervised machine learning classification tasks and will be useful for future preprocessing and modeling activities.