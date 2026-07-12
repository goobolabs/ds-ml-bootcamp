# Reflection Paper — Clustering Assignment

## Introduction

This assignment helped me understand the practical application of unsupervised machine learning, especially clustering techniques. The main goal was to group similar customers based on their purchasing behavior without using predefined labels. I implemented K-Means clustering from the lesson and explored an additional clustering algorithm to compare different approaches.

## What I Learned

Through this assignment, I learned how clustering algorithms identify hidden patterns in datasets. Unlike supervised learning, clustering does not require target labels. Instead, the algorithm analyzes similarities between data points and creates groups based on their characteristics.

I gained a better understanding of the K-Means algorithm, including how it selects cluster centers, assigns data points to the nearest centroid, and updates centroids iteratively until the clusters become stable. I also learned the importance of choosing the correct number of clusters using methods such as the Elbow Method.

## Data Preprocessing Experience

One important lesson from this assignment was that data preprocessing has a major impact on machine learning performance. Before applying clustering, I cleaned the dataset, selected relevant features, and standardized the data.

Feature scaling was necessary because clustering algorithms use distance measurements. Without scaling, features with larger numerical values could dominate the clustering results and create inaccurate groups.

## Challenges Faced

One challenge I faced was understanding how to evaluate clustering results because there are no predefined correct answers like in classification problems. I learned that evaluation methods such as SSE (Within-Cluster Sum of Squares) and visualization techniques help determine whether the clusters are meaningful.

Another challenge was interpreting the cluster results. After creating clusters, I needed to analyze customer characteristics and understand what each group represented.

## Comparison of Algorithms

By implementing K-Means and another clustering algorithm, I learned that different algorithms have different strengths and weaknesses. K-Means is simple, fast, and works well when clusters have a similar shape and size. However, it requires selecting the number of clusters beforehand.

Other clustering methods can handle different types of data structures and may discover patterns that K-Means cannot detect. Choosing the right algorithm depends on the dataset and the goal of the analysis.

## Real-World Applications

Clustering has many practical applications in different industries. Businesses can use customer segmentation to understand customer groups, improve marketing strategies, and provide personalized services.

Other examples include fraud detection, recommendation systems, medical research, image analysis, and social network analysis.

## Conclusion

This assignment improved my understanding of unsupervised learning and clustering techniques. I learned how to prepare data, apply clustering algorithms, evaluate results, and interpret the discovered patterns.

The experience showed me that machine learning is not only about training models but also about understanding data and selecting appropriate methods for solving real-world problems.
