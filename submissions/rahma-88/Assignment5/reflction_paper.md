# Part C – Reflection Paper
## Loan Approval Prediction Using Machine Learning
### 1. What Did You Implement?
In this project, I replicated the Lesson 5 preprocessing pipeline and built three machine learning classification models to predict loan acceptance. The preprocessing stage includes importing the dataset, cleaning missing values, turning categorical variables into numerical values, controlling outliers, constructing new features, and scaling numerical features where appropriate. The data was separated into training and testing sets following preprocessing.
Logistic Regression, Random Forest, and Decision Tree (my extra classifier) are the three classification methods I taught. To enable a fair comparison of each model's performance, the same processed dataset was used for training. Accuracy, Precision, Recall, and F1-Score were used to assess the models.
### 2. Comparison of Models
All three models were able to forecast whether a loan application would be accepted or denied during the sanity check, however their predictions weren't always the same. Based on linear correlations between the target variable and the features, logistic regression generated reliable predictions. choice trees produced more precise choice rules and occasionally made alternative predictions in complicated situations. By combining the forecasts of numerous decision trees, Random Forest was able to produce predictions that were more dependable and consistent.
Because Random Forest handled complex relationships in the data better than a single Decision Tree and decreased overfitting, it yielded the most realistic results among the three models. Additionally, when the dataset included non-linear patterns, it generated predictions that were more reliable than those made by Logistic Regression.
### 3. Understanding Random Forest
Random Forest is an ensemble machine learning technique used for classification and regression tasks. It operates by constructing numerous Decision Trees using different random samples of the training data. Each tree makes its own prognosis, and the final prediction is established by majority voting. For instance, the Random Forest model predicts authorized if the majority of trees indicate that a loan should be authorized.

Random Forest typically delivers higher accuracy and is less likely to overfit the training data because it uses multiple trees rather than just one.
### 4. Other Algorithm (Decision Tree)
I chose Decision Tree for my third classifier because it offers clear decision criteria and is simple to comprehend. Until a final prediction is made, a decision tree continuously divides data into smaller groups according to the most significant characteristics.

Decision trees have the benefit of being easy to understand and capable of handling both numerical and categorical input. One drawback is that, particularly when the tree gets too deep, it might quickly overfit the training set.
Compared with Logistic Regression and Random Forest, the Decision Tree achieved reasonable performance but generally produced lower evaluation metrics than Random Forest. Random Forest improved upon Decision Tree by combining multiple trees and reducing overfitting.
### 5. Metrics Discussion
According to the evaluation measures, Random Forest performed the best overall, with the highest F1-Score, Accuracy, Precision, and Recall. Although it was less successful in capturing intricate associations in the data, logistic regression likewise performed well and yielded consistent, understandable results. When compared to Random Forest, Decision Tree's overall performance was lower because it was more susceptible to overfitting.

These results suggest that Random Forest is the strongest model for this dataset because it gives balanced performance across all assessment metrics. While decision trees are beneficial for understanding how decisions are formed, they may not be as generalizable as logistic regression when model simplicity and interpretability are crucial.
### 6. My Findings
I would select Random Forest for loan approval prediction based on the project's findings. It generated the most accurate forecasts and had the highest overall performance across all evaluation metrics. It can model intricate links between application variables and loan approval choices and lessen overfitting by integrating numerous decision trees.

Random Forest offers superior prediction accuracy and more consistent performance, even if Decision Trees are easier to display and Logistic Regression is easier to understand. Among the three classifiers assessed in this experiment, Random Forest would be the best model for real-world loan approval systems when prediction quality is crucial.