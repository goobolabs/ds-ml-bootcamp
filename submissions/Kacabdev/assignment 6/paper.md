# Assignment Six — Part A: Clustering Theory

## 1. Introduction to Unsupervised Learning and Clustering

Unsupervised learning is a branch of machine learning in which a model is
given a dataset that has no labeled target variable, and it must find
structure in the data on its own. Instead of being told the "right answer"
for each example, the algorithm looks for patterns, groupings, or
relationships that already exist in the feature space — for example, which
data points are similar to one another, or which dimensions carry the most
variance in the data.

This is fundamentally different from **supervised learning**, which covers
both regression and classification. In supervised learning, every training
example comes with a known target: a continuous value in regression (e.g.,
predicting a house price) or a category in classification (e.g., predicting
whether an email is spam). The model learns a mapping from inputs to a known
output and is evaluated by comparing its predictions against ground-truth
labels. In unsupervised learning there is no ground truth to compare
against; success is judged by internal criteria such as how compact and
well-separated the discovered groups are, not by prediction accuracy against
a known answer.

- **Real-life example of clustering:** A telecom company groups its
  subscribers by call, data, and SMS usage patterns to design different
  subscription plans for "heavy data users," "occasional callers," and
  "roaming travelers," without knowing in advance which plan each customer
  should belong to.
- **Real-life example of supervised learning:** A bank predicts whether a
  loan applicant will default based on historical applications where the
  outcome (defaulted / repaid) is already known, and uses that label to
  train a classification model.

## 2. Clustering Algorithms

### K-Means

**How it works:** K-Means partitions data into a fixed number, *k*, of
clusters. It starts by placing *k* centroids (either randomly or via a
smarter method such as k-means++), then repeats two steps until
convergence: (1) assign each point to its nearest centroid using Euclidean
distance, and (2) recompute each centroid as the mean of the points assigned
to it. This "assign-and-update" loop minimizes the within-cluster sum of
squared distances (SSE).

**Real-world use case:** Segmenting retail or wholesale customers by their
annual spending across product categories, so that a distributor can design
different pricing or delivery strategies per segment.

**Advantages:** Simple, fast, and scales well to large datasets; easy to
interpret because each cluster has a clear centroid.

**Limitations:** Requires *k* to be chosen in advance; assumes clusters are
roughly spherical and similarly sized; sensitive to outliers and to feature
scaling; can converge to a poor local minimum depending on initialization.

### Hierarchical Clustering (Agglomerative)

**How it works:** Agglomerative hierarchical clustering starts with every
data point as its own cluster and repeatedly merges the two closest clusters
until only one cluster remains (or until a target number of clusters is
reached). "Closeness" between clusters is defined by a linkage criterion —
common choices are single, complete, average, or Ward linkage (which merges
the pair that produces the smallest increase in within-cluster variance).
The result can be visualized as a dendrogram, a tree diagram showing the
order in which clusters were merged.

**Real-world use case:** Grouping documents or gene-expression profiles into
a taxonomy of related items, where a natural nested structure (clusters
within clusters) is expected.

**Advantages:** Does not require choosing *k* in advance (it can be read off
the dendrogram at any cut height); produces an interpretable hierarchy; works
with any distance metric, not just Euclidean.

**Limitations:** Computationally expensive for large datasets (typically
O(n²) or worse in memory and time); merge decisions are greedy and cannot be
undone, so an early bad merge propagates through the rest of the tree; less
scalable than K-Means for very large *n*.

### DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

**How it works:** DBSCAN groups together points that are closely packed,
based on two parameters: `eps` (the neighborhood radius) and `min_samples`
(the minimum number of points required to form a dense region). A point with
at least `min_samples` neighbors within `eps` becomes a "core point," and
core points that are close to each other are merged into the same cluster.
Points that do not belong to any dense region are labeled as noise/outliers.

**Real-world use case:** Detecting anomalies or fraud in transaction data,
or identifying geographic hotspots of activity (e.g., clusters of
crime incidents or ride-hailing pickup points) where clusters can be
irregularly shaped.

**Advantages:** Does not require specifying the number of clusters in
advance; can find arbitrarily shaped clusters (not just spherical ones);
naturally identifies outliers as noise rather than forcing them into a
cluster.

**Limitations:** Sensitive to the choice of `eps` and `min_samples`, which
can be hard to tune; struggles with clusters of very different densities;
performance degrades in high-dimensional feature spaces because distance
becomes less meaningful ("curse of dimensionality").

## 3. Clustering Metrics

