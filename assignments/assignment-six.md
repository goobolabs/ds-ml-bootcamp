# Assignment Six: Clustering — Theory and Practice

**Due:** Thursday, July 9, 2026 — 12:00 PM (Africa/Mogadishu / EAT)

**Goal:** Demonstrate understanding of clustering concepts in Machine Learning. Reproduce the **Lesson 6** wholesale segmentation script in a Jupyter notebook, then research and implement **one additional clustering algorithm** — for a total of two methods (K-Means from class, plus your chosen algorithm) on the wholesale customers dataset.

---

## Part A — Theory

Write your answers in English using a clear academic style (headings, paragraphs, and references). Length: 2–3 pages. Use your own words — no copy-paste. You may use AI for clarification, but must understand and verify everything you write.

1. **Introduction to Unsupervised Learning and Clustering**

   - What is unsupervised learning in Machine Learning?
   - How is it different from regression and classification?
   - Give one real-life example of clustering and one of supervised learning.

2. **Clustering Algorithms**

   - Describe and compare the following:
     - K-Means
     - Hierarchical Clustering
     - DBSCAN
   - For each type, explain: how it works (basic idea), one real-world use case, and its main advantages and limitations.

3. **Clustering Metrics**

   - Define and explain what each metric measures:
     - Elbow Method (SSE)
     - Silhouette Score
     - Davies–Bouldin Index
   - Include a comparison table showing their differences (what each measures, what a good value looks like).

4. **Choosing k and Interpreting Segments**

   - How do you choose the number of clusters for K-Means?
   - In the wholesale distributor project, what does it mean when a cluster has high Fresh + Milk spend vs high Grocery + Detergents_Paper spend?
   - Why do we exclude Channel and Region from the clustering features?

5. **Real-World Case Study**

   - Research a real-world project or study that used clustering for customer or market segmentation in any field such as business, retail, or marketing.
   - Summarize: the goal, the data used, the clustering method applied, and the key results or insights.

---

## Part B — Practical: Wholesale Customer Segmentation

**Dataset:** `dataset/raw_wholesale_customers.csv`

Create a Jupyter Notebook named `customer_segmentation.ipynb` and implement the following steps. Include a brief print checkpoint after each major step.

> Follow the **Lesson 6** coding session and [`code/customer-segmentation.py`](../code/customer-segmentation.py). Implement the same pipeline in your own notebook — typed by you, with output cells visible.

1. **Load Dataset**

   - Load `raw_wholesale_customers.csv`.
   - Show head and info.

2. **Select Features + IQR Cap**

   - Use only these six columns for clustering: `Fresh`, `Milk`, `Grocery`, `Frozen`, `Detergents_Paper`, `Delicassen`.
   - Do **not** use `Channel` or `Region` as features.
   - Apply IQR capping (`k=1.5`) to each spend column — clip, do not delete rows.

3. **Scale Features**

   - Apply `StandardScaler` to the six spend columns before clustering.

4. **Elbow Method**

   - Run K-Means for k = 1 to 10 on the scaled features.
   - Print SSE (inertia) for each k.
   - Optional: plot k vs SSE in the notebook.

5. **Train K-Means (Reproduce Lesson)**

   - Fit `KMeans(n_clusters=5, n_init="auto", random_state=42)` on the scaled features.
   - Add a `Cluster` column to the dataframe.

6. **Evaluate K-Means**

   - Print Silhouette Score and Davies–Bouldin Index.
   - Print cluster centers in **original spend units** (use `inverse_transform` on the scaler).

7. **Research & Train a Second Clustering Algorithm**

   - The lesson covers **K-Means** only. Your assignment adds **one additional clustering algorithm** you research and implement yourself.
   - Choose an algorithm you did **not** use in the lesson script (e.g., Agglomerative/Hierarchical Clustering, DBSCAN, or GMM).
   - In a short markdown cell, explain:
     - Which algorithm you chose and why it fits wholesale customer segmentation.
     - One source you used for your research (documentation, tutorial, or article).
   - Train your model on the same scaled six-column features with sensible defaults and `random_state=42` where applicable.

8. **Compare Methods**

   - Print Silhouette Score for **both** K-Means and your second algorithm.
   - Briefly note which method produced better-separated clusters.

9. **Sanity Check**

   - Pick three clients from the dataset and show their spend values, Channel, Region, and cluster label from **both** methods.

10. **Save Output**

    - Save the dataframe with K-Means cluster labels to `segmented_wholesale_customers.csv`.

> **Lesson 6** walks through one script end-to-end. Your assignment reproduces it in a notebook and adds **one second clustering algorithm** you research yourself. Submit your notebook with all output cells visible.

---

## Part C — Reflection Paper

Write a short paper (1–2 pages, Markdown or PDF) answering the following:

1. **What did you implemented?**

   - Briefly describe how you segmented wholesale clients using K-Means and your additional clustering algorithm on the six spending columns.

2. **Segment Interpretation**

   - Describe 2–3 clusters from your K-Means results in plain language (what do they buy most?).
   - For each cluster you describe, suggest **one business action** the distributor could take.

3. **Understanding K-Means**

   - In your own words: what is K-Means and how does it work (centroids, k, assign-and-update loop)?

4. **Your Second Algorithm**

   - Which additional algorithm did you choose, and why?
   - Summarize what you learned from your research (how it works, one advantage, one limitation).
   - How did its Silhouette Score compare to K-Means?

5. **Your Findings**

   - In 1–2 paragraphs, explain which clustering approach you would recommend for this wholesale segmentation task and why.

---

## Deliverables

Submit these three files:

- `paper.md` or `paper.pdf` — Part A theory answers.
- `customer_segmentation.ipynb` — Part B notebook with all code and output cells visible.
- `reflection_paper.md` or `reflection_paper.pdf` — Part C reflection.

Also produce `segmented_wholesale_customers.csv` (saved from Part B).

---
