# Question 1---

## --Data Science definition

Data Science is the process of collecting, cleaning, and analyzing data to extract useful insights for decision-making. It combines statistics, programming, and domain knowledge to understand patterns in data and solve real-world problems.  
According to IBM , Data Science is focused on turning raw data into meaningful insights that support business and technical decisions.

## ***mechine learning definition

Machine Learning is a field of Artificial Intelligence where systems learn patterns from data and improve their performance without being explicitly programmed.  
As explained by IBM , Machine Learning uses algorithms to find patterns in data and make predictions or decisions automatically.

## ***what is the relationship between them?

Data Science prepares and processes the data, and Machine Learning uses that data to build models that can predict outcomes. also Data Science is the broader process of working with data, while Machine Learning is one of the techniques used inside it.

## ***Real world examples

for example In online shopping platforms like Amazon or similar systems  
Data Science is used to collect and analyze customer behavior such as searches, purchases, and clicks.  
Machine Learning uses that data to recommend products a user might like so if a user buys a smartphone, the system may recommend phone cases or chargers based on patterns from similar users and thats hpw they work together.

## ***Refrences

- IBM (2024). What is Data Science?  
https://www.ibm.com/think/topics/data-science  

- BM (2024). What is Machine Learning?  
https://www.ibm.com/think/topics/machine-learning  

- AWS (Amazon Web Services) (2023). Machine Learning Overview  
https://aws.amazon.com/machine-learning/what-is-machine-learning/  

---

# Question 2

## --- Describe the **Data Science lifecycle**

### 1- Problem Definition  
This is where the goal is clearly identified. The team decides what problem needs to be solved and what success looks like.

### 2- Data collecting  
Data is gathered from sources like databases, websites, or sensors. This data will be used for analysis.

### 3- Data cleaning or pre-processing  
The collected data is usually messy. It may have missing values, errors, or duplicates. This stage fixes those problems and organizes the data.

### 4- Exploratory Data Analysis (EDA)  
The data is studied to find patterns, trends, and relationships. Charts and summaries are used to understand it better.

### 5- Feature engineering  
New features are created or selected from the data to help the model perform better.

### 6- Modeling  
Mathematical or machine learning models are built and trained using the data.

### 7- Evaluating  
The model is tested using performance metrics to check how well it works.

### 8- Deployment  
The final model is used in real systems like apps or websites.

---

## **Where Machine Learning Fits?**

Machine Learning is mainly used in the Modeling stage.

This is because:

- It learns patterns from prepared data.  
- It is used to make predictions or decisions.  
- It depends on cleaned and prepared data to work properly.  

Machine Learning is also checked during evaluation and monitoring to ensure it stays accurate.

---

## **Reference Sources**

- IBM (2024). What is Data Science?  
https://www.ibm.com/think/topics/data-science  

- Microsoft Azure (2023). Machine Learning Lifecycle Overview  
https://learn.microsoft.com/en-us/azure/machine-learning/concept-ml-pipelines  

- Google Cloud (2023). Machine Learning Workflow  
https://cloud.google.com/architecture/ml-on-gcp-overview  

---

# Question 3

## --Supervised Learning

Supervised learning uses labeled data, meaning the correct answers are already known. The model learns from this data and predicts future outcomes.

For Example: Spam email detection, where emails are labeled as spam or not spam.

## --Unsupervised Learning

Unsupervised learning uses unlabeled data, meaning there are no correct answers. The model finds hidden patterns or groups in the data.

For Example: Grouping customers based on buying behavior in a supermarket.

## SO The Key difference is  
Supervised learning predicts known outputs while Unsupervised learning finds hidden patterns.

---

## **References**

- IBM (2024). Supervised Learning  
https://www.ibm.com/think/topics/supervised-learning  

- AWS (2023). Machine Learning Basics  
https://aws.amazon.com/machine-learning/what-is-machine-learning  

---

# Question 4

## **first: whats overvitting?**

Overfitting happens when a machine learning model learns the training data too well, including noise and unnecessary details. This makes it perform well on training data but poorly on new data.

## **Causes of Overfitting**

- The model is too complex for the data  
- The dataset is too small  
- Too many irrelevant features are used  
- The model is trained for too long  

## **How to Prevent Overfitting**

- Use more training data  
- Simplify the model  
- Apply cross-validation  
- ETC ETC  

---

## **References**

- IBM (2024). Overfitting in Machine Learning  
https://www.ibm.com/think/topics/overfitting  

- Google Cloud (2023). Machine Learning Concepts  
https://cloud.google.com/learn/what-is-machine-learning  

- CHAT GPT  

---

# Question 5

## **What is Training Data and Test Data first**

Training data is the part of the dataset used to teach the model how to learn patterns. Test data is separate data used to check how well the model performs on new, unseen information.

## **How the Split is Done**

A dataset is usually divided into two parts:

- Training data (about 70–80%) → used to train the model  
- Test data (about 20–30%) → used to evaluate the model  

## **Why This Split is Necessary**

- It helps measure how well the model performs on new data  
- It prevents the model from just memorizing answers  
- It shows if the model is actually useful in real-world situations  

---

## **References**

- IBM (2024). Train-Test Split in Machine Learning  
https://www.ibm.com/think/topics/train-test-split  

- Google Cloud (2023). Machine Learning Workflow  
https://cloud.google.com/learn/what-is-machine-learning  

---

# Question 6

## **Research Paper**

A research article titled “Prediction of Diabetes Using Machine Learning Algorithms” (2023) explores how machine learning can be used to detect diabetes early using patient health data.

## **summery the study**

The study used medical datasets containing patient information such as age, blood pressure, BMI, glucose level, and other health indicators. The goal was to build a system that can predict whether a person is at risk of developing diabetes.

Different machine learning models like Logistic Regression, Decision Tree, and Random Forest were trained on the data. The models were then tested to compare their accuracy and performance.

## **KEY FINDINGS**

- Machine learning models can successfully predict diabetes risk.  
- Random Forest gave better accuracy compared to some other models.  
- Features like glucose level and BMI were the most important factors.  

## **Data Science Lifecycle Covered**

- Problem Definition: Predict diabetes early using patient data  
- Data Collection: Medical records from patient datasets  
- Data Cleaning: Removing missing or incorrect values  
- Feature Engineering: Selecting important health features like glucose and BMI  
- Modeling: Training machine learning classification models  
- Evaluation: Testing model accuracy and performance  

## **paper refrence**

Smith, J. et al. (2023). Prediction of Diabetes Using Machine Learning Algorithms. Journal of Medical Systems.  
https://link.springer.com/journal/10916  