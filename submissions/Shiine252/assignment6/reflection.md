y

# Wholesale Customer Segmentation Analysis Report

---

## 1. Executive Summary: What Was Implemented

This project designed and executed a data-driven customer segmentation pipeline for a wholesale distributor using two distinct machine learning approaches: **K-Means Clustering** and a **Gaussian Mixture Model (GMM)** with a tied covariance structure ($covariance\_type="tied"$).

Both models evaluated clients across six core spending dimensions: `Fresh`, `Milk`, `Grocery`, `Frozen`, `Detergents_Paper`, and `Delicassen`. Prior to modeling, continuous variables were normalized using a `StandardScaler` to prevent larger scaling features (like high-volume fresh goods) from dominating the distance calculations. The optimal cluster size was mathematically determined to be **$k=3$** using the K-Means Elbow Method (evaluating Sum of Squared Errors) and verified against GMM's Bayesian Information Criterion (BIC).

---

## 2. Segment Interpretation (K-Means Results)

Based on the final cluster centers calculated in original units, the wholesale clients naturally split into three actionable business archetypes:

### Cluster 0: Supermarkets & Large Retailers

- **Behavioral Profile:** This segment exhibits exceptionally high spending profiles concentrated in **`Grocery`** (averaging ~16.6k to 17.2k), **`Milk`** (~10.1k), and **`Detergents_Paper`** (~7k to 7.6k). Their purchasing behavior aligns with large-scale grocery stores or retail chains requiring non-perishable inventory and household paper goods.
- **Suggested Business Action:** The distributor should establish **bulk inventory loyalty contracts** or automated cross-selling supply chains for cleaning/paper products bundled directly with primary grocery shipments to secure long-term recurring revenue.

### Cluster 1: Small Independent Businesses, Cafes, & Shops

- **Behavioral Profile:** This cluster represents the high-density baseline of the dataset, characterized by modest, conservative spending across all categories (typically averaging roughly 3.5k on groceries and 2.6k–3.5k on milk products). These are local independent convenience stores or small cafes.
- **Suggested Business Action:** Implement **automated digital marketing triggers** offering tiered dynamic discounts or lowered minimum order thresholds to incentivize higher purchase frequencies without increasing direct sales representative overhead.

### Cluster 2: Restaurants, Hotels, & Catering (Horeca)

- **Behavioral Profile:** This segment prioritizes perishable items above all else, driving massive spending on **`Fresh`** food ingredients (~16.6k to 22.8k) accompanied by significant volume in **`Frozen`** food items.
- **Suggested Business Action:** Launch a dedicated **"Cold Chain Priority Service"** guaranteeing rapid, temperature-controlled delivery slots tailored specifically around restaurant morning prep windows to capture premium delivery margins.

---

## 3. Understanding K-Means

**K-Means** is a distance-based unsupervised learning algorithm designed to partition a dataset into $k$ distinct, non-overlapping groups based on geometric proximity.

The algorithm operates via a simple, iterative **assign-and-update loop**:

1. **Initialization:** The user explicitly defines $k$ (the number of clusters desired). The algorithm then randomly places $k$ initial coordinates in the data space, known as **centroids** (the mathematical centers of the clusters).
2. **Assignment Step:** Every individual data point is evaluated against all centroids. The point is assigned to whichever centroid is closest to it globally (typically measured using standard straight-line Euclidean distance).
3. **Update Step:** Once all points are assigned, the algorithm calculates the mean coordinate of all data points assigned to each cluster. The centroid is then physically moved to this new mean position.
4. **Convergence:** Steps 2 and 3 repeat continuously until the centroids stop shifting positions, meaning the algorithm has minimized the overall variance within each cluster.

---

## 4. my Second Algorithm: Gaussian Mixture Models (GMM)

### Why Chosen & How It Works

A **Gaussian Mixture Model (GMM)** was chosen as the alternative clustering technique. While K-Means assumes rigid, spherical cluster boundaries, GMM is a probabilistic framework that assumes the data points are drawn from a mixture of a finite number of Gaussian (normal) distributions. Instead of assigning a client permanently to one cluster, GMM calculates a "soft assignment"—assigning a probability percentage that a client belongs to each distribution.

- **Advantage:** GMM accounts for correlations between variables. If clients who buy heavy groceries also predictably buy heavy milk volumes, GMM can form stretched, elliptical (oblong) cluster boundaries rather than being forced to draw perfect spheres.
- **Limitation:** It is computationally complex and highly sensitive to initialization, meaning it can easily get trapped in suboptimal mathematical solutions if data density shifts continuously.

### Performance & Metric Comparison

Initially, using a completely flexible model structure ($covariance\_type="full"$), the Silhouette Score dropped significantly to **`0.190`** (compared to K-Means' **`0.340`**) because the cluster distributions stretched too wide and overlapped heavily.

However, by tuning the model to a **`"tied"` covariance structure**—forcing all clusters to share the same overall smooth geometric shape—the GMM performance improved dramatically, achieving a Silhouette Score of **`0.294`** and a Davies–Bouldin index of **`1.337`**. This optimization successfully created compact, cleanly isolated boundaries while maintaining probabilistic flexibility.

---

## 5. Strategic Recommendations & Findings

For this specific wholesale segmentation task, **the Gaussian Mixture Model (GMM) with a tied covariance structure is highly recommended** over K-Means.

While K-Means boasts a slightly higher geometric Silhouette Score, it achieves this by aggressively carving strict boundaries right between complex customer profiles. Real-world wholesale operations rarely adhere to binary splits. Many businesses are hybrid operations—such as a small grocery store that also operates an in-house fresh espresso café.

GMM excels here because it provides **soft clustering probabilities**. Instead of forcing a hybrid buyer into a single category, GMM reveals the exact nuance (e.g., _70% Retailer / 30% Horeca_). This extra depth enables the marketing and supply chain teams to build far more personalized, realistic customer profiles and deploy highly sophisticated targeted promotions that K-Means' rigid boundaries naturally strip away.
