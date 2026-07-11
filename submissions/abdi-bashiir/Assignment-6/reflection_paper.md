# Reflection Paper

## Introduction

In this assignment, I learned how to perform customer segmentation using unsupervised machine learning techniques. The main objective was to group wholesale customers based on their purchasing behavior without using predefined labels. I reproduced the Lesson 6 clustering pipeline using K-Means and then researched and implemented Agglomerative Clustering as a second clustering method.

## Data Preparation

The first step was loading the wholesale customer dataset and selecting only the six spending features: Fresh, Milk, Grocery, Frozen, Detergents_Paper, and Delicassen. I did not use the Channel and Region columns as clustering features because they are categorical variables and could introduce bias into the clustering process.

Before training the models, I applied IQR capping to reduce the effect of extreme outliers while keeping all customers in the dataset. After that, I standardized the selected features using StandardScaler so that each feature contributed equally to the clustering process.

## K-Means Clustering

I used the Elbow Method to observe how the Sum of Squared Errors (SSE) changed for different values of k. Following the lesson instructions, I trained a K-Means model with five clusters.

To evaluate the model, I calculated the Silhouette Score and the Davies–Bouldin Index. I also transformed the cluster centers back into the original spending units using the inverse transformation of the scaler, making the results easier to interpret.

## Understanding How K-Means Works

K-Means is an iterative clustering algorithm. First, it randomly selects **k** initial centroids. Each customer is then assigned to the nearest centroid based on the distance between the customer and the centroid. After all customers have been assigned, the centroids are updated by calculating the mean of all data points within each cluster. This assign-and-update process continues until the centroids no longer change significantly or the maximum number of iterations is reached.

## Agglomerative Clustering

As an additional clustering method, I implemented Agglomerative Clustering. Unlike K-Means, which partitions the data directly into clusters, Agglomerative Clustering builds clusters gradually by merging similar observations.

I chose this algorithm because it can reveal natural hierarchical relationships between customers and provides a useful comparison with K-Means.

One advantage of Agglomerative Clustering is that it does not rely on randomly initialized centroids and can reveal hierarchical relationships between customers. However, one limitation is that it is computationally more expensive than K-Means on large datasets, making it less suitable for very large customer databases.

## Comparison of the Methods

I compared the Silhouette Scores produced by K-Means and Agglomerative Clustering. The comparison showed which algorithm created better-separated customer groups for this dataset.

Based on the evaluation results, the algorithm with the higher Silhouette Score produced more distinct and compact clusters. In my implementation, **K-Means achieved better cluster separation than Agglomerative Clustering**, making it the preferred method for this wholesale customer segmentation task.


## Segment Interpretation

The K-Means model grouped wholesale customers into five different clusters based on their purchasing behavior.

One cluster contained customers who spent a large amount on Fresh products. These customers may represent restaurants, hotels, or businesses that regularly purchase fresh food. A suitable business action would be to offer discounts on fresh products and provide faster delivery services.

Another cluster showed customers with high spending on Grocery and Detergents_Paper. These customers are likely to be supermarkets or retail stores. The distributor could provide bulk purchase discounts and loyalty programs to encourage larger and more frequent orders.

A third cluster contained customers with relatively low spending across most product categories. These customers could be targeted with promotional offers and personalized marketing campaigns to increase their purchasing activity.

## Challenges

One challenge I encountered was understanding how clustering differs from supervised learning because clustering has no target variable. Another challenge was selecting only the correct features and preparing the data properly before applying the algorithms. I also learned the importance of feature scaling because clustering algorithms are sensitive to differences in feature scales.

## Conclusion

This assignment improved my understanding of unsupervised learning and customer segmentation. I learned how to preprocess data using IQR capping and StandardScaler, apply K-Means and Agglomerative Clustering, evaluate clustering quality using the Silhouette Score and Davies–Bouldin Index, and interpret customer segments for business decision-making. Overall, this assignment strengthened both my theoretical understanding and my practical skills in clustering techniques, and it showed me how machine learning can help businesses better understand customer behavior.