# Personality Type Prediction Using Social Behavior Data

## 1. Title and Collection Method

### Title

Personality Type Prediction Based on Social and Lifestyle Preferences

### Collection Method

This dataset was created through a survey conducted among friends and classmates. Participants were asked several questions about their social habits and personal preferences. Their responses were manually recorded and converted into a structured dataset.

The survey focused on behaviors such as participating in group activities, meeting new people, working alone, preferring quiet places, and contacting friends. Based on these responses, each participant was assigned a personality category: Introvert, Ambivert, or Extrovert.

The final dataset contains 52 observations and was collected manually rather than using any public dataset repository.

---

## 2. Description of Features and Label

### Input Variables (Features X)

| Feature             | Description                                                         |
| ------------------- | ------------------------------------------------------------------- |
| group_activity      | Whether the participant enjoys group activities (0 = No, 1 = Yes)   |
| meet_new_people     | Whether the participant enjoys meeting new people (0 = No, 1 = Yes) |
| prefer_work_alone   | Whether the participant prefers working alone (0 = No, 1 = Yes)     |
| prefer_quiet_places | Whether the participant prefers quiet places (0 = No, 1 = Yes)      |
| call_friends        | Whether the participant frequently calls friends (0 = No, 1 = Yes)  |

### Output Variable (Label y)

| Label            | Description                                             |
| ---------------- | ------------------------------------------------------- |
| personality_type | Personality category: Introvert, Ambivert, or Extrovert |

---

## 3. Dataset Structure

### Dataset Size

* Rows: 52
* Columns: 6
* Features: 5
* Label: 1

### Sample Records

| group_activity | meet_new_people | prefer_work_alone | prefer_quiet_places | call_friends | personality_type |
| -------------- | --------------- | ----------------- | ------------------- | ------------ | ---------------- |
| 0              | 1               | 1                 | 1                   | 0            | Ambivert         |
| 1              | 0               | 0                 | 0                   | 1            | Extrovert        |
| 0              | 1               | 1                 | 1                   | 0            | Ambivert         |
| 1              | 1               | 0                 | 0                   | 0            | Extrovert        |
| 1              | 1               | 0                 | 0                   | 0            | Extrovert        |

---

## 4. Quality Issues

Several data quality issues were identified:

### Missing Values

Two records contain missing values:

* One missing value in meet_new_people.
* One missing value in call_friends.

### Possible Class Imbalance

Some personality categories may have more samples than others. This should be checked before model training.

### Human Error

Because the data was collected manually, some survey responses may contain recording mistakes or inconsistent answers.

### Small Dataset Size

The dataset contains only 52 samples, which may limit model performance and generalization.

---

## 5. Learning Type

This problem is a Supervised Learning problem.

The reason is that a clear target variable (personality_type) is provided for every observation. The machine learning model can learn patterns from the input features and predict the personality category of new individuals.

Because the target consists of categories (Introvert, Ambivert, Extrovert), this is specifically a Classification task.

---

## 6. Use Case and Machine Learning Application

### Potential Use Case

This dataset could be used to build a personality prediction system. Educational institutions, career counselors, or social applications could use similar information to understand user behavior patterns.

### Suitable Machine Learning Models

* Decision Tree Classifier
* Random Forest Classifier
* Logistic Regression
* K-Nearest Neighbors (KNN)

### Data Science Lifecycle Position

This dataset fits into the following stages of the Data Science Lifecycle:

1. Problem Definition

   * Predict personality type from behavioral traits.

2. Data Collection

   * Survey responses collected manually.

3. Data Cleaning

   * Handle missing values and verify data quality.

4. Exploratory Data Analysis

   * Study relationships between behaviors and personality types.

5. Model Building

   * Train a classification model.

6. Evaluation

   * Measure accuracy, precision, recall, and F1-score.

7. Deployment

   * Use the model in applications that recommend activities or assess personality traits.

## Conclusion

This project demonstrates how behavioral survey data can be used to predict personality types using machine learning. The dataset contains 52 samples and 5 behavioral features. Although the dataset has a small size and a few missing values, it provides a suitable example for practicing supervised learning, classification techniques, data cleaning, and exploratory analysis.
