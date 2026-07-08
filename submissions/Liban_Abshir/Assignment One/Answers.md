# RESEARCH ASSIGNMENT

*Introduction to Data Science and Machine Learning*

Submitted: June 2026

---

# 1. Defining Data Science and Machine Learning

## 1.1 Data Science

Data Science is a multidisciplinary field built on the intersection of statistics, computer science, and domain knowledge. Its core purpose is to extract meaning from data — raw, often messy collections of numbers, text, and records — so that organizations and researchers can make better decisions. One widely cited academic definition describes it as the study of the generalizable extraction of knowledge from data (Dhar, 2013, as quoted in Maglaras et al., 2020). In practice this involves gathering data, cleaning it, exploring it visually and statistically, building models, and communicating results to stakeholders.

The scope of data science is deliberately wide. IBM describes it as a broad, multidisciplinary field that extracts value from today's massive data sets, encompassing data mining, statistics, analytics, data modeling, machine learning, and programming. In other words, data science is less a single technique than a full pipeline: the profession that manages data from its raw origin all the way to an actionable insight or automated system.

## 1.2 Machine Learning

Machine Learning (ML) is a branch of Artificial Intelligence that gives computer systems the ability to improve their performance through experience rather than through explicit instruction. Magnimind Academy describes it as a field where *statistical methods are used to empower machines to learn without being programmed explicitly,* allowing algorithms to collect insights and make predictions on data they have never seen before. ML algorithms detect patterns in training data and then generalize those patterns to produce outputs — predictions, classifications, or decisions — when presented with new inputs.

## 1.3 The Relationship Between Them

The cleanest way to frame the relationship is one of **inclusion**: Data Science is the broader discipline, and Machine Learning is one of its most powerful tools. VinUniversity's academic program documentation states it plainly — data science encompasses the preparation, analysis, modeling, and communication of results, while machine learning provides the algorithmic engine for the modeling step. Within data science's wider analysis process, machine learning provides the techniques and tools necessary for building algorithms or models that learn by extracting meaning from the data studied.

## 1.4 Real-Life Example: Credit-Card Fraud Detection

Consider how a bank handles potentially fraudulent transactions. The data science team first defines the business problem — catching fraud without blocking legitimate purchases — then collects years of transaction records, cleans the data, and engineers useful features such as transaction location, time of day, and merchant category. That structured, analytical work is pure data science.

Within this pipeline, they then apply a machine learning model — typically a gradient-boosted classifier — trained on labeled examples of fraudulent and legitimate transactions. The model learns to recognize subtle patterns and flags suspicious charges in real time. As Syracuse University's iSchool notes, data science provides the statistical foundation by structuring and analyzing financial records, while machine learning enhances the actual process of fraud detection by recognizing subtle patterns that might indicate suspicious behavior. Neither discipline alone would produce a working system; they are complementary.

---

# 2. The Data Science Lifecycle

There are several established frameworks for organizing a data science project. The most widely adopted is CRISP-DM (Cross-Industry Standard Process for Data Mining), developed in the 1990s. Flatiron School describes it as a flexible, six-phase lifecycle that guides data professionals from the initial problem to the final solution, adding that it is cyclical and iterative — teams move forward and backward between phases as they learn more. The five-stage academic model used below maps onto CRISP-DM closely.

## Stage 1: Problem Definition (Business Understanding)

Every data science project starts by articulating what success looks like. This means converting a vague organizational need into a precise, answerable question. For example, rather than "improve customer retention," a team would define: "Predict within 30 days which customers are likely to cancel their subscription, so that a retention campaign can be triggered." Without this clarity, even technically impressive models solve the wrong problem.

## Stage 2: Data Collection and Preparation

With the question defined, practitioners identify and gather the required data. Raw data is almost never ready for modeling: it may contain missing values, duplicate records, inconsistent formats, or irrelevant columns. This stage involves cleaning, transforming, and encoding the data into a form suitable for analysis. According to Gyansetu's industry guide, this stage is where teams often discover they need more data and must loop back to collection, illustrating CRISP-DM's inherently iterative nature.

## Stage 3: Exploratory Data Analysis (EDA)

Before building any model, analysts examine distributions, correlations, and anomalies through statistics and visualization. EDA reveals whether the data actually contains signal relevant to the defined problem. It often surfaces data quality issues invisible in Stage 2 and guides feature engineering — the process of constructing informative inputs for later models.

## Stage 4: Model Building and Evaluation — Where ML Fits

This is the stage at which Machine Learning enters the lifecycle. Once data has been collected, cleaned, and explored, practitioners select appropriate ML algorithms, train them on the prepared dataset, and evaluate performance against held-out data. The choice of algorithm depends on whether the problem is a classification, regression, or clustering task, and on the volume and nature of the data. Evaluation metrics such as accuracy, precision, recall, or AUC-ROC determine whether the model meets the standards set in Stage 1.

