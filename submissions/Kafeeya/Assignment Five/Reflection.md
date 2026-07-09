________________________________________
Loan Approval Prediction Report
1. What did you implement?
I reproduced the Lesson 5 preprocessing pipeline by preparing the loan dataset before training the models. This included cleaning the data, encoding categorical variables, splitting the dataset into training and testing sets, and scaling the features where appropriate. I then trained three classification models to predict whether a loan application would be approved:
•	Logistic Regression
•	Random Forest
•	K-Nearest Neighbors (KNN) as the additional algorithm
After training, I evaluated each model using Accuracy, Precision, Recall, and F1-Score on the test dataset.
________________________________________
2. Comparison of Models
How did predictions differ across all three models?
The three models produced similar predictions, but their performance varied.
•	Logistic Regression provided balanced predictions with moderate accuracy.
•	Random Forest correctly classified more loan applications and produced fewer incorrect predictions.
•	K-Nearest Neighbors (KNN) identified more approved loans (higher recall) but also produced more false positives, resulting in lower precision.
Which model gave more realistic results? Why?
The Random Forest model gave the most realistic results because it achieved the highest overall accuracy and F1-score while maintaining high precision and recall. It provided the best balance between correctly identifying approved loans and minimizing incorrect approvals.
________________________________________
3. Understanding Random Forest
Random Forest is an ensemble machine learning algorithm that combines many decision trees to make predictions. During training, each tree is built using a random sample of the training data and a random subset of features.
For classification problems, each decision tree predicts a class label, and the final prediction is determined by majority voting. Since many trees work together, Random Forest is generally more accurate and less likely to overfit than a single decision tree.
________________________________________
4. Other Algorithm (Third Classifier)
I chose K-Nearest Neighbors (KNN) as my third classification algorithm.
I selected KNN because it is a simple, non-parametric algorithm that classifies a new data point based on the classes of its nearest neighboring data points.
How it works
KNN calculates the distance between a new observation and all training examples. It then finds the K nearest neighbors (in this case, K = 5) and predicts the class that appears most frequently among those neighbors.
Advantage
•	Easy to understand and implement.
•	Works well when similar observations belong to the same class.
Limitation
•	Performance decreases with large datasets because it must calculate distances to many observations.
•	Sensitive to feature scaling and irrelevant features.
Comparison with the other models
KNN achieved:
•	Accuracy: 0.714
•	Precision: 0.750
•	Recall: 0.857
•	F1-Score: 0.800
Compared to Logistic Regression, KNN achieved higher recall and F1-score but lower precision. Compared to Random Forest, KNN had lower overall accuracy, precision, and F1-score.
________________________________________
5. Metrics Discussion
Model	Accuracy	Precision	Recall	F1-Score
Logistic Regression	0.714	0.786	0.786	0.786
Random Forest	0.762	0.846	0.786	0.815
K-Nearest Neighbors	0.714	0.750	0.857	0.800
Best metrics
•	Best Accuracy: Random Forest (0.762)
•	Best Precision: Random Forest (0.846)
•	Best Recall: K-Nearest Neighbors (0.857)
•	Best F1-Score: Random Forest (0.815)
What does this tell us?
•	Random Forest achieved the best overall performance because it balanced precision and recall, giving it the highest F1-score.
•	Logistic Regression provided stable and balanced performance but was less accurate than Random Forest.
•	KNN had the highest recall, meaning it identified more approved loans, but its lower precision indicates it also made more incorrect approval predictions.
________________________________________
6. Your Findings
Based on the evaluation results, I would choose Random Forest for loan approval prediction. It achieved the highest accuracy (76.2%), highest precision (84.6%), and highest F1-score (81.5%), making it the strongest overall model. These results indicate that Random Forest is effective at correctly classifying loan applications while minimizing false approvals.
Although KNN had the highest recall, its lower precision means it approved more applicants who should not have been approved. Logistic Regression performed consistently but did not match the overall predictive performance of Random Forest. Therefore, Random Forest provides the best balance of performance metrics and is the most suitable model for this loan approval classification task.

