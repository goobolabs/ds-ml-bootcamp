# Reflection Paper – Wholesale Customer Segmentation

## What I Implemented

In this assignment, I performed customer segmentation using two clustering algorithms: **K-Means** and **Agglomerative Clustering**. I used the six spending-related features from the Wholesale Customers dataset: **Fresh, Milk, Grocery, Frozen, Detergents_Paper,** and **Delicassen**. I did not use the **Channel** or **Region** columns because they are categorical and were not required for clustering.

Before training the models, I prepared the data by applying **IQR capping** to reduce the effect of extreme outliers without removing any customers. I then used **StandardScaler** to standardize the six spending features so that each feature contributed equally to the clustering process.

For K-Means, I first used the Elbow Method to observe the SSE values for different numbers of clusters and then trained the model with **5 clusters**. I evaluated the clustering quality using the **Silhouette Score** and **Davies–Bouldin Index**. I also trained **Agglomerative Clustering** on the same scaled data and compared its Silhouette Score with K-Means.

---

# Segment Interpretation

### Cluster 0 – High Fresh Product Buyers

Customers in this cluster spend much more on fresh products than on other product categories. They are likely restaurants, hotels, or businesses that frequently purchase fresh food.

**Business Action:** Offer discounts on fresh products, provide priority delivery, and create loyalty programs for frequent buyers.

### Cluster 1 – Grocery and Detergent Buyers

Customers in this cluster spend heavily on grocery items and detergents. These customers are likely supermarkets, retail shops, or convenience stores that regularly purchase household products.

**Business Action:** Create bundle promotions for grocery and detergent products and offer bulk-purchase discounts.

### Cluster 2 – Moderate Spending Customers

Customers in this cluster have moderate spending across most product categories. They are balanced buyers without a strong preference for one category.

**Business Action:** Recommend complementary products and personalized promotions to encourage higher spending.

---

# Understanding K-Means

K-Means is an unsupervised machine learning algorithm that groups similar data into a fixed number of clusters (**k**). The algorithm first selects **k centroids** as the initial cluster centers. Each customer is assigned to the nearest centroid based on distance. After all customers are assigned, the centroid of each cluster is recalculated using the average of the points in that cluster. The assignment and centroid update steps are repeated until the cluster assignments no longer change or the algorithm reaches convergence.

The goal of K-Means is to minimize the distance between customers and the centroid of their assigned cluster, creating compact and well-separated groups.

---

# My Second Algorithm

For my second clustering algorithm, I selected **Agglomerative Clustering**, which is a hierarchical clustering algorithm.

Agglomerative Clustering starts by treating every customer as its own cluster. It then repeatedly merges the two most similar clusters until the desired number of clusters is reached.

One advantage of Agglomerative Clustering is that it does not depend on randomly selected centroids and can reveal hierarchical relationships among customers. One limitation is that it is generally slower than K-Means on larger datasets and can become computationally expensive.

When comparing the clustering quality, the Silhouette Scores were:

* **K-Means:** 0.283
* **Agglomerative Clustering:** 0.218

Since K-Means achieved the higher Silhouette Score, it produced better-separated customer clusters on this dataset.

---

# My Findings

Based on the evaluation results, I would recommend **K-Means** for this wholesale customer segmentation task. It produced a higher Silhouette Score than Agglomerative Clustering, indicating that the customer groups were more compact and better separated. K-Means is also efficient, easy to implement, and performs well on numerical datasets such as customer spending data.

Agglomerative Clustering was useful for understanding an alternative clustering approach and learning how hierarchical clustering works. Although its performance was slightly lower on this dataset, it remains a valuable method for datasets where hierarchical relationships are important. Overall, K-Means was the better choice for this wholesale customer segmentation task because it achieved better clustering quality and is well suited for large business datasets.
