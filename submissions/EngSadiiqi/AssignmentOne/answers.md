 Define **Data Science** and **Machine Learning**. What is the relationship between them? Use a real-life example to illustrate how they work together.
**Diffinition for Data Science:**
Data Science is the process of collecting, cleaning, analyzing, and interpreting data to discover useful insights and support decision-making.
**Diffiniton for Ml:**
 is a branch of Artificial Intelligence (AI) that enables computers to learn patterns from data and make predictions or decisions without being explicitly programmed for every task.
**Relation Ship**
Machine Learning is a subset of Data Science while Data Science covers the entire workflow of working with data, including data collection, cleaning, analysis, visualization, and interpretation. **so Machine Learning is one of the tools used within Data Science to build predictive models and automate decision-making.
Applicatons:**
Movies watched
Watch time
Ratings given
Search history

3. Describe the **Data Science lifecycle** (from problem definition to deployment). At which stage does Machine Learning typically fit in, and why?
1. Problem Definition

The first step is to identify and clearly define the problem that needs to be solved. The objectives, goals, and expected outcomes are established at this stage.

Example: A school wants to predict which students are at risk of poor academic performance.
2. Data Collection
Relevant data is gathered from various sources such as surveys, databases, websites, sensors, or application logs.
Example: Collect student attendance records, study hours, and exam scores.

3. Data Cleaning and Preprocessings
The collected data is prepared for analysis by handling missing values, removing duplicates, correcting errors, and transforming data into a usable format.

Example: Filling missing attendance records and standardizing grade formats.

4. Compare **Supervised Learning** and **Unsupervised Learning**, giving an example of each.
Comparison of Supervised Learning and Unsupervised Learning
Aspect	Supervised Learning	Unsupervised Learning
**Definition**	supervised is a machine learning technique that learns from labeled data, where the correct output (label) is already known while machine learning technique that learns from unlabeled data, where no target label is provided.
**Goal**	supervised predicts or classifys future outcomes based on known examples while unsupervised discover hidden patterns, structures, or relationships in data.
**Data Requirement** supervised	Requires labeled data (features and target variable).	Requires only input data (features) without labels.

6. What causes **Overfitting**? How can it be prevented?
  1: Small Training Dataset
If the model is trained on too little data, it may memorize the examples instead of learning general rules.
  2: A Very Complex Model
Models with too many parameters or layers can capture unnecessary details from the training data.
  3: Too Many Features
Including irrelevant or noisy features can confuse the model and cause it to learn incorrect patterns.

7. Explain how **training data** and **test data** are split, and why this process is necessary.
1. Training Data

Training data is the portion of the dataset used to teach the Machine Learning model.

The model learns patterns and relationships from this data.
It is used to adjust the model's parameters so it can make predictions.

Example:
If we have 1,000 student records, we may use 800 records as training data to teach a model how study habits affect grades.

2. Test Data

Test data is the portion of the dataset that is kept separate and used to evaluate the model after training.

The model has never seen this data before.
It checks whether the model can make accurate predictions on new, unseen examples.

Example:
The remaining 200 student records are used to test whether the model can correctly predict grades for new students.

Common Split Ratios

A common way to split data is:

80% Training Data
20% Test Data

Other splits can be:

70% Training / 30% Testing
90% Training / 10% Testing

The choice depends on the size of the dataset.

Why Is This Process Necessary?
To Measure Model Performance
Testing on unseen data shows how accurate the model really is.
To Prevent Overfitting
If a model is tested on the same data it trained on, it may only memorize the data instead of learning general patterns.
To Check Generalization
A good model should work well on new data, not just the examples it learned from.

8. Find one **case study** (research paper or article) that explains how Data Science or Machine Learning has been applied in healthcare, business, or transportation. Summarize its findings and identify which part of the Data Science lifecycle it covers.
9. 1. Problem Definition

Healthcare organizations have large amounts of patient data, such as medical history, symptoms, test results, and treatment records. The goal is to use Machine Learning to predict diseases early and help doctors make better decisions.

2. Data Collection

The researchers used healthcare data such as:

Patient age
Blood pressure
Medical test results
Symptoms
Previous health records
3. Data Cleaning and Preparation

The data was prepared by:

Removing incorrect or duplicate records
Handling missing values
Converting medical information into a format suitable for Machine Learning models
4. Machine Learning Application

Machine Learning algorithms were trained to recognize patterns in patient data and predict possible diseases.

For example:

A model can analyze patient information and predict whether a person is at high risk of heart disease.
Doctors can use the prediction to provide early treatment.
5. Findings

The study found that Machine Learning can:

Improve disease prediction accuracy
Help doctors identify high-risk patients earlier
Support faster and better medical decisions
Reduce human error in some diagnostic tasks

However, it also noted that models need high-quality data and must be carefully tested before being used in real healthcare environments.

6. Data Science Lifecycle Stages Covered

This case study covers several parts of the Data Science Lifecycle:

Problem Definition – identifying the need for disease prediction
Data Collection – gathering patient information
Data Preprocessing – cleaning and preparing medical data
Model Building – training Machine Learning algorithms
Evaluation – checking model accuracy
Deployment – using the model to assist healthcare professionals