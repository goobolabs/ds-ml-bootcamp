# Assignment Six: Clustering —  (Part A)

# Introduction to Unsupervised Learning and Clustering

## What is Unsupervised Learning?

Unsupervised learning is a type of machine learning in which algorithms learn patterns from data without using labeled outputs. Unlike supervised learning, there are no predefined answers or target values. Instead, the algorithm discovers hidden structures, similarities, and relationships among the data points.

One of the most common tasks in unsupervised learning is **clustering**, where similar observations are grouped together based on their characteristics. Clustering helps organizations better understand their data and identify meaningful patterns that may not be obvious through manual analysis.

## Difference Between Unsupervised Learning, Regression, and Classification

Regression and classification are supervised learning techniques because they require labeled data during training.

Regression predicts continuous numerical values, such as house prices, sales revenue, or temperatures.

Classification predicts categories or classes, such as whether an email is spam or not spam, or whether a customer will purchase a product.

In contrast, unsupervised learning does not use labels. Instead, it groups similar data together or identifies hidden structures within the dataset.

## Real-Life Examples

A real-world example of clustering is customer segmentation in retail. A supermarket can group customers according to their purchasing behavior without knowing the groups beforehand. These groups help the business create targeted marketing campaigns.

An example of supervised learning is predicting whether a bank customer will default on a loan using historical customer data where the default status is already known.

# Clustering Algorithms

## K-Means

K-Means is one of the most widely used clustering algorithms. It divides data into a predefined number of clusters (k). The algorithm begins by selecting k centroids. Each data point is assigned to the nearest centroid, after which the centroids are recalculated using the average position of all points in each cluster. This assignment-and-update process continues until the clusters stabilize.

A common use case for K-Means is customer segmentation in retail and marketing.

**Advantages**

* Simple to understand and implement.
* Fast on large datasets.
* Produces compact clusters.

**Limitations**

* The number of clusters must be chosen before training.
* Sensitive to outliers.
* Works best with roughly spherical clusters.

## Hierarchical Clustering

Hierarchical Clustering creates a hierarchy of clusters instead of producing all clusters at once. In agglomerative clustering, each data point starts as its own cluster, and the closest clusters are repeatedly merged until the desired number of clusters remains.

It is commonly used in biology for grouping similar genes and in marketing for customer analysis.

**Advantages**

* Does not require random centroid initialization.
* Produces a dendrogram that helps visualize relationships.
* Can reveal hierarchical structures.

**Limitations**

* Computationally expensive on large datasets.
* Sensitive to the distance metric and linkage method.

## DBSCAN

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) groups data points according to density rather than distance to centroids. Areas with many nearby points become clusters, while isolated points are treated as noise.

DBSCAN is widely used in geographical analysis, fraud detection, and anomaly detection.

**Advantages**

* Can detect clusters with irregular shapes.
* Automatically identifies outliers.
* Does not require specifying the number of clusters.

**Limitations**

* Choosing appropriate parameter values can be difficult.
* Performance decreases when data density varies significantly.

# Clustering Metrics

## Elbow Method (SSE)

The Elbow Method uses the Sum of Squared Errors (SSE) to evaluate clustering quality. As the number of clusters increases, SSE decreases. The best value of k is usually found where the graph forms an "elbow," indicating that adding more clusters provides only a small improvement.

## Silhouette Score

The Silhouette Score measures how well each data point fits within its own cluster compared with other clusters. Scores range from -1 to 1. Values closer to 1 indicate better-separated and more compact clusters.

## Davies–Bouldin Index

The Davies–Bouldin Index measures the average similarity between clusters. Lower values indicate better clustering because clusters are compact and well separated.

| Metric               | What It Measures                | Good Value        |
| -------------------- | ------------------------------- | ----------------- |
| Elbow Method (SSE)   | Total within-cluster error      | Clear elbow point |
| Silhouette Score     | Cluster separation and cohesion | Close to 1        |
| Davies–Bouldin Index | Similarity between clusters     | Close to 0        |

# Choosing k and Interpreting Segments

## Choosing the Number of Clusters

The number of clusters for K-Means is commonly selected using the Elbow Method and confirmed using the Silhouette Score. Domain knowledge and business objectives should also be considered when selecting the final value of k.

## Interpreting Customer Segments

Customers with high spending on **Fresh** and **Milk** may represent restaurants, hotels, or food-service businesses that purchase fresh ingredients regularly.

Customers with high spending on **Grocery** and **Detergents_Paper** are more likely to be supermarkets, convenience stores, or retailers that frequently stock household products.

Understanding these purchasing patterns allows distributors to develop personalized marketing strategies, pricing plans, and inventory management.

## Why Exclude Channel and Region?

Channel and Region are categorical variables that describe customer characteristics rather than purchasing behavior. The purpose of clustering is to group customers based on spending habits. Including these variables could influence the clustering process and reduce the algorithm's ability to discover natural purchasing patterns.

# Real-World Case Study

A well-known application of clustering is customer segmentation in retail businesses. Companies analyze customer purchasing histories to identify groups with similar buying behaviors. Transaction data, including purchase frequency, spending amount, and product categories, are commonly used.

Many studies apply K-Means clustering because it is efficient and easy to interpret. The resulting customer segments help businesses personalize promotions, improve customer retention, optimize inventory, and increase sales. For example, high-value customers can receive loyalty rewards, while infrequent customers may receive targeted discounts to encourage additional purchases.

# References

* Aurélien Géron. *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*. O'Reilly Media.
* Christopher M. Bishop. *Pattern Recognition and Machine Learning*. Springer.
* Han, Kamber, and Pei. *Data Mining: Concepts and Techniques*. Morgan Kaufmann.
* Scikit-learn Documentation. https://scikit-learn.org/
