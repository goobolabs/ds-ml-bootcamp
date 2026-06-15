# Machine Learning Assignment One

Define Data Science and Machine Learning. What is the relationship between them? Use a real-life example to illustrate how they work together.

Describe the Data Science lifecycle (from problem definition to deployment). At which stage does Machine Learning typically fit in, and why?

Compare Supervised Learning and Unsupervised Learning, giving an example of each.

What causes Overfitting? How can it be prevented?

Explain how training data and test data are split, and why this process is necessary.

Find one case study (research paper or article) that explains how Data Science or Machine Learning has been applied in healthcare, business, or transportation. Summarize its findings and identify which part of the Data Science lifecycle it covers.

1:Define Data Science and Machine Learning. What is the relationship between them? Use a real-life example to illustrate how they work together.

What is Data Science?

Data Science is an interdisciplinary field that uses scientific methods, statistical techniques, programming, and domain knowledge to collect, process, analyze, and interpret data. Its primary goal is to extract meaningful insights from structured and unstructured data to support better decision-making.

According to the IBM Data Science Overview, Data Science combines mathematics, statistics, computer science, and business expertise to uncover patterns and trends within data.

What is Machine Learning?

Machine Learning (ML) is a subset of Artificial Intelligence (AI) that enables computers to learn from data and improve their performance without being explicitly programmed. Machine Learning algorithms identify patterns in historical data and use those patterns to make predictions or decisions on new data.

According to IBM Machine Learning Guide, Machine Learning allows systems to learn from experience and adapt automatically based on data.

Relationship Between Data Science and Machine Learning

Data Science and Machine Learning are strongly interconnected. Data Science provides the framework for collecting, cleaning, analyzing, and preparing data, while Machine Learning uses this prepared data to build predictive models and automated decision-making systems.

Machine Learning is therefore considered one of the most important tools used within Data Science projects. Without quality data prepared through Data Science processes, Machine Learning models cannot produce reliable results.

The relationship can be summarized as follows:

Data Science gathers and prepares data.

Data Science explores and analyzes the data.

Machine Learning learns patterns from the prepared data.

Machine Learning generates predictions or recommendations.

Data Science evaluates and interprets the results for business use.

Real-Life Example: Amazon Product Recommendation System

A practical example of Data Science and Machine Learning working together can be seen in Amazon's recommendation system.

When customers browse products, search for items, or make purchases, Amazon collects large amounts of data about their behavior.

Role of Data Science:

Collects customer interaction data.

Cleans and organizes the data.

Analyzes purchasing trends and customer preferences.

Identifies useful features for prediction.

Role of Machine Learning:

Learns patterns from customer behavior.

Predicts products a customer may be interested in.

Generates personalized recommendations.

Continuously improves recommendations as more data becomes available.

## 2. Describe the Data Science Lifecycle. At Which Stage Does Machine Learning Fit In, and Why?

The Data Science lifecycle is a step-by-step process used to solve problems using data.

Problem Definition – Identify the problem and project goals.

Data Collection – Gather relevant data from different sources.

Data Cleaning & Preparation – Remove errors, duplicates, and missing values.

Exploratory Data Analysis (EDA) – Analyze data to find patterns and trends.

Model Building (Machine Learning) – Train a machine learning model using prepared data.

Model Evaluation – Test the model's performance and accuracy.

Deployment – Put the model into a real-world system for use.

Monitoring – Continuously check and improve the model over time.

Where Does Machine Learning Fit?

Machine Learning typically fits in the Model Building stage. At this stage, algorithms learn patterns from the cleaned and prepared data to make predictions or decisions.

Example: A store can use Machine Learning to predict future sales based on past sales data.

## 3. Compare Supervised Learning and Unsupervised Learning, Giving an Example of Each

Example of Supervised Learning

A bank uses historical customer data to predict whether a customer will repay a loan. Since the data includes known outcomes (repaid or not repaid), this is supervised learning.

Example of Unsupervised Learning

A supermarket groups customers based on their purchasing behavior to identify different customer segments. Since there are no predefined categories, this is unsupervised learning.

## 4. What Causes Overfitting? How Can It Be Prevented?

Overfitting occurs when a Machine Learning model learns the training data too well, including its noise and random patterns. As a result, the model performs very well on training data but poorly on new, unseen data.

Causes of Overfitting

Using a very complex model.

Training the model for too long.

Having too little training data.

Including too many irrelevant features.

How to Prevent Overfitting

Use more training data.

Remove unnecessary features.

Apply cross-validation.

Use simpler models.

Use regularization techniques.

Stop training when performance on validation data starts to decrease (early stopping).

Example

Suppose a student memorizes answers to past exam questions instead of understanding the concepts. They may score well on those specific questions but struggle with new ones. Similarly, an overfitted model memorizes training data instead of learning general patterns.

## 5. How Training Data and Test Data Are Split, and Why It Is Necessary

In Machine Learning, the dataset is usually divided into two main parts:

## 1. Training Data

This is the largest portion of the data (commonly 70–80%). It is used to train the model, meaning the model learns patterns, relationships, and rules from this data.

## 2. Test Data

This is the remaining portion (commonly 20–30%). It is used to test the model’s performance on new, unseen data.

How the Split is Done

A dataset is randomly divided to avoid bias. For example:

80% → Training set

20% → Test set

Sometimes a third part called a validation set is also used to fine-tune the model.

Why This Process Is Necessary

To check generalization: It ensures the model can work on new data, not just memorized data.

To avoid overfitting: If a model only performs well on training data, it is not useful in real life.

To measure accuracy fairly: Test data gives an honest evaluation of model performance.

To improve model selection: Helps compare different models and choose the best one.

Simple Example

Imagine a student studying for an exam:

Training data = study notes and practice questions

Test data = final exam

If the student only memorizes practice questions but fails the exam, they have “overfitted.” A good student understands concepts and performs well on both.

## 6. Case Study: Machine Learning in Healthcare (Diabetes Prediction)

A well-known study applied Machine Learning to predict diabetes using patient health records. One example is based on the Pima Indians Diabetes Dataset, widely used in research and healthcare analytics.

Reference: UCI Machine Learning Repository – Diabetes Dataset

Summary of Findings

In this study, researchers used Machine Learning algorithms to predict whether a patient is likely to develop diabetes based on medical features such as:

Age

Body Mass Index (BMI)

Blood pressure

Glucose level

Insulin level

What was done:

Patient data was collected and cleaned.

Important health features were selected.

Machine Learning models like Logistic Regression and Decision Trees were trained.

The models were tested on unseen data.

Results:

The system was able to predict diabetes risk with good accuracy.

Glucose level and BMI were found to be the strongest indicators.

The model helps detect high-risk patients early, even before symptoms become severe.

Impact:

Early detection of diabetes

Faster medical decision-making

Reduced healthcare costs

Better patient care and prevention strategie

## References

IBM. (2025). What is Data Science? Retrieved from: IBM Data Science Overview

IBM. (2025). What is Machine Learning? Retrieved from: IBM Machine Learning Guide

Microsoft Learn – Introduction to Data Science

Google Machine Learning Crash Course

Amazon Official Website (Recommendation System Example)

IBM – Data Science Overview

Google Machine Learning Crash Course

IBM – Supervised Learning

IBM – Unsupervised Learning

IBM – Overfitting in Machine Learning

Google Machine Learning Crash Course

IBM – Train/Test Split in Machine Learning

Google Machine Learning Crash Course
