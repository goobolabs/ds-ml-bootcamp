Unsupervised learning is a type of machine learning that learns from unlabeled data to find patterns or groups.

2. different between regression and classification?

- Unsupervised Learning: Uses data without labels or a target.
- Regression: Predicts a continuous numerical value.
- Classification: Predicts a category or class.

3. real-life example of clustering and one of supervised learning.

Clustering: A store groups customers based on their shopping behavior.
Supervised Learning: A bank predicts whether a loan application will be approved or rejected using labeled data.

1. K-Means

K-Means divides data into K clusters. It starts by choosing K centroids (center points), assigns each data point to the nearest centroid, and repeatedly updates the centroids until the clusters stabilize.

Real-World Use Case

Customer segmentation in marketing (grouping customers based on purchasing behavior).

**Advantages**

- Simple and fast.
- Works well on large datasets.
- Easy to understand and implement.

**Limitations**

- You must choose the number of clusters (K) beforehand.
- Sensitive to outliers.
- Works best when clusters are roughly spherical.

2. Hierarchical Clustering

Hierarchical Clustering builds a tree-like structure called a dendrogram. It either:

Starts with each point as its own cluster and merges them (Agglomerative), or
Starts with one cluster and splits it (Divisive).

**Real-World Use Case**

Grouping genes with similar characteristics in bioinformatics.

**Advantages**

- No need to specify the number of clusters initially.
- Produces a dendrogram that helps visualize relationships.
- Useful for small datasets.

**Limitations**

- Computationally expensive for large datasets.
- Sensitive to noise and outliers.
- Can become slow as data size increases.

3. DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

DBSCAN groups points that are closely packed together based on data density. Points in low-density areas are treated as noise (outliers).

Real-World Use Case:

Detecting fraudulent transactions or identifying unusual customer behavior.

**Advantages**

- Does not require specifying the number of clusters.
- Can find clusters of irregular shapes.
- Handles outliers well.

**Limitations**

- hoosing the right parameters (eps and min_samples) can be difficult.
- May struggle when cluster densities vary significantly.
- Performance can decrease in very high-dimensional data.

# Clustering Metrics

## 1. Elbow Method (SSE)

The Elbow Method uses the **Sum of Squared Errors (SSE)** to measure how close data points are to the center (centroid) of their cluster.

**What it measures**  

It measures the **compactness** of clusters. A lower SSE means data points are closer to their centroids.

**Good Value:**  

There is no fixed "good" value. Choose the **elbow point**, where adding more clusters only slightly reduces SSE.


## 2. Silhouette Score

The Silhouette Score measures how well each data point fits within its own cluster compared to other clusters.

**What it measures:**  

It evaluates both:

- **Cohesion** (how close points are within the same cluster)
- **Separation** (how far clusters are from each other)

**Good Value:**  

The score ranges from **-1 to 1**.

- **Close to 1:** Excellent clustering
- **Around 0:** Clusters overlap
- **Less than 0:** Poor clustering

## 3. Davies–Bouldin Index (DBI)


The Davies–Bouldin Index measures the average similarity between clusters by comparing cluster size and the distance between clusters.


It evaluates how **compact** and **well-separated** the clusters are.

**Good Value:**  

- **Lower values are better**
- A value closer to **0** indicates better clustering.

# Comparison Table

| Metric | What It Measures | Good Value | Best Used For |
|--------|-------------------|------------|---------------|
| **Elbow Method (SSE)** | Measures cluster compactness (distance to centroid) | Choose the **elbow point** where SSE stops decreasing sharply | Selecting the optimal number of clusters (K) |
| **Silhouette Score** | Measures cohesion and separation between clusters | **Closer to 1** | Evaluating clustering quality |
| **Davies–Bouldin Index (DBI)** | Measures cluster similarity and separation | **Lower is better** (closer to 0) | Comparing clustering models |


# Choosing K and Interpreting Segments

## Choosing the Best K

I chose K = 3 because it gives the best balance between the evaluation metrics. The Elbow Method shows that the SSE starts to level off around K = 3. Also, K = 3 has a higher Silhouette Score (0.340) than K = 5 (0.283), which means the clusters are better separated. Although K = 5 has a slightly lower Davies–Bouldin Score (1.270 vs. 1.297), the difference is small. Therefore, K = 3 is the better choice for this dataset.

A cluster with high Fresh and Milk spending represents customers who mainly buy fresh food and dairy products. These customers may be restaurants, hotels, or cafes. A cluster with high Grocery and Detergents_Paper spending represents customers who mainly buy grocery and cleaning products. These customers may be supermarkets or retail stores.

Channel and Region are excluded because they do not describe customers' purchasing behavior. K-Means works best with numerical spending features, so the clusters are created using the spending data only. Channel and Region can be used later to understand and describe the clusters.

# Real-World Case Study 

Customer Segmentation Using K-Means in Insurance and Telecommunication

**Goal**

The goal of the study was to identify customer segments based on purchasing behavior. The company wanted to find profitable customer groups and improve marketing and customer relationship management (CRM).

**Data Used**

The researchers used real customer data from insurance and telecommunication companies. The data included customers' purchase behavior and other customer characteristics.

**Clustering Method**

The study applied K-Means clustering to group customers with similar purchasing behavior. After clustering, the researchers also used decision trees to classify new customers into the discovered segments.

**Key Results and Insights**

The study successfully identified different customer segments. These segments helped the companies:

- Identify profitable customers.
- Improve marketing strategies.
- Better understand customer behavior.
- Predict which segment new customers belong to.

The researchers concluded that combining K-Means clustering with decision trees is effective for customer segmentation in real businesses.