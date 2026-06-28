# Assignment 02: Data foundations for machine learning

**Dataset:** AI Tools Usage and Productivity Dataset

---

## Title and collection method

### Dataset title

AI Tools Usage and Productivity Dataset

### How I collected it

I put together a short survey asking people how they use AI tools for work and study. The questions covered which tool they use, how long they have been using it, how satisfied they are, and whether they would recommend AI tools to someone else. I ended up with 50 responses.

---

## Features and label

### Features (X)

| Feature           | Description                             |
| ----------------- | --------------------------------------- |
| Age               | Age of the respondent                   |
| Occupation        | Profession of the respondent            |
| AI Tool Used      | Main AI tool used                       |
| HoursPerWeek      | Hours spent using AI tools per week     |
| TasksPerWeek      | Tasks completed using AI tools per week |
| ExperienceMonths  | Months of AI experience                 |
| SatisfactionScore | Satisfaction rating from 1 to 10        |

### Label (y)

| Label            | Description                                        |
| ---------------- | -------------------------------------------------- |
| WouldRecommendAI | Whether the user would recommend AI tools (Yes/No) |

The point is to predict whether someone would recommend AI tools based on how they actually use them.

---

## Dataset structure

The dataset has 50 rows and 8 columns: 7 features and 1 label.

### Sample data

| Age | Occupation     | AI Tool Used | SatisfactionScore | WouldRecommendAI |
| --- | -------------- | ------------ | ----------------- | ---------------- |
| 22  | Student        | ChatGPT      | 9                 | Yes              |
| 30  | Teacher        | Gemini       | 6                 | Yes              |
| 35  | Business Owner | ChatGPT      | 4                 | No               |

---

## Quality issues

A few things in this dataset could cause problems:

* Some fields are missing values.
* A few entries look wrong, probably typos when people filled in the form.
* People read the questions differently, so the answers are not always consistent.
* There are a lot more "Yes" answers than "No" answers, so the classes are unbalanced.
* The text columns like Occupation and AI Tool Used need to be encoded into numbers before a model can use them.

I would deal with these in the cleaning and preprocessing step before training anything.

---

## Learning type

This is supervised learning. Each row already has the answer I want to predict (WouldRecommendAI), so the model learns from labeled examples and then predicts the label for new ones.

---

## Machine learning problem

This is a classification problem. The label only has two possible values, Yes or No, so the model is sorting each user into one of two groups.

---

## Use case

A dataset like this is useful for:

* Looking at who adopts AI tools and who does not
* Checking how satisfied users are
* Working out which factors push someone toward recommending a tool
* Training a model that predicts whether a new user would recommend AI tools

---

## Data science lifecycle

The work would move through these stages:

1. Problem definition
2. Data collection
3. Data cleaning
4. Exploratory data analysis (EDA)
5. Feature engineering
6. Modeling
7. Evaluation
8. Deployment

---

## Conclusion

This dataset captures how 50 people use AI tools and whether they would recommend them. Since every row is labeled, it works for supervised learning, and because the label is Yes or No, the natural task is classification. With some cleaning to handle the missing values and the class imbalance, it is enough to train a basic model that predicts recommendations from usage and satisfaction.

---

## References

1. IBM Data Science Documentation
2. Microsoft Learn, Machine Learning Fundamentals
3. Scikit-Learn Documentation
4. Google Forms Documentation