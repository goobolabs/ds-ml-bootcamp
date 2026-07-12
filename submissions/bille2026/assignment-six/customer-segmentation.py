# --------------------------------
# Imports
# --------------------------------
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score, davies_bouldin_score


# --------------------------------
# 1) Load dataset
# --------------------------------
CSV_PATH = "dataset/raw_wholesale_customers.csv"

df = pd.read_csv(CSV_PATH)

print("\n=== INITIAL SNAPSHOT ===")
print(df.head())

print("\n=== DATA INFO ===")
df.info()


# --------------------------------
# 2) Select Features + IQR Capping
# --------------------------------
FEATURES = [
    "Fresh",
    "Milk",
    "Grocery",
    "Frozen",
    "Detergents_Paper",
    "Delicassen"
]

X = df[FEATURES].copy()


def iqr_fun(series, k=1.5):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)

    iqr = q3 - q1

    lower = q1 - k * iqr
    upper = q3 + k * iqr

    return lower, upper


# Apply IQR cap
for col in FEATURES:
    low, high = iqr_fun(X[col])
    X[col] = X[col].clip(
        lower=low,
        upper=high
    )


print("\n=== FEATURES AFTER IQR CAP ===")
print(X.head())


# --------------------------------
# 3) Scale Features
# --------------------------------
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("\nScaled shape:", X_scaled.shape)



# --------------------------------
# 4) Elbow Method (SSE)
# --------------------------------
print("\n=== ELBOW METHOD (SSE per k) ===")

sse = []

for k in range(1, 11):

    km = KMeans(
        n_clusters=k,
        n_init="auto",
        random_state=42
    )

    km.fit(X_scaled)

    sse.append(km.inertia_)

    print(
        f"k={k} → SSE={km.inertia_:.2f}"
    )


#  graph
# import matplotlib.pyplot as plt
#
# plt.plot(range(1,11), sse, marker="o")
# plt.xlabel("Number of Clusters (K)")
# plt.ylabel("SSE")
# plt.title("Elbow Method")
# plt.show()



# --------------------------------
# 5) Train K-Means (k=5)
# --------------------------------

kmeans = KMeans(
    n_clusters=5,
    n_init="auto",
    random_state=42
)

kmeans_labels = kmeans.fit_predict(X_scaled)


df["KMeans_Cluster"] = kmeans_labels.astype(int)


print("\n=== SAMPLE WITH KMEANS CLUSTERS ===")
print(df.head())



# --------------------------------
# 6) Evaluate K-Means
# --------------------------------

sil_kmeans = silhouette_score(
    X_scaled,
    kmeans_labels
)

dbi_kmeans = davies_bouldin_score(
    X_scaled,
    kmeans_labels
)


print("\n=== K-MEANS METRICS ===")

print(
    f"Silhouette Score : {sil_kmeans:.3f}"
)

print(
    f"Davies-Bouldin   : {dbi_kmeans:.3f}"
)



# --------------------------------
# 7) Cluster Centers
#    Back to Original Units
# --------------------------------

centers_scaled = kmeans.cluster_centers_

centers_original = scaler.inverse_transform(
    centers_scaled
)


centers_df = pd.DataFrame(
    centers_original,
    columns=FEATURES
)


centers_df.index.name = "Cluster"


print("\n=== CLUSTER CENTERS ===")
print(centers_df.round(2))



# --------------------------------
# 8) Second Algorithm
#    Hierarchical Clustering
# --------------------------------

hier = AgglomerativeClustering(
    n_clusters=5,
    linkage="ward"
)


hier_labels = hier.fit_predict(
    X_scaled
)


df["Hierarchical_Cluster"] = (
    hier_labels.astype(int)
)



# --------------------------------
# 9) Compare Methods
# --------------------------------

sil_hier = silhouette_score(
    X_scaled,
    hier_labels
)


print("\n=== MODEL COMPARISON ===")

print(
    f"K-Means Silhouette      : {sil_kmeans:.3f}"
)

print(
    f"Hierarchical Silhouette : {sil_hier:.3f}"
)


if sil_kmeans > sil_hier:
    print(
        "K-Means produced better-separated clusters."
    )
else:
    print(
        "Hierarchical produced better-separated clusters."
    )



# --------------------------------
# 10) Sanity Check
# --------------------------------

sample_idx = [0, 1, 2]


sanity = df.loc[
    sample_idx,
    [
        "Channel",
        "Region"
    ]
    + FEATURES
    + [
        "KMeans_Cluster",
        "Hierarchical_Cluster"
    ]
]


print("\n=== SANITY CHECK ===")
print(sanity)



# --------------------------------
# 11) Save Output
# --------------------------------

OUT_PATH = "dataset/segmented_wholesale_customers.csv"


df.to_csv(
    OUT_PATH,
    index=False
)


print(
    f"\nSaved file: {OUT_PATH}"
)