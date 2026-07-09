# Part A — Theory

## 1 Introduction to Unsupervised Learning and Clustering

What is Unsupervised Learning?
Unsupervised Learning is a type of Machine Learning that does not have labels (y or a correct output). The model is not given a predefined answer; instead, it explores the data on its own to find patterns and groups (clusters) where the data is similar.

How is it different from Supervised Learning?
Supervised Learning has labels or a target variable (y). This means the model is given both features and the correct label so that it can learn, and then predict on new data. Unsupervised Learning, on the other hand, has no labels or output. The model does not know the correct answer; instead, it groups the data into clusters or discovers hidden relationships within the data.

**Real-life example of Clustering (Unsupervised Learning):**
A wholesale distributor has data on its customers showing how much they spent annually on Fresh, Milk, Grocery, Frozen, and other products. There is no column indicating the type of customer. K-Means groups the customers based on their purchasing behavior, such as:

A group that mostly buys Fresh products.
A group that mostly buys Grocery products.
A group that spends moderately across all categories.


Real-life example of Classification (Supervised Learning):
Predicting whether a student will fail or pass an exam based on a labeled dataset that contains historical student data, where each record already has a known outcome (Failed or Passed).





## 2 Clustering Algorithms


1. K-Means Clustering
K-Means is the most well-known clustering algorithm. It divides data into K groups (clusters) using centroids (the center of each cluster).
How it works:

Choose the number of clusters (K).
Place initial centroids.
Assign each data point to the nearest centroid.
Move centroids to the mean of their assigned points.
Repeat until no further changes occur.

Real-world use case: A wholesale distributor wants to identify the types of customers it has based on what they purchase.
Advantages: Very fast; works well with large datasets; simple to understand and use; works well with numeric data.
Limitations: K must be chosen in advance; sensitive to outliers; data must be scaled before use; not suitable for clusters with irregular shapes.

2. Hierarchical Clustering
Hierarchical Clustering builds a tree called a Dendrogram to show the relationships between data points. Unlike K-Means, it does not start with a fixed number of clusters.
How it works (Agglomerative — most common):
Each data point starts as its own cluster. The two closest clusters are merged together. This merging continues until one large cluster is reached.
Real-world use case: A researcher wants to classify DNA types based on their similarity.
Advantages: No need to specify the number of clusters in advance; shows relationships between clusters; works well with small datasets.
Limitations: Slow on large datasets; uses a lot of memory; once clusters are merged, they cannot be separated again.

3. DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
DBSCAN groups data based on the density of points. If many points are close together, it forms a cluster. If a point is alone, it is labeled as Noise (Outlier).
How it works: DBSCAN uses two parameters:

eps → the maximum distance between two points to be considered neighbors.
min_samples → the minimum number of points needed to form a cluster.

Real-world use case: A bank uses DBSCAN to detect unusual transactions (Fraud).
Advantages: No need to specify the number of clusters; detects outliers effectively; can handle clusters of irregular shapes; not sensitive to outliers like K-Means.
Limitations: Choosing eps and min_samples is difficult; not suitable for datasets with varying density; can be slow on very large datasets.

Algorithm Comparison Table:
AlgorithmHow it worksBest forLimitationsK-MeansDivides data into K clusters using centroidsFast, large datasets, numeric dataK must be chosen, sensitive to outliers, data must be scaledHierarchicalBuilds a dendrogram showing data relationshipsNo K needed, small datasets, shows cluster relationshipsSlow, high memory, merges cannot be undoneDBSCANGroups data by density, identifies outliers as noiseNo K needed, irregular shapes, outlier detectionHard to tune eps and min_samples, varies with density

## 3 Clustering Metrics

Elbow Method (SSE)

Elbow Method (SSE) is a technique used to determine the optimal number of clusters (K) for K-Means Clustering.
It works by testing different values of K (such as 1, 2, 3, 4, 5) and calculating the SSE (Sum of Squared Errors) for each. SSE measures how close the data points are to the centroid of their cluster. A lower SSE means the data points within a cluster are more tightly grouped together.
When a graph of K vs SSE is plotted, the point where the graph bends like an elbow is selected. That point is usually the best number of clusters, because beyond it, the benefit gained by increasing K decreases significantly.

Silhouette Score

Silhouette Score is a metric used to evaluate the quality of clustering. It shows how well-separated the clusters are from one another and how tightly the data points within each cluster are grouped together. The Silhouette Score ranges from -1 to +1.

A value close to +1 indicates that the clusters are well-separated, and the data points within each cluster are very similar to one another.
A value close to 0 indicates that the clusters are overlapping or not clearly distinguished from each other.
A value below 0 (negative) indicates that some data points may have been assigned to the wrong cluster.



Davies–Bouldin Index (DBI)

The Davies–Bouldin Index (DBI) is a metric used to evaluate the quality of clustering. It looks at how similar the clusters are to one another and how far apart they are.
If the clusters are very close together or overlapping, the DBI increases, which indicates that the clustering is not good. If the clusters are well-separated from one another, and each cluster is tightly grouped internally, the DBI decreases.
In summary: the Davies–Bouldin Index measures how distinct the clusters are from each other. A lower value is better, because it indicates that the clusters are clearly separated and the clustering has good quality.

Comparison of Clustering Metrics
MetricWhat it MeasuresGood ValueElbow Method (SSE)Measures the total distance between the data points and their centroid, used to select the optimal K.Look for the point where the graph bends (the Elbow) — that point gives the best K.Silhouette ScoreMeasures how well-separated the clusters are and how tightly the data within each cluster is grouped.A value close to +1 is best.Davies–Bouldin Index (DBI)Measures how similar the clusters are to one another and how far apart they are.A lower value is best.