ML sits at this stage because it requires data to already be structured and informative. Applying an algorithm to raw, uncleaned data almost always produces unreliable results. The data science lifecycle ensures that by the time ML is invoked, the input is trustworthy and the success criteria are clearly defined.

## Stage 5: Deployment and Maintenance

A model that lives only in a notebook creates no real-world value. Deployment integrates the trained model into a business process or software system. As Enterprise Knowledge notes in their CRISP-DM analysis, this phase may involve integrating the model into existing systems, creating user interfaces, or automating workflows based on the model's predictions. Crucially, deployed models must be monitored over time: data distributions shift, business conditions change, and models can degrade in performance — a phenomenon called model drift — requiring periodic retraining.

---

# 3. Supervised vs. Unsupervised Learning

Machine learning algorithms are broadly categorized by the type of data they learn from. The two foundational categories are supervised learning and unsupervised learning. Understanding the distinction is essential because the choice between them is determined by the data available and the question being asked.

## 3.1 Supervised Learning

In supervised learning, the algorithm is trained on a **labeled dataset** — one in which each input example comes paired with the correct answer. The algorithm learns a mapping from inputs to outputs by minimizing the error between its predictions and the known labels. IBM describes supervised learning models as ideal for spam detection, sentiment analysis, weather forecasting, and pricing predictions. Supervised learning tasks are further divided into *classification* (predicting a category) and *regression* (predicting a continuous value).

**Example — Email Spam Detection:** An email provider trains a classifier on millions of messages already labeled "spam" or "not spam" by human reviewers or rule-based filters. The model learns features — unusual sender domains, certain keyword patterns, excessive links — that correlate with spam, and applies that learned rule to classify new incoming messages.

## 3.2 Unsupervised Learning

Unsupervised learning operates on **unlabeled data**. There is no pre-defined correct answer; instead, the algorithm discovers structure inherent in the data itself. Typical tasks include *clustering* (grouping similar observations) and *dimensionality reduction* (finding compact representations of data). IBM notes that unsupervised learning is a great fit for anomaly detection, recommendation engines, customer personas, and medical imaging.

**Example — Customer Segmentation:** A retail company has purchase histories for hundreds of thousands of customers but has not labeled them in any way. Using K-Means clustering, the model groups customers into segments based on shared patterns in their purchase frequency, average spend, and product categories — without any human pre-defining what those segments should look like. These segments can then drive targeted marketing campaigns.

## 3.3 Comparison Table

| **Dimension** | **Supervised Learning** | **Unsupervised Learning** |
|---|---|---|
| **Data Type** | Labeled (input + correct output) | Unlabeled (input only) |
| **Goal** | Predict a known target variable | Discover hidden patterns/groups |
| **Output** | Classification or regression result | Clusters, associations, or reduced features |
| **Example Algorithm** | Random Forest, SVM, Logistic Regression | K-Means Clustering, PCA |
| **Typical Use Case** | Spam detection, disease diagnosis | Customer segmentation, anomaly detection |
| **Human Effort Required** | High — labels must be provided | Lower — no labeling required |

---

# 4. Overfitting: Causes and Prevention

## 4.1 What Is Overfitting?

Overfitting occurs when a machine learning model learns the training data so thoroughly — including its noise and irrelevant quirks — that it loses the ability to generalize to new, unseen data. Analytically, it manifests as a large gap between training accuracy and test/validation accuracy: the model performs excellently on data it has seen but poorly on data it has not. Lyzr's ML glossary states that overfitting arises when a model prioritizes memorizing the training data over learning its underlying structure.

## 4.2 Causes of Overfitting

Four primary causes have been identified in the machine learning literature:

- **Model Complexity:** A model with too many parameters relative to the amount of training data can fit the training examples exactly, including their noise. Deep neural networks are particularly vulnerable when applied to small datasets.

- **Insufficient Training Data:** The smaller the dataset, the easier it is for a model to memorize it. A classifier trained on fifty labeled examples will almost always overfit.

- **Over-Training (Too Many Epochs):** Training for too many iterations gives the model excessive opportunity to memorize. As Lightly.ai notes, training for too many epochs makes the model memorize noise instead of learning underlying patterns.

- **Absence of Regularization:** Without constraints on parameter magnitudes or model complexity, algorithms are free to grow arbitrarily complex to fit every data point.

## 4.3 Prevention Strategies

Several well-established techniques address overfitting, often used in combination:

**Regularization:** Regularization introduces a penalty into the model's loss function to discourage large or numerous parameters. L1 regularization (Lasso) can drive irrelevant feature weights to exactly zero, effectively performing feature selection. L2 regularization (Ridge) shrinks all weights toward zero, preventing extreme values.

