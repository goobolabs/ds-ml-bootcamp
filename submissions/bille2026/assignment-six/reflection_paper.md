# Part C — Reflection Paper  
## Wholesale Customer Segmentation Using Clustering

## 1. What Did I Implement?

In this project, I implemented a wholesale customer segmentation system using unsupervised learning techniques. The main goal was to group wholesale customers based on their purchasing behavior without using predefined labels.

I used six spending-related features from the dataset:

- Fresh
- Milk
- Grocery
- Frozen
- Detergents_Paper
- Delicassen

I excluded the Channel and Region columns because they describe customer categories and locations rather than customer spending behavior. Including them could affect the clustering results and create groups based on location instead of purchasing patterns.

Before applying clustering algorithms, I performed data preprocessing. I applied IQR capping with k=1.5 to reduce the effect of extreme values without deleting any customer records. After handling outliers, I applied StandardScaler to normalize the six spending features because clustering algorithms use distance calculations.

I first implemented K-Means clustering with five clusters. The Elbow Method was used to examine different values of K by calculating SSE values from k=1 to k=10. After selecting k=5, I trained the K-Means model and added cluster labels to the dataset.

I also implemented a second clustering algorithm, Hierarchical Clustering, using Agglomerative Clustering with the same scaled features. Finally, I compared both methods using Silhouette Score.

---

# 2. Segment Interpretation

The K-Means algorithm divided customers into five different clusters based on their spending patterns. Each cluster represents a group of customers with similar purchasing behaviors.

## Cluster 0 — Balanced Product Customers

Cluster 0 has moderate spending across different product categories. The cluster center shows:

- Fresh: 9202.67
- Milk: 6833.30
- Detergents_Paper: 3280.12
- Delicassen: 1871.76

These customers purchase a mixture of products without focusing on only one category.

**Business action:**  
The distributor can provide product bundles that combine different categories and encourage these customers to increase their order size.

---

## Cluster 2 — High Spending Customers

Cluster 2 represents customers with high spending levels. The cluster center shows:

- Fresh: 17461.54
- Milk: 13805.60
- Detergents_Paper: 5460.56
- Delicassen: 3583.64

These customers purchase large amounts of fresh products and dairy-related items. They may represent valuable customers such as restaurants or businesses with high demand.

**Business action:**  
The distributor should provide loyalty programs, priority delivery, and special discounts to maintain these high-value customers.

---

## Cluster 4 — Grocery and Household Product Customers

Cluster 4 shows customers who spend more on household-related products:

- Fresh: 4916.98
- Milk: 10768.85
- Detergents_Paper: 7780.02
- Delicassen: 981.37

These customers have stronger demand for Grocery and Detergents_Paper products.

**Business action:**  
The distributor can create promotional packages that combine grocery products with household supplies and offer discounts for bulk purchases.

---

# 3. Understanding K-Means

K-Means is an unsupervised learning algorithm used to divide data into groups called clusters. The algorithm requires selecting the number of clusters, represented by K.

The process starts by randomly selecting K points as cluster centers called centroids. Each data point is assigned to the nearest centroid based on distance. After assigning all points, the algorithm updates the centroids by calculating the average position of all points inside each cluster.

This process of assigning points and updating centroids continues repeatedly until the centroids stop changing significantly. The final result is a set of clusters where customers inside the same cluster have similar purchasing behaviors.

---

# 4. My Second Algorithm: Hierarchical Clustering

The additional algorithm I selected was Hierarchical Clustering using Agglomerative Clustering.

I chose this algorithm because it provides a different approach from K-Means. Instead of using centroids, Hierarchical Clustering creates clusters by gradually combining similar data points based on distance.

From my research, I learned that Hierarchical Clustering can show relationships between data points through a tree structure called a dendrogram. One advantage of this algorithm is that it does not depend on random centroid initialization. However, one limitation is that it becomes slower when working with large datasets.

In this project, Hierarchical Clustering achieved a Silhouette Score of:

**0.218**

while K-Means achieved:

**0.283**

Since K-Means had a higher Silhouette Score, it produced better-separated clusters for this dataset.

---

# 5. Findings and Recommendation

The results showed that both K-Means and Hierarchical Clustering were able to identify groups of wholesale customers based on their spending patterns. The evaluation results showed that K-Means performed better, achieving a Silhouette Score of 0.283 compared with 0.218 from Hierarchical Clustering.

For this wholesale segmentation task, I would recommend K-Means clustering. K-Means is more suitable because it is faster, easier to interpret, and produced better-separated customer groups in this experiment. The clusters provide useful information about customer purchasing behavior, which can help the distributor design targeted marketing campaigns, improve customer relationships, and create better product offers.

Although Hierarchical Clustering provides useful information about relationships between customers, its lower Silhouette Score and higher computational cost make it less suitable than K-Means for this particular dataset.

---

# References

1. Scikit-learn Documentation — Clustering Algorithms.  
2. Han, J., Kamber, M., & Pei, J. (2012). Data Mining: Concepts and Techniques.  
3. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). An Introduction to Statistical Learning.