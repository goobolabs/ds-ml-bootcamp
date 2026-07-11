# Assignment 6 — Theory Paper: Clustering in Machine Learning

**Student:** Abdullahi
**Course:** Data Science & Machine Learning
**Due:** Wednesday, 8 July 2026 — 5:00 PM EAT

---

## 1. Introduction to Unsupervised Learning and Clustering

### What is Unsupervised Learning?

Unsupervised learning is a branch of machine learning in which algorithms are trained on data that has **no labels or pre-defined output**. Unlike supervised learning, where each training example is paired with a known answer (such as a house price or a loan decision), unsupervised algorithms receive only the input features and must discover patterns, structures, or groupings entirely on their own. The model is not corrected during training because there is no ground-truth target to compare against. Instead, the objective is to find hidden structure within the data.

Unsupervised learning is particularly valuable in situations where labeling data is expensive, time-consuming, or simply impossible — for example, discovering natural categories in millions of customer transactions without manually tagging every record.

### How is it Different from Regression and Classification?

**Regression** (supervised) learns a mapping from inputs to a continuous numerical output. For example, predicting a house's sale price given its square footage, number of rooms, and location. The model is trained by minimising a loss (e.g., Mean Absolute Error) against known price labels.

**Classification** (supervised) learns a mapping from inputs to a discrete class label. For example, predicting whether a loan application will be approved (Yes/No). The model is evaluated against the true class labels using metrics such as Accuracy, Precision, Recall, and F1-Score.

**Clustering** (unsupervised) receives inputs only — no labels. The algorithm groups similar observations together based purely on the patterns it detects in the feature space. There is no training target to optimise against, and evaluation relies on internal metrics (e.g., Silhouette Score) that measure the quality of the discovered groupings without referencing true labels.

| Aspect | Regression / Classification | Clustering |
|---|---|---|
| Labels needed | Yes | No |
| Output | Predicted value / class | Group assignment |
| Evaluation | MAE, R², Accuracy, F1 | Silhouette, Davies–Bouldin, Elbow |
| Goal | Predict a known answer | Discover hidden structure |

### Real-Life Examples

**Clustering example:** A retail supermarket analyses purchase histories of its customers and groups them into segments such as "bulk buyers," "health-conscious shoppers," and "convenience shoppers" — without any pre-existing category labels — so it can tailor promotions to each group.

**Supervised learning example:** A bank trains a classifier on thousands of historical loan applications (each marked "approved" or "rejected") to automatically predict the outcome of new applications.

---

## 2. Clustering Algorithms

### 2.1 K-Means

**How it works:** K-Means partitions data into exactly *k* clusters by iteratively minimising the sum of squared distances from each data point to its nearest cluster centroid. The algorithm begins by placing *k* initial centroids (often at randomly chosen data points), assigns every observation to its closest centroid, then recomputes each centroid as the mean of all assigned points. This assign-and-update cycle repeats until the centroids no longer move (convergence). The result is a hard partition: every data point belongs to exactly one cluster.

**Real-world use case:** Segmenting e-commerce customers by purchase frequency, average basket size, and product category — enabling targeted email campaigns for each segment.

**Advantages:**
- Simple to understand and implement.
- Scales well to large datasets.
- Computationally efficient (O(n·k·i·d) per iteration).

**Limitations:**
- Requires specifying *k* in advance.
- Sensitive to outliers (a single extreme point can pull a centroid far from its cluster).
- Assumes spherical, similarly-sized clusters; performs poorly on elongated or irregular shapes.
- Results can vary between runs due to random centroid initialisation (mitigated by `n_init` restarts).

---

### 2.2 Hierarchical Clustering (Agglomerative)

**How it works:** Hierarchical clustering builds a tree of clusters called a **dendrogram**. In the agglomerative (bottom-up) variant, each observation starts as its own cluster. At each step, the two most similar clusters are merged until a single cluster containing all observations remains. The similarity between clusters is determined by a *linkage criterion* — common choices include Ward linkage (minimises variance within merged clusters), complete linkage (maximum pairwise distance), and average linkage. The analyst cuts the dendrogram at a chosen height to obtain the desired number of clusters.

**Real-world use case:** Gene expression analysis in bioinformatics, where researchers group genes with similar expression profiles across different tissue samples.

**Advantages:**
- Does not require specifying *k* beforehand; the dendrogram reveals natural groupings at multiple scales.
- Deterministic — produces the same result every run (no random initialisation).
- The full hierarchy provides richer information than a flat partition.

