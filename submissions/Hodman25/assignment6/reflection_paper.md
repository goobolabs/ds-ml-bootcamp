# Wholesale Customer Segmentation Using K-Means and DBSCAN

## What I Implemented

 I implemented customer segmentation on the Wholesale Customers dataset using two unsupervised machine learning algorithms: **K-Means** and **DBSCAN**. The goal was to group customers based on their purchasing behavior across the following six spending categories:

- Fresh
- Milk
- Grocery
- Frozen
- Detergents_Paper
- Delicassen

Before clustering, I prepared the data by capping extreme outliers using the **Interquartile Range (IQR)** method and standardizing the six spending features with **StandardScaler**. Standardization ensures that each feature contributes equally to the clustering process.

I first applied the **Elbow Method** to determine a suitable number of clusters and selected **5 clusters** for K-Means. After training both K-Means and DBSCAN, I evaluated their performance using the **Silhouette Score** and **Davies-Bouldin Index**.


# Segment Interpretation

The K-Means cluster centers describe different purchasing patterns among wholesale customers.

## Cluster 2 – High-Value Customers

Customers in this cluster spend the highest amounts across almost every product category, especially:

- Fresh
- Milk
- Grocery
- Frozen
- Detergents_Paper
- Delicassen

These customers are likely the distributor's largest wholesale buyers.

**Business Action:**

Offer loyalty programs, premium customer support, and volume discounts to strengthen long-term relationships with these valuable customers.


## Cluster 3 – Fresh and Frozen Product Buyers

Customers in this cluster spend heavily on:

- Fresh products
- Frozen products

while spending relatively little on detergents and paper products.

These customers may represent restaurants, hotels, or food service businesses.

**Business Action:**

Create targeted promotions for fresh and frozen food bundles and provide seasonal discounts.



## Cluster 4 – Grocery and Household Supply Buyers

Customers in this cluster spend the most on:

- Grocery
- Milk
- Detergents & Paper

while spending less on Fresh and Frozen products.

These customers are likely supermarkets or grocery stores.

**Business Action:**

Provide bulk-order discounts and recommend complementary household products to increase sales.



# Understanding K-Means

K-Means is an unsupervised machine learning algorithm that groups similar data points into **k clusters**.

The algorithm works as follows:

1. Select the number of clusters (**k**).
2. Randomly initialize **k centroids**.
3. Assign each customer to the nearest centroid.
4. Recalculate each centroid as the average of all customers assigned to it.
5. Repeat the assignment and centroid update steps until the cluster assignments no longer change significantly.

The objective of K-Means is to minimize the distance between customers and the centroid of their assigned cluster, creating compact and well-separated groups.

---

# My Second Algorithm

The second clustering algorithm used in this assignment was **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**.

## Why I Chose DBSCAN

I selected DBSCAN because it does not require specifying the number of clusters before training. Instead, it groups customers based on the density of nearby data points and identifies unusual observations as noise (outliers).

## What I Learned

DBSCAN forms clusters by connecting points located in dense regions of the dataset. Any point that does not belong to a dense region is labeled as **noise (-1)** instead of being forced into a cluster.

### Advantage

- Automatically detects outliers.
- Does not require choosing the number of clusters beforehand.
- Can identify clusters with irregular shapes.

### Limitation

- Sensitive to the choice of **eps** and **min_samples** parameters.
- Performance decreases when clusters have different densities.

## Silhouette Score Comparison

| Algorithm | Silhouette Score |
|-----------|-----------------:|
| K-Means | **0.283** |
| DBSCAN | **0.283** |

Both algorithms achieved the same Silhouette Score, indicating similar overall cluster separation on this dataset.



# Findings

Both K-Means and DBSCAN successfully segmented wholesale customers based on their spending patterns. In this implementation, both algorithms achieved the same **Silhouette Score of 0.283**, suggesting comparable clustering quality according to this evaluation metric. However, the clustering results differed. K-Means assigned every customer to one of five clusters and produced cluster centers that clearly describe customer purchasing behavior. DBSCAN, on the other hand, identified some customers as noise (outliers), which can be useful for detecting unusual purchasing patterns.

Although both algorithms produced the same Silhouette Score, I would recommend **K-Means** for this wholesale customer segmentation task. The cluster centers are easy to interpret, making it simpler for businesses to develop targeted marketing campaigns, customer loyalty programs, and inventory management strategies. DBSCAN is valuable for identifying outliers, but its performance depends heavily on parameter selection and may produce clusters that are more difficult to interpret for business decision-making.