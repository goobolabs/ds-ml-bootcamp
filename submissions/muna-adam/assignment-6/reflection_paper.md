# What I Implemented

I segmented wholesale clients using the six spending columns: **Fresh, Milk, Grocery, Frozen, Detergents_Paper, and Delicassen**. First, I handled extreme outliers using the IQR method and capped them with `clip()`. Then, I standardized the data using `StandardScaler` so that large spending columns would not dominate the clustering results.

After scaling, I applied **K-Means clustering with K = 3**. I evaluated the model using the **Silhouette Score** and **Davies–Bouldin Score**. I also applied **Agglomerative Clustering with K = 3** as a second clustering algorithm and compared its Silhouette Score with K-Means.

# Segment Interpretation

## 1. Cluster 0: Grocery, Milk, and Detergents_Paper Buyers

Cluster 0 spends the most on **Grocery (16,653.32)**, **Milk (10,142.25)**, and **Detergents_Paper (7,022.05)**. This group is likely made up of supermarkets, retail stores, or large convenience shops because these businesses need many household and grocery products.

**Business action:** The distributor can offer bulk discounts, supermarket product bundles, and regular restocking agreements for Grocery, Milk, and Detergents_Paper.

## 2. Cluster 1: Low-to-Moderate Spending Clients

Cluster 1 has the lowest spending in most categories, especially **Milk (2,685.47)**, **Grocery (3,583.98)**, **Detergents_Paper (942.49)**, and **Delicassen (750.71)**. However, it has moderate spending on Fresh and Frozen products. This group may represent smaller shops, cafés, or small food businesses.

**Business action:** The distributor can provide smaller package sizes, loyalty rewards, and promotional offers to encourage these clients to increase their orders.

## 3. Cluster 2: High Fresh, Grocery, and Milk Buyers

Cluster 2 is the highest Fresh-spending segment. It spends the most on **Fresh products (22,881.83)**, followed by **Grocery (6,773.44)**, **Milk (5,870.35)**, and **Frozen products (5,057.43)**. Compared with the other clusters, it is especially distinguished by very high Fresh spending.

**Business action:** The distributor can offer frequent fresh-food deliveries, special prices for bulk Fresh and Frozen orders, and promotions on Delicassen products.

# Understanding K-Means

K-Means is an unsupervised machine learning algorithm that groups similar customers into a chosen number of clusters, called **K**. In this project, K was set to 3, meaning the customers were divided into three groups.

K-Means begins by creating three centroids, which are the center points of the clusters. Each client is assigned to the nearest centroid based on their spending values. Then, the centroids are recalculated using the average values of the clients inside each cluster. This assign-and-update process continues until the clusters stop changing significantly.

# My Second Algorithm

The additional algorithm I selected was **Agglomerative Clustering**. I chose it because it is a hierarchical clustering method and does not depend on random centroid initialization like K-Means.

Agglomerative Clustering starts by treating every client as its own separate cluster. It then repeatedly merges the most similar clients or groups until the required number of clusters is reached.

- **Advantage:** It does not depend on random centroid initialization and can show how clusters are merged step by step.
- **Limitation:** It can be slower than K-Means when the dataset becomes very large.

The Silhouette Score for Agglomerative Clustering was **0.2841**, while the K-Means Silhouette Score was **0.340**. Since a higher Silhouette Score is better, K-Means performed better for this dataset.

# Findings

I recommend using **K-Means clustering** for this wholesale customer segmentation task. K-Means achieved a higher Silhouette Score of **0.340**, compared with **0.2841** for Agglomerative Clustering. This shows that K-Means created clearer and better-separated customer groups.

K-Means is also useful because it produces cluster centroids, which show the average spending pattern of each customer segment. These results can help the distributor create targeted discounts, delivery plans, product bundles, and marketing strategies for different wholesale clients.