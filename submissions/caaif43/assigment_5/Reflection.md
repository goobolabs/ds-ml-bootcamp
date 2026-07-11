# Part C — Reflection Paper: Loan Approval Classification Project

## 1. What I Implemented

In this assignment, I reproduced the Lesson 5 machine learning pipeline using a real-world loan approval dataset. The work included data preprocessing, feature engineering, model training, and evaluation.

First, I cleaned the dataset by handling missing values, correcting inconsistent categorical labels, removing duplicates, and capping outliers using the IQR method. I also converted categorical variables into numerical form using label encoding and created new features such as Debt-to-Income ratio and Income per Year Employed.

After preprocessing, I scaled the numerical features using MinMaxScaler to normalize the data. Then, I trained three classification models: Logistic Regression, Random Forest, and a third model (Decision Tree) that I researched independently.

Finally, I evaluated all models using Accuracy, Precision, Recall, F1-score, and Confusion Matrix, and performed a sanity check by comparing predictions for a single test sample.

---

## 2. Comparison of Models

The predictions from the three models were slightly different when tested on the same input sample. Logistic Regression gave more stable but simpler predictions, while Decision Tree showed more variation due to its sensitivity to data splits. Random Forest produced the most consistent and reliable predictions across different test cases.

Based on the evaluation metrics, Random Forest generally performed better than the other two models, especially in terms of balancing Precision and Recall.

---

## 3. Understanding Random Forest

Random Forest is an ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy. Each tree is trained on a random subset of the data, and the final prediction is made by majority voting.

This method reduces overfitting, which is common in a single decision tree, and improves generalization on unseen data. However, it is less interpretable compared to simpler models like Logistic Regression because it combines many trees.

---

## 4. Other Algorithm (Decision Tree)

For the third classifier, I chose the Decision Tree algorithm because it is simple, interpretable, and commonly used in classification problems.

A Decision Tree works by splitting the dataset into branches based on feature conditions until it reaches a final decision (leaf node). One advantage is that it is easy to understand and visualize. However, a major limitation is that it can easily overfit the training data if not properly controlled.

---

## 5. Metrics Discussion

Among the three models, Random Forest achieved the highest performance in most metrics, including Accuracy, Precision, Recall, and F1-score. Logistic Regression performed moderately well, while Decision Tree had slightly lower and more unstable results.

This shows that Random Forest is more balanced and robust, especially for complex datasets. Logistic Regression is useful for simpler linear relationships, while Decision Tree is more flexible but prone to overfitting.

---

## 6. Final 

Based on the results, I would choose Random Forest as the best model for loan approval prediction. This is because it provides high accuracy while maintaining a good balance between Precision and Recall.

In real-world loan approval systems, minimizing incorrect approvals (false positives) is very important. Random Forest performs well in reducing such errors while still correctly identifying eligible applicants.

Overall, this assignment helped me understand the full machine learning workflow, from data cleaning to model evaluation, and improved my understanding of how different algorithms perform on classification tasks.