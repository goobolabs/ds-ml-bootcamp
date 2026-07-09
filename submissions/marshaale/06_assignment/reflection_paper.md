## What did you implemented

I implemented customer segmentation using kmeans and hierarchical agglomerative.
FIrst load and inspect dataset second handle outlier using iqr range and scale features then clustering with evaluation and sanity check.

## Segment Interpretation

| Channel | Region |    Fresh |    Milk | Grocery |  Frozen | Detergents_Paper | Delicassen | Cluster |
| ------: | -----: | -------: | ------: | ------: | ------: | ---------------: | ---------: | ------: |
|       3 |      1 | 13,265.0 | 1,196.0 | 4,221.0 | 6,404.0 |            507.0 |    1,788.0 |       3 |
|       7 |      2 |  7,579.0 | 4,956.0 | 9,426.0 | 1,669.0 |          3,321.0 |    2,566.0 |       0 |
|       1 |      2 |  7,057.0 | 9,810.0 | 9,568.0 | 1,762.0 |          3,293.0 |    1,776.0 |       0 |

| Cluster | Description                                                                                                                                          | Business Action                                                                               |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **0**   | Customers mainly buy high amounts of **Milk** and **Grocery** products, with moderate purchases of Frozen, Detergents_Paper, and Delicatessen items. | Offer bulk discounts and bundle milk and grocery products to increase repeat purchases.       |
| **3**   | Customers mainly buy **Fresh** products, with lower spending on Milk, Detergents_Paper, and Delicatessen items.                                      | Promote fresh products and recommend complementary grocery or frozen items to increase sales. |

## Understanding K-Means

K-Means is unsupervised algorithm it divides dataset n(k) clusters and uses centroid(mean of points in cluster) until clusters becomes stable.

**k** is number of clusters
**centroids** is average of all points in each cluster has it's own centroid
**assign-and-update loop** is the way kmeans uses to improve until clusters becomes stable

## Your Second Algorithm

I choose hierarchical agglomerative because groups data points in a tree of nested clusters it continuously merges based similarity.

**Advantages** handles irregularly shaped clusters,visualize relationships between data points using a dendrogram.

**Limitations** needs more computation,slow and memory-intensive for massive datasets,sensitive to noise and outliers.

Both have same Silhouette Score

## Your Findings

I recommended using kmeans because has better performance in Davies Bouldin which measures how compact each cluster is and how well-separated different clusters are.

## Reference

[Hierarchical Clustering](https://www.geeksforgeeks.org/machine-learning/hierarchical-clustering/)
