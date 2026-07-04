## What I Implemented

I reproduced the Lesson 5 preprocessing pipeline by loading the loan dataset, cleaning missing and incorrect values, encoding the Yes/No columns into numbers, removing duplicates, handling outliers, creating new features, and scaling the numeric data. Then, I trained three classifiers: Logistic Regression, Random Forest, and Decision Tree to predict whether a loan would be approved.

## Comparison of Models

In the sanity check performed on a single test application, all three models—Logistic Regression, Random Forest, and Decision Tree—correctly predicted the “Approved” outcome. While they agreed in this instance, the confusion matrices revealed broader differences. The Decision Tree was more aggressive, resulting in higher recall but lower precision compared to the more conservative Logistic Regression and Random Forest models.

Logistic Regression and Random Forest provided more balanced results for this dataset, making them arguably more “realistic” by avoiding the overfitting tendencies often seen in unconstrained decision trees.

## Understanding Random Forest

Random Forest is a machine learning algorithm that uses many Decision Trees to make predictions. For classification, each tree predicts a class, and the class with the most votes becomes the final prediction. Using many trees makes the model more accurate and reliable than using just one Decision Tree.

## My Algorithm Choice

I chose Decision Tree because it works well for classification tasks.

## What I Learned

A Decision Tree works by splitting the data into smaller groups based on feature values until it reaches a prediction.

Advantage: Easy to understand and explain.  
Limitation: It can overfit the training data if the tree becomes too deep.

The Decision Tree had the same accuracy (70%) as Logistic Regression and Random Forest. Its confusion matrix was slightly different, correctly predicting 12 approved loans compared to 11 for the other models, but it correctly predicted only 2 rejected loans compared to 3. Overall, the three models performed similarly, while Logistic Regression and Random Forest gave slightly more balanced predictions.

## Metrics Discussion

All three models performed almost the same:

Accuracy: All models = 0.700  
Precision: Logistic Regression = 0.733, Random Forest = 0.733, Decision Tree (slightly lower balance)  
Recall: Logistic Regression = 0.846, Random Forest = 0.846, Decision Tree (similar range but slightly less balanced)  
F1-Score: Logistic Regression = 0.786, Random Forest = 0.786, Decision Tree (slightly lower overall balance)

So, Logistic Regression and Random Forest performed the best overall and equally based on the metrics.

## Model Summary

Logistic Regression: Good at general prediction and very stable. It performs well even on small datasets, but it may miss complex patterns.  

Random Forest: Strong and reliable because it combines many decision trees. It handles complex patterns better and reduces errors, but it is less interpretable.  

Decision Tree: Easy to understand and explain, but less stable and can make more uneven predictions, leading to slightly weaker balance in the confusion matrix.

## Final Finding

For loan approval prediction, I would choose Random Forest. Even though all models showed similar accuracy, Random Forest is usually more reliable because it combines many decision trees and reduces the chance of errors from a single model. This makes it stronger at handling different patterns in the data and gives more stable predictions, which is important when making financial decisions like loan approvals.