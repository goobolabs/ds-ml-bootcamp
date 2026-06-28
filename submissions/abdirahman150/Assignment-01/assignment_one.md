# Research Assignment: Introduction to Data Science and Machine Learning

## 1. Definitions and Relationship

### What is Data Science?
Data Science is an interdisciplinary field that uses scientific methods, statistical analysis, and computing tools to extract knowledge and insights from data.

In practical terms, Data Science is not just about building models; it includes collecting data, cleaning it, exploring its structure, choosing the right analysis techniques, and interpreting the results.

### What is Machine Learning?
Machine Learning (ML) is a subset of Data Science and artificial intelligence focused on teaching computers to recognize patterns and make predictions using data.

Machine Learning algorithms learn from examples and create a general rule for making decisions or predictions, such as classifying images, forecasting sales, or grouping customers.

### Relationship between Data Science and Machine Learning
Machine Learning is one of the tools used within Data Science. Data Science is the broader process that includes problem definition, data collection, analysis, evaluation, and communication. Machine Learning fits into the analysis stage when a predictive or descriptive model is needed.

A useful way to picture the relationship is:
- Data Science is the project framework.
- Machine Learning is a set of methods used inside that framework.

### Real-life example
Consider a bank that wants to reduce loan defaults. Data Science begins by defining the problem, assembling customer financial records, cleaning missing values, and exploring patterns. Machine Learning is then used to train a model that estimates the probability a customer will fail to repay a loan.

In this example:
- Data Science identifies the business need and prepares the data.
- Machine Learning creates a predictive model from historical loan outcomes.
- The combined effort helps the bank decide which loan applications present too much risk.

## 2. The Data Science Lifecycle

The Data Science lifecycle is the sequence of steps taken from understanding a problem to delivering a working solution. A common version of the lifecycle includes:

1. Problem definition
2. Data acquisition
3. Data preparation
4. Exploratory data analysis (EDA)
5. Modeling
6. Evaluation
7. Deployment
8. Monitoring and maintenance

### Problem definition
The project starts by clarifying the question to answer, the goals, and the success criteria. This stage ensures that technical work will solve a real problem.

### Data acquisition
This stage collects the data needed for the project, whether from databases, APIs, sensors, surveys, or external sources.

### Data preparation
This involves cleaning, transforming, and integrating data. It addresses missing values, inconsistent formats, and outliers.

### Exploratory data analysis (EDA)
EDA helps uncover patterns, relationships, and data quality issues. It uses tables, graphs, and summary statistics to build intuition about the data.

### Modeling
At this stage, Machine Learning typically fits in. Data Scientists select algorithms, train models, and adjust parameters to capture relationships in the data.

Machine Learning belongs in the modeling stage because that is where predictive or descriptive algorithms learn from data. If the project requires classification, regression, clustering, or recommendation, Machine Learning provides the methods to build the model.

### Evaluation
Evaluation tests the model using held-out data or cross-validation. It checks whether the model performs well and whether it is stable enough to be trusted.

### Deployment
Deployment makes the solution available in a real environment. This may mean integrating a model into a web service, dashboard, or business process.

### Monitoring and maintenance
After deployment, the system is monitored for performance changes, data drift, and new requirements. Models are updated or retrained as needed.

## 3. Supervised Learning vs Unsupervised Learning

Machine Learning can be divided into supervised and unsupervised learning based on whether the training data includes labeled answers.

### Supervised Learning
Supervised learning uses labeled data, meaning each example includes the correct output. The model learns to map inputs to outputs.

- Example: Predicting house prices from location, size, and age of the building.
- Common tasks: classification and regression.

In the house price example, the algorithm is trained on past sales where the sale price is known. The model learns how features like number of rooms and neighborhood affect price.

### Unsupervised Learning
Unsupervised learning uses unlabeled data. The model discovers structure or patterns without predefined outputs.

- Example: Grouping customers into segments based on purchase behavior.
- Common tasks: clustering and dimensionality reduction.

In customer segmentation, the algorithm identifies groups of similar customers without being told the correct grouping ahead of time.

### Comparison table

| Feature | Supervised Learning | Unsupervised Learning |
| --- | --- | --- |
| Labels | Requires labeled outputs | Uses unlabeled data |
| Goal | Predict or classify outcomes | Discover hidden structure |
| Example task | Loan default prediction | Customer segmentation |
| Evaluation | Accuracy, RMSE, precision/recall | Cluster cohesion, silhouette score |

## 4. Causes of Overfitting and Prevention

### What causes overfitting?
Overfitting happens when a model learns the training data too well, including the noise and random fluctuations, rather than the underlying general pattern. As a result, it performs well on the training data but poorly on new, unseen data.

Common causes:
- Model complexity that is too high (e.g., too many parameters)
- Insufficient training data
- Noisy or irrelevant features
- Training too long without regularization

### How to prevent overfitting
Some practical strategies are:

- Use simpler models: choose a model with fewer parameters or less expressive power when data is limited.
- Regularization: add penalties for large weights (such as L1 or L2 regularization) to discourage overly complex models.
- Cross-validation: evaluate the model on different subsets of the data to ensure it generalizes.
- Feature selection: remove irrelevant or redundant input features.
- Early stopping: stop training when performance on validation data stops improving.
- Collect more data: larger datasets help models learn general patterns instead of noise.

## 5. Train/Test Split and Why It Is Necessary

### How data is split
When building a Machine Learning model, the available dataset is usually split into at least two parts:
- Training data: used to fit the model.
- Test data: held back and used only to evaluate the final model.

A common split is 70-80% for training and 20-30% for testing, though the exact ratio depends on dataset size and project needs. Sometimes a third validation set is used to tune model parameters and choose among candidate models.

### Why this process is necessary
Splitting the data is necessary to estimate how the model will perform on new examples. If a model is evaluated on the same data it learned from, its performance estimate will be overly optimistic.

The train/test split ensures that evaluation reflects generalization ability rather than memorization of training examples. It is a basic safeguard against overfitting.

## 6. Case Study: Machine Learning in Healthcare

### Selected case study
A widely cited example is the application of Machine Learning to detect diabetic retinopathy from retinal images.

In this case study, researchers trained a convolutional neural network on thousands of labeled eye images to classify whether a patient had signs of diabetic retinopathy. The model was evaluated against expert ophthalmologists and achieved accuracy comparable to specialist review.

### Findings
- The trained model could identify moderate or worse diabetic retinopathy with high sensitivity and specificity.
- Automated screening could reduce the workload of specialists and allow earlier detection of vision-threatening disease.
- The model performed best when trained on a large, diverse dataset and evaluated using held-out test images.

### Lifecycle coverage
This case study covers multiple stages of the Data Science lifecycle:
- Problem definition: reduce missed cases of diabetic retinopathy and improve screening.
- Data acquisition: collect labeled retinal images and diagnostic outcomes.
- Data preparation: standardize image sizes, remove poor-quality scans, and balance classes.
- Modeling: train a deep learning classifier using supervised learning.
- Evaluation: test on held-out images and compare with clinical experts.
- Deployment: propose integration into screening programs for primary care settings.

