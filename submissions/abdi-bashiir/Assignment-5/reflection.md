## What did you implement?

In this assignment, I implemented a complete loan approval prediction pipeline using the cleaned loan dataset. First, I reproduced the Lesson 5 preprocessing pipeline by loading the cleaned dataset, separating the features (`X`) and target (`Approved`), and splitting the data into training and testing sets using a stratified train-test split. I then trained three classification models: **Logistic Regression**, **Random Forest**, and **Decision Tree**. Finally, I evaluated each model using Accuracy, Precision, Recall, F1-Score, and the Confusion Matrix.

---

## Comparison of Models

During the single application sanity check, all three models predicted the same result for the selected loan application. However, their overall evaluation metrics showed some differences.

Both **Logistic Regression** and **Random Forest** achieved identical results:

- Accuracy: **0.700**
- Precision: **0.733**
- Recall: **0.846**
- F1-Score: **0.786**

The **Decision Tree** model also achieved an Accuracy of **0.700**, but its other metrics were different:

- Precision: **0.684**
- Recall: **1.000**
- F1-Score: **0.812**

I think Logistic Regression and Random Forest produced more realistic predictions because they provided a better balance between Precision and Recall. Decision Tree identified every approved loan, but it also incorrectly approved more rejected applications.

---

## Understanding Random Forest

Random Forest is an ensemble machine learning algorithm that combines many Decision Trees to make a prediction. Each tree is trained using a different random sample of the training data and a random subset of features. For classification tasks, every tree votes for a class, and the class with the most votes becomes the final prediction. This approach usually improves accuracy and reduces overfitting compared to using a single Decision Tree.

---

## Other Algorithm (Decision Tree)

The additional algorithm I chose was the **Decision Tree Classifier** because it is simple, easy to understand, and works well for binary classification problems such as loan approval prediction.

From my research, I learned that a Decision Tree works by repeatedly splitting the dataset into smaller groups based on feature values until it reaches a prediction. One advantage of Decision Trees is that they are easy to understand and visualize. One limitation is that they can overfit the training data if the tree becomes too deep.

Compared with Logistic Regression and Random Forest, the Decision Tree achieved the same Accuracy but had higher Recall and F1-Score. However, its Precision was lower because it predicted more rejected loan applications as approved.

---

## Metrics Discussion

All three models achieved the same Accuracy (**0.700**).

Logistic Regression and Random Forest achieved the highest Precision (**0.733**), while Decision Tree achieved the highest Recall (**1.000**) and F1-Score (**0.812**).

These results show that Logistic Regression and Random Forest were more balanced models, while Decision Tree was better at finding approved loans but produced more false positive predictions.

---

## Your Findings

Based on the evaluation results, I would choose **Random Forest** for loan approval prediction. Although it achieved the same evaluation metrics as Logistic Regression on this dataset, Random Forest is generally more robust because it combines many Decision Trees and can learn more complex patterns while reducing overfitting.

This assignment helped me understand the complete machine learning workflow, including data preprocessing, model training, model evaluation, and comparing different classification algorithms to determine which model is most suitable for predicting loan approval.