# Data Science & Machine Learning — Research Assignment

## Research Assignment

> **Course:** Introduction to Data Science and Machine Learning
> 

> **Style:** Research-oriented | English
> 

> **Date:** June 2026
> 

---

## Question 1: Defining Data Science and Machine Learning

### What Is Data Science?

Data science is the discipline of extracting useful knowledge from data — raw, messy, large-scale, or otherwise. It sits at the crossroads of statistics, computer science, and domain expertise. A data scientist does not just run models; they define the right question, clean the data, choose the right method, interpret the result, and communicate findings to people who may not know what a p-value is.

As Donoho (2017) argued in his widely cited paper *50 Years of Data Science*, the field is broader than statistics alone — it encompasses data wrangling, exploratory analysis, modeling, and the entire workflow from raw input to decision-ready output.

### What Is Machine Learning?

Machine learning (ML) is a subset of artificial intelligence where systems learn patterns from data rather than following explicitly programmed rules. Instead of a developer writing: *"if the email contains the word 'lottery', mark it as spam"*, an ML model learns that rule by itself after seeing thousands of labeled examples.

Mitchell (1997) defined it cleanly: *"A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E."*

The three main learning paradigms are supervised learning, unsupervised learning, and reinforcement learning — each suited to different types of problems.

### The Relationship Between Them

Machine learning is a tool within data science — a powerful one, but still a tool. Not every data science project uses ML. Some rely entirely on statistical analysis or simple rule-based logic. When a problem is complex enough that manual rule-writing becomes impractical, and there is enough labeled data to train on, ML is brought in.

Think of it this way: data science is the process; machine learning is one of the engines.

### Real-Life Example: Netflix Recommendations

Netflix runs a recommendation engine that decides what to show each user on their homepage. Here is how data science and ML work together in that system:

| Stage | What Happens |
| --- | --- |
| Data Science | Collects viewing history, ratings, search behavior, time of day, device type |
| Data Science | Cleans the data, removes bots, handles missing ratings |
| Machine Learning | Trains a collaborative filtering model to predict which content each user will watch next |
| Data Science | Evaluates model performance, A/B tests the output, reports impact on retention |

Without data science framing the problem, the ML model would have nothing meaningful to train on. Without ML, the recommendation logic would have to be manually written — and at Netflix's scale, that is not realistic.

**References:**

- Donoho, D. (2017). *50 Years of Data Science*. Journal of Computational and Graphical Statistics, 26(4), 745–766.
- Mitchell, T. (1997). *Machine Learning*. McGraw-Hill.
- Gomez-Uribe, C. A., & Hunt, N. (2015). The Netflix Recommender System. *ACM Transactions on Management Information Systems*, 6(4).

---

## Question 2: The Data Science Lifecycle

### Overview

The data science lifecycle is not a single straight line. In practice, teams move back and forth between stages as new findings emerge. That said, most frameworks agree on a core sequence. The CRISP-DM model (Cross-Industry Standard Process for Data Mining) remains the most widely adopted, and it maps neatly to the following stages:

### Stage-by-Stage Breakdown

**Stage 1 — Business/Problem Understanding**

Before any data is touched, the problem must be defined. What decision is being made? What does success look like? What data is available? Skipping this step is one of the most common reasons data science projects fail — teams build technically correct models that answer the wrong question.

**Stage 2 — Data Collection**

Data is gathered from relevant sources: databases, APIs, sensors, surveys, web scraping, or manual entry. The quality of everything that follows depends on the quality of what is collected here.

**Stage 3 — Data Cleaning and Preparation**

This is the part no one puts in the portfolio but everyone spends most of their time on. Missing values are handled, duplicates removed, formats standardized, outliers investigated. Rubin (1976) estimated that data cleaning alone can consume 60–80% of a project's time.

**Stage 4 — Exploratory Data Analysis (EDA)**

Before modeling, analysts explore the data visually and statistically — looking for patterns, distributions, correlations, and anomalies. EDA often reveals that the original problem definition needs adjusting.

**Stage 5 — Modeling**

This is where Machine Learning enters. Algorithms are selected, trained on historical data, tuned, and evaluated. Common approaches include decision trees, neural networks, regression models, and clustering algorithms.

**Stage 6 — Evaluation**

The model's performance is measured using metrics like accuracy, F1 score, RMSE, or AUC — depending on the problem type. The model is tested on data it has never seen before to check that it generalizes beyond the training set.

**Stage 7 — Deployment**

The model is integrated into a real system — a web app, mobile feature, internal tool, or automated pipeline. Deployment is not the end; models degrade over time as the world changes, so monitoring and retraining are necessary.

### Where Machine Learning Fits In

ML fits primarily in **Stage 5 (Modeling)**, but its influence extends into evaluation and sometimes back into feature engineering during preparation. ML is not appropriate at Stage 1 or 2 — those stages require human judgment, domain knowledge, and stakeholder input that algorithms cannot replace.

