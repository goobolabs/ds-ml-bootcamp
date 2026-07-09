# Assignment 5 – Reflection Paper

## Reflection on Loan Approval Prediction Project

This project provided practical experience in applying machine learning techniques to a real-world business problem. The objective was to develop predictive models capable of determining whether a loan application should be approved based on applicant information.

Throughout the project, I learned the complete machine learning workflow, including data preparation, feature engineering, model training, evaluation, and interpretation of results. One of the most important lessons was understanding that data quality has a significant impact on model performance. During the project, missing values were identified and handled before model training could begin.

Three classification algorithms were implemented and evaluated:

- Logistic Regression
- Random Forest
- Decision Tree

The models were assessed using Accuracy, Precision, Recall, F1-Score, and Confusion Matrix metrics. This process helped me understand that model evaluation should not rely solely on accuracy. Other metrics such as Recall and F1-Score often provide a more complete understanding of model performance.

The Decision Tree model achieved the best overall performance with an F1-Score of 0.80 and Recall of 0.923. This indicated that the model was highly effective at identifying approved loan applications. Logistic Regression also performed well and produced the same overall accuracy, while Random Forest showed slightly lower performance on this dataset.

One challenge encountered during the project involved missing values within the dataset. This caused model training errors because some machine learning algorithms cannot process null values directly. The issue was resolved through data preprocessing techniques that replaced missing values before training.

This project strengthened my understanding of supervised learning, classification problems, feature engineering, model evaluation, and predictive analytics. It also demonstrated how machine learning can support decision-making processes in industries such as banking and finance.

Overall, the project was valuable because it connected theoretical machine learning concepts with practical implementation. The experience improved my ability to build, evaluate, and interpret predictive models while following a structured data science workflow.


Best Model: Decision Tree

Accuracy: 70%
Precision: 70.6%
Recall: 92.3%
F1 Score: 80%