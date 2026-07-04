Reflection Paper: Loan Approval Classification
1. What Did You Implement?
In this project, I successfully reproduced the machine learning pipeline from Lesson 5 to preprocess a financial dataset and predict loan approvals (Approved vs. Denied). The pipeline involved loading the raw data, handling skewed numeric distributions, and performing feature engineering to construct domain-specific variables like DebtToIncome and IncomePerYearEmployed.

Why Feature Scaling is Essential
A critical component of this implementation was applying RobustScaler to the numerical features before training the models. Feature scaling was strictly necessary for two primary

Preventing Feature Dominance: Financial variables like LoanAmount or Income have raw values in the thousands or millions, whereas features like EmploymentYears or CreditScore exist on much smaller scales. Without scaling, algorithms would mathematically mistake larger magnitude numbers as being inherently more important, completely ignoring crucial smaller-scale features.

Handling Extreme Outliers: I chose RobustScaler specifically because financial datasets frequently contain extreme outliers (e.g., exceptionally high incomes or massive loan requests). Unlike MinMaxScaler or StandardScaler, which get heavily distorted by outliers, RobustScaler scales features using the median and the Interquartile Range (IQR), ensuring that extreme values do not corrupt the model's learning process.

Following the preprocessing stage, I split the data into an 80% training set and a 20% testing set (stratified by the target variable) and trained three classification algorithms: Logistic Regression, Random Forest Classifier, and Gradient Boosting Classifier.

2. Comparison of Models
Sanity Check Predictions
During the single-row sanity check (testing row index i = 2), all three models converged on the exact same prediction: Approved. This matched the ground truth (Actual label: Approved), demonstrating that for straightforward, clear-cut applicant profiles, both simple and complex algorithms yield consistent and reliable outputs.

Realistic Results & Code Troubleshooting
The Gradient Boosting Classifier provided the most realistic and nuanced overall performance.

