# Part C — Reflection Paper
## What did you implemented?
A hybrid data pipeline was built to segment wholesale clients using their annual spending across six columns (Fresh, Milk, Grocery, Frozen, Detergents_Paper, Delicassen). Categorical variables (Channel/Region) were excluded. The pipeline clips outliers using an IQR filter, standardizes features with StandardScaler, and runs K-Means alongside DBSCAN for side-by-side comparison.
## Segment Interpretation
Based on K-Means (K=2), clients split into two clear profiles:
- Cluster 0: Retailers & Supermarkets
Behavior: High spend on Grocery and Detergents_Paper.
Action: Offer volume discounts on non-perishables and household bundles.
- Cluster 1: Hospitality/Food Service (HoReCa)
Behavior: Heavy spend on Fresh and Frozen goods.
Action: Provide a "Just-In-Time" daily fresh delivery subscription to guarantee freshness.
## Understanding K-MeansK-Means 
is an algorithm that groups data into a chosen number of clusters (K) using an iterative assign-and-update loop.
- Centroids: Randomly places K center points (centroids) in the data space.
- Assign: Maps every data point to its closest centroid using geometric distance.
- Update: Moves each centroid to the exact mathematical average (mean) of its assigned points.
## Evaluation of the Second Algorithm (DBSCAN)
- Why Chosen: Wholesale data contains massive corporate outliers. DBSCAN groups data based on density rather than distance from a center, allowing it to isolate anomalies as Noise (-1) instead of forcing them into clusters.
- Pros & Cons: It finds cluster shapes automatically and handles outliers cleanly, but it struggles if different clusters have wildly varying densities.
- Performance: K-Means achieved a higher Silhouette Score (0.241) than DBSCAN (0.044) because the dataset has a well-distributed structure that K-Means can partition effectively, while DBSCAN struggled with the current hyperparameters.
## Final Findings & Recommendation
The ideal approach for this dataset is a hybrid framework: use DBSCAN to filter out extreme outliers, then apply K-Means to group the remaining stable clients. Running standalone K-Means allows extreme spenders to warp the cluster centers, ruining the profiles of average clients. Conversely, using standalone DBSCAN leaves high-value outliers completely unlabeled. By isolating anomalies first with DBSCAN (to be handled by VIP account managers), the distributor can use K-Means on the clean data to generate stable, highly actionable marketing segments.