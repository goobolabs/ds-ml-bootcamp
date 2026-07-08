## Introduction to Classification

Classification is supervised learning used to predict categorical labels or predicts which class set of classes.

Classification predicts which class example yes/no spam/not spam depends on your use case while regression predicts continuous numbers or how many.

Example: predicting temperature or age is regression while predicting yes/no or passed/failed or movie category like drama,romance,mystery all are classification

## Classification Algorithms

- ### Logistic Regression

  Is a supervised classification algorithm that uses an S-shaped curve. Its prediction is based on probability instead of hard-coded rules.
  - #### Main advantages

    It is simple and fast, best for binary classification (0/1 or Yes/No). It is also interpretable, so you can see which factors pushed the prediction toward Yes or No.

  - #### Limitations

    Struggles with complex non-linear relationships. Since it is probability-based, its decision depends on the calculated probability from the input features.

  - #### Real world use cases
    Email spam detection,Loan approval

- ### Decision Tree

  Is a supervised classification algorithm that splits data into branches based on feature values until a prediction is made.
  - #### Main advantages

    Handles non-linear relationships well. It is easy to visualize and explain what is happening during the prediction process.

    Handles both text and numerical data

  - #### Limitations

    Can easily overfit, especially when the dataset is small or contains low-quality data and small changes in data can completely change the tree.

  - #### Real world use cases

    Loan approval

- ### Random Forest

  Is a supervised classification algorithm that uses many decision trees and combines their predictions to produce a stronger final result.
  - #### Main advantages

    Handles non-linear relationships, uses multiple decision trees to make a stronger prediction based on multiple sources, achieves high accuracy, and reduces overfitting compared to a single decision tree.

  - #### Limitations

    Less interpretable than a single decision tree and generally requires more data and high computational power.

  - #### Real world use cases

    Loan approval, Fraud detection

## Classification Metrics

### Accuracy

Accuracy tells you overall model correct prediction and its useful when dataset is balanced.

Example test cases of 100 model predicts 85 positive predictions accuracy is 85%

Accuracy can't tell you weather the model is always predicts yes or no and high accuracy is not grantee model is best.

### Precision

Precision tells you overall when model predicts positive how many actually positive example model takes 20 test cases identifies 17 as positive. precision comes here and answers out 17 how many actually positive let's say 15/17 so it's 90%.

Useful when false positive is costly example when predicting medical cases false positive is costly.

### Recall

Recall tells you overall how many real positive predictions model finds/catches.

Example model take 30 test cases 10 is negative and model predicts 15 as positive out of 30 how many real positive model catches let's say 14 so it's 48%.

Useful when false negative is costly example again when predicting medical cases false negative is more costly than false positive.

### F1-Score

F1-Score is the harmonic mean of precision and recall. It is useful when you want to balance precision and recall, especially in cases where you have an imbalanced dataset.

### Confusion Matrix

A table layout that visualizes the performance of a classification algorithm and it tell you the exact counts of True Positives, True Negatives, False Positives, and False Negatives.

| METRIC           | MEASURE                                         | SENSITIVITY TO IN BALANCE |
| ---------------- | ----------------------------------------------- | ------------------------- |
| Accuracy         | overall model correct                           | Yes can be mislead        |
| Precision        | predicted positive how many is right            | No its useful             |
| Recall           | all positive cases how many model finds/catches | No its useful             |
| F1-Score         | balance between precision and recall            | No its useful             |
| Confusion Matrix | exact counts of TP, TN, FP, FN                  | No its useful             |

## Class Imbalance

`Why can Accuracy be misleading when classes are imbalanced` because accuracy tells you overall model correct prediction weather it's positive/negative. what if there no negative predictions or there is only one negative prediction the model always says it's positive thats why

Precision over Recall I will go Precision when false positive is costly example loan approval let's say loan request was 10k and his income 1k and credit score is high because previous loans are small like $200 what if the modal approve it's unworthy.

Recall over Precision I will go Recall when false negative is costly example rejecting acceptable loan request.

## Real-World Case Study

- **Goal:** Detect phishing websites that use homoglyph (lookalike Unicode) attacks by combining a hash function with machine learning.
- **Data Used:** URLs and domain names containing legitimate and homoglyph-based phishing websites.
- **Classifier Applied:** Random Forest classifier with hashed URL features.
- **Key Results / Insights:** The hash function improved detection by recognizing even small URL changes, and the Random Forest model achieved **99.8% accuracy**, outperforming existing phishing detection methods while improving security, integrity, and availability.

## Reference

[Homograph attack detection](https://www.mdpi.com/2224-2708/11/3/54)