| Lifecycle Stage | ML Involved? | Why |
| --- | --- | --- |
| Problem Definition | No | Requires human judgment |
| Data Collection | No | Domain-driven decisions |
| Data Cleaning | Partially | Some anomaly detection tools |
| EDA | No | Statistical exploration |
| Modeling | Yes — core stage | Pattern learning from data |
| Evaluation | Yes | Model performance metrics |
| Deployment | Yes | Serving predictions in production |

**References:**

- Chapman, P., et al. (2000). *CRISP-DM 1.0: Step-by-step data mining guide*. SPSS Inc.
- Rubin, D. B. (1976). Inference and Missing Data. *Biometrika*, 63(3), 581–592.

---

## Question 3: Supervised vs. Unsupervised Learning

### Supervised Learning

In supervised learning, the model is trained on a labeled dataset — meaning each input comes with a known, correct output. The algorithm learns to map inputs to outputs by minimizing prediction error. Once trained, it can predict outputs for new, unseen inputs.

**Example: Email Spam Detection**

A training dataset contains thousands of emails, each labeled "spam" or "not spam." A supervised classifier (e.g., Naive Bayes or Logistic Regression) learns which words, senders, and patterns are associated with spam. When a new email arrives, the model predicts whether it is spam or not.

**Common Supervised Algorithms:**

- Linear/Logistic Regression
- Decision Trees and Random Forests
- Support Vector Machines (SVM)
- Neural Networks

### Unsupervised Learning

In unsupervised learning, the training data has no labels. The algorithm must discover patterns, groupings, or structure on its own. There is no right or wrong answer given during training — the model finds whatever structure exists in the data.

**Example: Customer Segmentation**

A retail company has purchase history for 500,000 customers but no pre-assigned categories. A K-Means clustering algorithm groups customers into clusters based on spending patterns — high-frequency low-value buyers, occasional big spenders, seasonal shoppers, and so on. Marketing can then target each group differently.

**Common Unsupervised Algorithms:**

- K-Means Clustering
- Hierarchical Clustering
- Principal Component Analysis (PCA)
- Autoencoders

### Side-by-Side Comparison

| Feature | Supervised Learning | Unsupervised Learning |
| --- | --- | --- |
| Training data | Labeled | Unlabeled |
| Goal | Predict a known output | Discover hidden structure |
| Evaluation | Clear metrics (accuracy, F1) | Harder to evaluate |
| Example | Spam detection | Customer segmentation |
| Common algorithms | SVM, Neural Networks | K-Means, PCA |
| When to use | When labels are available | When labels do not exist |

**References:**

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning* (2nd ed.). Springer.

---

## Question 4: Overfitting — Causes and Prevention

### What Is Overfitting?

Overfitting happens when a model learns the training data too well — including its noise, random fluctuations, and outliers — and loses the ability to generalize to new data. The model memorizes rather than learns.

A classic analogy: a student who memorizes every past exam question word-for-word will fail the moment the exam uses slightly different phrasing. They did not understand the material; they just remembered specific examples.

### What Causes It?

**Too Complex a Model**

A model with too many parameters (e.g., a very deep decision tree or a large neural network) has enough capacity to memorize the training set rather than learning general patterns.

**Too Little Training Data**

When data is scarce, the model sees too few examples to understand the real underlying distribution. It fits to the few it sees.

**Too Many Training Epochs**

In iterative training (like neural networks), training for too long lets the model fit noise that should be ignored.

**Noisy or Mislabeled Data**

If labels are wrong or the data contains irrelevant features, the model may learn incorrect patterns.

### How to Prevent It

**1. Cross-Validation**

Instead of splitting data once into train/test, k-fold cross-validation splits data into k subsets and trains k models, each tested on a different fold. This gives a more reliable estimate of real-world performance.

**2. Regularization**

L1 (Lasso) and L2 (Ridge) regularization add a penalty term to the loss function that discourages overly large model weights. This limits complexity without reducing the model's architecture.

**3. Dropout (Neural Networks)**

During training, random neurons are deactivated at each step. This prevents co-adaptation and forces the network to learn redundant representations — making it more robust.

**4. Early Stopping**

Monitor performance on a validation set during training. When validation loss starts increasing even as training loss keeps decreasing, training is stopped. That divergence point marks where overfitting begins.

**5. More Data / Data Augmentation**

More training examples reduce overfitting. When real data is limited, augmentation techniques (e.g., rotating images, adding noise) artificially expand the dataset.

**6. Simpler Models**

Sometimes the fix is to use a less complex model. A logistic regression may outperform a neural network when the dataset is small.

**References:**

- Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.
- Srivastava, N., et al. (2014). Dropout: A Simple Way to Prevent Neural Networks from Overfitting. *Journal of Machine Learning Research*, 15, 1929–1958.

---

## Question 5: Train-Test Split — How and Why

### The Basic Idea

When building a machine learning model, you cannot evaluate it on the same data it was trained on. If you did, the model would look artificially good — it has already seen those examples. You need to test it on data it has never encountered, to simulate real-world performance.

The solution: split your dataset before training begins.

### How the Split Works

The most common approach is a simple random split. Typically:

- **70–80%** of the data goes into the training set
- **20–30%** goes into the test set

In many projects, a third split is added:

- **Training set** — used to train the model
- **Validation set** — used to tune hyperparameters and select the best model
- **Test set** — used only once, at the very end, to report final performance

