import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score, davies_bouldin_score
import matplotlib
matplotlib.use("Agg")  # headless plotting, safe for venv/CI runs
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 160)

RANDOM_STATE = 42
FEATURES = ["Fresh", "Milk", "Grocery", "Frozen", "Detergents_Paper", "Delicassen"]
DATA_PATH = "dataset/raw_wholesale_customers.csv"
OUT_CSV = "outputs/segmented_wholesale_customers.csv"
OUT_ELBOW_PLOT = "outputs/elbow_plot.png"


def checkpoint(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# ---------------------------------------------------------------------
# 1. Load Dataset
# ---------------------------------------------------------------------
checkpoint("STEP 1 — Load Dataset")
df = pd.read_csv(DATA_PATH)
print(f"Shape: {df.shape}")
print("\nHead:")
print(df.head())
print("\nInfo:")
df.info()

# ---------------------------------------------------------------------
# 2. Select Features + IQR Capping
# ---------------------------------------------------------------------
checkpoint("STEP 2 — Select Features + IQR Capping (k=1.5)")
df_clean = df.copy()
K_IQR = 1.5
cap_log = []

for col in FEATURES:
    q1 = df_clean[col].quantile(0.25)
    q3 = df_clean[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - K_IQR * iqr
    upper = q3 + K_IQR * iqr
    n_capped = ((df_clean[col] < lower) | (df_clean[col] > upper)).sum()
    df_clean[col] = df_clean[col].clip(lower=lower, upper=upper)
    cap_log.append((col, round(lower, 1), round(upper, 1), n_capped))

cap_df = pd.DataFrame(cap_log, columns=["Feature", "Lower Bound", "Upper Bound", "Values Capped"])
print(cap_df.to_string(index=False))
print(f"\nTotal values capped: {cap_df['Values Capped'].sum()} "
      f"out of {len(FEATURES) * len(df_clean)} spend cells "
      f"(rows preserved: {len(df_clean)})")

# ---------------------------------------------------------------------
# 3. Scale Features
# ---------------------------------------------------------------------
checkpoint("STEP 3 — Scale Features (StandardScaler)")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_clean[FEATURES])
print("Scaled feature matrix shape:", X_scaled.shape)
print("Per-feature mean after scaling (should be ~0):", np.round(X_scaled.mean(axis=0), 3))
print("Per-feature std after scaling (should be ~1):", np.round(X_scaled.std(axis=0), 3))

# ---------------------------------------------------------------------
# 4. Elbow Method
# ---------------------------------------------------------------------
checkpoint("STEP 4 — Elbow Method (k = 1..10)")
sse = []
for k in range(1, 11):
    km_k = KMeans(n_clusters=k, n_init="auto", random_state=RANDOM_STATE)
    km_k.fit(X_scaled)
    sse.append(km_k.inertia_)
    print(f"k={k:>2} -> SSE (inertia) = {km_k.inertia_:.2f}")

plt.figure(figsize=(7, 4.5))
plt.plot(range(1, 11), sse, marker="o")
plt.xlabel("Number of clusters (k)")
plt.ylabel("SSE (inertia)")
plt.title("Elbow Method — Wholesale Customers")
plt.xticks(range(1, 11))
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(OUT_ELBOW_PLOT, dpi=150)
plt.close()
print(f"\nElbow plot saved to {OUT_ELBOW_PLOT}")

# ---------------------------------------------------------------------
# 5. Train K-Means (Reproduce Lesson, k=5)
# ---------------------------------------------------------------------
checkpoint("STEP 5 — Train K-Means (n_clusters=5)")
kmeans = KMeans(n_clusters=5, n_init="auto", random_state=RANDOM_STATE)
labels_kmeans = kmeans.fit_predict(X_scaled)
df_clean["Cluster"] = labels_kmeans
print("Cluster sizes:")
print(df_clean["Cluster"].value_counts().sort_index())

# ---------------------------------------------------------------------
# 6. Evaluate K-Means
# ---------------------------------------------------------------------
checkpoint("STEP 6 — Evaluate K-Means")
sil_kmeans = silhouette_score(X_scaled, labels_kmeans)
dbi_kmeans = davies_bouldin_score(X_scaled, labels_kmeans)
print(f"Silhouette Score (K-Means):      {sil_kmeans:.4f}")
print(f"Davies-Bouldin Index (K-Means):  {dbi_kmeans:.4f}")

centers_original = scaler.inverse_transform(kmeans.cluster_centers_)
centers_df = pd.DataFrame(centers_original, columns=FEATURES).round(1)
centers_df.insert(0, "Cluster", range(5))
centers_df["ClusterSize"] = df_clean["Cluster"].value_counts().sort_index().values
print("\nCluster centers (original spend units):")
print(centers_df.to_string(index=False))

# ---------------------------------------------------------------------
# 7. Research & Train a Second Clustering Algorithm
# ---------------------------------------------------------------------
checkpoint("STEP 7 — Second Algorithm: Agglomerative (Hierarchical) Clustering")
print(
    "Chosen algorithm: Agglomerative Clustering with Ward linkage.\n"
    "Why it fits: wholesale spend segments are naturally nested (e.g. a broad\n"
    "'high grocery' segment can be split into 'high grocery + high detergents'\n"
    "vs 'high grocery only'). Ward linkage merges clusters by minimizing the\n"
    "increase in within-cluster variance, which pairs naturally with the\n"
    "Euclidean, standardized feature space used for K-Means, so the two\n"
    "methods are directly comparable on this dataset.\n"
    "Reference: scikit-learn User Guide - Hierarchical clustering\n"
    "(https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering)"
)
agglo = AgglomerativeClustering(n_clusters=5, linkage="ward")
labels_agglo = agglo.fit_predict(X_scaled)
df_clean["Cluster_Agglomerative"] = labels_agglo
print("\nCluster sizes (Agglomerative):")
print(pd.Series(labels_agglo).value_counts().sort_index())

# ---------------------------------------------------------------------
# 8. Compare Methods
# ---------------------------------------------------------------------
checkpoint("STEP 8 — Compare Methods")
sil_agglo = silhouette_score(X_scaled, labels_agglo)
dbi_agglo = davies_bouldin_score(X_scaled, labels_agglo)

comparison = pd.DataFrame({
    "Method": ["K-Means", "Agglomerative (Ward)"],
    "Silhouette Score": [round(sil_kmeans, 4), round(sil_agglo, 4)],
    "Davies-Bouldin Index": [round(dbi_kmeans, 4), round(dbi_agglo, 4)],
})
print(comparison.to_string(index=False))

better = "K-Means" if sil_kmeans > sil_agglo else "Agglomerative (Ward)"
print(f"\n=> {better} produced better-separated clusters "
      f"(higher Silhouette Score = more distinct, less overlapping clusters).")

# ---------------------------------------------------------------------
# 9. Sanity Check
# ---------------------------------------------------------------------
checkpoint("STEP 9 — Sanity Check (3 sample clients)")
sample_clients = df_clean.sample(3, random_state=RANDOM_STATE)
cols_to_show = ["Channel", "Region"] + FEATURES + ["Cluster", "Cluster_Agglomerative"]
print(sample_clients[cols_to_show].to_string())

# ---------------------------------------------------------------------
# 10. Save Output
# ---------------------------------------------------------------------
checkpoint("STEP 10 — Save Output")
final_df = df.copy()
final_df["Cluster"] = labels_kmeans
final_df.to_csv(OUT_CSV, index=False)
print(f"Saved K-Means cluster labels to {OUT_CSV}")
print(f"Final shape: {final_df.shape}")

checkpoint("PIPELINE COMPLETE")
