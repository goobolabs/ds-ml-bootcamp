Assignment-1-by sicid

1. Define Data Science and Machine Learning. What is the relationship between them?

Data Science is an interdisciplinary field that uses statistics, programming, mathematics, and domain knowledge to collect, clean, analyze, and interpret data to solve real-world problems and support decision-making.

Machine Learning (ML) is a branch of artificial intelligence (AI) that enables computers to learn patterns from data and make predictions or decisions without being explicitly programmed for every task.

Relationship between Data Science and Machine Learning

Machine Learning is a subset of Data Science. Data Science covers the entire process of working with data—from collecting and cleaning data to analyzing, visualizing, and communicating insights. Machine Learning is one of the tools used within Data Science, mainly for building predictive models.

Real-life example

A hospital wants to predict whether a patient is likely to develop diabetes.

Data Science is used to collect patient records, clean missing values, explore trends, and prepare the data.
Machine Learning trains a model using patient information (age, blood pressure, glucose level, BMI, etc.) to predict whether a new patient is at risk of diabetes.
The hospital uses these predictions to provide early treatment and improve patient care.
2. Describe the Data Science lifecycle. At which stage does Machine Learning fit in, and why?

The Data Science lifecycle consists of the following stages:

Problem Definition
Identify the business or research problem.
Example: Predict customer churn or detect diabetes early.
Data Collection
Gather data from databases, sensors, surveys, APIs, or other sources.
Data Cleaning and Preparation
Handle missing values, remove duplicates, correct errors, and transform data into a usable format.
Exploratory Data Analysis (EDA)
Analyze the data using statistics and visualizations to identify patterns and relationships.
Feature Engineering
Select or create useful variables (features) that improve model performance.
Model Building (Machine Learning Stage)
Train Machine Learning algorithms using the prepared data.
Compare different models and select the best-performing one.
Model Evaluation
Test the model using evaluation metrics such as accuracy, precision, recall, and F1-score.
Deployment
Deploy the model into a real-world application where users can benefit from its predictions.
Monitoring and Maintenance
Monitor model performance, retrain with new data, and update the model when necessary.
Where does Machine Learning fit?

Machine Learning primarily fits in the Model Building stage because this is where algorithms learn patterns from historical data to make predictions or classifications. However, it also plays a role during Model Evaluation and Monitoring, where the model's effectiveness is tested and maintained over time.

3. Compare Supervised Learning and Unsupervised Learning
Supervised Learning	Unsupervised Learning
Uses labeled data (input and correct output are known).	Uses unlabeled data (no correct output provided).
Goal is to predict outcomes.	Goal is to discover hidden patterns or groups.
Common tasks: Classification and Regression.	Common tasks: Clustering and Dimensionality Reduction.
Performance can be measured using known answers.	Results are evaluated based on how meaningful the discovered patterns are.
Example of Supervised Learning

A bank trains a model using past loan records labeled as "Approved" or "Rejected." The model predicts whether future loan applications should be approved.

Example of Unsupervised Learning

An online retailer groups customers into different shopping behavior categories without knowing the groups beforehand. The discovered clusters help create targeted marketing campaigns.

4. What causes Overfitting? How can it be prevented?
Causes of Overfitting

Overfitting occurs when a Machine Learning model learns the training data too well, including its noise and random variations, making it perform poorly on new data.

Common causes include:

Using a model that is too complex.
Having too little training data.
Training for too many iterations.
Including irrelevant or noisy features.
How to prevent Overfitting
Use more training data.
Split data into training, validation, and test sets.
Apply cross-validation.
Simplify the model.
Remove unnecessary features.
Use regularization techniques (L1 or L2).
Apply early stopping during training.
Use ensemble methods such as Random Forest.
5. Explain how training data and test data are split, and why this process is necessary.

A dataset is divided into two parts:

Training Data (typically 70–80%)
Used to teach the Machine Learning model by allowing it to learn patterns.
Test Data (typically 20–30%)
Used only after training to evaluate how well the model performs on unseen data.

Example:

Total dataset: 1,000 records
Training set: 800 records (80%)
Test set: 200 records (20%)
Why is splitting necessary?
Prevents overly optimistic performance estimates.
Detects overfitting.
Measures how well the model generalizes to new data.
Provides an unbiased evaluation before deployment.
6. Case Study: Machine Learning in Healthcare

Title: Use of artificial intelligence for public health surveillance: a case study to develop a machine learning algorithm to estimate the incidence of diabetes mellitus in France (2021).

Summary

Researchers developed a supervised Machine Learning model using data from a large French health database to estimate the incidence of diabetes. The study linked epidemiological cohort data with national healthcare reimbursement records and followed a structured Machine Learning workflow: defining the prediction target, selecting variables, splitting the dataset into training and test sets, training multiple models, validating them, and choosing the best-performing algorithm based on evaluation metrics such as the Area Under the ROC Curve (AUC). The results showed that Machine Learning can effectively support public health surveillance by identifying new diabetes cases more efficiently from large administrative datasets.

Data Science lifecycle stages covered

This case study covers several stages of the Data Science lifecycle:

Problem Definition: Estimate the incidence of diabetes.
Data Collection: Gather data from national healthcare databases and epidemiological cohorts.
Data Preparation: Select relevant records and create predictor variables.
Model Building: Train supervised Machine Learning models.
Model Evaluation: Compare models using performance metrics such as AUC.
Deployment/Application: Demonstrates how the model can support public health surveillance and decision-making.