# Reflection Paper — Wholesale Customer Segmentation


## 1. What I Implemented

In this assignment, I implemented customer segmentation for a wholesale distributor using clustering. The goal was to group customers based on their annual spending behavior, not to predict a known label. I used the six spending columns: Fresh, Milk, Grocery, Frozen, Detergents_Paper, and Delicassen. I did not use Channel and Region as clustering features because the purpose was to let the model discover groups from buying behavior only.

Before training the models, I applied IQR capping to reduce the effect of extreme spending values. I clipped outliers instead of deleting rows, because each row represents a real customer and removing customers could lose useful business information. After that, I used StandardScaler to scale the six spending columns. This was important because K-Means uses distance, and columns with larger numbers could dominate the clustering if the data is not scaled.

I trained K-Means as the main clustering method from the lesson. I also researched and implemented Agglomerative Clustering as a second method. Then I compared both methods using Silhouette Score. In my result, K-Means achieved a Silhouette Score of **0.340**, while Agglomerative Clustering achieved **0.284**. This means K-Means produced better-separated clusters for my experiment.

---

## 2. Segment Interpretation

After training K-Means and checking the cluster centers in original spending units, I interpreted the customer groups in plain business language. The exact cluster numbers are only labels, so the important part is the spending pattern behind each cluster.

One segment can be described as **grocery and detergents oriented buyers**. These customers spend more on Grocery and Detergents_Paper. This type of segment may represent retail shops or small supermarkets because those products are commonly sold to final consumers. A good business action for this group would be to create retail bundle offers, such as grocery plus detergent packages, and give discounts for repeated bulk orders.

Another segment can be described as **fresh product and dairy buyers**. These customers spend more on Fresh and Milk. This group may include hotels, restaurants, cafés, or food-service businesses that need fresh products regularly. A useful business action for this segment would be to offer reliable delivery schedules, fresh-product discounts, and dairy-focused promotions.

A third segment can be described as **lower or moderate spending customers**. These customers do not spend very highly in most product categories compared with the other segments. A good business action for this group would be to use loyalty campaigns, starter wholesale packages, or personalized follow-up to encourage them to buy more frequently.

This interpretation helped me understand that clustering is not only about numbers. The model gives cluster labels, but I have to translate those labels into useful business meaning.

---

## 3. Understanding K-Means

In my own understanding, K-Means is an algorithm that divides data into a chosen number of groups. The number of groups is called **k**. For example, if k = 3, the algorithm tries to divide the customers into three clusters.

K-Means works using centroids. A centroid is the center point of a cluster. At the beginning, K-Means chooses initial centroids. Then it assigns every customer to the closest centroid. After that, it moves each centroid to the average position of all customers assigned to that cluster. This process repeats: assign customers, update centroids, assign again, update again. The algorithm stops when the centroids no longer move much.

I understood K-Means better when I connected it to distance. Customers with similar spending behavior should be closer to each other in the scaled feature space. Customers with different spending behavior should be farther apart. This is why scaling was important before training K-Means.

---

## 4. My Second Algorithm: Agglomerative Clustering

For the second clustering algorithm, I chose **Agglomerative Clustering**, which is a type of Hierarchical Clustering. I chose it because it is easier to understand than some other algorithms and it fits customer segmentation well. It groups customers step by step based on similarity.

Agglomerative Clustering starts by treating each customer as its own cluster. Then it repeatedly merges the most similar customers or groups of customers until it reaches the required number of clusters. Unlike K-Means, it does not start with random centroids. This made it useful as a comparison method.

From my research, I learned that Agglomerative Clustering can show how groups are built gradually, which is helpful for understanding relationships between customers. One advantage is that it is more structured and does not depend on random centroid initialization. One limitation is that it can be slower on large datasets, and it does not provide centroids in the same simple way as K-Means.

In my experiment, Agglomerative Clustering produced a Silhouette Score of **0.284**, while K-Means produced **0.340**. Since a higher Silhouette Score means better-separated clusters, K-Means performed better in this comparison.

---

## 5. My Findings and Recommendation

Based on my results, I would recommend **K-Means** for this wholesale customer segmentation task. K-Means gave the better Silhouette Score in my notebook, which means its customer groups were more separated according to the metric. It was also easier to interpret because I could convert the cluster centers back into original spending units and see what each group buys most.

Agglomerative Clustering was still useful because it gave me another way to think about customer similarity. However, for a business user, K-Means is easier to explain. I can say, for example, “this cluster spends more on Grocery and Detergents_Paper” or “this cluster spends more on Fresh and Milk.” That makes the result more practical for marketing, sales planning, and customer relationship management.

The most important thing I learned is that clustering is not the same as prediction. There is no correct answer column. The model discovers groups, but the human must interpret those groups. In a real wholesale business, these segments could help the distributor design better offers, improve delivery planning, and communicate with customers in a more personalized way.

---

## Reference

scikit-learn. “Clustering.” https://scikit-learn.org/stable/modules/clustering.html
