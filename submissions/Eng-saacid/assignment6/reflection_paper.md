# Reflection Paper: Wholesale Customer Segmentation

## 1. What Did I Implement?

In this project, I implemented a customer segmentation pipeline using the Wholesale Customers dataset. The goal was to group customers with similar purchasing behaviors using unsupervised machine learning techniques.

I used six spending features for clustering:
- Fresh
- Milk
- Grocery
- Frozen
- Detergents_Paper
- Delicassen

Before applying clustering algorithms, I handled extreme values using IQR capping and standardized the features using StandardScaler.

Two clustering methods were implemented:
1. K-Means Clustering
2. Agglomerative Clustering

K-Means was trained with five clusters, following the Lesson 6 approach. Agglomerative Clustering was implemented as an additional algorithm to compare its performance with K-Means.

## 2. Segment Interpretation

The K-Means results showed different customer purchasing patterns among the clusters.

### Cluster 0: Fresh and Frozen Focused Customers

This cluster contains customers with relatively high spending on Fresh and Frozen products. These customers may represent businesses that frequently purchase fresh products.

Business action:
The distributor could offer bulk discounts and priority delivery services for fresh product orders.

### Cluster 1: Grocery and Detergents_Paper Focused Customers

This cluster shows higher spending on Grocery and Detergents_Paper products. These customers are likely retailers that purchase household and grocery products regularly.

Business action:
The company could create loyalty programs and volume-based pricing for these customers.

### Cluster 2: Balanced Customers

This cluster represents customers with moderate spending across multiple product categories.

Business action:
The distributor could provide personalized recommendations based on their purchasing history.

## 3. Understanding K-Means

K-Means is an unsupervised learning algorithm that divides data points into a selected number of clusters (k).

The algorithm starts by selecting k initial centroids. Each customer is assigned to the nearest centroid based on distance. After assigning customers, the centroids are updated by calculating the average position of all customers in each cluster.

This assign-and-update process continues until the centroids stop changing. The final clusters represent groups of customers with similar characteristics.

## 4. Agglomerative Clustering

The additional algorithm selected for this project was Agglomerative Clustering, which is a hierarchical clustering method.

Unlike K-Means, Agglomerative Clustering starts with each customer as an individual cluster and repeatedly merges the most similar clusters until the desired number of clusters is reached.

One advantage of this method is that it does not require random centroid initialization. However, a limitation is that it can become computationally expensive for very large datasets.

The Silhouette Score comparison showed:

- K-Means: 0.340
- Agglomerative Clustering: 0.284

K-Means achieved a higher score, indicating better-separated clusters for this dataset.

## 5. Findings and Recommendation

Based on the evaluation results, K-Means clustering is the recommended approach for this wholesale customer segmentation task.

K-Means achieved a higher Silhouette Score compared with Agglomerative Clustering, which means its clusters were more compact and better separated.

Although Agglomerative Clustering provided useful insights and was a valuable comparison method, K-Means was more suitable for this dataset because wholesale spending patterns are numeric and distance-based clustering works effectively.

The segmentation results can help the distributor understand customer purchasing behavior, design targeted marketing strategies, and improve customer relationship management.

