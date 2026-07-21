Assignment 6 Reflection: Wholesale Customer Segmentation
What did I implement?

In this assignment, I implemented an unsupervised machine learning solution for wholesale customer segmentation using clustering techniques.

The goal was to group customers based on their purchasing behavior using six spending features:

Fresh
Milk
Grocery
Frozen
Detergents_Paper
Delicassen

First, I performed data preprocessing by selecting the relevant spending features, handling extreme values using IQR capping, and applying StandardScaler to normalize the data.

After preprocessing, I used the Elbow Method to determine the appropriate number of clusters. Based on the elbow curve and assignment requirements, I selected k = 5 and trained a K-Means clustering model.

The K-Means model was evaluated using:

Silhouette Score: 0.283
Davies-Bouldin Index: 1.270

I also implemented a second clustering algorithm, Agglomerative Clustering, and compared its performance with K-Means.

The Silhouette Score comparison was:

K-Means: 0.283
Agglomerative Clustering: 0.218

Based on these results, K-Means produced better-separated clusters for this dataset.

Segment Interpretation

The K-Means algorithm created five customer segments with different purchasing behaviors.

Cluster 0: Balanced Retail Customers

Cluster 0 has moderate spending across several categories:

Fresh: 9,202
Milk: 6,833
Grocery: 9,104
Frozen: 1,326
Detergents_Paper: 3,280
Delicassen: 1,871

This cluster represents customers with balanced purchasing patterns. They buy different product categories without depending heavily on one specific category.

Business action:

The distributor can provide general product bundles and loyalty programs because these customers have diverse purchasing needs.

Cluster 1: Low Spending Customers

Cluster 1 shows relatively lower spending compared to other clusters:

Fresh: 8,376
Milk: 2,150
Grocery: 3,160
Frozen: 1,646
Detergents_Paper: 779
Delicassen: 674

These customers appear to be smaller buyers with limited purchasing volume.

Business action:

The distributor can offer small-volume discounts, introductory promotions, and encourage these customers to increase their order frequency.

Cluster 2: High Volume Wholesale Customers

Cluster 2 has high spending in almost all categories:

Fresh: 17,461
Milk: 13,805
Grocery: 17,524
Frozen: 4,120
Detergents_Paper: 5,460
Delicassen: 3,583

This cluster represents large wholesale buyers with strong demand across multiple product categories.

Business action:

The distributor should prioritize these customers by providing bulk discounts, dedicated support, and reliable inventory availability.

Cluster 3: Fresh Product Buyers

Cluster 3 has the highest Fresh spending:

Fresh: 22,346
Milk: 3,409
Grocery: 3,969
Frozen: 5,819
Detergents_Paper: 583
Delicassen: 1,566

These customers mainly focus on fresh products and have lower demand for packaged goods.

Business action:

The distributor should focus on maintaining fresh product quality, delivery speed, and availability for this customer segment.

Cluster 4: Grocery and Detergent Focused Customers

Cluster 4 has high spending in:

Grocery: 18,350
Detergents_Paper: 7,780
Milk: 10,768

This cluster represents customers who strongly purchase grocery and household-related products.

Business action:

The distributor can create targeted promotions for grocery packages and household product bundles.

Understanding K-Means

K-Means is an unsupervised machine learning algorithm used to divide data points into groups called clusters.

The algorithm requires choosing the number of clusters, represented by k. In this project, five clusters were selected.

The algorithm works through an iterative process:

Randomly initialize cluster centroids.
Calculate the distance between customers and centroids.
Assign each customer to the nearest centroid.
Update centroids based on the average position of assigned customers.
Repeat the process until the clusters become stable.

The purpose of K-Means is to minimize the distance between customers within the same cluster while maximizing differences between different clusters.

Second Algorithm: Agglomerative Clustering

For the second clustering approach, I selected Agglomerative Clustering (Hierarchical Clustering).

This algorithm starts by considering each data point as its own cluster. It then repeatedly merges the most similar clusters until the required number of clusters is reached.

I selected this algorithm because it provides a different approach from K-Means. Instead of using centroids, it creates clusters based on similarity relationships between data points.

Advantage:

Agglomerative Clustering does not require random centroid initialization and can reveal hierarchical relationships between data points.

Limitation:

It can become computationally expensive when applied to very large datasets.

The comparison results were:

Algorithm	Silhouette Score
K-Means	0.283
Agglomerative Clustering	0.218

K-Means achieved a higher Silhouette Score, meaning it produced better-separated customer groups for this dataset.

Findings and Recommendation

After implementing and comparing both clustering algorithms, K-Means provided the better solution for wholesale customer segmentation.

Although the Silhouette Score of 0.283 is not extremely high, it is acceptable for this type of real-world customer dataset where purchasing behaviors naturally overlap.

K-Means was selected as the recommended approach because it is simple, efficient, easy to interpret, and provides clear cluster centers that help businesses understand customer purchasing patterns.

The segmentation results can help the distributor create targeted marketing strategies, improve inventory planning, and provide customized services for different customer groups.

Agglomerative Clustering was useful for comparison and provided another perspective on customer similarity, but K-Means achieved better clustering performance based on the evaluation results.