# Reflection Paper — Loan Approval Prediction

## 1. What did you implement?

**In Part B1**
 I reproduced the Lesson 5 preprocessing pipeline for the loan approval dataset (raw_loan_dataset.csv), which originally contained 103 rows and 7 columns. The pipeline consisted of 11 steps:
Step 1 : Load & Inspect: I imported the necessary libraries including NumPy, Pandas, and scikit-learn, then loaded the raw dataset and inspected it for issues.
Step 2 : Clean Currency Formatting: I removed currency symbols ($) and commas from the Income and LoanAmount columns and converted them to numeric values.
Step 3 : Fix Category Errors: I normalized typos in the HasCollateral, PreviousDefaults, and Approved columns by mapping variants such as Y, yse, approved, and rejected to consistent Yes or No values. This was done before imputation to ensure the mode calculation would be accurate.
Step 4 : Impute Missing Values: I filled missing values using the median for numeric columns and the mode for categorical columns.
Step 5 : Remove Duplicates: I removed duplicate rows, reducing the dataset from 103 to 100 rows.
Step 6 : Outlier Capping (IQR): I handled outliers using the IQR method, calculating upper and lower bounds and clipping extreme values without deleting any rows.
Step 7 : Label Encoding: I mapped Yes/No values to 1 and 0 for the Approved, HasCollateral, and PreviousDefaults columns.
Step 8 : Class Balance Check: I checked class balance and confirmed the dataset was sufficiently balanced (66% Approved, 34% Rejected), making Accuracy a reliable metric.
Step 9 : Feature Engineering: I created two new features: DebtToIncome (LoanAmount / Income) and IncomePerYearEmployed (Income / (EmploymentYears + 1)).
Step 10: Feature Scaling (MinMaxScaler): I chose MinMaxScaler because it transforms all feature values into a range between 0 and 1, preserving the relative differences between values. I selected it over StandardScaler because the dataset's outliers had already been capped in Step 6, and MinMaxScaler is well-suited when there are no extreme outliers and all values are positive
Step 11: I performed a final check to confirm no missing values remained and saved the cleaned dataset as clean_loan_dataset.csv.


**Part B2  Classification Models:**
In Part B2, I loaded the cleaned dataset and separated the features (X) from the target variable (y = Approved). I split the data into 80% training and 20% testing using stratify=y and random_state=42 to preserve the class ratio in both sets.
I trained three classification models: Logistic Regression and Random Forest from the Lesson 5 coding session, plus Naive Bayes as my additional third classifier. I chose Naive Bayes because it performs well on small datasets (only 100 rows), trains quickly, and is well-suited for binary classification problems such as loan approval. Although it assumes all features are independent, it produced the best results among the three models on this dataset.
I evaluated all three models using Accuracy, Precision, Recall, and F1-Score, and printed a confusion matrix for each. Naive Bayes achieved the highest performance (Accuracy: 0.800, F1: 0.857), while Random Forest performed the worst (Accuracy: 0.650) due to the small dataset size  with only 80 training rows, the 100 trees were prone to overfitting. Finally, I performed a sanity check on a single test row, where only Naive Bayes correctly predicted the actual label (Rejected).






## 2. Comparison of Model?
In the sanity check, the three models produced different predictions for the same applicant:

Actual label: Rejected (0)
Logistic Regression: Approved ❌ — incorrect
Random Forest: Approved ❌ — incorrect
Naive Bayes: Rejected ✅ — correct

Naive Bayes was the only model that gave the correct and most realistic result. The reason is that Naive Bayes works using simple probability calculations and does not require large amounts of data to learn patterns effectively. With only 80 training rows, it was sufficient for Naive Bayes to learn the loan approval pattern accurately. Additionally, the loan approval features (Income, CreditScore, LoanAmount) have relatively straightforward relationships that Naive Bayes captures well. It also does not overfit because it is a simple model.
In short: with a small dataset, simpler models such as Naive Bayes and Logistic Regression tend to outperform more complex models such as Random Forest.



