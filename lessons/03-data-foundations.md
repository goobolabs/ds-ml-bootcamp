# Lesson 3 – Data Foundations

> Lesson 2 covered what ML is and how it works. Now we focus on the raw material every model depends on: **data** — how it’s structured, collected, and prepared.

---

## What You'll Learn

By the end of this lesson, students will be able to:

1. Understand the concepts of **features (X)** and **labels (y)**, and explain their role in ML problems.
2. Distinguish between a **sample** (single row) and a **dataset** (collection of samples).
3. Recognize the importance of **data collection**, and identify what makes data relevant, accurate, sufficient, and representative.
4. Explain why **preprocessing** is necessary before training ML models.
5. Apply knowledge of the main preprocessing techniques conceptually, including:

   - Handling missing values
   - Encoding categorical data
   - Scaling numerical features
   - Engineering and selecting features
   - Performing advanced data processing (dimensionality reduction, balancing, noise removal)

---

## Features & Labels

Before training any Machine Learning model, we must clearly define what goes **into** the model and what we want to **get out** of it.
The **inputs** are called **features (X)**, and the **output** we want to predict is called the **label (y)**.

Understanding features and labels is the **first step** in framing an ML problem, because they tell us exactly what the model should learn from the data. Without this distinction, the model has no direction.

---

### Visual Analogy

Think of solving a mystery:

- **Features (X) = clues** 🕵️ (footprints, fingerprints, witness reports).
- **Label (y) = the answer** 🧩 (who committed the crime).

Just like a detective uses many clues to figure out the truth, an ML model uses features to predict the correct label.

---

### Example: Housing Dataset

| Size (sq ft) | Bedrooms | Location | Price (\$) |
| ------------ | -------- | -------- | ---------- |
| 1000         | 2        | Suburb   | 200,000    |
| 1500         | 3        | City     | 300,000    |
| 2000         | 4        | Suburb   | 400,000    |
| 1800         | 3        | Rural    | 220,000    |

- **Features (X):** Size, Bedrooms, Location
- **Label (y):** Price

Each row is one **sample** (features + label). Together, all rows form the **dataset**.

---

## Sample vs Dataset

Once we know what features and labels are, the next step is to see how they are organized in our data.
In ML, data is structured into **samples** (individual examples) and **datasets** (collections of samples).

---

### What is a Sample?

- **Definition:** A **sample** is a single example from the dataset.
- It contains all the **feature values (X)** and the **label (y)** for one case.
- Usually represented as **one row in a table**.

#### Example: One house (sample)

| Size (sq ft) | Bedrooms | Location | Price (\$) |
| ------------ | -------- | -------- | ---------- |
| 1500         | 3        | City     | 300,000    |

- **Features (X):** \[1500, 3, “City”]
- **Label (y):** 300,000

Think of a sample as one **flashcard** — clues (features) on the front, answer (label) on the back.

### What is a Dataset?

- **Definition:** A **dataset** is a collection of many samples.
- It is the full table we use to train and test models.
- In tabular form:

  - **Rows = samples**
  - **Columns = features + label**

#### Example Dataset (Houses)

| Size (sq ft) | Bedrooms | Location | Price (\$) |
| ------------ | -------- | -------- | ---------- |
| 1000         | 2        | Suburb   | 200,000    |
| 1500         | 3        | City     | 300,000    |
| 2000         | 4        | Suburb   | 400,000    |
| 1800         | 3        | Rural    | 220,000    |

- Each **row = sample**
- Entire **table = dataset**

---

---

## Data Collection

Every Machine Learning project starts with **data**.
If you don’t have good data, you can’t build a good model — no matter how advanced the algorithm is.

There’s a famous saying in ML:

> **Garbage in → Garbage out**

If your dataset is poor quality, the predictions will also be poor.

So before preprocessing or modeling, we must carefully consider **where our data comes from** and whether it’s good enough for the task.

---

### Sources of Data

Data can come from many places. Some common sources include:

1. **Databases (internal company systems):**

   - Sales records, customer information, product inventories.
   - Example: Amazon using purchase history to recommend products.

2. **Sensors & IoT devices:**

   - Cameras, microphones, GPS trackers, weather stations.
   - Example: Tesla cars collecting driving data from sensors.

3. **User-generated behavior:**

   - Clicks, likes, shares, time spent on a page.
   - Example: YouTube recommending videos based on your watch history.

4. **Public datasets:**

   - Kaggle, UCI ML Repository, government open data portals.
   - Example: Titanic passenger dataset (predict survival).

5. **APIs / Web Scraping:**

   - Twitter API for tweets, financial APIs for stock prices.
   - Example: Collecting live news headlines to predict market sentiment.

> Always ensure legal basis, consent, and anonymization when working with sensitive data.

---

### Qualities of Good Data