- **Elbow Method (SSE):** Plots the sum of squared errors (within-cluster
  variance) against different values of *k*. As *k* increases, SSE always
  decreases, but the rate of improvement slows down after the "true" number
  of clusters is reached, forming a bend or "elbow" in the curve. That bend
  is used as a heuristic for choosing *k*.
- **Silhouette Score:** For each point, it compares the average distance to
  points in its own cluster (cohesion) against the average distance to
  points in the nearest neighboring cluster (separation). The score ranges
  from -1 to +1; values close to +1 mean the point is well matched to its
  own cluster and poorly matched to neighboring clusters.
- **Davies–Bouldin Index (DBI):** For every cluster, it computes the ratio
  of within-cluster scatter to between-cluster separation from the most
  similar other cluster, and averages these ratios across all clusters.
  Unlike the Silhouette Score, lower values indicate better clustering
  (compact, well-separated clusters), and there is no fixed upper bound.

| Metric | What it measures | Good value looks like |
|---|---|---|
| Elbow Method (SSE) | Total within-cluster variance as a function of k | The k at the "elbow," where SSE stops dropping sharply |
| Silhouette Score | Cohesion vs. separation, per point, averaged over all points | Close to +1 (values near 0 indicate overlapping clusters, negative values indicate likely misassignment) |
| Davies–Bouldin Index | Average similarity between each cluster and its closest neighbor | Close to 0 (lower is better; there is no fixed maximum) |

## 4. Choosing k and Interpreting Segments

Choosing the number of clusters, *k*, for K-Means is not an exact science;
it is usually approached by combining several signals rather than relying on
a single rule. The Elbow Method gives a visual heuristic for where adding
more clusters stops meaningfully reducing SSE. The Silhouette Score and
Davies–Bouldin Index can be computed for a range of *k* values, and the *k*
that gives the best (highest Silhouette, lowest DBI) score is a strong
candidate. Beyond the purely statistical view, domain knowledge matters: in
a business context like wholesale distribution, a value of *k* that produces
segments the sales and marketing teams can actually act on (e.g., 4–6
distinguishable customer types) is often preferred over a statistically
"optimal" but impractical value of *k* (such as 20 tiny clusters).

In the wholesale distributor project, a cluster with **high Fresh + Milk
spend** typically represents businesses like small restaurants, cafés, or
caterers that buy large volumes of perishable, ready-to-serve goods for
daily food preparation. A cluster with **high Grocery + Detergents_Paper
spend** typically represents retail-type buyers such as small supermarkets
or convenience stores, which stock packaged, shelf-stable goods and
cleaning/paper supplies in bulk. Recognizing this distinction lets the
distributor tailor delivery frequency (perishables need more frequent
delivery), credit terms, and product bundling to each segment.

We exclude `Channel` and `Region` from the clustering features because they
are categorical identifiers rather than spending behavior. Including them
directly would mix a nominal, non-ordinal scale with continuous spend
variables, distorting Euclidean distance calculations that K-Means depends
on. More importantly, the goal of the exercise is to discover behavioral
segments purely from *how much* a customer spends on each product category;
`Channel` and `Region` are kept aside so they can be used afterward as an
external, independent check on whether the discovered spending-based
clusters line up with real-world business categories (e.g., does the
"high Fresh + Milk" cluster largely correspond to Channel = HoReCa?).

## 5. Real-World Case Study

A study applying an extended RFM-style clustering framework (the LRFMP
model — Length, Recency, Frequency, Monetary, Periodicity) to a grocery
retail chain illustrates how clustering is used for customer segmentation
in a live business setting. The goal of the project was to move a grocery
retailer beyond simple demographic segmentation toward a data-driven
understanding of purchasing behavior, so that customer relationship
management (CRM) and marketing strategies could be tailored to each group.
The data used consisted of real transactional records from a grocery chain,
from which the LRFMP behavioral attributes were engineered for every
customer. K-Means clustering was applied to these engineered features, with
the number of clusters selected using multiple validation indices rather
than a single metric. The key result was the identification of five
distinct customer profiles — described as high-contribution loyal
customers, low-contribution loyal customers, uncertain customers,
high-spending lost customers, and low-spending lost customers — each of
which was paired with a specific recommended CRM or marketing action (for
example, win-back campaigns for high-spending customers who had stopped
purchasing, versus loyalty rewards for the high-contribution loyal group).
This mirrors the approach used in this assignment: raw transactional/
spending data is transformed into a small set of numeric features, scaled,
clustered, and then interpreted in business terms so that concrete actions
can be attached to each segment.

*Source:* "LRFMP model for customer segmentation in the grocery retail
industry: a case study," available via ResearchGate
(https://www.researchgate.net/publication/315979555).
