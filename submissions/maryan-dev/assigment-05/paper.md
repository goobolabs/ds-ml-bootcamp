# Classification in Machine Learning: Theory and Applications

## 1. Introduction to Classification

Classification is a type of supervised learning task in which a model learns
to assign a discrete label, or category, to an input based on a set of
labelled training examples. During training, the algorithm is shown many
examples of inputs paired with the correct category, and it uses this data
to build a decision rule that can then be applied to new, unseen inputs
(Géron, 2019). The output of a classification model is always one of a
finite, predefined set of classes — for example, "approved" or "denied,"
"spam" or "not spam," or "malignant" or "benign."

Classification is often confused with regression because both are
supervised learning tasks that use labelled data, but the key difference
lies in the type of output each one produces. A classification model
predicts a category, while a regression model predicts a continuous
numeric value (James et al., 2021). For instance, predicting whether a loan
application will be *approved or denied* is a classification problem,
because the answer belongs to one of two discrete categories. In contrast,
predicting *how much a bank should lend* to an applicant, or forecasting a
house's *sale price* based on its size and location, is a regression
problem, because the output can take any value along a continuous scale.

A real-life example of classification is email spam detection, where a
model reads the content of an email and assigns it to one of two classes:
"spam" or "not spam." A real-life example of regression is predicting a
person's monthly electricity bill based on the size of their home, the
number of appliances, and the local temperature — the output is a
continuous dollar amount rather than a category.

## 2. Classification Algorithms

### 2.1 Logistic Regression

Logistic Regression is a linear model that estimates the probability that
an input belongs to a particular class. Despite its name, it is used for
classification, not regression: it takes a weighted combination of the
input features, similarly to linear regression, and then passes that
combination through a sigmoid function, which squashes the result into a
value between 0 and 1 that can be interpreted as a probability (Hosmer et
al., 2013). If that probability is above a chosen threshold (commonly 0.5),
the model predicts the positive class; otherwise, it predicts the negative
class.

A common real-world use case for Logistic Regression is credit scoring,
where banks estimate the probability that a customer will default on a
loan based on features such as income, credit history, and existing debt.
Its main advantages are that it is fast to train, easy to interpret (the
learned coefficients show how much each feature pushes the prediction
toward one class or the other), and performs well when the relationship
between the features and the outcome is roughly linear. Its main
limitation is that it struggles to capture complex, non-linear
relationships between features unless those relationships are engineered
into the input data beforehand.

### 2.2 Decision Trees

A Decision Tree is a model that splits the data into smaller and smaller
subsets by repeatedly asking a series of yes/no questions about the
features, forming a tree-like structure of decision nodes (Breiman et al.,
1984). At each node, the algorithm selects the feature and threshold that
best separates the classes, often using a measure such as the Gini index
or information gain. Once trained, a new observation is classified by
following the path of questions from the root of the tree down to a leaf
node, which holds the predicted class.

Decision Trees are widely used in medical diagnosis, for example to
determine whether a patient is at high or low risk for a disease based on
a checklist of symptoms and test results. Their main advantage is
interpretability: the resulting tree can be visualized and read almost
like a flowchart, making it easy to explain a prediction to a
non-technical audience. Their main limitation is that a single deep tree
tends to overfit the training data, memorizing noise rather than learning
generalizable patterns, which can make it perform poorly on new data.

### 2.3 Random Forest

Random Forest is an ensemble method that builds on the idea of Decision
Trees by training many trees instead of just one and combining their
predictions (Breiman, 2001). Each tree in the forest is trained on a
different random sample of the training data (a technique called
bagging), and at each split, the tree is only allowed to consider a random
subset of the available features. This introduces diversity among the
trees, so that they tend to make different mistakes from one another. For
a classification task, every tree "votes" for a class, and the forest
outputs the class that receives the majority of votes.

Random Forests are commonly used in fraud detection, where banks need to
flag suspicious transactions among millions of legitimate ones. Their main
advantage is that averaging over many diverse trees reduces the
overfitting problem that a single Decision Tree suffers from, generally
resulting in a more robust and accurate model. Their main limitation is
reduced interpretability compared to a single tree or Logistic Regression:
because a prediction is the combined result of potentially hundreds of
trees, it is harder to explain exactly why the model reached a particular
decision, and the model is also more computationally expensive to train
and to use for prediction.

### 2.4 Comparison

Logistic Regression is the simplest and most interpretable of the three,
and works best when the relationship between features and the outcome is
close to linear. Decision Trees can capture non-linear relationships and
are also easy to interpret, but are prone to overfitting on their own. Random
Forest addresses that overfitting problem by combining many trees, usually
achieving higher accuracy, at the cost of interpretability and
computational efficiency.

## 3. Classification Metrics

Once a classification model has been trained, its quality is measured
using several standard metrics, each of which captures a different aspect
of performance (Powers, 2020).

**Accuracy** measures the overall proportion of predictions the model got
right, calculated as the number of correct predictions divided by the
total number of predictions. It is easy to understand, but it treats every
class equally regardless of how common it is in the data.

**Precision** measures, out of all the cases the model predicted as
positive, how many were actually positive. It answers the question: "when
the model says 'approved,' how often is it right?" Precision matters most
when the cost of a false positive is high.

