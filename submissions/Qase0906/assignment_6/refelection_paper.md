# Wholesale Customer Segmentation Using Clustering

## What I Implemented

In this project, I segmented wholesale customers using two clustering algorithms: **K-Means** and **Agglomerative Clustering**. The goal was to group customers based on their spending patterns in six product categories: **Fresh, Milk, Grocery, Frozen, Detergents_Paper, and Delicassen**.

Before training the models, I prepared the data by selecting the six spending columns, reducing the effect of extreme outliers using the IQR capping method, and scaling the data with **StandardScaler**. I then used the **Elbow Method** to find a suitable number of clusters and selected **k = 3**. After training both algorithms, I evaluated them using the **Silhouette Score** and compared their performance.

---

# Segment Interpretation

The K-Means algorithm divided the customers into three groups based on their purchasing behavior.

### Cluster 1 – Fresh Food Customers

Customers in this cluster spend more on **Fresh** and **Frozen** products than on other categories. They may represent restaurants, hotels, or businesses that regularly purchase fresh food.

**Business action:** Offer discounts on fresh food products or create special promotions for restaurants to encourage larger orders.

### Cluster 2 – Grocery and Household Customers

Customers in this group spend the most on **Milk**, **Grocery**, and **Detergents_Paper**. These customers are likely supermarkets or retail stores that buy household products in large quantities.

**Business action:** Provide bulk purchase discounts or loyalty programs to increase customer retention.

### Cluster 3 – Balanced Customers

Customers in this cluster have lower or moderate spending across most product categories. They do not specialize in one type of product and have more balanced purchasing habits.

**Business action:** Recommend personalized product bundles or targeted promotions to increase sales in different categories.

---

# Understanding K-Means

K-Means is an unsupervised machine learning algorithm used to group similar data into clusters. It does not need labeled data because it finds patterns automatically.

The algorithm starts by choosing a number of clusters, called **k**, and places a centroid in each cluster. Each customer is assigned to the nearest centroid based on distance. After all customers are assigned, the centroid of each cluster is recalculated. The assignment and update process continues until the centroids stop changing or change very little. The final result is a set of customer groups with similar spending behavior.

---

# My Second Algorithm

The second clustering algorithm I chose was **Agglomerative Clustering**.

I selected this algorithm because it builds clusters by gradually merging the most similar customers instead of assigning them to predefined centers. This makes it useful for discovering natural relationships in the data.

One advantage of Agglomerative Clustering is that it does not depend on randomly selected starting points, which can make the clustering results more stable. One limitation is that it becomes slower on larger datasets because it repeatedly calculates distances while merging clusters.

After evaluating both models with the Silhouette Score, I found that **K-Means achieved a slightly better Silhouette Score than Agglomerative Clustering**. This suggests that K-Means produced more clearly separated customer groups for this dataset.

---

# My Findings

Both clustering algorithms successfully grouped customers with similar purchasing behavior. However, K-Means produced better cluster quality according to the Silhouette Score and was also faster to train. It created clear customer segments that are easy to understand and useful for business decision-making.

For this wholesale customer segmentation task, I would recommend **K-Means** because it is simple, efficient, and produced better clustering results in this project. The customer groups can help the distributor design targeted marketing campaigns, offer product recommendations, and improve customer service based on different purchasing patterns.

---

# References

- Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* (3rd ed.). O'Reilly Media.
- Pedregosa, F., et al. (2011). *Scikit-learn: Machine Learning in Python*. Journal of Machine Learning Research, 12, 2825–2830.
- Tan, P., Steinbach, M., & Kumar, V. (2019). *Introduction to Data Mining* (2nd ed.). Pearson.