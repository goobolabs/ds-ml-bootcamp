# Reflection Paper — Wholesale Customer Segmentation

---

## 1. What I Implemented

I segmented 440 wholesale clients using their annual spending across six product categories: Fresh, Milk, Grocery, Frozen, Detergents_Paper, and Delicassen. Channel and Region were kept out of the clustering features — they describe where clients are, not what they buy.

The pipeline followed the same pattern as previous assignments: IQR capping to handle extreme spend values, StandardScaler to normalize the features, then K-Means with k=5 from the lesson. I added Agglomerative Clustering as the second method using the same scaled features and the same k for a fair comparison.

---

## 2. Segment Interpretation

Looking at the K-Means cluster centers in original spend units:

**Cluster 3 — High Fresh, Low Everything Else** (~22,347 Fresh, ~3,409 Milk, ~583 Detergents_Paper): These clients spend heavily on fresh produce but very little on packaged or cleaning products. Most likely restaurants and food service businesses that need large quantities of raw ingredients daily.
_Business action:_ Offer bulk fresh produce contracts with priority delivery slots.

**Cluster 4 — High Grocery and Detergents_Paper** (~4,917 Fresh, ~18,350 Grocery, ~7,780 Detergents_Paper): Almost no fresh food but very high spend on grocery and cleaning products. This looks like retail shops or small supermarkets stocking household goods.
_Business action:_ Bundle grocery and detergent orders with volume discounts.

**Cluster 1 — Low Spend Across All Categories** (~8,376 Fresh, ~2,151 Milk, ~779 Detergents_Paper): The lowest overall spenders in the dataset. Likely small or infrequent buyers — small cafes or occasional clients.
_Business action:_ Send targeted promotions to increase order frequency or basket size.

---

## 3. Understanding K-Means

K-Means groups data by finding k centroids — one per cluster — and assigning every data point to the nearest one. The process starts by placing k centroids randomly, then runs two steps in a loop: assign each point to the closest centroid, then move each centroid to the mean of its assigned points. This repeats until the centroids stop changing. The result is k groups where points inside each group are as similar as possible to each other.

---

## 4. My Second Algorithm — Agglomerative Clustering

I chose Agglomerative (Hierarchical) Clustering because it works from a completely different logic than K-Means — no centroids, no iterative updates. It starts with every data point as its own cluster and repeatedly merges the two closest clusters until only k remain. I used Ward linkage, which minimizes the total within-cluster variance at each merge step.

**Advantage:** Does not depend on random initialization, so the result is deterministic and reproducible without needing random_state.

**Limitation:** Merges are permanent — once two points are merged, they stay together even if a later merge would have been better. Also slower than K-Means on large datasets.

The Silhouette Score for Agglomerative Clustering was close to K-Means, which makes sense — both methods with k=5 on the same scaled data should find similar natural groupings in the spending patterns.

---

## 5. My Findings

K-Means is the better practical choice for this segmentation task. It is faster, more interpretable through the cluster centers, and the Elbow Method gives a clear way to justify the choice of k. The cluster centers in original spend units make it easy to explain each segment to a business stakeholder — you can say "Cluster 3 clients spend on average $22,000 on fresh produce" and that is immediately useful.

Agglomerative Clustering is a solid alternative for validation — if it produces similar groupings to K-Means, that gives more confidence that the segments are real and not just an artifact of K-Means initialization. For a dataset this size (440 rows) it runs fast enough to be practical. But for a production system processing thousands of clients regularly, K-Means scales better and is the right default.
