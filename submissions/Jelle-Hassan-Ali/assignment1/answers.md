  Executive Summary. Data science (DS) is an interdisciplinary field that applies scientific methods and tools
to extract knowledge and insights from raw data【8†L365-L368】. Machine learning (ML) is a subfield of DS
(and of AI) focused on designing algorithms that learn patterns from data to make predictions or decisions
without explicit programming.

 In practice, data scientists define business problems,
collect/clean data, analyze it, and then use ML models in the modeling phase

 For example, in healthcare data science, patient records might be cleaned and explored by a data
scientist, and then an ML model (e.g. a neural net) is trained to predict disease risk.

 The DS lifecycle typically flows from problem definition through data acquisition, preprocessing, modeling,
evaluation, and finally deployment.

A key difference is
that in supervised learning the data includes explicit labels (targets) and models learn to predict those
labels,  whereas unsupervised learning works on unlabeled data to uncover hidden
structure (e.g. clustering).

 Overfitting occurs when a model is too complex (high variance)
and fits training data noise, leading to poor generalization.
 it can be diagnosed by a large
gap between training and test performance or rising validation loss

Finally, data is split into training and test sets
(often with a stratified 70/30 or 80/20 split) so that cross-validation can estimate generalization
performance

Case Study – Predicting Heart Disease (Healthcare): We examine a recent peer-reviewed study (El-Sofany et al., 2024) that built ML models to predict heart disease from patient data. The study collected a clinical dataset, performed data preprocessing (feature selection, SMOTE for imbalance), trained multiple ML classifiers (SVM, Random Forest, XGBoost, etc.), and evaluated performance via cross-validation. The best model (XGBoost with selected features) achieved ~97.6% accuracy. The paper covers the lifecycle stages from problem definition through deployment (they even built a mobile app). Limitations include “dark data” (unseen asymptomatic cases) and the need for explainability (they used SHAP), which are discussed as future work.



        1: Definitions and Relationship

Data Science: A multidisciplinary field combining statistics, computation, and domain expertise to extract
knowledge from data. 
It encompasses the entire pipeline from defining a question to
collecting, cleaning, analyzing data, and communicating insights. Data science uses techniques from
statistics, databases, and ML to inform decision-making (e.g. predictive analytics, pattern discovery).

Machine Learning: A subset of artificial intelligence and data science. ML focuses on building models that 
learn from data. An ML algorithm is exposed to training data and “learns” patterns so it can make
predictions on new data without being explicitly programmed. The IBM definition
highlights ML as “algorithms that can learn the patterns of training data and, subsequently, make accurate
inferences about new data”. In other words, ML automates data analysis: “it can be
understood as a collection of algorithms and techniques to automate data analysis”.

Relationship: Data science is the broader process; ML is one of its tools. Data science provides the context,
data infrastructure, and analytical methods (e.g. data engineering, EDA, visualization), while ML provides
predictive models. For example, a recommender system (like Netflix or Spotify) uses DS to aggregate and
preprocess user behavior data, and ML to train a model that predicts user preferences.

           2: Data Science Lifecycle and ML Integration

The DS lifecycle typically flows from problem definition through data acquisition, preprocessing, modeling,
evaluation, and finally deployment.

The data science lifecycle is a structured workflow that begins with a clearly defined problem and ends
with a deployed solution. A widely used framework (often called CRISP-DM or OSEMN) involves these stages

 
Business Understanding (Problem Definition): Define goals and success criteria by consulting
stakeholders.

Data Acquisition (Obtain Data): Collect relevant data from databases, APIs, logs, etc. (this may
include new data collection or querying existing sources).

   Data Preparation (Scrub/Clean Data): Handle missing values, correct errors, normalize formats,
remove outliers. This may involve merging datasets and deriving new features.

   Exploratory Data Analysis (EDA): Use visualization and summary statistics to understand data
distributions and relationships. Identify key variables.

   Feature Engineering: Transform or create new features from raw data to help modeling.

   Modeling (ML Training): Apply machine learning algorithms to the prepared data. Here ML
