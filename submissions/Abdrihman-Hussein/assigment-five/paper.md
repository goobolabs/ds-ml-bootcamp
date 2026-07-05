# Classification in Machine Learning

## Introduction to Classification

Classification is a supervised machine learning task in which a model learns from labeled examples and predicts a discrete category for new observations. In other words, the output is a class label such as “approved” or “rejected,” “disease” or “no disease,” or “spam” and “not spam.” Regression, by contrast, predicts a continuous numerical value such as house price, temperature, or salary. A simple real-life example of classification is spam email detection; a real-life example of regression is predicting the selling price of a house.

## Classification Algorithms

### Logistic Regression

Logistic regression is a linear classification method that estimates the probability of a class and then applies a threshold, often 0.5, to decide the final label. Although its name includes the word “regression,” it is widely used for classification because the target is categorical. In practice, it is common in credit scoring, medical risk prediction, and customer churn modeling. Its main advantages are simplicity, speed, and interpretability. Its main limitation is that it works best when the relationship between inputs and the log-odds of the outcome is close to linear; it can struggle when the decision boundary is highly nonlinear.

### Decision Trees

A decision tree classifies data by repeatedly splitting the dataset into smaller groups using feature-based rules such as “if income > threshold” or “if age <= threshold.” The model learns these rules from the data, and the final prediction is made at a leaf node. Decision trees are useful in areas like loan screening, medical triage, and marketing segmentation. Their advantages are that they are easy to understand, can handle both numerical and categorical patterns, and can model nonlinear decision rules. Their main limitation is instability: a small change in the data can produce a different tree, and deep trees can overfit, which is why depth controls such as `max_depth` matter.

### Random Forest

Random forest is an ensemble method that builds many decision trees on different subsamples of the data and combines their predictions, usually by voting. Because it averages many trees, it typically improves predictive accuracy and reduces overfitting compared with a single tree. It is often used in credit risk, fraud detection, and medical classification. Its strengths are strong performance and robustness. Its weaknesses are that it is less interpretable than a single decision tree and usually more computationally demanding.

## Classification Metrics

Accuracy measures the proportion of all predictions that are correct. It is easy to understand, but it can be misleading when one class dominates the dataset. Precision measures how many predicted positives are truly positive, so it focuses on false positives. Recall measures how many actual positives are correctly found, so it focuses on false negatives. F1-score is the harmonic mean of precision and recall, so it is useful when both false positives and false negatives matter. A confusion matrix is the full table of true positives, true negatives, false positives, and false negatives, and it gives the most complete picture of classification errors.

| Metric           | What it measures                          | Best use                        | Sensitivity to class imbalance                                     |
| ---------------- | ----------------------------------------- | ------------------------------- | ------------------------------------------------------------------ |
| Accuracy         | Overall proportion of correct predictions | Balanced datasets               | High sensitivity; can be misleading                                |
| Precision        | Correctness of positive predictions       | When false positives are costly | More informative than accuracy for rare positive classes           |
| Recall           | Coverage of actual positive cases         | When false negatives are costly | More informative than accuracy for rare positive classes           |
| F1-Score         | Balance between precision and recall      | When both error types matter    | Better than accuracy, but still a single summary score             |
| Confusion Matrix | Full breakdown of prediction outcomes     | Diagnostic analysis             | Very useful because it shows the class-wise error pattern directly |

## Class Imbalance

Accuracy can be misleading when classes are imbalanced because a model can obtain a high score by predicting the majority class most of the time. For example, if only a small fraction of loan applicants will default, a model that predicts “no default” for everyone may still look accurate, even though it fails to identify risky borrowers. That is why precision-recall analysis is often preferred in imbalanced settings.

In loan approval, precision is more important when the cost of approving a bad borrower is high, because you want fewer false approvals. Recall is more important when missing a truly good borrower is costly, because you want to catch as many qualified applicants as possible. In a strict lending policy, you may prioritize precision to reduce risky approvals. In a growth-oriented lending strategy, you may prioritize recall to avoid rejecting too many good customers. The correct choice depends on business cost, risk tolerance, and regulatory requirements.

## Real-World Case Study

A strong real-world example is the 2019 study *A study on predicting loan default based on the random forest algorithm*. The goal was to predict loan default in a peer-to-peer lending setting using real-world Lending Club loan data. The authors applied Random Forest after data cleaning and dimensionality reduction, and they used SMOTE to handle class imbalance in the dataset. They compared Random Forest with logistic regression and decision tree models. Their main finding was that Random Forest performed better than logistic regression and decision tree methods for predicting default samples. The study shows why ensemble methods are valuable in finance, especially when the dataset is imbalanced and the goal is to detect risky borrowers accurately.

## Conclusion

Classification is one of the most important tasks in machine learning because it supports decisions in finance, healthcare, education, and business. Logistic regression is simple and interpretable, decision trees are rule-based and intuitive, and random forests are usually stronger and more stable because they combine many trees. For evaluation, accuracy is useful only when classes are fairly balanced, while precision, recall, F1-score, and the confusion matrix give a more realistic view of performance, especially in imbalanced problems such as loan default prediction.

## References

Fitzpatrick, T., & Mues, C. (2016). *An empirical comparison of classification algorithms for mortgage default prediction: evidence from a distressed mortgage market.* European Journal of Operational Research.

Zhu, L., Qiu, D., Ergu, D., Ying, C., & Liu, K. (2019). *A study on predicting loan default based on the random forest algorithm.* Procedia Computer Science.

scikit-learn documentation: LogisticRegression, DecisionTreeClassifier, RandomForestClassifier, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, balanced_accuracy_score, and precision-recall guidance.
