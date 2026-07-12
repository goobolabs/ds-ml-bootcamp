# Wholesale Customer Segmentation Analysis
**Course Assignment 6: Machine Learning Report**  
**Author:** Data Science Student  
**Date:** July 2026

---

## 1. Executive Summary & Implementation
In this project, I implemented a customer segmentation pipeline to analyze and categorize a wholesale distributor's clients based on their annual spending across six core product categories: `Fresh`, `Milk`, `Grocery`, `Frozen`, `Detergents_Paper`, and `Delicassen`.

### The Implementation Workflow
1. **Data Preprocessing & Outlier Mitigation:** Initial exploratory data analysis showed significant positive skewness across all spending dimensions. To handle extreme values without discarding critical customer data, I designed a custom Interquartile Range (IQR) bounding function (`calculate_iqr_bounds`) using a standard 1.5×IQR multiplier. Spending values exceeding these calculated fences were clipped to their respective lower and upper thresholds.
2. **Feature Normalization:** Because clustering algorithms rely heavily on distance metrics, and spending amounts across categories varied drastically in scale, I utilized the `StandardScaler` to transform the clipped dataset into standard normal distributions (mean = 0, variance = 1).
3. **Primary Model (K-Means Evaluation):** I conducted an elbow analysis scanning parameter values $k \in [1, 10]$ to observe the change in Sum of Squared Errors (SSE/Inertia). A finalized $K=5$ arrangement was chosen to group clients into distinct behavior segments.
4. **Secondary Model (Hierarchical Agglomerative Clustering):** For a rigorous comparative baseline, I implemented Hierarchical Agglomerative Clustering using a Ward linkage criteria on the same preprocessed dataset.
5. **Quality Assessment:** Models were assessed and compared using both the Silhouette Coefficient and the Davies-Bouldin Index.

---

## 2. K-Means Segment Interpretation & Strategic Actions

Based on the original metric unit cluster centers extracted from the model, here is a plain-language interpretation of three distinct client profiles identified by the K-Means algorithm, alongside targeted operational recommendations:

### Cluster A: The "High-Volume Grocery & Retailers"
* **Plain Language Profile:** These clients exhibit massive annual outlays centered predominantly on `Grocery`, `Milk`, and `Detergents_Paper` categories, while displaying comparatively low interest in bulk `Frozen` items. They resemble independent supermarkets, large convenience stores, or regional grocers.
* **Recommended Business Action:** The distributor should prioritize custom loyalty programs, volume-discount contract lock-ins, and supply chain optimizations for non-perishable goods. Cross-selling paper products alongside grocery shipments can maximize margin captured per delivery run.

### Cluster B: The "Fresh Food & Hospitality Outlets"
* **Plain Language Profile:** This segment is characterized by exceptionally high expenditures on `Fresh` produce and `Frozen` goods, with minimal investment in `Detergents_Paper`. These behavior indicators match full-service restaurants, catering companies, and hospitality/hotel kitchens.
* **Recommended Business Action:** Introduce automated regular delivery cadences optimized for highly perishable goods. Offering specialized seasonal promotions or volume packages combining fresh proteins with frozen foundational ingredients would highly appeal to this specific target group.

### Cluster C: The "Boutique Cafés & Delis"
* **Plain Language Profile:** This cluster represents a smaller, more specialized niche with balanced, moderate spending overall, but a disproportionately high emphasis on `Delicassen`, `Milk`, and premium `Grocery` items. These are likely high-end local coffee shops, specialty bakeries, or specialty delis.
* **Recommended Business Action:** Deploy targeted marketing materials highlighting artisanal items, premium dairy suppliers, or organic imports. Since their order sizes are smaller but frequent, optimizing a dynamic, user-friendly digital ordering platform with lower minimum order thresholds can enhance retention.

---

## 3. Core Conceptual Foundations

### Understanding K-Means
**K-Means** is a popular partition-based unsupervised machine learning algorithm designed to divide an unlabeled dataset into $K$ separate, non-overlapping clusters. The algorithm operates via a clean, repetitive optimization loop structured as follows:

1. **Initialization:** The user explicitly defines the parameter $k$, representing the desired number of customer groups. The algorithm selects $k$ initial points in the multi-dimensional feature space to act as the starting cluster centers (known as **centroids**).
2. **The Assign-and-Update Loop:**
   * **Assign Step:** The algorithm measures the geometric distance (usually Euclidean distance) between every individual data point and all $k$ centroids. Each data point is assigned to its closest neighboring centroid.
   * **Update Step:** Once all allocations are frozen, the algorithm recalculates the exact center of each group by computing the mathematical mean of all coordinate points assigned to that specific cluster. These newly computed means become the updated centroids.
3. **Convergence:** This loop runs iteratively until the centroids stop shifting positions or the maximum number of allowed iterations is reached.

### Your Second Algorithm: Hierarchical Agglomerative Clustering
For the secondary approach, I chose **Hierarchical Agglomerative Clustering (HAC)**. 

* **How it Works:** Unlike the top-down nature of K-Means, HAC is a bottom-up clustering technique. It starts by treating every individual customer profile as its own independent single-point cluster. At each sequential step, the algorithm identifies the two closest clusters based on a specified metric (such as Ward's linkage, which minimizes variance inside the combined groups) and merges them together. This process builds a tree-like hierarchy called a dendrogram until all observations are joined into one single master cluster.
* **Advantage:** HAC does not require the user to pre-specify the number of clusters $k$ before running. Analysts can build the full tree structure and visually slice it at the optimal height later. Furthermore, it easily uncovers nested structural relationships within data.
* **Limitation:** It is computationally expensive. It has a time complexity of $\mathcal{O}(N^3)$ or $\mathcal{O}(N^2 \log N)$, making it slow and memory-intensive when processing large enterprise data pools compared to K-Means.
* **Metrics Comparison:** 
  * **K-Means Silhouette Score:** `0.283`
  * **Agglomerative Clustering Silhouette Score:** `0.254`  
  * *Observation:* K-Means yielded a slightly tighter, more distinct boundary definition across the customer segments compared to the hierarchical approach.

---

## 4. Analytical Findings & Final Recommendations

After comprehensive validation, **I strongly recommend the K-Means clustering approach** for this specific wholesale client segmentation initiative. 

From a mathematical standpoint, K-Means achieved a superior Silhouette Score (`0.283` vs. `0.254`), demonstrating that its cluster hyper-spheres exhibit cleaner separation boundaries and tighter internal cohesion. Agglomerative clustering struggled slightly to separate overlapping boundaries because it can become overly sensitive to local density patterns when dealing with highly correlated spending data (like grocery items and paper goods).

From a practical business engineering perspective, K-Means is vastly more scalable. While the current sample size is relatively small, wholesale client populations expand over time as new accounts open. K-Means handles millions of rows with minimal resource consumption, allowing the distributor to rerun the pipeline on a nightly schedule. The resulting segments are highly operational, stable, and map directly onto clear-cut marketing actions, making K-Means the ideal choice for driving data-driven inventory and sales strategies.