methods (classification, regression, clustering, etc.) are used. For example, one chooses a model
(say, a regression or tree ensemble) and trains it on historical data.

   Evaluation: Assess model performance on a hold-out test set using metrics like accuracy, RMSE, F1
score, etc. Ensure the model meets business requirements.

   Deployment: Integrate the model into production (e.g. via an API or embedded in software). Then
continuously monitor its performance on new data and update as needed.


Importantly, ML typically enters during “Modeling.” After the data is cleaned and features are ready, ML
algorithms learn from the data. Data science provides the necessary preparation and interpretation; ML
provides the predictive engine. Finally, results from ML (e.g. predicted values, clusters) must be interpreted
and communicated back to stakeholders as actionable insights.


         3: Supervised vs. Unsupervised Learning

Machine learning is categorized by how it learns from data:

  Supervised Learning (SL): The training data include labels (target values). The goal is to learn a
function mapping inputs to outputs (regression for numeric targets, classification for categories).
 For example, a supervised model might predict house prices (a regression task)

from features like size and location, or classify images as “spam” vs. “not spam”.
Because labels are available, SL models can be evaluated directly by comparing predictions to true values.

  Unsupervised Learning (UL): The data have no labels. The goal is to discover hidden structure or
patterns. Common tasks include clustering (grouping similar examples) and dimensionality
reduction. For instance, customer segmentation groups customers into clusters by purchasing
behavior. Without labels, UL models are evaluated by measures of cohesion/
separation or downstream utility.


        4: Overfitting: Causes, Diagnosis, and Prevention

Overfitting occurs when a model learns the noise or idiosyncrasies in the training set rather than the
underlying general patterns. An overfit model has low training error but high test/validation error.

 In effect, the model “memorizes” the training data (like rote learning), so it fails to
generalize to new data. This is often due to excessive model complexity: for example, deep
neural networks with many layers or decision trees grown to full depth are so flexible that they can fit noise.


The bias–variance tradeoff underlies overfitting. High-variance (low-bias) models fit training data very
closely, leading to overfitting, whereas high-bias (low-variance) models are too simple and underfit. 

For instance, using a simple linear model on highly nonlinear data yields underfitting, while
a high-degree polynomial can overfit. High-dimensional datasets (many features) exacerbate this “curse of dimensionality”: as features increase, data become sparse and variance rises

Prevention: Common strategies to prevent overfitting include:

  Regularization:
  Cross-Validation:
  Pruning (for trees):
  Early Stopping:
  Data Augmentation:
  Feature Selection/Dimensionality Reduction:


      4: Train/Test Splits and Cross-Validation

Proper evaluation of ML models requires splitting data into separate subsets. A common approach is to
hold out a test set (e.g. 20–30% of the data) and train the model on the training set. This simulates how
the model will perform on new, unseen data. Scikit-learn provides 
train_test_split to do this randomly.

for example: 
from sklearn.model_selection import train_test_split
# Split 80% train, 20% test, preserving class ratios
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, stratify=y, random_state=42
):


     6. Case Study: Predicting Heart Disease (Healthcare)

Reference: El‐Sofany et al. (2024), “A proposed technique for predicting heart disease using machine learning algorithms and an explainable AI method”, Scientific Reports, vol. 14, Article 23277. (Open access: DOI 10.1038/s41598-024-74656-2.)

Objectives: This study aimed to develop an accurate machine learning model to predict early-stage heart disease (HD) risk from patient data. Accurate prediction enables timely intervention and could reduce mortality. The authors sought to compare multiple ML methods and feature selection strategies to identify the best approach. They also incorporated explainability (using SHAP) to interpret predictions.

Data: They used a combination of clinical datasets: a publicly available heart disease dataset and a private medical dataset. Features included patient symptoms, demographics, and test results. The data were imbalanced (fewer positive cases), so the Synthetic Minority Oversampling Technique (SMOTE) was applied to generate a balanced training set. The final feature set (“SF-2”) was chosen via statistical tests (chi-square, ANOVA, mutual information) to select the most relevant predictors.

