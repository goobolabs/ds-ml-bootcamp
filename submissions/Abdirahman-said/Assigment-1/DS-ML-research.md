# Data Science & Machine Learning Study Notes

---

## Table of Contents
1. [Definitions](#1-definitions)
2. [Data Science Lifecycle](#2-data-science-lifecycle)
3. [Supervised vs Unsupervised Learning](#3-supervised-vs-unsupervised-learning)
4. [Overfitting & Underfitting](#4-overfitting--underfitting)
5. [Training Data & Test Data](#5-training-data--test-data)
6. [Case Study – ML in Transportation](#6-case-study--ml-in-transportation)

---

## 1. Definitions

## Data science
Data science is the study of data used to extract meaningful insights for business decisions. It combines mathematics, computing and domain knowledge to solve real-world problems and uncover hidden patterns.

## Machine learning
Machine learning is the subset of artificial intelligence (AI) focused on algorithms that can “learn” the patterns of training data and, subsequently, make accurate inferences about new data.

## relationship between DS and ML

|concept | Data Science | Machine Learning |
|---|---|---|
| Scope | Broad: entire data lifecycle | Narrow: predictive algorithms
| Focus | Insights, decisions, communication | Learning patterns, predictions | |
| Task | Data cleaning, analysis, visualization, modeling | Model training, testing, optimization |
| Role | Understand data, find answers | Automate learning & prediction |
| Relationship | Uses ML as a tool | Subset of data science |


## Healthcare Example — Data Science vs Machine Learning
| part of the process | Data science| machine learning |
|---|---|---|
| Goal | Understand patient data and identify medical risk factors | Predict which patients are likely to develop a disease |
| Example Task | Analyze patient history, lab results, lifestyle data | Train a model to predict diabetes or heart‑disease risk |
| What Happens | Data is cleaned, explored, visualized, and interpreted | Algorithm learns patterns and makes predictions |
| Human Role | Doctors + data scientists define the problem and interpret insights | Engineers tune models, validate accuracy, and deploy predictions |
| output | Insights: “These factors increase disease risk” | Prediction: “This patient has a 78% risk of diabetes” |
| purpose | Support medical decisions and prepare high‑quality data | Automate risk detection and improve early intervention |

---

## 2. Data science lifecycle

The Data Science lifecycle is the end‑to‑end process of turning a real‑world problem into a working, deployed data‑driven solution.
Machine Learning fits in the middle, after the data is prepared and before deployment, because ML models need clean, structured data to learn from.

```
1. Proplem definition    →  What question are we answering?
2. Data collection          →  Surveys, logs, APIs sensors, databases
3. Clean the data        →  Fix errors, fill gaps, remove duplicates
4. Data exploration      →  Visualizations, summary statics, correlation analysis
5. Feature engineering  →  Creating new variables, encoding categories
6. Build the model  →   this is where ML fits in the lifecycle
7. Model evaluation    →  Test accuracy, fix errors, retrain
8. Deploy + Monitor      →  Ship to product. Track performance.
```
> ML is not the first step — it’s the step that turns prepared data into predictions.

---

## 3. supervised and unsupervised learninng

## supervised learning
supervised learning uses labeled examples to teach models to predict or classify.
using labeled inputs and outputs, the model can measure its accuracy and learn over time.

## Types of supervised learning:
1. classification
2. regression 
3. object detection.
## real world example

## Analysing selling price of for cars
Predicting the selling price of cars based on features like brand, model, age, mileage, and additional attributes. Predicting the selling price of cars based on a set of features is a classic example of regression in machine learning. In this scenario, a model is trained to understand the relationship between various attributes of cars and their corresponding selling prices.

## unsupervised learninng 
Unsupervised learning is a type of machine learning where the algorithm is provided with input data without explicit instructions on what to do with it. The system tries to learn the patterns and structure inherent in the data without labeled outputs.

## types of unsupervised learning:
1. Clustering
2. dimentionality reduction 
3. association.

## real world example

The Ted Talks Recommendation System employs machine learning algorithms to analyze user preferences and suggest relevant talks that align with individual interests.

## comparison

| Aspect | Supervised | Unsupervised |
|---|---|---|
| Data | Labeled input–output pairs. | Unlabeled input data only. |
| Primary Goal | Predict a known target or map inputs to outputs. | Discover hidden structure or patterns. |
|Common Tasks | Classification; Regression. | Clustering; Dimensionality reduction; Anomaly detection. |
| Evaluation | Measured against ground truth (accuracy, RMSE, AUC). | Intrinsic or downstream metrics (silhouette, reconstruction error). |
| When to Use | You have clear labeled outcomes and need predictions. | You want segmentation, exploration, or feature learning. |

## conclusion
In conclusion, supervised and unsupervised learning stand as pillars in the for machine learning, each offering unique capabilities and applications.

---

## 4. overfitting

- Overfitting happens when a machine learning model memorizes training data, including noise, and fails to generalize to new data.

## how to detect overfitting

- Large gap between training and validation performance(high training accuracy, much lower validation accuracy).
- Validation loss rising while training loss falls during training.

---

## 5. Test data and training data

Training and test data are split so that a model learns from one portion of the dataset and is evaluated on another it has never seen. This separation is necessary to measure how well the model generalizes to new, real‑world data and to prevent overfitting.

## Why Splitting Is Necessary

- **Prevents overfitting** : If you train and test on the same data, the model may memorize noise instead of learning general patterns.
- **Ensures generalization** : The test set simulates unseen, real‑world data. Performance here is a realistic measure of deployment success.
- **Fair comparison**: Different models can be compared objectively using the same test set.
- **Detects failure modes **: A large gap between training and test accuracy signals overfitting; poor performance on both indicates underfitting.

---

## 6. case study
A transportation case study showed that deep learning models (LSTM networks) significantly outperformed traditional statistical methods (ARIMA) in forecasting logistics demand across distribution centers in Brazil, improving resource planning and operational efficiency. 

## Case study overview

The paper “Deep Learning and Statistical Models for Forecasting Transportation Demand: A Case Study of Multiple Distribution Centers” (MDPI, 2023) examined how different modeling approaches perform in predicting transportation demand for a Brazilian carrier operating 54 distribution centers. 
- Problem: Logistics operators need accurate demand forecasts to optimize fleet usage, reduce costs, and plan resources.
- Methods: Researchers compared traditional ARIMA models with deep learning LSTM networks across eight scenarios, including different preprocessing techniques, handling of outliers, and cross‑validation splits.

## findings

- LSTM networks outperformed ARIMA in **94% of dispatching units**.
- ARIMA only worked better in about **5% of cases**, typically where data was simpler or highly linear.
- Deep learning models captured complex temporal dependencies and variability in demand more effectively.

**Impacts** : Improved demand forecasting led to better resource planning, dispatch scheduling, and supply chain resilience.

## 🔄 Lifecycle Stage Covered

This case study primarily illustrates the Modeling and Evaluation stages of the Data Science lifecycle:
- **Data preparation**: preprocessing and handling outliers were critical.
- **Modeling**: ARIMA vs LSTM comparison shows how algorithm choice affects performance.
- **Evaluation**: cross‑validation and scenario testing ensured robust results.
**It highlights that choosing the right modeling technique is central to solving forecasting problems in transportation*.

## 🧠 Key Takeaways

- **Deep learning (LSTM)** is better suited for complex, non‑linear demand patterns.
- **Traditional statistical models (ARIMA)** remain useful for simpler, linear demand series.
- **Evaluation across multiple scenarios** is essential to avoid overfitting and ensure generalization.
- **Business value**: Accurate demand forecasting directly improves logistics efficiency, cost savings, and customer satisfaction.

## why it matters

*This case study shows how machine learning in transportation can move beyond pilot projects to deliver tangible operational improvements. It demonstrates the importance of aligning modeling choices with the complexity of the data and the business need*.

## refference

*https://www.mdpi.com/2305-6290/7/4/86?utm_source=copilot.com*

---
