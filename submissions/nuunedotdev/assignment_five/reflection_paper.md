**Part C – Reflection Paper**

**Loan Approval Prediction Using Machine Learning**

**1. What Did You Implement?**

In the current project, I reproduced the Lesson 5 preprocessing pipeline and built three machine learning classification models to predict loan approval. Importing the dataset, removing missing values, converting categorical variables into numerical values, managing outliers, creating new features, and scaling numerical features as necessary are all part of the preprocessing step. After preprocessing, the data was divided into training and testing sets. I introduced three classification techniques: Decision Tree (my additional classifier), Random Forest, and Logistic Regression. To ensure a fair comparison of each model's performance, the same processed dataset was utilized for training. The models were evaluated using F1-Score, Accuracy, Precision, and Recall.

**2. Comparison of Models**

During the sanity check, all three models were able to predict whether a loan application would be approved or rejected, though their forecasts weren't always consistent. Logistic regression produced accurate predictions based on linear correlations between the target variable and the features. choice trees offered more accurate choice rules and occasionally made alternate predictions in difficult scenarios. Random Forest was able to generate predictions that were more reliable and consistent by merging the predictions of multiple decision trees. Out of the three models, Random Forest produced the most realistic results because it reduced overfitting and handled complex relationships in the data better than a single Decision Tree. Furthermore, when the dataset had non-linear patterns, it produced predictions that were more trustworthy than those produced by Logistic Regression when the dataset had non-linear patterns.

**3. Understanding Random Forest**

Random Forest is an ensemble machine learning technique used for classification and regression tasks. It operates by constructing numerous Decision Trees using different random samples of the training data. Each tree makes its own prognosis, and the final prediction is established by majority voting. For instance, the Random Forest model predicts authorized if the majority of trees indicate that a loan should be authorized.



Random Forest typically delivers higher accuracy and is less likely to overfit the training data because it uses multiple trees rather than just one.

**4. Other Algorithm (Decision Tree)**

Decision trees are easy to understand and provide clear decision criteria, which is why I choose them for my third classifier. A decision tree continuously splits data into smaller groups based on the most important features until a final prediction is generated.



One advantage of decision trees is that they can handle both numerical and categorical input and are simple to comprehend. One disadvantage is that the tree may quickly overfit the training set, especially if it becomes very deep. The Decision Tree performed fairly well when compared to Random Forest and Logistic Regression, but Random Forest typically produced higher assessment metrics. By merging several trees and minimizing overfitting, Random Forest outperformed Decision Tree.

**5. Metrics Discussion**

Random Forest had the best overall performance based on the evaluation metrics, including the highest F1-Score, Accuracy, Precision, and Recall. Logistic regression also performed well and produced consistent, intelligible findings, although it was less successful in capturing complex relationships in the data. Because Decision Tree was more prone to overfitting than Random Forest, it performed worse overall.



Because Random Forest provides balanced performance across all assessment metrics, these results imply that Random Forest is the best model for this dataset. Decision trees are useful for comprehending how decisions are made, but when model simplicity and interpretability are important, they might not be as generalizable as logistic regression.

**6. My Results**

Based on the results of the project, I would choose Random Forest for loan acceptance prediction. It performed the best overall across all evaluation metrics and produced the most accurate estimates. By including several decision trees, it helps reduce overfitting and represent complex relationships between application data and loan acceptance decisions.



Even though Decision Trees are simpler to see and Logistic Regression is simpler to comprehend, Random Forest provides better prediction accuracy and more consistent performance. For real-world loan approval systems where prediction quality is critical, Random Forest would be the best model out of the three classifiers evaluated in this experiment.



