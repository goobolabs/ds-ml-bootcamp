# Lesson 6 – Clustering

> In **Lesson 5**, we used labeled data to predict loan approval. Now we remove the labels entirely. **Clustering** finds groups in data on its own. Our project: **wholesale customer segmentation**.

---

## What You'll Learn

By the end of this lesson, students will be able to:

- Explain what **Unsupervised Learning** is and when to use it instead of supervised learning.
- Describe **K-Means** and how it groups data around cluster centroids.
- Choose *k* with the **Elbow Method** and evaluate results with **Silhouette Score** and **Davies–Bouldin Index**.
- Segment wholesale clients by **spending behavior** using a single end-to-end Python script.

---

## What is Clustering?

Instead of predicting a label we already know, we **discover groups** in the data.

- **Clustering** = grouping rows into clusters so that items in the same cluster are **more similar** to each other than to items in other clusters.
- There is **no target column** — the algorithm finds structure on its own.

### Our Project: Wholesale Customer Segmentation

A food **wholesale distributor** sells in bulk to **440 business clients** (hotels, restaurants, shops). Each row records **annual spend** on six product lines:

- Fresh, Milk, Grocery, Frozen, Detergents_Paper, Delicatessen

The business question: *Which types of buyers do we have, based on what they purchase?*

> We cluster on **spending columns only**. `Channel` and `Region` stay in the dataset for reference but are **not** used in K-Means.

### Real-World Examples

- 🏪 **Wholesale Segmentation** – group B2B clients by product mix (our project).
- 🛒 **Market Segmentation** – group retail customers by purchase behavior.
- 📱 **App Users** – group users into active vs casual usage clusters.

### Contrast with Supervised Learning

| | Regression / Classification (L4–L5) | Clustering (L6) |
| --- | --- | --- |
| **Labels** | Yes — Price, Approved, etc. | No — groups are discovered |
| **Goal** | Predict a known answer | Find hidden structure |
| **Metrics** | MAE, R², Accuracy, F1 | Elbow, Silhouette, Davies–Bouldin |
| **Example** | Predict loan approval | Group clients by spend pattern |

> Supervised = *with answers*. Unsupervised = *find the patterns yourself*.

---

## K-Means Clustering

- **Idea:** Partition data into *k* clusters around **centroids** (cluster centers).
- **Steps:**

  1. Choose *k* (number of clusters).
  2. Place initial centroids.
  3. Assign each point to the nearest centroid.
  4. Move centroids to the mean of their assigned points.
  5. Repeat until stable.

- **Best for:** Spherical clusters, numeric features, medium-to-large datasets.
- **Limitation:** Must choose *k* beforehand; sensitive to outliers and scale.

> Our coding session uses **K-Means** on six scaled spending columns. Other clustering methods (Hierarchical, DBSCAN, and more) are covered in **Assignment 6** — you will research and implement one additional algorithm there.

---

## Clustering Metrics

Unlike classification, there is no “correct” label to compare against. We use **clustering metrics** instead.

### Elbow Method (for K-Means)

- **Goal:** Choose a good *k*.
- Run K-Means for k = 1, 2, 3, … and record **SSE** (sum of squared distances to centroids).
- Plot or print k vs SSE; pick the **elbow** where improvement slows down.

Example:

- k=3 → SSE=2500
- k=4 → SSE=1800
- k=5 → SSE=1650
- k=6 → SSE=1600

At **k=5**, gains shrink — a reasonable choice for this dataset.

### Silhouette Score

- **Range:** -1 to +1
- **+1** → well-separated clusters; **0** → overlap; **-1** → poor assignments
- **Use when:** You want one number for overall cluster quality.

### Davies–Bouldin Index

- Measures average similarity **between** clusters.
- **Lower is better.**

### Summary Table

| Metric | What it Measures | Good Value Means |
| --- | --- | --- |
| Elbow (SSE) | Compactness vs k | Clear bend in SSE curve |
| Silhouette | Separation + cohesion | Closer to +1 |
| Davies–Bouldin | Between-cluster similarity | Lower |

---

## Our Dataset

**Source:** UCI Wholesale Customers ([Kaggle mirror](https://www.kaggle.com/datasets/binovi/wholesale-customers-data-set))

| Column | Meaning | Used in K-Means? |
| --- | --- | --- |
| Channel | 1=Horeca, 2=Retail | No |
| Region | 1=Lisbon, 2=Oporto, 3=Other | No |
| Fresh … Delicassen | Annual spend per category | **Yes** (all six) |

---

## Coding Session

Theory done — now we go hands-on. Open the script and run it:

[`code/customer-segmentation.py`](../code/customer-segmentation.py)

```bash
python code/customer-segmentation.py
```

---

## Summary

- **Clustering:** Unsupervised learning — no labels; the algorithm discovers groups. Our project segments **wholesale clients by spending behavior**.
- **K-Means:** Partitions data into *k* clusters around centroids — the method we use in class for this project.
- **Metrics:** Elbow (choose *k*), Silhouette (separation), Davies–Bouldin (between-cluster similarity).
- **Features:** Six annual spend columns only; **Channel** and **Region** excluded from clustering.
- **Pipeline:** IQR cap → StandardScaler → Elbow → K-Means → Silhouette + Davies–Bouldin → interpret cluster centers.
- **Coding session:** Run [`customer-segmentation.py`](../code/customer-segmentation.py).
- **Assignment 6:** Theory on other clustering algorithms + notebook reproduction + one additional method of your choice.

---

*End of Lesson 6*
