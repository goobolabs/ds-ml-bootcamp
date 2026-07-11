Assignment Five: Classification 
Part A — Theory
Introduction to Classification
What is Classification in Machine Learning?

Classification is a supervised machine learning technique that predicts the category or class of an observation based on its features. The model learns from labeled training data and then assigns new data to one of the predefined classes. Classification is commonly used when the target variable consists of categories such as "Yes/No," "Approved/Rejected," or "Spam/Not Spam" (IBM, 2024).

Difference Between Classification and Regression

Although both classification and regression are supervised learning methods, they solve different problems. Classification predicts categorical outcomes, while regression predicts continuous numerical values. For example, a classification model may predict whether a loan application will be approved or rejected, whereas a regression model estimates the selling price of a car.

Regression Example: Predicting the selling price of a used car.

Classification Example: Predicting whether a customer will be approved for a loan.

Classification Algorithms
Logistic Regression
Basic Idea

Logistic Regression predicts the probability that an observation belongs to a particular class by using a logistic (sigmoid) function. The probability is converted into a class label using a threshold, usually 0.5 (Google Developers, 2024).

Real-World Use Case

Banks use Logistic Regression to predict whether a customer is likely to repay a loan or default.

Advantages
Easy to understand and implement.
Fast to train.
Works well for binary classification.
Produces probability estimates.
Limitations
Assumes a mostly linear relationship.
Performance decreases with highly complex data.
Decision Trees
Basic Idea

A Decision Tree divides data into smaller groups by asking a sequence of questions based on feature values. The process continues until a final prediction is reached.

Real-World Use Case

Hospitals use Decision Trees to help classify patients according to disease risk based on symptoms and medical test results.

Advantages
Easy to visualize.
Handles numerical and categorical data.
No feature scaling is required.
Limitations
Can easily overfit training data.
Small changes in data may produce different trees.
Random Forest
Basic Idea

Random Forest is an ensemble learning method that combines many Decision Trees. Each tree is trained using different random samples of the data, and the final prediction is determined by majority voting.

Real-World Use Case

Financial institutions use Random Forest to detect fraudulent credit card transactions.

Advantages
High prediction accuracy.
Reduces overfitting compared to a single Decision Tree.
Handles large datasets effectively.
Limitations
Slower than Logistic Regression.
More difficult to interpret than a single Decision Tree.

Comparison of Classification Algorithms
Algorithm	            Basic Idea	                        Example Use	        Advantages	  
Logistic Regression	    Uses probabilities to classify data	Loan approval	Fast, simple, Limitations	Assumes mostly linear relationships

Decision Tree Splits data into branches using rules Disease diagnosis Easy to understand Can overfit

Random Forest	        Combines many Decision Trees	    Fraud detection	    High accuracy, reduces overfitting	    Limitations: Slower and less interpretable

Classification Metrics
Accuracy

Accuracy measures the proportion of correct predictions among all predictions. It is calculated by dividing the number of correct predictions by the total number of observations (Scikit-learn, 2025).

Precision

Precision measures how many predicted positive cases are actually positive. High precision means there are few false positive predictions.

Recall

Recall measures how many actual positive cases are correctly identified by the model. High recall means very few positive cases are missed.

F1-Score

The F1-Score combines Precision and Recall into one value by calculating their harmonic mean. It is useful when both false positives and false negatives are important.

Confusion Matrix

A Confusion Matrix summarizes classification results by showing:

True Positives
True Negatives
False Positives
False Negatives

It provides a detailed view of where the model makes correct and incorrect predictions.

Comparison of Classification Metrics
Metric	            Measures	                            Sensitive to Class Imbalance?
Accuracy	        Overall correct predictions	            Yes
Precision	        Correctness of positive predictions	    Less sensitive
Recall	            Ability to detect positive cases	    Less sensitive
F1-Score	        Balance between Precision and Recall	Suitable for imbalanced data
Confusion Matrix	Counts prediction outcomes	            Useful for all datasets
Class Imbalance

Class imbalance occurs when one class contains significantly more observations than another. In this situation, Accuracy can be misleading because a model may predict only the majority class and still achieve a high accuracy score.

For example, suppose a loan dataset contains 95% approved applications and only 5% rejected applications. A model that predicts every application as "Approved" would achieve 95% accuracy but completely fail to identify rejected applicants.

Precision should be prioritized when approving an ineligible applicant would have serious financial consequences. For example, a bank wants to avoid approving loans for customers who are unlikely to repay them.

Recall should be prioritized when missing qualified applicants is more harmful. In this case, the bank wants to identify as many eligible borrowers as possible, even if some additional applications require manual review.

Real-World Case Study
Loan Approval Prediction Using Machine Learning

A study published on Analytics Vidhya developed a machine learning model to predict loan approval decisions using applicant information such as income, education level, employment status, loan amount, credit history, and marital status. The goal was to help financial institutions make faster and more consistent lending decisions.

The researchers applied classification algorithms, including Logistic Regression and Random Forest, to classify applications as either Approved or Rejected. Before training the models, the data was cleaned, missing values were handled, and categorical variables were encoded.

The study found that Random Forest achieved higher prediction accuracy because it captured more complex relationships among applicant characteristics. Logistic Regression also produced reliable results while remaining easier to interpret. The project demonstrated how classification models can improve decision-making, reduce manual work, and support fairer loan evaluation processes.

References

Google Developers. (2024). Logistic regression. https://developers.google.com/machine-learning/crash-course/logistic-regression

IBM. (2024). What is classification in machine learning? https://www.ibm.com/think/topics/classification-machine-learning

Scikit-learn. (2025). Metrics and scoring: Quantifying the quality of predictions. https://scikit-learn.org/stable/modules/model_evaluation.html

Analytics Vidhya. (2023). Loan prediction using machine learning. https://www.analyticsvidhya.com/blog/2021/07/loan-prediction-using-machine-learning/

Microsoft Learn. (2024). Introduction to classification models. https://learn.microsoft.com/en-us/training/modules/introduction-classification-models/