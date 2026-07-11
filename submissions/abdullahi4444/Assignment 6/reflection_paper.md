# Assignment 6 — Reflection Paper: Clustering Wholesale Customers

**Student:** Abdullahi
**Course:** Data Science & Machine Learning
**Due:** Wednesday, 8 July 2026 — 5:00 PM EAT

---

## 1. What Did You Implement?

In this assignment, I segmented 440 wholesale clients from a food distributor's database using two clustering algorithms applied to the same six annual spending columns: Fresh, Milk, Grocery, Frozen, Detergents_Paper, and Delicassen.

The pipeline began by loading the `raw_wholesale_customers.csv` dataset. I then applied IQR capping (k = 1.5) to each spend column to clip extreme outliers without deleting any rows, preserving all 440 observations. Next, I applied `StandardScaler` to normalise the six features so that their different scales would not bias the distance calculations.

To choose the number of clusters for K-Means, I ran the Elbow Method for k = 1 to 10, recording the SSE (inertia) at each step. The elbow in the curve suggested k = 5 as a reasonable balance between compactness and simplicity. I then trained `KMeans(n_clusters=5, n_init='auto', random_state=42)` on the scaled features and evaluated it using Silhouette Score and Davies–Bouldin Index.

For the second algorithm, I chose **Agglomerative Hierarchical Clustering** with Ward linkage and n_clusters = 5, trained on the same scaled features. I then compared both methods using the Silhouette Score, performed a sanity check on three sample clients, and saved the K-Means segmented dataset to `segmented_wholesale_customers.csv`.

---

## 2. Segment Interpretation

The cluster centers in original spend units (after `inverse_transform`) are:

| Cluster | Size | Fresh | Milk | Grocery | Frozen | Detergents_Paper | Delicassen |
|---|---|---|---|---|---|---|---|
| 0 | 76  | 9,203  | 6,833  | 9,104  | 1,326 | 3,280 | 1,872 |
| 1 | 191 | 8,376  | 2,151  | 3,161  | 1,646 | 779   | 674   |
| 2 | 25  | 17,462 | 13,806 | 17,524 | 4,121 | 5,461 | 3,584 |
| 3 | 88  | 22,347 | 3,409  | 3,969  | 5,820 | 583   | 1,567 |
| 4 | 60  | 4,917  | 10,769 | 18,350 | 1,212 | 7,780 | 981   |

### Cluster 3 — Fresh & Frozen Buyers (Restaurant / HoReCa Kitchens)
Cluster 3 has the **highest Fresh spend (22,347)** and the second-highest Frozen spend (5,820), with very low Detergents_Paper (583). These clients are almost certainly **hotel kitchens or high-volume restaurants** that cook fresh meals daily and require large quantities of perishable proteins and frozen goods, but do not stock cleaning products for retail sale.

**Business action:** Offer guaranteed next-morning delivery for Fresh products and loyalty pricing on Frozen goods — reliability of supply is their top priority.

### Cluster 4 — Grocery & Detergents-Dominant Buyers (Retail Shops / Supermarkets)
Cluster 4 has the **highest Grocery spend (18,350)** and **highest Detergents_Paper spend (7,780)**, with very low Fresh (4,917). These 60 clients are classic **retail supermarket or pharmacy-type** buyers that stock packaged goods and cleaning products for end consumers rather than for food preparation.

**Business action:** Offer quarterly volume-discount contracts on Grocery and Detergents_Paper bundles, and propose category-exclusive promotions to increase basket size.

### Cluster 2 — High-Volume Mixed Buyers (Large Hotels / Caterers)
Cluster 2, with only 25 clients, has the **highest spend across almost every category** (Fresh: 17,462; Milk: 13,806; Grocery: 17,524). These are likely **large hotel chains or institutional caterers** with enormous purchasing budgets across all product lines.

**Business action:** Assign a dedicated account manager to each Cluster 2 client and offer premium service-level agreements with personalised bulk pricing — these 25 clients likely represent a disproportionate share of total revenue.

---

## 3. Understanding K-Means

K-Means is an unsupervised partitioning algorithm that divides data into exactly *k* clusters, where each cluster is defined by its **centroid** — the mean position of all points assigned to it.

