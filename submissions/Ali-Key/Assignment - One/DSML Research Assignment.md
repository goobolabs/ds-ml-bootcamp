# Introduction to Data Science and Machine Learning
> Research Assignment - DSML - 2026 

---

**Course:** Introduction to Data Science and Machine Learning
**Due:** Monday, June 15, 2026 at 12:00 PM (Africa/Mogadishu / EAT)        
**Author:** Ali Omar Abdi — Alikey
**Sources:** 16 references

---

## Table of Contents

1. [Q1 — Data Science and Machine Learning](#q1----data-science-and-machine-learning)
2. [Q2 — The Data Science Lifecycle](#q2----the-data-science-lifecycle)
3. [Q3 — Supervised vs. Unsupervised Learning](#q3----supervised-vs-unsupervised-learning)
4. [Q4 — Overfitting](#q4----overfitting)
5. [Q5 — Train/Test Split](#q5----traintest-split)
6. [Q6 — Case Study: ML in Healthcare](#q6----case-study-ml-in-healthcare)
7. [References](#references)

---

## Q1 — Data Science and Machine Learning

**Data Science** is the process of turning raw data into useful answers. It covers everything: collecting data, cleaning it, finding patterns, and explaining results. Think of it as the full job, not just one skill.

**Machine Learning** is one tool inside that job. Instead of writing rules by hand, you feed the computer examples and it figures out the patterns itself. Like teaching a child to recognize cats by showing pictures, not writing a rulebook.

They are related but not the same. ML is the prediction engine. Data Science is everything around it.

| | Data Science | Machine Learning |
|---|---|---|
| Covers | The whole process | Just the learning step |
| Goal | Useful insights | Predictions from data |
| Output | Reports, dashboards | A trained model |

**Real-life example: Fraud detection.**
Data Science collects and cleans bank transactions. ML then trains on millions of labeled examples (fraud / not fraud) and flags suspicious ones in milliseconds. One cannot work without the other here.

---

## Q2 — The Data Science Lifecycle

Most projects follow **CRISP-DM**, a six-stage framework built in the 1990s and still widely used today. The stages are not always linear — teams loop back when they learn something new.

| Stage | What Happens |
|---|---|
| 1. Business Understanding | Define the question clearly |
| 2. Data Understanding | Check what data exists and whether it is usable |
| 3. Data Preparation | Clean, fix, and structure the data (70-80% of the work) |
| 4. Modeling | Train a Machine Learning model — **this is where ML enters** |
| 5. Evaluation | Test the model on unseen data |
| 6. Deployment | Put the model into a real system and monitor it |

ML fits at Step 4 because it needs clean, prepared data to learn from. Skip Steps 1-3 and the model will not work properly.

---

## Q3 — Supervised vs. Unsupervised Learning

**Supervised learning** trains on labeled data — every example already has a correct answer attached. The model learns to predict that answer for new inputs.

**Unsupervised learning** has no labels. The algorithm finds hidden patterns on its own.

| | Supervised | Unsupervised |
|---|---|---|
| Data | Labeled | Unlabeled |
| Goal | Predict a known answer | Find hidden structure |
| Output | A prediction or category | Clusters or simplified data |
| Example | Spam filter | Customer segmentation |
| Algorithms | Linear Regression, SVM, Neural Networks | K-Means, PCA |

**Supervised example:** A spam filter trained on thousands of emails marked "spam" or "not spam."
**Unsupervised example:** A supermarket groups customers by purchase behavior, with no categories defined in advance.

---

## Q4 — Overfitting

Overfitting is when a model memorizes the training data instead of learning from it. It scores high on training but fails on new data.

Think of a student who memorizes last year's exam answers word for word. They pass that exact paper but fail when the questions change.

The core tension is the **bias-variance tradeoff:**

| Problem | Cause | Result |
|---|---|---|
| Underfitting (high bias) | Model too simple | Bad on both training and test data |
| Overfitting (high variance) | Model too complex | Great on training, bad on test data |

**How to prevent overfitting:**
- Get more training data
- Use regularization (L1 or L2) to penalize complexity
- Use cross-validation instead of one fixed test set
- Stop training early when performance plateaus
- Use a simpler model if it performs just as well
- Use dropout in neural networks

---

## Q5 — Train/Test Split

Before training, split the dataset into separate parts. The rule: **never test a model on data it trained on.** A model tested on its own training data looks great even if it just memorized the examples.

| Subset | Purpose |
|---|---|
| Training set | What the model learns from |
| Validation set | Used during development to tune settings |
| Test set | Used once at the end to measure real performance |

**Common split ratios:**

| Split | Train | Validation | Test |
|---|---|---|---|
| 80/20 | 80% | - | 20% |
| 70/15/15 | 70% | 15% | 15% |
| 80/10/10 | 80% | 10% | 10% |

Two rules: shuffle before splitting, and use stratified sampling when classes are unbalanced (e.g. only 2% fraud cases).

The test set is like a mock exam. If the model passes, it learned something real, not just memorized the study material.

---

## Q6 — Case Study: ML in Healthcare

**Source:** Iparraguirre-Villanueva et al. (2023). *Application of Machine Learning Models for Early Detection and Accurate Classification of Type 2 Diabetes.* Diagnostics, 13(14), 2383. https://doi.org/10.3390/diagnostics13142383

By 2021, 537 million adults had Type 2 diabetes. The number is rising. Catching it early matters because complications (kidney failure, nerve damage) develop slowly and silently. Standard diagnosis needs lab tests, which are not always accessible.

This study trained five ML models on the Pima Indian Diabetes Dataset (768 patients, 8 basic health measurements each) to predict diabetes risk.

| Algorithm | What It Does |
|---|---|
| K-Nearest Neighbors | Finds the most similar past patients |
| Naive Bayes | Uses probability to classify |
| Decision Tree | Asks yes/no questions to reach a conclusion |
| Logistic Regression | Calculates probability of each class |
| Support Vector Machine | Finds the best boundary between classes |

The SVM scored highest. All five models showed that basic clinical data is enough to predict diabetes risk reliably.

**CRISP-DM coverage:**

| Stage | What the Study Did |
|---|---|
| Business Understanding | Detect Type 2 diabetes early |
| Data Understanding | 768 records, 8 features |
| Data Preparation | Cleaned missing values, normalized data |
| Modeling | Trained 5 classifiers |
| Evaluation | Compared accuracy, precision, recall, F1-score |
| Deployment | Proposed best model as a clinical tool |

---

## References

1. Sartorius. (2020). *Data Science, AI and ML — understanding the relationship.* https://www.sartorius.com
2. Pangeanic. (2023). *The relationship between data science and machine learning.* https://blog.pangeanic.com
3. IBM. (2025). *Data science vs. machine learning.* https://www.ibm.com/think/topics/data-science-vs-machine-learning
4. Syracuse University iSchool. (2025). *Data Science vs. Machine Learning.* https://ischool.syracuse.edu
5. Excelsior University. (n.d.). *The Data Science Lifecycle (CRISP-DM).* https://express.excelsior.edu
6. Melo, G. (2024). *CRISP-DM: A comprehensive guide.* Medium. https://medium.com/@gcesarmelo7/crisp-dm
7. Studocu. (2025). *CRISP-DM Model Lifecycle.* https://www.studocu.com
8. IBM. (2025). *Supervised vs. unsupervised learning.* https://www.ibm.com/think/topics/supervised-vs-unsupervised-learning
9. AWS. (2025). *Supervised vs unsupervised learning.* https://aws.amazon.com
10. Lightly.ai. (2024). *Overfitting in machine learning.* https://www.lightly.ai/blog/overfitting
11. Aya Data. (2025). *Underfitting vs. overfitting — a complete guide.* https://www.ayadata.ai
12. Jaro Education. (2025). *Bias-variance tradeoff explained.* https://www.jaroeducation.com
13. EMB Global. (2024). *Train and test data best practices.* https://blog.emb.global
14. Encord. (2026). *How to split machine learning datasets.* https://encord.com/blog/train-val-test-split/
15. Alnuaimi et al. (2024). *Train/test ratio in ML for medical imaging.* PMC / NIH. https://pmc.ncbi.nlm.nih.gov/articles/PMC11419616/
16. Iparraguirre-Villanueva et al. (2023). *ML for early detection of Type 2 Diabetes.* Diagnostics, 13(14), 2383. https://doi.org/10.3390/diagnostics13142383

---


*Submitted for DS-ML Bootcamp — Assignment 1*
*Due: Saturday, June 15, 2026*