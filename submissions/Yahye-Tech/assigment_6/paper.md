# Assignment Six: Clustering — Theory and Practice

# Part A: Theory

## 1. Introduction to Unsupervised Learning and Clustering

Unsupervised learning is a branch of Machine Learning that discovers hidden patterns or structures in data without using labeled outputs. Unlike supervised learning, it does not require a target variable. Instead, it groups similar data points based on their characteristics.

Regression and classification are supervised learning techniques because they require labeled data. Regression predicts continuous numerical values, while classification predicts categories or classes.

A real-life example of clustering is customer segmentation in a supermarket, where customers are grouped according to their purchasing behavior. A real-life example of supervised learning is email spam detection, where emails are classified as spam or not spam using labeled training data.

---

## 2. Clustering Algorithms

### K-Means

K-Means is one of the most popular clustering algorithms. It partitions data into K clusters by assigning each data point to the nearest centroid. The centroids are updated repeatedly until they no longer change significantly.

**Use Case**
- Customer segmentation
- Market analysis
- Product recommendation

**Advantages**
- Fast and simple.
- Works well on large datasets.
- Easy to understand.

**Limitations**
- The number of clusters (K) must be chosen in advance.
- Sensitive to outliers.
- Assumes clusters are roughly spherical.

---

### Hierarchical Clustering

Hierarchical Clustering creates a tree-like structure called a dendrogram. It can be performed using either agglomerative (bottom-up) or divisive (top-down) methods.

**Use Case**
- Biological classification
- Document clustering
- Customer grouping

**Advantages**
- No need to specify K initially.
- Produces an interpretable dendrogram.

**Limitations**
- Slower on large datasets.
- Difficult to modify after clustering.

---

### DBSCAN

DBSCAN groups points based on density. It identifies dense regions as clusters while treating isolated points as noise.

**Use Case**
- Fraud detection
- GPS location clustering
- Anomaly detection

**Advantages**
- Finds clusters of arbitrary shapes.
- Detects noise automatically.

**Limitations**
- Sensitive to parameter selection.
- Performance decreases when densities vary.

---

## 3. Clustering Metrics

### Elbow Method (SSE)

The Elbow Method measures the Sum of Squared Errors (SSE). It helps determine the optimal number of clusters by identifying the point where adding more clusters provides only a small improvement.

### Silhouette Score

The Silhouette Score measures how similar an object is to its own cluster compared to other clusters. Values close to 1 indicate well-separated clusters.

### Davies–Bouldin Index

The Davies–Bouldin Index evaluates cluster quality by measuring the average similarity between clusters. Lower values indicate better clustering.

| Metric | Measures | Good Value |
|---------|----------|------------|
| Elbow Method (SSE) | Cluster compactness | Elbow point |
| Silhouette Score | Cluster separation | Close to 1 |
| Davies–Bouldin Index | Cluster similarity | Close to 0 |

---

## 4. Choosing K and Interpreting Segments

The Elbow Method is commonly used to select the optimal value of K. The best K is chosen where the decrease in SSE starts to slow significantly.

Customers with high Fresh and Milk spending are usually restaurants, hotels, or businesses that frequently purchase fresh food.

Customers with high Grocery and Detergents_Paper spending are often supermarkets and retail stores that require cleaning supplies and grocery products.

Channel and Region are excluded because they are labels describing customer categories rather than purchasing behavior. Including them could bias the clustering results.

---

## 5. Real-World Case Study

A retail company used K-Means clustering to segment customers according to purchasing behavior. Customer transaction data, including spending in different product categories, was collected. K-Means identified groups of customers with similar buying habits. The results helped the company improve marketing strategies, personalize promotions, and optimize inventory management.

## References

- Scikit-learn Documentation: https://scikit-learn.org/
- Han, Kamber & Pei. Data Mining: Concepts and Techniques.
- Tan, Steinbach & Kumar. Introduction to Data Mining.