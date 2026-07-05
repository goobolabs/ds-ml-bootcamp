Reflection Paper

Assignment Five: Classification — Theory and Practice

1. What Did You Implement?

In this assignment, I reproduced the Lesson 5 preprocessing pipeline and built three machine learning classification models to predict loan approval. The raw loan dataset was cleaned by removing currency symbols, correcting inconsistent category values, filling missing values, removing duplicate records, capping outliers, encoding categorical variables, engineering new features, and scaling the numeric features using RobustScaler.

After preprocessing, I trained three classification models: Logistic Regression, Random Forest Classifier, and Decision Tree Classifier. The dataset was divided into training and testing sets using an 80/20 split with stratification to preserve the class distribution. Each model was evaluated using Accuracy, Precision, Recall, F1-Score, and a Confusion Matrix.

---

2. Comparison of Models

The three models produced slightly different predictions during the sanity check. Logistic Regression made predictions based on a linear decision boundary, while Decision Tree created decisions using a sequence of rules. Random Forest combined the predictions of many decision trees through majority voting.

Among the three models, Random Forest generally produced the most reliable and consistent predictions. Logistic Regression performed well but was less effective when relationships between variables became more complex. Decision Tree was easy to understand but occasionally produced unstable predictions because it can overfit the training data.

---

3. Understanding Random Forest

Random Forest is an ensemble learning algorithm that builds many decision trees using random subsets of the training data and random subsets of the available features. Each decision tree predicts a class independently, and the final prediction is determined by the majority vote of all trees.

This approach reduces the weaknesses of individual decision trees by decreasing overfitting and improving generalization. Because multiple trees contribute to the final prediction, Random Forest usually achieves higher accuracy and greater stability than a single Decision Tree.

---

4. Other Algorithm: Decision Tree

For the third classifier, I selected the Decision Tree algorithm. A Decision Tree works by repeatedly splitting the dataset into smaller groups based on feature values until it reaches a final decision. Each path from the root to a leaf represents a classification rule.

One advantage of Decision Trees is that they are easy to understand and visualize. They also handle both numerical and categorical data effectively. However, Decision Trees can overfit the training data if they become too deep, resulting in lower performance on unseen data.

After comparing the evaluation metrics, the Decision Tree achieved reasonable performance but generally produced lower accuracy and F1-Score than Random Forest. This demonstrates the benefit of combining multiple trees rather than relying on a single one.

---

5. Metrics Discussion

The three models were evaluated using Accuracy, Precision, Recall, and F1-Score.

Random Forest achieved the strongest overall performance because it generally produced the highest Accuracy and F1-Score while maintaining good Precision and Recall. Logistic Regression provided competitive results and served as a strong baseline model, especially when relationships between variables were approximately linear. Decision Tree performed adequately but was more sensitive to variations in the training data.

These metrics show that Random Forest is better at balancing correct predictions while minimizing classification errors.

---

6. Findings

This assignment improved my understanding of classification algorithms and the importance of preprocessing data before model training. I learned that data cleaning, feature engineering, and proper evaluation all contribute significantly to model performance.

Among the three algorithms, I prefer Random Forest for loan approval prediction because it consistently provides accurate predictions while reducing the risk of overfitting. Although Logistic Regression is simple and computationally efficient, and Decision Trees are highly interpretable, Random Forest offers the best balance between accuracy, robustness, and reliability for real-world loan approval systems.

Overall, this assignment strengthened my practical skills in data preprocessing, machine learning model development, and classification model evaluation using Python and Scikit-learn.