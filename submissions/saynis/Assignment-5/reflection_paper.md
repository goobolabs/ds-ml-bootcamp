# Part C — Reflection Paper

## What I Implemented

In this assignment, I reproduced the Lesson 5 classification pipeline using the loan approval dataset. First, I cleaned and prepared the raw dataset in `loan_data_processing.ipynb`. I removed currency symbols from numeric columns, fixed inconsistent Yes/No values, filled missing values, removed duplicate rows, capped outliers using the IQR method, encoded categorical Yes/No columns as 1 and 0, checked class balance, created new features, and applied feature scaling.

For feature engineering, I added `DebtToIncome` and `IncomePerYearEmployed`. These features were created only from input features, not from the target column, so they did not leak the answer into the model. For scaling, I used `RobustScaler` instead of `StandardScaler` because loan datasets can contain outliers in financial columns such as Income and LoanAmount.

In the second notebook, `loan_approval_prediction.ipynb`, I loaded the cleaned dataset, prepared `X` as the feature columns and `y` as the `Approved` target column, split the data into training and testing sets using an 80/20 split, and trained three classification models: Logistic Regression, Random Forest, and Decision Tree.

## Comparison of Models

The three models gave slightly different results. Logistic Regression and Decision Tree both achieved the same Accuracy of 0.700, while Random Forest achieved 0.650. Logistic Regression had the highest Precision at 0.733, meaning its approval predictions were slightly more reliable. Decision Tree had the highest Recall at 0.923, meaning it found most of the actually approved applications.

The model results were:

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 0.700 | 0.733 | 0.846 | 0.786 |
| Random Forest | 0.650 | 0.714 | 0.769 | 0.741 |
| Decision Tree | 0.700 | 0.706 | 0.923 | 0.800 |

In the sanity check, I compared one row from the test set with the predictions from all three models. This helped me see how the models make individual predictions, not only overall metric scores. Even when models have similar Accuracy, they can still make different decisions on the same applicant.

## Understanding Random Forest

Random Forest is an ensemble classification algorithm. In simple words, it combines many Decision Trees instead of relying on one tree. Each tree makes its own prediction, and the final class is chosen by majority vote. For example, if most trees vote `Approved`, the Random Forest predicts `Approved`.

This approach makes Random Forest more stable than a single Decision Tree. A single tree can overfit by learning very specific patterns from the training data, but Random Forest reduces this problem by averaging the decisions of many trees. The main limitation is that Random Forest is harder to explain than a single Decision Tree because many trees are involved in the final prediction.

## My Third Classifier: Decision Tree

For the third classifier, I chose Decision Tree. I selected it because it is easy to understand and fits the loan approval problem naturally. Loan approval often depends on rule-based conditions such as credit score, income, previous defaults, collateral, and debt-to-income ratio. A Decision Tree works in a similar way by asking a sequence of questions and following branches until it reaches a final decision.

One advantage of Decision Tree is interpretability. It is easier to explain why a decision was made compared to more complex models. One limitation is overfitting. If the tree becomes too deep, it may memorize the training data and perform less well on new data.

In this experiment, Decision Tree performed well. It had the highest Recall and F1-Score among the three models. However, its Precision was lower than Logistic Regression, which means it approved more applicants but also made more wrong approval predictions.

## Metrics Discussion

The best Accuracy was shared by Logistic Regression and Decision Tree, both scoring 0.700. The best Precision was achieved by Logistic Regression with 0.733. This means Logistic Regression was slightly better at making reliable approval predictions. The best Recall was achieved by Decision Tree with 0.923. This means Decision Tree was the best at finding applicants who were actually approved. The best F1-Score was also achieved by Decision Tree with 0.800, showing the best balance between Precision and Recall in this experiment.

The confusion matrices supported these results. Decision Tree correctly approved 12 out of 13 actually approved applicants, but it also produced 5 false positives. Logistic Regression had fewer false positives than Decision Tree, so it was more careful when predicting approvals. Random Forest had the lowest overall performance on this small test set, but this does not mean Random Forest is a weak algorithm. The dataset was small, so a few wrong predictions can strongly affect the final scores.

## My Findings

Based on this experiment, I would choose Decision Tree if the goal is to find as many approvable applicants as possible. It achieved the highest Recall and F1-Score, meaning it was strong at identifying applicants who should be approved. This can be useful if the bank wants to avoid rejecting good applicants.

However, if the bank wants to reduce risky approvals, Logistic Regression may be the safer choice because it had the highest Precision. In a real loan approval system, the final model choice should depend on business priorities. For this assignment, I prefer Decision Tree because it gave the best overall balance in my results and was also easy to explain.
