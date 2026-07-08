# Assignment Five: Classification Theory Paper

## 1. Introduction to Classification
In Machine Learning, **Classification** is a supervised learning approach where the target task is to predict a categorical, discrete class label for a given input instance. The model learns decision boundaries from historical training data to map independent input features into explicit groups or classes.

Classification differs strictly from **Regression** based on the nature of the target variable:
* **Classification** predicts a discrete value belonging to a predefined set of categories (e.g., $\{0, 1\}$ or $\text{\{Approved, Rejected\}}$).
* **Regression** predicts a continuous, numeric real value across an infinite scale (e.g., predicting a numerical credit score or asset value).

### Real-World Examples:
* **Classification Use Case:** Credit risk assessment determining whether a loan application should be *Approved* or *Rejected* based on applicant details.
* **Regression Use Case:** Predicting the specific market price of a residential property in dollars based on its square footage, location, and rooms.


## 2. Classification Algorithms

### Logistic Regression
* **Basic Idea:** Despite its name, it is a linear classification model. It passes a linear combination of inputs ($z = \beta_0 + \beta_1x_1 + \dots + \beta_nx_n$) through the **Sigmoid function** $\sigma(z) = \frac{1}{1 + e^{-z}}$. This squashes the output value between $0$ and $1$, mapping it directly as a conditional class probability.
* **Real-World Use Case:** E-mail spam filtering (Spam vs. Not Spam).
* **Advantages:** Exceptionally fast to train, requires minimal computational resources, highly interpretable, and yields well-calibrated probabilities.
* **Limitations:** Assumes a linear relationship between independent variables and log-odds; struggles to capture complex, non-linear interactions without intensive manual feature engineering.

### Decision Trees
* **Basic Idea:** A non-parametric model that builds a hierarchical, tree-like structure by recursively partitioning the training dataset based on feature thresholds. Splits are chosen at nodes to maximize information gain or minimize node impurity (using metrics like Gini Impurity or Entropy).
* **Real-World Use Case:** Medical diagnosis trees classifying patients into risk tiers based on sequential clinical symptoms.
* **Advantages:** Easy to visualize, requires minimal data preprocessing (no feature scaling required), and naturally captures non-linear feature interactions.
* **Limitations:** Highly prone to **overfitting** by growing overly deep, complex branches that capture random noise in the training set, making them unstable to small changes in data.

### Random Forest
* **Basic Idea:** An ensemble learning technique based on **Bagging (Bootstrap Aggregating)**. It constructs a collection ("forest") of independent Decision Trees at training time. Each individual tree is grown on a random bootstrap sample of the data using a random subset of features at each split. The final prediction is determined via a **majority vote** across all individual trees.
* **Real-World Use Case:** E-commerce customer churn prediction.
* **Advantages:** Highly accurate, strongly resistant to overfitting, robust to noisy data, and provides internal feature importance metrics.
* **Limitations:** Slower inference time than individual trees, consumes significant memory, and acts as a "black box," losing the visual simplicity of a single Decision Tree.


## 3. Classification Metrics
To properly judge a classifier, multiple evaluation metrics are used depending on the business context:
* **Accuracy:** The proportion of total correct predictions out of all instances.
  $$\text{Accuracy} = \frac{\text{True Positives (TP)} + \text{True Negatives (TN)}}{\text{TP} + \text{TN} + \text{False Positives (FP)} + \text{False Negatives (FN)}}$$
* **Precision:** The proportion of actual positive instances among all instances predicted as positive by the model. It quantifies the cost of committing a False Positive.
  $$\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}$$
* **Recall (Sensitivity):** The proportion of actual positive instances that the model correctly identified. It quantifies the risk of committing a False Negative.
  $$\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}$$
* **F1-Score:** The harmonic mean of Precision and Recall, providing a single balanced metric that penalizes extreme imbalances between the two.
  $$\text{F1-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$
* **Confusion Matrix:** A $2\times2$ tabular grid tracking specific cross-counts of actual versus predicted classes ($\text{TP}, \text{TN}, \text{FP}, \text{FN}$), detailing exactly where classification errors occur.

### Summary Comparison Table:
| Metric | Primary Measurement Focus | Sensitivity to Class Imbalance |
| :--- | :--- | :--- |
| **Accuracy** | Overall correctness across all classes | **Highly Sensitive** (Highly misleading for imbalanced data) |
| **Precision** | Reliability of positive predictions (minimizing false alarms) | Low sensitivity to majorities; focuses on the positive class |
| **Recall** | Coverage of actual positive instances (minimizing missed targets) | Low sensitivity to majorities; focuses on actual positives |
| **F1-Score** | Balance between Precision and Recall | **Robust** (Ideal choice for imbalanced distributions) |


## 4. Class Imbalance
When a dataset contains a disproportionate number of samples in one class over another (e.g., $95\%$ non-fraudulent vs. $5\%$ fraudulent), **Accuracy becomes highly misleading**. A naive model could simply predict the majority class for every row and achieve a deceptive $95\%$ accuracy score while completely failing to identify any critical minority events.

### Loan Approval Trade-offs (Precision vs. Recall):
* **Prioritizing Precision over Recall:** A financial institution prioritizes Precision when it wants to be absolutely certain that a borrower marked as "Approved" will not default. A False Positive here means approving a high-risk borrower who goes bankrupt, leading to severe financial loss. Higher Precision minimizes this credit risk.
* **Prioritizing Recall over Precision:** A lending company prioritizes Recall when its core business strategy is aggressive market expansion. A False Negative here means mistakenly rejecting a creditworthy borrower, causing a lost customer acquisition opportunity. High Recall ensures the institution does not turn away viable revenue.


## 5. Real-World Case Study
* **Goal:** Automate credit scoring and default risk prediction for retail banking portfolios.
* **Data Used:** Anonymized demographic data, historical credit usage, payment delays, debt ratios, and employment durations.
* **Classifier Applied:** Random Forest Classifier combined with SMOTE (Synthetic Minority Over-sampling Technique) to combat class imbalance.
* **Key Insights:** The study demonstrated that Random Forest significantly outperformed standard Logistic Regression, particularly in identifying high-risk defaults (Recall). The integration of engineered features like Debt-to-Income ratios proved to have the highest feature importance score, reducing bank loan defaults by over $12\%$ during production deployments.