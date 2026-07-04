## What did you implement?

First was data preprocessing where i cleaned,formatted,transformed,scaled,removed duplicates,iqr capping,label encoding and saved clean full dataset also in preprocessing i used train and test split then scaled `.fit_transform` for train and `.transform` for test to avoid data leakage then saved train.csv and test.csv.

Second was model training,testing and evaluation in this case i trained four different models random forest,logistic regression,decision tree,svn classifier.

Logistic regression and Decision tree are the top two best performance

## Comparison of Models

There is some differences but all four models perform well in sanity check

Decision tree and Logistic regression almost predicts too realist.

## Understanding Random Forest

Is Supervised machine learning algorithms and it's tree based decision.

create trees each tree strong previous tree to make realist prediction it's a voting when decision is voted it seem trustable because of different opinion.

## Other Algorithms (Your Third Classifier)

I chose decision tree because its easy to interpret and visualize, its suitable for understanding the decision-making process behind loan approvals.

It can handle both numerical and categorical data, which is common in loan datasets.

Decision trees can capture non-linear relationships between features and the target variable, allowing for more accurate predictions.

Its limitations include overfitting and sensitivity to small changes in the data, which can lead to different tree structures.

Compared to random forest it's higher performance but same performance level to logistic regression.

## Metrics Discussion

Decision tree and Logistic regression has the best performance metrics of overall models.

Decision Tree,Logistic regression and svm has 70+ accuracy while random forest is equal to 60 tells well the model is in overall.

Decision Tree and Logistic regression has 75+ precision while random forest and svm <= 69 tells how you can trust the positive predictions the two highest can be trustable compared to the others.

All models has 80+ recall tells you how model catches the positive cases.

## Your Findings

I trained and tested four classification models logistic regression,random forest,decision tree,svm.

I chose Decision tree and Logistic regression because of the best performance metrics and trustable positive predictions.

Why all models has 80+ recall and different precision in random forest and svm because of a lot of false positive cases in random forest and svm which is not trustable.

## References

[Machine Learning Algorithms for Classification](https://www.geeksforgeeks.org/machine-learning/top-machine-learning-algorithms-for-classification/)
