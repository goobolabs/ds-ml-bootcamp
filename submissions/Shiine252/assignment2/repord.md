## Mobile Phone Usage Survey Dataset: A Data Science and Machine Learning Perspective

---

## \* Title and Collection Method

Dataset Title

Mobile Phone Usage Survey Dataset

### Collection Method

This dataset was collected using a Google Forms survey created by the researcher. The survey was distributed online to friends, classmates, and other participants. The objective was to gather information about smartphone usage habits, social media usage, and users' perceptions of their phone usage.

The dataset contains more than 50 responses collected directly from participants. Since the data was gathered personally through a survey, it satisfies the requirement of creating and collecting an original dataset rather than using an existing public dataset.

---

### \* Data Science Context

Data Science involves collecting, cleaning, analyzing, and modeling data to extract useful insights and support decision-making.

This project represents the early stages of the Data Science lifecycle:

1. Problem Definition
2. Data Collection
3. Data Cleaning and Preprocessing
4. Exploratory Data Analysis
5. Machine Learning Modeling
6. Evaluation and Deployment

The current assignment focuses primarily on data collection and understanding the structure and quality of the dataset before preprocessing and modeling.

---

### \* Features and Label

#### Features (X)

The dataset contains the following input variables:

Feature | Description
Age| Age of the participant
Gender| Gender of the participant
Smartphone Type| Android, iPhone, or Other
Daily Phone Usage Hours| Average hours spent using the phone each day
Daily Social Media Hours| Average hours spent on social media each day
Favorite App| Most frequently used mobile application

#### Label (y)

The target variable is:

Do you think you spend too much time on your phone?

Possible responses:

- Yes
- No
- Not Sure

This variable can be used as the output label for machine learning classification tasks.

---

### \* Dataset Structure

Dataset Dimensions

- Samples (Rows): 52
- Features: 6
- Label: 1
- Total Columns: 7 (excluding timestamp and comments)

Sample Records

Age| Gender| Smartphone Type| Phone Usage Hours| Social Media Hours| Favorite App| Spend Too Much Time
24| Male| Android| 10| 9| TikTok| Yes
20| Male| Android| 4| 2| TikTok| No
19| Male| Android| 6| 3| TikTok| Yes
23| Male| Android| 6| 6| YouTube| Yes
22| Male| Android| 9| 7| TikTok| Yes

The dataset contains both numerical and categorical variables, making it suitable for machine learning preprocessing techniques such as encoding and feature scaling.

---

### \* Data Quality Issues

Several quality issues were observed in the collected dataset.

Missing Values

Some participants left optional comment fields empty.

Typographical Errors

Examples include:

- TELGRMA instead of Telegram
- Iphone instead of iPhone

These inconsistencies should be standardized during preprocessing.

Outliers

Some responses contain unrealistic values.

Example:

- Phone usage = 6 hours
- Social media usage = 30 hours

This observation may represent a data entry error and should be investigated.

Duplicate Responses

Online surveys may allow participants to submit more than once, creating duplicate records.

Class Imbalance

One response category ("Yes") appears more frequently than other categories. This may affect machine learning performance and should be considered during model training.

Validation Issues

Although the survey intended to collect responses from adults, some participants reported ages below 18 years.

---

### \* Learning Type

This dataset is suitable for Supervised Learning.

A supervised learning problem contains:

- Features (X)
- Known Labels (y)

In this dataset, the label is:

«Do you think you spend too much time on your phone?»

Because the correct output is already known for each participant, machine learning algorithms can learn patterns from the data and predict labels for future users.

If the label were removed and the goal became grouping similar users together, the problem would become an Unsupervised Learning task.

---

### \* Machine Learning Use Case

Classification Problem

The primary machine learning application for this dataset is classification.

Objective

Predict whether a user believes they spend too much time on their phone based on:

- Age
- Gender
- Smartphone Type
- Phone Usage Hours
- Social Media Hours
- Favorite App

Possible Algorithms

- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)

Alternative Use Case

The dataset could also be used for clustering by removing the label and grouping users based on their phone usage patterns.

Example clusters:

- Heavy Users
- Moderate Users
- Light Users

---

### \* Data Science Lifecycle Placement

This project fits within the Data Science lifecycle as follows:

Stage| Description
Problem Definition| Understand smartphone usage behavior
Data Collection| Gather responses using Google Forms
Data Preparation| Clean missing values and inconsistencies
Data Analysis| Explore trends and patterns
Machine Learning| Train classification models
Evaluation| Measure prediction accuracy

---

### \* Conclusion

This project involved collecting and documenting an original mobile phone usage dataset using Google Forms. The dataset contains more than 50 responses and includes both numerical and categorical features.

The dataset is suitable for supervised machine learning because it contains a clearly defined target variable. Several data quality issues were identified, including missing values, inconsistent spellings, and outliers, which will require preprocessing before machine learning models can be developed.

# Overall, this dataset provides a practical example of how data is collected, structured, and prepared within the Data Science lifecycle.
