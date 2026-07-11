# Part A — Theory

# 1. Introduction to Unsupervised Learning and Clustering

Unsupervised Learning is a type of machine learning where the model works without labelled data. It learns patterns on its own by grouping similar data points or finding hidden structures without any human intervention.

**How is it different from regression and classification?**

- Classification predicts categories or labels like spam/not spam, disease/no disease, etc.
- Regression predicts continuous values like price, temperature, sales, etc.

**Give one real-life example of clustering and one of supervised learning.**

supervised example: **Heart Disease Prediction**

example of clustering: **Image Segmentation**

# 2. Clustering Algorithms

## K-Means
**K-means clustering** is an unsupervised learning algorithm used for data clustering, which groups unlabeled data points into groups or clusters.

 ###  how it works (basic idea)
The k-means clustering algorithm operates by categorizing data points into clusters by using a mathematical distance measure, usually euclidean, from the cluster center. The objective is to minimize the sum of distances between data points and their assigned clusters. Data points that are nearest to a centroid are grouped together within the same category. A higher k value, or the number of clusters, signifies smaller clusters with greater detail, while a lower k value results in larger clusters with less detail.

### one real-world use case in K-Means
**Image segmentation:** A computer vision technique that divides a digital image into distinct sets of pixels. This research dives into how k-means models are used to help identify boundaries in medical image.

### advantages of K-Means 
- **Simple:** K-means clustering is simple to understand and to put in practice.
- **Fast:** K-means clustering is designed with a computationally simple iterative approach.
- **Scalable:** K-means is also easily scalable to large datasets and generalizes to clusters of different shapes and sizes, which is ideal for cluster analysis.

### limitations of K-Means
- Sensitivity to Outliers
- Assumption of Round Clusters
- Need to Know the Number of Clusters
- Handling Large Datasets

## Hierarchical Clustering
Hierarchical Clustering is an unsupervised learning technique that groups data into a hierarchy of clusters based on similarity. It builds a tree‑like structure (dendrogram) that helps visualize relationships and decide the optimal number of clusters.

### How Does Hierarchical Clustering Work?
- **Compute Similarity**: Calculate the distance (similarity) between all pairs of data points using a metric like Euclidean distance or Manhattan distance.
-  **Merge Closest Clusters:**Find the two closest data points (or clusters) and merge them into a new cluster.
- **Recompute Distances:** Update the distances between the newly formed cluster and all other clusters.

### one real-world use case in Hierarchical Clustering

Genetics: Group genes or species based on similarity.

### advantages of Hierarchical Clustering
- No need to specify the number of clusters beforehand.
- Provides a hierarchy of clusters for better interpretability.
- Works well with small datasets and gives detailed insights.

### Limitations of Hierarchical Clustering
- Computationally expensive for large datasets.
- Sensitive to noise and outliers.
- Choice of linkage criterion and distance metric can significantly impact results.

## DBSCAN
**What is DBSCAN?**
DBSCAN, which stands for Density-Based Spatial Clustering of Applications with Noise, is a powerful clustering algorithm that groups points that are closely packed together in data space. Unlike some other clustering algorithms, DBSCAN doesn’t require you to specify the number of clusters beforehand, making it particularly useful for exploratory data analysis.

### How Does DBSCAN Work?
- **Parameter Selection:**
    - Choose ε (epsilon): The maximum distance between two points for them to be considered as neighbors.
    - Choose MinPts: The minimum number of points required to form a dense region.
- **Select a Starting Point**
    - The algorithm starts with an arbitrary unvisited point in the dataset.
- **Examine the Neighborhood:**
    - It retrieves all points within the ε distance of the starting point.
    - If the number of neighboring points is less than MinPts, the point is labeled as noise (for now).
    - If there are at least MinPts points within ε distance, the point is marked as a core point, and a new cluster is formed.
- **Expand the Cluster:-**
    - All the neighbors of the core point are added to the cluster.
    - If it’s a core point, its neighbors are added to the cluster recursively.
    - If it’s not a core point, it’s marked as a border point, and the expansion stops.

### one real-world use case in DBSCAN
Detecting fraudulent banking transactions by identifying unusual transactions as outliers (noise)

### advantages of  DBSCAN
- No Specified Number of Clusters: DBSCAN does not require the user to predefine the number of clusters, providing flexibility.
- Robust to Noise and Outliers: The algorithm can handle noise effectively, making it robust in real-world scenarios.
- Cluster Shape Variability: DBSCAN is capable of identifying clusters of arbitrary shapes and varying sizes, overcoming the limitations of convex-shaped assumptions.

### limitation of DBSCAN
- Sensitive to Parameter Selection
- Struggles with Varying Densities
- Performance on High-Dimensional Data
- Difficulty Choosing ε


## Clustering Metrics
### Elbow Method (SSE)
The Elbow Method is used to find the optimal number of clusters (k) in K-Means by analyzing how the clustering performance changes with different k values.

### Silhouette Score
The Silhouette Score is a metric used to evaluate the quality of clustering results. It measures how similar each data point is to its own cluster compared to other clusters, helping assess how well the data has been grouped. This score is widely used to evaluate clustering algorithms like K-Means.

### Davies–Bouldin Index
The Davies-Bouldin Index is a validation metric that is used to evaluate clustering models. It is calculated as the average similarity measure of each cluster with the cluster most similar to it.

|Metric|what it measures| good value|
|------|----------------|-----------|
|Elbow Method (SSE)|Compactness of clusters (distance from points to centroids)|Lower is better|
|Silhouette Score|Cohesion and separation of clusters|Closer to 1|
|Davies–Bouldin Index|cluster similarity|Closer to 0|

## Choosing k and Interpreting Segments

**How do you choose the number of clusters for K-Means?**
Choose the optimal K value using the Elbow Method (plotting Within-Cluster Sum of Squares) to find the "bend" in the curve, or use Silhouette Analysis to evaluate cluster cohesion and separation.

High Fresh + Milk spend: The cluster represents customers like restaurants or hotels that buy more fresh food and dairy products for daily operations.
High Grocery + Detergents_Paper spend: The cluster represents customers like supermarkets or retail stores that buy more packaged goods and cleaning products.

exclude Channel and Region because they do not represent customer spending behavior. They are existing categories that describe where customers belong, not how they purchase.



## Real-World Case Study

**Bank Customer Segmentation Using Clustering**
A bank wanted to better understand its customers and provide more personalized financial products. The goal was to group customers based on their financial behavior and service usage.

The data used included customer age, income, account balance, credit card usage, loan history, transaction frequency, and savings patterns.

The bank applied Hierarchical Clustering to identify groups of customers with similar financial characteristics. This method helped the bank visualize relationships between customers and determine meaningful segments.

The analysis revealed several customer groups, including high-income investors, regular savers, frequent borrowers, and low-activity customers. Each group had different financial needs and behaviors.

Using these insights, the bank offered customized products and services, such as investment plans for high-income customers and special loan offers for frequent borrowers. This improved customer satisfaction, increased product adoption, and helped the bank strengthen customer relationships.

This case study demonstrates how clustering can be used to identify customer segments and support more effective business and marketing strategies.









