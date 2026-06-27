1. Definition of Data Science and Machine Learning
What is Data Science?

Data Science is an interdisciplinary field that combines statistics, mathematics, computer science, and domain knowledge to collect, process, analyze, and interpret data. Its primary objective is to extract meaningful insights from structured and unstructured data to support decision-making and solve real-world problems.

Data scientists use programming languages such as Python and R, along with visualization and machine learning techniques, to discover patterns hidden within large datasets.

What is Machine Learning?

Machine Learning (ML) is a branch of Artificial Intelligence (AI) that enables computers to learn from data without being explicitly programmed. Instead of following fixed rules, machine learning algorithms identify patterns in historical data and use those patterns to make predictions or decisions.

Machine learning systems improve their performance as they are exposed to more data.

Relationship Between Data Science and Machine Learning

Machine Learning is one of the major tools used within Data Science.

Data Science covers the complete process of collecting, cleaning, analyzing, visualizing, and interpreting data, whereas Machine Learning focuses specifically on building predictive models using data.

Therefore:

Data Science is the broader discipline.
Machine Learning is a subset of Data Science.
Real-Life Example

Netflix recommends movies based on users' viewing history.

Data Science collects and prepares user data.
Machine Learning analyzes viewing patterns.
The trained model predicts movies each user is likely to enjoy.
Recommendations improve as more user data becomes available.
2. Data Science Lifecycle

The Data Science lifecycle consists of several stages that transform raw data into useful knowledge.

Stage	Description
Problem Definition	Understand the business problem and define objectives.
Data Collection	Gather data from databases, sensors, APIs, or surveys.
Data Cleaning	Remove missing values, duplicates, and incorrect data.
Exploratory Data Analysis (EDA)	Analyze patterns using statistics and visualization.
Feature Engineering	Select and transform variables that improve model performance.
Model Building	Train Machine Learning algorithms using prepared data.
Model Evaluation	Measure model performance using evaluation metrics.
Deployment	Deploy the model into a real-world application.
Monitoring	Continuously monitor and update the model as new data arrives.
Where Does Machine Learning Fit?

Machine Learning is mainly used during the Model Building stage.

At this stage:

Algorithms learn from historical data.
Models identify patterns.
Predictions are generated for future data.

Machine Learning also contributes to model evaluation and continuous improvement after deployment.

3. Supervised Learning vs Unsupervised Learning
Feature	Supervised Learning	Unsupervised Learning
Training Data	Labeled data	Unlabeled data
Goal	Predict known outcomes	Discover hidden patterns
Output	Classification or Regression	Clustering or Association
Example	Predict house prices	Customer segmentation
Supervised Learning Example

A bank uses previous loan records to predict whether a customer will repay a loan.

The historical data already contains the correct answers (loan repaid or defaulted), allowing the algorithm to learn.

Unsupervised Learning Example

A retail company groups customers according to purchasing behavior without knowing customer categories beforehand.

The algorithm automatically discovers similar groups of customers.

4. Overfitting
What is Overfitting?

Overfitting occurs when a Machine Learning model learns not only the meaningful patterns in the training data but also random noise and minor details.

As a result:

Excellent performance on training data.
Poor performance on unseen test data.
Causes of Overfitting

Common causes include:

Small datasets
Excessively complex models
Too many features
Insufficient training data
Training the model for too many iterations
Preventing Overfitting

Several techniques help reduce overfitting:

Collect more training data.
Use cross-validation.
Apply regularization techniques.
Reduce unnecessary features.
Use early stopping.
Simplify the model.
Prune decision trees.
Apply dropout (for neural networks).
5. Training Data and Test Data

Machine Learning datasets are usually divided into:

Training Set
Test Set

A common split is:

80% Training Data
20% Test Data

Other common splits include:

70/30
75/25
Why Is Data Split?

Training data is used to teach the model.

Test data is kept separate until training is complete.

Testing on unseen data helps determine whether the model can generalize to new information rather than memorizing the training data.

Without a test set, model accuracy may appear unrealistically high.

6. Case Study
Healthcare: Detecting Diabetic Retinopathy Using Deep Learning
Background

Diabetic Retinopathy is a leading cause of blindness worldwide.

Researchers at Google developed a Deep Learning model capable of detecting diabetic retinopathy from retinal images.

Method

The researchers collected thousands of labeled retinal images.

The images were cleaned and prepared before training a convolutional neural network (CNN).

The model learned to distinguish healthy eyes from diseased eyes.

Findings

The model achieved high sensitivity and specificity, comparable to experienced ophthalmologists.

The study demonstrated that Machine Learning can assist doctors by providing faster and more accurate screening.

Data Science Lifecycle Covered

The study includes almost every stage of the Data Science lifecycle:

Problem Definition
Data Collection
Data Preparation
Feature Learning
Model Training
Evaluation
Deployment for clinical screening
Conclusion

Data Science transforms raw data into valuable knowledge through systematic processes such as data collection, preparation, analysis, modeling, and deployment. Machine Learning is an essential component of this process because it enables predictive models that improve decision-making. Understanding concepts such as supervised learning, unsupervised learning, overfitting, and data splitting is fundamental for building reliable machine learning systems. Modern applications in healthcare, finance, transportation, and business continue to demonstrate the growing importance of Data Science and Machine Learning in solving real-world problems.

References (APA Style)
Provost, F., & Fawcett, T. (2013). Data Science for Business. O'Reilly Media.
James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). An Introduction to Statistical Learning (2nd ed.). Springer.
Géron, A. (2023). Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow (3rd ed.). O'Reilly Media.
Bishop, C. M. (2006). Pattern Recognition and Machine Learning. Springer.
LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep Learning. Nature, 521(7553), 436–444.
Gulshan, V., et al. (2016). Development and Validation of a Deep Learning Algorithm for Detection of Diabetic Retinopathy in Retinal Fundus Photographs. JAMA, 316(22), 2402–2410.