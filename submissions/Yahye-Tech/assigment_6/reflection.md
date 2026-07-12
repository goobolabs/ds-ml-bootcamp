# Reflection Paper

## 1. What Did You Implement?

In this practical assignment, I implemented two clustering algorithms on the Wholesale Customers dataset. The first algorithm was K-Means, which groups customers based on similar purchasing behavior. The second algorithm was Agglomerative Hierarchical Clustering, which creates clusters by gradually merging similar customers.

Before clustering, I selected the six spending features: Fresh, Milk, Grocery, Frozen, Detergents_Paper, and Delicassen. I applied IQR capping to reduce the effect of outliers and then standardized the data using StandardScaler. After preprocessing, I trained both clustering models and compared their performance using the Silhouette Score.

---

## 2. Segment Interpretation

### Cluster 1

Customers in this cluster spend large amounts on Fresh and Frozen products. These customers are likely restaurants, hotels, or food service businesses.

**Business Action:**
Offer discounts on fresh food products and create loyalty programs for frequent buyers.

---

### Cluster 2

Customers in this cluster spend more on Grocery and Detergents_Paper products. They are likely supermarkets or retail stores.

**Business Action:**
Provide bulk purchase discounts and special promotions for cleaning and grocery products.

---

### Cluster 3

Customers in this cluster have relatively low spending across all product categories.

**Business Action:**
Encourage higher spending by offering promotional packages and personalized marketing campaigns.

---

## 3. Understanding K-Means

K-Means is an unsupervised machine learning algorithm used to divide data into K clusters. It begins by selecting K initial centroids. Each customer is assigned to the nearest centroid based on distance. The centroids are then recalculated using the average of the assigned points. This process repeats until the centroids no longer change significantly. The final result is a set of clusters where customers within the same cluster have similar purchasing behavior.

---

## 4. My Second Algorithm

The second algorithm I selected was Agglomerative Hierarchical Clustering. I chose this algorithm because it does not rely on centroid initialization and provides a hierarchical view of customer relationships.

One advantage of Agglomerative Clustering is that it can discover meaningful hierarchical structures in the data. One limitation is that it is slower than K-Means when working with large datasets.

After comparing the Silhouette Scores, I observed that the algorithm with the higher score produced better-separated clusters.

---

## 5. My Findings

Both clustering algorithms successfully grouped customers based on their purchasing behavior. K-Means performed efficiently and produced clear customer segments. Agglomerative Clustering also generated useful clusters and provided an alternative way of organizing customers.

For this wholesale customer segmentation task, I recommend K-Means because it is faster, easier to interpret, and performs well on this dataset. It is suitable for business applications such as customer segmentation, inventory planning, and targeted marketing. However, Agglomerative Clustering is also valuable when hierarchical relationships between customers are important.

## Conclusion

This assignment improved my understanding of unsupervised learning and clustering techniques. I learned how data preprocessing, feature scaling, and evaluation metrics contribute to successful customer segmentation. These techniques can help businesses better understand customer behavior and make data-driven decisions.