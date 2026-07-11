# Reflection Paper
### Wholesale Customer Segmentation

---

## 1. What Did I Implement?

I segmented the wholesale distributor's clients using only the six continuous annual-spend columns: `Fresh`, `Milk`, `Grocery`, `Frozen`, `Detergents_Paper`, and `Delicassen`, leaving out `Channel` and `Region` since those are pre-existing category labels rather than behavioural measurements. I computed IQR outlier bounds (`k=1.5`, Q1 − 1.5·IQR to Q3 + 1.5·IQR) for each spend column, then standardized all six features with `StandardScaler` so that no single high-value category like Fresh would dominate the distance calculations simply because it's measured in larger numbers.

I ran K-Means for `k = 1` through `10` and recorded the SSE (inertia) at each step to build an elbow plot, then trained the final model with `KMeans(n_clusters=3, n_init="auto", random_state=42)`. Each client was assigned a `Cluster` label (0–2), and I converted the cluster centroids back into original spend units with `scaler.inverse_transform()` so they'd be interpretable in real currency terms. As a second, independently researched algorithm, I trained an `AgglomerativeClustering` model (ward linkage, `n_clusters=3`) on the same six standardized features and compared it against K-Means using the Silhouette Score and Davies–Bouldin Index.

*(Note to self for a future pass: I calculated the IQR lower/upper bounds for each column but never actually called `.clip()` with them before scaling, so the outlier-capping step didn't end up changing the data — the largest spenders are still fully present in the clusters below. That's worth fixing before a final submission, since it likely explains why Cluster 1 below is so small and so extreme.)*

## 2. Segment Interpretation

The K-Means cluster centers in original spend units show three clearly different groups:

**Cluster 0 — Everyday, moderate-spend clients (350 clients, the large majority).** Average spend across all six categories is modest and fairly balanced (Fresh ≈8,936, Milk ≈4,229, Grocery ≈5,848, Detergents_Paper ≈1,914). This is the "typical" client — a small shop or restaurant with steady, unremarkable order volumes. *Business action:* keep this group on a standard delivery and pricing plan, but look for upsell opportunities (e.g., bundling Detergents_Paper with Grocery orders) since their spend is currently spread thin across categories rather than concentrated anywhere.

**Cluster 1 — Extreme Fresh/Frozen buyers (53 clients).** This group's Fresh spend (≈34,540) and Frozen spend (≈9,842) are far above every other cluster, while Detergents_Paper stays low (≈981). These look like large-scale HoReCa operations — big hotels, catering firms, or restaurant chains — buying enormous volumes of perishable stock. *Business action:* this group deserves a dedicated cold-chain logistics track (refrigerated trucks, tighter delivery windows) since spoiled inventory would be very costly for both the client and the distributor at this volume.

**Cluster 2 — High Grocery/Detergents_Paper retail buyers (37 clients).** This group stands out for very high Grocery (≈30,466) and by far the highest Detergents_Paper spend (≈14,759), with comparatively low Fresh (≈8,705). This profile matches supermarkets or larger grocery retailers restocking shelf-stable goods in bulk. *Business action:* offer this group volume-based contract pricing and scheduled (e.g., weekly) bulk deliveries rather than urgent restocking, since none of their top categories are perishable.

## 3. Understanding K-Means

In my own words, K-Means is an algorithm that splits a set of data points into `k` groups so that the points inside each group are as close together as possible. It works through a repeating two-step cycle:

1. **Assign:** for every data point, measure its distance to each of the `k` centroids (the current "center" positions) and assign the point to whichever centroid is nearest. This creates `k` groups.
2. **Update:** recompute each centroid as the mean position of all the points currently assigned to it, so the centroid moves toward the middle of its group.

These two steps repeat — assign, then update, then assign again with the new centroid positions — until the centroids stop moving by more than a small tolerance, at which point the algorithm has converged. The number of clusters, `k`, is not something the algorithm figures out on its own; it has to be chosen in advance, which is exactly why I ran the elbow method first, to get some evidence for a reasonable value of `k` before committing to `k=3` for the final model.

## 4. My Second Algorithm

I chose **Agglomerative (Hierarchical) Clustering** with ward linkage as my second algorithm, because wholesale client types don't necessarily split into perfectly flat, evenly separated groups — there's a natural nesting to spending behaviour (smaller and larger versions of the same basic client type), and hierarchical clustering builds a tree of nested groupings that can reveal that structure, which K-Means can't show directly.

From researching scikit-learn's documentation on hierarchical clustering, I learned that agglomerative clustering starts with every point as its own cluster and repeatedly merges the two closest clusters until only the target number remain. With ward linkage, "closest" means whichever merge increases total within-cluster variance the least — the same underlying objective K-Means optimizes, which is what makes the two methods reasonably comparable. One advantage is that it doesn't assume clusters are round or evenly sized, unlike K-Means. One limitation is that a merge, once made, can never be undone later in the process, and it also scales worse computationally on larger datasets than K-Means does.

On this dataset, K-Means came out ahead: a Silhouette Score of **0.458** versus **0.265** for Hierarchical Clustering, and a Davies–Bouldin Index of **1.249** versus **1.285** (lower is better here, so K-Means also won on that metric). Interestingly, Hierarchical Clustering's cluster sizes were far more lopsided (6 / 281 / 153) than K-Means' (350 / 53 / 37), which suggests the two algorithms are drawing the group boundaries in noticeably different places, even though both were asked for 3 clusters.

## 5. My Findings

Based on both metrics, I'd recommend **K-Means** as the primary clustering approach for this task. It scored meaningfully better than Hierarchical Clustering on both the Silhouette Score and the Davies–Bouldin Index, meaning its three segments are more compact and better separated in the six-dimensional spend space. It's also cheap to retrain as new client data comes in, and its cluster centroids translate directly into a simple business story ("this group spends mostly on X and Y"), which matters if the distributor's sales team needs to act on these segments without a data science background.

That said, I wouldn't discard the hierarchical clustering result entirely — its very different, more lopsided grouping (6/281/153 vs. K-Means' 350/53/37) is itself a useful signal. It suggests the six-dimensional spend data may not have three naturally equal-sized, evenly separated "true" clusters, and that the boundary between groups is more sensitive to the clustering method than I initially expected. Before treating either result as final, I'd want to go back and actually apply the IQR clipping I calculated but never used, and re-run the elbow method and both metrics again, since a handful of extreme outliers (like the Fresh ≈34,540 cluster) can easily pull K-Means' centroids toward themselves and make a cluster look more "extreme" than the typical client in that group really is.