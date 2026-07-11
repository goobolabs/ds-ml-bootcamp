## Introduction to Unsupervised Learning and Clustering

Unsupervised learning is opposite of supervised learning in supervised we have features(X) and target(Y),But in unsupervised learning, we only have features (X), so the target (Y) is what we need to discover by using clustering(grouping similar data into clusters).

The difference between regression and classification compared to clustering is that, in regression and classification we have target and we the know possible output we can say either is category or its numeric.

In clustering case we have explore data and discover the target.

**Clustering** real use cases is recommendation,marketing,health care.
**Supervised** real use case loan approval,age prediction,grade classification.

## Clustering Algorithms

### K-Means

K-Means is unsupervised algorithm it divides dataset n(k) clusters and uses centroid(mean of points in cluster) until clusters becomes stable.

Steps

- Choose k(numbers of clusters(groups))
- Place initial centroid
- Assign every point to nearest centroid
- Update centroid using average
- Repeat until clusters stable

Use cases customer segmentation,movie recommendation

**Advantages** Simple,fast,best for numeric,best for medium to large

**Limitations** Must choose k(clusters(groups)),sensitive to outliers,needed to scale

### Hierarchical Clustering

Hierarchical is unsupervised algorithm groups data points in a tree of nested clusters it continuously merges or split data based similarly

There are two types of Hierarchical Clustering: Agglomerative Clustering and Divisive clustering

Agglomerative starts with each data point as standalone cluster and merges step by step similar data until cluster becomes stable

Divisive start one big cluster and splits until cluster becomes stable

Use cases marketing and customer segmentation,image segmentation,document and text clustering

**Advantages** handles irregularly shaped clusters,visualize relationships between data points using a dendrogram.

**Limitations** needs more computation,slow and memory-intensive for massive datasets,sensitive to noise and outliers.

### DBSCAN Clustering

DBSCAN is unsupervised algorithm groups data points that are closely packed together and marked outliers as noise base their density.

DBSCAN works by categorizing data points into three types:

- Core points
- Border points
- Noise points

Key Parameters

- `Eps (ε)`: Maximum distance between two points to be considered neighbors.
- `MinPts`: Minimum number of neighboring points required to form a dense region.

Use cases customer segmentation,GPS/location data analysis,fraud detection

**Advantages** handles irregularly shaped clusters,handles noise and outliers.

**Limitations** choosing appropriate Eps and MinPts can be difficult,performance decreases when clusters have very different densities.

## Clustering Metrics

**Elbow Method (SSE)** is a method used to decide your k in kmeans algorithm by comparing each `k` and `sse`.

**Silhouette Score** measures how points are close to their own cluster uses range -1 between +1. < 0 is bad, 0 is overlap cluster, 0.5 > good and < 0.5 weak cluster.

**Davies–Bouldin Index** measures how compact each cluster is and how well-separated different clusters are.

- Compact clusters: Data points are close to their centroid.
- Well-separated clusters: Centroids of different clusters are far apart.

unlike silhouette score lower is better.

| **Elbow Method**                  | **Silhouette Score**                                                                | **Davies–Bouldin Index**                                           |
| --------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Used to decide **k** for K-Means. | Measures how close points are to their own cluster and how far from other clusters. | Measures how compact clusters are and how well-separated they are. |
| **Elbow point = Best k**          | **Higher = Better**                                                                 | **Lower = Better**                                                 |

## Choosing k and Interpreting Segments

### How do you choose the number of clusters for K-Means?

Choose k using the elbow method by comparing k and sse. choose k when sse drops down slowly example k 1 sse 100 k2 sse 60 k3 sse 40 k4 sse 20. the k is likely 3.

### What does a cluster with high Fresh + Milk spend vs high Grocery + Detergents_Paper spend mean?

High Fresh + Milk indicates fresh product buyers, while high Grocery + Detergents_Paper indicates grocery and cleaning product buyers.

### Why do we exclude Channel and Region from the clustering features?

Channel and Region are spending behavior and makes clustering noise.so they are excluded and used only for interpretation.

## Real-World Case Study

**Goal:** Develop a customer segmentation model to improve decision-making in the online retail industry by better understanding customer purchasing behavior.

**Data Used:** A UK-based online retail dataset from the UCI Machine Learning Repository containing **541,909 customer records** and **8 features**. The study used the **RFM (Recency, Frequency, Monetary)** framework to measure customer value.

**Clustering Methods Applied:** The study compared five clustering algorithms:

- K-means
- Gaussian Mixture Model (GMM)
- DBSCAN
- Agglomerative Clustering
- BIRCH

**Key Results/Insights:** Among all the clustering methods, the **Gaussian Mixture Model (GMM)** achieved the best performance with a **Silhouette Score of 0.80**, making it the most effective algorithm for customer segmentation in this study.

## Reference

[An Exploration of Clustering Algorithms for Customer Segmentation in the UK Retail Market](https://www.mdpi.com/2813-2203/2/4/42)