Not all data is useful. Good datasets should be:

1. **Relevant** – Must match the problem you want to solve.

   - If predicting house prices, don’t collect unrelated data like the owner’s favorite color.

2. **Accurate** – Free from mistakes and errors.

   - Wrong house sizes or incorrect prices will mislead the model.

3. **Sufficient** – Enough examples to learn patterns.

   - A dataset with only 10 houses isn’t enough to build a reliable price predictor.

4. **Representative** – Covers all types of cases.

   - If you only collect city houses, your model won’t work for rural houses.

---

### Example: Housing Dataset (Collected)

Let’s say we collect housing sales data from a real estate website.

| Size (sq ft) | Bedrooms | Location | Price (\$) |
| ------------ | -------- | -------- | ---------- |
| 1000         | 2        | Suburb   | 200,000    |
| 1500         | 3        | City     | 300,000    |
| 2000         | 4        | Suburb   | 400,000    |
| 1800         | 3        | Rural    | 220,000    |
| 1200         | 2        | City     | 250,000    |

- **Relevant:** All columns help predict price.
- **Accurate:** Sizes and prices are correct.
- **Sufficient:** We would need **thousands** of rows like this.
- **Representative:** Must include houses from different regions (City, Suburb, Rural).

---

### Common Challenges in Data Collection

- **Missing data:** Some rows don’t have complete information.
- **Bias:** If only one group is represented (e.g., city houses only).
- **Noisy data:** Wrong entries or typos (e.g., “3000000” instead of “300000”).
- **Privacy:** Some data (like medical or financial) may be restricted.

This is why preprocessing (next step) is critical.

---

## Data Preprocessing

Raw data in the real world is **messy**:

- Some values are missing.
- Some columns are text, which computers can’t process directly.
- Some features are on very different scales.

**Preprocessing** is the step where we **clean and transform** raw data into a format that a machine learning model can use effectively.

Without preprocessing, even the best algorithm will give poor results.

---

### Why Preprocessing is Important

- **Completeness:** Missing data confuses the model.
- **Consistency:** Text categories must be converted into numbers.
- **Fairness:** Features on large scales shouldn’t dominate small-scale features.
- **Accuracy:** Cleaned data → better predictions.

Think of preprocessing as _washing and preparing ingredients before cooking_.

---

### Example Raw Housing Dataset

| Size (sq ft) | Bedrooms | Location | Price (\$) |
| ------------ | -------- | -------- | ---------- |
| 1000         | 2        | Suburb   | 200,000    |
| 1500         | 3        | City     | 300,000    |
| NaN          | 4        | Suburb   | 400,000    |
| 1800         | NaN      | Rural    | 220,000    |
| 1200         | 2        | **??**   | 250,000    |

Problems here:

- Missing **Size** (row 3).
- Missing **Bedrooms** (row 4).
- Unknown **Location** (row 5).

---

### Preprocessing Techniques

### Handling Missing Values

Options:

1. **Remove** rows/columns (if very few are missing).

   - Example: Drop row 5 (location unknown).

2. **Fill (Impute)** missing values with:

   - **Numerical columns** → Mean, Median, or Mode.

     - Example: Replace missing Size with average of other sizes.

   - **Categorical columns** → Most Frequent Category.

     - Example: Fill missing Bedrooms with the most common number of bedrooms (3).

This ensures the dataset stays usable.

---

### Encoding Categorical Data

ML models only understand **numbers**, not text like “City” or “Suburb.”

Two main methods:

1. **Label Encoding**

   - Assign a unique number to each category.
   - Example: City=0, Suburb=1, Rural=2.
   - Problem: Implies order (City < Suburb < Rural), which may not be true.

2. **One-Hot Encoding (preferred for most ML)**

   - Create a new column for each category.
   - Example:

| Size | Bedrooms | Loc_City | Loc_Suburb | Loc_Rural | Price |
| ---- | -------- | -------- | ---------- | --------- | ----- |
| 1000 | 2        | 0        | 1          | 0         | 200k  |
| 1500 | 3        | 1        | 0          | 0         | 300k  |
| 2000 | 4        | 0        | 1          | 0         | 400k  |
| 1800 | 3        | 0        | 0          | 1         | 220k  |

Now the model can “see” location as numbers without fake ordering.

---

### Feature Scaling

Once features are encoded into numbers, there’s still another problem:
Different features may exist on **very different scales**.

For example, in our housing dataset:

- **Size (sq ft):** 1000–2000
- **Bedrooms:** 2–4
- **Price:** 200,000–400,000

Here, “Size” has values in the thousands, while “Bedrooms” is a small integer. If we train models directly, the algorithm may mistakenly think “Size” is far more important than “Bedrooms” simply because its numbers are larger.

---

#### Why Scaling Matters

