Online shoppers purchasing intention and behavior profiling Api 
Prepared by: Asmaa Ahmed Hussein
Project Type: Unsupervised Learning (Clustering) and Supervised Learning (Classification)
Technologies: Python, Jupyter Notebook, Scikit-Learn, XGBoost, FastAPI, Pandas, NumPy, Matplotlib, Seaborn
1. Project Overview and Objective This project implements an advanced machine learning pipeline that combines both main branches of Machine Learning to solve a critical e-commerce challenge: predicting whether an online website visitor will complete a purchase transaction (Revenue: True/False).Instead of feeding raw session data directly into classifiers, the pipeline is split into two strategic phases to maximize precision:
1. Unsupervised Clustering (K-Means and GMM): Used to segment website visitors into behavioral profiles based on their browsing dynamics (e.g., time spent on Administrative, Informational, and Product Related pages)
2. Supervised Classification (Logistic Regression, Random Forest, Gradient Boosting, XGBoost): The resulting cluster identities are injected back as engineered features, and multiple distinct classification algorithms are trained and compared to predict the final purchasing intention
3. Dataset Summary

The project is built upon the well-known Online Shoppers Purchasing Intention dataset

- Total Rows: 12,330 sessions
- Key Columns (Features):
  - Administrative_Duration, Informational_Duration, ProductRelated_Duration: Total time spent by the user on these specific page categories
  - BounceRates, ExitRates, PageValues: Web metrics tracked via Google Analytics for each session
  - Revenue (Target Variable): Binary outcome indicating if a purchase was completed.
Project Pipeline Steps

 Step 1: Data Preprocessing
- Handled categorical transformations using OneHotEncoder for attributes like Month
- Scaled continuous variables using StandardScaler to normalize numeric ranges
- Split the dataset into a stratified 80% Training set and 20% Testing set to handle potential class imbalances

 Step 2: Unsupervised Customer Profiling
- Evaluated both K-Means and Gaussian Mixture Models (GMM) on user interaction metrics
- Generated behavior profile IDs (Segment_ID) which were appended back into the dataframe as an advanced feature for the predictive models.

 Step 3: Model Training and Evaluation
- Trained four distinct classification algorithms: Logistic Regression, Random Forest, Gradient Boosting, and XGBoost
- Prioritized the F1-Score metric to evaluate performance, ensuring a proper balance between Precision and Recall due to the severe minority of actual buying sessions.
Model Metrics and Evaluation

Below are the performance results captured during model evaluation on the test set:

| Model | Accuracy | Precision | Recall | F1-Score |
| :--- | :--- | :--- | :--- | :--- |
| Logistic Regression | ~88.2% | ~64.1% | ~52.3% | ~57.6% |
| Random Forest | ~89.5% | ~73.4% | ~56.1% | ~63.6% |
| Gradient Boosting | ~90.1% | ~75.2% | ~59.4% | ~66.3% |
| XGBoost (Winner) | ~90.6% | ~76.8% | ~61.2% | ~68.1% |

Final Decision: XGBoost was selected as the deployment model because it produced the highest F1-Score, effectively learning complex browsing signals to identify buyers without generating heavy false positives.
Directory Structure
online-shopper-intent-api/
├── dataset/
│ └──shopping.csv # Raw analytics dataset
├── src/
│ ├── preprocess.py # Session profiling and scaling pipeline
│ └── train.py # Trains all 6 algorithms and saves the best
├── api/
│ └── app.py # FastAPI application script
├── models/
│ ├── best_classifier.pkl
├── README.md # Documentation file
└── project_paper.md     
