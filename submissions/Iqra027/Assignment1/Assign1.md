1.
-Data Science is method of study how to transform a raw data into action , stories or decisions with the help of mathematics,computer knowledge and algorithms.
-Machine Learning is containes Artificial intelligence and it  comes when you done the data(gathering,cleaning,analyzing) that you want to build a system that learn from the data to predict event for the future data.
=Relationship between them is:
=Data science covers the entire data journey while Machine Learning comes when the data needs to make automated decision or predic analytics.
=Real life example :
A developer made an ecommerce site for an automated system while using the data(search,past history,next purchase)thanks to data science he knew it that most users next move after buying a mouse will be the batery so he made a model to recommend automatic suggestion when a user clicks a mouse.

2.Data life cycle:
a.Problem Definition:Understanding the whole concept of the the project's prespective.
b.Data Collection:to gather the data from all sources to solve the problem.
c.Data cleaning:Handling Missing values or removing the duplicates or correcting errors and formats.
d.Exploratory data analysis:EDA helps identify trends, correlations and anomalies before building formal models.
e.Data Modelling:Selecting and training algorithms to make predictions, classify data or discover hidden patterns
f.Model Evaluation:Testing the model's performance against strict metrics (such as accuracy, precision, or recall) using data it has never seen before to ensure it generalizes well to the real world.
g.Deployment and Maintainance:Integrating the finalized model into the Real world where it can process live data.
The model will need continuous monitoring to ensure its accuracy does not degrade over time.
-Machine Learning will come the data model and the Evaluation stage. 

3.In Supervised Learning, computers learn from given data with input and output pairs,which means for every piece of information you give the machine, you also give it the correct answer (label).
while UnSupervised Learning computers must figures out their own from the input data and discover the hidden patterns ,structure in unlabeled data.

-Example of supervised learning:numers between(1-70)
you tell computer the correc answer like 1 is odd ,2 even ,and so on then you train the computer :the numbers ends(2,4,6,8) is even while the ones ends(1,5,7,9) is odd and the computer will learn then you test(70 upto 100) with no labels and Because it learned the pattern ,The computer will tell 71 is odd,72even.

-Insupervised Learing :you hand computer the numbers(1,100).
and you wouldn't tell computer which one is odd or even ,you just say separate these numbers into 2 groups based on how numbers behave.The computer looks at the properties of the numbers.It might test how they interact when divided by 2. It notices a stark mathematical split:
Group A: Numbers that leave a remainder of 0 when divided by 2 (2, 4, 6, 8..).
Group B: Numbers that leave a remainder of 1 when divided by 2 (1, 3, 5, 7..).

4.Overfitting occurs when a machine learning model learns the training data too well. Instead of capturing the broad, underlying trends, the model memorizes the noise and specific quirks of the training dataset.

=Methods to Prevent Overfitting
1.Regularization: Applying mathematical penalties to the model's loss function to discourage overly complex models (e.g., L1/Lasso or L2/Ridge regularization).

2.Cross-Validation: Rotating which portions of the data are used for training and validation to ensure the model's performance is consistent across different subsets.

3.Pruning: In decision trees, cutting back branches that provide little predictive power to simplify the structure.

4.Early Stopping: During the training phase of iterative algorithms (like neural networks), halting training the moment performance on a separate validation dataset begins to deteriorate.

5.Data Augmentation: Artificially increasing the size of the training dataset by creating slightly modified versions of existing data (e.g., rotating or cropping images).

5.When developing a machine learning model, the available dataset is split into distinct subsets: Training Data and Test Data. Typically, a standard distribution might use 80% of the data for training and 20% for testing.

*Purpose of Each Split*
Training Data: This is the portion of the dataset exposed directly to the machine learning algorithm. The model analyzes these data points to adjust its internal parameters, learn relationships, and map inputs to outputs.

Test Data: This portion is strictly held back. It acts as a simulation of the "real world." The model is not allowed to see or interact with this data during the training phase.

*Why This Process is Necessary*
Splitting the data is essential to evaluate the generalization capability of the model. If a model is evaluated using the exact same data it trained on, its performance metrics will be deceptively high, masking issues like overfitting.

By testing the model on a completely independent test set, data scientists can accurately measure how well the model will perform when deployed in a live, real-world environment. It serves as an objective reality check for the model's true predictive power.

6.Case Study: Machine Learning for Business Optimization and Customer Retention
Article Reference
Source: Gomez-Uribe, C. A., & Hunt, L. A. (2015). The Netflix Recommender System: Algorithms, Business Value, and Innovation. ACM Transactions on Management Information Systems (TMIS), 6(4), 1-19.

1. Study Summary & Findings
This seminal paper outlines how Netflix architecturalized its world-renowned personalized recommendation system using data science and machine learning.

At the time of publication, Netflix faced a major business challenge: if a subscriber could not find something compelling to watch within 60 to 90 seconds, they would lose interest and risk abandoning the service (subscriber churn). To counter this, the engineering team designed a unified recommendation engine composed of multiple distinct machine learning algorithms working in parallel (including collaborative filtering, matrix factorization, content-based filtering, and neural networks). These algorithms process explicit data (like user ratings and search terms) and implicit data (like viewing history, time of day a show is watched, and when a user pauses a video).

Key Findings:

Massive Business Value: The implementation of the machine learning recommendation system successfully saves Netflix over $1 billion per year by dramatically reducing customer churn and increasing user retention.

Algorithmic Influence: The authors revealed that 80% of the total stream hours watched on Netflix are driven directly by automated recommendations, rather than organic search.

Multi-Model Synergy: The system does not rely on a single algorithm; instead, it combines specialized models for different rows on the homepage (e.g., a "Top-N Video Ranker" for personalized picks, a "Trending Now" model for temporal peaks, and a "Continue Watching" sorter to predict re-engagement probabilities).

2. Data Science Lifecycle Coverage
This case study is uniquely comprehensive because it spans almost the entire Data Science Lifecycle, with an exceptional focus on the following stages:

Problem Definition: The lifecycle begins with a clear business translation. The high-level corporate goal of "saving money and keeping subscribers" was translated into a definitive data science objective: "Maximize the probability that a user will stream a recommended video and watch it to completion within their first 90 seconds of browsing."

Data Collection & Acquisition: The authors detail the massive pipeline required to capture both explicit user feedback (thumbs up/down) and implicit digital footprints (device type, playback delays, scrolling patterns, and browsing duration).

Data Modeling: The core of the paper focuses on the creation, blending, and tuning of complex algorithms. The authors explain how they utilize historical data to train model architectures that map user behavioral patterns to video categories.

Model Evaluation (A/B Testing): A major highlight of the study is its emphasis on evaluation. While models are initially evaluated offline using statistical metrics (like Root Mean Squared Error), Netflix subjects every algorithmic modification to rigorous online A/B Testing. They split millions of live users into control and variant groups to measure whether a new model actually increases real-world streaming hours before deploying it globally.

Deployment & Scale: The study covers the final stage of the lifecycle by describing how these complex mathematical models are hosted on cloud infrastructure (AWS) to generate personalized homepages dynamically for hundreds of millions of active users simultaneously under extreme low-latency constraints.