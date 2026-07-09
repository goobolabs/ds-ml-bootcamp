# Assignment 6 -- Part A: Theory

## Clustering in Machine Learning

### Introduction to Unsupervised Learning and Clustering

Machine Learning can be divided into supervised learning and
unsupervised learning. **Unsupervised learning** is a type of machine
learning in which the algorithm learns patterns from data that has **no
labeled output**. Instead of predicting a known answer, it discovers
hidden structures, relationships, or groups in the dataset.

Clustering is one of the most common unsupervised learning techniques.
It groups similar data points into clusters so that items within the
same cluster are more similar to each other than to items in other
clusters. Businesses, healthcare organizations, and researchers use
clustering to understand data and make better decisions.

### Difference Between Unsupervised Learning, Regression, and Classification

Regression and classification are supervised learning methods because
they require labeled training data.

-   **Regression** predicts continuous numerical values, such as house
    prices or sales.
-   **Classification** predicts categories, such as spam or not spam.
-   **Unsupervised learning** does not use labels. It finds patterns and
    groups automatically.

**Real-life clustering example:** A supermarket groups customers
according to their purchasing behavior for targeted marketing.

**Real-life supervised learning example:** A bank predicts whether a
loan applicant will default using historical labeled data.

# Clustering Algorithms

## 1. K-Means

**Basic idea:** K-Means divides data into K clusters. It starts with K
centroids, assigns each point to the nearest centroid, recalculates the
centroids, and repeats until the clusters become stable.

**Use case:** Customer segmentation in retail.

**Advantages** - Simple and fast. - Works well on large datasets. - Easy
to interpret.

**Limitations** - K must be chosen before training. - Sensitive to
outliers. - Assumes roughly spherical clusters.

## 2. Hierarchical Clustering

**Basic idea:** Hierarchical clustering builds a hierarchy of clusters.
Agglomerative clustering starts with each point as its own cluster and
repeatedly merges the closest clusters until a stopping point is
reached.

**Use case:** Gene analysis, document organization, and small customer
datasets.

**Advantages** - No need to choose K at the beginning. - Produces a
dendrogram for visualization. - Works well with small datasets.

**Limitations** - Computationally expensive for large datasets. -
Difficult to undo incorrect merges.

## 3. DBSCAN

**Basic idea:** DBSCAN groups points based on density. Areas with many
nearby points form clusters, while isolated points are treated as noise
or outliers.

**Use case:** GPS location analysis, fraud detection, and anomaly
detection.

**Advantages** - Finds clusters of different shapes. - Detects outliers
automatically. - Does not require choosing K.

**Limitations** - Choosing the parameters (eps and MinPts) can be
difficult. - Performance decreases when data densities vary greatly.

# Clustering Metrics

## Elbow Method (SSE)

The Elbow Method uses the **Sum of Squared Errors (SSE)**. SSE measures
the distance between data points and their cluster centroids. Lower SSE
means tighter clusters. The best K is usually found at the "elbow,"
where further increases in K provide only small improvements.

## Silhouette Score

The Silhouette Score measures how similar a point is to its own cluster
compared to other clusters. Values range from **-1 to 1**. - Close to 1
= excellent clustering. - Around 0 = overlapping clusters. - Less than 0
= poor clustering.

## Davies--Bouldin Index

The Davies--Bouldin Index measures cluster similarity. It compares the
distance between clusters with the spread inside each cluster.

Lower values indicate better clustering because clusters are compact and
well separated.

## Comparison Table

  ------------------------------------------------------------------------
  Metric            What it Measures                 Good Value
  ----------------- -------------------------------- ---------------------
  Elbow Method      Total within-cluster error       Lower SSE with a
  (SSE)                                              clear elbow

  Silhouette Score  Separation and cohesion          Close to 1

  Davies--Bouldin   Cluster similarity               As low as possible
  Index                                              
  ------------------------------------------------------------------------

# Choosing K and Interpreting Segments

## Choosing the Number of Clusters

The number of clusters in K-Means is commonly selected using: - The
Elbow Method. - The Silhouette Score. - Business knowledge and domain
expertise.

These methods help balance model simplicity and clustering quality.

## Interpreting Wholesale Customer Segments

A cluster with **high Fresh and Milk spending** represents customers who
mainly purchase fresh food and dairy products. These may include
restaurants, hotels, and food service businesses.

A cluster with **high Grocery and Detergents_Paper spending** represents
customers who buy packaged grocery products and cleaning supplies. These
customers are often supermarkets, convenience stores, or retail shops.

## Why Exclude Channel and Region?

Channel and Region are excluded because clustering should be based only
on customer purchasing behavior. These columns describe customer
categories instead of spending patterns. Including them may bias the
clustering results and reduce the quality of customer segmentation.

# Real-World Case Study

A well-known application of clustering is customer segmentation in
retail. Retail companies collect customer transaction data, including
purchase frequency, spending amount, and product categories.

The goal is to identify groups of customers with similar buying
behavior. Many studies use K-Means clustering because it is simple and
efficient for large datasets.

After clustering, businesses discover groups such as high-value
customers, occasional buyers, and discount-focused shoppers. These
insights help companies improve marketing campaigns, personalize
promotions, manage inventory, and increase customer satisfaction and
profitability.

# Conclusion

Clustering is an important unsupervised learning technique for
discovering hidden patterns in data. K-Means, Hierarchical Clustering,
and DBSCAN each have strengths and weaknesses. Choosing the correct
algorithm and evaluation metric depends on the dataset and business
objective. In customer segmentation, clustering helps organizations
understand customer behavior and make better strategic decisions.


