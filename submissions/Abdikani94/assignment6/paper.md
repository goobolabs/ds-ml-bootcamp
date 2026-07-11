# Assignment Six: Clustering — Theory

## 1. Introduction to Unsupervised Learning and Clustering

Unsupervised learning is when we give the model data without labels and let it find patterns on its own. There is no "correct answer" column to train against. The model just looks at the structure of the data and groups similar things together.

This is different from regression and classification, which are both supervised learning. In supervised learning we already know the answer for each row (a price, a class, yes/no) and we train the model to predict that answer for new data. In unsupervised learning we don't have that answer, we just want to understand the data better, for example by finding groups or reducing the number of features.

Real-life example of clustering: a store grouping its customers into segments like "big spenders", "occasional shoppers", "bargain hunters" based on purchase history, without anyone telling the model in advance who belongs where.

Real-life example of supervised learning: a bank predicting whether a loan applicant will default, based on past applicants where we already know who defaulted and who didn't.

## 2. Clustering Algorithms

**K-Means**
K-Means picks a number of clusters, k, then places k centers (centroids) in the data. Each point is assigned to the nearest centroid, then the centroids are moved to the average position of the points assigned to them. This repeats until the centroids stop moving much. It is used a lot in customer segmentation, like grouping wholesale customers by spending habits. It is fast and simple to understand, but you have to choose k yourself, and it struggles when clusters are not round or are very different in size.

**Hierarchical Clustering**
This method builds a tree of clusters instead of picking a fixed number upfront. The most common form (agglomerative) starts with every point as its own cluster, then keeps merging the two closest clusters together until everything is in one cluster. You can then "cut" the tree at any level to get the number of clusters you want. It's used for things like grouping genes with similar expression patterns in biology. Its advantage is you can see the whole merging structure (dendrogram) and decide the number of clusters after looking at it. Its limitation is that it gets slow on large datasets because it compares many pairs of points.

**DBSCAN**
DBSCAN groups points that are packed closely together (dense regions) and marks points that sit alone in low-density areas as noise/outliers. It doesn't need you to set the number of clusters in advance. It's used for things like finding unusual spending patterns or detecting anomalies in sensor data, since it naturally separates outliers. Its advantage is it can find clusters of any shape and it handles noise well. Its limitation is it's sensitive to its two parameters (eps and min_samples), and it struggles when clusters have very different densities.

## 3. Clustering Metrics

- **Elbow Method (SSE):** For each k, we calculate the sum of squared distances between each point and its cluster center (SSE, also called inertia). As k increases, SSE always goes down. We plot k against SSE and look for the point where the drop starts to flatten out (the "elbow"). That point is a good candidate for k.

- **Silhouette Score:** For each point, this measures how close it is to its own cluster compared to the nearest other cluster. It ranges from -1 to 1. A value close to 1 means the point fits well in its cluster and is far from other clusters. A value near 0 means the point is on the border between two clusters, and negative means it's probably in the wrong cluster.

- **Davies-Bouldin Index:** This compares the average distance inside each cluster to the distance between cluster centers. A lower value means clusters are tight and well separated from each other. A higher value means clusters overlap or are spread out too much.

| Metric | What it measures | Good value looks like |
|---|---|---|
| Elbow Method (SSE) | How much error is left inside clusters as k grows | The k where the curve bends and stops improving much |
| Silhouette Score | How well-matched a point is to its own cluster vs. others | Closer to +1 |
| Davies-Bouldin Index | Ratio of within-cluster spread to between-cluster distance | Lower value, closer to 0 |

## 4. Choosing k and Interpreting Segments

To choose k for K-Means, we usually run the elbow method first to get a rough idea, then check the silhouette score for a few candidate k values to see which one actually separates the clusters best. Sometimes business knowledge also matters — for example, if the company only wants to manage 3-4 customer types, that limits how big k should be.

In the wholesale distributor project, a cluster with high Fresh + Milk spend but low Grocery + Detergents_Paper spend usually looks like a HoReCa client (hotel, restaurant, cafe) — they buy perishable/fresh goods often because they cook and serve food daily. A cluster with high Grocery + Detergents_Paper spend usually looks like a retail client (supermarket/shop) — they stock shelf-stable goods and cleaning products in bulk.

We exclude Channel and Region from the clustering features because they are categorical labels, not spending behavior. If we included them, the clustering would just be grouping by an ID-like label instead of by how much the customer actually buys. We want the clusters to come purely from spending patterns so we can compare the result against Channel/Region afterward as a sanity check.

## 5. Real-World Case Study

A well known example is how retailers like Sephora and other beauty/retail chains use RFM (Recency, Frequency, Monetary) based K-Means clustering to segment customers for marketing. The goal is to group customers by how recently they bought, how often they buy, and how much they spend. The data used is transaction history (purchase dates and amounts) per customer. They apply K-Means (sometimes after scaling the RFM values) to split customers into segments like "loyal high spenders", "at-risk customers who used to buy often but stopped", and "new customers". The key insight from this kind of study is that a small percentage of customers (the loyal high spenders) usually generates a large share of revenue, so the company focuses retention campaigns and personalized offers on that segment, while sending win-back discounts to the "at-risk" segment. This is the same basic idea used in this assignment, just applied to a different type of purchase data (wholesale spend by category instead of RFM).
