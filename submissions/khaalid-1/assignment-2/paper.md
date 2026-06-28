# Practical Assignment: Data Foundations for Machine Learning

## Title

**The Relationship Between Daily Screen Time and Sleep Duration Among Individuals**

---

# 1. Introduction and Collection Method

The purpose of this study is to investigate whether screen usage habits are associated with sleep duration among individuals. With the increasing use of smartphones, computers, and other digital devices, many people spend several hours per day using screens, especially before bedtime. This research aims to explore whether these habits affect sleep patterns.

The dataset was collected through an online questionnaire created using Google Forms. The survey was distributed to individuals who voluntarily participated in the study. A total of 51 responses were collected. To protect privacy, the questionnaire was anonymous and did not collect personal identification information such as names, phone numbers, or addresses.

---

# 2. Features and Label

The dataset contains the following variables:

| Variable          | Type        | Description                                         |
| ----------------- | ----------- | --------------------------------------------------- |
| Age               | Feature (X) | Age of the respondent                               |
| Gender            | Feature (X) | Male or Female                                      |
| Screen Time       | Feature (X) | Average daily screen usage                          |
| Phone Before Bed  | Feature (X) | Whether the respondent uses a phone before sleeping |
| Sleep Quality     | Feature (X) | Self-reported sleep quality                         |
| Daytime Tiredness | Feature (X) | Whether the respondent feels tired during the day   |
| Sleep Hours       | Label (y)   | Average sleep duration category                     |

The features represent the input variables (X), while Sleep Hours represents the target variable or label (y).

---

# 3. Dataset Structure

Dataset Summary:

* Number of Rows: 51
* Number of Columns: 7
* Number of Features: 6
* Number of Labels: 1

### Sample Records

| Age | Gender | Screen Time | Phone Before Bed | Sleep Quality | Daytime Tiredness | Sleep Hours       |
| --- | ------ | ----------- | ---------------- | ------------- | ----------------- | ----------------- |
| 20  | Male   | 1–3 hours   | Yes              | Average       | No                | 4–5 hours         |
| 25  | Male   | 10+ hours   | Yes              | Bad           | Yes               | Less than 4 hours |
| 25  | Male   | 10+ hours   | Yes              | Good          | No                | 4–5 hours         |
| 26  | Male   | 7–9 hours   | Yes              | Average       | Yes               | 4–5 hours         |
| 22  | Female | 7–9 hours   | Yes              | Good          | No                | 8–9 hours         |

---

# 4. Quality Issues

Several data quality challenges were encountered during data collection. Some respondents entered text instead of numeric values in the age field, while others provided age values that appeared unrealistic. In addition, some individuals were hesitant to participate due to privacy concerns and needed clarification about the purpose of the research. Since the data was self-reported, responses related to screen time, sleep duration, and sleep quality may contain minor inaccuracies or estimation errors.

---

# 5. Learning Type

This dataset is suitable for **Supervised Learning** because it contains both input variables (features) and a target variable (label).

The target variable is **Sleep Hours**, while the remaining variables are used as features to predict the target.

This problem can be treated as a **Classification** task because the target variable is recorded as categories such as:

* Less than 4 hours
* 4–5 hours
* 6–7 hours
* 8–9 hours

The goal is to predict the sleep duration category based on screen usage habits and personal characteristics.

---

# 6. Use Case and Data Science Lifecycle

This dataset can be used to build a machine learning model that predicts sleep duration categories based on personal characteristics and screen usage habits.

Potential applications include:

* Digital wellness research
* Student lifestyle analysis
* Health awareness programs
* Sleep behavior studies

Within the Data Science lifecycle, this project fits into the following stages:

1. Data Collection – gathering responses through a questionnaire.
2. Data Cleaning and Preprocessing – validating age values and standardizing responses.
3. Exploratory Data Analysis – identifying relationships between screen time and sleep.
4. Machine Learning Modeling – building a classification model.
5. Evaluation and Interpretation – assessing model performance and drawing conclusions.

---

# 7. Conclusion

This study collected data from 51 participants to examine the relationship between screen usage habits and sleep duration. The dataset includes demographic information, technology usage behaviors, and sleep-related variables. Despite some data quality challenges, the dataset provides a useful foundation for machine learning and data analysis. The project demonstrates the importance of data collection, data quality assessment, and understanding the role of features and labels in supervised learning.

 
