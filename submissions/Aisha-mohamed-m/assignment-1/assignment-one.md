1. Data Science and Machine Learning: Definitions and Relationship
Data Science

Data Science is an interdisciplinary field that combines statistics, computer science, and domain knowledge to extract meaningful insights from structured and unstructured data. It involves processes such as data collection, cleaning, analysis, visualization, and interpretation to support decision-making.

According to Provost & Fawcett (2013), Data Science focuses on “turning data into actionable knowledge.”

Machine Learning

Machine Learning (ML) is a subfield of artificial intelligence that enables systems to learn patterns from data and make predictions or decisions without being explicitly programmed.

Tom Mitchell (1997) defines ML as:

“A computer program is said to learn from experience E with respect to some task T and performance measure P…”

Relationship Between Data Science and Machine Learning

Machine Learning is a core tool inside Data Science, but Data Science is broader.

Data Science = entire process (data collection → insights → communication)
Machine Learning = modeling technique used within Data Science to predict or classify data
Real-Life Example: Hospital Patient Queue System

In a smart hospital system:

Data Science collects patient data (arrival time, symptoms, waiting time)
Machine Learning predicts:
which patients are urgent
estimated waiting time
doctor workload

 ML is used inside the Data Science pipeline to improve decision-making and efficiency.

2. Data Science Lifecycle and Machine Learning Placement

The Data Science lifecycle typically includes:

Stages
Stage	Description
1. Problem Definition	Define business or research goal
2. Data Collection	Gather raw data from sources
3. Data Cleaning	Handle missing, noisy, or incorrect data
4. Exploratory Data Analysis (EDA)	Understand patterns and trends
5. Feature Engineering	Select and transform variables
6. Modeling (Machine Learning stage)	Build predictive models
7. Evaluation	Test model accuracy and performance
8. Deployment	Put model into real system
9. Monitoring	Track performance over time
Where Machine Learning Fits

Machine Learning mainly occurs in:

Feature Engineering
Modeling
Evaluation
Why?

Because ML algorithms require:

Clean data
Structured features
Defined target outputs (in supervised learning)

ML transforms raw data into predictive models used for decision-making.

3. Supervised vs Unsupervised Learning
Supervised Learning

Supervised learning uses labeled data (input + correct output).

Example:

Predicting whether a patient has diabetes:

Input: age, BMI, glucose level
Output: diabetic / non-diabetic

Common algorithms:

Linear Regression
Decision Trees
Random Forest
Neural Networks
Unsupervised Learning

Unsupervised learning uses unlabeled data and finds hidden patterns.

Example:

Grouping hospital patients based on symptoms:

No predefined labels
System clusters similar patients together

Common algorithms:

K-Means Clustering
Hierarchical Clustering
PCA
Comparison Table
Feature	Supervised Learning	Unsupervised Learning
Data Type	Labeled	Unlabeled
Goal	Prediction	Pattern discovery
Output	Known categories/values	Clusters/groups
Example	Disease prediction	Patient segmentation
4. Overfitting: Causes and Prevention
What is Overfitting?

Overfitting occurs when a model learns the training data too well, including noise and irrelevant details, resulting in poor performance on new data.

Causes of Overfitting
Too complex model (e.g., deep decision trees)
Small training dataset
Too many features
Lack of regularization
Training too long
Prevention Methods
Method	Explanation
Train/Test Split	Evaluate model on unseen data
Cross-validation	Use multiple data splits
Regularization (L1/L2)	Penalize complexity
Pruning	Simplify decision trees
More Data	Improves generalization
Early Stopping	Stop training before overfitting
5. Training Data vs Test Data Split
Definition
Training data: used to teach the model patterns
Test data: used to evaluate model performance on unseen data
Common Split Ratio
70% training / 30% testing
or 80% training / 20% testing
Why This is Necessary

Without splitting:

The model may only memorize data (overfitting)
We cannot measure real-world performance
Simple Illustration
Dataset Type	Purpose
Training Set	Model learning
Test Set	Performance evaluation

Optionally, a validation set is used for tuning parameters.

6. Case Study: Machine Learning in Healthcare
Study: Predicting Hospital Readmission Using Machine Learning

(Source: Obermeyer et al., Science, 2019; and related healthcare ML studies)

Problem

Hospitals want to predict which patients are likely to be readmitted within 30 days after discharge.

Method
Data collected from electronic health records (EHR)
Features included:
age
medical history
diagnosis codes
previous admissions
ML models used:
Logistic Regression
Random Forest
Gradient Boosting
Findings
Machine Learning models improved prediction accuracy compared to traditional statistical methods.
Hospitals could identify high-risk patients early.
Interventions (follow-ups, medication monitoring) reduced readmission rates.
Impact
Improved healthcare efficiency
Reduced hospital costs
Better patient outcomes
Lifecycle Stage Covered
Lifecycle Stage	How It Appears in Case Study
Problem Definition	Reduce readmission rates
Data Collection	EHR data from hospitals
Data Cleaning	Standardizing medical records
Feature Engineering	Creating risk indicators
Modeling	ML algorithms applied
Evaluation	Accuracy, ROC-AUC scores
Deployment	Hospital decision systems

 This case study covers the full Data Science lifecycle, especially strong in the modeling and deployment stages.

References
Provost, F. & Fawcett, T. (2013). Data Science for Business. O’Reilly Media.
Mitchell, T. (1997). Machine Learning. McGraw Hill.
James, G. et al. (2021). An Introduction to Statistical Learning. Springer.
Bishop, C. (2006). Pattern Recognition and Machine Learning. Springer.
Obermeyer, Z. et al. (2019). “Dissecting racial bias in an algorithm used to manage the health of populations.” Science.
Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press.