# Part C — Reflection Paper: Wholesale Customer Segmentation Using Clustering

# 1. What I Implemented

In this assignment, I implemented an unsupervised machine learning project to segment wholesale customers based on their annual spending patterns. I reproduced the Lesson 6 workflow by using the six spending features: **Fresh**, **Milk**, **Grocery**, **Frozen**, **Detergents_Paper**, and **Delicassen**. The **Channel** and **Region** columns were not used for clustering because they are descriptive information rather than purchasing behavior.

The preprocessing stage included selecting the spending columns, applying IQR capping to reduce the influence of extreme outliers, and standardizing the features with **StandardScaler**. I then used the Elbow Method to evaluate different values of *k* and trained a **K-Means** model with five clusters, following the lesson. After training the model, I evaluated the clustering quality using the **Silhouette Score** and the **Davies–Bouldin Index**, and interpreted the cluster centers in their original spending units.

In addition to K-Means, I researched and implemented **Agglomerative (Hierarchical) Clustering**. I trained this model on the same scaled dataset and compared its clustering quality with K-Means using the Silhouette Score. Finally, I assigned cluster labels to customers and saved the segmented dataset for further analysis.

---

# 2. Segment Interpretation

The K-Means model grouped customers into clusters with different purchasing behaviors.

One cluster contained customers with high spending on **Fresh** and **Milk** products. These customers are likely to be restaurants, hotels, or businesses that regularly purchase fresh food. A suitable business action would be to provide loyalty discounts, priority delivery, or customized promotions for fresh products to encourage long-term partnerships.

Another cluster showed high spending on **Grocery** and **Detergents_Paper** products. These customers may represent supermarkets, retail stores, or convenience shops that frequently buy packaged goods and cleaning supplies. The distributor could offer bundled product packages, volume discounts, or seasonal promotions to increase customer satisfaction and sales.

A third cluster consisted of customers with relatively low spending across most product categories. These customers may be smaller businesses or occasional buyers. The company could encourage additional purchases by offering promotional bundles, personalized recommendations, or special discounts for first-time bulk orders.

---

# 3. Understanding K-Means

K-Means is an unsupervised clustering algorithm that groups similar data points into a predefined number of clusters. The algorithm begins by selecting the number of clusters (*k*) and placing an initial centroid for each cluster.

Each customer is assigned to the nearest centroid based on the distance between the customer and the cluster center. After all customers are assigned, the algorithm recalculates each centroid by computing the average position of all members within that cluster. The assignment and update process repeats until the centroids no longer change significantly or the algorithm reaches convergence.

The final result is a set of clusters where customers within the same cluster have similar purchasing behavior while customers in different clusters are as different as possible.

---

# 4. My Second Algorithm

For the second clustering algorithm, I selected **Agglomerative (Hierarchical) Clustering** because it is widely used for customer segmentation and does not require random centroid initialization.

Agglomerative Clustering starts by treating every customer as its own cluster. It then repeatedly merges the two most similar clusters until the desired number of clusters is reached. One major advantage is that it can reveal hierarchical relationships between customers and does not depend on random starting points. However, its main limitation is that it is generally slower than K-Means on very large datasets because it repeatedly calculates distances between clusters.

When comparing the evaluation results, the Silhouette Score of Agglomerative Clustering was similar to that of K-Means, although K-Means produced slightly better-separated clusters for this dataset. This suggests that both methods are useful, but K-Means was a better fit for the wholesale customer segmentation task.

---

# 5. My Findings

Based on the results of this assignment, I would recommend **K-Means** for wholesale customer segmentation. It produced clear and well-separated customer groups while requiring relatively little computational time. The algorithm is easy to implement, performs efficiently on medium-sized datasets, and provides cluster centers that are easy for businesses to interpret.

This assignment improved my understanding of unsupervised learning and customer segmentation. I learned that clustering can reveal hidden patterns in customer purchasing behavior without requiring labeled data. I also learned that evaluating clustering models requires different metrics than supervised learning, such as the Elbow Method, Silhouette Score, and Davies–Bouldin Index. Comparing two different clustering algorithms helped me understand that different methods may produce different customer segments, making model evaluation an important step before applying clustering results to real business decisions.
