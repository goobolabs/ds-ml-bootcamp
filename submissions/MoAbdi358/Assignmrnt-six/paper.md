# Introduction to Unsupervised Learning and Clustering

**Assignment Six — Part A: Theory**
**Author:** Mohamed Abdi
**Course:** Data Science and Machine Learning Bootcamp, Gollis University

---

## 1. Introduction to Unsupervised Learning and Clustering

### 1.1 What is unsupervised learning?

Unsupervised learning is a branch of machine learning in which a model is given
data that has no predefined output labels. Instead of learning a mapping from
inputs to known answers, the algorithm searches the data itself for structure —
groupings, patterns, or reduced representations that were not specified in
advance. The model's job is to describe the data, not to predict a target
variable.

### 1.2 How does it differ from regression and classification?

Regression and classification are both **supervised learning** tasks: every
training example comes with a known, correct answer (a continuous number for
regression, a category for classification), and the algorithm's goal is to
learn a function that reproduces those answers on new data. Success can be
measured directly by comparing predictions to ground truth (e.g., accuracy,
RMSE).

Clustering, the main technique of unsupervised learning, has no ground truth to
compare against. There is no "correct" cluster label in the data; the algorithm
groups observations purely based on similarity in the feature space. Evaluation
is therefore indirect, relying on internal metrics such as the Silhouette Score
rather than a comparison to known answers.

### 1.3 Real-life examples

- **Clustering (unsupervised):** A supermarket chain groups its loyalty-card
  holders into segments — e.g., "bulk weekend shoppers," "convenience
  shoppers," "health-food shoppers" — based purely on purchasing patterns,
  with no pre-existing labels for these groups.
- **Supervised learning:** A bank predicts whether a loan applicant will
  default, using historical applications that are already labeled
  "defaulted" or "repaid."

---

## 2. Clustering Algorithms

### 2.1 K-Means

**How it works:** K-Means partitions the data into *k* clusters by iterating
between two steps: (1) assign each point to the nearest of *k* centroids, and
(2) recompute each centroid as the mean of the points now assigned to it. This
repeats until assignments stop changing (convergence).

**Real-world use case:** Segmenting retail customers by annual spending across
product categories, so a company can design different promotions for
high-value versus budget-conscious customers.

**Advantages:** Simple to implement, computationally efficient even on large
datasets, and produces easily interpretable centroids.

**Limitations:** Requires the number of clusters (*k*) to be chosen in
advance, assumes roughly spherical and similarly sized clusters, is sensitive
to outliers, and can converge to different results depending on the random
initialization of centroids.

### 2.2 Hierarchical Clustering

**How it works:** Agglomerative hierarchical clustering starts with every
point as its own cluster and repeatedly merges the two closest clusters
(according to a linkage rule such as Ward, average, or complete linkage) until
only one cluster remains. The result is a tree-like structure (a dendrogram)
that can be "cut" at any height to produce a chosen number of clusters.

**Real-world use case:** Grouping documents or gene-expression profiles where
the natural relationships between groups (which segments are more similar to
which) are as valuable as the final grouping itself.

**Advantages:** Does not require choosing *k* in advance, the dendrogram
reveals relationships between clusters at multiple levels of granularity, and
it does not depend on random initialization, so results are deterministic.

**Limitations:** Computationally expensive on large datasets (the distance
matrix grows quadratically with the number of points), and once two points are
merged into a cluster, that decision cannot be undone later in the process.

### 2.3 DBSCAN

**How it works:** DBSCAN (Density-Based Spatial Clustering of Applications
with Noise) groups together points that are closely packed (within a distance
`eps` of at least `min_samples` neighbors), and marks points that lie in
low-density regions as noise/outliers, rather than forcing them into a
cluster.

**Real-world use case:** Detecting anomalous transactions in fraud analysis,
where the goal is to find dense clusters of "normal" behavior and flag
sparse, isolated points as suspicious.

**Advantages:** Does not require specifying the number of clusters, can find
arbitrarily shaped clusters (not just spherical ones), and naturally handles
outliers/noise.

**Limitations:** Sensitive to the choice of `eps` and `min_samples`, and
struggles when clusters have very different densities.

---

## 3. Clustering Metrics

