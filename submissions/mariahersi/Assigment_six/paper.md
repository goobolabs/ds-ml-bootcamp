# Part A — Clustering Theory Paper

## 1. Introduction to Unsupervised Learning and Clustering

Unsupervised learning is a type of Machine Learning where a model learns patterns from data without using a known target label. In supervised learning, the dataset usually contains both input variables and an output variable, such as predicting exam result, loan approval, or house price. In unsupervised learning, the model only receives the input variables and tries to discover hidden structure. Clustering is one of the most common unsupervised learning tasks because it groups similar records together based on their features.

Clustering is different from regression and classification because regression and classification are supervised learning tasks. Regression predicts a continuous numeric value, such as sales amount or car price. Classification predicts a category, such as approved/rejected or pass/fail. Clustering does not predict a known label. Instead, it discovers natural groups in the data. For example, a supermarket can use clustering to group customers based on their spending behavior. A supervised learning example would be using past customer data to predict whether a customer will buy a product.

In customer segmentation, clustering is useful because it helps businesses understand different customer types. For example, wholesale customers who spend more on Fresh and Frozen products may behave differently from customers who spend more on Grocery and Detergents_Paper. By identifying these groups, a distributor can create better marketing, stock planning, pricing, and delivery strategies.

## 2. Clustering Algorithms

### K-Means

K-Means is a centroid-based clustering algorithm. The user chooses the number of clusters, called k. The algorithm starts with k centroids, assigns each data point to the nearest centroid, then updates the centroids based on the average position of the assigned points. This assign-and-update process continues until the clusters become stable. Scikit-learn explains that K-Means separates samples into groups by minimizing inertia, also called within-cluster sum of squares.

A real-world use case of K-Means is customer segmentation in retail. Customers can be grouped based on spending score, income, purchase frequency, or product category spending. The main advantage of K-Means is that it is simple, fast, and easy to interpret. Its limitation is that the user must choose k before training, and it can be affected by outliers and feature scaling.

### Hierarchical Clustering

Hierarchical clustering creates clusters in a tree-like structure. Agglomerative clustering is the most common form. It begins with each data point as its own cluster, then repeatedly merges the most similar clusters until the required number of clusters is reached. Scikit-learn describes Agglomerative Clustering as a method that recursively merges pairs of clusters using linkage distance.

A real-world use case is grouping wholesale customers based on similar purchasing behavior. Its advantage is that it can show relationships between clusters and does not require random centroid initialization. Its limitation is that it can be slower than K-Means for large datasets and may be sensitive to the chosen linkage method.

### DBSCAN

DBSCAN means Density-Based Spatial Clustering of Applications with Noise. It groups points that are close together in dense areas and marks points in sparse areas as noise or outliers. It uses two important parameters: epsilon, which defines the neighborhood distance, and min_samples, which defines the minimum number of points needed to form a dense region.

A real-world use case of DBSCAN is detecting unusual customer behavior, fraud patterns, or geographic location clusters. Its main advantage is that it can find irregularly shaped clusters and detect noise. Its limitation is that it can be difficult to choose good epsilon and min_samples values, especially when the dataset has different density levels.

## 3. Clustering Metrics

The Elbow Method uses SSE, also known as inertia, to help choose a good number of clusters for K-Means. SSE measures how close data points are to their assigned cluster center. As k increases, SSE usually decreases. The best k is often near the “elbow,” where the decrease becomes slower.

The Silhouette Score measures how similar a point is to its own cluster compared with the nearest other cluster. According to scikit-learn, the Silhouette Coefficient uses the mean distance within the same cluster and the mean distance to the nearest different cluster. A higher score means better-separated clusters.

The Davies–Bouldin Index measures the average similarity between clusters. Lower values are better because they show clusters are compact and well separated.

| Metric | What It Measures | Good Value |
|---|---|---|
| Elbow Method / SSE | Within-cluster error for K-Means | Lower SSE, but choose the elbow point |
| Silhouette Score | Separation between clusters and compactness within clusters | Higher is better; close to 1 is strong |
| Davies–Bouldin Index | Average similarity between clusters | Lower is better |

## 4. Choosing k and Interpreting Segments

The number of clusters in K-Means can be chosen using the Elbow Method, Silhouette Score, domain knowledge, and business usefulness. The Elbow Method shows how SSE changes as k increases. The Silhouette Score helps check whether clusters are well separated. However, the final choice should also make sense for the business. A clustering result with good metrics but confusing business meaning may not be useful.

In the wholesale distributor project, a cluster with high Fresh and Milk spending may represent customers such as restaurants, hotels, or food sellers that need perishable products. A cluster with high Grocery and Detergents_Paper spending may represent retailers or shops that sell packaged goods and household items. These interpretations help the distributor understand what each segment mainly buys.

Channel and Region are excluded from the clustering features because they are not spending amounts. They are categorical descriptors that can be used later for interpretation, but including them directly in distance-based clustering may distort the results. The six spending columns are more suitable because they describe customer purchasing behavior.

## 5. Real-World Case Study

A real-world customer segmentation study in Sweden tested clustering methods for retail customer segmentation. The study used customer purchase behavior features and compared clustering approaches including K-Means and Agglomerative Clustering. The result showed that K-Means and Agglomerative Clustering with an LRFMP model produced useful customer segments, including low-contribution customers and high-contributing loyal customers.

The goal of the study was to identify meaningful retail customer groups so that businesses could better understand customer value and create improved marketing strategies. The data used included customer transaction behavior. The clustering methods helped profile customers into groups that could support customer relationship management and targeted business actions.

## References

Memon, N. A. (2023). *Customer segmentation in retail: An experiment in Sweden*. DiVA Portal. https://www.diva-portal.org/smash/get/diva2:1784356/FULLTEXT01.pdf

Scikit-learn. (n.d.). *Clustering*. https://scikit-learn.org/stable/modules/clustering.html

Scikit-learn. (n.d.). *AgglomerativeClustering*. https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html

Scikit-learn. (n.d.). *silhouette_score*. https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html
