# Part A — Theory: Unsupervised Learning and Clustering

## Introduction

Machine Learning is a branch of Artificial Intelligence that enables computers to learn patterns from data without being explicitly programmed. Machine learning techniques are generally divided into two major categories: **supervised learning** and **unsupervised learning**. Supervised learning uses labeled data to predict known outcomes, while unsupervised learning discovers hidden structures and relationships in unlabeled data. One of the most widely used unsupervised learning techniques is **clustering**, which groups similar data points together based on their characteristics.

---

# 1. Introduction to Unsupervised Learning and Clustering

## What is Unsupervised Learning?

Unsupervised learning is a machine learning approach where algorithms analyze data without predefined labels or target values. Instead of predicting a known outcome, the algorithm identifies patterns, similarities, and structures within the dataset.

The primary goal of unsupervised learning is to organize data into meaningful groups or discover hidden relationships that may not be immediately visible.

Common tasks include:

* Clustering
* Dimensionality reduction
* Association rule mining
* Anomaly detection

---

## How is Unsupervised Learning Different from Regression and Classification?

Regression and classification are supervised learning techniques because they require labeled training data.

| Feature                | Unsupervised Learning    | Regression               | Classification       |
| ---------------------- | ------------------------ | ------------------------ | -------------------- |
| Uses labeled data      | No                       | Yes                      | Yes                  |
| Predicts target values | No                       | Yes (continuous values)  | Yes (categories)     |
| Main objective         | Discover hidden patterns | Predict numerical values | Predict class labels |
| Example                | Customer segmentation    | House price prediction   | Email spam detection |

Regression predicts continuous numerical values such as house prices or temperatures. Classification predicts discrete categories such as whether an email is spam or not. In contrast, unsupervised learning identifies natural groups in the data without knowing the correct answers beforehand.

---

## Real-Life Examples

### Clustering Example

A supermarket groups customers according to their purchasing behavior. Customers who frequently purchase fresh food may form one cluster, while customers buying cleaning products and packaged goods may form another. These groups help businesses create targeted marketing campaigns.

### Supervised Learning Example

A bank predicts whether a customer will default on a loan using historical customer records labeled as either "default" or "not default."

---

# 2. Clustering Algorithms

## K-Means Clustering

### Basic Idea

K-Means partitions data into **K clusters**. The algorithm randomly selects K centroids, assigns each data point to its nearest centroid, recalculates the centroid positions, and repeats the process until the clusters stabilize.

### Real-World Use Case

Retail companies use K-Means to segment customers based on purchasing behavior so that each customer group can receive personalized promotions.

### Advantages

* Easy to understand and implement.
* Fast on large datasets.
* Produces compact and well-separated clusters.

### Limitations

* Requires choosing K beforehand.
* Sensitive to outliers.
* Performs poorly on non-spherical clusters.

---

## Hierarchical Clustering

### Basic Idea

Hierarchical clustering builds a hierarchy of clusters using either:

* Agglomerative approach (bottom-up)
* Divisive approach (top-down)

The relationships between clusters are visualized using a dendrogram.

### Real-World Use Case

Biologists use hierarchical clustering to group genes with similar expression patterns.

### Advantages

* Does not require specifying the number of clusters initially.
* Produces an interpretable dendrogram.
* Useful for exploring data structure.

### Limitations

* Computationally expensive on large datasets.
* Difficult to update once clusters are formed.
* Sensitive to noise.

---

## DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

### Basic Idea

DBSCAN groups together points located in dense regions while labeling isolated points as noise or outliers. It uses two parameters:

* Epsilon (ε): neighborhood radius
* MinPts: minimum number of neighboring points required to form a dense region

### Real-World Use Case

GPS applications use DBSCAN to identify traffic hotspots and detect unusual travel patterns.

### Advantages

* Detects clusters with arbitrary shapes.
* Automatically identifies outliers.
* Does not require specifying the number of clusters.

### Limitations

* Choosing appropriate parameter values can be difficult.
* Performance decreases when cluster densities vary significantly.

---

# Comparison of Clustering Algorithms

| Algorithm    | Best For                                  | Advantages                                    | Limitations                       |
| ------------ | ----------------------------------------- | --------------------------------------------- | --------------------------------- |
| K-Means      | Large datasets with spherical clusters    | Fast and simple                               | Requires K, sensitive to outliers |
| Hierarchical | Small datasets and exploratory analysis   | Produces dendrogram                           | Slow for large datasets           |
| DBSCAN       | Data containing noise or irregular shapes | Finds arbitrary clusters and detects outliers | Sensitive to parameter selection  |

