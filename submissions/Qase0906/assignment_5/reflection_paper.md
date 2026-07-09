# Part C — Reflection Paper


## 1. What did I implemente?

For this project, I replicated the preprocessing pipeline from Lesson 5 to get a loan dataset ready for machine learning. I preprocessed the data by filling missing values, correcting invalid formats (such as currency symbols), encoding categorical variables, and removing duplicates. I also handled outliers using IQR method and created new features like Loan to Income ratio. I split the dataset into training and testing set after pre-processing. Then I trained three classification models i.e. Logistic Regression, Random Forest and Decision Tree for predicting loan approval. Finally, I evaluated the models using accuracy, precision, recall, F1-score and confusion matrix.

## 2. Comparison of Models

The results of the performance of the models were different. The best performance was obtained using Logistic Regression with accuracy of 0.700 followed by Random Forest and Decision Tree with accuracy of 0.650. In the sanity check, Logistic Regression correctly predicted the actual label for most of the cases. The Random Forest did quite well, but had a few more wrong guesses. In the sanity check, the Decision Tree model had one prediction error, indicating that it is less stable than the other models. In summary, Logistic Regression provided the most consistent and reasonable predictions for this dataset.

## 3. Understanding Random Forest

Random Forest is an ensemble learning technique that builds many decision trees and then combines their predictions to increase the overall accuracy and robustness of the model. Each tree is trained on a random subset of data and each tree gives a prediction. The final output is obtained by majority voting over all trees. This approach reduces overfitting and improves general performance over a decision tree. It is popularly used because of its stability , accuracy and compatibility with numerical and categorical data.



## 4. Other Algorithms (Your Third Classifier)

For the final classifier, I employed a decision tree. A decision tree divides a data set into branches, each of which makes a choice depending on a feature's value. It's easy, simple, simple, and easy, simple, and it's, simple, and it's, and it's, and it's. Its ability to model non-linear relationships in the data is one benefit. However, it is that a downside is that a drawback is that a drawback is that a drawback is that a drawback. With an accuracy of 0.650, Decision Tree performed similarly to Random Forest in this project, albeit its forecasts were less reliable.


## 5. Metrics Discussion

Logistic Regression performed best overall with Accuracy = 0.700, Precision = 0.733, Recall = 0.846, and F1-score = 0.786. Random Forest and Decision Tree both achieved Accuracy = 0.650, with slightly lower performance across all metrics. This shows that Logistic Regression was more effective for this dataset, especially in identifying positive loan approvals, as shown by its higher recall. Random Forest and Decision Tree were less accurate but still provided balanced performance.


## 6. Your Findings

Based on the results, I would recommend Logistic Regression as the final model for this dataset. In this dataset, Logistic Regression outperformed Random Forest and produced more accurate predictions in the sanity check, despite the fact that Random Forest is often stronger in many situations. Additionally, it had the highest recall, which is crucial for loan acceptance since it lowers the possibility of overlooking qualified candidates.

Random Forest is still a strong model as it is stable and reduces overfitting but in this case it performed worse than Logistic Regression. Decision Tree is good for interpretation, but it had the least stability and comparable performance to Random Forest. Hence, Logistic Regression is the most suitable model for this data set.

