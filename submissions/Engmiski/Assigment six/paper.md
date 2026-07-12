# Assignment Six: Clustering — Theory 

## Part A – Theory

# Introduction to Unsupervised Learning and Clustering

## What is Unsupervised Learning?

Machine Learning is divided into supervised and unsupervised learning. Unsupervised learning is a type of machine learning that works with data that has no predefined labels or target values. Instead of predicting known outcomes, the algorithm discovers hidden structures and relationships within the dataset.

One of the most common techniques in unsupervised learning is clustering. Clustering groups similar data points together based on their characteristics. The objective is to identify natural patterns that can help organizations understand their data and make informed decisions.

Unsupervised learning is widely used in customer segmentation, fraud detection, recommendation systems, image analysis, and biological research.

---

## Difference Between Unsupervised Learning, Regression, and Classification

Regression and classification belong to supervised learning because they require labeled training data. Regression predicts continuous numerical values such as house prices or sales revenue, while classification predicts categories such as spam or non-spam emails.

Unsupervised learning does not require labeled data. Instead, it analyzes the similarities between observations and automatically creates meaningful groups.

| Technique      | Input Data | Output            | Example                |
| -------------- | ---------- | ----------------- | ---------------------- |
| Classification | Labeled    | Categories        | Email Spam Detection   |
| Regression     | Labeled    | Continuous Values | House Price Prediction |
| Clustering     | Unlabeled  | Groups            | Customer Segmentation  |

---

## Real-Life Examples

### Clustering Example

A wholesale distributor records customer purchases throughout the year. By applying clustering, customers with similar purchasing behavior can be grouped together. One group may spend heavily on fresh food, while another mainly purchases grocery products and cleaning supplies. These groups help the company develop targeted marketing strategies and improve customer service.

### Supervised Learning Example

A bank uses historical customer information to predict whether a loan applicant is likely to repay a loan. Since previous loan outcomes are already known, this is a supervised learning problem.

---

# Clustering Algorithms

## K-Means Clustering

K-Means is one of the most popular clustering algorithms. It begins by selecting the number of clusters (**k**). The algorithm randomly initializes cluster centers called centroids. Each data point is assigned to the nearest centroid. The centroids are then recalculated based on the average position of all assigned points. This process repeats until the cluster assignments no longer change significantly.

### Use Case

Retail companies use K-Means to group customers according to purchasing behavior for personalized marketing campaigns.

### Advantages

* Easy to understand and implement.
* Fast for large datasets.
* Efficient for compact clusters.
* Produces meaningful customer segments.

### Limitations

* Requires selecting the number of clusters beforehand.
* Sensitive to outliers.
* Assumes clusters have similar shapes.
* Requires feature scaling.

---

## Hierarchical (Agglomerative) Clustering

Hierarchical clustering builds clusters step by step. Agglomerative clustering starts with every observation as its own cluster. The closest clusters are merged repeatedly until the desired number of clusters is reached.

### Use Case

Hospitals use hierarchical clustering to group patients with similar medical characteristics for disease analysis.

### Advantages

* Does not require random initialization.
* Produces a dendrogram showing relationships.
* Useful for discovering hierarchical structures.

### Limitations

* Computationally expensive on large datasets.
* Sensitive to noise.
* Once clusters are merged, they cannot be separated later.

---

## DBSCAN

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) groups observations based on density rather than distance. Dense regions become clusters, while isolated observations are treated as noise.

### Use Case

Banks and financial institutions use DBSCAN to identify fraudulent or unusual transactions.

### Advantages

* Detects clusters of different shapes.
* Automatically identifies outliers.
* Does not require specifying the number of clusters.

### Limitations

* Choosing suitable parameter values can be difficult.
* Performance decreases when cluster density varies.

---

# Clustering Metrics

## Elbow Method (SSE)

The Elbow Method helps determine the best number of clusters by calculating the Sum of Squared Errors (SSE) for different values of **k**. The optimal value is usually where the graph forms an "elbow," indicating that additional clusters provide only a small improvement.

---

## Silhouette Score

The Silhouette Score measures how well observations fit within their assigned clusters while remaining separated from other clusters.

* Close to **1** = Excellent clustering
* Around **0** = Overlapping clusters
* Less than **0** = Poor clustering

Higher values indicate better clustering quality.

---

## Davies–Bouldin Index

The Davies–Bouldin Index evaluates cluster compactness and separation. Lower values indicate better clustering because clusters are more distinct from one another.

---

## Comparison of Metrics

| Metric               | Measures              | Good Value  | Purpose                    |
| -------------------- | --------------------- | ----------- | -------------------------- |
| Elbow Method (SSE)   | Within-cluster error  | Elbow point | Select k                   |
| Silhouette Score     | Cohesion & Separation | Close to 1  | Evaluate cluster quality   |
| Davies–Bouldin Index | Cluster similarity    | Close to 0  | Measure cluster separation |

---

# Choosing the Number of Clusters

The number of clusters is commonly selected using the Elbow Method. The Silhouette Score can also be used to compare different values of **k**. In practice, business knowledge should also be considered when choosing the final number of clusters.

---

# Interpreting Customer Segments

In the wholesale customer dataset, the six spending variables represent annual purchases of different product categories.

Customers with high spending on **Fresh** and **Milk** are likely to be restaurants, hotels, or food service businesses that require fresh products every day.

Customers with high spending on **Grocery** and **Detergents_Paper** are more likely to be supermarkets or retail stores that purchase packaged foods and cleaning products in large quantities.

Understanding these customer segments allows wholesalers to improve inventory planning, create targeted promotions, and strengthen customer relationships.

---

# Why Are Channel and Region Excluded?

Channel and Region describe customer categories rather than purchasing behavior. Including these variables would influence clustering based on location or sales channel instead of spending patterns. Therefore, only the six spending variables are used to discover natural customer segments.

---

# Real-World Case Study

Many retail companies use customer segmentation to improve marketing performance. A common approach is applying K-Means clustering to customer purchase histories after standardizing the data. The resulting clusters often identify high-value customers, occasional buyers, and customers with specialized purchasing patterns.

These insights allow companies to personalize promotions, improve inventory management, increase customer satisfaction, and allocate marketing resources more effectively.

---

# Conclusion

Clustering is an important unsupervised learning technique that helps organizations discover hidden patterns within data. K-Means, Hierarchical Clustering, and DBSCAN each have strengths and limitations, making them suitable for different applications.

In the wholesale customer segmentation project, clustering identifies groups of customers with similar purchasing behavior. These customer groups provide valuable business insights that support better marketing, inventory management, and strategic decision-making.

---

# References

1. Géron, A. (2023). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.

2. Han, J., Kamber, M., & Pei, J. (2012). *Data Mining: Concepts and Techniques* (3rd ed.). Morgan Kaufmann.

3. Pedregosa, F., et al. (2011). *Scikit-learn: Machine Learning in Python*. Journal of Machine Learning Research, 12, 2825–2830.

4. Scikit-learn Developers. *Clustering User Guide*. https://scikit-learn.org/stable/modules/clustering.html