A common ratio is 60/20/20 or 70/15/15.

### A Visual Breakdown

```
Full Dataset (100%)
│
├── Training Set (70%) ← Model learns from this
├── Validation Set (15%) ← Used to tune the model
└── Test Set (15%) ← Final evaluation only
```

The test set must remain completely untouched until the final evaluation. If you look at test results mid-project and adjust the model accordingly, your test set has effectively become a second validation set — and you no longer have an honest measure of generalization.

### Why This Matters

Without this split, you have no reliable way to know if your model will work in the real world. A model with 99% accuracy on training data and 60% accuracy on new data is not a good model — it overfits. The split reveals that.

For smaller datasets where even a 70/30 split leaves too little training data, k-fold cross-validation is used instead. It makes maximum use of available data while still providing honest performance estimates.

**References:**

- Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.
- James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning* (2nd ed.). Springer.

---

## Question 6: Case Study — ML in Healthcare

### Study: Deep Learning for Diabetic Retinopathy Detection

**Source:** Gulshan, V., et al. (2016). *Development and Validation of a Deep Learning Algorithm for Detection of Diabetic Retinopathy in Retinal Fundus Photographs*. JAMA, 316(22), 2402–2410.

### Background

Diabetic retinopathy (DR) is the leading cause of blindness in working-age adults worldwide. It is caused by damage to blood vessels in the retina, and it is detectable through fundus photography — but only if trained specialists review the images. In low-income and rural settings, there are simply not enough ophthalmologists to screen everyone.

Google's research team asked: can a deep learning model screen retinal images as reliably as a trained specialist?

### What They Did

The team trained a convolutional neural network (CNN) on 128,175 retinal fundus images, each graded by a panel of ophthalmologists. The model learned to detect signs of diabetic retinopathy across five severity levels — from no DR to proliferative DR (the most severe).

The model was then evaluated on two independent validation datasets totaling 12,522 images.

### Key Findings

| Metric | Model Performance | Specialist Benchmark |
| --- | --- | --- |
| Sensitivity (detecting DR) | 90.3% | 86.6% (median specialist) |
| Specificity (correctly ruling out DR) | 98.1% | 93.9% (median specialist) |
| AUC (Area Under Curve) | 0.991 | — |

The model matched or exceeded the performance of the majority of ophthalmologists in the study on both datasets.

### Which Part of the Data Science Lifecycle It Covers

| Lifecycle Stage | Covered in This Study? | How |
| --- | --- | --- |
| Problem Definition | Yes | Defined the clinical need for automated screening |
| Data Collection | Yes | 128,000+ graded retinal images |
| Data Cleaning | Yes | Multiple graders per image, adjudication panel for disagreements |
| EDA | Partially | Grade distributions reviewed before training |
| Modeling | Yes — core focus | CNN trained with deep learning |
| Evaluation | Yes | Two independent validation sets, sensitivity/specificity metrics |
| Deployment | Not in this paper | Subsequent Google Health work covers this |

This study covers all major lifecycle stages except deployment — which became the focus of later work, including clinical trials in Thailand and India.

### Why This Matters

This case study is significant not because AI is replacing doctors, but because it addresses a real access problem. A reliable automated screening tool means patients in rural areas without access to specialists can still be flagged early — when treatment is most effective.

**References:**

- Gulshan, V., Peng, L., Coram, M., Stumpe, M. C., Wu, D., Narayanaswamy, A., ... & Webster, D. R. (2016). Development and Validation of a Deep Learning Algorithm for Detection of Diabetic Retinopathy in Retinal Fundus Photographs. *JAMA*, 316(22), 2402–2410.
- Ting, D. S. W., et al. (2017). Development and Validation of a Deep Learning System for Diabetic Retinopathy and Related Eye Diseases. *JAMA*, 318(22), 2211–2223.

---

## Full Reference List

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Chapman, P., et al. (2000). *CRISP-DM 1.0: Step-by-step data mining guide*. SPSS Inc.
- Donoho, D. (2017). 50 Years of Data Science. *Journal of Computational and Graphical Statistics*, 26(4), 745–766.
- Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.
- Gomez-Uribe, C. A., & Hunt, N. (2015). The Netflix Recommender System. *ACM Transactions on Management Information Systems*, 6(4).
- Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.
- Gulshan, V., et al. (2016). Development and Validation of a Deep Learning Algorithm for Detection of Diabetic Retinopathy. *JAMA*, 316(22), 2402–2410.
- Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning* (2nd ed.). Springer.
- James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning* (2nd ed.). Springer.
- Mitchell, T. (1997). *Machine Learning*. McGraw-Hill.
- Rubin, D. B. (1976). Inference and Missing Data. *Biometrika*, 63(3), 581–592.
- Srivastava, N., et al. (2014). Dropout: A Simple Way to Prevent Neural Networks from Overfitting. *Journal of Machine Learning Research*, 15, 1929–1958.
- Ting, D. S. W., et al. (2017). Development and Validation of a Deep Learning System for Diabetic Retinopathy. *JAMA*, 318(22), 2211–2223.
