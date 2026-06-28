# Predicting Employment Outcomes Among Somali University Graduates

**Author: Ali Omar Abdi**                                          
**Course: DS-ML Bootcamp — Assignment 2**                               
**Due: Saturday, June 20, 2026 — 12:00 PM (EAT)**      

---

## Table of Contents

1. [Collection Method](#1-collection-method)
2. [Features and Label](#2-features-and-label)
3. [Dataset Structure](#3-dataset-structure)
4. [Data Quality Issues](#4-data-quality-issues)
5. [Learning Type](#5-learning-type)
6. [Machine Learning Use Cases](#6-machine-learning-use-cases)

---

## 1. Collection Method

In Somalia, finishing university does not guarantee a job. Some graduates get hired fast. Others wait months, or never find work. The reasons are not always clear.

This dataset was made to study that gap. The goal was simple: collect information about graduates and their employment outcomes, then use machine learning to find what factors actually matter.

Data was gathered through a structured questionnaire given to 110 university graduates and final-year students across Somalia. Each person answered questions about their background, academic record, skills, and current employment status.

Participants came from universities in eight cities: Mogadishu, Hargeisa, Garoowe, Bosaso, Galkayo, Baidoa, Burao, and Beledweyne.

Each respondent answered ten questions:

- Age and gender
- University attended and the town it is located in
- Degree program studied
- GPA (out of 4.0)
- English proficiency (Low, Medium, or High)
- Whether they completed an internship (Yes or No)
- Digital skills level (Beginner, Intermediate, or Advanced)
- Number of professional certificates earned
- Current employment status (Employed or Unemployed)

This dataset was built from scratch for this assignment. It was not downloaded from Kaggle, UCI, or any other public source.

---

## 2. Features and Label

Every machine learning dataset is divided into two parts: the features and the label.

**Features (X)** are the input variables. These are the clues we give the model.
**Label (y)** is the output variable. This is what the model learns to predict.

Think of it like a detective case. The features are the evidence. The label is the answer.

### Features (X)

| No. | Feature | Type | Description |
|---|---|---|---|
| 1 | Age | Numerical | Graduate's age in years |
| 2 | Gender | Categorical | Male or Female |
| 3 | University | Categorical | Name of university attended |
| 4 | Town | Categorical | City where the university is located |
| 5 | Degree Program | Categorical | Subject of study |
| 6 | GPA | Numerical | Academic grade, out of 4.0 |
| 7 | English Proficiency | Categorical | Low, Medium, or High |
| 8 | Internship Experience | Categorical | Yes or No |
| 9 | Digital Skills Level | Categorical | Beginner, Intermediate, or Advanced |
| 10 | Certifications Count | Numerical | Number of professional certificates earned |

### Label (y)

| Label | Type | Values |
|---|---|---|
| Employment Status | Categorical | Employed or Unemployed |

Every row already has a known Employment Status. That is what makes this a supervised learning problem. The model has real answers to learn from.

---

## 3. Dataset Structure

| Property | Value |
|---|---|
| Total Rows (Samples) | 110 |
| Total Columns | 11 |
| Features | 10 |
| Label | 1 |

### Sample Table (7 Rows)

| Age | Gender | University | Town | Degree | GPA | English | Internship | Digital Skills | Certs | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| 28 | Female | Jaamacadda Hormuud | Mogadishu | Economics | 3.02 | High | Yes | Intermediate | 1 | Employed |
| 24 | Female | mogadishu university | Mogadishu | Software Engineering | 2.30 | Low | No | Intermediate | 1 | Unemployed |
| 30 | Female | Jaamacadda Hormuud | Mogadishu | Public Health | 3.88 | High | Yes | Intermediate | 2 | Employed |
| 24 | Male | Jaamacadda Soomaaliya | Mogadishu | Law | 2.42 | Low | Yes | Intermediate | 2 | Unemployed |
| 26 | Male | Jaamacadda Hormuud | Mogadishu | Law | 3.65 | High | Yes | Advanced | 6 | Employed |
| 24 | Male | Jaamacada Golis | Hargeisa | Civil Engineering | 3.80 | Medium | Yes | Advanced | 1 | Employed |
| 25 | Female | Jaamacadda Puntland State University | Garoowe | Civil Engineering | 3.61 | Medium | No | Advanced | 3 | Employed |

A pattern already shows. Graduates with high English proficiency, internship experience, and strong digital skills tend to be employed. Graduates with low English, no internship, and beginner digital skills tend to be unemployed.

Row 2 is a real example of a quality issue. "mogadishu university" (lowercase) is the same institution that appears elsewhere as "Jaamacadda Muqdisho." The spelling inconsistency is not a typo added for illustration. It came from the raw survey responses.

---

## 4. Data Quality Issues

Survey data is never clean. This dataset has six types of problems that must be fixed before training a model.

### Missing Values

Some participants skipped questions. GPA is missing in 7 rows. Certifications Count is missing in 8 rows. English Proficiency, Internship Experience, and Digital Skills Level are each missing in 5 to 6 rows.

Empty cells break machine learning models. The model cannot learn from a row it cannot read.

**Fix:** For number columns like GPA, fill the missing cell with the average (mean) of all other values. For category columns like English Proficiency, fill it with the most common value (mode).

### Spelling and Naming Inconsistencies

The same university appears under several different names. For example:

"Jaamacadda SIMAD" vs "SIMAD" vs "simad"
"Jaamacadda Muqdisho" vs "mogadishu university"
"Jaamacada Jamhuuriya ee Culuumta iyo Tiknooloojiyada" vs "JUST"

The computer reads each version as a different category. That corrupts any analysis involving university name.

**Fix:** During preprocessing, pick one standard name for each university and apply it to every row that refers to that institution.

### Duplicate Rows

Three rows are exact duplicates, most likely from a graduate submitting the survey twice. Training the model on the same row twice teaches it nothing new and can cause overfitting.

**Fix:** Check for rows where every value is identical and delete the duplicates.

### Outlier in GPA

One row has a GPA of 4.3. Somalia's standard grading scale has a maximum of 4.0. This is either a data entry error or the participant misunderstood the question.

**Fix:** Cap the value at 4.0, or remove the row if the rest of its data is also unreliable.

### Class Imbalance

85 out of 110 graduates (77%) are Employed. Only 25 (23%) are Unemployed. This is imbalanced. A model trained on this data will quickly learn that predicting "Employed" is correct most of the time, so it stops actually learning the pattern.

**Fix:** Use SMOTE (Synthetic Minority Oversampling Technique) to generate synthetic examples of the minority class (Unemployed), or reduce the number of majority class rows.

### Self-Reporting Bias

GPA, English proficiency, and digital skills were self-reported with no verification. Some participants may have given optimistic answers.

**Fix:** This is difficult to fix with code alone. The best solution is to verify responses during data collection. During modeling, cross-validation helps detect if the data is producing unreliable results.

---

## 5. Learning Type

This is a **Supervised Learning** problem. Specifically, it is a **Classification** task.

### Why Supervised?

Supervised learning is used when every row already has a label. In this dataset, every graduate has a known Employment Status. The model has real answers to study. It looks at the features for each graduate, checks the employment outcome, and over time learns which patterns lead to employment.

As Lesson 2 explains, supervised learning is like studying with an answer key. The model sees the question (features) and the correct answer (label) together, many times, until it understands the pattern.

### Why Classification, Not Regression?

The label is a category, not a number. Employed or Unemployed. Two options.

Regression predicts numbers. For example, if the label were monthly salary in dollars, that would be a regression problem. But since we are predicting which group a graduate falls into, we use classification.

---

## 6. Machine Learning Use Cases

This dataset suits supervised classification. Every row has a known label, so the model can learn and be evaluated properly. There are three ways it can be used.

**Classification (primary use):** Build a model that predicts whether a graduate will be Employed or Unemployed based on their academic background and skills profile.

**Feature importance analysis:** Find out which factor matters most. Is it GPA? Internship experience? English proficiency? Digital skills? The answer could help universities and students focus their efforts in the right direction.

**Clustering (exploratory, unsupervised):** Group graduates into profiles without using the employment label. For example, "high GPA, no internship" vs "average GPA, strong digital skills." This can reveal patterns that the classification model misses.

Practically, a trained model from this dataset could help universities spot students at risk of unemployment before they graduate, give government agencies and NGOs data to design better skills training programs, and give individual students an early, honest estimate of their job prospects.

---

*Submitted for DS-ML Bootcamp — Assignment 2*
*Due: Saturday, June 20, 2026*
