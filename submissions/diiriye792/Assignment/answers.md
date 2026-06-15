Introduction to Data Science
and Machine Learning

A Research Assignment

Submitted: June 14, 2026   |   Due: June 15, 2026 — 12:00 PM EAT





1. DEFINING DATA SCIENCE AND MACHINE LEARNING
1.1 Data Science
Data Science is a multidisciplinary field that combines statistical analysis, software engineering, data engineering, and domain knowledge to extract meaningful insights from large volumes of data.
In other words, data science is not a single technique but rather a full process — from asking the right question, gathering raw data, cleaning and transforming it, analyzing patterns, building predictive models, and finally communicating results to decision-makers. It draws from mathematics, computer science, and domain expertise simultaneously.
1.2 Machine Learning
Machine Learning (ML) is a sub-field of Artificial Intelligence (AI) and a key component of data science. Tom Mitchell's widely cited formal definition states:
“A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E.”
Put simply, ML is the mechanism by which computers learn patterns from data without being explicitly programmed for every outcome. The more data the system is exposed to, the better its predictions become — analogous to how a child gradually learns to recognize objects through repeated exposure.
1.3 Their Relationship
The relationship is hierarchical: Machine Learning sits inside Data Science. Data Science provides the full analytical process (problem framing, data collection, cleaning, visualization, communication), while ML provides the algorithmic engine that automates prediction and pattern discovery within that process.


Dimension	Data Science	Machine Learning
Scope	Broad — full data lifecycle	Narrow — algorithm training
Goal	Derive business insights from data	Build models that learn from data
Tools	Python, SQL, Tableau, Spark	scikit-learn, TensorFlow, PyTorch
Output	Reports, dashboards, models	Trained predictive model
Relationship	Parent discipline	Tool/sub-field within DS


1.4 Real-Life Example: Student Academic Performance Prediction
Consider a university that wants to identify students who are at risk of failing a course.
•	Statistics/Data Science defines the problem ("Which students are likely to fail the final examination?"), collects student records, cleans the dataset, and explores important variables such as attendance rate, assignment scores, study hours, and previous GPA. Statistical methods are used to summarize the data, identify trends, and examine relationships among variables. 
•	Machine Learning then trains a classification model (e.g., Logistic Regression, Random Forest, or XGBoost) using historical student data to predict whether a student is likely to pass or fail. 
•	Statistics/Data Science again takes over for model evaluation and interpretation. Performance metrics such as accuracy, precision, recall, and ROC-AUC are assessed. The results are then communicated to university administrators and instructors, allowing them to provide targeted academic support to at-risk students.
2. THE DATA SCIENCE LIFECYCLE
The most widely adopted framework for structuring data science work is CRISP-DM (Cross-Industry Standard Process for Data Mining), developed in 1999 and still considered the gold standard across industries. It defines a set of interconnected, iterative phases rather than a rigid linear sequence — teams frequently cycle back to earlier stages as new findings emerge.
#	Phase	Key Activities	Machine Learning Role?
1	Business Understanding	Define the problem, success criteria, project goals, and constraints in business terms.	No
2	Data Understanding	Collect raw data, explore its structure, identify data quality issues, and discover initial patterns.	No
3	Data Preparation	Clean, transform, integrate, and format data for modelling. Feature engineering is performed here.	Partial
4	Modelling	Select algorithms, train models on prepared data, and tune hyperparameters to optimize performance.	YES — Primary ML stage
5	Evaluation	Assess model performance against business objectives. Decide whether to deploy or iterate.	YES — Model assessment
6	Deployment	Integrate the model into production, monitor its performance on live data, and manage retraining cycles.	YES — Ongoing monitoring


