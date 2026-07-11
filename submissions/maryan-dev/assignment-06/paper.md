### 1.1 What Is Unsupervised Learning?

Unsupervised learning is a branch of machine learning in which a model is trained on data that has no predefined labels or target outcomes. Instead of learning a mapping from inputs to known outputs, the algorithm is left to discover structure, patterns, or relationships that exist naturally within the data (Bishop, 2006). Clustering, dimensionality reduction, and association-rule mining are all examples of unsupervised techniques. The central goal is descriptive rather than predictive: the algorithm groups, compresses, or reorganizes the data so that a human analyst can better understand it.

### 1.2 How Does It Differ from Regression and Classification?

Regression and classification are both supervised learning tasks: the model is trained using historical examples in which the correct answer (a continuous value for regression, or a discrete category for classification) is already known. The algorithm's objective is to minimize the difference between its predictions and these known ground-truth labels. In contrast, unsupervised learning receives no ground truth at all. There is no "correct" cluster label to compare against, so the algorithm cannot be evaluated by prediction accuracy; instead, it is judged by how coherent, separated, or useful the discovered groupings turn out to be. In short, supervised learning answers the question "given this input, what is the known output?", while clustering, an unsupervised method, answers "which of these unlabelled points naturally belong together?"

### 1.3 Real-Life Examples

**Clustering example:** A retail chain analyses its transaction data to group customers by purchasing behaviour (e.g., frequency, basket size, product categories) without knowing in advance how many types of shoppers exist. Clustering algorithms reveal segments such as "bulk buyers," "occasional high spenders," or "discount seekers," which marketing teams can then target with different campaigns.

**Supervised learning example:** A bank builds a credit-scoring model using historical loan records where each past applicant is already labelled as either "defaulted" or "repaid." A classification algorithm learns from these labelled examples to predict whether a new applicant is likely to default.

---

## 2. Clustering Algorithms

### 2.1 K-Means

**Basic idea:** K-Means partitions data into a pre-specified number of clusters, *k*, by iteratively assigning each point to the nearest centroid and then recalculating each centroid as the mean of the points assigned to it. This assign-and-update cycle repeats until the centroids stabilise (MacQueen, 1967).

**Real-world use case:** Segmenting customers of an online store into groups such as high-value, average, and low-value buyers based on spending and visit frequency, so that marketing budgets can be allocated more efficiently.

**Advantages:** Computationally efficient and easy to scale to large datasets; simple to interpret since each cluster is summarised by its centroid.

**Limitations:** Requires *k* to be chosen in advance; assumes roughly spherical, similarly sized clusters; sensitive to outliers and to the initial placement of centroids.

### 2.2 Hierarchical Clustering

**Basic idea:** Hierarchical clustering builds a tree-like structure (a dendrogram) of nested clusters. In the common agglomerative form, each point starts as its own cluster, and the two closest clusters are repeatedly merged until only one cluster remains; the dendrogram can then be cut at any level to obtain a chosen number of clusters (Everitt et al., 2011).

**Real-world use case:** Grouping species in biology based on genetic similarity, or organising documents into topic hierarchies in text mining, where a natural nested structure is expected.

**Advantages:** Does not require the number of clusters to be fixed beforehand; the dendrogram provides an intuitive visual of how clusters relate to one another at different levels of granularity.

**Limitations:** Computationally expensive for large datasets (typically O(n²) or worse); once a merge is made it cannot be undone, so early mistakes propagate through the tree.

### 2.3 DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

**Basic idea:** DBSCAN groups together points that are closely packed in space (high density) and marks points that lie alone in low-density regions as noise/outliers. It uses two parameters, a neighbourhood radius (eps) and a minimum number of points (minPts), to decide whether a region is dense enough to form a cluster (Ester et al., 1996).

**Real-world use case:** Identifying fraudulent transaction patterns or anomalous sensor readings, where the number of natural groupings is unknown and outliers must be explicitly flagged rather than forced into a cluster.

**Advantages:** Does not require the number of clusters to be specified; can find arbitrarily shaped clusters; naturally identifies outliers as noise.

**Limitations:** Struggles with clusters of varying density; performance is sensitive to the choice of eps and minPts; less effective in very high-dimensional feature spaces.

---

## 3. Clustering Metrics

Because unsupervised learning has no ground-truth labels, clustering quality must be assessed using internal metrics that examine the geometry of the clusters themselves rather than comparing predictions to known answers.

### 3.1 Elbow Method (SSE)

The Elbow Method examines the Sum of Squared Errors (SSE), also called inertia, which is the total squared distance between each data point and the centroid of the cluster it belongs to. As *k* increases, SSE always decreases, but the rate of decrease slows down after the "true" number of clusters is passed. Plotting SSE against different values of *k* produces a curve that bends like an elbow; the *k* at that bend is taken as a reasonable choice.

### 3.2 Silhouette Score

The Silhouette Score measures, for each point, how much closer it is to points in its own cluster than to points in the nearest other cluster. It combines a cohesion term (average distance to points in the same cluster) and a separation term (average distance to points in the nearest neighbouring cluster) into a single score between -1 and 1 (Rousseeuw, 1987).

### 3.3 Davies–Bouldin Index

The Davies–Bouldin Index measures the average "similarity" between each cluster and the cluster most like it, where similarity increases when clusters are large (spread out) and their centroids are close together. Unlike the Silhouette Score, lower values are better, with zero representing perfectly separated, compact clusters (Davies & Bouldin, 1979).

