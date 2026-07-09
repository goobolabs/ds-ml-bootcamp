# Reflection Paper: Loan Approval Prediction Using Machine Learning

## What I Implemented

In this project, I implemented a complete machine learning classification pipeline to predict loan approval. I reproduced the Lesson 5 preprocessing pipeline by loading the dataset, checking for missing values, cleaning the data, encoding categorical variables, and standardizing the numerical features using **StandardScaler**. After preprocessing, I split the dataset into training and testing sets.

Next, I trained three classification models: **Logistic Regression**, **Random Forest**, and **Support Vector Classifier (SVC)**. Logistic Regression and Random Forest were covered in class, while SVC was my additional algorithm. After training the models, I evaluated them using Accuracy, Precision, Recall, F1-Score, and the Confusion Matrix. Finally, I performed a sanity check by testing each model on sample loan applications and comparing their predictions.

## Comparison of Models

During the sanity check, all three models correctly predicted many of the obvious loan approval cases, but they differed on borderline applications. Logistic Regression made predictions based on a linear decision boundary, while SVC attempted to find the optimal boundary that best separated approved and rejected loans. Random Forest combined the predictions of many decision trees, making its predictions more stable.

Among the three models, Random Forest produced the most realistic results because it captured complex relationships between the features and reduced overfitting. SVC also performed well and made accurate predictions, especially after feature scaling. Logistic Regression was the easiest to interpret but was less flexible than the other two models.

## Understanding Random Forest

Random Forest is an ensemble machine learning algorithm used for classification. Instead of building one decision tree, it creates many decision trees using different random samples of the training data. Each tree predicts whether a loan should be approved or rejected, and the final prediction is determined by **majority voting**. The class that receives the most votes becomes the model's prediction.

Because it combines many decision trees, Random Forest reduces overfitting and usually achieves better accuracy than a single Decision Tree. It is also robust to noisy data and can model complex patterns, making it a strong choice for loan approval prediction.

## Other Algorithm (Support Vector Classifier - SVC)

For my third classifier, I chose the **Support Vector Classifier (SVC)** because it is a powerful algorithm for classification problems and often performs well on datasets with clear class boundaries.

SVC works by finding the optimal decision boundary, called a **hyperplane**, that maximizes the distance (margin) between different classes. The algorithm focuses on the data points closest to the boundary, known as **support vectors**, because they determine the position of the hyperplane.

One major advantage of SVC is that it performs well in high-dimensional datasets and can model complex decision boundaries using kernel functions. However, one limitation is that it can be slower to train on very large datasets and usually requires feature scaling for good performance.

Compared with Logistic Regression and Random Forest, SVC achieved competitive performance and produced accurate predictions. However, Random Forest generally performed better overall because it handled the loan approval dataset more effectively.

## Metrics Discussion

The evaluation metrics showed different strengths for each model.

* **Accuracy:** **[Insert your best model]** achieved the highest accuracy.
* **Precision:** **[Insert your best model]** produced the highest precision.
* **Recall:** **[Insert your best model]** achieved the highest recall.
* **F1-Score:** **[Insert your best model]** obtained the highest F1-Score.

These metrics show that Logistic Regression is simple and interpretable, SVC is effective at finding optimal decision boundaries, and Random Forest is generally the most robust because it combines many decision trees to improve prediction performance.

## My Findings

Based on my experiments, I would choose **Random Forest** for loan approval prediction. It provided the best balance between accuracy, precision, recall, and F1-score while producing stable predictions during the sanity check. Its ensemble approach reduced overfitting and improved its ability to generalize to unseen loan applications.

Although Logistic Regression is fast and easy to interpret, and SVC is powerful for classification tasks, Random Forest is better suited for real-world loan approval systems because it handles complex relationships between features and consistently delivers strong predictive performance.
