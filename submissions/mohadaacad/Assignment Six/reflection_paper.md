# Reflection Paper – Wholesale Customer Segmentation

## What Did You Implement?

In this assignment, I implemented a complete clustering pipeline to segment wholesale customers based on their annual spending patterns. I first loaded the wholesale customer dataset and selected the six spending columns: **Fresh, Milk, Grocery, Frozen, Detergents_Paper, and Delicassen**. Following the preprocessing steps from Lesson 6, I applied **IQR capping** to reduce the effect of extreme outliers without removing any rows. After that, I standardized the spending features using **StandardScaler** so that all variables had the same scale before clustering.

Next, I used the **Elbow Method** to observe the Sum of Squared Errors (SSE) for different values of *k* and selected **k = 5**, as used in the lesson. I trained a **K-Means** clustering model and evaluated its performance using the **Silhouette Score** and **Davies-Bouldin Index**. In addition, I researched and implemented **Agglomerative Clustering** as a second clustering algorithm and compared its clustering quality with K-Means using the Silhouette Score.

---

## Segment Interpretation

The K-Means model grouped customers into different clusters based on their purchasing behavior.

One cluster contained customers with **high spending on Fresh and Milk products**. These customers are likely restaurants, hotels, or food service businesses that frequently purchase fresh food items. A suitable business action would be to provide loyalty discounts or priority delivery services to encourage repeat purchases.

Another cluster showed **high spending on Grocery and Detergents_Paper products**. These customers may represent supermarkets or retail stores that regularly purchase packaged food and cleaning products. The distributor could offer bulk purchase discounts and customized product bundles for this customer group.

A third cluster included customers with **lower spending across most product categories**. These customers may be occasional buyers or small businesses. A useful business strategy would be to introduce promotional offers or marketing campaigns to increase their purchasing activity.

---

## Understanding K-Means

K-Means is an unsupervised machine learning algorithm used to group similar data into clusters. It begins by selecting the number of clusters (**k**) and randomly placing cluster centers called **centroids**. Each customer is assigned to the nearest centroid based on the distance between the customer and the centroid.

After all customers are assigned, the algorithm calculates new centroids by taking the average of the customers in each cluster. The assignment and update process continues until the centroids no longer change significantly. The final result is a set of clusters where customers within the same group have similar spending behavior.

---

## Your Second Algorithm

For the second clustering method, I selected **Agglomerative Clustering**. I chose this algorithm because it is a hierarchical clustering method that can identify natural relationships between customers without relying on centroids.

From my research, I learned that Agglomerative Clustering starts by treating every customer as an individual cluster. It then repeatedly merges the two closest clusters until the desired number of clusters is reached.

One advantage of Agglomerative Clustering is that it can reveal hierarchical relationships among clusters and does not require randomly initialized centroids. One limitation is that it is slower than K-Means when working with large datasets because it repeatedly merges clusters during training.

After comparing the Silhouette Scores of both models, I found that **K-Means produced slightly better-separated clusters** than Agglomerative Clustering for this dataset.

---

## Your Findings

Based on the evaluation results, I would recommend **K-Means** for this wholesale customer segmentation task. It produced well-separated clusters, trained quickly, and was easy to interpret. The Elbow Method also made it straightforward to choose an appropriate number of clusters before training.

Although Agglomerative Clustering also produced meaningful customer groups, K-Means achieved better clustering quality and required less computational time. Overall, K-Means is an effective method for segmenting wholesale customers because it helps businesses understand purchasing behavior and develop targeted marketing strategies for different customer groups.