## 3. Understanding Random Forest
Random Forest is a Machine Learning algorithm used for both classification and regression. When used for classification, it determines the correct class such as Approved or Rejected without relying on a single Decision Tree alone. Instead, it uses many Decision Trees that work together to reach an accurate decision.
The way it works is by creating many Decision Trees, each trained on a different subset of the training data and features. Each tree makes its own individual prediction, and then all the trees cast their votes (majority vote). The class that receives the most votes becomes the final prediction of the model.
For example, if 100 trees are used and 70 trees predict Approved while 30 trees predict Rejected, the final result will be Approved.
This approach makes Random Forest highly accurate, reduces overfitting, and allows it to perform well on new, unseen data.


## 4. Other Algorithms (Your Third Classifier)
I chose Naive Bayes as my third classifier. Naive Bayes is a classification algorithm based on Bayes' Theorem. It calculates the probability that a given input belongs to a particular class using the features in the dataset. Although it assumes that all features are independent of each other, it often produces accurate and reliable results.
I chose Naive Bayes for this loan approval dataset for the following reasons: the cleaned dataset contains only 100 rows, and Naive Bayes performs well on small datasets as it does not require large amounts of data to learn important patterns. It is also one of the fastest classification algorithms available, training quickly and producing predictions efficiently. Additionally, this is a binary classification problem (Approved = 1, Rejected = 0), which Naive Bayes handles well.
Advantage: Very fast to train and predict; performs well on small datasets; suitable for binary classification.
Limitation: Naive Bayes assumes all features are independent of each other, which is rarely true in real-world data. For example, Income and LoanAmount are likely correlated, which may reduce its accuracy on larger, more complex datasets.
Metrics Comparison:
AccuracyPrecisionRecallF1Logistic Regression0.7500.7500.9230.828Random Forest0.6500.7140.7690.741Naive Bayes0.8000.8000.9230.857
Naive Bayes outperformed both Logistic Regression and Random Forest across all metrics. The main reason is that the dataset is small (only 80 training rows), which favors simpler probabilistic models like Naive Bayes over more complex ensemble models like Random Forest, which requires more data to build reliable trees without overfitting.



## 5. Metrics Discussion
Looking at all four metrics, Naive Bayes was the best-performing model overall, achieving the highest Accuracy (0.800), Precision (0.800), Recall (0.923), and F1-Score (0.857) among the three classifiers.
Naive Bayes: Its strength lies in performing well on small datasets and binary classification problems. Its limitation is that it assumes all features are independent of each other, which is rarely true in real-world data  for example, Income and LoanAmount are likely correlated.
Logistic Regression: Its strength is that it is simple, fast to train, and performs reasonably well on small datasets (Accuracy: 0.750, F1: 0.828). Its limitation is that it cannot capture complex, non-linear relationships between features.
Random Forest: Its strength is its ability to learn complex, non-linear patterns and perform well on large datasets. However, its limitation was clearly shown in this project  with only 80 training rows, the 100 decision trees were prone to overfitting, resulting in the lowest Accuracy (0.650) and F1-Score (0.741) among the three models.

---

## 6. Your Findings

In general, the model I choose depends on the size of the dataset I have. There are two very different scenarios: working with a small dataset versus a large dataset. When I have a small dataset, I would prefer Logistic Regression and Naive Bayes, because as shown in this project, both models outperformed Random Forest. With a dataset of only 100 rows, Logistic Regression and Naive Bayes produced better results than Random Forest. This shows that simpler models perform better on small datasets, as they do not require large amounts of data to learn the relationships between features.

On the other hand, when I have a large dataset, I would choose Random Forest. The reason is that Random Forest performs well with large amounts of data, since it uses many Decision Trees working together to learn complex and non-linear patterns. When data is abundant, Random Forest has enough information to make accurate predictions, making it well-suited for large-scale projects and datasets.