**Limitations:**
- Computationally expensive for large datasets: O(n² log n) time and O(n²) memory.
- Once two clusters are merged, the decision cannot be reversed (greedy).
- Sensitive to noise and outliers.

---

### 2.3 DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

**How it works:** DBSCAN groups points that are *densely packed* together and labels sparse regions as noise. It defines two hyperparameters: **ε (epsilon)** — the neighbourhood radius — and **MinPts** — the minimum number of points required within ε to form a *core point*. A cluster is grown by connecting all core points that are reachable from one another within ε. Points that are reachable from a core point but are not themselves core points become *border points*. All remaining points are labelled as **noise/outliers** and assigned no cluster.

**Real-world use case:** Detecting geographic hotspots of criminal incidents in a city — clusters of high incident density emerge naturally, while isolated incidents are flagged as anomalies.

**Advantages:**
- Does not require specifying the number of clusters in advance.
- Naturally identifies and isolates outliers as noise points.
- Finds clusters of arbitrary shape (not limited to spherical).

**Limitations:**
- Choosing ε and MinPts is non-trivial and dataset-dependent.
- Performs poorly when clusters have varying densities.
- High-dimensional data reduces the effectiveness of distance-based density estimation.

---

### Comparative Summary

| Algorithm | k Required? | Outlier Handling | Cluster Shape | Scalability |
|---|---|---|---|---|
| K-Means | Yes | Poor (absorbed) | Spherical | High |
| Agglomerative | No (k optional) | Poor (absorbed) | Any | Low–Medium |
| DBSCAN | No | Excellent (noise) | Any (arbitrary) | Medium |

---

## 3. Clustering Metrics

Unlike classification or regression, clustering has no ground-truth labels to compare predictions against. We therefore rely on **internal metrics** that evaluate the quality of a clustering based solely on the data and the cluster assignments.

### 3.1 Elbow Method (SSE — Sum of Squared Errors)

The Elbow Method is used specifically to choose a good value of *k* for K-Means. For each value of k from 1 to some maximum (e.g., 10), K-Means is trained and the **inertia** (sum of squared distances from each point to its assigned centroid) is recorded. As k increases, inertia always decreases because more centroids mean shorter distances. The analyst plots k vs. inertia and looks for an **"elbow"** — a point where the rate of decrease sharply diminishes. This elbow suggests that adding more clusters beyond this point yields diminishing returns in cluster compactness.

**What a good value looks like:** A clear, sharp bend in the SSE curve, after which the curve flattens significantly.

### 3.2 Silhouette Score

The Silhouette Score measures how well each data point has been placed in its assigned cluster. For each point *i*, it computes:

- **a(i):** the mean distance from point *i* to all other points in the same cluster (cohesion).
- **b(i):** the mean distance from point *i* to all points in the nearest *other* cluster (separation).

The silhouette value for point *i* is: **s(i) = (b(i) − a(i)) / max(a(i), b(i))**

The overall Silhouette Score is the average across all points. It ranges from **−1 to +1**:
- Near **+1**: well-separated, compact clusters.
- Near **0**: points are on or near the boundary between clusters.
- Near **−1**: points are likely assigned to the wrong cluster.

**What a good value looks like:** A score above **0.50** is generally considered good; above **0.70** is excellent.

### 3.3 Davies–Bouldin Index

The Davies–Bouldin Index (DBI) measures the **average similarity between each cluster and its most similar neighbouring cluster**. Similarity here is defined as the ratio of within-cluster scatter to between-cluster distance. A lower DBI indicates that clusters are more compact (small within-cluster scatter) and more separated from each other (large between-cluster distance).

**What a good value looks like:** **Lower is better.** A DBI near 0 indicates well-separated, tight clusters.

### Comparison Table

| Metric | What it Measures | Range | Good Value | Used For |
|---|---|---|---|---|
| Elbow (SSE) | Compactness of clusters vs. k | 0 → ∞ (lower better) | Clear bend in curve | Choosing k for K-Means |
| Silhouette Score | Separation + cohesion of assignments | −1 to +1 (higher better) | > 0.50 | Overall cluster quality |
| Davies–Bouldin | Between-cluster similarity | 0 → ∞ (lower better) | Closer to 0 | Comparing clustering solutions |

---

## 4. Choosing *k* and Interpreting Segments

### Choosing the Number of Clusters

