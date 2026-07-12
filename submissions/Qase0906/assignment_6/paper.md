# Part A — Theory

## 1. Introduction to Unsupervised Learning and Clustering

- **Unsupervised Learning**: is a type of Machine Learning in which the Model learns patterns from data without labelled outputs. Unlike supervised learning, the algorithm learns without being given the correct answers in training. Instead, it analyses the data and finds hidden structures, relationships or similarities among the observations.
- Regression and classification are both examples of supervised learning, meaning they require labeled training data.
**Regression** predicts a continuous numerical value, such as house prices or sales revenue.
**Classification** predicts a category or class, such as whether an email is spam or not spam.
**Unsupervised** learning does not use labels. Instead, it finds hidden patterns, groups, or structures within the data.
- **Real-Life Examples**

    Clustering Example

    A supermarket may use clustering to group customers based on their purchasing behavior. Customers who buy similar products are placed into the same cluster, allowing the business to create personalized marketing campaigns.

    Supervised Learning Example

    A bank may build a classification model to predict whether a customer will repay a loan using previous loan records with known outcomes.

## 2. Clustering Algorithms

**A. K-Means Clustering**

**How It Works**

    K-Means divides the data into k clusters. It starts by selecting k random centroids. Each data point is assigned to the nearest centroid. The centroids are then updated based on the average position of all points in each cluster. This process repeats until the centroids stop changing significantly.

*Real-World Use Case*
*Retail companies use K-Means to segment customers according to their purchasing behavior for targeted promotions.*

*Advantages*
- Simple and easy to understand.
- Fast on large datasets.
- Works well when clusters are compact and roughly circular.

*Limitations*
- The number of clusters (k) must be chosen beforehand.
- Sensitive to outliers.
- Performs poorly when clusters have irregular shapes.


**B. Hierarchical Clustering**

*How It Works*
    Hierarchical clustering builds a tree-like structure called a dendrogram. In agglomerative clustering, each data point starts as its own cluster, and the closest clusters are repeatedly merged until all points belong to one cluster.

*Real-World Use Case*

    *Biologists use hierarchical clustering to group genes with similar expression patterns.*

*Advantages*
- Does not require choosing the number of clusters before training.
- Produces a dendrogram that helps visualize relationships.
- Can detect nested cluster structures.

*Limitations*
- Computationally expensive for large datasets.
- Sensitive to noise and outliers.
- Once clusters are merged, they cannot be separated later.



**C. DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
How It Works**

*DBSCAN groups together points that are located in dense regions while marking isolated points as noise or outliers. It uses two important parameters:*

Epsilon (ε): neighborhood radius.
MinPts: minimum number of nearby points required to form a cluster.

*Real-World Use Case*

GPS applications use DBSCAN to identify traffic hotspots and crowded locations.

*Advantages*
- Does not require specifying the number of clusters.
- Detects clusters with irregular shapes.
- Identifies outliers automatically.

*Limitations*
- Choosing appropriate parameter values can be difficult.
- Performance decreases when data density varies greatly.
- Less effective in high-dimensional datasets.


## 3. Clustering Metrics

   Clustering metrics help evaluate how well the data has been grouped.

**Elbow Method (SSE)**

The Elbow Method uses the Sum of Squared Errors (SSE), which measures the distance between each data point and its assigned cluster center.

As the number of clusters increases, SSE decreases. The best value of k is usually found at the "elbow" point where the decrease in SSE becomes much smaller.

Good Result: A clear elbow in the graph.

**Silhouette Score**

The Silhouette Score measures how similar each point is to its own cluster compared to other clusters.

The score ranges from -1 to 1.

1 = excellent clustering
0 = overlapping clusters
Negative values = many points assigned to the wrong cluster

Good Result: Close to 1.

**Davies–Bouldin Index**

The Davies–Bouldin Index measures the average similarity between each cluster and its most similar neighboring cluster.

Lower values indicate clusters that are compact and well separated.

Good Result: Close to 0.


## Comparison Table

| Metric | What It Measures | Good Value |
|--------|-------------------|------------|
| Elbow Method (SSE) | Total distance between data points and their assigned cluster centers. Used to help choose the optimal number of clusters. | A clear **elbow point** where SSE begins to decrease more slowly. |
| Silhouette Score | How well data points fit within their own cluster compared to other clusters. Measures cluster separation and cohesion. | Close to **1** (higher is better). |
| Davies–Bouldin Index | The average similarity between each cluster and its most similar neighboring cluster. Measures cluster compactness and separation. | Close to **0** (lower is better). |




## 4. Choosing k and Interpreting Segments

I have Used this two techniques to choose the best value of k for K-Means:

- Used the Elbow Method to find where SSE begins to level off.
- Compared different values of k using the Silhouette Score.

**High Fresh + Milk Spending**

Customers in this cluster spend large amounts on fresh food and dairy products. These customers are often restaurants, hotels, cafes, or food service businesses that require fresh products regularly.

**High Grocery + Detergents_Paper Spending**

Customers in this cluster spend more on packaged groceries, cleaning supplies, and paper products. They are more likely to be supermarkets, grocery stores, or retail shops that sell household products.

**Why Exclude Channel and Region?**

    The variables Channel and Region already describe known categories.
    Including them in clustering would influence the algorithm to group customers based on existing labels rather than discovering natural purchasing patterns.

## 5. Real-World Case Study

Customer Segmentation Using K-Means in Retail

One widely known application of clustering is customer segmentation in retail businesses. A common example uses the Online Retail transaction dataset from the UCI Machine Learning Repository.

**Goal**

The objective was to group customers according to their purchasing behavior so that the company could improve marketing strategies, customer retention, and personalized recommendations.

Data Used

The project used customer transaction data, including:

- Purchase frequency
- Total spending
- Quantity purchased
- Recency of purchases

These variables were used to calculate customer behavior measures before clustering.

**Clustering Method**

Researchers applied K-Means clustering after preprocessing and scaling the data. The Elbow Method and Silhouette Score helped determine the appropriate number of clusters.

**Key Results**

The clustering identified several distinct customer groups, including:

- High-value loyal customers
- Frequent but low-spending customers
- Occasional shoppers
- Customers at risk of leaving


**References**
- Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow. Aurélien Géron. (2022).
- UCI Machine Learning Repository. Online Retail Dataset.