Methods: The study systematically applied ten ML classifiers (Naive Bayes, SVM, voting ensemble, XGBoost, AdaBoost, bagging, decision trees, KNN, random forest, logistic regression) to the selected feature subsets. They used cross-validation extensively: multiple train/test splits ensured robust evaluation. The best-performing model was XGBoost trained on the SF-2 feature set. The authors built an explainable AI pipeline: after training, they applied SHAP (SHapley Additive exPlanations) to interpret which features most influenced the model’s output.

Results: The XGBoost model on the SF-2 features achieved 97.64% accuracy, with 96.61% sensitivity and 98% AUC. (These high metrics indicate excellent discrimination between patients with and without heart disease.) The SHAP analysis identified which clinical features were most predictive (not detailed in the source excerpt). The model outperformed simpler algorithms; ensemble methods and boosting were particularly effective in this dataset.

Limitations: The authors discuss a key limitation: “dark data”—unrecorded or asymptomatic cases. Because the model was trained on symptomatic individuals, it may underperform for patients without clear symptoms. They also note the risk of over-relying on symptom-based input, suggesting future integration of demographic or test data. Finally, they acknowledge that machine learning can be a “black box,” so they included SHAP for interpretability, but further transparency (PDPs, ICE plots, LIME) is needed in future work.

Lifecycle Mapping:

Problem Definition: Early prediction of heart disease to aid clinicians (motivated by global health statistics).
Data Collection: Patient medical records and diagnostic data were gathered (private and public sources).
Data Preparation: The data were preprocessed: relevant features selected (ANOVA, chi-square), class imbalance handled with SMOTE.
Exploratory Analysis: (Implied) Feature analysis likely guided selection (though details aren’t provided, it’s standard practice).
Modeling: Multiple ML algorithms were trained on the processed data. XGBoost was identified as optimal.
Evaluation: They used k-fold cross-validation and held-out test sets to measure accuracy, sensitivity, etc. Consistently high test scores confirmed generalizability.
Deployment: The study mentions developing a mobile app using the XGBoost model to predict heart disease from user-input symptoms, indicating a deployment stage.
This case demonstrates the full Data Science workflow. It shows how healthcare data is transformed via statistical preprocessing and ML to produce a predictive tool. The study’s reporting (features, models, metrics) provides transparency for each lifecycle stage. For example, the authors explicitly note defining features (data cleaning/feature engineering) and methods (modeling), and even address deployment (mobile app). The limitations section highlights ongoing lifecycle concerns (data quality and ethical deployment).

Summary: The paper exemplifies how data science and ML collaborate to solve a real healthcare problem. It covers problem formulation, extensive data preprocessing, rigorous modeling and validation, and progress toward deployment, illustrating the entire lifecycle and the synergy of data science and machine learning.

References

El‐Sofany, H., Bouallegue, B., & Abd El-Latif, Y. M. (2024). A proposed technique for predicting heart disease using machine learning algorithms and an explainable AI method. Scientific Reports, 14, 23277. https://doi.org/10.1038/s41598-024-74656-2
Subrahmanya, S. V. G., Shetty, D. K., Patil, V., Hameed, B. M. Z., Paul, R., Smriti, K., Naik, N., & Somani, B. K. (2022). The role of data science in healthcare advancements: applications, benefits, and future prospects. Irish Journal of Medical Science, 191(4), 1473–1483. https://doi.org/10.1007/s11845-021-02730-z
Bergmann, D. (2024). What is machine learning? IBM. https://www.ibm.com/think/topics/machine-learning
IBM. (n.d.). Supervised vs. unsupervised learning: What’s the difference? IBM. https://www.ibm.com/think/topics/supervised-vs-unsupervised-learning
IBM. (n.d.). What is overfitting? IBM. https://www.ibm.com/think/topics/overfitting
Scikit-learn. (2025). 3.1. Cross-validation: evaluating estimator performance. https://scikit-learn.org/stable/modules/cross_validation.html


