# ===============================
# Wholesale Customer Segmentation
# - IQR cap + K-Means + clustering metrics
# - Clusters on 6 spend columns only (Channel/Region excluded)
# ===============================

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import silhouette_score, davies_bouldin_score

CSV_PATH = "dataset/raw_wholesale_customers.csv"
OUT_PATH = "dataset/segmented_wholesale_customers.csv"
RANDOM_STATE = 42


# --------------------------------
# 1) Load dataset
# --------------------------------
df = pd.read_csv(CSV_PATH)
print("\n=== INITIAL SNAPSHOT ===")
# print(df.head())

# --------------------------------
# 2) Select features + IQR cap
# L3: clip extreme spend values before scaling — same idea as house/loan pipelines
# --------------------------------
FEATURES = ["Fresh", "Milk", "Grocery",
            "Frozen", "Detergents_Paper", "Delicassen"]
X = df[FEATURES].copy()
# print("\n=== FEATURE SNAPSHOT ===")
# print(X.describe())


def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper


low_fresh,  high_fresh = iqr_fun(X["Fresh"])
low_milk,    high_milk = iqr_fun(X["Milk"])
low_grocery, high_grocery = iqr_fun(X["Grocery"])
low_frozen,  high_frozen = iqr_fun(X["Frozen"])
low_det,     high_det = iqr_fun(X["Detergents_Paper"])
low_deli,    high_deli = iqr_fun(X["Delicassen"])

X["Fresh"] = X["Fresh"].clip(lower=low_fresh,  upper=high_fresh)
X["Milk"] = X["Milk"].clip(lower=low_milk,    upper=high_milk)
X["Grocery"] = X["Grocery"].clip(lower=low_grocery, upper=high_grocery)
X["Frozen"] = X["Frozen"].clip(lower=low_frozen,  upper=high_frozen)
X["Detergents_Paper"] = X["Detergents_Paper"].clip(
    lower=low_det, upper=high_det)
X["Delicassen"] = X["Delicassen"].clip(lower=low_deli, upper=high_deli)

df[FEATURES] = X

# print("\n=== IQR CAP SUMMARY FOR EACH FEATURE ===")
# print(
#     f"Fresh             low={low_fresh:.2f}  high={high_fresh:.2f}  |  after cap min={X['Fresh'].min():.2f}  max={X['Fresh'].max():.2f}")
# print(
#     f"Milk              low={low_milk:.2f}  high={high_milk:.2f}  |  after cap min={X['Milk'].min():.2f}  max={X['Milk'].max():.2f}")
# print(
#     f"Grocery           low={low_grocery:.2f}  high={high_grocery:.2f}  |  after cap min={X['Grocery'].min():.2f}  max={X['Grocery'].max():.2f}")
# print(
#     f"Frozen            low={low_frozen:.2f}  high={high_frozen:.2f}  |  after cap min={X['Frozen'].min():.2f}  max={X['Frozen'].max():.2f}")
# print(
#     f"Detergents_Paper  low={low_det:.2f}  high={high_det:.2f}  |  after cap min={X['Detergents_Paper'].min():.2f}  max={X['Detergents_Paper'].max():.2f}")
# print(
#     f"Delicassen        low={low_deli:.2f}  high={high_deli:.2f}  |  after cap min={X['Delicassen'].min():.2f}  max={X['Delicassen'].max():.2f}")

# print("\n=== FEATURES HEAD (after IQR cap) ===")
# print(X.head())

# --------------------------------
# 3) Scale features
# --------------------------------
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
# print("\nScaled shape:", X_scaled.shape)
# print("\n=== AFTER SCALING SNAPSHOT ===")
# print(X_scaled)


# --------------------------------
# 4) Elbow method (print SSE)
# --------------------------------
print("\n=== ELBOW METHOD (SSE per k) ===")
for k in range(1, 11):
    km = KMeans(n_clusters=k, n_init="auto", random_state=RANDOM_STATE)
    km.fit(X_scaled)
    print(f"k={k} → SSE={km.inertia_:.2f}")

# --------------------------------
# 5) Fit K-Means with chosen k
# --------------------------------
K = 2
kmeans = KMeans(n_clusters=K, n_init="auto", random_state=RANDOM_STATE)
labels = kmeans.fit_predict(X_scaled)

df["Cluster"] = labels.astype(int)
print("\n=== SAMPLE WITH CLUSTERS ===")
print(df.head())   


# --------------------------------
# 6) Evaluate clustering
# --------------------------------
sil = silhouette_score(X_scaled, labels)
dbi = davies_bouldin_score(X_scaled, labels)
print("\n=== METRICS ===")
print(f"Number of clusters: {K}")
print(f"Silhouette Score : {sil:.3f} (closer to +1 is better)")
print(f"Davies–Bouldin   : {dbi:.3f} (lower is better)")

# --------------------------------
# 7) Cluster centers (back to original units)
# --------------------------------
centers_scaled = kmeans.cluster_centers_
centers_original = scaler.inverse_transform(centers_scaled)

centers_df = pd.DataFrame(centers_original, columns=FEATURES)
centers_df.index.name = "Cluster"

print("\n=== CLUSTER CENTERS (Original Units) ===")
print(centers_df.round(2))

# --------------------------------
# 8) Sanity checks (3 clients)
# --------------------------------
sample_idx = [0, 1, 2]
sanity = df.loc[sample_idx, ["Channel", "Region"] + FEATURES + ["Cluster"]]
print("\n=== SANITY CHECK (3 Clients) ===")
print(sanity)

# --------------------------------
# 9) Save labeled dataset
# --------------------------------
df.to_csv(OUT_PATH, index=False)
print(f"\nSaved clustered dataset → {OUT_PATH}")