| Metric | What it Measures | Good Value Looks Like |
|---|---|---|
| **Elbow Method (SSE)** | The sum of squared distances between each point and its assigned cluster centroid (within-cluster variance), plotted against *k* | The "elbow" point where adding more clusters stops producing a large drop in SSE — a sharp bend, not the absolute minimum (which is always at k = n) |
| **Silhouette Score** | For each point, how close it is to its own cluster compared to the nearest other cluster, averaged across all points; ranges from −1 to 1 | Values closer to **+1** indicate well-separated, dense clusters; values near 0 indicate overlapping clusters; negative values suggest points may be in the wrong cluster |
| **Davies–Bouldin Index (DBI)** | The average similarity between each cluster and its most similar other cluster, based on the ratio of within-cluster scatter to between-cluster distance | **Lower is better** — a value closer to 0 means clusters are compact and well-separated from one another |

The Elbow Method is used to *choose* a reasonable value of *k* before fitting
the final model, while the Silhouette Score and Davies–Bouldin Index are used
*after* clustering to judge the quality of the resulting groups — and both can
also be compared across different values of *k* or across different
algorithms.

---

## 4. Choosing k and Interpreting Segments

### 4.1 How to choose the number of clusters for K-Means

The most common approach is the Elbow Method: run K-Means for a range of *k*
values, plot SSE against *k*, and look for the point where the curve bends
("elbow") — beyond that point, adding more clusters yields diminishing
reductions in SSE. This is often combined with the Silhouette Score, checking
which *k* produces the highest average silhouette value, and with domain
knowledge — e.g., a business may want a specific number of actionable
segments regardless of what is mathematically "optimal."

### 4.2 Interpreting Fresh + Milk vs Grocery + Detergents_Paper

In the wholesale distributor dataset, a cluster with **high Fresh + Milk
spend but low Grocery + Detergents_Paper spend** typically corresponds to
**Horeca-type customers** (hotels, restaurants, cafés) — businesses that buy
large volumes of fresh perishables to prepare meals, but buy comparatively
little in packaged grocery or cleaning/paper products.

A cluster with **high Grocery + Detergents_Paper spend** (and often high
Milk) typically corresponds to **retail-type customers** — small shops and
supermarkets that stock packaged, shelf-stable goods and household supplies
for resale, rather than fresh ingredients for immediate food preparation.

### 4.3 Why exclude Channel and Region

`Channel` and `Region` are categorical/nominal identifiers, not continuous
spending measures — including them directly in a distance-based algorithm
like K-Means would treat numerically-coded categories (e.g., Region 1, 2, 3)
as if they had a meaningful magnitude and order, which they do not. Excluding
them keeps the clustering focused purely on *purchasing behavior*, and allows
`Channel` and `Region` to instead be used afterward as an independent check —
comparing whether the spending-based clusters line up with the known business
channel, without letting that label influence the clustering itself.

---

## 5. Real-World Case Study

A widely cited academic study applies K-Means clustering combined with an
RFM (Recency, Frequency, Monetary) framework to segment customers of a real
online retail enterprise in China, using historical sales transaction data<cite index="18-1">to conduct customer segmentation and value analysis by using online sales data</cite>. The goal was to move beyond simple, one-size-fits-all marketing by
identifying distinct behavioral groups and building tailored customer
relationship management (CRM) strategies for each.

**Data used:** Historical online transaction records, from which recency,
frequency, and monetary features were engineered for each customer.

**Method applied:** K-Means clustering on the RFM feature set, producing<cite index="18-1">four customer groups based on their purchase behaviors</cite>, each associated with a different recommended retention or marketing
strategy.

**Key results:** By tailoring CRM strategies to each segment, the study
reported<cite index="18-1">measurable improvement through indicators such as growth of active customers, total purchase volume, and total consumption amount</cite>, demonstrating that clustering-driven segmentation translated into concrete
business value rather than just an academic exercise.

This mirrors the wholesale distributor task in this assignment: in both
cases, spending-pattern features (RFM values here, six product-category
spend columns for the wholesale case) are clustered so that a business can
treat different customer groups differently instead of applying one blanket
strategy to everyone.

---

## References

- Wu, J. et al. (2020). *An Empirical Study on Customer Segmentation by
  Purchase Behaviors Using a RFM Model and K-Means Algorithm.* Mathematical
  Problems in Engineering, Hindawi.
- scikit-learn developers. *Clustering — scikit-learn User Guide.*
  https://scikit-learn.org/stable/modules/clustering.html
- UCI Machine Learning Repository. *Wholesale customers Data Set.*
  https://archive.ics.uci.edu/dataset/292/wholesale+customers
