# Assignment 6 – Part C: Reflection Paper

# Reflection on Wholesale Customer Segmentation

## What I Implemented

In this project, I implemented a complete customer segmentation pipeline using the Wholesale Customers dataset. The dataset contains six spending variables: **Fresh, Milk, Grocery, Frozen, Detergents_Paper, and Delicassen**. These six spending columns were selected because they represent customers' purchasing behavior. The **Channel** and **Region** columns were excluded from clustering because they describe customer categories rather than spending patterns and could bias the clustering results.

The project started with data preprocessing. I applied **IQR capping** to reduce the effect of extreme outliers without removing any customer records. Next, I standardized the six spending features using **StandardScaler** because clustering algorithms based on distance perform better when all variables are on the same scale.

I first reproduced the Lesson 6 implementation using **K-Means clustering** with **k = 5**. I also applied the **Elbow Method** to calculate the Sum of Squared Errors (SSE) for different values of *k* before training the final model. After training, I evaluated the clustering results using the **Silhouette Score** and **Davies–Bouldin Index** and interpreted the resulting customer segments.

As an additional requirement, I researched and implemented **Agglomerative Clustering**. I selected this algorithm because it is one of the most popular hierarchical clustering methods and does not rely on centroid updates like K-Means. It builds clusters gradually by merging the most similar groups until the required number of clusters is reached. This allowed me to compare a centroid-based clustering method with a hierarchical clustering method on the same dataset.

Finally, I completed an additional task beyond the clustering requirements. After generating the K-Means cluster labels, I saved the clustered dataset and converted the problem into a **supervised learning** task. I used the generated cluster labels as the target variable and trained a **Random Forest classifier** to predict which cluster a new customer belongs to based on spending behavior.

---

## Segment Interpretation

The K-Means model divided the wholesale customers into five different clusters representing different purchasing patterns.

One important cluster contained customers with **high spending on Fresh and Frozen products**. These customers are likely to be restaurants, hotels, or food service businesses that purchase fresh food regularly. A suitable business strategy for this group would be to offer volume discounts, faster delivery services, and loyalty programs for fresh products.

Another cluster showed **very high spending on Grocery and Detergents_Paper**. These customers are likely supermarkets or retail stores that purchase packaged food and cleaning products in large quantities. The distributor could improve sales by providing bulk pricing, promotional campaigns, and long-term supply contracts for grocery and cleaning products.

A third cluster contained customers with **balanced or moderate spending across most product categories**. These customers may represent medium-sized businesses with regular purchasing habits. The distributor could encourage higher spending by recommending complementary products and offering personalized marketing campaigns based on previous purchases.

---

## Understanding K-Means

K-Means is an unsupervised machine learning algorithm that groups similar data points into a predefined number of clusters. The value of **k** represents the number of clusters that the algorithm should create.

The algorithm begins by selecting **k initial centroids**. Each customer is assigned to the nearest centroid based on the Euclidean distance. After all customers have been assigned, the centroid of each cluster is recalculated as the mean of all points within that cluster. The assignment and centroid update steps are repeated until the centroids no longer change significantly or the algorithm converges.

The objective of K-Means is to minimize the distance between customers and the centroid of the cluster they belong to, producing compact and well-separated groups.

---

## My Second Algorithm

The additional clustering algorithm I selected was **Agglomerative Clustering**. I chose this method because it provides a different clustering approach from K-Means. Instead of updating centroids, Agglomerative Clustering starts with every customer as an individual cluster and repeatedly merges the closest clusters until the desired number of clusters is reached.

From my research, I learned that Agglomerative Clustering is useful for understanding hierarchical relationships within data and does not require centroid initialization. One major advantage is that it produces a hierarchical structure of clusters and can reveal relationships between groups. However, one limitation is that once two clusters are merged, the algorithm cannot undo that decision, which may reduce clustering quality if an early merge is not optimal.

I compared both algorithms using the Silhouette Score:

* **K-Means Silhouette Score:** **0.283**
* **Agglomerative Clustering Silhouette Score:** **0.218**

The comparison shows that **K-Means produced better-separated clusters** than Agglomerative Clustering for this dataset. The higher Silhouette Score indicates that customers within each K-Means cluster are more similar to one another and more distinct from customers in other clusters.

---

## Additional Supervised Learning Experiment

To extend the project, I transformed the clustered dataset into a supervised learning problem. After K-Means generated the cluster labels, I saved the segmented dataset and reloaded it for classification. The **Cluster** column became the target variable, while the six spending variables remained the input features.

I trained a **Random Forest classifier** to predict the cluster membership of new customers. The classifier achieved the following results:

* **Accuracy:** 95.5%
* **Precision:** 95.5%
* **Recall:** 95.5%
* **F1-Score:** 95.4%

The confusion matrix also showed that most customers were classified into the correct clusters, with only a small number of misclassifications. This demonstrates that the spending features contain enough information for the classifier to accurately predict customer segments generated by K-Means. The trained model can therefore be used to assign new customers to an existing cluster without running the clustering algorithm again.

---

## My Findings

Based on the experimental results, I would recommend **K-Means** for this wholesale customer segmentation task. It achieved a higher Silhouette Score (**0.283**) than Agglomerative Clustering (**0.218**), indicating better cluster separation. K-Means was also computationally efficient, easy to interpret, and well suited to standardized numerical spending data.

Overall, this project helped me understand both unsupervised and supervised machine learning. I learned how clustering can discover hidden customer groups without labels and how those discovered clusters can later be used as labels in a supervised classification model. Combining K-Means with Random Forest demonstrated how customer segmentation can support future customer prediction, targeted marketing, inventory planning, and business decision-making.