### 3.4 Comparison Table

| Metric | What It Measures | How It Is Used | Sign of a Good Value |
|---|---|---|---|
| **Elbow Method (SSE)** | Sum of squared distances between each point and its cluster centroid (within-cluster variance) | SSE is plotted against *k*; the point where the decrease sharply slows (the "elbow") suggests a suitable *k* | A clear bend in the curve after which SSE flattens out; no single numeric threshold |
| **Silhouette Score** | How similar a point is to its own cluster compared to the nearest neighbouring cluster | Computed per point and averaged across the dataset for a given *k* | Ranges from -1 to 1; values closer to 1 indicate dense, well-separated clusters |
| **Davies–Bouldin Index** | Average similarity between each cluster and its most similar cluster, based on cluster size and inter-cluster distance | Computed for each candidate *k* and compared across values | Lower values indicate better clustering; 0 is the theoretical minimum |

---

## 4. Choosing k and Interpreting Segments

### 4.1 Choosing the Number of Clusters for K-Means

In practice, *k* is chosen by combining several of the metrics above rather than relying on just one. Analysts typically run K-Means for a range of *k* values (e.g., 2 to 10), record the SSE, Silhouette Score, and Davies–Bouldin Index for each, and look for a *k* where the elbow curve flattens, the Silhouette Score is high (and stable), and the Davies–Bouldin Index is low. Beyond these statistical checks, the final choice should also make business sense: a *k* that produces clusters too small or too similar to act on is rarely useful, even if it scores well numerically.

### 4.2 Interpreting Spend-Based Segments in the Wholesale Distributor Project

When a cluster shows high spending on Fresh and Milk but low spending on Grocery and Detergents_Paper, it typically represents clients such as restaurants, cafés, or hotels (the HoReCa channel) that need perishable goods delivered frequently and in smaller batches for immediate consumption. Conversely, a cluster with high Grocery and Detergents_Paper spend alongside lower Fresh and Milk spend typically represents retail clients, such as supermarkets or small grocery shops, that stock longer shelf-life, packaged goods in bulk for resale. Recognising this distinction lets the distributor tailor delivery schedules, credit terms, and promotions differently for each segment.

### 4.3 Why Exclude Channel and Region from the Clustering Features

Channel and Region are categorical labels that describe how or where a customer already operates, rather than measurements of their purchasing behaviour. Including them would let the algorithm cluster customers by their existing category label instead of by the spending patterns we actually want to discover, which defeats the purpose of an unsupervised, behaviour-driven segmentation. Keeping them out of the feature set also avoids mixing categorical and continuous variables with very different scales, which can distort distance-based algorithms such as K-Means. Instead, Channel and Region are best kept aside and used afterward to validate or interpret the clusters that emerge, checking whether the spend-based segments align with, or cut across, the existing channel and regional groupings.

---

## 5. Real-World Case Study

A representative real-world application of clustering for customer segmentation is a 2025 study of a retail business named Icon Yasika, based in Makassar, Indonesia, which applied K-Means clustering to design a more targeted marketing strategy (ResearchGate, 2025).

**Goal:** The study aimed to segment the store's customers so that marketing budgets and promotions could be directed toward the right groups, rather than treating all customers the same way.

**Data used:** The researchers used transaction records covering roughly a year and a half of sales, from which they engineered features following the LRFM model: Length (how long a customer has been active), Recency (how recently they purchased), Frequency (how often they purchase), and Monetary value (how much they spend).

**Clustering method applied:** K-Means clustering was applied to the standardized LRFM scores. To determine the appropriate number of clusters, the researchers combined the Elbow Method with the Davies–Bouldin Index rather than relying on a single metric, which allowed them to cross-check that the chosen cluster count was both mathematically well-separated and consistent with the point of diminishing returns in SSE.

**Key results and insights:** The analysis produced five distinct customer segments, ranging from lost customers who had stopped purchasing, through occasional or new customers, to core, high-value customers who purchased frequently and recently. These segments were visualised on an interactive dashboard, giving managers a real-time view of how customers moved between groups. The insights were then used to design differentiated marketing actions, such as re-engagement offers for lapsed customers and loyalty incentives for core customers, illustrating how a purely data-driven, unsupervised technique can directly inform business strategy and improve the efficiency of promotional spending.

---

## References

Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.

Davies, D. L., & Bouldin, D. W. (1979). A Cluster Separation Measure. *IEEE Transactions on Pattern Analysis and Machine Intelligence, 1*(2), 224-227.

Ester, M., Kriegel, H.-P., Sander, J., & Xu, X. (1996). A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise. *Proceedings of the Second International Conference on Knowledge Discovery and Data Mining (KDD-96)*.

Everitt, B. S., Landau, S., Leese, M., & Stahl, D. (2011). *Cluster Analysis* (5th ed.). Wiley.

MacQueen, J. (1967). Some Methods for Classification and Analysis of Multivariate Observations. *Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability, 1*, 281-297.

ResearchGate. (2025). *Customer Segmentation Using the K-Means Algorithm for Marketing Strategy Design: Case Study at the Icon Yasika Makassar*. Retrieved from https://www.researchgate.net/publication/393783515

Rousseeuw, P. J. (1987). Silhouettes: A Graphical Aid to the Interpretation and Validation of Cluster Analysis. *Journal of Computational and Applied Mathematics, 20*, 53-65.