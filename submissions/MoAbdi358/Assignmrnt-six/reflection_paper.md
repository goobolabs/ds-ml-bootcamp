# Reflection Paper — Wholesale Customer Segmentation

**Assignment Six — Part C**
**Author:** Mohamed Abdi

---

## 1. What I Implemented

I segmented the 440 wholesale customers using their annual spending across six
product categories (Fresh, Milk, Grocery, Frozen, Detergents_Paper,
Delicassen). After capping extreme outliers with the IQR method and scaling
the features with `StandardScaler`, I trained two clustering models on the
same six-column feature set: **K-Means** (k = 5, matching the lesson) and
**Agglomerative (Hierarchical) Clustering** with Ward linkage (also 5
clusters), which I researched myself as the required second algorithm.

## 2. Segment Interpretation

Looking at the K-Means cluster centers (converted back to original spend
units), three segments stand out clearly:

- **A large, low-spend segment (191 customers):** Spending is modest across
  every category, with Fresh as the largest line item and very little spent
  on Grocery or Detergents_Paper. These look like small, budget-driven
  accounts. *Business action:* offer volume-based discounts or a loyalty
  program to grow their basket size before investing heavily in
  relationship management here.

- **A high-Fresh / high-Frozen segment (~88 customers):** Fresh and Frozen
  spend are both well above average, while Grocery and Detergents_Paper stay
  low — the classic signature of Horeca-type buyers (restaurants, hotels,
  cafés) stocking ingredients rather than shelf goods. *Business action:*
  prioritize reliable, frequent delivery of perishables and flexible order
  sizing, since these customers' businesses depend on freshness and
  consistency.

- **A small but very high-spend segment (~25 customers):** Every category is
  elevated, especially Fresh, Milk and Grocery — these are the distributor's
  biggest accounts by far, even though they're a small fraction of the
  customer base. *Business action:* assign dedicated account management and
  negotiate long-term contracts, since losing even one of these customers
  would have an outsized revenue impact.

## 3. Understanding K-Means

In my own words: K-Means is a way of automatically sorting data points into
*k* groups based on how similar they are to each other. You start by picking
*k* random center points (centroids). Every data point is then assigned to
whichever centroid it's closest to. Once everyone has a group, each
centroid moves to the average position of the points now assigned to it.
Then the assignment step repeats with the updated centroids. This
"assign-then-update" loop keeps running until the assignments stop changing —
at that point the clusters have stabilized and the algorithm stops.

## 4. My Second Algorithm

I chose **Agglomerative (Hierarchical) Clustering with Ward linkage**. I
picked it because, unlike K-Means, it doesn't assume the clusters have to be
round and evenly sized, and because it doesn't rely on random starting
points, so it gives the same result every time on the same data — useful when
comparing against K-Means for this assignment.

From my research: it works by starting with every single customer as their
own tiny cluster, then repeatedly merging the two closest clusters together
(Ward linkage merges whichever pair increases within-cluster variance the
least) until you're down to the target number of clusters. **One advantage**
is that it doesn't need a `k` decided in advance — you can look at the merge
history (a dendrogram) and decide afterward. **One limitation** is that it
gets slow and memory-heavy on larger datasets, because it has to compare
distances between every pair of points.

On this dataset, its **Silhouette Score (≈0.22) was lower than K-Means'
(≈0.28)**, meaning K-Means produced somewhat more clearly separated clusters
here.

## 5. My Findings

For this specific wholesale segmentation task, I would recommend **K-Means**
as the primary method. It scored higher on the Silhouette metric, meaning its
clusters are more internally consistent and better separated, and its
centroids are easy to explain to a non-technical audience ("this group spends
heavily on Fresh and Frozen" is intuitive in a way a dendrogram cut is not).
It's also fast enough to re-run every time new sales data comes in, which
matters for a distributor that wants to keep segments current.

That said, I wouldn't throw away Hierarchical Clustering entirely — I'd keep
it as a diagnostic tool. Its dendrogram is genuinely useful the first time you
segment a new dataset, because it shows visually how many "natural" groups
exist before you commit to a fixed *k* for K-Means. In practice, I'd use
Hierarchical Clustering once, upfront, to sanity-check the choice of *k=5*,
and then rely on K-Means for the ongoing, repeatable segmentation work.
