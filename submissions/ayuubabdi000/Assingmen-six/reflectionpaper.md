# Wholesale Customer Segmentation Using Clustering Algorithms

## What I Implemented

In this project, I implemented a wholesale customer segmentation pipeline using unsupervised machine learning. The goal was to group wholesale clients into meaningful segments based on their purchasing behavior.

I loaded the wholesale customer dataset and selected only the six spending columns required for clustering:

* Fresh
* Milk
* Grocery
* Frozen
* Detergents_Paper
* Delicassen

I excluded **Channel** and **Region** because they were not used as clustering features. Before training the models, I applied IQR capping with a value of 1.5 to reduce the influence of extreme spending values without removing any customers. After handling outliers, I standardized the six spending features using `StandardScaler`.

I used the Elbow Method to analyze different values of K from 1 to 10 and then trained a K-Means model with:

`KMeans(n_clusters=5, n_init="auto", random_state=42)`

I also implemented a second clustering algorithm, **Agglomerative Clustering**, using the same scaled features. Finally, I compared both methods using the Silhouette Score and saved the final dataset with K-Means cluster labels.

---

## Segment Interpretation

The K-Means algorithm created five customer clusters. Looking at the cluster centers in original spending units, some customer groups showed different purchasing patterns.

### Cluster Example 1: High Grocery and Detergents_Paper Customers

This cluster contains customers who spend heavily on grocery products and detergents/paper items. These customers are likely retail-focused businesses that purchase frequently for consumer demand.

**Business action:**
The distributor could offer bulk discounts, loyalty programs, and promotions focused on grocery and household products to increase repeat purchases.

---

### Cluster Example 2: High Fresh Product Customers

This cluster contains customers with higher spending on fresh products compared with other categories. They may represent businesses such as restaurants, food stores, or fresh product retailers.

**Business action:**
The distributor could provide special fresh product packages, reliable delivery schedules, and volume-based pricing to maintain these customers.

---

### Cluster Example 3: Lower Spending General Customers

This group contains customers with lower overall spending across most categories. They may be smaller businesses or customers who purchase less frequently.

**Business action:**
The distributor could target this group with beginner-level offers, smaller package sizes, and marketing campaigns designed to increase purchasing frequency.

---

## Understanding K-Means

K-Means is an unsupervised machine learning algorithm used to divide data into groups called clusters. The algorithm requires choosing a value for **K**, which represents the number of clusters to create.

The algorithm works through an assign-and-update process:

1. The algorithm randomly places K initial centroids (cluster centers).
2. Each data point is assigned to the nearest centroid based on distance.
3. The centroids are updated by calculating the average position of all points assigned to each cluster.
4. Steps 2 and 3 repeat until the centroids stop changing.

The final result is a set of clusters where customers inside the same cluster have similar purchasing patterns.

---

## My Second Algorithm: Agglomerative Clustering

The additional algorithm I selected was **Agglomerative Clustering**, also known as hierarchical clustering.

I chose this algorithm because it provides a different approach from K-Means. Instead of assigning customers directly to fixed groups, Agglomerative Clustering starts with each customer as an individual cluster and gradually combines the most similar customers until the desired number of clusters is reached.

One advantage of Agglomerative Clustering is that it can discover hierarchical relationships between customers and does not require selecting random initial centroids.

One limitation is that it can become computationally expensive with very large datasets because it compares distances between many data points.

For this project, Agglomerative Clustering produced a Silhouette Score of **0.218**, while K-Means achieved a higher Silhouette Score of **0.283**. This means K-Means produced better-separated customer groups for this dataset.

---

## Findings

Based on the evaluation results, I would recommend using **K-Means clustering** for this wholesale customer segmentation task. K-Means achieved a higher Silhouette Score (0.283 compared with 0.218 for Agglomerative Clustering), which indicates that the clusters were more clearly separated.

K-Means is also practical for business applications because it is simple, fast, and easy to interpret. The cluster centers provide useful information about customer purchasing behavior, allowing distributors to create targeted strategies for different customer groups.

Although Agglomerative Clustering was useful for comparison and provided another perspective on customer relationships, K-Means produced stronger segmentation results for this dataset. Therefore, I would use K-Means as the primary method for identifying wholesale customer segments and making business decisions.
