# Assignment Five: Classification — Theory Paper

## Part A — Theory

---

### 1. Introduction to Classification

#### What is Classification in Machine Learning?

Classification is a type of supervised machine learning task in which the goal is to assign an input observation to one of a predefined set of discrete categories, or classes. The algorithm learns a mapping function from a labeled training set — where each example has both a set of input features and a known class label — and then uses that learned function to predict the class of previously unseen observations. The output of a classification model is always categorical: for example, "Approved" or "Rejected," "Spam" or "Not Spam," or one of several named disease types.

#### How is it Different from Regression?

Although both classification and regression are forms of supervised learning, they differ fundamentally in the type of output they produce. Regression predicts a **continuous numeric value** — it answers the question "how much?" For example, a regression model might estimate that a house is worth $342,000, or that tomorrow's temperature will be 28°C. Classification, by contrast, predicts a **discrete label** — it answers the question "which category?" The boundary between classes is learned during training, and the model assigns each new input to whichever category it finds most likely.

A useful mental model: regression outputs live on a number line with infinite possible values, while classification outputs live in a finite set of buckets.

#### Real-Life Examples

- **Classification:** A bank's fraud detection system that examines each credit card transaction and labels it as either **Legitimate** or **Fraudulent** based on transaction amount, location, merchant type, and time of day.
- **Regression:** A real estate platform that predicts the **selling price** (in dollars) of a home based on its square footage, number of bedrooms, neighborhood, and year built.

---

### 2. Classification Algorithms

#### Logistic Regression

**How it works:** Despite containing the word "regression" in its name, Logistic Regression is a classification algorithm. It models the probability that an observation belongs to a particular class by applying the **sigmoid function** to a linear combination of the input features. The sigmoid function compresses any real-valued number into the interval (0, 1), which can then be interpreted as a probability. A threshold — typically 0.5 — converts this probability into a hard class label: if the model estimates a probability above 0.5, it predicts the positive class; otherwise, it predicts the negative class.

**Real-world use case:** Email spam filtering — the model estimates the probability that an email is spam based on keyword frequency, sender reputation, and subject line content, then labels it accordingly.

**Advantages:**
- Computationally efficient and fast to train, even on large datasets.
- Outputs calibrated probabilities, not just hard labels, which enables threshold tuning.
- Highly interpretable: the sign and magnitude of each coefficient directly indicate a feature's influence on the predicted class.

**Limitations:**
- Assumes a roughly linear decision boundary, which means it struggles with complex, non-linear relationships in the data.
- Feature engineering (e.g., polynomial terms, interaction terms) is required to capture curvature.
- Sensitive to outliers, which can distort the fitted coefficients.

---

#### Decision Trees

**How it works:** A Decision Tree is a hierarchical model that splits the training data into progressively smaller, purer subsets using a series of binary questions based on feature values. At each internal node, the algorithm selects the feature and threshold that best separates the classes — most commonly measured by **Gini impurity** or **information gain (entropy)**. The process repeats recursively on each resulting subset until a stopping condition is met (maximum depth, minimum samples per leaf, or perfect purity), at which point the leaf node is assigned a class label corresponding to the majority class it contains.

**Real-world use case:** Customer churn prediction in a telecommunications company — the tree might first split on "contract type," then on "monthly charges," then on "number of service calls," to arrive at a prediction of whether a customer will leave within the next month.

**Advantages:**
- Highly interpretable and can be visualized as a flowchart that a non-technical stakeholder can follow.
- No feature scaling required — the algorithm is invariant to monotonic transformations of the input.
- Naturally handles both numeric and categorical features without heavy preprocessing.

**Limitations:**
- Highly prone to overfitting when allowed to grow deep — a single tree can memorize noise in the training data.
- Unstable: small changes to the training data can lead to a completely different tree structure.
- Typically outperformed by ensemble methods such as Random Forest on complex datasets.

---

#### Random Forest

