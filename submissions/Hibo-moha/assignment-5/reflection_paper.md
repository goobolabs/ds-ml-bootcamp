# Reflection Paper

## Assignment Five: Loan Approval Classification

# Introduction

This assignment provided me with practical experience in applying machine learning techniques to a real-world loan approval prediction problem. I learned how to clean and preprocess raw data, engineer meaningful features, train multiple classification models, and evaluate their performance using different evaluation metrics. The assignment also helped me understand the importance of selecting the right algorithm for a specific prediction task and interpreting the results correctly.

---

# 1. What Did I Implement?

In this assignment, I reproduced the complete preprocessing pipeline presented during Lesson 5. The first stage focused on preparing the loan approval dataset before training the machine learning models.

The preprocessing steps included loading and inspecting the dataset, cleaning currency values by removing dollar signs and commas, correcting inconsistent categorical values, handling missing data using median and mode imputation, removing duplicate records, capping outliers with the Interquartile Range (IQR) method, encoding categorical variables into numerical values, checking class balance, creating new features, and scaling numerical variables using **RobustScaler**.

After preprocessing, I trained three different classification models:

* Logistic Regression
* Random Forest Classifier
* Decision Tree Classifier

These models were trained using the same training dataset so that their performance could be compared fairly.

---

# 2. Comparison of Models

After training the three models, I evaluated them using Accuracy, Precision, Recall, F1-Score, and the Confusion Matrix.

The sanity check showed that all three models produced similar predictions for many test samples. However, there were cases where the Decision Tree produced a different prediction because it makes decisions based on a single tree structure. Logistic Regression produced stable predictions but was limited when relationships between variables became more complex.

Among the three models, Random Forest produced the most reliable and consistent predictions. Since it combines multiple Decision Trees, it reduces overfitting and generally performs better on unseen data.

---

# 3. Understanding Random Forest

Random Forest is an ensemble machine learning algorithm that combines many Decision Trees to improve prediction accuracy.

Instead of relying on one tree, Random Forest creates multiple trees using different subsets of the training data. Each tree independently predicts whether a loan should be approved or rejected. The final prediction is determined through majority voting.

This approach makes Random Forest more robust than a single Decision Tree because errors made by individual trees are often corrected by the majority of the forest. As a result, the model achieves higher accuracy and better generalization.

---

# 4. My Additional Classifier

For the third classification algorithm, I selected the **Decision Tree Classifier**.

I chose this algorithm because it is simple to understand and provides interpretable decision rules. It visually explains how different variables influence the final prediction, making it useful for educational purposes and business decision-making.

Through my research, I learned that Decision Trees recursively split the data into smaller subsets based on feature values. Each split aims to maximize the separation between classes.

### Advantage

* Easy to understand and explain.
* Can handle both numerical and categorical features.
* Requires minimal data preparation.

### Limitation

* Easily overfits the training data if not properly controlled.
* Sensitive to small changes in the dataset.

Compared with Logistic Regression and Random Forest, the Decision Tree generally achieved reasonable performance but slightly lower accuracy because it relied on a single tree rather than an ensemble of trees.

---

# 5. Discussion of Evaluation Metrics

The evaluation metrics provided different perspectives on model performance.

* **Accuracy** measured the percentage of correct predictions.
* **Precision** measured how many approved loan predictions were actually correct.
* **Recall** measured how many truly approved loans were successfully identified.
* **F1-Score** balanced Precision and Recall into a single performance measure.

Among the three models, Random Forest achieved the strongest overall performance because it maintained consistently high values across all evaluation metrics. Logistic Regression also performed well but struggled with more complex relationships in the data. Decision Tree produced acceptable results but was more likely to overfit.

These results demonstrate that evaluating multiple metrics is important because relying only on Accuracy can sometimes give a misleading impression of model performance.

---

# 6. My Findings

This assignment demonstrated that data preprocessing is one of the most important stages of any machine learning project. High-quality preprocessing improves model performance and ensures reliable predictions. Cleaning inconsistent values, handling missing data, removing duplicates, engineering new features, and scaling numerical variables all contributed to building stronger classification models.

Based on my evaluation, I would choose **Random Forest** for loan approval prediction. It achieved the best balance between Accuracy, Precision, Recall, and F1-Score while reducing the risk of overfitting. Although Logistic Regression is easier to interpret and Decision Trees are easier to visualize, Random Forest provides more stable and dependable predictions, making it a better choice for financial decision-making.

Overall, this assignment strengthened my understanding of classification algorithms, model evaluation, feature engineering, and data preprocessing. It also improved my confidence in implementing complete machine learning workflows using Python and Scikit-learn.

---

# Conclusion

Completing this assignment gave me valuable hands-on experience in building a complete machine learning classification system. From preprocessing raw data to evaluating multiple predictive models, I learned how each stage contributes to the success of a machine learning project. I also discovered that selecting an appropriate algorithm and evaluating it using several performance metrics are essential for making reliable predictions. The knowledge gained from this assignment will be valuable for future projects involving predictive analytics and intelligent decision-making systems.

---

# References

* Géron, A. (2023). *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* (3rd Edition). O'Reilly Media.
* James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning* (2nd Edition). Springer.
* Scikit-learn Developers. *Scikit-learn User Guide*. https://scikit-learn.org/stable/
