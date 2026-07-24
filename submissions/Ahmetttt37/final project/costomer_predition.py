import pandas as pd
import os
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


# Load Dataset

CSV_PATH = r"C:\Users\Ali Black\Desktop\bootcamp1\ds-ml-bootcamp\submissions\Ahmetttt37\final project\marketing_campaign.csv"

df = pd.read_csv(CSV_PATH,sep="\t")


# Select Spending Features

spending_features = ["MntWines", "MntFruits", "MntMeatProducts", "MntFishProducts", "MntSweetProducts",
 "MntGoldProds"
]

X = df[spending_features]

# Missing Values

X = X.fillna(X.median())

# Scaling

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)



for k in range(2, 11):

    kmeans = KMeans(n_clusters=k, random_state=42, n_init="auto")
    kmeans.fit(X_scaled)
    print(f"K={k}, Inertia={kmeans.inertia_:.2f}")

# Final K-Means Model

kmeans = KMeans(n_clusters=4, random_state=42, n_init="auto")
clusters = kmeans.fit_predict(X_scaled)
df["Cluster"] = clusters

# Cluster Summary

cluster_summary = df.groupby("Cluster")[spending_features].mean()

print("\nCluster Summary:")
print(cluster_summary)

# Cluster Size

print("\nNumber of Customers per Cluster:")

print(
    df["Cluster"].value_counts()
)



# ===============================
# Save Model
# ===============================

os.makedirs("models",exist_ok=True)

joblib.dump(kmeans, "models/kmeans.pkl")

joblib.dump(scaler, "models/cluster_scaler.pkl")

df.to_csv("models/customer_segments.csv", index=False)


print(
    "\nCustomer Segmentation Completed Successfully!"
)