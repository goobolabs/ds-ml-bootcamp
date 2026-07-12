# Reflection Paper

## Assignment Six – Clustering: Theory and Practice

### 1. What did you implement?

In this assignment, I implemented a customer segmentation project using the Wholesale Customers dataset. The dataset contains customers' annual spending on six product categories: Fresh, Milk, Grocery, Frozen, Detergents_Paper, and Delicassen. Before applying clustering algorithms, I cleaned the data by applying IQR capping to reduce the effect of extreme outliers. I then standardized the features using StandardScaler because the spending values have different ranges.

The first clustering algorithm I implemented was K-Means, using five clusters as suggested by the Elbow Method. After training the model, I evaluated it using the Silhouette Score and the Davies–Bouldin Index. I also converted the cluster centers back to the original spending units to make the results easier to interpret.

For the second method, I implemented Agglomerative Clustering. I selected this algorithm because it is a hierarchical clustering technique that groups customers based on their similarities without relying on randomly initialized centroids. Finally, I compared the Silhouette Scores of both algorithms to determine which method produced better-separated customer groups.



## 2. Segment Interpretation

The clustering results showed that customers have different purchasing behaviors.

One cluster contained customers who spent large amounts on Fresh and Frozen products. These customers are likely to be restaurants, hotels, or catering businesses that require fresh food regularly. A suitable business strategy would be to provide discounts on fresh food products and create loyalty programs for frequent buyers.

Another cluster showed customers with high spending on Grocery and Detergents_Paper. These customers are likely supermarkets or retail stores that purchase packaged food and cleaning products in large quantities. The distributor could offer bulk purchase discounts and long-term supply contracts to strengthen customer relationships.

A third cluster represented customers with relatively low spending across most product categories. These customers may be small shops or occasional buyers. The distributor could encourage higher spending by offering promotional packages and personalized marketing campaigns.



## 3. Understanding K-Means

K-Means is an unsupervised machine learning algorithm used to divide data into a specified number of clusters. The algorithm begins by selecting k initial centroids. Each customer is assigned to the nearest centroid based on distance. After all customers are assigned, the centroids are recalculated using the average values of the assigned points. This assign-and-update process continues until the centroids no longer change significantly or the algorithm reaches convergence.

The objective of K-Means is to minimize the distance between customers and the centroids of their assigned clusters. This creates groups in which customers have similar purchasing behaviors.



## 4. My Second Algorithm

For this assignment, I selected Agglomerative Clustering as the second clustering algorithm. I chose this method because it creates clusters hierarchically and does not depend on random centroid initialization. It starts by treating each customer as an individual cluster and repeatedly merges the closest clusters until the required number of clusters is reached.

From my research, I learned that Agglomerative Clustering is useful for understanding the relationships among clusters and can reveal hierarchical structures in the data. One advantage is that it provides stable clustering results without random initialization. One limitation is that it becomes computationally expensive for very large datasets.

After comparing the Silhouette Scores, I observed that one of the algorithms produced better-separated clusters. This comparison helped me understand that different clustering algorithms can produce different segmentation results even when they use the same dataset.



## 5. My Findings

This assignment helped me understand how clustering can be applied to real business problems such as customer segmentation. Data preprocessing, including outlier handling and feature scaling, played an important role in improving clustering performance. I also learned that selecting appropriate evaluation metrics, such as the Silhouette Score and Davies–Bouldin Index, is essential for assessing clustering quality.

Overall, I would recommend K-Means for this wholesale customer segmentation task because it is simple, efficient, and performs well on numerical spending data after proper preprocessing. It is easy to interpret and provides meaningful customer groups that businesses can use for marketing and decision-making. However, Agglomerative Clustering is also valuable because it reveals hierarchical relationships among customers and serves as a useful alternative for comparing clustering results.



## Conclusion

Through this assignment, I gained practical experience in customer segmentation using unsupervised machine learning. I successfully implemented K-Means and Agglomerative Clustering, evaluated their performance using clustering metrics, and interpreted the resulting customer segments. This project improved my understanding of clustering techniques and demonstrated how machine learning can support better business decisions through data-driven customer analysis.