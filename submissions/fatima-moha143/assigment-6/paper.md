# Part A – Introduction to Unsupervised Learning and Clustering

## Introduction to Unsupervised Learning and Clustering

### What is Unsupervised Learning?

Unsupervised learning is a type of machine learning in which the algorithm learns from data that does not contain labeled outputs. Unlike supervised learning, there are no correct answers provided during training. Instead, the algorithm searches for hidden patterns, similarities, or structures within the data.

A common task in unsupervised learning is **clustering**, where similar data points are grouped together based on their characteristics.

### How is it Different from Regression and Classification?

Regression and classification are supervised learning techniques because they require labeled training data.

* **Regression** predicts a continuous numerical value, such as predicting house prices or sales revenue.
* **Classification** predicts a category or class, such as determining whether an email is spam or not spam.
* **Unsupervised learning** does not use labels. Instead, it automatically discovers patterns and groups within the data.

### Real-Life Examples

**Clustering Example**

A supermarket groups customers according to their purchasing behavior. Customers with similar buying habits are placed into the same segment so that personalized promotions can be offered.

**Supervised Learning Example**

A bank predicts whether a customer will repay a loan based on previous customer data labeled as "paid" or "defaulted."

---

# Clustering Algorithms

## 1. K-Means

### How it Works

K-Means divides data into a fixed number (**k**) of clusters. It starts by selecting **k centroids**, assigns each data point to its nearest centroid, updates the centroid positions, and repeats this process until the clusters become stable.

### Real-World Use Case

Retail companies use K-Means to segment customers based on purchasing behavior for targeted marketing campaigns.

### Advantages

* Simple and easy to implement.
* Fast on large datasets.
* Efficient for numerical data.
* Produces compact clusters.

### Limitations

* The number of clusters (**k**) must be chosen beforehand.
* Sensitive to outliers.
* Works best when clusters are roughly spherical.

---

## 2. Hierarchical Clustering

### How it Works

Hierarchical Clustering builds clusters step by step. In Agglomerative Clustering, each data point begins as its own cluster. The algorithm repeatedly merges the most similar clusters until the desired number of clusters is reached.

### Real-World Use Case

Healthcare organizations use hierarchical clustering to group patients with similar medical conditions for treatment planning.

### Advantages

* Does not require random centroid initialization.
* Produces a hierarchy of clusters.
* Helpful for understanding relationships between groups.

### Limitations

* Slower than K-Means on large datasets.
* Computationally expensive for large amounts of data.

---

## 3. DBSCAN

### How it Works

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) groups together points that are located in dense regions and labels isolated points as outliers.

### Real-World Use Case

GPS and location-based services use DBSCAN to identify areas with high customer activity and detect unusual locations.

### Advantages

* Automatically identifies outliers.
* Does not require specifying the number of clusters.
* Works well with irregularly shaped clusters.

### Limitations

* Sensitive to the choice of parameters (`eps` and `min_samples`).
* May perform poorly when cluster densities vary significantly.

---

# Comparison of Clustering Algorithms

| Algorithm               | Main Idea                         | Advantages       | Limitations             | Example Use Case            |
| ----------------------- | --------------------------------- | ---------------- | ----------------------- | --------------------------- |
| K-Means                 | Groups data around centroids      | Fast and simple  | Must choose k           | Customer segmentation       |
| Hierarchical Clustering | Gradually merges similar clusters | Shows hierarchy  | Slow on large datasets  | Healthcare patient grouping |
| DBSCAN                  | Groups dense regions              | Detects outliers | Sensitive to parameters | GPS hotspot detection       |

---

# Clustering Metrics

## Elbow Method (SSE)

The Elbow Method uses the **Sum of Squared Errors (SSE)** to help determine the appropriate number of clusters. As the number of clusters increases, SSE decreases. The best value of **k** is usually found at the "elbow" point, where the decrease in SSE begins to slow down.

### Good Result

Choose the value of **k** where the elbow appears.

---

## Silhouette Score

The Silhouette Score measures how well each data point fits within its assigned cluster compared to other clusters.

The score ranges from **-1 to 1**.

* Close to **1** → excellent clustering.
* Around **0** → overlapping clusters.
* Below **0** → poor clustering.

### Good Result

Higher values are better.

---

## Davies–Bouldin Index

The Davies–Bouldin Index measures how similar clusters are to each other.

A lower score indicates clusters that are compact and well separated.

### Good Result

Lower values are better.

---

# Comparison of Clustering Metrics

| Metric               | Measures                        | Good Value        |
| -------------------- | ------------------------------- | ----------------- |
| Elbow Method (SSE)   | Within-cluster error            | Clear elbow point |
| Silhouette Score     | Cluster separation and cohesion | Closer to 1       |
| Davies–Bouldin Index | Cluster similarity              | Closer to 0       |

---

# Choosing k and Interpreting Segments

## How Do You Choose the Number of Clusters?

The number of clusters is commonly selected using the **Elbow Method**. By plotting SSE against different values of **k**, we choose the point where adding more clusters provides only a small improvement. This point usually represents the optimal number of clusters.

## Interpreting Customer Segments

Customers with **high Fresh and Milk spending** are likely restaurants, hotels, cafés, or businesses that regularly purchase fresh food and dairy products.

Customers with **high Grocery and Detergents_Paper spending** are more likely supermarkets, grocery stores, or retail businesses that purchase packaged food and cleaning products in large quantities.

These customer segments help distributors understand different purchasing behaviors and create targeted marketing strategies.

## Why Exclude Channel and Region?

The clustering analysis focuses on purchasing behavior. The **Channel** and **Region** columns describe customer categories and locations rather than spending patterns. Including them could influence the clustering results and reduce the model's ability to group customers based solely on their purchasing behavior.

---

# Real-World Case Study

## Customer Segmentation in Retail

Many retail companies use clustering to better understand customer purchasing behavior. A common goal is to divide customers into meaningful groups so that marketing campaigns and product recommendations can be personalized.

The data used typically includes purchase history, spending amounts, shopping frequency, and product categories. One widely used clustering method is **K-Means**, which groups customers with similar buying patterns into the same cluster.

The results help businesses identify valuable customer groups, improve targeted advertising, increase customer satisfaction, and optimize inventory management. Customer segmentation has become an important business strategy because it enables companies to make data-driven marketing decisions and improve overall sales performance.

**Research Source**

* Scikit-learn Documentation: https://scikit-learn.org/stable/modules/clustering.html
* Han, J., Kamber, M., & Pei, J. *Data Mining: Concepts and Techniques* (3rd Edition).
