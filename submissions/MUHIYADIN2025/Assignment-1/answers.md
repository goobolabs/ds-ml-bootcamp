Course: Data Science & Machine Learning Bootcamp (1 Month) Author: Muhiadin Said Hassan Date: 15/Jun/2026
1. Define Machine Learning using a real-life example.
Machine Learning (ML) is a field of Artificial Intelligence where computers automatically learn patterns from data to make predictions or decisions without explicit programming. ML allows systems to improve performance as they are exposed to more data.
Example (Finance - Fraud Detection): Banks use ML models to detect fraudulent credit card transactions. The model is trained on past transaction data labeled as legitimate or fraudulent and learns patterns like unusual transaction amounts or locations. When new transactions occur, the model predicts potential fraud to alert the bank.
Reference: Jordan, M. I., & Mitchell, T. M. (2015). Machine learning: Trends, perspectives, and prospects. Science, 349(6245), 255–260. https://doi.org/10.1126/science.aaa8415
2. Compare Supervised Learning and Unsupervised Learning, giving an example of each.
Supervised Learning Learns from labeled data (input-output pairs).
Tasks: Regression (predict continuous values), Classification (predict categories).
Example (Healthcare): Predicting diabetes based on patient age, BMI, blood sugar levels.
Unsupervised Learning
Learns from unlabeled data to identify hidden patterns.
Tasks: Clustering (grouping similar items), Dimensionality Reduction (simplifying features).
Example (Marketing): Segmenting customers based on purchasing behavior for targeted advertising.
Comparison Table
Aspect	Supervised Learning	Unsupervised Learning
Data Labels	Required ✅	Not required ❌
Goal	Predict outcomes	Discover hidden patterns
Algorithms	Linear Regression, Random Forest, Logistic Regression	K-Means, PCA
Real-world Example	Predicting hospital readmission	Customer segmentation
References:

Hastie, T., Tibshirani, R., & Friedman, J. (2009). The Elements of Statistical Learning. Springer. https://doi.org/10.1007/978-0-387-84858-7
Murphy, K. P. (2012). Machine Learning: A Probabilistic Perspective. MIT Press.
3. What causes Overfitting? How can it be prevented?
Overfitting occurs when a model captures noise instead of general patterns. Underfitting occurs when a model is too simple to capture the underlying structure.

Causes of Overfitting:

Too complex models for limited data
Noisy or irrelevant features
Insufficient training examples
Prevention Methods:

Train-test split and cross-validation
Regularization (L1/L2)
Feature selection
Early stopping
Data augmentation
Example: A neural network memorizes every transaction in a small fraud dataset → high training accuracy but fails on new data.

Reference: Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press.

4. Explain how training data and test data are split, and why this process is necessary.
Purpose: To check how well a machine learning model can predict new, unseen data, and to avoid overfitting.

Example of Splitting:

Suppose we have 1,000 images of animals for a classification task.
Training data (70%) → 700 images used to teach the model to recognize features of each animal.
Test data (30%) → 300 images kept aside and never shown to the model during training; used to evaluate how well the model predicts labels for new images.
Key Points:

The training set is what the model learns from.
The test set is what we use to measure real-world performance.
Validation set (optional) can be used to tune model parameters without touching the test set.
This split ensures that performance metrics reflect the model's ability to generalize, not just memorize training data.
Reference: Géron, A. (2019). Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow. O'Reilly Media.

5. Find one case study (research paper or article) that explains how Machine Learning has been applied in healthcare, business, or transportation. Summarize its findings.
Study: Prediction of Diabetes Using Statistical and Machine Learning Techniques. Algorithms, 18(3), 145. https://doi.org/10.3390/a18030145



Summary:

Objective: Predict diabetes onset using patient demographics and clinical measurements.
Data: 768 patients with features like glucose, BMI, age.
Models Tested: Logistic Regression, Decision Trees, Random Forests, Gradient Boosting.
Findings: Ensemble models (Random Forest, Gradient Boosting) achieved highest predictive accuracy (~85–87%).
Implication: ML can identify high-risk patients early, enabling preventative healthcare interventions.
Reference: Prediction of Diabetes Using Statistical and Machine Learning Techniques. (2025). Algorithms, 18(3), 145. https://doi.org/10.3390/a18030145

References
Beam, A. L., & Kohane, I. S. (2018). Big data and machine learning in health care. JAMA, 319(13), 1317–1318. https://doi.org/10.1001/jama.2017.18391
Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press.
Hastie, T., Tibshirani, R., & Friedman, J. (2009). The Elements of Statistical Learning. Springer. https://doi.org/10.1007/978-0-387-84858-7
Jordan, M. I., & Mitchell, T. M. (2015). Machine learning: Trends, perspectives, and prospects. Science, 349(6245), 255–260. https://doi.org/10.1126/science.aaa8415
Kohavi, R. (1995). A study of cross-validation and bootstrap for accuracy estimation and model selection. Proceedings of IJCAI.
Murphy, K. P. (2012). Machine Learning: A Probabilistic Perspective. MIT Press.
Prediction of Diabetes Using Statistical and Machine Learning Techniques. (2025). Algorithms, 18(3), 145. https://doi.org/10.3390/a18030145
Prepared by: Muhiadin Said Hassan