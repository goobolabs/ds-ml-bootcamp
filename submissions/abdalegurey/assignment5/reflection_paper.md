# Part C – Reflection Paper

## Loan Approval Classification Reflection

### What Did I Implement?

In this assignment, I reproduced the preprocessing pipeline from Lesson 5 and applied it to a loan approval dataset. First, I loaded and inspected the raw dataset to identify missing values, inconsistent category labels, and formatting issues in the numeric columns. I cleaned the currency values by removing dollar signs and commas, normalized Yes/No category values, filled missing values using the median for numerical features and the mode for categorical features, removed duplicate records, and capped outliers using the Interquartile Range (IQR) method.

After cleaning the dataset, I encoded the categorical Yes/No columns into binary values (1 and 0), engineered two new features (DebtToIncome and IncomePerYearEmployed), and scaled the numerical features using **RobustScaler** because it is less sensitive to outliers than StandardScaler. Finally, I saved the cleaned dataset as **clean_loan_dataset.csv** for model training.

Using the cleaned dataset, I trained three classification models to predict loan approval:

* Logistic Regression (from the lesson)
* Random Forest (from the lesson)
* Decision Tree (my additional researched algorithm)

Each model was trained using the same training and testing split with `stratify=y` and `random_state=42`. I evaluated each model using Accuracy, Precision, Recall, F1-Score, and a Confusion Matrix.

---

## Comparison of Models

During the sanity check, I selected one sample from the test dataset and compared the predictions of all three models with the actual loan approval label. In my experiment, the models generally produced similar predictions, although the Decision Tree occasionally differed because it makes decisions based on a single tree, while Random Forest combines predictions from many trees.

Among the three models, Random Forest produced the most realistic and reliable predictions. Since it combines multiple decision trees instead of relying on only one, it reduces overfitting and usually generalizes better to unseen loan applications.

---

## Understanding Random Forest

Random Forest is an ensemble machine learning algorithm used for both classification and regression problems. Instead of building a single decision tree, it creates many decision trees using different random subsets of the training data and features.

For classification tasks, each decision tree predicts a class label independently. The final prediction is determined by majority voting, meaning the class predicted by most trees becomes the final output. This ensemble approach improves prediction accuracy, reduces overfitting, and produces more stable results than a single Decision Tree.

---

## Other Algorithm (Decision Tree)

For my third classifier, I selected the **Decision Tree Classifier**.

I chose Decision Tree because it is simple, easy to understand, and produces interpretable decision rules. It works by repeatedly splitting the dataset into smaller groups based on feature values until a prediction can be made.

From my research, I learned that Decision Trees are effective for handling both numerical and categorical data and can capture non-linear relationships between features. One major advantage is that they are easy to visualize and explain. However, one limitation is that a single Decision Tree can easily overfit the training data, especially when it grows very deep.

Compared with Logistic Regression and Random Forest, the Decision Tree achieved competitive performance but generally produced slightly lower evaluation metrics because of its higher tendency to overfit.

---

## Metrics Discussion

Among the three models, Random Forest achieved the strongest overall performance across Accuracy, Precision, Recall, and F1-Score. Logistic Regression also performed well and provided a strong baseline model, particularly because of its simplicity and efficiency.

Decision Tree performed reasonably well but was generally less stable than Random Forest. These evaluation metrics demonstrate that although all three models can classify loan applications, Random Forest offers the best balance between correctly identifying approved loans and minimizing incorrect predictions.

---

## My Findings

Based on the evaluation results, I would choose **Random Forest** for loan approval prediction. It consistently produced the strongest performance across multiple evaluation metrics while reducing the risk of overfitting through its ensemble learning approach. Because loan approval decisions affect both financial institutions and applicants, a model that generalizes well to new data is extremely important.

This assignment improved my understanding of the complete machine learning workflow for classification problems. I learned how proper data preprocessing directly affects model performance, how different classification algorithms make predictions, and why multiple evaluation metrics are necessary instead of relying only on accuracy. Overall, Random Forest proved to be the most reliable model for this loan approval prediction task.
