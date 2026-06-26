 ### Mahmud Ali Yousuf - Kure Bere

---

## Title: Personal Finance Transaction Dataset for Anomaly Detection

This dataset is to study spending behavior and explore how machine learning can be used to identify unusual financial transactions and this dataset was created from my own financial records and reflects real-world spending activities.

---

## Dataset Collection Method

The dataset was collected through personal financial tracking. Every income and expense transaction was manually recorded along with relevant information such as amount, transaction type, category, and date.

---

## Features and Label

### Features (X)

The dataset contains the following features:


| Feature | Description |
|----------|----------|
| Amount | Value of the transaction |
| Type | Indicates whether the transaction is an Income or Expense |
| Category | Category associated with the transaction |
| Transaction Date | Date of the transaction occurred |
| Day Of Week | Day corresponding to the transaction date |

These features describe financial behavior through transaction values, categories.

## Label (y)

This dataset does not contain a label (target variable).

The objective is not to predict a known outcome but to discover spending patterns and identify transactions that differ significantly from normal behavior.

---

## Dataset Structure

### Dataset Size

| Metric | Value |
|----------|----------|
| Rows | 155 |
| Columns | 5 |

### Sample Records

| Amount | Type | Category | Transaction Date | Day Of Week |
|----------|----------|----------|----------|----------|
| $0.25 | Expense | Transportation | April 7, 2026 | Tuesday |
| $0.50 | Expense | Transportation | April 7, 2026 | Tuesday |
| $7.50 | Expense | Food | April 7, 2026 | Tuesday |
| $3.75 | Income | Food | April 7, 2026 | Tuesday |
| $0.50 | Expense | Transportation | April 7, 2026 | Tuesday |

---

## Data Quality Issues

Real-world data often contains issues that must be addressed before machine learning can be applied.

### Currency Formatting

The Amount feature contains currency symbols such as:

- $0.25
- $7.50
- $20.00

These values must be converted into numeric format before analysis.

### Categorical Variables

Several features contain text values:

- Type
- Category
- Day Of Week

Machine learning algorithms generally require numerical input, so these features will need encoding during preprocessing.

### Date Formatting

The Transaction Date feature is stored as text and may need to be converted into a date format.

### Class Imbalance

The dataset contains:

- 148 Expense transactions
- 7 Income transactions

This imbalance may influence data analysis and should be considered during preprocessing.

### Outliers

Some transaction amounts are significantly larger than typical daily expenses. These values may represent valid transactions but can behave as outliers when analyzing spending patterns.

### Feature Scaling

Transaction amounts vary across different ranges. Scaling may be applied to ensure that larger numerical values do not dominate the learning process.

---

## Learning Type

This dataset represents an **unsupervised learning** problem.

In supervised learning, a model learns from labeled examples where a target variable is provided. In this dataset, there is no label indicating whether a transaction is normal or unusual.

Instead, the model must learn spending patterns directly from the data and identify transactions that deviate from those patterns. Therefore, the dataset is appropriate for unsupervised learning.

---

## Machine Learning Use Case

The primary machine learning application for this dataset is **anomaly detection**.

Anomaly detection aims to identify observations that differ significantly from normal behavior. In personal finance, this can help detect:

- Unusually large expenses
- Rare spending categories
- Uncommon transaction patterns
- Spending behavior that differs from historical trends

The dataset is suitable for anomaly detection because it contains historical financial records that represent normal spending behavior over time. A machine learning model can learn these patterns and flag transactions that appear unusual.

---

## Data Science Lifecycle

### Problem Definition

Identify unusual spending behavior within personal financial transactions.

### Data Collection

Collect income and expense records through personal financial tracking.

### Data Cleaning and Preprocessing

Prepare the data by:

- Converting currency values into numeric format
- Encoding categorical features
- Processing date values
- Handling outliers
- Scaling numerical features if necessary

## #Modeling

Apply an anomaly detection technique to learn normal spending patterns from historical transactions.

### Deployment

Use the trained model to analyze future transactions and identify potentially unusual expenses.

---

## Conclusion

This project demonstrates the application of Data Science and Machine Learning concepts using a personally collected financial dataset. The dataset contains 155 transaction records and five features describing income and expense activities.

Since the dataset does not contain a target variable, it is best suited for unsupervised learning. Anomaly detection can be applied to identify transactions that differ significantly from normal spending behavior.

The project highlights key data foundations concepts including data collection, features, labels, dataset structure, preprocessing, and the role of machine learning within the Data Science lifecycle.