**How it works:** Random Forest is an **ensemble method** that addresses the instability and overfitting of individual decision trees by building a large collection of trees and combining their predictions. Two key sources of randomness are introduced during training: (1) **Bootstrap sampling** — each tree is trained on a random sample of the training data drawn with replacement (a "bagged" sample), and (2) **Feature subsampling** — at each split within a tree, only a random subset of features is considered as candidates for the best split. For classification, each tree casts a vote for a class label, and the forest's final prediction is the class that receives the **majority of votes**.

**Real-world use case:** Credit scoring at a bank — hundreds of trees independently evaluate an applicant's income, credit history, employment duration, and existing debts, and their collective majority vote determines the loan approval recommendation.

**Advantages:**
- Significantly more accurate and robust than a single decision tree due to variance reduction through averaging.
- Handles non-linear relationships and feature interactions without manual engineering.
- Built-in feature importance scores, which identify which variables most strongly influence predictions.

**Limitations:**
- Much less interpretable than a single decision tree — it is often described as a "black box."
- Computationally more expensive to train and predict, especially with many trees and high-dimensional data.
- Hyperparameter tuning (number of trees, max depth, feature subset size) requires careful cross-validation.

---

#### Algorithm Comparison Table

| Feature | Logistic Regression | Decision Tree | Random Forest |
|---|---|---|---|
| Output type | Class probability then label | Hard class label | Hard class label (majority vote) |
| Interpretability | High | Very high | Low |
| Handles non-linearity | Limited | Yes | Yes |
| Overfitting risk | Low | High | Low (ensemble reduces variance) |
| Feature scaling needed | Yes | No | No |
| Training speed | Very fast | Fast | Slower (many trees) |
| Best used as | Simple, fast baseline | Explainable decisions | Strong general-purpose model |

---

### 3. Classification Metrics

When evaluating a classification model, it is essential to look beyond a single number. Four foundational point metrics and one summary matrix are used in practice.

#### Accuracy

Accuracy is the proportion of all predictions that were correct — both correctly predicted positives and correctly predicted negatives. It is the most intuitive metric: if a model gets 90 out of 100 loan decisions right, its accuracy is 90%. However, accuracy is **sensitive to class imbalance**: if 95 out of 100 applicants are always approved, a model that naively predicts "Approved" for every applicant achieves 95% accuracy while completely failing to identify any risky borrowers.

#### Precision

Precision answers the question: *Of all the applicants the model predicted as "Approved," how many were genuinely creditworthy?* It is calculated as the number of True Positives divided by the total number of predicted positives (True Positives + False Positives). High precision means the model rarely approves someone who should be rejected. Precision is not affected by the total number of actual negatives, so it remains informative even when classes are imbalanced.

#### Recall (Sensitivity)

Recall answers the question: *Of all the applicants who genuinely should have been approved, how many did the model correctly identify?* It is calculated as True Positives divided by the total number of actual positives (True Positives + False Negatives). High recall means the model rarely misses a good applicant. Like precision, recall is insensitive to the class imbalance of the negative class.

#### F1-Score

The F1-Score is the **harmonic mean** of Precision and Recall. Because it uses the harmonic mean rather than the arithmetic mean, it strongly penalizes imbalances between the two metrics: a model with very high precision but very low recall (or vice versa) will have a low F1-Score. This makes F1 the preferred single metric when both false positives and false negatives carry meaningful costs and classes are not perfectly balanced.

#### Confusion Matrix

The Confusion Matrix is a 2x2 table (for binary classification) that provides a complete breakdown of all prediction outcomes:

|  | Predicted Approved | Predicted Rejected |
|---|---|---|
| **Actually Approved** | True Positive (TP) | False Negative (FN) |
| **Actually Rejected** | False Positive (FP) | True Negative (TN) |

Every scalar metric above (Accuracy, Precision, Recall, F1) is derivable from these four cells. Reading the matrix directly reveals not just how often the model is wrong, but *what kind* of mistakes it makes — which is critical for real-world decision making.