## 4 Choosing k and Interpreting Segments


### Choosing k and Interpreting Segments
1. How do you choose the number of clusters for K-Means?

In K-Means clustering, the number of clusters (k) must be selected before training the model. Choosing the correct value of k is important because too few clusters may combine different customer groups together, while too many clusters may create unnecessary groups.

One common method used to select the best value of k is the Elbow Method. This method measures the within-cluster variation (inertia) for different values of k and looks for the point where adding more clusters provides only a small improvement. This point is called the “elbow” and is usually chosen as the optimal number of clusters.

Another method is the Silhouette Score, which evaluates how well each data point fits within its cluster. A higher silhouette score indicates better-separated and more meaningful clusters.

In the wholesale distributor project, the optimal number of clusters can be selected by comparing these evaluation methods and choosing the value that creates clear and meaningful customer segments.

2. What does it mean when a cluster has high Fresh + Milk spend vs high Grocery + Detergents_Paper spend?

In the wholesale distributor project, different clusters represent customers with different purchasing behaviors.

A cluster with high Fresh and Milk spending represents customers who purchase a large amount of fresh products and dairy items. These customers are likely to be businesses such as restaurants, hotels, or food service companies because they require fresh ingredients regularly.

On the other hand, a cluster with high Grocery and Detergents_Paper spending represents customers who purchase more packaged goods and household products. These customers are more likely to be supermarkets, retail stores, or businesses that sell daily-use products.

Therefore, analyzing cluster spending patterns helps the company understand the type of customers in each group and create better sales and marketing strategies.

3. Why do we exclude Channel and Region from the clustering features?

Channel and Region are excluded from clustering features because they do not represent customer purchasing behavior.

The purpose of clustering is to discover groups based on what customers buy and how much they spend. Features such as Fresh, Milk, Grocery, Frozen, Detergents_Paper, and Delicassen provide information about customer spending patterns.

However, Channel and Region are already existing categories. Including them may cause the model to create clusters based on location or business type instead of actual purchasing behavior. This could reduce the quality of customer segmentation.

By excluding Channel and Region, the clustering model can focus on finding meaningful customer groups based on their spending habits.

Summary

K-Means clustering requires selecting an appropriate value of k using methods such as Elbow Method and Silhouette Score. In the wholesale distributor project, clusters help identify different customer purchasing patterns, such as customers focused on Fresh and Milk products or customers focused on Grocery and Detergents_Paper products. Channel and Region are excluded because the goal is to segment customers based on buying behavior rather than location or predefined categories.




## 5Real-World Case Study

### Real-World Case Study: Mall Customer Segmentation Using K-Means Clustering
Goal

This project was developed to understand customer behavior in a shopping mall and identify different types of customers based on their income and spending habits. The main goal was to divide customers into different groups (segments) so that the mall management could create targeted marketing strategies, personalized offers, and better customer services for each group.

For example, customers who spend more money can be identified as valuable customers, while customers with low spending behavior can be targeted with special promotions to encourage more purchases.

Data Used

The dataset contained information from 200 mall customers. It included the following features:

CustomerID: A unique identification number for each customer.
Gender: The gender of the customer (Male/Female).
Age: The age of the customer.
Annual Income (k$): The customer's yearly income measured in thousands of dollars.
Spending Score (1-100): A score that represents the customer's purchasing behavior and spending level.

For the clustering analysis, the main features used were:

Annual Income
Spending Score

These two features were selected because they clearly show the relationship between a customer's financial ability and their shopping behavior.

Clustering Method Applied

The project used K-Means Clustering, which is an unsupervised machine learning algorithm.

K-Means works by:

Finding similarities between customers based on their features.
Grouping customers with similar behaviors into the same cluster.
Assigning each customer to the cluster with the closest characteristics.

The Elbow Method was used to determine the optimal number of clusters. Based on the analysis, 5 clusters were selected as the most suitable number of customer groups.

Key Results and Insights

After applying K-Means Clustering, customers were divided into five different segments:

Cluster 1: High Income - High Spending
Customers have high annual income.
They spend a lot of money in the mall.
They are considered the most valuable customers (VIP customers).
The mall should provide special rewards and loyalty programs for them.
Cluster 2: High Income - Low Spending
Customers have high income.
However, their spending level is low.
The mall can attract them through personalized discounts and special offers.
Cluster 3: Low Income - High Spending
Customers have lower income.
But they have a high spending score.
They enjoy shopping and may respond well to affordable promotions.
Cluster 4: Low Income - Low Spending
Customers have both low income and low spending behavior.
They contribute less to sales.
The mall can use low-cost promotions to encourage their purchases.
Cluster 5: Medium Income - Medium Spending
Customers have average income and average spending habits.
They represent regular customers who need continuous engagement and good customer service.
Conclusion

This project demonstrated that K_Means Clustering is an effective technique for understanding customer differences and creating meaningful customer segments. By using clustering, the mall can avoid treating all customers in the same way and instead develop specific marketing strategies for each customer group.

The insights from this analysis can help increase sales, improve customer satisfaction, and make marketing campaigns more effective by targeting the right customers with the right offers.

References (APA 7th Edition)

Kaggle. (2018). Mall Customer Segmentation Data. Kaggle.
https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial

Han, J., Kamber, M., & Pei, J. (2012). Data Mining: Concepts and Techniques (3rd ed.). Morgan Kaufmann.