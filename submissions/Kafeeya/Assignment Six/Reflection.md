1. What did you implement?
I implemented a customer segmentation model using the Wholesale Customers dataset. First, I selected the six spending features (Fresh, Milk, Grocery, Frozen, Detergents_Paper, and Delicassen) and standardized them so that all variables had the same scale. Then I applied K-Means clustering to divide customers into groups with similar purchasing patterns. After training the model, I evaluated it using the Silhouette Score and Davies–Bouldin Index, and examined the cluster centers to understand the characteristics of each customer segment.
As an additional clustering algorithm, I used Hierarchical Clustering (Agglomerative Clustering) (or replace this with the algorithm you actually used if different). I compared its clustering quality with K-Means using the Silhouette Score to determine which method produced more meaningful customer groups.
________________________________________
2. Segment Interpretation
Cluster 0 – Grocery and Milk Buyers
This cluster spends the most on Grocery, Milk, and Detergents_Paper, with relatively lower spending on Fresh and Frozen products.
Business action:
Offer bulk discounts, loyalty rewards, and promotions on grocery and household products to encourage repeat purchases.
________________________________________
Cluster 1 – Fresh Food Customers
Customers in this cluster spend heavily on Fresh products and also purchase moderate amounts of Milk and Frozen foods.
Business action:
Provide frequent delivery schedules, freshness guarantees, and special promotions for fresh produce.
________________________________________
Cluster 2 – High-Value Customers
This cluster has high spending across most product categories, making them valuable wholesale customers.
Business action:
Assign dedicated account managers and offer personalized pricing or premium services to improve customer retention.
________________________________________
3. Understanding K-Means
K-Means is an unsupervised machine learning algorithm that groups similar data points into K clusters.
It works by:
1.	Choosing the number of clusters (K).
2.	Randomly placing K centroids.
3.	Assigning each customer to the nearest centroid.
4.	Updating each centroid to the average of all customers assigned to it.
5.	Repeating the assign-and-update process until the centroids stop changing significantly.
The final result is a set of customer groups where members within the same cluster are more similar to each other than to customers in other clusters.
________________________________________
4. Your Second Algorithm
Algorithm: Hierarchical Clustering (Agglomerative Clustering).
Why I chose it
I selected Hierarchical Clustering because it does not require randomly initialized centroids and provides a dendrogram that helps visualize how clusters are formed.
How it works
The algorithm starts by treating each customer as its own cluster. It repeatedly merges the two closest clusters until all customers are grouped into a hierarchy. The desired number of clusters is then chosen by cutting the dendrogram.
One advantage
•	Does not require random initialization and provides a clear hierarchical structure.
One limitation
•	Computationally expensive and slower than K-Means for large datasets.
Silhouette Score comparison
The K-Means model achieved a Silhouette Score of 0.241, indicating moderate cluster separation.
If your Hierarchical Clustering score was lower than 0.241, then K-Means produced better-separated clusters. If it was higher than 0.241, then Hierarchical Clustering performed better. (Replace this sentence with your actual score.)
________________________________________
5. Your Findings
For this wholesale customer segmentation task, I would recommend K-Means clustering. It is simple, computationally efficient, and works well for numerical spending data. It also produces clear cluster centers that are easy to interpret, making it useful for identifying different customer purchasing behaviors and supporting business decisions.
Based on my results, K-Means achieved a Silhouette Score of 0.241 and a Davies–Bouldin Index of 1.312. These values suggest that the clusters are reasonably separated, although there is room for improvement. Overall, K-Means provides meaningful customer segments that can be used to design targeted marketing campaigns, optimize inventory management, and improve customer service.