#### Metrics Comparison Table

| Metric | Question it Answers | Formula | Sensitive to Class Imbalance? |
|---|---|---|---|
| Accuracy | How many predictions are correct overall? | (TP + TN) / (TP + TN + FP + FN) | Yes |
| Precision | Of predicted approvals, how many were truly approvable? | TP / (TP + FP) | No |
| Recall | Of actual approvals, how many did the model catch? | TP / (TP + FN) | No |
| F1-Score | How well do Precision and Recall balance? | 2 x (P x R) / (P + R) | No |
| Confusion Matrix | What are the exact counts of TP, FP, FN, TN? | Full breakdown | Shows full picture |

---

### 4. Class Imbalance

#### Why Can Accuracy Be Misleading?

Accuracy is computed as the fraction of all predictions that are correct. When one class dominates the dataset — for example, 95% of loan applications are approved — the overall accuracy figure is dominated by performance on the majority class. A trivial classifier that predicts "Approved" for every single applicant achieves 95% accuracy without ever examining any feature. This creates a false sense of model quality: in a real bank, approving every application regardless of risk would be financially catastrophic. Accuracy fails here because it does not separately account for how well the model performs on each class.

#### Precision vs. Recall in Loan Approval

The appropriate metric to prioritize depends on the **cost of each type of mistake**:

- **Prioritize Precision** when false positives are costly. In the loan context, a false positive means approving an applicant who will default. The bank loses the principal amount of the loan. If the bank wants to minimize its credit losses, it should maximize Precision — even if that means rejecting some genuinely creditworthy applicants.

- **Prioritize Recall** when false negatives are costly. A false negative in loan approval means rejecting a good applicant who would have repaid. The bank loses the potential revenue from that loan and may damage its reputation. If the bank is trying to grow its loan portfolio and is less worried about defaults, it should maximize Recall to catch as many qualifying applicants as possible.

In practice, the F1-Score is used as a compromise metric when both types of error have significant consequences.

---

### 5. Real-World Case Study

**Field:** Healthcare  
**Reference:** Rajpurkar, P., et al. (2017). *CheXNet: Radiologist-Level Pneumonia Detection on Chest X-Rays with Deep Learning.* Stanford ML Group.

**Goal:** Automate the detection of pneumonia from chest X-ray images, enabling faster and more scalable screening — particularly valuable in resource-constrained settings where radiologists are scarce.

**Data Used:** The ChestX-ray14 dataset from the National Institutes of Health (NIH), containing over 100,000 frontal-view chest X-ray images labeled across 14 different thoracic diseases, with a binary pneumonia label used for the primary classification task.

**Type of Classifier Applied:** A deep convolutional neural network (CNN) — specifically a 121-layer DenseNet architecture fine-tuned on the labeled chest X-ray dataset. While architecturally different from traditional classifiers like Logistic Regression or Random Forest, it is fundamentally a binary classification model predicting "Pneumonia" or "No Pneumonia" for each image.

**Key Results:** CheXNet achieved an F1-Score of 0.435 on the NIH test set, which surpassed the average F1-Score of 0.387 achieved by a panel of four practicing radiologists on the same images. The study demonstrated that a classification model could reach expert-level performance on a specific diagnostic task. The authors emphasized that Recall was particularly important in this context — missing a case of pneumonia (a false negative) carries a far greater cost than flagging a healthy patient for review (a false positive), since untreated pneumonia can be life-threatening. This mirrors the Recall-prioritization logic discussed in the loan approval context, illustrating how the choice of evaluation metric must always align with the real-world consequences of each type of error.

---

*References:*
- *Rajpurkar, P., et al. (2017). CheXNet: Radiologist-Level Pneumonia Detection on Chest X-Rays with Deep Learning. arXiv:1711.05225.*
- *Geron, A. (2022). Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow (3rd ed.). O'Reilly Media.*
- *Scikit-learn Documentation: https://scikit-learn.org/stable/supervised_learning.html*
