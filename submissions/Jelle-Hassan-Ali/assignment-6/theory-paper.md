Part A — Theory
Introduction to Unsupervised Learning and Clustering
Introduction to Unsupervised Learning

Unsupervised Learning is a branch of Machine Learning where algorithms learn patterns and structures from data without using labeled outputs. Unlike supervised learning, the dataset does not contain a target variable or predefined answers. The main goal of unsupervised learning is to discover hidden relationships, groups, or patterns within the data.

Clustering is one of the most common techniques in unsupervised learning. It groups similar data points together based on their characteristics. These groups are called clusters, and they help organizations understand patterns that may not be obvious from raw data.

For example, in a business environment, a company can use clustering to divide customers into different groups based on purchasing behavior. A retailer may discover groups such as high-value customers, occasional buyers, or customers interested in specific product categories.

Unsupervised learning is different from supervised learning methods such as regression and classification.

Regression is a supervised learning technique used to predict continuous numerical values. For example, predicting house prices based on size, location, and other features.

Classification is also supervised learning, but it predicts categories or labels. For example, predicting whether an email is spam or not spam.

The main difference is that regression and classification require labeled training data, while unsupervised learning works with unlabeled data and tries to discover hidden patterns.

Clustering Algorithms
K-Means Clustering

K-Means is one of the most popular clustering algorithms used for grouping similar data points.

The main idea behind K-Means is to divide data into a predefined number of clusters (k). Each cluster has a center point called a centroid. The algorithm works by assigning each data point to the nearest centroid and then updating the centroid based on the average position of the assigned points.

The process continues through repeated assign-and-update steps until the clusters become stable.

Real-world Use Case:

A supermarket can use K-Means clustering to segment customers based on their purchasing behavior. Customers can be grouped into categories such as frequent buyers, premium customers, or low-spending customers.

Advantages:
Simple and easy to understand.
Efficient for large datasets.
Produces clear cluster centers that are easy to interpret.
Limitations:
The number of clusters (k) must be selected before training.
Sensitive to outliers.
Performance depends on the initial centroid selection.
Hierarchical Clustering

Hierarchical Clustering creates clusters by building a hierarchy of groups. Unlike K-Means, it does not require choosing cluster centers.

There are two main approaches:

Agglomerative Clustering: Starts with each data point as an individual cluster and gradually merges similar clusters.
Divisive Clustering: Starts with one large cluster and splits it into smaller groups.

In this project, Agglomerative Clustering was used as the second algorithm for comparison with K-Means.

Real-world Use Case:

Companies can use hierarchical clustering to analyze customer relationships and identify groups of customers with similar behaviors.

Advantages:
Does not require random centroid initialization.
Can show relationships between different groups.
Useful for exploratory analysis.
Limitations:
Computationally expensive for very large datasets.
Sensitive to the distance measurement method.
Choosing the final number of clusters can be difficult.
DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

DBSCAN is a density-based clustering algorithm that groups data points based on areas of high density. Unlike K-Means, it does not require specifying the number of clusters in advance.

DBSCAN uses two main parameters:

Epsilon (ε): Defines the maximum distance between neighboring points.
Minimum Points: Defines the minimum number of points required to form a dense region.

Points that do not belong to any dense region are considered noise or outliers.

Real-world Use Case:

DBSCAN can be used in geographic data analysis to identify locations with high activity, such as detecting customer locations or unusual patterns in transportation data.

Advantages:
Can identify clusters of different shapes.
Automatically detects noise and outliers.
Does not require selecting the number of clusters beforehand.
Limitations:
Choosing suitable parameters can be difficult.
Performs poorly when clusters have different densities.
Less effective in high-dimensional datasets.
Clustering Metrics
Elbow Method (Sum of Squared Errors - SSE)

The Elbow Method is commonly used to determine the appropriate number of clusters for K-Means.

It measures the Sum of Squared Errors (SSE), which represents the total distance between each data point and its assigned cluster centroid.

As the number of clusters increases, SSE decreases because clusters become smaller. The goal is to find the point where adding more clusters provides only a small improvement. This point is called the elbow.

Silhouette Score

The Silhouette Score measures how well-separated and compact the clusters are.

It considers:

How close a data point is to points in the same cluster.
How far it is from points in other clusters.

The score ranges from -1 to 1.

Interpretation:

Close to 1: Strong and well-separated clusters.
Around 0: Overlapping clusters.
Negative values: Incorrect clustering.

A higher Silhouette Score indicates better clustering quality.

Davies-Bouldin Index

The Davies-Bouldin Index measures the similarity between clusters by comparing cluster distance and cluster size.

A lower value indicates better clustering because clusters are more separated and compact.

Unlike Silhouette Score, where higher is better, the Davies-Bouldin Index should be minimized.

Comparison of Clustering Metrics
Metric	What it Measures	Good Value
Elbow Method (SSE)	Measures total distance between points and cluster centers	The point where SSE reduction slows down
Silhouette Score	Measures cluster separation and similarity	Higher values closer to 1
Davies-Bouldin Index	Measures similarity between clusters	Lower values closer to 0
Choosing k and Interpreting Segments

Choosing the correct number of clusters is an important step in K-Means clustering.

One common approach is the Elbow Method. Different values of k are tested, and the SSE values are compared. The best choice is usually where the decrease in SSE starts becoming smaller.

In the wholesale customer segmentation project, the Elbow Method showed that k = 5 provided a good balance between model simplicity and clustering quality.

Cluster interpretation is important because clustering results should provide business meaning.

For example:

A cluster with high Fresh and Milk spending represents customers who purchase large amounts of fresh products and dairy items. These customers may include restaurants, hotels, or businesses that require fresh supplies regularly.

A cluster with high Grocery and Detergents_Paper spending represents customers focused on supermarket-style products and household supplies. These customers may benefit from promotions involving grocery packages and household products.

Channel and Region were excluded from clustering features because they are categorical business labels rather than customer purchasing behaviors.

Including these features could force the algorithm to create clusters based on location or customer type instead of actual spending patterns. The goal of this project was to discover groups based on purchasing behavior.

Real-World Case Study: Customer Segmentation Using Clustering

One real-world example of clustering in business is customer segmentation used by retail companies to improve marketing strategies.

A common application is using customer transaction data to identify different customer groups based on purchasing habits.

In these projects, companies usually use data such as:

Purchase frequency
Total spending amount
Product categories purchased
Customer demographics

Clustering algorithms such as K-Means are often applied to divide customers into meaningful groups.

The goal is to understand customer behavior and create personalized strategies.

The results can help businesses:

Provide targeted promotions.
Improve customer loyalty programs.
Optimize inventory planning.
Identify valuable customer segments.

For example, a retail company may discover a group of high-value customers who purchase frequently and spend more money. The company can provide special offers to retain these customers.

References
Scikit-learn Documentation — Clustering Algorithms
https://scikit-learn.org/stable/modules/clustering.html
Han, J., Kamber, M., & Pei, J. (2012). Data Mining: Concepts and Techniques.
James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). An Introduction to Statistical Learning.
MacQueen, J. (1967). Some Methods for Classification and Analysis of Multivariate Observations.