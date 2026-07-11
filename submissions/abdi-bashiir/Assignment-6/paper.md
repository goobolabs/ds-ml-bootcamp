# Clustering in Machine Learning

## 1. Introduction to Unsupervised Learning and Clustering

### What is Unsupervised Learning?

Unsupervised learning is a type of machine learning where the model learns patterns from data without using labeled outputs or target variables. Instead of predicting known answers, the algorithm discovers hidden structures, similarities, and relationships within the data. Clustering is one of the most common techniques used in unsupervised learning.

### Difference Between Unsupervised Learning, Regression, and Classification

Regression and classification are supervised learning methods because they require labeled data.

- **Regression** predicts continuous numerical values such as house prices or temperatures.
- **Classification** predicts categories or classes such as spam vs. non-spam emails.
- **Unsupervised learning** does not use labels. Instead, it groups similar data points together based on their characteristics.

### Real-Life Examples

**Clustering Example:**

A supermarket groups customers based on their purchasing behavior. Customers with similar shopping habits are placed in the same group so the company can provide personalized offers.

**Supervised Learning Example:**

A bank predicts whether a loan application will be approved using historical data that already contains approved and rejected loan records.

---

# 2. Clustering Algorithms

## K-Means

### How it Works

K-Means divides data into **k** clusters. It begins by selecting k random centroids. Each data point is assigned to its nearest centroid. The centroids are then updated by calculating the mean of all points assigned to each cluster. This process repeats until the centroids stop changing significantly.

### Real-World Use Case

Customer segmentation for marketing campaigns.

### Advantages

- Simple to understand.
- Fast on large datasets.
- Works well when clusters are clearly separated.

### Limitations

- The value of **k** must be chosen before training.
- Sensitive to outliers.
- Assumes clusters are roughly spherical.

---

## Hierarchical Clustering

### How it Works

Hierarchical Clustering builds clusters step by step. Agglomerative clustering starts with each data point as its own cluster and repeatedly merges the closest clusters until the stopping condition is reached.

### Real-World Use Case

Grouping customers based on purchasing behavior or organizing biological data.

### Advantages

- No random centroid initialization.
- Produces a dendrogram that helps visualize relationships.

### Limitations

- Slower than K-Means.
- Less suitable for very large datasets.

---

## DBSCAN

### How it Works

DBSCAN groups data based on density. Points in dense regions form clusters, while isolated points are treated as noise or outliers.

### Real-World Use Case

Detecting fraudulent transactions or identifying unusual customer behavior.

### Advantages

- Automatically detects outliers.
- Does not require specifying the number of clusters.

### Limitations

- Choosing suitable parameters can be difficult.
- Performance decreases when cluster densities vary significantly.

---

# 3. Clustering Metrics

## Elbow Method (SSE)

The Elbow Method uses the Sum of Squared Errors (SSE) to help determine the best number of clusters. As the number of clusters increases, SSE decreases. The best value of **k** is usually found at the "elbow" point where the decrease begins to slow.

## Silhouette Score

The Silhouette Score measures how well each data point fits within its own cluster compared to other clusters.

- Range: **-1 to 1**
- A value close to **1** indicates well-separated clusters.

## Davies–Bouldin Index

The Davies–Bouldin Index measures how similar clusters are to one another.

- Lower values indicate better clustering.
- A smaller score means clusters are compact and well separated.

## Comparison Table

| Metric | Measures | Good Value |
|---------|----------|------------|
| Elbow Method (SSE) | Total clustering error | Clear elbow point |
| Silhouette Score | Cluster separation | Close to 1 |
| Davies–Bouldin Index | Cluster similarity | Close to 0 |

---

# 4. Choosing k and Interpreting Customer Segments

## Choosing the Number of Clusters

The Elbow Method is commonly used to choose the best value of **k**. By plotting SSE against different values of **k**, we look for the point where the curve starts to flatten. That point usually represents the most suitable number of clusters.

## Interpreting Customer Segments

Customers with high spending on **Fresh** and **Milk** products may represent restaurants, hotels, or businesses that regularly purchase fresh food.

Customers with high spending on **Grocery** and **Detergents_Paper** are more likely to be supermarkets or retail stores that buy household products in bulk.

Understanding these groups helps businesses create targeted marketing strategies and improve customer service.

## Why Channel and Region Are Excluded

Channel and Region are excluded because the objective is to cluster customers using only their purchasing behavior. Including these columns could bias the clustering results since they describe customer categories rather than spending patterns.

---

# 5. Real-World Case Study

## Customer Segmentation in Retail

Many retail companies use clustering to understand customer behavior. One common example is customer segmentation based on purchasing history.

### Goal

The goal is to identify different groups of customers so businesses can improve marketing strategies and customer satisfaction.

### Data Used

The dataset usually contains customer spending information, purchase frequency, and product categories.

### Clustering Method

K-Means Clustering is one of the most commonly used algorithms because it is simple, efficient, and works well for customer segmentation.

### Results

The analysis identifies customer groups with different purchasing habits. Businesses can then provide personalized promotions, loyalty programs, and product recommendations, leading to improved customer satisfaction and increased sales.

---

# References

1. Scikit-learn Documentation. *Clustering Algorithms.* https://scikit-learn.org/stable/modules/clustering.html

2. Han, J., Kamber, M., & Pei, J. *Data Mining: Concepts and Techniques.* Morgan Kaufmann.

3. Géron, A. *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow.* O'Reilly Media.