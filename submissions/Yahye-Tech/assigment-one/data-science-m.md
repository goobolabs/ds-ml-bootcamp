# Data Science & Machine Learning

A simple guide with examples and a case study.

## 1. Definitions and Relationship

**Data Science** is a field that uses statistics, computer skills, and subject knowledge to find useful information in data. It covers everything from collecting data to sharing results.

**Machine Learning (ML)** is a part of AI where computer programs learn patterns from data and get better at a task over time, without someone writing exact rules for every case.

### How They Connect

ML is one tool that Data Science uses. Data Science is the bigger process (asking questions, gathering data, cleaning it, building models, and sharing results), and ML is the part where the model actually learns and predicts.

### Example: Bank Fraud Detection

A bank collects transaction data like amount, location, and time. The team cleans this data, looks for patterns linked to past fraud cases, then builds an ML model that flags suspicious transactions. The ML model does the prediction, but the whole process around it, deciding what counts as fraud, checking the data is correct, and adding the model to the bank's system, is Data Science.

---

## 2. The Data Science Lifecycle

1. **Problem Definition** – Figure out the question you're trying to answer.
2. **Data Collection** – Gather data from databases, sensors, or other sources.
3. **Data Cleaning** – Fix missing values, remove duplicates, fix errors.
4. **Exploratory Analysis** – Look at the data to spot patterns and trends.
5. **Modeling** – Build the model, this is where ML comes in.
6. **Evaluation** – Test how well the model works.
7. **Deployment** – Put the model into real use.
8. **Monitoring** – Keep checking the model and update it when needed.

### Why ML Fits at Step 5

ML needs clean, organized data to work with. If the data is messy or the question isn't clear, ML won't work well. After building the model, evaluation and modeling often go back and forth until the results are good enough.

---

## 3. Supervised vs. Unsupervised Learning

|  | Supervised Learning | Unsupervised Learning |
|---|---|---|
| **Data** | Has labels (correct answers given) | No labels |
| **Goal** | Predict an answer | Find hidden patterns or groups |
| **Examples** | Linear regression, decision trees | K-means clustering, PCA |

### Supervised Example: Loan Approval

A bank has past loan records, each marked as "approved" or "rejected," along with the applicant's income, credit score, and job history. The model learns from these past results, then predicts whether a new applicant should be approved.

### Unsupervised Example: Customer Grouping

A store has data on what customers buy, but no labels for "types" of customers. A clustering tool groups customers by their shopping habits, then the store can name these groups, like "weekend shoppers" or "bulk buyers."

---

## 4. What Causes Overfitting and How to Stop It

**Overfitting** happens when a model learns the training data too closely, including small mistakes and random noise. It does great on training data but poorly on new data.

### Main Causes

- The model is too complex (too many details to learn from too little data).
- Not enough training data.
- Training for too long.
- Too many unhelpful features in the data.

### How to Fix It

- **Cross-validation** – Test the model on different parts of the data.
- **Regularization** – Add a penalty to stop the model from getting too complex.
- **Pruning** – Cut back parts of a decision tree that aren't useful.
- **Early stopping** – Stop training once results stop improving.
- **Dropout** – Randomly turn off parts of a neural network during training.
- **More data** – Helps the model learn general patterns instead of memorizing.
- **Feature selection** – Remove data columns that don't help.

---

## 5. Training and Test Data Split

- **Training set** (about 70-80%) – Used to teach the model.
- **Test set** (about 20-30%) – Kept separate, used only to check the final model.
- **Validation set** (optional) – Used to fine-tune the model before final testing.

### Why This Matters

The goal of ML is for the model to work well on new data it hasn't seen before, this is called **generalization**. If you test the model on the same data it learned from, it will look like it's doing great just because it memorized the answers. Keeping a separate test set gives an honest result. Usually data is split **randomly**, but for things like stock prices, a **time-based split** is better (older data trains, newer data tests), since this matches how it would work in real life.

---

## 6. Case Study: ML in Transportation

**Source:** "Intelligent Transportation System's Machine Learning-Based Traffic Flow Prediction Tool," published October 2024

### Background

The goal was to build a traffic prediction tool that considers things like road repairs, events, and traffic signals, all the everyday stuff that affects how traffic moves. Since traffic data is huge and growing fast, the study used big data methods because older models couldn't keep up with real-world traffic.

### What They Found

The researchers used machine learning along with genetic algorithms, built around three parts: data input, ML processing, and output through a mobile app. This setup worked with both live traffic data and past records, giving fast and useful predictions.

The mobile app connects the prediction model to actual drivers, giving them near real-time updates so they can plan better routes. The researchers also pointed out this could help with self-driving car technology in the future.

Another related study tackled a common problem: predicting traffic on roads that don't have sensors. They built a model that predicts traffic from 1 hour up to 24 hours ahead, using hourly data to reduce noise. They later improved this by training on a full year of data instead of just 3 months.

### Which Lifecycle Stages Does This Cover?

- **Problem Definition** – Clear goal: reduce traffic congestion and help drivers.
- **Data Collection** – Real-time and historical traffic data, plus extra factors like road events.
- **Modeling** – Main focus, combining ML with genetic algorithms.
- **Deployment** – Strong here, the mobile app is a real product people can use.
- **Evaluation** – Mentioned but not the main focus.

This study stands out because it actually reaches the **deployment** stage with a working app, many research papers stop at just building and testing the model.

---

## References

1. "Intelligent Transportation System's Machine Learning-Based Traffic Flow Prediction Tool." *Journal of Applied Data Sciences*, Vol. 5, No. 4, October 2024. [Link](https://bright-journal.org/Journal/index.php/JADS/article/download/364/275)
2. "Proposal of a Machine Learning Approach for Traffic Flow Prediction." *PMC*, 2024. [Link](https://pmc.ncbi.nlm.nih.gov/articles/PMC11014399/)
