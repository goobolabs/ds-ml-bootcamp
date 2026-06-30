# The Impact of Social Media on Children

## Project Goal

The goal of this assignment is to collect an original dataset and explain how it can be used in a Machine Learning project. The dataset focuses on people's opinions about the impact of social media on children and follows the requirements of the Data Science assignment.

---

## Dataset Collection

The dataset was collected using a **Google Forms** survey. The survey link was shared through **WhatsApp** and **Telegram** groups, and respondents voluntarily completed the questionnaire.

### Dataset Summary

* **Collection Method:** Google Forms Survey
* **Distribution:** WhatsApp and Telegram Groups
* **Total Responses (Samples):** 69
* **Total Columns:** 16
* **Assignment Requirement:** At least 50 samples and at least 5 features ✔️

---

## Features (X)

The dataset contains the following input features:

1. Age
2. Gender
3. Occupation
4. Do you have children?
5. Should children use social media?
6. Recommended age for children to use social media
7. Most used social media platform
8. Estimated daily social media usage
9. Main purpose of social media use
10. Learning impact
11. Academic performance impact
12. Parent monitoring
13. School education on safe social media use

---

## Label (y)

**Do you think social media negatively affects children's mental health?**

This variable is used as the target (label) for the machine learning model.

---

## Dataset Structure

* **Rows (Samples):** 69
* **Columns:** 16

Each row represents one survey respondent, while each column represents one variable collected through the Google Forms survey. The dataset contains demographic information together with respondents' opinions about children's use of social media.

---

## Sample Dataset

| Age      | Gender | Occupation     | Has Children | Platform  | Mental Health Impact |
| -------- | ------ | -------------- | ------------ | --------- | -------------------- |
| 18–25    | Male   | Student        | No           | TikTok    | Agree                |
| 26–35    | Female | Teacher        | Yes          | YouTube   | Strongly Agree       |
| 18–25    | Male   | Employee       | No           | Instagram | Agree                |
| 36–45    | Female | Parent         | Yes          | Facebook  | Neutral              |
| Above 45 | Male   | Business Owner | Yes          | TikTok    | Disagree             |

*The table above shows only a small sample of the dataset.*

---

## Quality Issues

Possible quality issues in the dataset include:

* Missing values
* Duplicate responses
* Opinion bias
* Spelling variations in text responses
* Class imbalance
* Open-ended responses that require preprocessing

These issues can be addressed during the data preprocessing stage.

---

## Learning Type

This dataset is suitable for **Supervised Learning** because it contains input features (X) and a target label (y).

### Machine Learning Task

**Classification**

The model can be trained to classify respondents' opinions about whether social media negatively affects children's mental health.

---

## Use Case

This dataset can be used to build a Machine Learning classification model that predicts respondents' opinions about the impact of social media on children's mental health. It can also be used to analyze how demographic factors and social media usage relate to these opinions.

---

## Data Science Lifecycle

This dataset follows the early stages of the Data Science lifecycle:

1. Problem Definition
2. Data Collection (Google Forms)
3. Data Cleaning and Preprocessing
4. Exploratory Data Analysis (EDA)
5. Machine Learning Model Building (Classification)
6. Model Evaluation

---

## Repository Contents

* **README.md** – Project description and dataset documentation.
* **social_media_children_responses.csv** – Dataset collected using Google Forms.

---

## Author

**Name:** Deko Hussein Sid

**Course:** Data Science
