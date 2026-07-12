# Assignment Six — Part A: Clustering Theory

**Author:** Ali Omar Abdi
**Course:** DS-ML Bootcamp
**Due:** Thursday, July 9, 2026 — 12:00 PM (Africa/Mogadishu / EAT)

---

## Table of Contents

1. [Introduction to Unsupervised Learning and Clustering](#1-introduction-to-unsupervised-learning-and-clustering)
2. [Clustering Algorithms](#2-clustering-algorithms)
3. [Clustering Metrics](#3-clustering-metrics)
4. [Choosing k and Interpreting Segments](#4-choosing-k-and-interpreting-segments)
5. [Real-World Case Study](#5-real-world-case-study)
6. [References](#references)

---

## 1. Introduction to Unsupervised Learning and Clustering

### What Is Unsupervised Learning?

Unsupervised learning is a branch of machine learning where the model is given data with no known answer attached. There is no target column to predict — instead, the algorithm is asked to find structure, patterns, or groupings in the data on its own. This contrasts with supervised learning (regression and classification), where every training example comes with a labeled answer the model learns to reproduce.

**Clustering** is the most common unsupervised technique. It groups rows of data into clusters so that items within the same cluster are more similar to each other than to items in other clusters, based purely on the patterns found in the features themselves.

### How Is It Different from Regression and Classification?

Regression and classification are both supervised tasks: the model is trained on labeled examples (a known price, a known approval decision) and learns a function that maps inputs to that known output. Clustering has no such target. The algorithm is not told what the "correct" grouping is; it discovers groupings based on similarity in the feature space. Because there is no ground-truth label to compare against, clustering is also evaluated differently — with metrics that describe how compact and well-separated the discovered groups are, rather than metrics that compare predictions to known answers.

| | Regression / Classification | Clustering |
|---|---|---|
| Labels | Yes — a known target column | No — groups are discovered |
| Goal | Predict a known answer | Find hidden structure |
| Metrics | MAE, R², Accuracy, F1 | Elbow (SSE), Silhouette, Davies–Bouldin |
| Example | Predict loan approval | Group clients by spending pattern |

### Real-Life Examples

**Clustering:** A wholesale food distributor grouping its business clients by their annual spending across product categories (fresh produce, groceries, frozen goods, and so on), without knowing in advance what "types" of buyers exist. The algorithm can reveal, for example, that some clients spend heavily on fresh and frozen goods (restaurant-style buyers) while others spend heavily on packaged groceries and cleaning supplies (retail-style buyers).

**Supervised learning:** A bank predicting whether a loan applicant will be approved or rejected, based on historical applications where the true outcome (Approved/Rejected) is already known for every past applicant. The model learns from these labeled examples and then predicts the outcome for new applicants.

---

## 2. Clustering Algorithms

### K-Means

**How it works:** K-Means partitions the data into a fixed number of clusters, *k*, chosen in advance. It starts by placing *k* centroids (cluster centers) in the feature space, then repeats two steps until the centroids stop moving significantly: (1) assign every data point to its nearest centroid, and (2) move each centroid to the mean position of the points assigned to it. The result is *k* clusters, each represented by the average of its members.

**Real-world use case:** Segmenting retail or wholesale customers by spending behavior, so a business can design different marketing or account strategies for different buyer types.

**Advantages:** Fast and computationally efficient even on large datasets; simple to understand and implement; works well when clusters are roughly round (spherical) and similarly sized.

**Limitations:** The number of clusters *k* must be chosen in advance; it assumes clusters are spherical and of similar density, which real data does not always satisfy; it is sensitive to outliers and to the initial placement of centroids, and it requires numeric features on a comparable scale.

### Hierarchical Clustering

**How it works:** Hierarchical (agglomerative) clustering builds clusters from the bottom up. Every data point starts as its own cluster, and the algorithm repeatedly merges the two closest clusters until only one cluster remains, recording each merge. This produces a tree-like structure called a dendrogram, which can be "cut" at any height to produce a chosen number of clusters after the fact — the number of clusters does not need to be decided before running the algorithm.

**Real-world use case:** Exploring nested customer sub-groups, for example within a broad "restaurant client" segment, discovering that it further splits into small cafés versus large hotel kitchens.

**Advantages:** Does not require choosing the number of clusters in advance; the dendrogram gives an interpretable view of how clusters relate to one another at different levels of granularity; works with various distance and linkage definitions, not just Euclidean distance.

**Limitations:** Computationally expensive on large datasets, since it generally requires computing distances between all pairs of points; once two points are merged into a cluster, that decision cannot be undone later in the process; results can be sensitive to the choice of linkage method (e.g., single, complete, average, or Ward).

### DBSCAN

**How it works:** DBSCAN (Density-Based Spatial Clustering of Applications with Noise) groups together points that are closely packed in the feature space, marking points in low-density regions as noise/outliers rather than forcing them into a cluster. It defines clusters using two parameters: `eps`, the neighborhood radius, and `min_samples`, the minimum number of points required to form a dense region. Clusters grow outward from dense "core" points as long as neighboring points also meet the density requirement.

**Real-world use case:** Detecting naturally occurring groups of unusual shape, such as geographic clusters of events on a map, while automatically flagging isolated points as outliers rather than forcing them into a nearby cluster.

**Advantages:** Does not require specifying the number of clusters in advance; can find clusters of arbitrary shape, not just round ones; naturally identifies outliers/noise instead of misclassifying them into a cluster.

**Limitations:** Sensitive to the choice of `eps` and `min_samples`, which can be difficult to tune; struggles when clusters have very different densities, since a single `eps` value may not suit all of them; less effective in high-dimensional feature spaces, where distance measures become less meaningful.

### Comparison Table

| | K-Means | Hierarchical Clustering | DBSCAN |
|---|---|---|---|
| Needs *k* in advance | Yes | No (choose after building the tree) | No |
| Cluster shape assumption | Spherical | Flexible, depends on linkage | Arbitrary (density-based) |
| Handles outliers | Poorly (outliers pull centroids) | Poorly | Well (flags them as noise) |
| Scalability | Good on large datasets | Poor on large datasets | Moderate |
| Best use case | Well-separated, roughly round groups | Exploring nested/hierarchical structure | Irregularly shaped clusters with noise |

---

## 3. Clustering Metrics

Since clustering has no ground-truth labels to check predictions against, it is evaluated with metrics that describe how well-formed the discovered clusters are.

### Elbow Method (SSE)

The Elbow Method helps choose a good value of *k* for K-Means. It runs K-Means for a range of *k* values and records the Sum of Squared Errors (SSE, also called inertia) — the total squared distance from each point to its assigned centroid. SSE always decreases as *k* increases, since more clusters mean points sit closer to their nearest centroid. The method looks for the point where the rate of decrease slows sharply, forming a bend or "elbow" in the SSE-vs-*k* curve; beyond this point, adding more clusters yields diminishing returns.

### Silhouette Score

The Silhouette Score measures, for each point, how similar it is to its own cluster compared to the next-nearest cluster, then averages this across all points. It ranges from -1 to +1: values near +1 mean points are well-matched to their own cluster and far from neighboring clusters; values near 0 mean clusters overlap; negative values suggest points may have been assigned to the wrong cluster. It is useful as a single overall number describing cluster quality, and can also help compare different values of *k* or different algorithms against each other.

### Davies–Bouldin Index

The Davies–Bouldin Index measures the average similarity between each cluster and its most similar neighboring cluster, where "similarity" combines how spread out each cluster is with how far apart their centers are. Unlike the Silhouette Score, lower values are better here — a low score means clusters are compact and well-separated from their nearest neighbors, while a high score means clusters overlap or are poorly distinguished from each other.

### Comparison Table

| Metric | What It Measures | Good Value Looks Like |
|---|---|---|
| Elbow Method (SSE) | Compactness of clusters as k changes | A clear bend/elbow in the SSE-vs-k curve |
| Silhouette Score | Cohesion within clusters vs. separation between clusters | Closer to +1 |
| Davies–Bouldin Index | Average similarity between each cluster and its closest neighbor | Lower value |

---

## 4. Choosing k and Interpreting Segments

### How Do You Choose the Number of Clusters for K-Means?

The number of clusters is chosen by combining a couple of methods rather than relying on one number alone. The Elbow Method gives a candidate range by showing where SSE stops improving quickly. The Silhouette Score and Davies–Bouldin Index can then be checked across that candidate range to confirm which value of *k* produces clusters that are both compact and well-separated. Beyond the statistics, the choice should also be validated against business interpretability: a value of *k* is only useful in practice if the resulting clusters correspond to groups that make sense and can be acted on — a statistically "optimal" k that produces clusters no one can describe or use is not actually a good choice.

### Interpreting High Fresh + Milk vs. High Grocery + Detergents_Paper Spend

In the wholesale distributor project, these two spending patterns correspond to two different types of business client. A cluster with high spending on **Fresh** and **Milk** (and often Frozen) typically represents food-service buyers — restaurants, cafés, and hotels (the "Horeca" channel) — who need perishable ingredients to prepare meals on-site. A cluster with high spending on **Grocery** and **Detergents_Paper** typically represents retail-style buyers — shops that stock packaged goods and household supplies for resale directly to consumers. Recognizing this split lets the distributor tailor delivery schedules, credit terms, and product bundles differently for each type of client.

### Why Exclude Channel and Region from the Clustering Features?

`Channel` and `Region` are excluded from the features used to fit K-Means for two reasons. First, they are categorical labels rather than continuous spending measures, so including them directly alongside six numeric spend columns would distort Euclidean distance calculations, which assume comparable, continuous scales. Second, and more importantly, `Channel` in particular is close to being the answer we are hoping to discover — spending on Fresh/Frozen versus Grocery/Detergents_Paper is largely what distinguishes Horeca from Retail clients in the first place. Including `Channel` as a clustering feature would let the algorithm "cheat" by grouping on the label rather than genuinely discovering the pattern from spending behavior. Keeping `Channel` and `Region` out of the clustering step, but available afterward, lets us use them to validate and interpret the clusters the algorithm finds independently.

---

## 5. Real-World Case Study

**Source:** Nivedhitha, M., Naveen, G., and Monis, S. A. (2025). Customer Segmentation in Retail Using K-Means Clustering: A Case Study on Shopping Trends. *International Journal of Research Publication and Reviews*, 6(9), 1237-1247.

**Goal:** The study set out to move a retailer away from generic, one-size-fits-all marketing by using K-Means clustering to uncover distinct customer segments from a shopping-trends dataset, so that marketing, retention, and inventory decisions could be tailored to each group instead of applied uniformly to everyone.

**Data used:** The dataset combined demographic attributes (age, gender, annual income, region) with transactional behavior (purchase frequency, average transaction value, total spending, preferred payment method, and product category preferences). Before clustering, the authors imputed missing values, capped outliers using the IQR method, one-hot encoded categorical variables, and applied Min-Max normalization so that no single feature would dominate the distance calculations.

**Clustering method applied:** K-Means was selected for its simplicity and efficiency. The optimal number of clusters was chosen by combining the Elbow Method, which tracks how the within-cluster sum of squares changes as *k* increases, with the Silhouette Score, which confirmed that the chosen *k* produced compact, well-separated groups rather than just a statistically convenient one.

**Key results:** The analysis produced four distinct segments: high-value frequent shoppers who spend heavily and consistently across categories; budget-conscious occasional buyers who mainly respond to discounts and seasonal sales; trend-driven younger shoppers heavily influenced by social media and product launches; and infrequent, low-engagement buyers with narrow, specific purchase needs. Each segment was paired with a distinct business strategy — VIP loyalty treatment for the high-value group, discount-driven reactivation campaigns for budget-conscious and low-engagement buyers, and influencer-style marketing for trend-driven shoppers.

**Why this is relevant:** This case study mirrors the wholesale distributor project directly. Both use K-Means with IQR capping and feature scaling as preprocessing, both rely on the Elbow Method and Silhouette Score to justify the number of clusters rather than picking one arbitrarily, and both translate the resulting clusters into concrete business actions rather than treating clustering as a purely statistical exercise. It reinforces a central lesson of unsupervised learning in practice: the algorithm can find groups automatically, but the value only appears once those groups are interpreted in terms a business can act on.

---

## References

MacQueen, J. (1967). Some methods for classification and analysis of multivariate observations. *Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability*, 281-297.

Nivedhitha, M., Naveen, G., and Monis, S. A. (2025). Customer Segmentation in Retail Using K-Means Clustering: A Case Study on Shopping Trends. *International Journal of Research Publication and Reviews*, 6(9), 1237-1247.

Ester, M., Kriegel, H.-P., Sander, J., and Xu, X. (1996). A density-based algorithm for discovering clusters in large spatial databases with noise. *Proceedings of the Second International Conference on Knowledge Discovery and Data Mining*, 226-231.

Rousseeuw, P. J. (1987). Silhouettes: A graphical aid to the interpretation and validation of cluster analysis. *Journal of Computational and Applied Mathematics*, 20, 53-65. https://doi.org/10.1016/0377-0427(87)90125-7

Davies, D. L., and Bouldin, D. W. (1979). A cluster separation measure. *IEEE Transactions on Pattern Analysis and Machine Intelligence*, PAMI-1(2), 224-227. https://doi.org/10.1109/TPAMI.1979.4766909

Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.

---

*Submitted for DS-ML Bootcamp — Assignment Six, Part A*