# Reflection Paper: Loan Approval Prediction

## 1. Implementation Overview
In this project, I implemented a machine learning pipeline to predict loan approvals. The process followed these key steps:
* **Preprocessing:** Loaded `clean_loan_dataset.csv` and separated features (`X`) from the target (`Approved`).
* **Data Splitting:** Partitioned the data into 80% training and 20% testing sets, utilizing `stratify=y` to ensure consistent class representation, with `random_state=42` for reproducibility.
* **Model Training:** I trained the required **Logistic Regression** and **Random Forest** models, alongside an additional research-based model: **Gradient Boosting**.

## 2. Comparison of Models
During my sanity check (comparing a single test row's actual label to model predictions), I observed that models varied in their output.
* **Findings:** While some models predicted the outcome accurately, others did not. The Gradient Boosting model provided the most realistic and accurate results across the test set, demonstrating superior performance in identifying the positive ("Approved") class.

## 3. Understanding Random Forest
Random Forest is an ensemble learning method that builds multiple decision trees during the training phase. For classification, it arrives at a final prediction through a **majority vote** of all the individual trees in the "forest." By aggregating these predictions, the model mitigates the overfitting common in single decision trees and provides a more generalized, robust output. [Image of how a random forest classifier works]

## 4. Other Algorithms (Gradient Boosting)
I selected **Gradient Boosting** as my third algorithm because of its high performance on tabular datasets.
* **Mechanism:** Unlike Random Forest, which builds trees in parallel, Gradient Boosting builds trees sequentially. Each subsequent tree is designed to minimize the errors (residuals) of the previous tree.
* **Pros/Cons:** It is highly accurate, though it can be more prone to overfitting and computationally demanding if hyperparameters are not tuned properly.
* **Performance:** Gradient Boosting demonstrated the best metrics (Accuracy, Precision, Recall, and F1-Score) compared to the Logistic Regression and Random Forest baselines.

## 5. Metrics Discussion
* **Best Performer:** Gradient Boosting achieved the highest scores across all metrics, specifically reaching a perfect recall for the positive class.
* **Strengths/Weaknesses:** The base models (Logistic Regression/Random Forest) were effective but showed a tendency toward false negatives. Gradient Boosting’s high recall highlights its strength in ensuring that qualified applicants are correctly identified.

## 6. Your Findings
For loan approval prediction, I recommend using the **Gradient Boosting** model. Its ability to iteratively refine its understanding of the data allows it to capture complex relationships that simpler algorithms might miss.

Given the financial context of this task, the model's superior recall ensures that the system is sensitive enough to identify deserving applicants, making it the most reliable choice for an automated loan approval framework.
