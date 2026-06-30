# Assignment 01: Introduction to Data Science and Machine Learning

**Name:** Alisalad

---

## 1. Data Science vs. Machine Learning

Data Science is the broader field — collecting, cleaning, analyzing, and interpreting data to answer questions or guide decisions. Machine Learning is a subset of it: techniques where a system learns patterns from data instead of following hand-written rules.

**Example:** A mobile money service wants to catch fraudulent transactions. The Data Science part is pulling transaction logs, cleaning them, and deciding which features matter (amount, frequency, location). The Machine Learning part is training a model on past flagged transactions so it can score new ones automatically. Data Science frames the problem and prepares the data; Machine Learning is the pattern-learning piece.

---

## 2. The Data Science Lifecycle

The typical lifecycle stages are:

1. Problem definition
2. Data collection
3. Data cleaning and preparation
4. Exploratory data analysis
5. Modeling
6. Evaluation
7. Deployment
8. Monitoring

Machine Learning fits in at the **modeling** stage. However, the quality of the model depends heavily on the stages before it — data collection and cleaning usually take more time and effort than building the model itself.

---

## 3. Supervised vs. Unsupervised Learning

**Supervised Learning:** Uses labeled data, where the model learns a mapping from inputs to known outputs.
*Example:* Emails labeled as "spam" or "not spam" are used to train a model that classifies new, incoming emails.

**Unsupervised Learning:** Uses unlabeled data; the model finds structure or groupings on its own without predefined categories.
*Example:* An Aphone retailer clusters customers based on purchase behavior. The model groups similar buyers together without being told the categories in advance, and the business interprets the clusters afterward (e.g., budget buyers vs. repeat brand-loyal customers).

---

## 4. Overfitting

**Overfitting** occurs when a model learns the training data too well — including its noise and random variations — so it performs well on training data but poorly on new, unseen data.

**Common causes:**
- Model too complex relative to the amount of data
- Training for too long
- Too little training data
- Irrelevant or noisy features

**Prevention methods:**
- Cross-validation
- Regularization (L1/L2)
- Simplifying the model (fewer parameters)
- Early stopping
- Increasing training data
- Dropout (for neural networks)

---

## 5. Training/Test Data Split

Data is typically split into:
- **Training set** (often 70–80%) — used to fit the model
- **Test set** (often 20–30%) — held back and used only for final evaluation

A **validation set** may also be carved out from the training data for tuning hyperparameters.

**Why this matters:** Evaluating a model on the same data it was trained on measures memorization, not real-world performance. The test set simulates how the model will behave on new, unseen data. For time-series data, the split is done chronologically (train on past, test on future) rather than randomly, to avoid leaking future information into training.

---

## 6. Case Study — Machine Learning in Healthcare

Microsoft's **InnerEye** software differentiates healthy cells from tumor cells and plans radiation therapy courses roughly **13 times faster** than manual methods.

*Source: Glorium Tech, "Machine Learning in Healthcare: Case Studies of Those Who Did," gloriumtech.com*

**Lifecycle stage covered:** Modeling and Deployment. The model was trained on labeled medical imaging data (healthy vs. tumor — a supervised learning approach) and deployed into clinical workflows to provide an automated first-pass tumor contouring for radiologists.

**Key takeaway:** The goal of this technology is to increase the productivity and coverage of the existing healthcare system, not to replace clinicians — a clear example of Data Science and Machine Learning working together while humans retain final decision-making authority.

---

## References

- Glorium Tech. "Machine Learning in Healthcare: Case Studies of Those Who Did." https://gloriumtech.com/reasons-to-implement-machine-learning-in-healthcare-case-studies-of-those-who-did/
- James, G., Witten, D., Hastie, T., & Tibshirani, R. *An Introduction to Statistical Learning* (concepts on overfitting and train/test splitting)
- CRISP-DM Methodology (reference for the Data Science lifecycle structure)
