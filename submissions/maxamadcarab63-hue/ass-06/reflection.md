Wholesale Customer Segmentation Using Clustering Algorithms
1. What I Implemented

In this project, I implemented a customer segmentation model for a wholesale distributor using machine learning clustering techniques. The main objective was to group wholesale clients based on their purchasing behavior and identify meaningful customer segments.

I used the Wholesale Customers dataset and selected six spending-related features for clustering:

Fresh
Milk
Grocery
Frozen
Detergents_Paper
Delicassen

The variables Channel and Region were excluded because they describe customer categories rather than purchasing behavior. Including them could influence the clustering results and prevent the model from discovering natural patterns based only on customer spending.

Before applying clustering, I handled extreme values using the Interquartile Range (IQR) method. Extreme spending values were capped to reduce the effect of outliers. After that, I standardized the six spending features using StandardScaler so that all variables had equal importance during the clustering process.

I applied the K-Means clustering algorithm with five clusters (K=5). The Elbow Method was used to examine the Sum of Squared Errors (SSE), and clustering quality was evaluated using the Silhouette Score and Davies–Bouldin Index.

2. Segment Interpretation

The K-Means algorithm divided wholesale clients into five groups based on their purchasing patterns. Each cluster represents customers with similar spending behaviors.

Cluster Example 1: Fresh and Milk Focused Customers

This cluster contains customers with high spending on Fresh and Milk products. These customers are likely restaurants, hotels, cafes, or food service businesses because they require large amounts of fresh and dairy products.

Business Action:

The distributor could provide customized offers for fresh products, create bulk purchase discounts, and improve delivery services for perishable goods.

Cluster Example 2: Grocery and Detergents_Paper Focused Customers

This cluster represents customers with higher spending on Grocery and Detergents_Paper products. They are likely supermarkets, grocery stores, and retail businesses that sell packaged food and household products.

Business Action:

The distributor could create promotional packages that combine grocery and household products. They could also introduce loyalty programs for frequent retail buyers.

Cluster Example 3: Balanced Purchasing Customers

This cluster includes customers with relatively balanced spending across multiple product categories, including Fresh, Grocery, Frozen, and Delicassen.

These customers may represent businesses with diverse product requirements, such as large retailers or institutions.

Business Action:

The distributor could provide personalized product recommendations and flexible ordering options based on their broad purchasing needs.

3. Understanding K-Means

K-Means is an unsupervised machine learning algorithm used to divide data points into groups called clusters. The main idea of K-Means is to find groups of similar observations based on their characteristics.

The algorithm requires selecting a value called K, which represents the number of clusters. In my project, I selected K=5, meaning the algorithm created five customer segments.

K-Means works through an iterative process:

Initialize centroids:
The algorithm randomly selects K initial cluster centers called centroids.
Assign data points:
Each customer is assigned to the nearest centroid based on distance.
Update centroids:
The algorithm calculates new centroids by finding the average position of all points assigned to each cluster.
Repeat the process:
The assign-and-update process continues until the centroids stop changing significantly.

The final result is a set of clusters where customers inside the same group have similar purchasing patterns.

4. My Second Clustering Algorithm: DBSCAN

The second clustering algorithm I selected was DBSCAN (Density-Based Spatial Clustering of Applications with Noise).

I selected DBSCAN because it uses a different clustering approach compared with K-Means. While K-Means creates clusters based on distance from centroids, DBSCAN identifies clusters based on the density of data points. This makes it useful for finding irregularly shaped groups and detecting unusual customers.

How DBSCAN Works

DBSCAN uses two main parameters:

Epsilon (ε): Defines the neighborhood distance around each point.
Minimum Points (MinPts): Defines the minimum number of nearby points required to form a dense region.

The algorithm identifies dense areas as clusters and labels isolated points as noise or outliers.

Advantage

One major advantage of DBSCAN is that it does not require the number of clusters to be specified in advance. It can also identify outliers automatically.

Limitation

A limitation of DBSCAN is that choosing suitable values for epsilon and minimum points can be difficult. It may also perform poorly when clusters have different densities.

Silhouette Score Comparison

The Silhouette Score measures how well-separated and compact clusters are. A higher score indicates better clustering quality.

In my experiment, I compared the Silhouette Score of DBSCAN with K-Means. The algorithm with the higher Silhouette Score produced better-separated clusters for this dataset. If K-Means achieved a higher score, it suggests that wholesale purchasing behavior is better represented by compact, centroid-based groups. If DBSCAN achieved a higher score, it indicates that density-based grouping captured customer patterns more effectively.

5. My Findings and Recommendation

After implementing and comparing clustering approaches, I would recommend K-Means for this wholesale customer segmentation task. The main reason is that wholesale purchasing behavior can naturally be represented through spending levels across product categories. K-Means works well because it creates clear customer groups based on average spending patterns.

Additionally, K-Means is simple, fast, and easy for business managers to understand. The cluster centers provide direct information about what each customer group purchases most, allowing the distributor to design targeted marketing strategies.

Although DBSCAN provides useful advantages, such as detecting outliers and not requiring the number of clusters beforehand, it may not be the best choice for this dataset because customer spending patterns are likely to form relatively compact groups rather than irregular density-based clusters.

Overall, K-Means provides more interpretable segments for the wholesale distributor. The identified clusters can support better decisions in marketing, inventory planning, customer relationship management, and personalized business strategies.