---

# 3. Clustering Metrics

Evaluating clustering quality is essential because there are no true labels available. Several metrics help determine how well clusters have been formed.

## Elbow Method (SSE)

The Elbow Method uses the **Sum of Squared Errors (SSE)**, which measures how close data points are to their assigned cluster centers.

As the number of clusters increases, SSE decreases. The ideal number of clusters is usually found at the "elbow" point where the rate of improvement begins to slow.

Lower SSE indicates tighter clusters.

---

## Silhouette Score

The Silhouette Score measures how similar a data point is to its own cluster compared to other clusters.

Its values range from **-1 to 1**.

* Near 1: Excellent clustering
* Around 0: Overlapping clusters
* Below 0: Poor clustering

Higher values indicate better cluster separation.

---

## Davies–Bouldin Index

The Davies–Bouldin Index evaluates the similarity between clusters.

It considers both:

* Cluster compactness
* Distance between clusters

Unlike the Silhouette Score, **lower values are better** because they indicate more distinct clusters.

---

## Comparison of Clustering Metrics

| Metric               | Measures                        | Good Value                                          |
| -------------------- | ------------------------------- | --------------------------------------------------- |
| Elbow Method (SSE)   | Within-cluster variation        | Lowest value before improvement slows (elbow point) |
| Silhouette Score     | Cluster separation and cohesion | Close to 1                                          |
| Davies–Bouldin Index | Similarity between clusters     | Close to 0                                          |

---

# 4. Choosing K and Interpreting Customer Segments

## How Do You Choose the Number of Clusters?

The number of clusters in K-Means is commonly selected using:

* Elbow Method
* Silhouette Score
* Domain knowledge
* Business requirements

Typically, analysts first examine the Elbow plot and then confirm the choice using the Silhouette Score.

---

## Interpreting Customer Segments in the Wholesale Distributor Dataset

### High Fresh + Milk Spending

Customers with high spending on **Fresh** and **Milk** products are typically restaurants, hotels, cafés, or businesses that sell fresh food and dairy products. These customers require frequent deliveries because their products are highly perishable.

### High Grocery + Detergents_Paper Spending

Customers with high spending on **Grocery** and **Detergents_Paper** products are often supermarkets, convenience stores, and retail shops. They focus on packaged goods and household cleaning products that generally have longer shelf lives.

Understanding these customer segments allows distributors to design targeted marketing strategies, improve inventory planning, and provide personalized services.

---

## Why Are Channel and Region Excluded?

The variables **Channel** and **Region** already describe predefined customer categories rather than purchasing behavior.

Including them would influence the clustering process by forcing customers into existing groups instead of discovering natural patterns based on spending habits.

Therefore, clustering is performed using only purchasing features to ensure unbiased customer segmentation.

---

# 5. Real-World Case Study

## Customer Segmentation Using K-Means in Retail

### Goal

A retail company wanted to better understand customer purchasing behavior in order to improve marketing strategies and customer retention.

### Data Used

The dataset included:

* Annual spending
* Purchase frequency
* Customer income
* Product preferences
* Demographic information

### Clustering Method

Researchers applied the **K-Means clustering algorithm** after standardizing the numerical features. The optimal number of clusters was selected using the Elbow Method.

### Key Results

The clustering process identified several distinct customer groups, including:

* High-value loyal customers
* Budget-conscious shoppers
* Occasional buyers
* Premium product customers

The company used these customer segments to personalize promotions, optimize product recommendations, and improve marketing campaigns. As a result, customer engagement and marketing efficiency improved because different customer groups received offers tailored to their purchasing behavior.

---

# Conclusion

Unsupervised learning plays an important role in discovering hidden patterns within data. Clustering algorithms such as K-Means, Hierarchical Clustering, and DBSCAN enable organizations to identify meaningful customer segments without requiring labeled data. Evaluating clustering quality using metrics like the Elbow Method, Silhouette Score, and Davies–Bouldin Index helps ensure reliable results. In business, healthcare, marketing, and many other industries, clustering supports better decision-making by revealing valuable insights that would otherwise remain hidden.

---

# References

1. Aurélien Géron. *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow*. O'Reilly Media.

2. Christopher M. Bishop. *Pattern Recognition and Machine Learning*. Springer.

3. Ian Goodfellow, Yoshua Bengio, and Aaron Courville. *Deep Learning*. MIT Press.

4. Scikit-learn Developers. *Clustering Documentation*. https://scikit-learn.org/stable/modules/clustering.html

5. Han, Kamber, and Pei. *Data Mining: Concepts and Techniques*. Morgan Kaufmann.
