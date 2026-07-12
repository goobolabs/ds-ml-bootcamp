# Reflection Paper: Wholesale Customer Segmentation

## 1. What I Implemented

I segmented 440 wholesale customers using their annual spending on six product categories: Fresh, Milk, Grocery, Frozen, Detergents_Paper, and Delicassen. Before clustering, I capped outliers in each feature using the IQR method (1.5×IQR beyond Q1/Q3) so a handful of extreme high-spend accounts wouldn't distort the cluster shapes, then standardized all six features with `StandardScaler` so no single high-magnitude category (like Fresh) would dominate the distance calculations.

I ran K-Means for k = 1–10 and used the elbow in the inertia curve, together with silhouette and Davies–Bouldin scores, to settle on **k = 3**. As a second, comparison algorithm, I ran **Agglomerative (Hierarchical) Clustering with Ward linkage**, also with k = 3, on the same scaled features so the two methods could be compared on equal footing.

## 2. Segment Interpretation (K-Means, k=3)

| Cluster | Size | Dominant spending pattern |
|---|---|---|
| 1 | 249 | Fresh-heavy, everything else low |
| 0 | 101 | Milk, Grocery, and Detergents_Paper heavy |
| 2 | 90 | Very high Fresh, elevated Frozen and Delicassen |

**Cluster 1 – "Fresh-only buyers" (249 customers).** Average spend is led by Fresh (~9,400) while Milk, Grocery, and Detergents_Paper are all low (under 3,600). This looks like small restaurants, cafés, or produce-focused retailers that buy almost exclusively perishable fresh goods and little else.
*Business action:* Offer a high-frequency, small-batch fresh delivery schedule (e.g., every 1–2 days) rather than the standard weekly drop, and consider a freshness/quality loyalty tier, since this is clearly their core purchasing need.

**Cluster 0 – "Grocery/retail staples buyers" (101 customers).** This group spends heavily on Grocery (~16,700), Milk (~10,100), and Detergents_Paper (~7,000) — the classic packaged/retail-shelf categories — while Fresh and Delicassen are comparatively modest. These are likely small supermarkets or convenience stores restocking shelf-stable goods.
*Business action:* Introduce volume-based discounts or bundled staple packages (milk + grocery + paper goods) to encourage larger, less frequent orders, and cross-sell Detergents_Paper to Cluster 1 customers who currently buy almost none.

**Cluster 2 – "High-volume fresh & frozen buyers" (90 customers).** This is the smallest but highest-spending group: Fresh averages ~22,900 (more than double Cluster 1), with clearly elevated Frozen (~5,100) and Delicassen (~2,450) as well. These look like large caterers, hotels, or big retail accounts with broad, high-volume needs across perishable categories.
*Business action:* Assign a dedicated account manager and prioritize cold-chain logistics/capacity for this segment, since they represent disproportionate revenue concentrated in a small number of accounts — losing one is costly, so retention and service-level guarantees matter most here.

## 3. Understanding K-Means

K-Means is an unsupervised algorithm that groups data points into a chosen number of clusters, **k**, based on similarity. It works as an iterative "assign-and-update" loop:

1. **Initialize** k centroids (points in feature space), typically at random or via a smarter method like k-means++.
2. **Assign step:** every data point is assigned to the nearest centroid, usually measured by Euclidean distance, forming k groups.
3. **Update step:** each centroid is recalculated as the mean position of all points currently assigned to it.
4. **Repeat** steps 2–3 until assignments stop changing (or centroids move less than a small tolerance) — this means the algorithm has converged.

The goal is to minimize the total within-cluster sum of squared distances (inertia) between points and their assigned centroid. Because the result depends on where centroids start, K-Means is usually run multiple times with different initializations and the best (lowest-inertia) result is kept.

## 4. Second Algorithm: Agglomerative (Hierarchical) Clustering

I chose **Agglomerative Clustering with Ward linkage** because it clusters using the same standardized feature space but builds groups in a fundamentally different way — bottom-up merging rather than centroid-based partitioning — which makes it a good, distinct point of comparison, and because it produces a dendrogram that can help sanity-check whether k=3 is really a reasonable number of segments.

**How it works:** Agglomerative clustering starts by treating every data point as its own cluster, then repeatedly merges the two closest clusters until only k clusters remain. "Ward linkage" specifically merges the pair of clusters that causes the smallest possible increase in total within-cluster variance at each step, which tends to produce compact, evenly-sized clusters similar in spirit to K-Means' objective.

**One advantage:** It doesn't require committing to k in advance — you can build the full dendrogram once and then "cut" it at whatever number of clusters makes sense, and it's deterministic (no random initialization, so results are reproducible every run).

**One limitation:** It scales poorly to large datasets, since computing and updating the distance/similarity structure across all points is roughly O(n²) or worse in time and memory, and merge decisions are greedy and irreversible — once two clusters are merged, that choice can't be undone even if it turns out to be suboptimal later.

**Silhouette comparison:** K-Means achieved a silhouette score of **0.340** (Davies–Bouldin 1.297), while Agglomerative Clustering scored **0.284** (Davies–Bouldin 1.495) on the same scaled data with k=3. K-Means produced somewhat tighter, better-separated clusters by both metrics. A cross-tab of the two labelings also showed only partial agreement — most of K-Means' Cluster 1 (Fresh-only) mapped onto Agglomerative's cluster 2, but the grocery-heavy and high-fresh groups split and recombined differently, indicating the two algorithms are drawing the segment boundaries in noticeably different places rather than just relabeling the same groups.

## 5. Findings

For this wholesale segmentation task, I would recommend **K-Means** as the primary method. It produced a higher silhouette score and lower Davies–Bouldin index than Agglomerative Clustering, meaning its three segments are more internally consistent and better separated in the scaled feature space. K-Means is also computationally lighter and scales better, which matters if this distributor's customer base grows well beyond 440 accounts, and its cluster centers translate directly into interpretable "average spending profiles" that are easy to explain to a non-technical business audience.

That said, I wouldn't discard hierarchical clustering entirely — its dendrogram is a useful diagnostic tool precisely *because* it doesn't require picking k up front. Before finalizing k=3 for a production segmentation, I'd want to inspect the dendrogram to confirm 3 is a natural cutoff rather than an artifact of the elbow method alone. In practice, I'd use hierarchical clustering as an exploratory/validation step and K-Means as the deployed model that assigns new customers to segments going forward.
