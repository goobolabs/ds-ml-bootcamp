# Assignment Six: Clustering — Theory


## 1. Introduction to Unsupervised Learning and Clustering

Unsupervised learning is a type of Machine Learning where the model is trained on data without a known target label. In supervised learning, the model learns from examples that already contain the correct answer, such as a house price, a loan approval result, or a student pass/fail label. In unsupervised learning, the model only receives the input features and must discover hidden patterns by itself.

Clustering is one of the most common unsupervised learning tasks. It groups similar rows together so that items inside the same group are more similar to each other than to items in other groups. In this assignment, clustering is used to segment wholesale customers based on their annual spending behavior. The model does not know the customer type in advance. It only sees spending values such as Fresh, Milk, Grocery, Frozen, Detergents_Paper, and Delicassen, then tries to discover customer groups.

The main difference between clustering and supervised learning is the presence of a target column. In regression, the target is a continuous number, such as predicting a car price. In classification, the target is a category, such as predicting whether a loan is approved or rejected. In clustering, there is no target column. The goal is not to predict an answer, but to understand the structure of the data.

A real-life example of clustering is customer segmentation in a supermarket. Customers can be grouped into high-value buyers, discount buyers, fresh-food buyers, or occasional buyers based on their purchase history. A real-life example of supervised learning is a bank predicting whether a customer will repay a loan using previous labeled loan records.

---

## 2. Clustering Algorithms

### K-Means Clustering

K-Means is a centroid-based clustering algorithm. The user first chooses the number of clusters, called **k**. The algorithm then creates cluster centers, called centroids, and assigns each data point to the closest centroid. After assigning points, it updates each centroid by taking the mean of the points inside that cluster. This assign-and-update process repeats until the centroids become stable.

K-Means is useful for customer segmentation because it can divide customers into groups based on numeric behavior, such as spending amounts. In the wholesale customer project, K-Means can group clients who buy mostly fresh products, grocery products, or mixed products.

The main advantage of K-Means is that it is simple, fast, and easy to understand. It works well when clusters are fairly compact and numeric features are properly scaled. Its main limitation is that the number of clusters must be chosen before training. It is also sensitive to outliers and feature scale, which is why preprocessing steps such as IQR capping and StandardScaler are important. The scikit-learn documentation explains that K-Means separates samples into a selected number of groups and minimizes inertia, also called within-cluster sum of squares [1].

### Hierarchical Clustering

Hierarchical clustering builds clusters step by step in a tree-like structure. The most common version is **Agglomerative Clustering**, which starts by treating each observation as its own cluster. Then it repeatedly merges the most similar clusters until the required number of clusters is reached. The result can be represented as a dendrogram, which shows how clusters are connected at different levels.

A real-world use case of hierarchical clustering is grouping customers, products, or documents when we want to understand the relationship between groups. For example, a business may use it to see which types of customers are closely related based on buying behavior.

The advantage of hierarchical clustering is that it gives a more visual and structured way to understand data. It does not depend on random starting centroids like K-Means. However, it can be slower on large datasets, and choosing the final number of clusters may still require judgment. In scikit-learn, AgglomerativeClustering uses a bottom-up approach where each observation starts as its own cluster and clusters are merged successively [2].

### DBSCAN

DBSCAN stands for Density-Based Spatial Clustering of Applications with Noise. Unlike K-Means, DBSCAN does not require the user to choose the number of clusters in advance. Instead, it finds dense areas of points and treats them as clusters. Points that are far away from dense areas can be marked as noise or outliers.

A real-world use case for DBSCAN is detecting unusual behavior, such as fraud detection, location-based customer groups, or identifying abnormal records in a dataset. For example, if most customers follow normal spending patterns but a few are very different, DBSCAN can help identify those unusual customers.

The advantage of DBSCAN is that it can find clusters with different shapes and can detect outliers. Its main limitation is that it depends heavily on two parameters: `eps` and `min_samples`. If these are not chosen well, the results may be poor. DBSCAN can also struggle when the dataset has clusters with very different densities. The scikit-learn documentation describes DBSCAN as a method that views clusters as high-density areas separated by low-density areas [3].

### Algorithm Comparison

| Algorithm | Basic Idea | Advantage | Limitation |
|---|---|---|---|
| K-Means | Groups data around centroids | Fast and easy to interpret | Must choose k; sensitive to scale and outliers |
| Hierarchical / Agglomerative | Merges similar points or clusters step by step | Shows relationships between groups | Can be slower; interpretation may be harder |
| DBSCAN | Finds dense regions and marks noise | Handles outliers and irregular shapes | Parameter selection can be difficult |

---

## 3. Clustering Metrics

Because clustering has no true target label, it cannot be evaluated with accuracy, precision, recall, or F1-score. Instead, we use internal clustering metrics that measure how compact and separated the clusters are.

### Elbow Method and SSE

The Elbow Method is mainly used with K-Means to help choose the value of **k**. We train K-Means several times using different values of k, such as k = 1 to 10. For each k, we record SSE, also called inertia. SSE measures the total squared distance between each point and its assigned cluster centroid. Lower SSE means points are closer to their centroids.

However, SSE always decreases when k increases, because more clusters usually mean each point can be closer to a centroid. The goal is to find the “elbow” point where adding more clusters no longer gives a large improvement. This point is often a reasonable choice for k.

