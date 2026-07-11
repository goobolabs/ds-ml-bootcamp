Assignment Six – Part A: Theory

Student Information

- Assignment: Assignment Six – Clustering: Theory and Practice
- Course: Data Science & Machine Learning Bootcamp
- Student Name: Nasteho abdi aden
- Submission Date: July 8, 2026

---

Introduction

This document presents the theoretical section of Assignment Six. It explains the fundamentals of unsupervised learning, clustering algorithms, clustering evaluation metrics, customer segmentation, and a real-world application of clustering in business.

---

1. Introduction to Unsupervised Learning and Clustering

What is Unsupervised Learning?

Unsupervised learning is a type of Machine Learning where the algorithm learns from data that has no labeled outputs. Instead of predicting known answers, the model discovers hidden patterns, structures, or relationships within the dataset. It groups similar data points together based on their characteristics without human guidance. Unsupervised learning is commonly used for clustering, dimensionality reduction, and anomaly detection.

How is it Different from Regression and Classification?

Regression and classification are supervised learning methods because they require labeled data. Regression predicts continuous numerical values, such as house prices or sales revenue. Classification predicts predefined categories, such as whether an email is spam or not spam.

In contrast, unsupervised learning does not use labeled data. Instead, it identifies natural groupings or patterns within the dataset. The algorithm decides how to organize the data without knowing the correct answers beforehand.

Real-Life Examples

Clustering Example: Customer segmentation in a supermarket. Customers with similar purchasing habits are grouped together so the business can provide personalized promotions and marketing strategies.

Supervised Learning Example: Email spam detection. The model is trained using labeled emails and learns to classify new emails as either spam or not spam.

---

2. Clustering Algorithms

K-Means

K-Means is one of the most popular clustering algorithms. It works by selecting a fixed number of clusters (k), assigning each data point to the nearest cluster center (centroid), and repeatedly updating the centroids until the clusters become stable.

Real-world use case: Customer segmentation in retail businesses.

Advantages

- Simple and fast.
- Easy to understand and implement.
- Works well on large datasets.

Limitations

- The number of clusters (k) must be chosen before training.
- Sensitive to outliers.
- Performs best with clusters that are roughly spherical.

---

Hierarchical Clustering

Hierarchical Clustering builds clusters by creating a tree-like structure called a dendrogram. It can either merge smaller clusters together (agglomerative) or split larger clusters into smaller ones (divisive).

Real-world use case: Grouping patients with similar medical characteristics.

Advantages

- No need to specify the number of clusters initially.
- Produces an easy-to-interpret dendrogram.
- Useful for exploring relationships among data.

Limitations

- Computationally expensive for large datasets.
- Sensitive to noise and outliers.
- Difficult to adjust once clusters are merged.

---

DBSCAN

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) groups together points that are closely packed while marking isolated points as noise or outliers. It identifies clusters based on density rather than distance to centroids.

Real-world use case: Detecting geographical hotspots or identifying fraudulent transactions.

Advantages

- Can discover clusters with irregular shapes.
- Detects outliers automatically.
- Does not require specifying the number of clusters.

Limitations

- Choosing appropriate parameter values can be difficult.
- Performance decreases when data density varies significantly.
- Less effective in very high-dimensional datasets.

---

3. Clustering Metrics

Elbow Method (SSE)

The Elbow Method uses the Sum of Squared Errors (SSE), also called inertia, to help determine the optimal number of clusters. As the number of clusters increases, SSE decreases. The best value of k is usually found where the curve forms an "elbow," indicating that adding more clusters provides only small improvements.

Silhouette Score

The Silhouette Score measures how well each data point fits within its assigned cluster compared to other clusters. The score ranges from -1 to 1. Values close to 1 indicate well-separated clusters, values near 0 indicate overlapping clusters, and negative values suggest incorrect clustering.

Davies–Bouldin Index

The Davies–Bouldin Index evaluates clustering quality by measuring the similarity between clusters. Lower values indicate better clustering because clusters are more compact and better separated.

Comparison Table

Metric| What it Measures| Good Value
Elbow Method (SSE)| Within-cluster error| Lower SSE with a clear elbow point
Silhouette Score| Cluster separation and cohesion| Close to 1
Davies–Bouldin Index| Similarity between clusters| Close to 0

---

4. Choosing k and Interpreting Segments

How do you choose the number of clusters for K-Means?

The number of clusters is commonly chosen using the Elbow Method and validated using the Silhouette Score. The selected value of k should balance low SSE with well-separated clusters that are meaningful for the business problem.

What does a cluster with high Fresh and Milk spending mean?

Customers in this cluster purchase large amounts of fresh food and dairy products. These customers may include restaurants, hotels, cafeterias, or businesses that require fresh ingredients regularly.

What does a cluster with high Grocery and Detergents_Paper spending mean?

Customers in this cluster spend more on grocery products and cleaning supplies. They are likely supermarkets, convenience stores, or retailers that sell packaged foods and household products.

Why are Channel and Region excluded from the clustering features?

Channel and Region are categorical variables rather than spending behaviors. Including them could bias the clustering process because the objective is to group customers based only on their purchasing patterns. They can still be used later to interpret the resulting clusters.

---

5. Real-World Case Study

A well-known application of clustering is customer segmentation in retail businesses. Companies analyze customer purchasing behavior to identify groups with similar spending habits. In many studies, K-Means clustering is applied to transaction data such as purchase frequency, product categories, and spending amounts. The goal is to create customer segments that support personalized marketing, inventory planning, and customer relationship management.

The results often reveal distinct customer groups, such as high-value customers, occasional buyers, and price-sensitive shoppers. Businesses use these insights to improve marketing campaigns, recommend products, and increase customer satisfaction and profitability.

---

References

1. Han, J., Kamber, M., & Pei, J. Data Mining: Concepts and Techniques.
2. Géron, A. Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow.
3. Scikit-learn Documentation – Clustering Algorithms.