- **Distance-based models** (KNN, K-Means, SVM) → need scaling to measure distances fairly.
- **Gradient-based models** (Logistic Regression, Neural Networks) → scale helps optimization converge faster.
- **Regularization-based models** (Ridge, Lasso) → penalization depends on feature size.
- **Tree-based models** (Decision Trees, Random Forest, XGBoost) → mostly unaffected by scaling.

In short: **most ML models need scaling**, except for trees.

---

#### Methods of Scaling

There are several ways to scale features:

#### A. Normalization (Min-Max Scaling)

- Rescales every feature to fit within a fixed range, usually **[0, 1]**.
- The smallest value becomes 0, the largest becomes 1, and everything else falls in between.

✅ Keeps values bounded, good for neural networks.
❌ Sensitive to outliers.

---

#### B. Standardization (Z-score Scaling)

- Shifts and stretches each feature so it has a **mean of 0** and a **standard deviation of 1**.
- Values above average become positive; values below average become negative.

✅ Good default, works even with outliers.
✅ Preferred for algorithms assuming normal distribution.

---

#### C. Robust Scaling

- Instead of using the mean and range, it uses the **median** and **IQR (interquartile range)**.
- Because the median and IQR ignore extreme values, outliers have much less influence on the result.

✅ Best choice when the dataset contains many outliers.

---

#### Which Scaling to Use?

- **Min-Max Normalization** → Neural Networks, KNN (when no outliers).
- **Standardization (Z-score)** → General-purpose, safe default.
- **Robust Scaling** → When dataset has many outliers.

---

**Key idea:** Feature scaling doesn’t change the meaning of data — it only makes features comparable, ensuring that algorithms learn fairly.

---

### Feature Engineering & Advanced Data Processing

After **basic preprocessing** (cleaning, encoding, scaling), we often need to go further:
**Feature Engineering** = creating new features or transforming existing ones to improve model performance.
**Other Data Processing** = extra steps like dimensionality reduction, balancing datasets, or noise filtering.

These steps are often the **”secret sauce”** of good ML projects.

---

#### What is Feature Engineering?

**Definition:**
Feature engineering is the process of using **domain knowledge + creativity** to create, transform, or select features that make machine learning models more effective.

#### Examples with Housing Dataset

| Size (sq ft) | Bedrooms | Location | Price |
| ------------ | -------- | -------- | ----- |
| 1000         | 2        | Suburb   | 200k  |
| 1500         | 3        | City     | 300k  |
| 2000         | 4        | Suburb   | 400k  |
| 1800         | 3        | Rural    | 220k  |

#### Possible Feature Engineering:

1. **Create new features**

   - `Price per sq ft = Price / Size`
   - `Bedrooms per 1000 sq ft = Bedrooms / Size`

2. **Transform features**

   - Convert “Location” into urban=1 vs non-urban=0.
   - Apply log transformation to “Size” if skewed.

3. **Combine features**

   - “House Age” + “Renovation Year” → “Effective Age.”

---

### Feature Selection

Not all features are useful. Some may be irrelevant or harmful (noise).
Feature selection is the process of choosing the **most important features**.

#### Methods:

- **Manual selection** using domain knowledge.
- **Statistical tests** (correlation, chi-square).
- **Model-based selection** (e.g., Random Forest feature importance).

Example: If “Owner’s favorite color” is in the dataset → drop it, because it’s irrelevant to predicting price.

---

### Other Data Processing Steps

#### A. Dimensionality Reduction

- When you have **too many features**, models become slow and may overfit.
- Technique: **Principal Component Analysis (PCA)** reduces features while keeping most of the information.
- Example: 1000 pixel features in images → reduce to 50 principal components.

---

#### B. Balancing Datasets

- Many real-world datasets are **imbalanced** (e.g., 95% healthy patients, 5% sick).
- Models tend to predict the majority class always.
- Solutions:

  - **Oversampling** minority class (e.g., SMOTE).
  - **Undersampling** majority class.

Example: Fraud detection (only 1% of transactions are fraud) → must balance.

---

#### C. Noise Reduction

- Real data may contain errors (sensor glitches, typos).
- Techniques:

  - Smoothing noisy time-series (moving averages).
  - Removing outliers (values far from normal distribution).

---

## Summary

- **Features (X):** Inputs used for prediction (e.g., size, bedrooms, location).
- **Labels (y):** Outputs we want to predict (e.g., house price).
- **Sample vs Dataset:** One row = sample, collection of rows = dataset.
- **Data Collection:** Good data must be relevant, accurate, sufficient, and representative.
- **Preprocessing:** Essential for model success — includes handling missing values, encoding categories, and scaling features.
- **Feature Engineering & Advanced Processing:** Create new features, drop irrelevant ones, reduce dimensions, balance classes, and handle noise to make data model-ready.

---

*End of Lesson 3*

---