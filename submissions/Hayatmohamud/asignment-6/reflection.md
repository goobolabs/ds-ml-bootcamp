# Part C — Reflection Paper

## What I Implemented

In this assignment, I implemented a complete customer segmentation pipeline using the **Wholesale Customers** dataset. I first loaded the dataset and selected only the six spending features: **Fresh, Milk, Grocery, Frozen, Detergents_Paper,** and **Delicassen**. The **Channel** and **Region** columns were excluded because they represent existing categories rather than customer purchasing behavior.

Before clustering, I applied **IQR capping (k = 1.5)** to reduce the impact of extreme outliers while keeping all customers in the dataset. Next, I standardized the six spending features using **StandardScaler** so that each feature contributed equally to the clustering process.

I then trained a **K-Means** clustering model with **five clusters** (`n_clusters=5`). After fitting the model, I evaluated its performance using the **Silhouette Score** and **Davies–Bouldin Index** and examined the cluster centers by converting them back to the original spending units.

As a second clustering algorithm, I implemented **Agglomerative (Hierarchical) Clustering** using the same scaled features. I compared its Silhouette Score with that of K-Means to determine which algorithm produced better-separated customer groups.

---

# Segment Interpretation

The K-Means algorithm divided customers into groups with similar purchasing patterns. Although the exact spending values differ for each dataset, the clusters can be interpreted in business terms.

### Cluster 1 – Fresh Food Customers

Customers in this cluster spend most of their budget on **Fresh** products and relatively less on packaged goods. These customers are likely restaurants, hotels, or businesses that require frequent deliveries of fresh food.

**Business Action**

The distributor could provide faster delivery schedules, freshness guarantees, and discounts for bulk fresh food purchases to improve customer loyalty.

---

### Cluster 2 – Grocery and Cleaning Product Customers

This cluster contains customers who spend heavily on **Grocery** and **Detergents_Paper** products. They are likely supermarkets, convenience stores, or retail businesses that sell packaged food and household supplies.

**Business Action**

The distributor could create wholesale bundle offers and loyalty programs for grocery and cleaning products to encourage larger purchases.

---

### Cluster 3 – Balanced Customers

Customers in this cluster have moderate spending across most product categories without a strong preference for a single type of product.

**Business Action**

The distributor could recommend complementary products and offer personalized promotions to increase purchases across multiple product categories.

---

# Understanding K-Means

K-Means is an unsupervised machine learning algorithm used to divide data into **K clusters** based on similarity. The algorithm begins by selecting **K centroids**, which represent the center of each cluster. Every customer is assigned to the nearest centroid according to the distance between the customer's features and the centroid.

After all customers have been assigned, the algorithm recalculates each centroid by computing the average of all customers belonging to that cluster. The assignment and centroid update steps are repeated until the cluster memberships no longer change significantly or the algorithm reaches convergence.

This iterative process allows K-Means to create compact clusters where customers within the same group have similar purchasing behavior while customers in different groups are more distinct.

---

# My Second Algorithm

For the second clustering method, I selected **Agglomerative (Hierarchical) Clustering**.

I chose this algorithm because it builds clusters by gradually merging the most similar customers together. Unlike K-Means, it does not rely on centroid updates and instead creates a hierarchy of clusters based on customer similarity.

During my research, I learned that Agglomerative Clustering starts by treating every customer as an individual cluster. It then repeatedly merges the closest clusters until the desired number of clusters is reached.

One major advantage of this method is that it can reveal hierarchical relationships among customer groups and often works well for exploratory analysis.

One limitation is that it is computationally more expensive than K-Means, making it less suitable for very large datasets.

After training both models, I compared their **Silhouette Scores**. The algorithm with the higher Silhouette Score produced better-separated clusters. In my implementation, I used this metric to determine which clustering method performed better on the wholesale customer data.

---

# My Findings

Both clustering algorithms successfully grouped customers according to their purchasing behavior. K-Means produced clear customer segments and was easy to implement, making it an effective choice for wholesale customer segmentation. It is also computationally efficient and scales well to large datasets, which makes it practical for real business applications.

Agglomerative Clustering provided another perspective on the customer groups by building clusters based on hierarchical relationships. While it offered useful insights, it generally requires more computation and may not perform as efficiently on large datasets.

Overall, I would recommend **K-Means** for this wholesale segmentation task because it is simple, fast, and produces meaningful customer segments that can easily be interpreted by business managers. Agglomerative Clustering is valuable for exploring the structure of the data, but K-Means is better suited for routine customer segmentation due to its speed, scalability, and ease of interpretation.
