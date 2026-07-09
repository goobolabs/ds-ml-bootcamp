# Assignment Six — Clustering: Theory and Practice

---

## 1. Introduction to Unsupervised Learning and Clustering

Unsupervised learning is a type of machine learning where the model works with data that has no labels. There is no right answer to learn from — the model finds patterns and structure in the data on its own.

This is different from supervised learning (regression and classification) where every training example has a known output. In unsupervised learning there is no y — just X. The model figures out the groupings, relationships, or structure by itself.

**Clustering example:** A wholesale distributor has 440 clients but no labels for them. A clustering algorithm groups them by spending behavior — some clients spend heavily on fresh produce, others on grocery and cleaning products. No one labeled these groups in advance.

**Supervised learning example:** Predicting whether a loan application gets approved or rejected based on labeled historical data — where the outcome for each past application is already known.

---

## 2. Clustering Algorithms

### K-Means
K-Means groups data into k clusters by minimizing the distance between each point and its cluster center (centroid). You choose k before training.

**How it works:** It randomly places k centroids, assigns every data point to the nearest centroid, then moves each centroid to the mean of its assigned points. This assign-and-update loop repeats until the centroids stop moving.

**Use case:** Segmenting supermarket customers by purchase behavior to target promotions.

**Advantage:** Fast, simple, and scales well to large datasets.

**Limitation:** You have to choose k manually. Sensitive to outliers since the mean shifts when extreme values are present. Only works well with round, similarly-sized clusters.

---

### Hierarchical Clustering
Hierarchical Clustering builds a tree of clusters (called a dendrogram) by progressively merging or splitting groups. You do not need to choose k upfront.

**How it works (Agglomerative):** Starts with every data point as its own cluster. Then repeatedly merges the two closest clusters until everything is one big cluster. You cut the dendrogram at a chosen level to get your final clusters.

**Use case:** Grouping genes with similar expression patterns in biology research — where you do not know how many groups to expect.

**Advantage:** No need to specify k in advance. The dendrogram gives a visual overview of the cluster structure at every level.

**Limitation:** Slow on large datasets — O(n²) memory and time complexity. Merges are permanent, so a bad early merge cannot be undone.

---

### DBSCAN
DBSCAN (Density-Based Spatial Clustering of Applications with Noise) finds clusters based on density — areas where points are tightly packed together. It does not require k and can find clusters of any shape.

**How it works:** It defines a cluster as a region where a minimum number of points (`min_samples`) fall within a radius (`eps`). Points that do not belong to any dense region are labeled as noise and ignored.

**Use case:** Detecting fraud in financial transactions — fraudulent activity often forms small dense clusters in an otherwise sparse feature space.

**Advantage:** Finds clusters of any shape. Automatically handles noise and outliers by labeling them separately.

**Limitation:** Sensitive to the `eps` and `min_samples` parameters — choosing them wrong leads to poor results. Struggles when clusters have different densities.

---

## 3. Clustering Metrics

### Elbow Method (SSE)
SSE (Sum of Squared Errors) measures the total distance between each point and its cluster center. You plot SSE for k = 1 to 10 and look for the "elbow" — the point where adding more clusters stops reducing SSE significantly.

### Silhouette Score
Measures how similar a point is to its own cluster compared to other clusters. Ranges from -1 to +1. A score close to +1 means the point is well inside its cluster and far from others. A score near 0 means it is on a border. Negative means it may be in the wrong cluster.

### Davies–Bouldin Index
Measures the average similarity between each cluster and its most similar neighbor. Lower is better. A score of 0 means perfect separation between clusters.

---

### Comparison Table

| Metric | What It Measures | Good Value | Needs k? |
|---|---|---|---|
| Elbow (SSE) | Total within-cluster distance | Sharp drop then flattening | Yes |
| Silhouette Score | How well separated each point is | Close to +1 | No |
| Davies–Bouldin Index | Average cluster similarity | Close to 0 | No |

---

## 4. Choosing k and Interpreting Segments

The most common way to choose k is the Elbow Method — you run K-Means for several values of k, plot SSE, and pick the k where the curve bends. The Silhouette Score can help confirm the choice: if k=5 has a higher silhouette score than k=4 or k=6, that supports the decision.

In the wholesale distributor project, a cluster with high Fresh and Milk spend most likely represents restaurants or food service businesses — they need large quantities of perishables regularly. A cluster with high Grocery and Detergents_Paper spend looks more like retail shops or supermarkets — they stock household goods and packaged products.

Channel and Region are excluded from clustering because they are identifiers, not spending behavior. Including them would let the algorithm separate clients by where they are or what channel they use — not by what they actually buy. The goal is to find spending segments, so only the six spend columns are used as features.

---

## 5. Real-World Case Study — Customer Segmentation in Retail

**Source:** Cluster Analysis for Market Segmentation — towards data science article by Rustam Nazarov (2021), referencing the UCI Wholesale Customers dataset and real retail segmentation practice.

**Goal:** Segment wholesale customers into distinct groups based on annual spending across product categories, so the distributor can offer each group tailored pricing and promotions.

**Data used:** The UCI Wholesale Customers dataset — 440 clients with annual spend across Fresh, Milk, Grocery, Frozen, Detergents_Paper, and Delicassen. Channel and Region were kept only for post-analysis interpretation, not as clustering features.

**Method:** K-Means with k selected via the Elbow Method. Features were standardized before clustering to prevent high-spend categories from dominating the distance calculation.

**Key results:** Three to five clusters consistently emerged across different runs. The clearest segments were high-Fresh spenders (food service), high-Grocery and Detergents_Paper spenders (retail shops), and low-spend clients across all categories (small or infrequent buyers). Knowing these segments allowed the distributor to design separate supply agreements and discount structures for each group rather than treating all 440 clients the same way.