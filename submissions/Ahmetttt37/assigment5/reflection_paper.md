Part C — Reflection Paper
1. What did you implement?

In this assignment, I reproduced the Lesson 5 machine learning workflow using a loan approval dataset. First, I implemented a full preprocessing pipeline that included data cleaning, handling missing values, fixing categorical inconsistencies, removing duplicates, and performing outlier treatment using IQR capping. I also engineered new features such as Debt-to-Income ratio and Income per Year Employed to improve model performance.

After preprocessing, I trained three classification models to predict loan approval: Logistic Regression and Random Forest from the lesson, and an additional model I researched, Decision Tree Classifier. Finally, I evaluated all models using accuracy, precision, recall, F1-score, confusion matrix, and a single-row prediction sanity check.

2. Comparison of Models

During the sanity check, I observed that the three models did not always agree on the same prediction for individual loan applications. Logistic Regression produced more linear and conservative predictions, while Random Forest showed more stable and balanced predictions due to averaging multiple decision trees. The Decision Tree model tended to overfit slightly and produced more extreme or rule-based predictions.

Overall, Random Forest gave the most realistic and consistent results because it combines multiple decision trees and reduces overfitting compared to a single decision tree.

3. Understanding Random Forest

Random Forest is an ensemble learning algorithm used for classification and regression tasks. It works by building multiple decision trees on different random subsets of the training data. Each tree makes a prediction, and the final output is determined by majority voting (for classification).

This approach improves accuracy and reduces overfitting compared to a single decision tree. It is widely used in real-world applications such as credit scoring, fraud detection, and risk analysis.

4. Other Algorithms (Decision Tree)

For the third classifier, I chose the Decision Tree algorithm because it is simple, interpretable, and commonly used in classification problems.

From my research, I learned that a decision tree splits the dataset into branches based on feature conditions until it reaches a decision outcome.

Advantage: It is very easy to understand and interpret visually.
Limitation: It can easily overfit the training data if not properly controlled.

When comparing metrics, the Decision Tree performed slightly worse than Random Forest but was sometimes similar to Logistic Regression. Random Forest generally had better and more stable performance.

5. Metrics Discussion

Among the three models, Random Forest achieved the best overall performance in terms of Accuracy, Precision, Recall, and F1-score. Logistic Regression performed reasonably well but was slightly weaker in capturing complex patterns in the dataset. The Decision Tree showed competitive results but was less stable and more sensitive to small changes in the data.

This indicates that Random Forest is more robust and generalizes better, while Logistic Regression is simpler but less flexible, and Decision Tree is highly interpretable but prone to overfitting.

6. Your Findings

Based on my experiments, I would choose the Random Forest model for loan approval prediction. This is because it consistently provides higher performance across all evaluation metrics and reduces the risk of overfitting by combining multiple decision trees.

Although Logistic Regression is faster and easier to interpret, it may not capture complex relationships in financial data. The Decision Tree is useful for explanation and interpretability, but it is less reliable on unseen data. Therefore, Random Forest offers the best balance between accuracy and robustness for real-world loan approval prediction.