**Cross-Validation:** Rather than evaluating the model on a single test set, k-fold cross-validation partitions the data into k subsets and trains k separate models, each tested on a different held-out fold. This gives a more reliable estimate of how the model will behave on truly new data.

**Dropout (for Neural Networks):** During training, dropout randomly deactivates a fraction of neurons in each forward pass. This prevents individual neurons from co-adapting too closely to specific training examples and forces the network to learn distributed, redundant representations.

**Early Stopping:** Training is halted when the model's performance on a separate validation set stops improving, even if training-set performance continues to rise. This prevents the model from entering the memorization phase.

**More Data and Data Augmentation:** Fundamentally, overfitting is harder when a model has more diverse examples to learn from. In computer vision, artificial augmentation techniques (flipping, rotating, cropping images) effectively expand the training set.

---

# 5. Training Data and Test Data: The Split and Its Necessity

## 5.1 The Concept

When building a machine learning model, the available labeled data is divided into at least two non-overlapping subsets: a training set and a test set. The model is trained exclusively on the training set — it adjusts its internal parameters based on these examples alone. The test set, containing examples the model has never encountered, is then used to evaluate how well the model generalizes. Many projects also introduce a third subset, the validation set, used during training to tune hyperparameters without touching the final test set.

A three-set summary:

- **Training Set:** The data the model learns from. It is the largest portion, typically 60–80% of available data.
- **Validation Set:** Used to monitor performance during training and tune settings (hyperparameters) without biasing the final evaluation. Typically 10–20%.
- **Test Set:** Reserved entirely for the final, unbiased performance evaluation. Never used during training or hyperparameter tuning. Typically 10–20%.

## 5.2 Why the Split Is Necessary

The fundamental motivation is to obtain an honest estimate of real-world performance. If a model were evaluated on the same data it was trained on, the result would be deeply misleading: a model that has memorized training examples will score near 100% on them regardless of whether it has learned anything useful. Tpoint Tech notes that the main purpose of the training data is to help understand and comprehend the assumptions of the model, while the test data is used to evaluate the efficiency and performance of the model. Without this separation, there is no way to detect overfitting before deployment.

The principle is analogous to studying for an exam. A student who only re-reads the exact questions from last year's exam may score well on a repetition of those same questions but fail any novel question. A properly held-out test set is the novel question — it reveals whether genuine learning occurred.

## 5.3 Common Split Ratios

The 80/20 split (80% training, 20% testing) is the most widely adopted convention in practice. This ratio is loosely driven by the Pareto principle (also called the 80–20 rule), which states that 80% of the effect is driven by 20% of causes. In practice, the optimal split varies: very large datasets can afford 99/1 splits because even 1% yields a statistically robust test set, while small datasets may require cross-validation instead of a single split. The 80/20 convention dominates contemporary practice and is validated by empirical research showing it produces optimal prediction performance across most model types.

## 5.4 Key Principle: Avoiding Data Leakage

A critical practical rule is that no information from the test set must ever influence model training or feature engineering. When preprocessing steps such as normalization or imputation are applied to the entire dataset before splitting, information from the test set "leaks" into the training process, producing an overly optimistic and ultimately dishonest performance estimate. The correct procedure is to fit all preprocessing transformers on the training set alone and then apply them to the test set.

---

# 6. Case Study: Machine Learning for Cardiovascular Disease Prediction

## 6.1 Source

Kahraman, A. et al. (2025). "Machine learning techniques for improved prediction of cardiovascular diseases using integrated healthcare data." *Frontiers in Artificial Intelligence*, Vol. 8, DOI: 10.3389/frai.2025.1694450.

## 6.2 Background and Motivation

Cardiovascular disease (CVD) remains one of the leading causes of mortality worldwide. Traditional diagnostic approaches, such as coronary angiography, are expensive, invasive, and not universally accessible. This study, published in *Frontiers in Artificial Intelligence* in 2025, investigates whether integrating multiple publicly available healthcare datasets and applying a range of supervised ML classifiers can produce a more robust and accurate CVD prediction tool than models trained on a single, limited dataset.

## 6.3 Data and Methodology

The research team collected clinical records from multiple public health databases. After merging the datasets on shared clinical features and applying data preprocessing steps — cleaning, alignment of features, and removal of missing values — the final dataset comprised 311,710 patient samples, making it one of the largest CVD datasets used in a published academic study. Features included standard clinical parameters such as blood pressure readings, blood glucose levels, cholesterol measurements, age, and body mass index.

Several ML algorithms were implemented and compared, including logistic regression as a baseline, support vector machines, Random Forest, XGBoost, and CatBoost. Each model was trained on a portion of the dataset and evaluated on a held-out test set using standard metrics including AUC-ROC, accuracy, precision, and recall.

## 6.4 Findings

