# Assignment Six: Clustering — Theory and Practice

## Part A – Theory

# 1. Introduction to Unsupervised Learning and Clustering

### What is Unsupervised Learning?

Unsupervised learning is a type of machine learning where algorithms analyze data without using labeled outputs. The model is not provided with the correct answers; instead, it identifies hidden patterns, similarities, and structures within the dataset. Clustering is one of the most common applications of unsupervised learning because it groups similar data points into meaningful clusters.

### How is it Different from Regression and Classification?

Regression and classification are supervised learning methods because they require labeled data. Regression predicts continuous numerical values, such as house prices or sales revenue. Classification predicts predefined categories, such as spam versus non-spam emails or loan approval decisions. In contrast, unsupervised learning works without target labels and focuses on discovering patterns rather than making predictions.

### Real-Life Examples

A common example of clustering is customer segmentation in a wholesale distribution company. Customers with similar purchasing behavior are grouped together so that businesses can provide personalized marketing strategies and improve customer satisfaction.

An example of supervised learning is loan approval prediction, where historical loan records are used to train a model that predicts whether future applicants should be approved or rejected.



# 2. Clustering Algorithms

## K-Means Clustering

K-Means is a partition-based clustering algorithm that divides data into a predefined number of clusters (k). The algorithm starts by selecting random centroids, assigns each data point to its nearest centroid, recalculates the centroids, and repeats the process until the cluster assignments become stable.

**Real-world use case:** Customer segmentation in retail businesses.

**Advantages**

* Simple and fast.
* Efficient for large datasets.
* Easy to understand and implement.

**Limitations**

* The number of clusters must be chosen in advance.
* Sensitive to outliers.
* Performance depends on centroid initialization.



## Hierarchical (Agglomerative) Clustering

Hierarchical clustering creates a hierarchy of clusters. Agglomerative clustering starts with each observation as its own cluster and gradually merges the closest clusters until the desired number of clusters is obtained.

**Real-world use case:** Customer segmentation, biological classification, and document organization.

**Advantages**

* Does not depend on random centroid initialization.
* Produces a dendrogram that helps visualize cluster relationships.
* Useful for understanding hierarchical structures.

**Limitations**

* Computationally expensive for large datasets.
* Sensitive to the distance metric and linkage method.



## DBSCAN

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) groups together points that are closely packed while identifying isolated points as noise or outliers.

**Real-world use case:** Fraud detection, geographic data analysis, and anomaly detection.

**Advantages**

* Detects clusters of arbitrary shapes.
* Automatically identifies outliers.
* Does not require specifying the number of clusters beforehand.

**Limitations**

* Choosing appropriate parameter values can be difficult.
* Performance decreases when data densities vary significantly.



# 3. Clustering Metrics

## Elbow Method (SSE)

The Elbow Method uses the Sum of Squared Errors (SSE) to evaluate clustering quality. As the number of clusters increases, SSE decreases. The optimal value of k is usually found at the "elbow" point, where the decrease in SSE begins to slow.

## Silhouette Score

The Silhouette Score measures how similar an observation is to its own cluster compared to other clusters. The score ranges from -1 to 1. Values close to 1 indicate well-separated clusters, values near 0 indicate overlapping clusters, and negative values indicate poor clustering.

## Davies–Bouldin Index

The Davies–Bouldin Index measures the average similarity between clusters. Lower values indicate better clustering because the clusters are more compact and better separated.

### Comparison Table

| Metric               | What it Measures                | Good Value                            |
| -------------------- | ------------------------------- | ------------------------------------- |
| Elbow Method (SSE)   | Total within-cluster error      | Lower values with a clear elbow point |
| Silhouette Score     | Cluster cohesion and separation | Close to 1                            |
| Davies–Bouldin Index | Cluster similarity              | Close to 0                            |



# 4. Choosing k and Interpreting Segments

### How do you choose the number of clusters for K-Means?

The number of clusters is commonly selected using the Elbow Method or the Silhouette Score. The Elbow Method identifies the point where adding more clusters no longer significantly reduces SSE, while the Silhouette Score evaluates how well the clusters are separated.

### What does a cluster with high Fresh and Milk spending indicate?

Customers with high spending on Fresh and Milk products are typically restaurants, hotels, or food service businesses that regularly purchase fresh food and dairy products in large quantities.

### What does a cluster with high Grocery and Detergents_Paper spending indicate?

Customers with high Grocery and Detergents_Paper spending are often supermarkets, retail stores, or convenience shops that purchase packaged food and household cleaning products in bulk.

### Why are Channel and Region excluded?

Channel and Region are excluded because they are existing categorical labels rather than purchasing behavior. Clustering should be performed only on spending features so that the algorithm groups customers based on their buying patterns instead of predefined categories.



# 5. Real-World Case Study

A well-known application of clustering is customer segmentation in retail businesses. Many retailers analyze customer purchasing behavior to understand different shopping patterns and improve marketing strategies.

The project collected customer purchase histories, including the amount spent on different product categories. K-Means clustering was applied to divide customers into groups with similar purchasing behaviors.

The results showed that some customers frequently purchased fresh food products, while others mainly bought grocery and household items. These insights enabled businesses to create targeted promotions, improve inventory management, and offer personalized recommendations, ultimately increasing customer satisfaction and sales.



# References

1. Han, J., Kamber, M., & Pei, J. (2012). *Data Mining: Concepts and Techniques* (3rd ed.). Morgan Kaufmann.

2. Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* (3rd ed.). O'Reilly Media.

