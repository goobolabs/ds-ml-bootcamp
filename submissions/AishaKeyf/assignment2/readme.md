# Research Paper: Analysis of an AI Usage and Perception Survey Dataset

## 1. Title and Collection Method

### Title

**Analysis of AI Usage, Trust, and Perceptions Among AI Users**

### Collection Method

This dataset was collected through an online survey I created using Microsoft Forms. The purpose of the survey was to understand how people use Artificial Intelligence (AI), their level of trust in AI-generated information, the benefits they experience, and their perceptions of AI's future impact on society.

The survey was distributed online and completed voluntarily by participants. Responses were automatically stored in an Excel spreadsheet for further analysis. The dataset consists of 51 responses collected from individuals with different occupations, age groups, and levels of AI experience.

---

## 2. Description of Features and Labels

In Machine Learning, features (X) are the input variables used for prediction, while the label (y) is the target variable we want the model to predict.

### Features (X)

The dataset contains several useful features, including:

* Age
* Gender
* Occupation
* AI usage frequency
* Preferred AI tools
* Trust in AI-generated answers
* Verification behavior
* Satisfaction with AI tools
* Perceived improvement in productivity
* Perceived improvement in knowledge
* Main purpose of AI use
* Experiences while using AI

Examples of feature columns:

| Feature                                     | Description               |
| ------------------------------------------- | ------------------------- |
| Age                                         | Participant age group     |
| Gender                                      | Participant gender        |
| Occupation                                  | Current occupation        |
| How frequently do you use AI?               | Frequency of AI usage     |
| Which AI tool do you use mostly?            | Preferred AI systems      |
| How much do you trust AI-generated answers? | Trust level in AI outputs |
| Do you verify AI-generated information?     | Fact-checking behavior    |
| Main purpose of AI use                      | Reason for using AI       |

### Label (y)

A suitable target variable for Machine Learning would be:

**"Do you think AI will become essential in everyday life and work in the future?"**

Possible classes:

* Yes
* No
* Unsure

This makes the dataset suitable for classification tasks because the target variable has clear categories.

---

## 3. Dataset Structure

### Dataset Size

* Total Rows (Responses): **51**
* Total Columns (Variables): **26**

Each row represents one survey participant, while each column represents a survey question or metadata field.

### Sample Records

| Age   | Gender | Occupation                  | AI Use Frequency     | Main Purpose of AI Use   | Future Essential? |
| ----- | ------ | --------------------------- | -------------------- | ------------------------ | ----------------- |
| 15–24 | Female | Student                     | 8–14 times           | Programming, Translation | Yes               |
| 15–24 | Female | Teacher, Software Developer | Daily                | Research, Programming    | Yes               |
| 15–24 | Male   | Student                     | Daily                | Studying, Programming    | Yes               |
| 15–24 | Male   | Student                     | Daily                | Programming, Studying    | Yes               |
| 15–24 | Female | Student                     | Multiple times a day | Programming, Research    | Yes               |

---

## 4. Dataset Quality Issues

Several data quality issues were identified.

### 1. Empty Columns

The columns:

* Name
* Last modified time

contain no useful data and can be removed during preprocessing.

### 2. Lack of Class Diversity

Every participant answered "Yes" to the question "Do you use AI?". Because there are no "No" responses, this variable cannot be used as a prediction target.

### 3. Multi-Value Responses

Many questions allow multiple answers separated by semicolons. For example:

* AI tools used
* Occupation
* Main purpose of AI use

These responses must be transformed into machine-readable features before model training.

### 4. Open-Ended Responses

The question:

"What is your biggest concern or benefit when using AI?"

contains free-text answers. These responses may include spelling variations and different writing styles that require text preprocessing.

### 5. Possible Sampling Bias

Most respondents belong to the 15–24 age group and are students or technology users. Therefore, the dataset may not fully represent the general population.

---

## 5. Learning Type

### Supervised Learning

This dataset is best categorized as a **Supervised Learning** problem.

A supervised learning problem contains:

* Input variables (features X)
* A known target variable (label y)

In this dataset:

* Features (X): Age, Gender, Occupation, AI Usage Frequency, Trust Level, Satisfaction Level, etc.
* Label (y): Whether participants believe AI will become essential in everyday life and work.

Since the correct output is already known for each participant, a model can learn patterns from existing responses and predict future outcomes.

Therefore, the dataset satisfies the requirements of supervised learning.

---

## 6. Use Case and Data Science Lifecycle

### Potential Machine Learning Applications

#### Classification

The dataset is most suitable for a classification problem.

Example:

Predict whether a person will answer:

* Yes
* No
* Unsure

to the question about AI becoming essential in the future.

Possible algorithms include:

* Logistic Regression
* Decision Trees
* Random Forest
* Support Vector Machines (SVM)

#### Sentiment Analysis

The open-ended text responses can be analyzed to determine whether participants express:

* Positive attitudes
* Negative concerns
* Neutral opinions

about AI.

#### Clustering

Unsupervised techniques such as K-Means clustering can group respondents based on:

* Usage frequency
* Trust levels
* AI tool preferences
* Occupation

This may reveal different categories of AI users.

---

### Position in the Data Science Lifecycle

This dataset fits into several stages of the Data Science Lifecycle:

#### 1. Data Collection

Survey responses are gathered using Microsoft Forms.

#### 2. Data Cleaning

Missing values, empty columns, and text inconsistencies are addressed.

#### 3. Data Exploration

Researchers analyze trends in AI usage and attitudes.

#### 4. Modeling

Machine Learning algorithms are trained to predict perceptions and future expectations of AI.

#### 5. Evaluation

Model performance is measured using accuracy, precision, recall, and F1-score.

#### 6. Communication

Findings are presented through reports, dashboards, and visualizations.

---

## Conclusion

The AI Usage and Perception Survey dataset provides valuable information about how individuals use AI technologies and how they perceive their impact on society. The dataset contains 51 responses and 26 variables covering demographics, AI usage behavior, trust levels, satisfaction, and future expectations. Although some cleaning is required, the dataset is suitable for supervised machine learning tasks, particularly classification. It can also support clustering and sentiment analysis projects, making it a useful resource for understanding human interaction with Artificial Intelligence.
