# Assignment Six — Part C: Reflection Paper

**Author:** Ali Omar Abdi
**Course:** DS-ML Bootcamp
**Topic:** Wholesale Customer Segmentation

---

## Table of Contents

1. [What Did I Implement?](#1-what-did-i-implement)
2. [Segment Interpretation](#2-segment-interpretation)
3. [Understanding K-Means](#3-understanding-k-means)
4. [My Second Algorithm](#4-my-second-algorithm)
5. [My Findings](#5-my-findings)

---

## 1. What Did I Implement?

I segmented 440 wholesale distributor clients using their annual spending across six product categories: Fresh, Milk, Grocery, Frozen, Detergents_Paper, and Delicassen. `Channel` and `Region` were kept in the dataset for reference but excluded from the clustering features themselves, since they are categorical labels rather than continuous spending measures, and `Channel` in particular is close to being the pattern I was trying to discover in the first place.

The pipeline capped outliers in each spending column with IQR clipping (`k=1.5`), scaled all six columns with `StandardScaler`, then used the Elbow Method to check how SSE changed from k=1 to k=10 before fitting `KMeans(n_clusters=5, n_init="auto", random_state=42)` as specified. I evaluated the result with Silhouette Score and Davies–Bouldin Index, and printed the cluster centers back in original spend units using `inverse_transform`. As my second algorithm, I researched and implemented **Agglomerative (Hierarchical) Clustering** with Ward linkage on the same scaled features, then compared both methods on a three-client sanity check.

## 2. Segment Interpretation

The K-Means run produced five clusters of very different sizes (76, 191, 25, 88, and 60 clients). Three of them stood out clearly in plain-language terms:

**Cluster 3 (88 clients) — Fresh/Frozen-heavy buyers.** Average Fresh spend was about 22,347, roughly double the overall average, and Frozen spend was about 5,820, over twice the average — while Detergents_Paper spend was far below average at 583. This looks like classic food-service (Horeca) behavior: restaurants and cafés buying perishable ingredients rather than packaged retail goods.
*Business action:* Offer this group fast, frequent delivery contracts for fresh and frozen goods, since their business depends on ingredient freshness and short lead times matter more to them than bulk packaged pricing.

**Cluster 4 (60 clients) — Grocery/Detergents-heavy buyers.** Average Detergents_Paper spend was about 7,780 — more than three times the overall average — with Grocery at 18,350 and Milk at 10,769, both well above average, while Fresh spend was the lowest of any cluster. This matches retail-style buyers stocking packaged goods and household supplies for resale to consumers.
*Business action:* Offer volume-based pricing tiers and bulk-order discounts on packaged goods, since this group's value comes from consistent large-case orders rather than frequent small deliveries.

**Cluster 2 (25 clients, the smallest group) — High spenders across every category.** Every single spending column was well above the overall average here — Fresh at 17,462, Grocery at 17,524, Milk at 13,806 — with no clear specialization in one category. These are the distributor's highest-volume accounts overall.
*Business action:* Assign dedicated account managers and prioritize service levels for this group. Even though it is the smallest cluster by client count, it likely represents a disproportionate share of total revenue, so retention matters more here than for any other segment.

## 3. Understanding K-Means

K-Means is a centroid-based clustering algorithm. It starts by choosing a number of clusters, *k*, and placing that many centroids in the feature space. Then it repeats a two-step loop: first, every data point is assigned to whichever centroid is closest to it; second, each centroid is recalculated as the average (mean) position of all the points currently assigned to it. These two steps — assign, then update — repeat until the centroids stop moving meaningfully, at which point the algorithm has converged and the final cluster assignments are locked in.

In this project, *k* was fixed at 5 as specified by the assignment. Each of the five resulting centroids, once converted back to original spend units with `inverse_transform`, represents the "typical" spending profile of a client in that cluster — which is exactly what let me describe Cluster 3 as fresh/frozen-heavy and Cluster 4 as grocery/detergents-heavy above.

## 4. My Second Algorithm

I chose **Agglomerative (Hierarchical) Clustering** with Ward linkage. I picked it because, unlike K-Means, it does not force clusters to be spherical or rely on random centroid initialization — it builds clusters bottom-up by repeatedly merging the two closest points or clusters, which can reveal nested sub-groups that a flat K-Means partition might miss. I used the scikit-learn documentation for `sklearn.cluster.AgglomerativeClustering` as my research source.

**What I learned:** Ward linkage specifically minimizes the increase in within-cluster variance at every merge step, which makes it a natural point of comparison against K-Means, since K-Means is also fundamentally a variance-minimizing algorithm — just approached top-down instead of bottom-up.

- **Advantage:** It does not require deciding the number of clusters before running the algorithm — the dendrogram it builds can be cut at any level afterward, which is useful for exploring the data at different levels of granularity.
- **Limitation:** It is far more computationally expensive than K-Means on large datasets, since it generally needs pairwise distances between all points, and once two points are merged the decision cannot be undone later in the process.

**Silhouette Score comparison:** Agglomerative Clustering scored 0.2185, versus 0.2831 for K-Means, on the same five clusters and same scaled features — meaning K-Means produced the better-separated clusters on this dataset.

## 5. My Findings

For this wholesale segmentation task, I would recommend **K-Means** as the primary method. It scored higher on Silhouette (0.2831 vs. 0.2185), meaning its clusters were more internally consistent and better separated from each other, and its cluster centers translate directly into an interpretable "typical client" profile per segment — something the distributor's sales team can act on immediately, such as targeting Cluster 3 clients with fresh/frozen delivery offers or Cluster 4 clients with bulk packaged-goods pricing.

That said, neither Silhouette Score was especially high in absolute terms (both were closer to 0.2–0.3 than to the 0.7+ range that would indicate very clean separation), which tells me the six spending categories overlap somewhat between client types rather than forming five perfectly distinct "islands." I would keep Agglomerative Clustering's dendrogram as a secondary diagnostic tool — it is well suited to checking whether any of the five K-Means clusters actually contain meaningful sub-groups worth splitting further, even though K-Means itself is the better choice for producing the final, actionable client segments.

---

*Submitted for DS-ML Bootcamp — Assignment Six, Part C*