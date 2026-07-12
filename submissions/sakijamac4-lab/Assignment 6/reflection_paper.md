# reflection_paper.md —

## 1. What did you implemented?

In this project, I segmented wholesale customers using two clustering algorithms: **K-Means** and **Agglomerative Clustering**. I used the six spending features (**Fresh, Milk, Grocery, Frozen, Detergents_Paper, and Delicassen**) because they reflect how customers spend on different product categories. I did not include **Channel** and **Region** since the goal was to group customers based on their purchasing behavior rather than their business type or location.

Before applying the clustering algorithms, I reduced the impact of outliers using IQR capping and standardized the data with **StandardScaler** so that all features were on the same scale. I then applied **K-Means** to create customer segments and used **Agglomerative Clustering** on the same dataset to compare the results.

By comparing both methods, I was able to identify groups of customers with similar spending patterns and evaluate how well each algorithm separated the customer segments. This gave me a better understanding of customer behavior and showed how different clustering techniques can be used for the same segmentation task.


## 2. Segment Interpretation


Cluster 3 — Fresh-Focused Customers:
This group spends heavily on fresh products such as meat and vegetables (Fresh = $22,347), but spends very little on Grocery ($3,969) and Detergents_Paper ($583). This suggests that this group likely consists of hotels or restaurants that require fresh products on a daily basis.
Business action: The distributor could send this group specialized offers on fresh products such as vegetables and other perishables, or offer a discounted price if they purchase in larger quantities.

Cluster 4 — Grocery-Focused Customers:
This group spends heavily on Grocery ($18,350) and Detergents_Paper ($7,780), but spends very little on Fresh products ($4,917). This suggests that this group consists of retail stores selling storable products such as packaged food and household cleaning supplies.
Business action: The distributor could send this group updates on new arrivals in Grocery and Detergents product lines, or offer special discounts when they purchase in large quantities.

Cluster 2 — High-Volume Customers:
This group spends heavily across all product categories (Fresh $17,462, Milk $13,806, Grocery $17,524). This suggests that this group consists of large customers such as major hotels or food companies that purchase across all product types.
Business action: The distributor could offer this group a dedicated VIP plan, such as free delivery or exclusive pricing, since they are the highest-spending customers.


## 3. Understanding K-Means

K-Means is an unsupervised machine learning algorithm and the most well-known clustering method. It is used to divide data into groups (clusters) based on the similarity of the data points. First, we choose the number of clusters (k) — for example, k=5 means 5 groups. The algorithm then randomly places a centroid (center point) for each cluster.
The assign step involves assigning each data point to the nearest centroid. Once all data points have been assigned, the centroids are recalculated as the mean of all points in each cluster (the update step). These two steps (assign and update) are repeated continuously until the centroids stop changing or the model reaches the best solution. Finally, the data is divided into groups whose members share similar characteristics.

## 4. Your Second Algorithm — Agglomerative Clustering

I chose Agglomerative Clustering (Hierarchical Clustering) as my second clustering algorithm.
Agglomerative Clustering initially treats each customer as its own individual cluster. It then gradually merges the most similar customers together based on the distance between them, until the desired number of clusters is reached.
This algorithm is well-suited for wholesale customer segmentation because it can group customers with similar purchasing behavior together. In this project, customers were segmented based on their annual spending across six product categories: Fresh, Milk, Grocery, Frozen, Detergents_Paper, and Delicassen.
I chose this algorithm because it provides a different clustering approach compared to K-Means. While K-Means groups customers based on cluster centroids, Agglomerative Clustering builds groups by analyzing the relationships and similarities between customers. This helps produce meaningful customer segments and allows for a direct comparison with K-Means results.
Advantage: Unlike K-Means, Agglomerative Clustering does not require the number of clusters to be specified in advance. The decision can be made from a Dendrogram — for example, you can observe that the data naturally splits into 3 or 4 groups.
Limitation: It becomes very slow when the dataset is large, because it continuously calculates the distance between all data points and merges the closest ones. For example: 100 customers → works well. 100,000 customers → can become very slow.
Silhouette Score Comparison:

K-Means: 0.283
Agglomerative Clustering: 0.218

K-Means produced better-separated clusters on this dataset, as shown by its higher Silhouette Score (0.283 vs 0.218).
Research Source: IBM — Hierarchical Clustering explanation.


## 5. Your Findings

For the wholesale customers dataset, I would recommend K-Means Clustering because it outperforms Agglomerative Clustering in two key areas: clustering quality and suitability for the dataset size.
Silhouette Score Comparison:

K-Means → Silhouette Score = 0.283
Agglomerative Clustering → Silhouette Score = 0.218

The Silhouette Score measures how well-separated the clusters are and how tightly grouped the data points within each cluster are. A higher value is better. Therefore, K-Means (0.283) produced slightly better-separated clusters than Agglomerative Clustering (0.218).
Our dataset contains 440 customers, which is a medium-sized dataset. K-Means is well-suited for medium to large datasets containing large amounts of numeric data, such as customer spending figures. Agglomerative Clustering, on the other hand, is better suited for small datasets or when a detailed understanding of the relationships within the data is needed. Since 440 rows is a medium-sized dataset, K-Means is more appropriate because it is simple to understand, the number of clusters (k) can be chosen using the Elbow Method, it trains quickly, and its results are easy to explain to the business.
However, if the dataset were small, I would choose Agglomerative Clustering instead, because it works well with small datasets by carefully analyzing the distance between each data point to understand their relationships. For example, with 60 or 140 customers, Agglomerative Clustering would be able to clearly show how similar the customers are to one another.