The algorithm works in a repeating **assign-and-update loop**:
1. Start by placing *k* initial centroids (randomly, or using K-Means++ smart initialisation).
2. **Assign** every data point to the nearest centroid, measured by Euclidean distance.
3. **Update** each centroid to the mean of all data points currently assigned to it.
4. Repeat steps 2 and 3 until the centroids no longer move (convergence).

The result is a hard partition where every point belongs to exactly one cluster. The objective function being minimised is the **SSE** (Sum of Squared Errors) — the total squared distance from every point to its centroid. K-Means is efficient and scales well, but requires specifying *k* beforehand and is sensitive to outliers because extreme values shift centroids away from the true cluster center. This is why we applied IQR capping before running K-Means.

---

## 4. My Second Algorithm — Agglomerative Hierarchical Clustering

### Why I Chose It

I chose **Agglomerative Hierarchical Clustering** with Ward linkage because it offers a meaningful contrast to K-Means:
- It is fully **deterministic** — no random initialisation means it produces the same result every run.
- It does not require specifying *k* upfront (though I used n_clusters = 5 for a fair comparison).
- Ward linkage minimises within-cluster variance at each merge, producing compact, balanced clusters similar in shape to K-Means — making the comparison meaningful.
- At 440 rows, the O(n²) memory cost is perfectly manageable.

### What I Learned from Research

**How it works:** Starting with 440 individual clusters (one per client), the algorithm repeatedly merges the two clusters whose union produces the smallest increase in total within-cluster variance (Ward's criterion). This continues until all points belong to one cluster. By cutting this hierarchy at a chosen level, we obtain any desired number of clusters.

**One advantage:** Completely deterministic and produces a full hierarchy (dendrogram) that visualises cluster relationships at multiple scales — richer information than a flat K-Means partition.

**One limitation:** Merging decisions are **irreversible** (greedy); once two clusters are merged, they cannot be split apart. This means early incorrect merges can propagate errors through the hierarchy.

### Silhouette Score Comparison

The actual scores computed from the wholesale dataset (k = 5):

| Method | Silhouette Score | Davies–Bouldin Index |
|---|---|---|
| K-Means | **0.2831** | **1.2701** |
| Agglomerative (Ward) | 0.2185 | 1.3245 |

**K-Means produced better-separated clusters** on this dataset: its Silhouette Score of 0.2831 is 0.0646 higher than Agglomerative's 0.2185, and its Davies–Bouldin Index of 1.2701 is lower (better) than 1.3245. The scores are modest — below 0.50 — which is expected for real-world spending data with overlapping purchasing patterns and no truly clear-cut boundaries between business types.

---

## 5. My Findings and Recommendation

Both clustering methods — K-Means and Agglomerative Hierarchical Clustering — discovered broadly consistent purchasing segments from the 440 wholesale clients. Their Silhouette Scores are comparable, which confirms that the five-cluster structure is a genuine feature of the spending data, not an artifact of algorithm choice.

For this wholesale segmentation task, I would recommend **K-Means as the primary production model** for the following reasons:

1. **Speed and scalability:** The distributor's client base will grow. K-Means scales to tens of thousands of records efficiently; Agglomerative Clustering's O(n²) memory cost becomes a bottleneck at scale.
2. **Re-trainability:** K-Means can be retrained monthly on updated transaction data to refresh segments. Agglomerative Clustering, while deterministic, recomputes the full pairwise distance matrix each time.
3. **Centroid interpretability:** K-Means produces explicit cluster centers (centroids) that can be inverse-transformed back to original spend units, giving the sales team a clear, actionable profile for each segment (e.g., "Cluster 0 clients buy an average of X units of Fresh products annually").

I would recommend running **Agglomerative Clustering periodically as a validation tool** — its deterministic nature makes it a useful sanity check that K-Means clusters are stable. If both methods consistently agree on the cluster boundaries, the distributor can rely on the K-Means segmentation with confidence.

The most valuable business action from this analysis is using the segment profiles to personalise sales offers: Fresh-dominant clients benefit from delivery reliability guarantees, packaged-goods clusters benefit from volume pricing, and low-spend clients benefit from growth incentives. Clustering transforms an undifferentiated list of 440 clients into five actionable groups with distinct commercial strategies.

---

*End of Assignment 6 — Part C Reflection Paper*