**Recall** (also called sensitivity) measures, out of all the cases that
were actually positive, how many the model correctly identified. It
answers the question: "out of all the applicants who truly deserved
approval, how many did the model actually approve?" Recall matters most
when the cost of a false negative is high.

**F1-Score** is the harmonic mean of Precision and Recall, combining both
into a single number. It is especially useful when there is a trade-off
between Precision and Recall and a balanced view of both is needed.

**Confusion Matrix** is a table that lays out all four possible outcomes of
a classifier's predictions compared to the actual labels: true positives,
true negatives, false positives, and false negatives. Rather than
summarizing performance into a single number, it shows exactly what kinds
of mistakes the model is making, which is useful for diagnosing whether a
model is biased toward false positives or false negatives.

| Metric | What It Measures | Sensitivity to Class Imbalance |
|---|---|---|
| Accuracy | Overall proportion of correct predictions | High — can be misleadingly high if one class dominates |
| Precision | Correctness of positive predictions | Moderate — drops if the model over-predicts the positive class |
| Recall | Coverage of actual positive cases | Moderate — drops if the model misses positive cases in the minority class |
| F1-Score | Balance between Precision and Recall | Low — more robust than accuracy for imbalanced data |
| Confusion Matrix | Full breakdown of all four outcome types | Not summarized into one number, so imbalance is directly visible |

## 4. Class Imbalance

Accuracy can be misleading when the classes are imbalanced because a model
can achieve a high accuracy score simply by always predicting the majority
class. For example, if 90% of loan applicants in a dataset are approved
and only 10% are denied, a model that blindly predicts "approved" for
every applicant would achieve 90% accuracy, despite never correctly
identifying a single denied applicant. This makes accuracy an unreliable
metric on its own whenever one class is much more frequent than the other
(He and Garcia, 2009).

Whether to prioritize Precision or Recall depends on which type of error is
more costly for the specific application. In the context of loan approval,
if the bank wants to avoid approving loans that are likely to default, it
would prioritize Precision, since a false positive (approving an applicant
who should have been denied) directly leads to a bad loan and a potential
financial loss. On the other hand, if the bank's main priority is ensuring
that no creditworthy applicant is unfairly denied — for instance to remain
competitive or to comply with fair-lending regulations — it would
prioritize Recall, since a false negative (denying an applicant who should
have been approved) means losing a good customer and potential reputational
or legal risk. In practice, most lenders try to balance both concerns,
which is why the F1-Score is often reported alongside Precision and Recall
individually.

## 5. Real-World Case Study

A recent example of classification applied in the finance sector is a 2025
study titled *"Data-Driven Loan Default Prediction: A Machine Learning
Approach for Enhancing Business Process Management,"* published in the
journal *Systems* (MDPI). The goal of the study was to evaluate how
effectively different machine learning models could predict whether a
borrower would default on a loan, with the aim of improving risk
management and loan approval decisions for financial institutions.

The researchers used a structured loan dataset and applied a full machine
learning pipeline, including data preprocessing, feature engineering, and
techniques to handle class imbalance such as SMOTE (Synthetic Minority
Over-sampling Technique) and class weighting, since defaulters typically
make up a much smaller share of borrowers than non-defaulters. They
compared several classifiers, including XGBoost, Gradient Boosting, Random
Forest, and LightGBM, and evaluated them using accuracy, F1-score, ROC AUC,
precision-recall curves, and confusion matrices (MDPI, 2025).

The key finding was that Gradient Boosting achieved the strongest overall
performance among the models tested, reaching an accuracy of roughly 0.89
and a recall of roughly 0.80, a result the authors highlighted as
particularly valuable for minimizing the risk of missing actual defaulters
(MDPI, 2025). The study also reported practical benefits for financial
institutions, such as improved risk management and more efficient loan
approval processes, while pointing out ongoing challenges around
regulatory compliance and model interpretability. This echoes the same
trade-off discussed in Section 2 of this paper: simpler models like
Logistic Regression are easier to explain, while ensemble models like
Gradient Boosting and Random Forest tend to perform better numerically but
are harder to interpret. This case study reinforces a central theme of
classification in practice: the "best" model is not always the most
accurate one in isolation, but the one that best matches the priorities
and constraints of the real-world problem it is being used to solve.

## References

Breiman, L. (2001). Random forests. *Machine Learning*, 45(1), 5–32.

Breiman, L., Friedman, J. H., Olshen, R. A., & Stone, C. J. (1984).
*Classification and Regression Trees*. Wadsworth International Group.

Géron, A. (2019). *Hands-On Machine Learning with Scikit-Learn, Keras, and
TensorFlow* (2nd ed.). O'Reilly Media.

He, H., & Garcia, E. A. (2009). Learning from imbalanced data. *IEEE
Transactions on Knowledge and Data Engineering*, 21(9), 1263–1284.

Hosmer, D. W., Lemeshow, S., & Sturdivant, R. X. (2013). *Applied Logistic
Regression* (3rd ed.). Wiley.

James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An
Introduction to Statistical Learning: with Applications in R* (2nd ed.).
Springer.

MDPI. (2025). Data-Driven Loan Default Prediction: A Machine Learning
Approach for Enhancing Business Process Management. *Systems*, 13(7), 581.
https://www.mdpi.com/2079-8954/13/7/581

Powers, D. M. W. (2020). Evaluation: From precision, recall and F-measure
to ROC, informedness, markedness and correlation. arXiv preprint
arXiv:2010.16061.