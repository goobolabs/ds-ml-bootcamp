# Lesson 1 – Data Science

## What You'll Learn

By the end of this lesson, students will be able to:

1. Define what Data Science is and why it matters.
2. Understand the relationship between **Data Science**, **Machine Learning**, and **AI**.
3. Describe the **Data Science lifecycle** from problem to insight.
4. Identify the core **tools and skills** used by data scientists.
5. Recognize real-world applications of Data Science.

---

## What is Data Science?

We live in a world flooded with data — every click, purchase, search, and sensor reading generates information.
**Data Science** is the discipline that turns this raw data into meaningful insights and actions.

---

### Definition

**Data Science:**

> An interdisciplinary field that uses scientific methods, statistics, algorithms, and software tools to extract knowledge and insights from structured and unstructured data.

Think of a data scientist as a **translator** — they take messy, raw data and turn it into stories, decisions, and predictions that humans and organizations can act on.

---

### The Data Science Universe

Data Science sits at the intersection of three core areas:

| **Area**               | **Focus**                                         |
| ---------------------- | ------------------------------------------------- |
| Mathematics/Statistics | Understanding patterns, probability, and testing  |
| Computer Science       | Programming, algorithms, and data engineering     |
| Domain Knowledge       | Understanding the business/field the data is from |

Without all three, a data scientist is incomplete.

---

### Data Science vs Machine Learning vs AI

These three terms are often confused. Here is how they relate:

```
Artificial Intelligence (AI)
    └── Machine Learning (ML)
            └── Deep Learning
Data Science uses all of the above as tools
```

- **AI** is the broad goal: making machines simulate human intelligence.
- **Machine Learning** is one approach to AI: teaching machines to learn from data.
- **Data Science** is the end-to-end process: collecting, cleaning, analyzing, and communicating data — and using ML when prediction is needed.

A data scientist might spend only 20% of their time on ML models. The other 80% is data wrangling, exploration, and communicating findings.

---

### Why Data Science Matters

- **Better decisions**: Companies use data to make evidence-based choices instead of guessing.
- **Efficiency**: Automated analysis of millions of records in seconds.
- **Personalization**: Netflix recommends what you'll watch next; doctors predict which patients need urgent care.
- **Discovery**: Scientists use data science to find patterns in genomics, climate data, and particle physics.

---

### Real-World Examples

1. **Healthcare**
   - Predicting patient readmission rates.
   - Detecting diseases from medical images.

2. **Finance**
   - Fraud detection on credit card transactions.
   - Algorithmic trading and risk modeling.

3. **Retail & E-commerce**
   - Customer segmentation and targeted marketing.
   - Demand forecasting to manage inventory.

4. **Social Media**
   - Sentiment analysis on tweets and posts.
   - Content recommendation algorithms.

5. **Government & NGOs**
   - Tracking disease outbreaks (e.g., COVID-19 dashboards).
   - Optimizing resource distribution in humanitarian crises.

---

## The Data Science Lifecycle

Every data science project follows a lifecycle — a repeating cycle of stages.
Skipping a stage almost always leads to bad results.

---

### The Stages

#### **Stage 1: Problem Definition**

- Identify the question or problem to solve.
- Ask: _What do we want to know? What decision will this data inform?_
- Example: "Can we predict which customers are likely to cancel their subscription?"

⚠️ A poorly defined problem leads to useless analysis, even with great data.

---

#### **Stage 2: Data Collection**

- Gather raw data from relevant sources.
- Sources include:
  - Internal databases (sales records, logs)
  - External APIs (Twitter, weather, financial data)
  - Public datasets (Kaggle, UCI ML Repository, government open data)
  - Surveys and web scraping

Example: Collect 3 years of customer purchase history and support ticket logs.

---

#### **Stage 3: Data Cleaning (Preprocessing)**

Raw data is almost never ready to use. This stage is where most of a data scientist's time is spent.

Tasks include:
- Handle missing values (fill, drop, or impute).
- Remove duplicate records.
- Fix inconsistent formats (dates, units, categories).
- Filter out outliers that would distort analysis.

> Rule of thumb: 70–80% of data science work is cleaning data.

---

#### **Stage 4: Exploratory Data Analysis (EDA)**

Before modeling anything, **explore** the data to understand it.

- Look at distributions, ranges, and correlations.
- Visualize relationships with charts and graphs.
- Generate hypotheses about what patterns might exist.

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("customers.csv")
print(df.describe())          # Summary statistics
df["age"].hist()              # Distribution of customer ages
plt.show()
```

---

#### **Stage 5: Feature Engineering**

- Transform raw data into features that are useful for a model.
- Combine, encode, or create new variables.
- Example: From a "signup date," derive "days since signup," "signup month," or "is weekend signup."

---

#### **Stage 6: Modeling (optional, when prediction is needed)**

- Choose and train a Machine Learning model.
- This is where DS and ML overlap.
- Not every data science project needs a model — sometimes the insight from EDA is enough.

---

#### **Stage 7: Evaluation**

- Test the model or analysis on unseen data.
- Measure if it answers the original question.
- Use domain knowledge to sanity-check results.

---

#### **Stage 8: Communication & Deployment**

- Share findings with stakeholders (reports, dashboards, presentations).
- If a model is involved, deploy it to production.
- Monitor performance over time.

> The best insight in the world has zero value if no one understands or acts on it.

---

## Core Tools of a Data Scientist

### Programming Languages

| **Language** | **Why It's Used**                                     |
| ------------ | ----------------------------------------------------- |
| Python       | The most popular language for DS and ML               |
| R            | Widely used in academia and statistics                |
| SQL          | Essential for querying databases                      |

---

### Key Python Libraries

| **Library**    | **Purpose**                                      |
| -------------- | ------------------------------------------------ |
| `numpy`        | Numerical computing, arrays, math operations     |
| `pandas`       | Data manipulation and analysis (DataFrames)      |
| `matplotlib`   | Basic plotting and visualization                 |
| `seaborn`      | Statistical data visualization                   |
| `scikit-learn` | Machine Learning models and utilities            |
| `jupyter`      | Interactive notebooks for exploration            |

> See the **Setup Guide** ([`00-tools-and-setup.md`](00-tools-and-setup.md)) for installation and your first notebook.

---

### A First Look at the Workflow in Python

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales_data.csv")

# Inspect the data
print(df.shape)        # (rows, columns)
print(df.head())       # First 5 rows
print(df.isnull().sum()) # Count missing values

# Explore a numeric column
print(df["revenue"].describe())

# Visualize
df["revenue"].plot(kind="hist", title="Revenue Distribution")
plt.show()
```

This is the starting point of nearly every real data science project.

---

## What Does a Data Scientist Actually Do?

### Typical Day-to-Day Tasks

- Write queries to extract data from databases.
- Clean and transform messy datasets.
- Build visualizations to explore trends.
- Present findings to non-technical stakeholders.
- Train and evaluate predictive models.
- Collaborate with engineers to deploy solutions.

### Skills Required

- **Technical**: Python/SQL, statistics, data visualization, ML basics.
- **Analytical**: Critical thinking, pattern recognition, problem framing.
- **Communication**: Explaining findings clearly to non-technical audiences.

---

## Summary

- Data Science is the end-to-end process of extracting insight from data — using statistics, programming, and domain knowledge.
- It overlaps with AI and ML but is broader: not every project needs a model.
- The lifecycle: Define → Collect → Clean → Explore → Model → Evaluate → Communicate.
- Python (with pandas, numpy, matplotlib, scikit-learn) is the primary toolkit.
- The most underestimated skill: **communicating results** clearly.

---

*End of Lesson 1*

---
