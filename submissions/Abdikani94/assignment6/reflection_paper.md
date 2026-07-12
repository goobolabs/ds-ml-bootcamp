# Reflection Paper — Assignment Six

## 1. What did I implement?

I segmented the wholesale customers using their spending on six categories: Fresh, Milk, Grocery, Frozen, Detergents_Paper, and Delicassen. I capped outliers with IQR clipping, scaled the values with StandardScaler, then ran K-Means with k=5 (same setup as the lesson). After that I also ran Agglomerative Clustering with the same k=5 on the same scaled features, and compared the two using Silhouette Score and Davies-Bouldin Index.

## 2. Segment Interpretation

Looking at the K-Means cluster centers in original spend units:

- **Cluster 2** has the highest spend across almost everything (Fresh ~17.4k, Milk ~13.8k, Grocery ~17.5k, Detergents_Paper ~5.4k). These are the big-volume clients. Business action: assign them a dedicated account manager and offer volume discounts to keep them loyal, since losing one of these customers would hurt revenue a lot.

- **Cluster 3** has very high Fresh (~22.3k) and Frozen (~5.8k) but low Grocery and Detergents_Paper. This looks like restaurant/hotel type buyers who need fresh and frozen food daily but don't stock cleaning or packaged goods. Business action: offer faster/more frequent fresh delivery schedules to this group instead of bulk discounts, since their need is freshness, not volume.

- **Cluster 4** has low Fresh (~4.9k) but high Grocery (~18.3k) and Detergents_Paper (~7.8k). This looks like retail/shop type buyers stocking shelf-stable goods. Business action: push bulk packaging deals and loyalty pricing on grocery and cleaning products, since that's clearly where their budget goes.

## 3. Understanding K-Means

K-Means is a way to group data into k clusters based on distance. You pick a number k, and the algorithm starts by placing k centroids somewhere in the data. Then it repeats two steps: first, assign every point to whichever centroid is closest to it, and second, move each centroid to the average position of all the points now assigned to it. It keeps repeating assign-and-update until the centroids barely move anymore. The end result is k groups where points inside a group are close to each other and far from points in other groups. It's simple and fast, but you need to decide k yourself, and it assumes clusters are roughly round and similar in size.

## 4. My Second Algorithm

I chose Agglomerative (Hierarchical) Clustering. I picked it because it doesn't assume clusters are round like K-Means does, and it's a common alternative that's easy to compare directly since I could use the same k=5.

From my research: it starts by treating every single data point as its own cluster, then repeatedly merges the two closest clusters together, one merge at a time, until you're left with the number of clusters you asked for. One advantage is it doesn't force clusters into round shapes and you can inspect the dendrogram to reconsider the number of clusters. One limitation is it's slower and heavier on memory for large datasets since it has to keep track of distances between every pair of clusters as it merges.

On this dataset, K-Means actually scored better than Agglomerative Clustering: K-Means got a Silhouette Score of 0.283 and Davies-Bouldin of 1.270, while Agglomerative got a Silhouette Score of 0.218 and Davies-Bouldin of 1.325. So K-Means gave tighter, better separated clusters here.

## 5. My Findings

For this wholesale segmentation task, I'd recommend K-Means over Agglomerative Clustering. Not only did it score better on both metrics, it's also much faster to run and easier to explain to a non-technical audience (5 spending "profiles" with clear centers), which matters if the distributor's sales team needs to actually use these segments day to day.

That said, I wouldn't throw away the elbow/silhouette results completely — at k=2 both methods actually score higher (silhouette around 0.36-0.37) than at k=5, meaning the data may naturally split into just two rough Horeca vs Retail groups. The 5-cluster version is more useful for detailed marketing actions, but a 2-cluster version might be a better starting point if the distributor only wants a very simple split of its customer base.
