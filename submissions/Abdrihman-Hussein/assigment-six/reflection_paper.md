# Reflection Paper: Wholesale Customer Segmentation

## What I Implemented

In this assignment, I implemented two clustering algorithms on the Wholesale Customers dataset: **K-Means** and **Agglomerative Clustering**. Both algorithms were applied to the six customer spending features: **Fresh, Milk, Grocery, Frozen, Detergents_Paper,** and **Delicassen**. Before clustering, the data was standardized so that each feature contributed equally to the clustering process.

The goal was to segment wholesale customers into groups based on their purchasing behavior. After training both models, I evaluated the clustering results using the **Silhouette Score**, which measures how well-separated the clusters are.

## Segment Interpretation

One cluster contained customers who spent a large amount on **Fresh** and **Frozen** products but relatively less on Grocery and Detergents. These customers may represent restaurants, hotels, or food service businesses that purchase fresh ingredients regularly. A suitable business strategy would be to offer discounts on bulk fresh food orders and provide fast delivery services.

Another cluster consisted of customers with high spending on **Milk, Grocery,** and **Detergents_Paper**. These customers likely represent supermarkets or retail stores that frequently purchase household products. The distributor could increase customer loyalty by offering volume discounts, loyalty rewards, or personalized promotions.

A third cluster showed customers with relatively low spending across all categories. These customers may be small shops or infrequent buyers. The distributor could encourage larger purchases by offering promotional bundles or discounts for higher-order quantities.

## Understanding K-Means

K-Means is an unsupervised machine learning algorithm that groups similar data points into a predefined number of clusters, represented by **k**. The algorithm begins by selecting **k** initial centroids. Each customer is assigned to the nearest centroid based on distance, usually Euclidean distance.

After all customers are assigned, the algorithm recalculates the centroid of each cluster by computing the average position of the assigned points. The assignment and centroid update process continues repeatedly until the centroids stop changing significantly or a maximum number of iterations is reached. The final clusters contain customers with similar purchasing patterns.

## My Second Algorithm

For the second clustering method, I selected **Agglomerative Clustering**, a hierarchical clustering algorithm. I chose this algorithm because it does not rely on random centroid initialization and creates a hierarchy of clusters by gradually merging the most similar groups.

Agglomerative Clustering starts by treating each data point as its own cluster. It repeatedly merges the two closest clusters until the desired number of clusters is reached. One advantage of this method is that it can capture hierarchical relationships between data points and often performs well on datasets with complex structures. One limitation is that it is computationally more expensive than K-Means, especially for large datasets.

When comparing the Silhouette Scores, K-Means achieved a slightly higher score than Agglomerative Clustering. This indicates that K-Means produced slightly better-separated and more compact clusters for this dataset.

## My Findings

Based on the results, I would recommend **K-Means** for the wholesale customer segmentation task. It produced well-defined clusters, achieved a better Silhouette Score, and was computationally efficient. It is also easy to implement and scales well to large datasets, making it suitable for business applications.

Agglomerative Clustering was still useful because it provided another perspective on the customer groups and did not depend on random centroid initialization. However, considering both clustering quality and computational efficiency, K-Means is the more practical choice for segmenting wholesale customers and supporting marketing and business decision-making.
