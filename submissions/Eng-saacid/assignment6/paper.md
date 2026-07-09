# Part A: Clustering Theory and Practice

## 1. Introduction to Unsupervised Learning and Clustering

### Unsupervised Learning

Unsupervised learning is a type of machine learning where algorithms learn patterns and structures from data without using labeled outputs. Unlike supervised learning, the dataset does not contain a target variable that tells the model the correct answer. Instead, the algorithm discovers hidden relationships, similarities, and groups within the data.

Clustering is one of the most common unsupervised learning techniques. It organizes data points into groups called clusters, where objects inside the same cluster are more similar to each other than objects in different clusters.

### Difference Between Unsupervised Learning, Regression, and Classification

Supervised learning uses labeled data, meaning that the model learns from examples where the correct output is already known.

Regression is a supervised learning task used to predict continuous numerical values. For example, predicting house prices based on location, size, and number of rooms.

Classification is also supervised learning but predicts categories or classes. For example, a bank may classify loan applications as approved or rejected.

Unsupervised learning does not predict a known output. Instead, it discovers patterns from the data itself. For example, a company can use clustering to group customers based on purchasing behavior without knowing the customer groups in advance.

### Real-Life Examples

An example of clustering is customer segmentation in retail. A company can group customers according to their purchasing habits, such as customers who buy large amounts of grocery products versus customers who buy more fresh products.

An example of supervised learning is email spam detection, where a model learns from labeled emails marked as spam or not spam and predicts the category of new emails.

---

# 2. Clustering Algorithms

## K-Means Clustering

K-Means is one of the most popular clustering algorithms. It divides data into a predefined number of clusters (k). The algorithm starts by selecting k initial centroids. Each data point is assigned to the nearest centroid based on distance. After assignment, the centroids are updated by calculating the average position of points in each cluster. This process continues until the centroids become stable.

### Real-world Use Case

K-Means is commonly used for customer segmentation. Businesses use it to group customers based on purchasing behavior, spending patterns, or demographic information.

### Advantages

- Simple and easy to understand.
- Efficient for large datasets.
- Works well with numerical data.

### Limitations

- The number of clusters (k) must be selected in advance.
- Sensitive to outliers.
- Different initial centroids may produce different results.

---

## Hierarchical Clustering

Hierarchical clustering creates a hierarchy of clusters by either repeatedly merging smaller clusters or splitting larger clusters.

Agglomerative clustering, a common type of hierarchical clustering, starts with each data point as an individual cluster and gradually merges the most similar clusters until the desired number of clusters is reached.

### Real-world Use Case

Hierarchical clustering is used in biology for grouping similar genes and in customer analysis for discovering natural customer groups.

### Advantages

- Does not require random centroid initialization.
- Can reveal relationships between clusters.
- Useful for exploring data structure.

### Limitations

- Computationally expensive for large datasets.
- Once clusters are merged, they cannot easily be separated again.
- Choosing the number of clusters can still be challenging.

---

## DBSCAN Clustering

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is a clustering algorithm that groups points based on data density. It identifies areas with many closely packed points as clusters and marks isolated points as noise.

### Real-world Use Case

DBSCAN is used in geographic analysis, such as identifying locations with high activity or detecting unusual patterns in spatial data.

### Advantages

- Can detect clusters of different shapes.
- Does not require specifying the number of clusters beforehand.
- Can identify outliers as noise.

### Limitations

- Sensitive to parameter selection.
- May struggle when clusters have different densities.
- Less effective for high-dimensional datasets.

---

# 3. Clustering Metrics

## Elbow Method (SSE)

The Elbow Method helps determine a suitable number of clusters for K-Means. It calculates the Sum of Squared Errors (SSE), which measures the distance between data points and their assigned cluster centroids.

As the number of clusters increases, SSE decreases. The optimal k is usually selected where the improvement starts to slow down, creating an "elbow" shape.

---

## Silhouette Score

The Silhouette Score measures how similar each data point is to its own cluster compared with other clusters.

The value ranges from -1 to 1:

- A value close to 1 indicates well-separated clusters.
- A value close to 0 indicates overlapping clusters.
- A negative value indicates poor clustering.

---

## Davies-Bouldin Index

The Davies-Bouldin Index measures the similarity between clusters by comparing cluster distance and cluster size.

A lower value indicates better clustering because clusters are more separated and compact.

---

## Metric Comparison Table

| Metric | What it Measures | Good Value |
|---|---|---|
| SSE (Elbow Method) | Distance between points and centroids | Lower SSE; choose the elbow point |
| Silhouette Score | Cluster separation and compactness | Higher value (closer to 1) |
| Davies-Bouldin Index | Similarity between clusters | Lower value |

---

# 4. Choosing k and Interpreting Segments

The number of clusters in K-Means can be selected using methods such as the Elbow Method and Silhouette Score. The Elbow Method identifies where adding more clusters provides less improvement, while the Silhouette Score evaluates how well-separated the clusters are.

In the wholesale distributor project, a cluster with high Fresh and Milk spending represents customers who purchase large amounts of fresh products and dairy items. These customers may include supermarkets or businesses that frequently require fresh inventory.

A cluster with high Grocery and Detergents_Paper spending represents customers focused on household and grocery products. These customers may benefit from bulk pricing and product promotions.

Channel and Region are excluded because clustering should be based on customer purchasing behavior. Including these columns could make clusters depend on business type or location instead of spending patterns.

---

# 5. Real-World Case Study

A common application of clustering is customer segmentation in the retail industry. Many companies use clustering techniques to understand customer behavior and create personalized marketing strategies.

For example, retail companies analyze customer transaction data containing purchase frequency, spending amounts, and product categories. K-Means clustering is often applied to divide customers into groups with similar buying patterns.

The goal is to identify valuable customer segments, improve marketing campaigns, and provide better services. The results help businesses understand different customer needs and create targeted offers.

---

# References

- Scikit-learn Documentation. Clustering Methods.
  https://scikit-learn.org/stable/modules/clustering.html

- Han, J., Kamber, M., & Pei, J. (2022). *Data Mining: Concepts and Techniques.*

- Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow.*