Machine Learning fits most prominently into Phase 4 (Modelling) and Phase 5 (Evaluation). However, it increasingly influences Phase 3 (feature engineering using automated feature selectors) and Phase 6 (automated retraining pipelines via MLOps). The lifecycle is explicitly described as iterative — for instance, poor model performance in Phase 5 will send the team back to Phase 3 to revisit feature engineering, or even back to Phase 1 if the original problem definition proves inadequate.
3. SUPERVISED VS. UNSUPERVISED LEARNING
3.1 Supervised Learning
Supervised learning trains a model on labelled data — a dataset where each input is already paired with the correct output. The algorithm learns to map inputs to outputs by iteratively adjusting its internal parameters to minimize prediction error. Because the ‘answers’ are provided during training, the model can measure its own accuracy and improve.
Algorithms: Linear Regression, Logistic Regression, Decision Trees, Support Vector Machines (SVM), Random Forests, and Neural Networks.
Example: An email spam filter trained on thousands of emails already labelled ‘spam’ or ‘not spam’. The model learns which word patterns predict spam, and then classifies new emails automatically.
3.2 Unsupervised Learning
Unsupervised learning trains on unlabelled data. There are no pre-assigned correct answers. Instead, the algorithm discovers hidden patterns, groupings, or structures on its own. Success is harder to measure because there is no ground truth to compare against.
Algorithms: K-Means Clustering, DBSCAN, Principal Component Analysis (PCA), Autoencoders, and Hierarchical Clustering.
Example: A bank segments its customers into distinct groups based on spending behaviour, demographics, and transaction frequency — without knowing in advance what those groups should be. The algorithm discovers that, for instance, ‘high-income frequent travellers’ form a natural cluster.
3.3 Comparison Table
Criterion	Supervised Learning	Unsupervised Learning
Data	Requires labelled data (input + output pairs)	Works on unlabeled raw data
Goal	Predict a specific outcome or classify inputs	Discover hidden patterns or groupings
Evaluation	Straightforward — compare predictions to labels	Subjective — no ground truth to compare
Risk	Overfitting to training labels; needs quality labels	May discover spurious or irrelevant patterns
Typical Use	Email spam detection, disease diagnosis, price prediction	Customer segmentation, anomaly detection, dimensionality reduction


OVERFITTING: CAUSES AND PREVENTION
4.1 What is Overfitting?
Overfitting happens when a machine learning model learns the training data too well, including random errors and noise. Instead of learning general patterns, the model memorizes the training data. 
As a result, it performs very well on the training data but poorly on new, unseen data.

The opposite problem is underfitting, which occurs when a model is too simple to learn the important patterns in the data. In this case, the model performs poorly on both training and test data.

Overfitting and underfitting are related to the bias-variance tradeoff, which means finding the right balance between a model that is too simple and one that is too complex.

4.2 Main Causes of Overfitting
Complex Models: Models with many parameters (such as deep neural networks or large decision trees) can easily memorize the training data.
Small Training Dataset: When there is not enough data, the model may learn random patterns that do not represent the real population.
Training for Too Long: If a model is trained for too many iterations or epochs, it may start learning noise instead of useful patterns.
Irrelevant Features: Including unnecessary or noisy variables can confuse the model and increase overfitting.
No Regularization: Without techniques that control model complexity, the model may fit the training data too closely.
4.3 Methods to Prevent Overfitting
Regularization: Adds a penalty to large model weights, helping keep the model simple and reducing overfitting.
Dropout: In neural networks, randomly removes some neurons during training so the model learns more general patterns.
Early Stopping: Stops training when performance on validation data no longer improves.
Cross-Validation: Splits the dataset into several parts and tests the model multiple times to obtain a more reliable estimate of performance.
Data Augmentation: Creates additional training examples by modifying existing data, making the dataset larger and more diverse.
Feature Selection or Pruning: Removes unnecessary features or branches, reducing model complexity and improving generalization.

NOTE
Overfitting: Excellent performance on training data, poor performance on new data.
Underfitting: Poor performance on both training and new data.
Good Fit: Good performance on both training and new data.

5. Train-Test Split: Purpose and Process


