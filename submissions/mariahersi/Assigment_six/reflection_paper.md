# Part C — Reflection Paper

## 1. What I Implemented

In this practical assignment, I implemented wholesale customer segmentation using the six spending columns: Fresh, Milk, Grocery, Frozen, Detergents_Paper, and Delicassen. I did not use Channel and Region as clustering features because they are categorical descriptors, not product spending values. First, I applied IQR capping with `k=1.5` to reduce the effect of extreme values without deleting rows. After that, I scaled the six features using StandardScaler so that all spending columns contributed fairly to distance-based clustering.

I trained two clustering algorithms. The first method was K-Means with `n_clusters=5`, `n_init="auto"`, and `random_state=42`, as required by the lesson. The second method was Agglomerative Clustering with five clusters. Finally, I compared the two methods using Silhouette Score and Davies-Bouldin Index, performed a sanity check with three selected clients, and saved the K-Means segmented dataset as `segmented_wholesale_customers.csv`.

## 2. Segment Interpretation

The K-Means model produced five customer clusters. Cluster centers were converted back to original spending units so the segments could be interpreted in business language.

One segment, Cluster 0, had high spending mainly in Fresh and Grocery. This type of customer may need regular supply of these product categories. A suitable business action is to offer product bundles or discounts connected to their strongest categories.

Another segment, Cluster 1, showed strong spending in Fresh and Grocery. This may represent customers with a different purchasing pattern, such as retailers or food-service clients. A useful action is to create targeted promotions based on the product categories they already buy most.

Cluster 2 was also important because its center showed higher demand in Grocery and Fresh. The distributor could use this information to improve inventory planning and recommend related products to these customers.

## 3. Understanding K-Means

K-Means is an unsupervised clustering algorithm that groups similar data points into k clusters. The value of k is chosen before training. The algorithm begins by creating k centroids. Each customer is assigned to the nearest centroid based on distance. After assignment, the centroids are updated by calculating the average position of the customers in each cluster. This assign-and-update loop continues until the centroids become stable or the algorithm reaches its stopping condition.

In this project, K-Means grouped wholesale customers based on their scaled spending behavior. The final cluster labels help identify customers with similar product demand patterns.

## 4. My Second Algorithm

The second algorithm I chose was Agglomerative Clustering. I chose it because it is a hierarchical clustering method and gives a useful comparison against K-Means. It works by starting with each customer as a separate cluster, then merging the closest clusters step by step until the final number of clusters is reached.

One advantage of Agglomerative Clustering is that it does not rely on random centroid initialization. One limitation is that it can be slower for larger datasets and the final clusters can depend on the linkage method used.

In my results, K-Means achieved a Silhouette Score of **0.2831**, while Agglomerative Clustering achieved a Silhouette Score of **0.2185**. Based on Silhouette Score, **K-Means** produced better-separated clusters.

## 5. My Findings

For this wholesale segmentation task, I would recommend **K-Means** because it produced the higher Silhouette Score on the scaled spending features. A higher Silhouette Score suggests that customers were grouped more clearly, with better separation between clusters.

However, I would still review the business meaning of each cluster before making a final decision. In real business use, clustering should not be selected by metrics only. The best method should also create segments that are understandable and useful for marketing, stock planning, and customer relationship management.