For K-Means, the most practical approach is the **Elbow Method** combined with the **Silhouette Score**. First, run K-Means for k = 1 to 10 and plot the inertia curve. Identify the elbow — the value of k where inertia stops dropping sharply. Then, compute the Silhouette Score for the candidate k values near the elbow and choose the k that maximises it. This combined approach balances compactness (Elbow) with separability (Silhouette).

Domain knowledge can also guide the choice. In a wholesale distribution context, knowing that the client base typically falls into three or four broad purchasing profiles can validate the data-driven k selection.

### Interpreting Segments in the Wholesale Project

When a cluster exhibits **high Fresh + Milk spend** relative to other clusters, it suggests clients in this group buy large quantities of perishable products and dairy — a pattern consistent with **restaurants or hotel kitchens** that prepare fresh meals daily.

In contrast, a cluster with **high Grocery + Detergents_Paper spend** suggests clients focus on non-perishable packaged goods and cleaning supplies — a pattern more consistent with **retail shops or supermarkets** that stock shelves for end consumers and maintain hygiene standards.

### Why Channel and Region are Excluded from Clustering

`Channel` (Horeca vs. Retail) and `Region` (Lisbon, Oporto, Other) are **categorical identifiers**, not spending behaviours. Including them would bias the clustering toward geographic or channel-type groupings rather than actual purchasing patterns. Our goal is to discover **behavioural segments** defined by what clients buy, not where they are or what business type they are registered as. Excluding these columns ensures the clusters reflect genuine spending diversity across the six product categories.

---

## 5. Real-World Case Study: Customer Segmentation Using RFM and K-Means

### Overview

A well-documented real-world application of clustering for customer segmentation is the **RFM (Recency, Frequency, Monetary) analysis** conducted on the UCI Online Retail dataset, which contains approximately 500,000 transactions from a UK-based e-commerce company between 2010 and 2011 (Chen et al., 2012).

### Goal

The goal was to segment approximately 4,000 unique customers based on their purchasing behaviour in order to identify high-value clients, at-risk customers, and dormant buyers — enabling targeted retention and marketing strategies.

### Data Used

Three engineered features were derived from the raw transaction records:
- **Recency:** Days since the customer's last purchase.
- **Frequency:** Total number of orders placed.
- **Monetary Value:** Total amount spent (GBP).

### Clustering Method Applied

K-Means clustering (k = 4) was applied after standardising the three RFM features using `StandardScaler`. The optimal k was identified using the Elbow Method combined with Silhouette Score analysis. Log transformation was applied to reduce skewness before scaling.

### Key Results and Insights

The four clusters revealed distinct customer personas:
1. **Champions** (high Frequency, high Monetary, low Recency): loyal, high-spending recent buyers — the distributor's most valuable segment.
2. **At-Risk Customers** (medium Frequency, medium Monetary, high Recency): once loyal but not purchased recently — candidates for win-back campaigns.
3. **New Customers** (low Frequency, low Monetary, very low Recency): recently acquired but with limited history — candidates for onboarding promotions.
4. **Dormant** (low Frequency, low Monetary, very high Recency): inactive customers unlikely to return without a strong incentive.

The business deployed different email sequences to each segment, resulting in measurable improvements in reactivation rates for the at-risk group and higher average basket sizes for champions offered loyalty rewards.

**Source:** Daqing Chen, Sai Liang Sain, and Kun Guo, "Data mining for the online retail industry: A case study of RFM model-based customer segmentation using data mining," *Journal of Database Marketing and Customer Strategy Management*, 19(3), 197–208, 2012.

---

## References

- Chen, D., Sain, S. L., & Guo, K. (2012). Data mining for the online retail industry: A case study of RFM model-based customer segmentation using data mining. *Journal of Database Marketing & Customer Strategy Management*, 19(3), 197–208.
- Ester, M., Kriegel, H.-P., Sander, J., & Xu, X. (1996). A density-based algorithm for discovering clusters in large spatial databases with noise. *KDD-96 Proceedings*, 226–231.
- Kaufman, L., & Rousseeuw, P. J. (2009). *Finding Groups in Data: An Introduction to Cluster Analysis.* Wiley.
- Pedregosa, F., et al. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research*, 12, 2825–2830.
- UCI Machine Learning Repository: Wholesale Customers Data Set. https://archive.ics.uci.edu/ml/datasets/Wholesale+customers

---

*End of Part A Theory Paper*
