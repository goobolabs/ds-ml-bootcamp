# Assignment Five – Reflection Paper

## What Did You Implement?

In this assignment, I reproduced the Lesson 5 preprocessing pipeline and implemented three classification models for loan approval prediction. I prepared and cleaned the loan dataset by removing currency symbols, correcting category inconsistencies, handling missing values, removing duplicate rows, handling outliers, encoding categorical variables, and creating new features.

After preprocessing, I trained three machine learning models:

- Logistic Regression
- Random Forest
- Decision Tree

Logistic Regression and Random Forest were implemented from the lesson materials, while Decision Tree was selected as an additional algorithm after research.

---

## Comparison of Models

The predictions from the three models were slightly different during the sanity check because each model uses different techniques to learn patterns from the data.

Logistic Regression predicts outcomes using probability and linear relationships.

Random Forest predicts outcomes by combining multiple decision trees and using majority voting.

Decision Tree predicts outcomes using rule-based branching structures.

Among the three models, Random Forest produced more realistic predictions because it combines several trees and reduces overfitting.

---

## Understanding Random Forest

Random Forest is an ensemble classification algorithm that combines multiple decision trees.

Instead of using one tree, Random Forest creates many decision trees using random samples from the dataset. Each tree independently predicts an outcome.

The final prediction is selected using majority voting.

Example:

- Tree 1 → Approved
- Tree 2 → Approved
- Tree 3 → Rejected

Final Prediction:

Approved

Random Forest improves prediction accuracy and reduces overfitting.

---

## Other Algorithm (Decision Tree)

The additional algorithm selected was Decision Tree.

Decision Tree was chosen because it is simple and effective for loan approval prediction. The model creates decisions based on features such as:

- Income
- Credit Score
- Loan Amount
- Employment Years

### Advantage

Easy to understand and visualize.

### Limitation

Can overfit training data.

Compared with Logistic Regression and Random Forest, Decision Tree performed reasonably well, although Random Forest generally achieved stronger performance.

---

## Metrics Discussion

Among the three models, Random Forest achieved stronger overall performance in:

- Accuracy
- Precision
- Recall
- F1-Score

Higher Accuracy means more predictions were correct.

Higher Precision indicates fewer false positive predictions.

Higher Recall shows that more actual positive cases were identified correctly.

Higher F1-Score indicates a good balance between Precision and Recall.

These results suggest that Random Forest provides stronger and more reliable predictions.

---

## Findings

Based on the results of this assignment, I would choose Random Forest for loan approval prediction.

Random Forest performs better because it reduces overfitting and captures complex relationships among variables more effectively than individual models.

Loan approval decisions depend on multiple factors such as income, credit score, loan amount, and employment history. Random Forest can learn these relationships effectively and produce reliable predictions.

Overall, this assignment improved my understanding of:

- Data preprocessing
- Classification algorithms
- Performance metrics
- Model comparison