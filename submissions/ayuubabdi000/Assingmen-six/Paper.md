# Introduction to Unsupervised Learning and Clustering

## What is Unsupervised Learning in Machine Learning?

Unsupervised learning is a type of Machine Learning where a computer learns from data without having correct answers or labels provided. The main purpose is to discover hidden patterns, relationships, or groups inside the data.

One common method of unsupervised learning is clustering. Clustering groups similar data points together so that we can better understand the structure of the data.

## Difference Between Unsupervised Learning, Regression, and Classification

Unsupervised learning is different from supervised learning methods such as regression and classification.

- Unsupervised learning uses data without labels and tries to find patterns automatically.
- Classification uses labeled data to predict categories. For example, deciding whether an email is spam or not spam.
- Regression uses labeled data to predict a continuous value. For example, predicting the price of a house.

### Real-Life Examples

A clustering example is a supermarket grouping customers based on their shopping habits. Some customers may buy more fresh food, while others may buy more household products.

A supervised learning example is a bank predicting whether a customer will receive a loan based on previous customer information.

---

# Clustering Algorithms

## 1. K-Means Clustering

### How It Works

K-Means is one of the most common clustering algorithms. It divides data into a selected number of groups called clusters. Each cluster has a center point called a centroid. Data points are assigned to the closest centroid, and the centroids are updated until the clusters become stable.

### Real-World Use Case

Companies use K-Means to divide customers into groups based on spending behavior. This helps businesses create better marketing strategies.

### Advantages

- Easy to understand and implement.
- Works quickly with large datasets.
- Useful for finding clear customer groups.

### Limitations

- The number of clusters must be selected before starting.
- It can be affected by outliers.
- It works best when clusters have similar shapes.

---

## 2. Hierarchical Clustering

### How It Works

Hierarchical clustering creates groups by building a tree-like structure called a dendrogram. It starts with each data point as a separate group and slowly combines similar groups together.

### Real-World Use Case

Hospitals can use hierarchical clustering to group patients with similar medical conditions.

### Advantages

- The number of clusters does not need to be chosen at the beginning.
- It shows the relationship between different groups.
- Useful for smaller datasets.

### Limitations

- It can become slow with large amounts of data.
- It can be affected by noise and unusual data points.
- Results may require human interpretation.

---

## 3. DBSCAN

### How It Works

DBSCAN creates clusters by finding areas where many data points are close together. It can also identify points that do not belong to any group and treat them as noise.

### Real-World Use Case

DBSCAN can be used to find areas with high customer activity in geographic data.

### Advantages

- Does not require the number of clusters in advance.
- Can detect clusters with unusual shapes.
- Handles outliers better than K-Means.

### Limitations

- Choosing the correct settings can be difficult.
- It may not work well when data groups have different densities.
- It is less suitable for very large and complex datasets.

---

# Clustering Metrics

Clustering metrics are used to check how good the created clusters are.

| Metric | What It Measures | Good Result |
|--------|------------------|-------------|
| Elbow Method (SSE) | Measures the distance between data points and their cluster centers. | The best point is where improvement starts slowing down (the elbow point). |
| Silhouette Score | Measures how well each data point fits into its own cluster compared with others. | A value closer to 1 is better. |
| Davies-Bouldin Index | Measures how similar clusters are to each other. | Lower values mean better clusters. |

## Elbow Method (SSE)

The Elbow Method helps choose the best number of clusters for K-Means. It calculates the total distance between points and their cluster centers. When adding more clusters stops giving major improvement, that point is usually selected as the best number of clusters.

## Silhouette Score

The Silhouette Score checks whether data points are correctly placed in their clusters. A high score means the clusters are separated well and the data points fit their groups.

## Davies-Bouldin Index

The Davies-Bouldin Index measures how close clusters are to each other. A lower score means the clusters are more different and better separated.

---

# Choosing k and Understanding Customer Segments

## How to Choose the Number of Clusters for K-Means

Choosing the correct number of clusters is important. Common methods include:

- Using the Elbow Method to find where adding more clusters gives less improvement.
- Using the Silhouette Score to find the best-separated clusters.
- Considering business needs and whether the groups are useful in real situations.

## Meaning of Wholesale Distributor Clusters

In a wholesale distributor project:

A cluster with high Fresh and Milk spending usually represents customers such as restaurants or businesses that need fresh products regularly.

A cluster with high Grocery and Detergents_Paper spending represents customers who mainly purchase packaged food and household items.

These clusters help the company understand different customer types and plan better business strategies.

## Why Are Channel and Region Removed?

Channel and Region are not included because they are categories, not measures of customer purchasing behavior. Including them could make the algorithm group customers based on location or business type instead of their actual spending habits.

The purpose of clustering is to discover natural customer groups based on meaningful patterns.

---

# Real-World Case Study: Customer Segmentation in Retail

## Goal of the Project

A retail company used clustering to understand its customers better. The main goal was to identify different customer groups and improve marketing decisions.

## Data Used

The company collected information such as:

- Customer purchase history
- Amount of money spent
- Frequency of purchases
- Types of products purchased

## Clustering Method Used

The company applied K-Means clustering to divide customers into different groups. Each group contained customers with similar shopping behaviors.

## Key Results and Insights

The analysis identified different customer groups, including:

- High-value customers who spent more money.
- Regular customers who purchased often.
- Customers interested in specific product categories.

The company used these results to create personalized offers, improve customer relationships, and increase sales.

Clustering is useful in business because it helps companies understand customers even when the categories are not known before analysis.