### Silhouette Score

Silhouette Score measures how well each point fits inside its assigned cluster compared with the nearest other cluster. It ranges from -1 to +1. A score close to +1 means the clusters are well separated. A score close to 0 means the clusters overlap. A negative score suggests some points may be assigned to the wrong cluster. According to scikit-learn, a higher Silhouette Coefficient relates to better-defined clusters, while scores around zero indicate overlapping clusters [4].

### Davies–Bouldin Index

The Davies–Bouldin Index measures the average similarity between clusters. It compares the size of clusters with the distance between them. A lower Davies–Bouldin Index means better clustering because the clusters are more separated and less similar to each other. The best possible value is 0, and values closer to 0 indicate a better partition [5].

### Metric Comparison Table

| Metric | What It Measures | Good Value Means |
|---|---|---|
| Elbow Method / SSE | Compactness of clusters for different k values | A clear bend where improvement slows down |
| Silhouette Score | Separation and cohesion of clusters | Closer to +1 is better |
| Davies–Bouldin Index | Similarity between clusters | Lower is better |

---

## 4. Choosing k and Interpreting Segments

Choosing the number of clusters for K-Means requires both metrics and business understanding. The Elbow Method helps show where SSE improvement begins to slow down. Silhouette Score can help compare which k gives better-separated clusters. Davies–Bouldin Index can also help because a lower value means better separation.

However, the final choice of k should not be based only on numbers. It should also make sense for the business problem. For a wholesale distributor, two clusters might simply separate low spenders from high spenders. This can be useful, but it may be too general. Three to five clusters can sometimes provide more useful business segments, such as fresh-product buyers, grocery and detergents buyers, frozen-product buyers, and low-spending customers.

In the wholesale distributor project, a cluster with high Fresh and Milk spending may represent hotels, restaurants, cafés, or food-service clients that need fresh and dairy products regularly. A cluster with high Grocery and Detergents_Paper spending may represent retail shops or supermarkets, because those categories are more common in retail purchasing. A cluster with low spending across most categories may represent smaller clients or less active customers.

Channel and Region are excluded from the clustering features because the goal is to group customers by spending behavior, not by location or business type. Channel and Region are still useful for interpretation after clustering. For example, after creating clusters, we can check whether a certain cluster contains more retail customers or more Horeca customers. But if we include Channel and Region in training, the model may group customers based on labels or location instead of actual purchase behavior.

---

## 5. Real-World Case Study: Retail Customer Segmentation

A relevant real-world study is **“An Exploration of Clustering Algorithms for Customer Segmentation in the UK Retail Market.”** The goal of this study was to improve customer segmentation in the retail market by understanding customer purchasing behavior and supporting better decision-making.

The study used a UK-based online retail dataset from the UCI Machine Learning Repository. The dataset contained 541,909 customer records and eight features. The researchers used the RFM framework, which stands for Recency, Frequency, and Monetary value. This framework helps measure how recently a customer purchased, how often they purchase, and how much money they spend.

The study compared several clustering algorithms, including K-Means, Gaussian Mixture Model, DBSCAN, Agglomerative Clustering, and BIRCH. The key result was that the Gaussian Mixture Model performed best in their experiment, achieving a Silhouette Score of 0.80 [6].

This case study is related to the wholesale customer project because both use clustering to understand customers based on behavior. In both cases, the business value is not just the cluster number. The real value comes from interpreting the segments and using them for actions such as targeted marketing, personalized offers, customer retention, and better product planning.

---

## Conclusion

Clustering is useful when we want to discover groups in data without a known target label. In this assignment, the wholesale customer dataset is a good example because the business wants to understand different types of buyers based on spending behavior. K-Means is simple and interpretable, especially when cluster centers are converted back into original spending units. Hierarchical clustering gives another way to group customers by similarity, while DBSCAN is useful for density-based clusters and outlier detection.

The most important lesson is that clustering is not only a technical task. After the algorithm creates groups, the data scientist must interpret those groups in a business context. For the wholesale distributor, this means turning clusters into meaningful customer segments and suggesting actions that can help the business serve each group better.

---

## References

[1] scikit-learn. “2.3.2. K-means.” https://scikit-learn.org/stable/modules/clustering.html#k-means  

[2] scikit-learn. “2.3.6. Hierarchical clustering.” https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering  

[3] scikit-learn. “2.3.7. DBSCAN.” https://scikit-learn.org/stable/modules/clustering.html#dbscan  

[4] scikit-learn. “2.3.11.5. Silhouette Coefficient.” https://scikit-learn.org/stable/modules/clustering.html#silhouette-coefficient  

[5] scikit-learn. “2.3.11.7. Davies-Bouldin Index.” https://scikit-learn.org/stable/modules/clustering.html#davies-bouldin-index  

[6] John, J. M., Shobayo, O., & Ogunleye, B. “An Exploration of Clustering Algorithms for Customer Segmentation in the UK Retail Market.” arXiv, 2024. https://arxiv.org/abs/2402.04103  

[7] Cardoso, M. “Wholesale customers.” UCI Machine Learning Repository. https://archive.ics.uci.edu/dataset/292/wholesale+customers
