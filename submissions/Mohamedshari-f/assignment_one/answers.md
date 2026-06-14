1. Define Data Science and Machine Learning. What is the relationship between them? Use a real-life example to illustrate how they work together.

Data Science

Data Science is an interdisciplinary field that uses statistics, programming, and domain knowledge to collect, process, analyze, and interpret data in order to extract useful insights and support decision-making.

Machine Learning

Machine Learning (ML) is a branch of Artificial Intelligence (AI) that enables computers to learn patterns from data and make predictions without being explicitly programmed.

Relationship Between Data Science and Machine Learning

Data Science is the broader field that includes data collection, cleaning, analysis, visualization, and interpretation. Machine Learning is a tool used within Data Science to build predictive models. In other words, Machine Learning helps Data Science solve problems that require prediction or automation.

Real-Life Example

Netflix collects and analyzes user viewing data through Data Science techniques. Machine Learning algorithms then use this data to recommend movies and TV shows based on a user's preferences and viewing history.


2. Describe the Data Science lifecycle (from problem definition to deployment). At which stage does Machine Learning typically fit in, and why?

The Data Science lifecycle consists of the following stages:

1. Problem Definition
2. Data Collection
3. Data Cleaning
4. Exploratory Data Analysis (EDA)
5. Feature Engineering
6. Modeling
7. Evaluation
8. Deployment

Where Does Machine Learning Fit?

Machine Learning typically fits in the Modeling Stage because the data must first be collected, cleaned, and prepared before a model can learn patterns and make predictions.


3. Compare Supervised Learning and Unsupervised Learning, giving an example of each.

Supervised Learning:
Uses labeled data and predicts known outcomes.
Example: Spam Detection.

Unsupervised Learning:
Uses unlabeled data and finds hidden patterns.
Example: Customer Segmentation.

Supervised Learning Example

A spam filter is trained using emails labeled as "Spam" or "Not Spam." It then predicts whether new emails are spam.

Unsupervised Learning Example

A retail company groups customers based on purchasing behavior without predefined categories.


4. What causes Overfitting? How can it be prevented?

What is Overfitting?

Overfitting occurs when a Machine Learning model learns the training data too well, including noise and unnecessary details. As a result, it performs well on training data but poorly on new data.

Causes of Overfitting

- Small training datasets
- Too many features
- Complex models
- Excessive training

Prevention Methods

- Use more training data
- Apply regularization techniques
- Use simpler models
- Perform cross-validation
- Use feature selection
- Apply early stopping


5. Explain how training data and test data are split, and why this process is necessary.

A dataset is usually divided into:

Training Data (80%) – Used to train the model.

Test Data (20%) – Used to evaluate the model.

Why Is This Necessary?

The train-test split helps determine whether the model can perform well on unseen data rather than simply memorizing the training data.

Example

If a dataset contains 10,000 records:

8,000 records are used for training.

2,000 records are used for testing.

This process helps measure the model's real-world performance and detect overfitting.


6. Case Study: Machine Learning in Healthcare

Case Study

Predicting Cardiovascular Risk Factors from Retinal Fundus Photographs Using Deep Learning

This study used Deep Learning to predict cardiovascular risk factors from retinal fundus photographs. Researchers trained a neural network using thousands of eye images to identify health indicators such as age, blood pressure, and smoking status. The results showed that the model could accurately predict several cardiovascular risk factors. This demonstrates how Machine Learning can support early disease detection and assist healthcare professionals in making better clinical decisions.

Data Science Lifecycle Stages Covered

Data Collection

Data Preprocessing

Modeling

Evaluation

