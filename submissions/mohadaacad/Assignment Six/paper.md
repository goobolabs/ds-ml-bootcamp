# Assignment 6 – Clustering (Part A: Theory)

# Machine Learning Clustering: Theory and Applications

## Introduction to Unsupervised Learning and Clustering

### What is Unsupervised Learning?

Unsupervised learning is a type of Machine Learning where the data does not contain target labels. Instead of predicting a known answer, the algorithm analyzes the data and automatically discovers hidden patterns or groups. The goal is to identify similarities among observations without being told the correct output.

Clustering is one of the most common unsupervised learning techniques. It divides similar data points into groups called **clusters**. Items within the same cluster are more similar to each other than to items in other clusters. Unlike supervised learning, clustering does not require a target variable.

### Difference Between Unsupervised Learning and Supervised Learning

Supervised learning uses labeled data to predict known outcomes. It includes both regression and classification.

* **Regression** predicts continuous numerical values such as house prices or temperatures.
* **Classification** predicts categories such as Approved/Rejected or Spam/Not Spam.
* **Clustering** does not predict labels. Instead, it discovers natural groups in the data based on similarity.

For example, predicting whether a loan application will be approved is a supervised learning problem because the correct answers already exist. Grouping wholesale customers based on their purchasing behavior is an unsupervised learning problem because no predefined groups are available.

### Real-World Examples

**Clustering Example**

A retail company groups customers according to their purchasing behavior. Customers who buy similar products frequently are placed into the same cluster. The company then creates personalized marketing campaigns for each customer group.

**Supervised Learning Example**

A bank predicts whether a customer will be approved for a loan using features such as income, credit score, employment years, and loan amount.

---

# Clustering Algorithms

## K-Means Clustering

### Basic Idea

K-Means is a clustering algorithm that divides data into **k** clusters. It begins by selecting the number of clusters, then randomly initializes cluster centers called **centroids**. Each data point is assigned to its nearest centroid. The centroids are updated by calculating the average position of the assigned points, and the process repeats until the centroids no longer change significantly.

### Real-World Use Case

A wholesale distributor can group customers according to their annual spending on products such as Fresh, Milk, Grocery, Frozen, Detergents_Paper, and Delicatessen. Each group represents customers with similar purchasing habits.

### Advantages

* Simple and easy to understand.
* Fast on medium and large datasets.
* Works well with numerical features.
* Produces clear customer segments.

### Limitations

* The number of clusters (**k**) must be selected before training.
* Sensitive to outliers.
* Requires scaled data for better performance.
* Does not perform well with irregularly shaped clusters.

---

## Hierarchical Clustering

### Basic Idea

Hierarchical Clustering builds clusters step by step instead of choosing all clusters at once. It begins by treating every data point as its own cluster. The closest clusters are merged repeatedly until all observations belong to one hierarchy. The results are displayed as a dendrogram, which helps decide the number of clusters.

### Real-World Use Case

A marketing company may use Hierarchical Clustering to group customers based on purchasing behavior and then analyze the dendrogram to identify natural customer segments.

### Advantages

* Does not require choosing the number of clusters before training.
* Easy to visualize with a dendrogram.
* Can discover natural relationships among clusters.

### Limitations

* Computationally expensive for large datasets.
* Sensitive to noise and outliers.
* Once clusters are merged, the decision cannot be reversed.

---

## DBSCAN

### Basic Idea

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) groups observations according to data density instead of centroids. Areas with many nearby points become clusters, while isolated observations are identified as noise or outliers.

### Real-World Use Case

Banks can use DBSCAN to detect unusual financial transactions. Transactions that do not belong to any dense cluster may indicate fraudulent activity.

### Advantages

* Does not require choosing the number of clusters beforehand.
* Can identify outliers automatically.
* Works well for clusters with irregular shapes.

### Limitations

* Choosing suitable parameter values can be difficult.
* Performance decreases when data density varies significantly.
* Less effective for very high-dimensional datasets.

---

# Clustering Metrics

Since clustering has no correct labels, special evaluation metrics are used to measure cluster quality.

## Elbow Method (SSE)

The Elbow Method helps determine a suitable number of clusters (**k**) for K-Means. The algorithm is trained using different values of **k**, and the **Sum of Squared Errors (SSE)** is calculated for each one. As **k** increases, SSE decreases. The best choice is usually where the decrease becomes much smaller, forming an "elbow" in the graph.

---

## Silhouette Score

The Silhouette Score measures how well data points fit within their assigned clusters compared to neighboring clusters.

Its values range from **-1 to +1**.

* **+1** indicates well-separated clusters.
* **0** indicates overlapping clusters.
* **Negative values** indicate poor cluster assignments.

Higher values indicate better clustering performance.

---

## Davies–Bouldin Index

The Davies–Bouldin Index measures the similarity between clusters.

A lower value indicates better separation and more compact clusters. Unlike the Silhouette Score, smaller values are preferred.

---

## Comparison of Clustering Metrics

| Metric               | What It Measures                 | Good Value        |
| -------------------- | -------------------------------- | ----------------- |
| Elbow Method (SSE)   | Cluster compactness as k changes | Clear elbow point |
| Silhouette Score     | Cluster separation and cohesion  | Close to +1       |
| Davies–Bouldin Index | Similarity between clusters      | Lower value       |

---

# Choosing *k* and Interpreting Customer Segments

## How Do We Choose the Number of Clusters?

The Elbow Method is commonly used to select the value of **k**. We train K-Means using several values of **k** and compare the SSE values. The point where the improvement begins to slow down is selected as the most appropriate number of clusters.

---

## Interpreting Wholesale Customer Segments

If one cluster has **high Fresh and Milk spending**, the customers may represent hotels, restaurants, or businesses that regularly purchase fresh food products.

If another cluster has **high Grocery and Detergents_Paper spending**, those customers are more likely to be supermarkets, retail stores, or wholesalers that purchase packaged goods and cleaning supplies in large quantities.

Understanding these purchasing patterns helps businesses design targeted marketing strategies, discounts, and inventory planning.

---

## Why Are Channel and Region Excluded?

The objective of this project is to group customers according to their **spending behavior**. Channel and Region describe customer information rather than purchasing amounts.

Including these columns could influence the clustering process and reduce the ability of the algorithm to discover natural spending patterns. Therefore, only the six annual spending variables are used for clustering, while Channel and Region remain available for interpreting the final clusters.

---

# Real-World Case Study

## Customer Segmentation Using K-Means in Retail

Many retail companies use K-Means clustering to improve customer segmentation. One common approach is to group customers based on purchasing history, spending frequency, and transaction amounts.

The goal is to identify customers with similar buying behavior so that businesses can create personalized marketing campaigns and improve customer satisfaction.

The dataset typically contains customer purchase information such as annual spending, product categories, purchase frequency, and transaction value. K-Means clustering is applied to these features after scaling the data.

The results often identify several customer groups, including high-value customers, frequent shoppers, occasional buyers, and low-spending customers. Businesses use these insights to offer targeted promotions, loyalty programs, and personalized product recommendations, leading to improved sales and stronger customer relationships.

---

# References

1. Han, J., Kamber, M., & Pei, J. (2012). *Data Mining: Concepts and Techniques* (3rd ed.). Morgan Kaufmann.

2. Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* (3rd ed.). O'Reilly Media.

3. Pedregosa, F., et al. (2011). *Scikit-learn: Machine Learning in Python*. Journal of Machine Learning Research, 12, 2825–2830.

4. UCI Machine Learning Repository. Wholesale Customers Dataset.
