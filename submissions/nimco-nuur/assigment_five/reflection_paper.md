# Assignment Five – Reflection Paper

## Student Name

**Nimco Nuur**

---

# Reflection Paper

## 1. What Did I Implement?

In this assignment, I implemented a complete machine learning classification pipeline to predict loan approval. The project involved two major stages: data preprocessing and classification model development.

During preprocessing, I loaded the raw loan dataset and inspected it for missing values, inconsistent categorical labels, and formatting problems. I cleaned the currency symbols from the **Income** and **LoanAmount** columns, standardized categorical values, filled missing data, removed duplicate records, and handled outliers using the Interquartile Range (IQR) capping technique.

Next, I encoded the categorical variables into binary values and checked the class distribution to ensure that the dataset was suitable for classification.

To improve the predictive ability of the models, I created two additional features:

* **DebtToIncome** = LoanAmount / Income
* **IncomePerYearEmployed** = Income / (EmploymentYears + 1)

Instead of using **StandardScaler**, I selected **RobustScaler** because it is less sensitive to outliers and performs better on financial datasets where extreme values are common.

Finally, I trained and evaluated three classification algorithms:

* Logistic Regression
* Random Forest
* Decision Tree

All three models were trained using the same training dataset and evaluated using the same testing dataset.

---

# 2. Comparison of Models

The three models produced different levels of performance.

### Logistic Regression

Logistic Regression achieved the best overall performance among the three models.

* Accuracy: **75.0%**
* Precision: **75.0%**
* Recall: **92.3%**
* F1-Score: **82.8%**

The confusion matrix showed that the model correctly predicted **12 approved loans** and **3 rejected loans**. It made only **one false negative** but incorrectly approved **four rejected applications**.

The high Recall indicates that Logistic Regression successfully identified most applicants who should be approved.

---

### Random Forest

Random Forest produced lower performance than expected.

* Accuracy: **55.0%**
* Precision: **62.5%**
* Recall: **76.9%**
* F1-Score: **69.0%**

The confusion matrix showed that the model correctly classified **10 approved loans** but correctly identified only **one rejected loan**.

Although Random Forest usually performs very well, its performance on this dataset was weaker than Logistic Regression. This may be due to the relatively small dataset or the characteristics of the available features.

---

### Decision Tree

Decision Tree produced moderate performance.

* Accuracy: **60.0%**
* Precision: **72.7%**
* Recall: **61.5%**
* F1-Score: **66.7%**

The model correctly classified **8 approved loans** and **4 rejected loans**.

Decision Tree performed better than Random Forest in identifying rejected applications but achieved a lower Recall than Logistic Regression.

---

# 3. Understanding Random Forest

Random Forest is an ensemble machine learning algorithm that combines many Decision Trees to improve prediction accuracy.

Each Decision Tree is trained using a different random sample of the training dataset. During prediction, every tree votes for a class, and the final prediction is determined by majority voting.

The main advantage of Random Forest is that it reduces overfitting and generally produces more stable predictions than a single Decision Tree. It also handles noisy data effectively and usually performs well on complex datasets.

However, in this assignment, Random Forest did not outperform the other models. This demonstrates that no single algorithm is always the best. Model performance depends on the quality of the dataset, preprocessing techniques, feature engineering, and dataset size.

---

# 4. My Third Classification Algorithm

The third classification algorithm I selected was **Decision Tree**.

I chose Decision Tree because it is easy to understand and interpret. The model makes predictions by following a sequence of decision rules based on the values of the input features.

One important advantage of Decision Tree is that every prediction can be explained visually through branches and nodes, making it suitable for business decision-making.

Its main disadvantage is that it can overfit the training data, especially when the tree becomes too deep.

In this assignment, Decision Tree achieved:

* Accuracy: **60.0%**
* Precision: **72.7%**
* Recall: **61.5%**
* F1-Score: **66.7%**

Although its performance was lower than Logistic Regression, it still produced reasonable predictions and demonstrated how tree-based models classify loan applications.

---

# 5. Metrics Discussion

The evaluation metrics revealed clear differences among the three classification models.

| Model               |  Accuracy | Precision |    Recall |  F1-Score |
| ------------------- | --------: | --------: | --------: | --------: |
| Logistic Regression | **75.0%** | **75.0%** | **92.3%** | **82.8%** |
| Random Forest       |     55.0% |     62.5% |     76.9% |     69.0% |
| Decision Tree       |     60.0% |     72.7% |     61.5% |     66.7% |

From these results:

* **Logistic Regression achieved the highest Accuracy.**
* **Logistic Regression achieved the highest Recall.**
* **Logistic Regression achieved the highest F1-Score.**
* **Logistic Regression also achieved the highest Precision.**

These results indicate that Logistic Regression provided the most balanced performance on this loan approval dataset.

The relatively lower performance of Random Forest suggests that the dataset may be too small or not complex enough for an ensemble model to demonstrate its full potential.

---

# 6. My Findings

Based on the evaluation results, I would choose **Logistic Regression** for this loan approval prediction task.

Although Random Forest is generally considered one of the strongest classification algorithms, it did not achieve the best performance on this particular dataset. Logistic Regression produced the highest Accuracy (75%), the highest Recall (92.3%), and the highest F1-Score (82.8%), making it the most reliable model for predicting loan approval in this project.

The single application sanity check also showed consistent predictions. The actual loan application was **Approved**, and both Logistic Regression and Random Forest correctly predicted **Approved**, indicating that the models were able to classify that sample correctly.

This assignment helped me understand the complete machine learning workflow, including preprocessing, feature engineering, feature scaling, model training, evaluation, and model comparison. I also learned that choosing the best algorithm depends on the characteristics of the dataset rather than assuming that one algorithm will always outperform the others.

---

# Conclusion

This assignment provided practical experience in building and evaluating machine learning classification models for loan approval prediction.

By applying data preprocessing, feature engineering, RobustScaler, and three classification algorithms, I gained a deeper understanding of how different models perform on the same dataset.

Among the three algorithms, **Logistic Regression produced the best overall performance**, achieving the highest Accuracy, Precision, Recall, and F1-Score. These results demonstrate that a simpler model can sometimes outperform more complex algorithms depending on the dataset and preprocessing techniques used.
