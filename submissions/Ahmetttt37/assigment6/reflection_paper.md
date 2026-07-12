# Part C — Reflection Paper

# Wholesale Customer Segmentation Reflection

## What I Implemented

In this assignment, I implemented a customer segmentation pipeline using the Wholesale Customers dataset. First, I loaded the dataset and selected only the six spending-related features: Fresh, Milk, Grocery, Frozen, Detergents_Paper, and Delicassen. I excluded the Channel and Region columns because they describe customer information rather than purchasing behavior.

Before clustering, I applied IQR capping to reduce the effect of extreme outliers without removing any customers from the dataset. Next, I standardized the spending features using StandardScaler so that all variables had the same scale. I then used the Elbow Method to examine different values of k and trained a K-Means model with five clusters. After training the model, I evaluated the results using the Silhouette Score and the Davies–Bouldin Index and converted the cluster centers back to the original spending units for interpretation.

As an additional clustering method, I implemented Agglomerative Clustering. I trained it using the same scaled spending features and compared its Silhouette Score with the K-Means model to evaluate which algorithm produced better-separated customer groups.

---

## Segment Interpretation

One cluster contained customers with high spending on Fresh and Milk products. These customers are likely to be restaurants, hotels, or food service businesses that purchase fresh products frequently. A useful business action would be to provide discounts on fresh products or offer priority delivery services to encourage customer loyalty.

Another cluster showed high spending on Grocery and Detergents_Paper products. These customers may represent supermarkets or retail stores that purchase packaged goods and cleaning products in large quantities. The distributor could create bulk purchase promotions or long-term supply agreements for these customers.

A third cluster had relatively low spending across most product categories. These customers may be occasional buyers or small businesses. The distributor could increase engagement by offering promotional packages, seasonal discounts, or product recommendations to encourage higher purchasing activity.

---

## Understanding K-Means

K-Means is an unsupervised learning algorithm that divides data into a predefined number of clusters. The algorithm starts by selecting k initial centroids. Each customer is assigned to the nearest centroid based on distance. After all customers are assigned, the centroids are recalculated using the average position of all points within each cluster. The assignment and update steps are repeated until the cluster assignments no longer change or the algorithm reaches convergence.

The objective of K-Means is to group customers with similar purchasing behavior while maximizing the differences between different clusters.

---

## My Second Algorithm

For my second clustering algorithm, I selected Agglomerative Clustering. I chose this method because it groups customers by gradually merging the most similar observations instead of relying on randomly initialized centroids.

From my research, I learned that Agglomerative Clustering builds a hierarchy of clusters and can produce meaningful groupings for smaller datasets. One advantage is that it does not require random centroid initialization. One limitation is that it is computationally more expensive than K-Means for larger datasets and the merging process cannot be reversed once completed.

After evaluating both models, I compared their Silhouette Scores. K-Means produced a slightly better Silhouette Score than Agglomerative Clustering, indicating that its clusters were more clearly separated for this dataset.

---

## My Findings

Based on my results, I would recommend K-Means for this wholesale customer segmentation task. It was simple to implement, computationally efficient, and produced well-separated clusters according to the evaluation metrics. The cluster centers also made it easy to understand the purchasing behavior of each customer segment.

Although Agglomerative Clustering also produced meaningful customer groups, it required more computation and did not achieve a better clustering quality than K-Means in this project. Overall, K-Means provided the best balance between performance, simplicity, and interpretability, making it the most suitable algorithm for segmenting wholesale customers in this dataset.