The CatBoost gradient-boosting model achieved the highest performance, reaching an Area Under the Curve (AUC) of 94.1% — a strong result indicating that the model correctly distinguishes between patients with and without CVD in 94 out of 100 cases on average. The study also demonstrated that integrating multiple datasets produced models meaningfully more accurate than those trained on any single source, suggesting that data integration itself, as a data science practice, yields significant clinical value. The authors concluded that machine learning decision-support systems using routinely collected clinical parameters represent a viable and cost-effective complement to traditional CVD diagnostics.

## 6.5 Lifecycle Stages Covered

This case study spans the full data science lifecycle and is therefore particularly instructive:

- **Problem Definition:** The clinical problem is clearly stated — develop a reliable, non-invasive alternative to angiography for CVD risk prediction.
- **Data Collection and Preparation:** Multiple public health datasets are merged and preprocessed, addressing missing values and feature misalignment.
- **Exploratory Analysis:** Clinical features are analyzed and selected for model input.
- **Model Building and Evaluation (Machine Learning):** Multiple ML classifiers are trained and compared using AUC-ROC and other metrics; CatBoost is identified as the best-performing model.
- **Deployment Potential:** The authors explicitly position the model as a clinical decision-support tool, pointing toward deployment in hospital information systems.

The study demonstrates how data science and machine learning, when combined with high-quality integrated data, can address real, high-stakes problems in healthcare — moving from raw clinical records to a deployable predictive system with measurable accuracy.

---

# References

Dhar, V. (2013). Data science and prediction. *Communications of the ACM*, 56(12), 64–73. [Cited in: Maglaras et al., 2020, arXiv:2001.04561]

IBM. (2025, November). Data science vs. machine learning: What's the difference? *IBM Think*. https://www.ibm.com/think/topics/data-science-vs-machine-learning

IBM. (2026, May). Supervised vs. unsupervised learning: What's the difference? *IBM Think*. https://www.ibm.com/think/topics/supervised-vs-unsupervised-learning

Kahraman, A. et al. (2025). Machine learning techniques for improved prediction of cardiovascular diseases using integrated healthcare data. *Frontiers in Artificial Intelligence*, 8. https://doi.org/10.3389/frai.2025.1694450

Magnimind Academy. (2026). Connection between data science, machine learning (ML), and artificial intelligence (AI). https://magnimindacademy.com/blog/connection-between-data-science-machine-learning-ml-and-artificial-intelligence-ai/

Maglaras, L. et al. (2020). A survey on machine learning-based performance improvement of wireless networks: PHY, MAC and network layer. arXiv:2001.04561.

Pangeanic. (2023, June). The relationship between data science and machine learning. https://blog.pangeanic.com/trelationship-between-data-science-and-machine-learning

VinUniversity. (2026, January). Machine learning vs data science: Scope and skillsets. https://vinuni.edu.vn/data-science-vs-machine-learning/

Flatiron School. (2026, January). Intro to data science: Understanding CRISP-DM. https://flatironschool.com/blog/intro-to-data-science-understanding-crisp-dm/

Gyansetu. (2026, June). Data science life cycle: 8 phases, tools & real examples. https://www.gyansetu.in/data-science/data-science-life-cycle/

Enterprise Knowledge. (2025, May). Understanding the role of knowledge intelligence in the CRISP-DM framework. https://enterprise-knowledge.com/understanding-the-role-of-knowledge-intelligence-in-the-crisp-dm-framework-a-guide-for-data-science-projects/

Built In. (2024). Supervised vs. unsupervised learning. https://builtin.com/artificial-intelligence/supervised-vs-unsupervised-learning

Lyzr. (2026, March). Overfitting. https://www.lyzr.ai/glossaries/overfitting/

Lightly.ai. (2024). Overfitting in machine learning: Causes, detection, and prevention. https://www.lightly.ai/blog/overfitting

GeeksforGeeks. (2025, November). Overfitting and regularization in ML. https://www.geeksforgeeks.org/machine-learning/overfitting-and-regularization-in-ml/

EliteDataScience. (2022, July). Overfitting in machine learning: What it is and how to prevent it. https://elitedatascience.com/overfitting-in-machine-learning

Ahmed, N. (2023, March). The motivation for train-test split. *Medium*. https://medium.com/@nahmed3536/the-motivation-for-train-test-split-2b1837f596c3

Tpoint Tech. (2026, April). Why we use an 80-20 split for training and test data. https://www.tpointtech.com/why-we-use-an-80-20-split-for-training-and-test-data

Baeldung. (2025, February). Splitting a dataset into train and test sets. https://www.baeldung.com/cs/train-test-datasets-ratio

Lightly.ai. (2024). Train test validation split: Best practices & examples. https://www.lightly.ai/blog/train-test-validation-split

Syracuse University iSchool. (2025, April). Data science vs. machine learning: Key differences explained. https://ischool.syracuse.edu/data-science-vs-machine-learning/
