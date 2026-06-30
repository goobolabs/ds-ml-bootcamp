## 1 What did you implement?

First loaded dataset then specify features(x)I and target(y) then split into train and test samples.

Then i trained linear and random forest regression models to predict car price.

## 2 Comparison of Models?

Both models give me some how accurate prediction and the random forest model looks like realistic prediction.

In case both models are different in training and test performance

[First train](./img/Screenshot%20from%202026-06-29%2023-10-35.png)

<img src="./img/Screenshot from 2026-06-29 23-10-35.png" alt="First train performance" heigh="250">

[Second train after feature re selected](./img/Screenshot%20from%202026-06-29%2023-13-30.png)

<img src="./img/Screenshot from 2026-06-29 23-13-30.png" alt="Second train performance" heigh="250">

[Third Train after polynomial transform](./img/Screenshot%20from%202026-06-30%2008-26-35.png)

<img src="./img/Screenshot from 2026-06-30 08-26-35.png" alt="Third train performance" heigh="250">

These results show that there is overfitting in random forest model and under fitting in linear regression model.

### Cause

- small dataset
- noisy features
- dataset does not have enough features to determine the target value.

## 3 Random Forest?

Is Supervised machine learning algorithms and it's tree based decision.

It creates tree and each tree is trained on a set of random data from the entire dataset to improve the accuracy and efficiency of the model

## 4 Metrics Discussion?

Linear regression has better performance metrics

| R2   | MAE     | RMSE    |
| ---- | ------- | ------- |
| 0.53 | 1150.97 | 1765.38 |

The strengths and weaknesses of each model is that in random forest has strength performance in training and poor performance in testing while linear regression has mixed performance in training 0.53 and testing 0.65

## 5 Your Findings?

After these findings and separate attempts at training, testing, and checking the performance on both the training and testing datasets,

In my decision, there is not enough data and features to determine the target value.

I prefer Linear Regression because it is able to handle unseen data.
