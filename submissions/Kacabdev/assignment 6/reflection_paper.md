# Assignment Six — Part C: Reflection Paper

## 1. What did I implement?

I segmented the 440 clients in the wholesale customers dataset using their
annual spending across six product categories: `Fresh`, `Milk`, `Grocery`,
`Frozen`, `Detergents_Paper`, and `Delicassen`. `Channel` and `Region` were
excluded from the clustering features and kept only for later validation.
After capping outliers in each spend column with the IQR method (k=1.5) and
standardizing all six features with `StandardScaler`, I trained two
clustering models on the identical scaled feature matrix: K-Means (k=5,
`random_state=42`, reproducing the Lesson 6 script) and Agglomerative
Clustering with Ward linkage (also 5 clusters) as my independently
researched second algorithm. Both models were evaluated with the Silhouette
Score and the Davies–Bouldin Index, and their outputs were compared directly
on the same three sample clients as a sanity check.

## 2. Segment Interpretation

Based on the K-Means cluster centers (converted back to original spend
units), three of the five segments stood out clearly:

- **Cluster 1 (n=191, the largest group) — "Small / low-volume buyers."**
  Low spend across nearly every category, with Fresh (~8.4k) as the only
  moderately sized line item and everything else well below the dataset
  average. **Business action:** these are likely small accounts or
  occasional buyers; the distributor could offer a simplified, low-minimum
  order tier or bundle small orders together to keep delivery costs
  efficient, rather than treating them the same as high-volume clients.

- **Cluster 3 (n=88) — "Fresh & Frozen heavy, HoReCa-style buyers."** High
  spend on Fresh (~22.3k) and Frozen (~5.8k), but low Milk, Grocery, and
  Detergents_Paper. This spending pattern is typical of restaurants, cafés,
  or caterers that need perishable, ready-to-cook ingredients rather than
  packaged goods. **Business action:** offer more frequent, smaller
  deliveries (since fresh/frozen goods spoil quickly) and prioritize
  reliability of the cold-chain logistics for this segment.

- **Cluster 4 (n=60) — "Grocery & Detergents_Paper heavy, retail-style
  buyers."** High spend on Grocery (~18.3k) and Detergents_Paper (~7.8k),
  with comparatively low Fresh and Frozen spend. This looks like small
  supermarkets or convenience stores stocking shelf-stable goods.
  **Business action:** offer bulk-purchase discounts and less frequent but
  larger deliveries, since these products have longer shelf life and can be
  warehoused.

(The remaining two clusters — a mid-size balanced spender segment and a
small group of very high-volume clients across all categories — round out
the full five-cluster picture but were less distinct to describe in a short
paragraph than the three above.)

## 3. Understanding K-Means

In my own words, K-Means is an algorithm that tries to split a dataset into
*k* groups so that points within the same group are as close to each other
as possible. It works in a loop: first, it picks *k* starting points called
centroids (in this project, scikit-learn's `n_init="auto"` runs this
initialization multiple times and keeps the best result). Then it repeats
two steps until nothing changes anymore: **assign** — every data point is
matched to whichever centroid is nearest to it (using straight-line/
Euclidean distance) — and **update** — each centroid is recalculated as the
average position of all the points now assigned to it. Since the centroid
moves after every update, some points that were closest to one centroid may
now be closer to a different one, so the assignment step runs again. This
"assign-and-update" cycle keeps repeating until the assignments stop
changing, at which point the algorithm has converged and each of the *k*
clusters is defined by its final centroid.

## 4. My Second Algorithm

I chose **Agglomerative (Hierarchical) Clustering with Ward linkage**. I
picked it because, unlike K-Means, it does not need spherical, equally
sized clusters and instead builds clusters bottom-up by repeatedly merging
the two most similar groups, which felt like a natural fit for spending
data that can have nested structure (e.g., a broad "high grocery" segment
that further splits into sub-groups). From researching it (scikit-learn's
clustering documentation), I learned that Ward linkage specifically merges
the pair of clusters that causes the smallest possible increase in total
within-cluster variance at each step, which is conceptually close to what
K-Means optimizes, making the two methods reasonably comparable on the same
scaled features. **One advantage** I found is that it does not require
randomly initializing centroids, so it is deterministic — running it twice
on the same data always gives the same result. **One limitation** I ran
into is scalability: because it has to track distances between every pair
of clusters as they merge, it becomes slow and memory-heavy on large
datasets, which would matter if this distributor's real customer base were
in the hundreds of thousands rather than 440 clients.

On this dataset, the Silhouette Score for Agglomerative Clustering was
**0.2185**, compared to **0.2831** for K-Means — so K-Means produced
somewhat better-separated clusters here. The Davies–Bouldin Index agreed
with this ranking (1.2701 for K-Means vs. 1.3245 for Agglomerative, where
lower is better).

## 5. My Findings

For this specific wholesale segmentation task, I would recommend **K-Means**
as the primary method, mainly because it produced the higher Silhouette
Score and lower Davies–Bouldin Index on the same standardized features, and
because its cluster centers are directly interpretable in the original
spend units (via `inverse_transform`), which makes it easy to explain each
segment to a non-technical sales or marketing audience ("this group spends
heavily on Fresh and Frozen"). K-Means is also cheap to re-run as new
customer data arrives, which matters for a distributor that would want to
refresh these segments periodically.

That said, I would not dismiss Agglomerative Clustering entirely — its
dendrogram gives a view of *how* segments relate to and split from one
another, which could help the business decide whether to use a coarser
3-segment view or a finer 7-segment view depending on how granular the
marketing team wants to get, without having to retrain the model from
scratch for every candidate *k*. In a scenario with a much larger customer
base, however, I would lean further toward K-Means (or a scalable density
method like DBSCAN) purely because Agglomerative Clustering's computational
cost grows quickly with the number of clients.
