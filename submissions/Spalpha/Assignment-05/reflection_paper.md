# Assignment Five: Practical Reflection Paper

## 1. Implementation Summary
For this assignment, I successfully implemented a complete end-to-end Machine Learning classification pipeline inside two Jupyter Notebooks using the dataset `raw_loan_dataset.csv`[cite: 1, 3]. In `loan_data_processing.ipynb`, I built a data preparation routine that cleaned text currency symbols, resolved mixed-string label typos using an automated map dictionary, filled missing items via median/mode imputation, capped extreme outliers using Interquartile Range (IQR) bounding boundaries, and engineered two predictive features: `DebtToIncome` and `IncomePerYearEmployed`[cite: 1, 3]. Instead of default normalization, I researched and integrated `RobustScaler` to transform numeric scales safely around outliers[cite: 1, 3].

In `loan_approval_prediction.ipynb`, the clean dataset was loaded and split using a stratified 80/20 partition[cite: 1, 2]. I trained three models: **Logistic Regression** and **Random Forest** (to reproduce the lesson parameters), plus a researched third algorithm: **K-Nearest Neighbors (KNN)**[cite: 1, 2].


## 2. Comparison of Models & Sanity Check
During the automated sample check (index test row 3), the models yielded identical predictions[cite: 2]:
* **Actual Label:** 1[cite: 2]
* **Logistic Regression Prediction:** 1[cite: 2]
* **Random Forest Prediction:** 1[cite: 2]
* **KNN Prediction:** 1[cite: 2]

While all three models successfully flagged the sample applicant correctly, their inner mechanisms differed significantly[cite: 2]. Logistic Regression provides a smoother, generalized probability estimate across a linear plane[cite: 2]. Random Forest provides a more realistic and robust assessment for complex applications because it evaluates strict conditional split thresholds (such as combinations of low debt-to-income and strong credit scores) without assuming linear trends[cite: 2].
-

## 3. Understanding Random Forest
A **Random Forest** is an ensemble classifier that operates by building multiple individual Decision Trees during training. To prevent individual trees from replicating the exact same rules, it injects random variations: each tree is trained on a random sample of rows (bootstrapping) and evaluates only a random subset of features at each split point. 

When a new loan applicant needs evaluation, the data is fed into every tree in the forest. Each tree outputs its own prediction (e.g., Tree 1 says "Approve", Tree 2 says "Reject", Tree 3 says "Approve"). The forest combines these outputs, and the **majority vote** determines the final consensus prediction.


## 4. Third Classifier Research: K-Nearest Neighbors (KNN)
* **Algorithm Choice:** K-Nearest Neighbors (`KNeighborsClassifier`)[cite: 2].
* **Why it fits:** KNN calculates mathematical distances (such as Euclidean distance) across features to classify an instance based on its proximity to its $k$ closest neighbors[cite: 2]. Because our numerical features were completely standardized using `RobustScaler` in Part B1, spatial distances are uniform and meaningful[cite: 2, 3].
* **Findings and Metrics:** KNN matched the Random Forest model on overall test performance[cite: 2]. 
  * *Advantage:* Simple to understand, non-parametric, and highly intuitive for loan officers who want to view identical historical peer files[cite: 2].
  * *Limitation:* Highly sensitive to noisy features and computationally expensive as the size of the loan database grows.


## 5. Metrics Discussion
Based on the empirical test evaluations from the pipeline run[cite: 2]:
* **Logistic Regression:** Accuracy: `0.700` | Precision: `0.733` | Recall: `0.846` | F1-Score: `0.786`[cite: 2]
* **Random Forest:** Accuracy: `0.650` | Precision: `0.714` | Recall: `0.769` | F1-Score: `0.741`[cite: 2]
* **K-Nearest Neighbors:** Accuracy: `0.650` | Precision: `0.688` | Recall: `0.846` | F1-Score: `0.759`[cite: 2]

### Insights:
* **Logistic Regression** achieved the highest overall Accuracy (`0.700`) and Precision (`0.733`), meaning it had the lowest rate of false approval decisions[cite: 2].
* **K-Nearest Neighbors** matched Logistic Regression's high Recall rate (`0.846`), showing a shared ability to capture a high proportion of qualified borrowers, though it suffered from a higher rate of false alarms compared to Logistic Regression[cite: 2].


## 6. Final Findings & Production Recommendation
Given the experimental results on this dataset, **Logistic Regression** is the recommended model for deployment[cite: 2]. It leads across the core metrics, securing the top spot in overall Accuracy (`0.700`) and F1-Score (`0.786`) while displaying strong Precision (`0.733`)[cite: 2]. 

In credit risk environments, minimizing high-risk false approvals (maximizing Precision) while keeping broad coverage intact (high Recall) is essential. Logistic Regression achieves the most effective balance here[cite: 2]. Additionally, its clear coefficient weights offer transparent explanations for credit audits, making it the most sensible choice for the lending platform.