6.1 Source
Adhiya, J., Barghi, B., & Azadeh-Fard, N. (2024). Predicting the risk of hospital readmissions using a machine learning approach: a case study on patients undergoing skin procedures. Frontiers in Artificial Intelligence, 6, 1213378. DOI: 10.3389/frai.2023.1213378
6.2 Context and Problem
Hospital readmissions — patients returning to hospital within 30 days of discharge — impose substantial financial costs on healthcare systems and inflict measurable psychological burden on patients. Despite advances in medical care, this problem persists across specialties. The study focused on a previously underexplored group: patients who underwent dermatological (skin) procedures. Two questions drove the research: (1) What patient-level factors most strongly predict readmission risk in this population? (2) Which machine learning algorithms achieve the highest predictive accuracy for this task?
6.3 Methods
The researchers applied seven ML classification algorithms to electronic health records data from dermatology patients: Logistic Regression (LR), Support Vector Machine (SVM), Random Forest (RF), Naive Bayes (NB), Artificial Neural Network (ANN), XGBoost (XG), and K-Nearest Neighbor (KNN). Patient features included demographic variables, diagnosis codes, procedure type, physician characteristics, and temporal variables (month of procedure). The target variable was binary: readmitted within 30 days, or not.
6.4 Key Findings
•	XGBoost (XG) and Random Forest (RF) outperformed all other algorithms in prediction accuracy — both are ensemble methods that combine multiple decision trees and are well-suited to tabular healthcare data.
•	Approximately 6% of patients were readmitted within one month of their initial skin procedure.
•	Male patients and patients aged 21–40 showed higher readmission propensity — a counterintuitive finding given that older age typically predicts worse outcomes in other specialties.
•	Readmission rates spiked in March and April, suggesting a seasonal dimension (potentially related to post-winter illness patterns or staffing cycles) that deserves further investigation.
•	Physician gender was also identified as a significant factor: patients treated by female physicians showed lower 30-day readmission rates, consistent with prior literature on surgical outcomes.
6.5 CRISP-DM Lifecycle Stages Covered
This study spans Phases 1 through 5 of the CRISP-DM lifecycle:
•	Phase 1 (Business Understanding): Defined clinically and financially relevant problem — predicting which patients will be readmitted.
•	Phase 2 (Data Understanding): Explored electronic health records, identifying relevant patient features and the class imbalance in readmission outcomes.
•	Phase 3 (Data Preparation): Cleaned and transformed clinical data, encoded categorical variables, handled missing values, and engineered features.
•	Phase 4 (Modelling): Trained and compared seven ML classification algorithms.
•	Phase 5 (Evaluation): Compared algorithm performance, identified XGBoost and RF as best-performing, and linked findings back to clinical significance.
Phase 6 (Deployment) was not covered — the study did not integrate models into live hospital systems, which represents a gap and a direction for future work.
References
Adhiya, J., Barghi, B., & Azadeh-Fard, N. (2024). Predicting the risk of hospital readmissions using a machine learning approach: a case study on patients undergoing skin procedures. Frontiers in Artificial Intelligence, 6, 1213378. https://doi.org/10.3389/frai.2023.1213378
Flatiron School. (2026, January 15). Intro to Data Science: Understanding CRISP-DM. https://flatironschool.com/blog/intro-to-data-science-understanding-crisp-dm/
Hex. (2026, March 9). What is overfitting? Causes, detection & prevention. https://hex.tech/blog/what-is-overfitting/
IBM. (2025). Supervised vs. Unsupervised Learning: What's the Difference? IBM Think. https://www.ibm.com/think/topics/supervised-vs-unsupervised-learning
Lightly. (n.d.). Supervised vs Unsupervised Learning: A Comparison. https://www.lightly.ai/blog/supervised-vs-unsupervised-learning
Lightly. (n.d.). Train Test Validation Split: Best Practices & Examples. https://www.lightly.ai/blog/train-test-validation-split
Mitchell, T. M. (1997). Machine Learning. McGraw-Hill.
Pangeanic. (2023, June 20). The relationship between data science and machine learning. https://blog.pangeanic.com/trelationship-between-data-science-and-machine-learning
Rice University MDS Program. (n.d.). Data Science vs. AI & Machine Learning. https://csweb.rice.edu/academics/graduate-programs/online-mds/blog/data-science-vs-ai-and-ml
Sartorius. (2020, July 15). Understanding the Relationship Between Data Science, AI, and Machine Learning. https://www.sartorius.com/en/knowledge/science-snippets/data-science-vs-artificial-intelligence-vs-machine-learning-602514
Wevolver. (2023, July 19). Unsupervised vs Supervised Learning: A Comprehensive Comparison. https://wevolver.com/article/unsupervised-vs-supervised-learning-a-comprehensive-comparison
Yeung, A., et al. (2022). Large Language Models in the Data Science Lifecycle: A Systematic Mapping Study. arXiv:2508.11698.

