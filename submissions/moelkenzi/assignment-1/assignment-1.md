# Research Assignment: Introduction to Data Science and Machine Learning

**1. Data Science and Machine Learning: Definitions and Relationship**

- **Data Science (DS)** is the pipeline that takes messy, raw data, cleans it, processes it, structures it, and applies mathematical and statistical models to find underlying patterns, make predictions, and tell a story that drives actionable decisions.
- **Machine Learning (ML)** is a subfield of artificial intelligence (AI) that focuses on the development of algorithms capable of identifying complex patterns within data to make autonomous decisions.

**Relationship & Real-Life Example:**
Data Science is the overarching framework, while Machine Learning is the engine used for the predictive modeling phase within that framework.

_Example:_
Consider an early-warning system designed to predict drought risks in the Horn of Africa 30<sup>°</sup>C to 60<sup>°</sup>C days in advance to protect local food security. **Data Science** encompasses the entire pipeline: collecting satellite imagery, organizing historical rainfall data, cleaning noisy soil moisture readings, and engineering features. **Machine Learning** is the specific phase where an algorithm (such as a Random Forest or Neural Network) trains on this cleaned historical data to learn the complex, hidden relationships between weather anomalies and subsequent droughts, ultimately outputting a precise risk probability for the upcoming month.

---

**2. The Data Science Lifecycle**
The lifecycle of a Data Science project typically follows a structured, iterative path:

1.  **Problem Definition:** Understanding the primary goal (e.g., "predicting extreme weather events").
2.  **Data Collection:** Gathering raw data from databases, APIs, or physical sensors.
3.  **Data Cleaning & Preprocessing:** Handling missing values, removing outliers, and normalizing data so it is machine-readable.
4.  **Exploratory Data Analysis (EDA):** Visualizing data distributions to discover initial trends and correlations.
5.  **Machine Learning Modeling:** Selecting, training, and tuning algorithms to make predictions based on the data.
6.  **Evaluation:** Testing the model's accuracy against unseen data using specific mathematical metrics.
7.  **Deployment & Monitoring:** Integrating the model into a live system (like a dashboard, API, or mobile app) and tracking its performance over time.

## <br>

<br>

**3. Supervised vs. Unsupervised Learning**

| Feature          | Supervised Learning                                                                                                                                                         | Unsupervised Learning                                                                                                                                                          |
| :--------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Definition**   | The algorithm is trained on a "labeled" dataset, meaning both the input features and the correct output (target) are provided. It learns to map inputs to specific outputs. | The algorithm is trained on an "unlabeled" dataset. The system tries to learn the hidden structure, distribution, or groupings of the data without explicit target outputs.    |
| **Primary Goal** | Prediction or classification of new, unseen data based on past examples.                                                                                                    | Finding hidden patterns, grouping similar data points, or reducing data dimensionality.                                                                                        |
| **Example**      | Predicting crop yields based on temperature and rainfall amounts (Regression), or classifying an email as Spam or Not Spam (Classification).                                | Grouping different agricultural regions into clusters based on similar soil moisture behaviors without knowing the specific names of those soil types beforehand (Clustering). |

---

<br>

**4. Overfitting: Causes and Prevention**
Overfitting occurs when a Machine Learning model learns the "noise" and random fluctuations in the training data rather than the underlying, true mathematical pattern. An overfitted model performs exceptionally well on its training data but performs very poorly on new, unseen data (a state known as high variance).

- **Causes:**
  - The model is too complex for the dataset (e.g., using a high-degree polynomial equation to model a simple curve).
  - The training data contains too much noise, errors, or irrelevant features.
  - The model is trained for too many iterations, memorizing the training data instead of generalizing.
- **Prevention:**
  - **Cross-Validation:** Using techniques like k-fold cross-validation to test the model on multiple mini-subsets of data to ensure it generalizes well.
  - **Regularization:** Adding a mathematical penalty for complexity to force the model to keep its learned weights small and simple.
  - **Pruning:** Deliberately removing unnecessary nodes or branches in algorithms like Decision Trees.
  - **Early Stopping:** Halting the training process before the model starts memorizing the noise.

---

**5. Training Data and Test Data Split**
When developing an ML model, the available dataset is split into two distinct, non-overlapping subsets:

- **Training Data (typically 70-80%):** The portion of the data used to teach the algorithm. The model analyzes this data to adjust its internal parameters and learn relationships.
- **Test Data (typically 20-30%):** The holdout portion. It is kept completely hidden from the model during the training phase.

_Why it is necessary:_ This split is the only reliable way to simulate how the model will perform in the real world. If a model is evaluated on the exact same data it was trained on, it will appear artificially accurate because it has already "memorized" the answers. Testing on unseen data provides an objective, unbiased measure of the model's true predictive power and proves that it can generalize to new situations.

---

**6. Case Study: Machine Learning in Transportation**
**Title:** _Smart and Sustainable Transportation Based on Artificial Intelligence in Big Cities: A case study of Isfahan, Iran_ (OICC Press, February 2026)

- **Summary of Findings:** This recent research study deployed an advanced AI architecture to solve urban congestion and reduce environmental impact in a metropolitan area. The researchers utilized Graph Neural Networks (GNNs) combined with Long Short-Term Memory (LSTM) layers to achieve over 80% accuracy in short-term traffic prediction. Additionally,
