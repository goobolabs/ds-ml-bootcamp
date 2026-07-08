# Assignment Five Part A: Classification — Theory

 1. Introduction to Classification

Classification is a supervised machine learning task in which a model learns to assign input data to one of a fixed set of categories, or classes, based on labeled training examples. The model is trained on data where the correct category is already known, and it learns the patterns that separate those categories so it can predict the class of new, unseen data.

Classification differs from regression in what it predicts. Classification outputs a discrete label — for example, "approved" or "rejected," "spam" or "not spam" — while regression outputs a continuous numeric value, such as a price, a temperature, or a probability treated as a quantity rather than a category. Both are supervised learning tasks, but the nature of the target variable determines which one applies: if the target is categorical, it is classification; if the target is a continuous number, it is regression.

**Example of classification:** predicting whether a bank loan application should be approved or rejected based on the applicant's income, credit score, and employment history.

**Example of regression:** predicting the sale price of a house based on its square footage, location, and number of bedrooms.

## 2. Classification Algorithms

### Logistic Regression

Logistic Regression works by fitting a linear combination of the input features and passing the result through a sigmoid function, which squashes the output into a probability between 0 and 1. A threshold (commonly 0.5) is then applied to that probability to decide the final class.

- **Use case:** predicting whether a customer will churn (cancel a subscription) based on usage patterns and account history.
- **Advantages:** simple, fast to train, easy to interpret (the coefficients show how each feature influences the outcome), and performs well when the relationship between features and the target is roughly linear.
- **Limitations:** struggles with complex, non-linear relationships between features and the target, and is sensitive to outliers and highly correlated features.

### Decision Trees

A Decision Tree works by repeatedly splitting the data into subsets based on feature values, choosing the split at each step that best separates the classes (commonly measured using Gini impurity or information gain). The result is a tree of if/then rules that can be followed from the root down to a leaf, which represents a final predicted class.

- **Use case:** medical diagnosis systems that classify a patient as high-risk or low-risk based on a sequence of measurable symptoms and test results.
- **Advantages:** easy to visualize and interpret, requires little data preprocessing, and can capture non-linear relationships and interactions between features.
- **Limitations:** prone to overfitting, especially with deep trees, and can be unstable — small changes in the training data can produce a very different tree.

### Random Forest

Random Forest is an ensemble method that builds many individual Decision Trees, each trained on a random subset of the data and a random subset of features, and then combines their predictions through a majority vote (for classification). This process, called bagging, reduces the overfitting problem that a single Decision Tree suffers from.

- **Use case:** credit risk scoring, where many overlapping but slightly different signals (income, debt, payment history, collateral) need to be combined into one robust decision.
- **Advantages:** generally more accurate and more stable than a single Decision Tree, resistant to overfitting, and can rank feature importance.
- **Limitations:** less interpretable than a single Decision Tree or Logistic Regression (it behaves like a "black box"), and is more computationally expensive to train and to use for prediction.

3. Classification Metrics

- **Accuracy:** the proportion of all predictions that were correct — (True Positives + True Negatives) / Total.
- **Precision:** of all the cases the model predicted as positive, the proportion that were actually positive — True Positives / (True Positives + False Positives). Precision answers: "when the model says yes, how often is it right?"
- **Recall:** of all the cases that were actually positive, the proportion the model correctly identified — True Positives / (True Positives + False Negatives). Recall answers: "of all the real positives, how many did the model catch?"
- **F1-Score:** the harmonic mean of Precision and Recall, giving a single score that balances both — useful when neither Precision nor Recall alone tells the full story.
- **Confusion Matrix:** a table that breaks predictions into four categories — True Positives, True Negatives, False Positives, and False Negatives — giving a full picture of where the model succeeds and fails, rather than a single summary number.

| Metric | What it measures | Sensitivity to class imbalance |
|---|---|---|
| Accuracy | Overall proportion of correct predictions | High — can be misleading if one class dominates |
| Precision | Correctness of positive predictions | Moderate — affected by how many negatives get misclassified as positive |
| Recall | Coverage of actual positives | Moderate — affected by how many positives get missed |
| F1-Score | Balance between Precision and Recall | Lower than Accuracy — more informative when classes are imbalanced |
| Confusion Matrix | Full breakdown of prediction outcomes | Not a single number, so it is not distorted by imbalance — it exposes it |

 4. Class Imbalance

Accuracy can be misleading when classes are imbalanced because a model can achieve a high accuracy score simply by always predicting the majority class, without actually learning anything useful about the minority class. For example, if 90% of loan applications in a dataset are approved, a model that blindly predicts "approved" for every application would score 90% accuracy while completely failing to identify any rejected applications.

In the loan approval context, whether to prioritize Precision or Recall depends on which type of mistake is more costly:

- **Prioritize Precision** when the cost of a false positive (approving a loan that should have been rejected) is high — for example, if the bank is very concerned about defaults and wants to be confident that everyone it approves will actually repay the loan.
- **Prioritize Recall** when the cost of a false negative (rejecting a loan that should have been approved) is high — for example, if the bank wants to avoid turning away creditworthy customers and losing their business to competitors, or if there is a regulatory/fairness concern about denying qualified applicants.

In practice, most loan approval systems try to balance both, often using the F1-Score or a custom cost-weighted metric rather than optimizing for just one.

 5. Real-World Case Study

A widely discussed real-world application of classification is credit scoring at consumer lending companies, where machine learning models classify loan applicants as likely to repay or likely to default. One well-documented example is the use of classification models by fintech lenders (such as those studied in research on alternative credit scoring) to assess borrowers who lack traditional credit histories.

- **Goal:** predict the probability that a loan applicant will default, to inform approve/reject decisions and interest rate pricing.
- **Data used:** applicant financial data (income, existing debt, repayment history where available) combined with alternative data sources such as utility payment records, mobile phone usage patterns, and transaction histories, especially for applicants without a formal credit bureau score.
- **Type of classifier applied:** ensemble tree-based models (such as Random Forest and Gradient Boosting) are commonly used in this space because they handle the mixed, non-linear nature of financial and behavioral data well.
- **Key results/insights:** studies in this area generally find that incorporating alternative data alongside traditional financial features improves default prediction for "thin-file" applicants (those with little credit history), allowing lenders to extend credit responsibly to a wider population while still managing risk. This illustrates the same core tradeoff discussed in Section 4: lenders must balance Precision (avoiding risky approvals) against Recall (not excluding creditworthy applicants) when tuning these classification systems.

*(Note: this summary reflects general, well-established findings from published research on alternative credit scoring rather than a single specific paper, in line with the assignment's instruction to research a real-world classification project or study.)*