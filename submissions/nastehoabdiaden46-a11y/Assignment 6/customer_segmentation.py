# Assignment Six - Part B
# Wholesale Customer Segmentation

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score, davies_bouldin_score


# 1. Load Dataset

df = pd.read_csv("dataset/raw_wholesale_customers.csv")

print("Dataset loaded successfully!")
print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Information:")
df.info()


# 2. Select Six Features for Clustering
# Channel and Region are excluded

features = [
    "Fresh",
    "Milk",
    "Grocery",
    "Frozen",
    "Detergents_Paper",
    "Delicassen"
]

X = df[features].copy()

print("\nSelected Features:")
print(features)


# 3. Apply IQR Capping (k=1.5)

def iqr_capping(data, columns, k=1.5):
    data = data.copy()

    for col in columns:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)

        IQR = Q3 - Q1

        lower = Q1 - k * IQR
        upper = Q3 + k * IQR

        data[col] = data[col].clip(lower, upper)

    return data


X_capped = iqr_capping(X, features)

print("\nIQR Capping completed!")


# 4. Feature Scaling

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X_capped)

print("\nStandard Scaling completed!")


# 5. Elbow Method (K = 1 to 10)

sse = []

print("\nSSE Values:")

for k in range(1, 11):

    model = KMeans(
        n_clusters=k,
        n_init="auto",
        random_state=42
    )

    model.fit(X_scaled)

    sse.append(model.inertia_)

    print(f"K={k}: SSE={model.inertia_}")


# Elbow Plot

plt.figure(figsize=(8,5))

plt.plot(
    range(1,11),
    sse,
    marker="o"
)

plt.xlabel("Number of Clusters (k)")
plt.ylabel("SSE")
plt.title("Elbow Method")

plt.show()


# 6. Train K-Means Model

kmeans = KMeans(
    n_clusters=5,
    n_init="auto",
    random_state=42
)

kmeans_labels = kmeans.fit_predict(X_scaled)

df["KMeans_Cluster"] = kmeans_labels

print("\nK-Means clustering completed!")


# 7. Evaluate K-Means

kmeans_silhouette = silhouette_score(
    X_scaled,
    kmeans_labels
)

kmeans_db = davies_bouldin_score(
    X_scaled,
    kmeans_labels
)

print("\nK-Means Evaluation")
print("Silhouette Score:", kmeans_silhouette)
print("Davies-Bouldin Index:", kmeans_db)


# 8. Cluster Centers in Original Spend Units

centers = scaler.inverse_transform(
    kmeans.cluster_centers_
)

cluster_centers = pd.DataFrame(
    centers,
    columns=features
)

print("\nK-Means Cluster Centers:")
print(cluster_centers)


# 9. Second Algorithm - Hierarchical Clustering

hierarchical = AgglomerativeClustering(
    n_clusters=5
)

hierarchical_labels = hierarchical.fit_predict(
    X_scaled
)

df["Hierarchical_Cluster"] = hierarchical_labels

print("\nHierarchical Clustering completed!")


# 10. Evaluate Hierarchical Model

hierarchical_silhouette = silhouette_score(
    X_scaled,
    hierarchical_labels
)

hierarchical_db = davies_bouldin_score(
    X_scaled,
    hierarchical_labels
)

print("\nHierarchical Evaluation")
print("Silhouette Score:", hierarchical_silhouette)
print("Davies-Bouldin Index:", hierarchical_db)


# 11. Compare Both Methods

comparison = pd.DataFrame({
    "Method": [
        "K-Means",
        "Hierarchical"
    ],
    "Silhouette Score": [
        kmeans_silhouette,
        hierarchical_silhouette
    ],
    "Davies-Bouldin Index": [
        kmeans_db,
        hierarchical_db
    ]
})

print("\nModel Comparison:")
print(comparison)


# 12. Sanity Check - Three Clients

print("\nThree Sample Clients:")

print(
    df.sample(
        3,
        random_state=42
    )[
        [
            "Fresh",
            "Milk",
            "Grocery",
            "Frozen",
            "Detergents_Paper",
            "Delicassen",
            "Channel",
            "Region",
            "KMeans_Cluster",
            "Hierarchical_Cluster"
        ]
    ]
)


# 13. Save Final Output

df.to_csv(
    "segmented_wholesale_customers.csv",
    index=False
)

print("\nFile saved: segmented_wholesale_customers.csv")