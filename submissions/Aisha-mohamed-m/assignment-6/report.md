# Project Report: Wholesale Customer Segmentation using K-Means

## 1. Executive Summary

The main objective of this project is to analyze wholesale customer transaction data from the dataset **raw_wholesale_customers.csv** and identify different customer groups based on their annual spending patterns across multiple product categories.

To achieve this goal, the **K-Means Clustering algorithm** was applied, which is an unsupervised machine learning technique used to divide data points into meaningful groups. The clustering process separated customers into three distinct segments with similar purchasing behaviors.

The results of this project can help businesses understand customer needs, create targeted marketing strategies, improve inventory planning, and provide customized services for different customer groups.

---

## 2. Data Preprocessing

Before applying the K-Means clustering algorithm, the dataset was prepared through important preprocessing steps to improve model performance.

### Outlier Handling (IQR Capping)

Customer purchasing data may contain extremely high or low values that can negatively affect clustering results. To reduce the impact of these extreme values, the Interquartile Range (IQR) method was used.

Values beyond **1.5 × IQR** from the first and third quartiles were identified and capped using the `.clip()` method. This helped prevent unusual spending values from dominating the cluster formation process.

### Feature Scaling (Standardization)

The product categories in the dataset have different monetary ranges. For example, some customers may spend much more on Grocery products than on other categories.

To solve this problem, **StandardScaler** was applied. This transformation converted all features into a standard normal distribution with a mean of 0 and a variance of 1.

Scaling ensured that every feature contributed equally during the distance calculations used by the K-Means algorithm.

---

## 3. Optimal Cluster Selection (Choosing k)

The Elbow Method was used to determine the best number of clusters for the dataset. Different values of k were tested from 1 to 10 clusters, and the Sum of Squared Errors (SSE), also known as Inertia, was measured.

The main results were:

 Number of Clusters (k)  SSE (Inertia) 

 k = 1                   2640.00       
 k = 2                   1728.19       
 k = 3                   1363.45       
 k = 4                   1202.41       

Based on the Elbow Method results, **k = 3** was selected as the optimal number of clusters. The graph showed a clear elbow point at three clusters, after which the improvement became smaller.

Therefore, the customer base was divided into three main segments.



## 4. Cluster Evaluation Metrics

To evaluate the quality of the generated clusters, two unsupervised learning evaluation metrics were calculated.

### Silhouette Score

The Silhouette Score obtained was:

**0.340**

This indicates that the clusters have reasonable separation, although some customers may have similar characteristics between groups.

### Davies–Bouldin Index

The Davies–Bouldin Index value was:

**1.297**

A lower Davies–Bouldin value represents better clustering quality. This result shows that the created clusters are reasonably separated and well-defined.



## 5. Cluster Profiling and Analysis

After creating the clusters, the cluster centers were converted back into their original monetary scale using the inverse transformation method. This allowed the business to understand the spending behavior of each customer group.

### Cluster 0: Grocers and Large Retail Outlets

This cluster represents customers with high spending on:

* Grocery products
* Detergents and Paper products
* Milk products

These customers are likely to be large retailers or grocery stores that purchase large quantities of non-perishable goods and household supplies.



### Cluster 1: Small Retail and Convenience Stores

This group contains customers with lower overall spending compared with the other clusters.

Their purchases are distributed more evenly across different product categories. These customers represent small shops or convenience stores with regular but limited purchasing needs.



### Cluster 2: Restaurants, Hotels, and Cafés

This cluster shows very high spending on:

* Fresh products
* Frozen products
* Delicassen items

These customers are likely businesses in the hospitality industry that require large amounts of fresh and specialty products for daily operations.



## 6. Conclusion

The K-Means clustering algorithm successfully divided wholesale customers into three meaningful segments based on their purchasing behavior.

The final dataset, **segmented_wholesale_customer.csv**, contains customer labels assigned according to their cluster membership.

These results can be integrated into Customer Relationship Management (CRM) systems to support personalized marketing campaigns, improve customer service, and optimize business decisions.

By understanding different customer segments, companies can create more effective strategies and provide services that match the needs of each customer group.


