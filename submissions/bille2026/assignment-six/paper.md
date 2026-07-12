# Part A — Theory: Unsupervised Learning and Clustering

## 1. Introduction to Unsupervised Learning and Clustering

### Unsupervised Learning in Machine Learning

Unsupervised learning is a branch of machine learning where algorithms learn patterns and structures from data without using labeled outputs. Unlike supervised learning, the dataset does not contain predefined answers or target values. The main goal of unsupervised learning is to discover hidden relationships, groups, or patterns within the data.

Clustering is one of the most common techniques in unsupervised learning. It groups similar data points together based on their characteristics. The algorithm does not know the names or meanings of the groups; instead, it identifies natural similarities in the data.

### Difference Between Unsupervised Learning, Regression, and Classification

Supervised learning uses labeled data, meaning each input has a known output. It includes classification and regression.

Classification predicts categories. For example, a model can predict whether a loan application is approved or rejected.

Regression predicts numerical values. For example, predicting house prices based on features such as size, location, and number of rooms.

Unsupervised learning does not use labeled outputs. Instead, it discovers hidden structures in data. For example, clustering can group customers based on their purchasing behavior.

### Real-Life Examples

An example of clustering is customer segmentation in retail. Companies group customers based on spending patterns and buying behavior.

An example of supervised learning is spam email detection, where models learn from emails labeled as spam or not spam.

---

# 2. Clustering Algorithms

## K-Means Clustering

K-Means is one of the most popular clustering algorithms. It divides data into K groups. The algorithm selects cluster centers called centroids and assigns each data point to the nearest centroid. The centroids are updated by calculating the average position of points in each cluster until the clusters become stable.

### Real-world Use Case

K-Means is widely used for customer segmentation, where businesses group customers based on purchasing behavior.

### Advantages

- Simple and easy to implement.
- Fast for large datasets.
- Works well when clusters are clearly separated.

### Limitations

- Requires choosing the number of clusters before training.
- Sensitive to outliers.
- Does not work well with irregular cluster shapes.

---

## Hierarchical Clustering

Hierarchical clustering creates a tree structure called a dendrogram. Agglomerative clustering starts with each data point as a separate cluster and repeatedly combines the closest clusters until a hierarchy is created.

### Real-world Use Case

It is used in biology for gene analysis and in businesses for analyzing customer relationships.

### Advantages

- Shows relationships between clusters using a dendrogram.
- Does not always require choosing K at the beginning.
- Useful for smaller datasets.

### Limitations

- Slower than K-Means.
- Not suitable for very large datasets.
- Sensitive to distance measurements.

---

## DBSCAN

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) groups points based on density. It identifies areas with many closely located points as clusters and marks isolated points as noise.

### Real-world Use Case

DBSCAN is used in geographical analysis and fraud detection to identify unusual patterns.

### Advantages

- Detects irregularly shaped clusters.
- Handles noise and outliers.
- Does not require specifying the number of clusters.

### Limitations

- Parameter selection can be difficult.
- Performance decreases with high-dimensional data.

---

# 3. Clustering Metrics

## Elbow Method (SSE)

The Elbow Method helps choose the best value of K for K-Means. It measures the Sum of Squared Errors (SSE), which shows how close data points are to their cluster centers.

The best K is usually selected where adding more clusters does not significantly improve the SSE value.

## Silhouette Score

Silhouette Score measures how similar each point is to its own cluster compared with other clusters.

The score ranges from -1 to +1. Values closer to +1 indicate better-separated clusters.

## Davies–Bouldin Index

Davies–Bouldin Index measures similarity between clusters.

Lower values indicate better clustering because clusters are more separated.

## Comparison Table

| Metric | What it Measures | Good Value |
|---|---|---|
| Elbow Method (SSE) | Cluster error and choosing K | Elbow point |
| Silhouette Score | Cluster separation and similarity | Close to +1 |
| Davies-Bouldin Index | Cluster similarity | Lower is better |

---

# 4. Choosing k and Interpreting Segments

The number of clusters in K-Means can be selected using the Elbow Method and Silhouette Score.

In the wholesale distributor project:

A cluster with high Fresh and Milk spending represents customers who buy more fresh products and dairy items.

A cluster with high Grocery and Detergents_Paper spending represents customers who purchase more packaged goods and household products.

Channel and Region are excluded because they describe customer categories and locations rather than purchasing behavior. Including them could make clusters based on location instead of spending patterns.

---

# 5. Real-World Case Study: Customer Segmentation

Customer segmentation is a common application of clustering in business and marketing.

Retail companies analyze customer transaction data, including spending amounts, purchase frequency, and product preferences. Using clustering algorithms such as K-Means, businesses divide customers into groups with similar behaviors.

The goal is to create personalized marketing strategies, improve customer experience, and identify valuable customer groups.

The results help companies understand different customer types, such as high-value customers, regular customers, and customers with specific product interests.

---

# References

1. Scikit-learn Documentation: Clustering Algorithms.
2. Han, J., Kamber, M., & Pei, J. (2012). Data Mining: Concepts and Techniques.
3. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). An Introduction to Statistical Learning.