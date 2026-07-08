Spending Pattern Analysis - Assignment 6
This folder contains my work for Assignment 6 – Spending Pattern Analysis with K-Means (Clustering). The project explores customer segmentation based on income and spending habits using unsupervised learning.

Contents
customer_segmentation.ipynb.ipynb
Jupyter Notebook containing the full clustering workflow:

Data loading and preprocessing (handling missing values).
Feature scaling using StandardScaler.
Optimal cluster determination via the Elbow Method (SSE calculation).
Model training with K-Means.
Performance evaluation using Silhouette Score and Davies–Bouldin Index.
Cluster center analysis in original units.
A reflection paper answering assignment questions, including:

Description of the K-Means implementation.
Justification for the chosen K value based on metrics.
Interpretation of customer segments (e.g., High Income / High Spending).
Suggested business actions for each cluster and discussion of limitations.
spending_labeled_clusters.csv
The final output dataset with an added Cluster column assigning each customer to their respective segment.

Dataset
Uses Loan.csv, which contains customer information including CustomerID, Age, Income_$, and SpendingScore.
Requirements
Python 3.x
pandas, numpy, scikit-learn
Jupyter Notebook
Note on Windows Compatibility
The notebook includes a fix for a known K-Means memory leak warning on Windows by setting OMP_NUM_THREADS=1.