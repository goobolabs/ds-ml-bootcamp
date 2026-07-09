# Part C – Reflection Paper

## What Did I Implement?

In this project, I reproduced the Lesson 5 preprocessing pipeline and applied it to a loan approval dataset. The preprocessing steps included loading the dataset, handling missing values, removing duplicates, encoding categorical variables, and splitting the data into training and testing sets. These steps ensured that the data was clean and suitable for machine learning models.

After preprocessing, I trained three classification algorithms to predict loan approval:

1. Logistic Regression
2. Random Forest
3. Decision Tree (additional algorithm)

Each model was trained using the same training data and evaluated on the same testing data to ensure a fair comparison. I then measured their performance using Accuracy, Precision, Recall, and F1-Score.

---

# Comparison of Models

During the sanity check, the three models produced similar predictions for many loan applications, but there were also some differences. Logistic Regression made predictions based on probability and performed well on simple patterns. Decision Tree produced decisions by following a sequence of rules, which made it easy to understand but sometimes resulted in overfitting. Random Forest combined the predictions of many decision trees and generally produced more stable and accurate results.

Among the three models, Random Forest gave the most realistic predictions because it reduced the effect of overfitting and was better at handling complex relationships within the dataset. Logistic Regression served as a strong baseline model, while Decision Tree was useful for understanding how classification decisions were made.

---

# Understanding Random Forest

Random Forest is an ensemble machine learning algorithm that consists of multiple Decision Trees. Instead of relying on a single tree, it trains many trees using different random samples of the dataset. Each tree independently predicts the class of a new observation.

For classification problems, the final prediction is determined using a majority vote. The class predicted by most trees becomes the final output. This approach improves prediction accuracy and reduces the risk of overfitting compared to using a single Decision Tree.

---

# Other Algorithm (Decision Tree)

The additional algorithm I selected was Decision Tree.

I chose Decision Tree because it is simple to understand and provides a clear visualization of how decisions are made. The model works by repeatedly splitting the dataset according to the most informative features until a final decision is reached.

One major advantage of Decision Tree is that it is easy to interpret and explain. However, one limitation is that it can easily overfit the training data if the tree grows too deep.

Compared with Logistic Regression and Random Forest, the Decision Tree achieved reasonable performance but generally produced lower evaluation metrics. Random Forest achieved the highest overall performance because it combines multiple trees, while Logistic Regression remained competitive because of its simplicity and efficiency.

---

# Metrics Discussion

The evaluation metrics showed that Random Forest achieved the best overall Accuracy, Precision, Recall, and F1-Score. This indicates that it correctly classified more loan applications while maintaining a good balance between false positives and false negatives.

Logistic Regression performed well and provided a simple, interpretable model, but it struggled with more complex relationships in the data. Decision Tree was easy to understand but showed signs of overfitting, resulting in lower performance on the testing dataset.

The comparison demonstrates that each model has strengths and weaknesses. Logistic Regression is efficient and interpretable, Decision Tree is easy to visualize, and Random Forest offers higher predictive performance by combining multiple decision trees.

---

# My Findings

Based on the experimental results, I would choose Random Forest for loan approval prediction. It consistently achieved the best evaluation metrics and produced the most reliable predictions. By combining multiple decision trees, it reduces overfitting and performs well even when the relationships between variables are complex.

Although Logistic Regression is easier to interpret and Decision Tree is simpler to explain, Random Forest provides a better balance between accuracy and generalization. For real-world financial applications such as loan approval prediction, reliable predictions are essential because incorrect decisions may result in financial losses or unfair rejection of qualified applicants. Therefore, Random Forest would be my preferred model for this task.

---

# Conclusion

This project improved my understanding of the complete machine learning classification process, including data preprocessing, model training, model evaluation, and performance comparison. It also demonstrated that selecting the appropriate algorithm depends on the characteristics of the dataset and the goals of the prediction task. Among the three classifiers, Random Forest provided the best overall performance for predicting loan approval.