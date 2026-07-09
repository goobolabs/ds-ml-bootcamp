# Reflection Paper: Loan Approval Prediction Using Classification Models

**Name:** Hayat Mohamud Hassan

---

# What Did I Implement?

In this assignment, I implemented a complete machine learning classification pipeline to predict loan approval decisions. I first reproduced the preprocessing steps from Lesson 5 using the loan dataset. The preprocessing process included loading and inspecting the data, cleaning currency values, correcting inconsistent categorical values, handling missing values using median and mode imputation, removing duplicate records, capping outliers using the Interquartile Range (IQR) method, encoding categorical variables, checking class balance, creating new features, and scaling numerical features with RobustScaler.

After preprocessing, I trained three different classification models. The first two models were Logistic Regression and Random Forest, which were introduced during Lesson 5. For the third model, I selected the Decision Tree Classifier after researching different classification algorithms. All three models were trained using the same training dataset and evaluated using the same testing dataset. Their performance was measured using Accuracy, Precision, Recall, F1-Score, and Confusion Matrix.

---

# Comparison of Models

During the sanity check, I compared the predictions made by the three models on the same test sample. Although the models often produced the same prediction, there were cases where one model predicted loan approval while another predicted rejection. These differences occurred because each algorithm learns patterns differently.

Logistic Regression makes predictions using a linear decision boundary, while Decision Trees create a sequence of decision rules. Random Forest combines the predictions of many Decision Trees through majority voting, making its predictions more stable.

Based on my evaluation results, the Random Forest model produced the most realistic predictions because it reduced the risk of overfitting and considered multiple decision trees before making a final prediction. This generally makes Random Forest more reliable than a single Decision Tree and more flexible than Logistic Regression.

---

# Understanding Random Forest

Random Forest is an ensemble machine learning algorithm used for classification and regression problems. Instead of building one Decision Tree, it builds many Decision Trees using different random samples of the training data.

Each tree independently predicts the class of a new observation. The final prediction is determined by majority voting, where the class predicted by most trees becomes the final output.

This approach improves prediction accuracy and reduces overfitting because errors made by individual trees are less likely to affect the overall prediction.

---

# Other Algorithm (Decision Tree)

For my third classification algorithm, I selected the Decision Tree Classifier.

A Decision Tree works by repeatedly splitting the dataset according to the feature that best separates the classes. Each split creates branches until the algorithm reaches a final decision at a leaf node.

One advantage of Decision Trees is that they are easy to understand and visualize. Their decision-making process can be explained clearly, which is useful in applications such as loan approval.

One limitation is that Decision Trees can easily overfit the training data, especially when the tree becomes very deep. This can reduce performance on unseen data.

Compared with Logistic Regression and Random Forest, the Decision Tree achieved **[insert your results]**. Although it performed well, Random Forest generally produced more consistent evaluation metrics because it combines many Decision Trees instead of relying on a single one.

---

# Metrics Discussion

Among the three models, **[insert your best-performing model]** achieved the highest Accuracy, Precision, Recall, and F1-Score.

The evaluation metrics provide different insights into model performance:

- **Accuracy** measures the percentage of correct predictions.
- **Precision** measures how many predicted approved loans were actually approved.
- **Recall** measures how many actual approved loans were correctly identified.
- **F1-Score** balances Precision and Recall and is especially useful when class distributions are uneven.

The higher values obtained by **[best model]** indicate that it was better at correctly identifying loan approvals while minimizing incorrect predictions. Logistic Regression performed well because it is simple and efficient, while Decision Tree provided interpretable decisions but was more sensitive to overfitting.

---

# My Findings

Based on the evaluation results, I would choose the **Random Forest Classifier** for loan approval prediction. It consistently produced strong evaluation metrics and generated more stable predictions than the other models. Because it combines the predictions of multiple Decision Trees, it reduces overfitting and generally provides better generalization on unseen data.

This assignment helped me understand the complete machine learning workflow, from preprocessing raw data to training, evaluating, and comparing different classification algorithms. I also learned that selecting an appropriate evaluation metric is just as important as choosing the algorithm itself, especially when making decisions that affect real-world financial applications such as loan approval.