# Part A — Theory
## 1. Introduction to Classification

**Classification** is a supervised machine learning technique used to predict labels or categories from input data. It assigns each data point to a predefined class based on learned patterns

* How is it different from regression?
 - Classification predicts categories or labels like spam/not spam, disease/no disease, etc.
 - Regression predicts continuous values like price, temperature, sales, etc.

###  one real-life example of classification and one of regression.

 ### Classification Example: Email Spam DetectionInput Data: 
 The sender's email address, the subject line, keywords used in the body (e.g., "win," "limited time," "invoice"), and hyperlinks.
 **Output**: A discrete category predicting whether the email is Spam or Not Spam.
 **Use Case**: Email providers (like Gmail or Outlook) use classification models to automatically filter out junk mail into a separate folder before it ever reaches your primary inbox.

### Regression Example: Real Estate Price PredictionInput Data: 
House size (in square meters), number of bedrooms, location, and age of the property.
**Output**: A continuous numerical value representing the estimated price of the house in a specific currency (such as USD or Somali Shilling).
**Use Case**: Property platforms (such as Zillow) use regression to determine a listing's expected market value, or to help buyers estimate how much a house is worth based on its specific attributes

## 2. Classification Algorithms

## Logistic Regression
Logistic Regression is a supervised machine learning algorithm used for classification problems. Unlike linear regression, which predicts continuous values it predicts the probability that an input belongs to a specific class.

- It is used for binary classification where the output can be one of two possible categories such as Yes/No, True/False or 0/1.
- It uses sigmoid function to convert inputs into a probability value between 0 and 1.

##### how it works (basic idea)
Predicts the probability of a class using a logistic (sigmoid) function and assigns the most likely class.

#### advantage of logistic regression
- Logistic regression is easier to implement, interpret, and very efficient to train.
- It is very fast at classifying unknown records.

### real-world use case in Logistic Regression
Disease Prediction (Disease / No Disease)

### limitations of Logistic Regression
May perform poorly on complex non-linear relationships

## Decision Trees
A decision tree is a supervised learning algorithm used for both classification and regression tasks. It has a hierarchical tree structure which consists of a root node, branches, internal nodes and leaf nodes. It works like a flowchart that helps in making step-by-step decisions, where:

- Internal nodes represent attribute tests
- Branches represent attribute values
- Leaf nodes represent final decisions or predictions.

### How Does a Decision Tree Work
A decision tree splits the dataset based on feature values to create pure subsets ideally all items in a group belong to the same class. Each leaf node represents the final output, which can be a class label (in classification) or a continuous value (in regression). 

### advantage of Decision Trees
- Easy to Understand and Interpret
- Handle Both Categorical and Numerical Data
- Automatic Feature Selection
- Can Handle Missing Values

### real-world use case in Decision Trees
Medical diagnosis (Disease/No Disease).

### limitation of Decision Trees
Can overfit the training data and become unstable with small data changes.

## Random Forest
Random Forest is a machine learning algorithm that uses many decision trees to make better predictions. Each tree looks at different random parts of the data and their results are combined by voting for classification or averaging for regression which makes it as ensemble learning technique. This helps in improving accuracy and reducing errors.

### Working of Random Forest Algorithm
- Create Many Decision Trees: 
- Pick Random Features
- Each Tree Makes a Prediction
- Combine the Predictions

### advantage of Random Forest
- Random forests reduce the risk of overfitting
- allow for customized hyperparameters
- allow you to measure the relative importance of each feature in your model.

### real-world use case in Random Forest
Credit risk assessment and fraud detection.

### limitation of random forest
More computationally expensive and less interpretable than a single Decision Tree.


## 3. Classification Metrics

**accuracy** is a performance metric that measures the percentage of correct predictions a model makes out of all predictions

**Precision** in machine learning is the proportion of positive predictions made by a model that are actually correct.

**Recall** is an evaluation metric that measures the percentage of actual positive cases a model successfully identified.

**F1-Score** is a machine learning metric used to evaluate a classification model.

**A confusion matrix** is a table used to evaluate the performance of a classification machine learning model.


### Comparison Table
| Metric               | What It Measures                     | Formula               | Best Used When                | Sensitivity to Class Imbalance |
| -------------------- | ------------------------------------ | --------------------- | ----------------------------- | ------------------------------ |
| **Accuracy**         | Overall correctness of predictions   | (TP + TN) / Total     | Classes are balanced          | **High** (can be misleading)   |
| **Precision**        | Correctness of positive predictions  | TP / (TP + FP)        | False positives are costly    | **Low–Moderate**               |
| **Recall**           | Ability to find actual positives     | TP / (TP + FN)        | False negatives are costly    | **Low–Moderate**               |
| **F1-Score**         | Balance between Precision and Recall | 2 × (P × R) / (P + R) | Need a single balanced metric | **Low**                        |
| **Confusion Matrix** | Detailed prediction breakdown        | TP, TN, FP, FN table  | Understanding model errors    | **Not a metric itself**        |


## 4 Class Imbalance

**Why can Accuracy be misleading when classes are imbalanced?**
Accuracy is misleading with imbalanced classes because it heavily reflects the majority class while masking poor performance on the minority class.

**When would you prioritize Precision over Recall?**
Precision is prioritized when approving a bad loan is costly.

Loan approval example:
A bank wants to avoid giving loans to risky borrowers. High Precision means most approved loans go to reliable customers.

**When would you prioritize Recall over Precision?**
Recall is prioritized when missing qualified borrowers is costly.

Loan approval example:
A bank wants to approve as many eligible customers as possible. High Recall means fewer qualified applicants are wrongly rejected.

# Real-World Case Study: Student Performance Prediction


## Project Goal

The goal of this project was to predict whether a student would **pass** or **fail** before the end of the academic term. By identifying at-risk students early, schools and teachers could provide additional support and interventions to improve academic outcomes.

## Data Used

The dataset included information about students such as:

* Attendance rate
* Previous grades
* Study time
* Family support
* Internet access
* Participation in extracurricular activities

### Target Variable

* **Pass**
* **Fail**

## Classification Algorithm Used

**Decision Tree Classifier**

A Decision Tree classifier makes predictions by splitting data into branches based on feature values. For example, it may ask questions such as:

* Is attendance greater than 80%?
* Is the previous grade above 60%?

Based on the answers, the model classifies the student as either likely to pass or fail.

## Key Results and Insights

* The model successfully identified students who were at risk of failing.
* Teachers were able to provide additional academic support to these students.
* Early intervention helped improve overall student performance.
* The model provided an interpretable way to understand factors affecting student success.

                            |

## Conclusion

This case study demonstrates how classification can be applied in education to predict student performance. Using a Decision Tree classifier, schools can identify students who may struggle academically and take proactive measures to improve their chances of success.


