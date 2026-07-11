# Loan Approval Prediction Using Classification Models

## What Did I Implement?

In this project, I reproduced the Lesson 5 machine learning pipeline for loan approval prediction. The process began with data preprocessing, including cleaning currency-formatted values, correcting inconsistent categorical values, handling missing data, removing duplicates, capping outliers using the IQR method, encoding categorical variables, checking class balance, creating new features, and scaling numerical features. The final cleaned dataset was saved as `clean_loan_dataset.csv`.

After preprocessing, I trained three classification models to predict whether a loan application would be approved or rejected. The first two models, Logistic Regression and Random Forest, were reproduced from the Lesson 5 coding session. I then researched and implemented a third classifier, Decision Tree, to compare its performance with the other models. The dataset was split into training and testing sets using an 80/20 split with stratification to preserve class balance.

---

## Comparison of Models

To compare the models, I evaluated Accuracy, Precision, Recall, and F1-Score on the test dataset. I also performed a sanity check by selecting a sample from the test set and comparing the predictions from all three models.

In the sanity check, the models often produced the same prediction, but in some cases the Decision Tree differed from Logistic Regression and Random Forest. Random Forest generally produced the most consistent predictions because it combines the decisions of many trees rather than relying on a single model. This reduces the risk of overfitting and usually results in more reliable classifications.

Among the three models, Random Forest appeared to provide the most realistic results because it achieved strong performance across multiple evaluation metrics and handled complex relationships in the data more effectively.

---

## Understanding Random Forest

Random Forest is an ensemble learning algorithm that combines multiple Decision Trees to make predictions. Instead of training one tree, the algorithm creates many trees using random subsets of the training data and random subsets of features.

For classification tasks, each tree predicts a class label. The final prediction is determined through majority voting, meaning the class predicted by the largest number of trees becomes the model’s output. This approach reduces overfitting, improves generalization, and often achieves higher accuracy than a single Decision Tree.

For loan approval prediction, Random Forest can learn complex patterns from features such as income, credit score, employment history, and collateral information while maintaining strong predictive performance.

---

## Other Algorithm: Decision Tree

For my third classifier, I selected the Decision Tree algorithm. A Decision Tree works by repeatedly splitting the dataset into smaller groups based on feature values. These splits form a tree-like structure that eventually leads to a prediction at the leaf nodes.

One advantage of Decision Trees is that they are easy to understand and interpret. The decision-making process can be visualized and explained clearly. A limitation is that Decision Trees can overfit the training data, which may reduce their performance on unseen data.

From my research and experimentation, I learned that Decision Trees are effective for capturing non-linear relationships between features and the target variable. However, they are generally less stable than Random Forest because a single tree can be heavily influenced by small changes in the data.

When comparing metrics, the Decision Tree performed reasonably well but generally achieved lower and less consistent scores than Random Forest. Logistic Regression remained competitive, especially when the relationship between features and the target was relatively simple.

---

## Metrics Discussion

The model with the highest Accuracy, Precision, Recall, and F1-Score was Random Forest. This suggests that it was the most effective model at correctly identifying approved loans while minimizing classification errors.

Logistic Regression performed well and provided a strong baseline model. Its main strength is simplicity and interpretability, but it may struggle when relationships in the data are complex and non-linear.

Decision Tree performed adequately and was easy to explain, but it was more susceptible to overfitting than Random Forest. As a result, its performance was generally less stable across different test samples.

The comparison of metrics shows that no single metric should be used alone. Accuracy measures overall correctness, Precision measures how reliable positive predictions are, Recall measures how many actual positive cases are identified, and F1-Score balances Precision and Recall. Evaluating all four metrics provides a more complete understanding of model performance.

---

## My Findings

Based on the results of this project, I would choose Random Forest for loan approval prediction. It consistently produced strong performance across Accuracy, Precision, Recall, and F1-Score while handling complex relationships in the data more effectively than the other models.

Random Forest is particularly suitable for financial datasets because it reduces overfitting through the use of multiple Decision Trees and majority voting. While Logistic Regression is easier to interpret and Decision Trees are simple to visualize, Random Forest offers the best balance between predictive accuracy and reliability. For these reasons, it would be my preferred model for a real-world loan approval system.
