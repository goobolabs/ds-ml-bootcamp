Part C — Reflection Paper
1. What did I implement?

In this assignment, I implemented a full machine learning pipeline for loan approval prediction. First, I reproduced the Lesson 5 preprocessing steps, including data cleaning, handling missing values, encoding categorical variables, feature engineering, and feature scaling. After preparing the dataset, I trained three classification models: Logistic Regression and Random Forest from the lesson, and an additional model, Decision Tree, which I selected through independent research.

The main objective was to predict whether a loan application would be approved or rejected based on applicant financial and personal features. I also evaluated the models using standard classification metrics and performed a sanity check using individual test samples.

2. Comparison of Models

During the sanity check, the three models sometimes produced similar predictions, but differences appeared in borderline cases. Logistic Regression tended to give more conservative predictions, while Random Forest showed more balanced and accurate results due to its ensemble structure. The Decision Tree model was more sensitive to small changes in the data and sometimes overfitted individual patterns.

Random Forest provided the most realistic and stable predictions overall because it combines multiple decision trees and reduces variance, making it more reliable for real-world loan approval decisions.

3. Understanding Random Forest

Random Forest is an ensemble learning algorithm that builds multiple decision trees and combines their outputs. For classification tasks, each tree makes a prediction, and the final result is determined by majority voting. This approach improves accuracy and reduces overfitting compared to a single decision tree.

Random Forest works well because it introduces randomness in both data sampling and feature selection, which makes the model more robust. It is widely used in classification problems such as credit scoring and fraud detection.

4. Other Algorithms (Decision Tree)

For my third classifier, I selected the Decision Tree algorithm. I chose it because it is easy to understand and interpret, and it helps visualize how decisions are made step by step.

A Decision Tree splits the dataset based on feature conditions until it reaches a final decision (leaf node). One advantage of Decision Trees is that they are simple and require little preprocessing. However, a major limitation is that they are prone to overfitting, especially when the tree becomes too deep.

Compared to Logistic Regression and Random Forest, the Decision Tree performed moderately. It was less accurate than Random Forest but more flexible than Logistic Regression in capturing non-linear relationships.

5. Metrics Discussion

Among the three models, Random Forest achieved the best overall performance in terms of Accuracy, Precision, Recall, and F1-Score. Logistic Regression performed reasonably well but was slightly weaker in capturing complex relationships. The Decision Tree had the lowest stability and was more sensitive to noise.

This shows that Random Forest is more powerful for this dataset because it handles complexity better and reduces overfitting. Logistic Regression is useful for simpler linear relationships, while Decision Trees are easier to interpret but less reliable alone.

6. Your Findings

Based on the results, I would choose the Random Forest model for loan approval prediction. This is because it consistently provided higher accuracy and more balanced precision and recall values compared to the other models. It also handled non-linear relationships in the data better than Logistic Regression.

However, Logistic Regression remains useful when interpretability is required, and Decision Trees can be helpful for understanding decision rules. In a real banking system, Random Forest would be the most practical choice due to its strong predictive performance and robustness.