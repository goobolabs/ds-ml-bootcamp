# Introduction to Data Science and Machine Learning
> Research Assignment - DSML - 2026 


---

**Course:** Introduction to Data Science and Machine Learning  
**Due:** Monday, June 15, 2026 at 12:00 PM (Africa/Mogadishu / EAT)  
**Sources:** 16 references — books, scholarly articles, and peer-reviewed papers                             
**Author:** Ali Omar Abdi - Alikey

---

## Table of Contents

1. [Q1 — What Are Data Science and Machine Learning?](#q1----what-are-data-science-and-machine-learning)
2. [Q2 — The Data Science Lifecycle](#q2----the-data-science-lifecycle)
3. [Q3 — Supervised vs. Unsupervised Learning](#q3----supervised-vs-unsupervised-learning)
4. [Q4 — Overfitting: Causes and Prevention](#q4----overfitting-causes-and-prevention)
5. [Q5 — Training and Test Data Split](#q5----training-and-test-data-split)
6. [Q6 — Case Study: ML in Healthcare](#q6----case-study-ml-in-healthcare)
7. [References](#references)

---

## Q1 — What Are Data Science and Machine Learning?

### What Is Data Science?

Every time you buy something online, search for a video, or tap your card at a shop, data is created. Data Science is the field that takes all that raw information and turns it into something useful — answers, patterns, and decisions that people and organizations can act on.

Think of a data scientist as a detective. They look at messy, scattered clues (data) and figure out what is really going on.

IBM (2025) describes Data Science as the field that "brings structure to big data" — it covers the full journey from collecting and cleaning data all the way to sharing the findings with decision-makers. It is not just one skill or tool; it is the whole process from start to finish.

### What Is Machine Learning?

Machine Learning (ML) is a type of Artificial Intelligence where a computer learns from examples instead of being told exactly what to do step by step.

Think of it this way: teaching a child to recognize cats. You do not write a list of rules like "has four legs, pointy ears, and whiskers." You just show them hundreds of pictures of cats and non-cats, and eventually they figure it out themselves. ML works the same way — but with data instead of pictures, and an algorithm instead of a child.

As Pangeanic (2023) puts it, ML uses algorithms that "extract data, learn from these data, and generate forecasts about future trends." The programmer does not write the rules. The algorithm learns them from the examples.

### How Are They Related?

Data Science and Machine Learning are not the same thing. ML is one tool used inside the bigger process of Data Science. Sartorius (2020) explains that "Data science is a field that incorporates some areas of AI, machine learning and deep learning, while having a specific focus of gaining insight from data."

A simple way to see the difference:

- **Data Science** = the full journey. Asking the right question, collecting and cleaning data, finding patterns, sometimes building a model, and explaining the results.
- **Machine Learning** = one step in that journey — the step where the computer learns to make predictions.

Not every Data Science project even uses ML. A data scientist might spend most of their time just cleaning and visualizing data, with no model at all. ML only comes in when you need the computer to learn patterns and make predictions on its own.

| | Data Science | Machine Learning |
|---|---|---|
| What it covers | The whole process | Just the learning/prediction step |
| Main goal | Turn data into useful insights | Build a model that predicts things |
| Tools used | Statistics, charts, SQL, sometimes ML | Algorithms like Decision Trees, Neural Networks |
| Final result | Reports, dashboards, or predictions | A trained model that scores new data |

### Real-Life Example: Catching Credit Card Fraud

Banks need to catch fraud instantly — millions of transactions happen every minute, and a human cannot check each one. This is where Data Science and Machine Learning work together.

**Data Science does the preparation work:**
- The bank collects years of transaction records (amounts, locations, times, merchant types)
- Data scientists clean the messy data — fixing missing values, removing duplicates, standardizing formats
- They create useful features. For example, a raw timestamp gets turned into "hour of day," "day of week," and "minutes since last purchase" — three pieces of information a model can actually learn from
- They explore the data: what does a normal purchase pattern look like? How are fraud cases different?

**Machine Learning does the detection:**
- A model (like a Random Forest) is trained on millions of past transactions, each labeled "fraud" or "not fraud"
- It learns which patterns are suspicious — for example, a large foreign transaction two minutes after a local one
- After training, the model checks every new transaction in milliseconds and decides whether to flag it

As Syracuse University's iSchool (2025) explains, "machine learning enhances the actual process of fraud detection by recognizing subtle patterns that might indicate suspicious behavior" — patterns too small and too fast for any human to catch.

Neither works alone. Without Data Science, there is no clean data for the model to learn from. Without Machine Learning, there is no way to check millions of transactions per day. They depend on each other.

| Step | Who Does It | What Happens |
|---|---|---|
| Collecting data | Data Science | Transaction records gathered from banking systems |
| Cleaning & feature creation | Data Science | Missing values fixed, useful columns created |
| Exploring patterns | Data Science | Normal vs. fraud spending patterns compared |
| Training the model | Machine Learning | Random Forest trained on labeled fraud/non-fraud data |
| Deploying the model | Both | Model plugged into the live payment system |
| Monitoring & updating | Both | Performance tracked, model retrained as fraud tactics change |

---

## Q2 — The Data Science Lifecycle

A Data Science project does not happen all at once. It follows a series of stages, from asking the first question all the way to putting a working solution in front of real users. The most widely used framework for this is called **CRISP-DM** — which stands for Cross-Industry Standard Process for Data Mining.

CRISP-DM was created in the late 1990s by a group of companies including Daimler-Benz and NCR, working with over 200 data practitioners. Excelsior University describes it as "the systematic framework for conducting successful data science projects." It has six stages, and they do not always go in a straight line — teams often loop back to earlier stages as they learn more.

```
Step 1: Business Understanding
           |
Step 2: Data Understanding
           |
Step 3: Data Preparation
           |
Step 4: Modeling  <-- Machine Learning enters HERE
           |
Step 5: Evaluation
           |
Step 6: Deployment
           |
     (loop back if needed)
```

### Step 1: Business Understanding — What Problem Are We Solving?

Before touching any data, the team must clearly define what they are trying to find out. What question needs answering? What decision will the results support?

Studocu's CRISP-DM guide identifies vague problem definitions as one of the most common reasons data science projects fail. If you do not know exactly what you are looking for, no amount of data analysis will help.

**Example:** "Can we predict which patients are likely to be readmitted to hospital within 30 days?"

### Step 2: Data Understanding — What Data Do We Have?

The team looks at what data is available and decides if it is good enough to answer the question. They check for quality problems, missing records, and whether the right variables are even being collected.

### Step 3: Data Preparation — Cleaning Up the Mess

This is usually the longest and most tedious stage. Real-world data is rarely clean. It has missing values, typos, duplicate rows, inconsistent formats, and outliers that do not make sense.

In this stage, data scientists clean and restructure the data so that an algorithm can actually use it. The IBM CRISP-DM documentation says this phase covers "all activities involved in familiarizing oneself with the data." Most practitioners estimate that this step takes 70 to 80 percent of the total project time.

### Step 4: Modeling — Where Machine Learning Comes In

Only after the data is clean and ready does the team bring in Machine Learning. They choose an algorithm, feed it the prepared data, and let it learn the patterns. As Studocu (2025) describes, "various modeling techniques depending on the problem statement are selected and applied, and their parameters are calibrated to find optimal modeling performance."

Common algorithm choices include Linear Regression, Decision Trees, Random Forests, and Neural Networks.

**Why does ML only enter here?** Because ML needs clean, well-organized data to work properly. Skipping the earlier steps and jumping straight to modeling produces bad, unreliable results.

### Step 5: Evaluation — Does It Actually Work?

The trained model is tested on data it has never seen before. The team checks whether it answers the original question and performs well enough for real use. Common measures include accuracy, precision, recall, and F1-score.

### Step 6: Deployment — Putting It to Work

Once the model passes evaluation, it is integrated into a real system — a website, an app, a hospital tool, or a bank's transaction processor. After deployment, the team continues monitoring it, because the real world changes over time in ways the training data did not capture. This gradual shift in data patterns is called **concept drift**.

---

## Q3 — Supervised vs. Unsupervised Learning

### Supervised Learning — Learning with a Teacher

In supervised learning, the model is trained on data that already has the correct answers attached. Each example has an input (the information) and a label (the correct answer). The model learns to connect the two, and can then predict answers for new examples it has never seen.

IBM (2025) explains that "the algorithm 'learns' from the training data set by iteratively making predictions on the data and adjusting for the correct answer."

There are two main types of supervised tasks:

- **Classification** — predicting a category. Is this email spam or not? Does this patient have diabetes?
- **Regression** — predicting a number. What will this house sell for? How many units will we sell next month?

**Simple example:** Imagine training a spam filter. You give it thousands of emails, each already marked as "spam" or "not spam." The model studies them, figures out which words and patterns appear in spam, and then uses that knowledge to sort new emails it has never seen before.

### Unsupervised Learning — Finding Patterns Alone

In unsupervised learning, the data has no labels. There are no correct answers provided. The algorithm has to find patterns and structure in the data entirely on its own.

AWS (2025) puts it this way: "unsupervised machine learning is when you give the algorithm input data without any labeled output data. Then, on its own, the algorithm identifies patterns and relationships in and between the data."

The two most common unsupervised tasks are:

- **Clustering** — grouping similar items together without being told what the groups should be
- **Dimensionality Reduction** — simplifying data that has too many variables, keeping only the most important information

**Simple example:** A supermarket has data on what every customer buys, but no categories for customers. An unsupervised clustering algorithm processes the data and finds natural groups on its own — for example: "budget shoppers who buy basics," "health-conscious shoppers," and "impulse buyers." The supermarket did not define these groups; the algorithm discovered them.

### Side-by-Side Comparison

| | Supervised Learning | Unsupervised Learning |
|---|---|---|
| Does the data have labels? | Yes — correct answers provided | No — algorithm finds patterns alone |
| How much human guidance? | High — someone must label the data | Lower during training |
| What is the goal? | Predict a known answer | Discover hidden groups or structure |
| What does it output? | A prediction or category | Clusters, associations, simplified data |
| How easy is it to evaluate? | Straightforward — compare predictions to correct answers | Harder — no "right answer" to check against |
| Common algorithms | Linear Regression, SVM, Neural Networks | K-Means, DBSCAN, PCA |
| Everyday examples | Spam filter, disease diagnosis, house price prediction | Customer segmentation, anomaly detection, topic grouping |

---

## Q4 — Overfitting: Causes and Prevention

### What Is Overfitting?

Imagine a student who memorizes every answer from last year's exam instead of actually understanding the subject. They do brilliantly on that exact exam — but fail completely when the questions change slightly. That is overfitting.

In machine learning, overfitting happens when a model learns the training data too well — including all its noise, quirks, and random errors — instead of learning the general pattern. It performs nearly perfectly on training data but fails on new data it has never seen.

Lightly.ai (2024) describes it simply: "instead of capturing the underlying patterns, the model memorizes the data, leading to poor generalization." The clearest warning sign is when training accuracy is very high but test accuracy is much lower.

### The Bias-Variance Tradeoff

This concept helps explain the balance every model needs to find:

- **Too simple (High Bias / Underfitting)** — The model misses real patterns. Like drawing a straight line through data that clearly curves. It performs badly on both training and test data.
- **Too complex (High Variance / Overfitting)** — The model memorizes noise. Like a wiggly line that passes through every single training point perfectly but makes no sense for new points.

Aya Data (2025) explains it clearly: "High Variance (Overfitting): The model is complex and highly sensitive to the training data, leading to low training error but high test error."

The goal is to find the sweet spot — complex enough to learn real patterns, simple enough to generalize to new data.

### What Causes Overfitting?

| Cause | Plain-English Explanation |
|---|---|
| Model is too complex | Too many adjustable parts relative to how much data you have |
| Not enough training data | Too few examples to learn from — the model just memorizes what it saw |
| Too many training rounds | The model keeps adjusting until it has memorized every example |
| Irrelevant features in the data | Useless columns confuse the model and teach it patterns that do not hold in the real world |
| No limits on the model | Without any constraints, the model is free to get as complicated as it wants |

### How to Prevent It

**1. Get more training data.**
More examples make it much harder for the model to memorize individual cases and force it to learn general rules.

**2. Use regularization (L1 or L2).**
This adds a small penalty to the model every time it gets too complicated, keeping it from growing beyond what the data justifies. Jaro Education (2025) confirms that "increasing regularisation strength lowers variance by preventing overfitting."

**3. Use cross-validation.**
Instead of testing on one fixed test set, the data is split into several parts and the model is tested on each part in turn. This gives a more honest picture of real performance.

**4. Stop training early.**
Watch the model's performance on a separate validation set while training. As soon as performance stops improving, stop — do not give the model more chances to memorize.

**5. Use a simpler model.**
If a simple model gives similar results to a complex one, choose the simple one. Unnecessary complexity almost always leads to overfitting.

**6. Use dropout (for neural networks).**
During training, some neurons are randomly switched off at each step. This stops the network from becoming too dependent on any single path through the data, making it more robust overall.

---

## Q5 — Training and Test Data Split

### The Basic Idea

Before training a model, you divide your dataset into separate parts. The most important rule is this: **the model should never be tested on the same data it was trained on.**

Why? Because a model that is evaluated on its own training data will almost always look great — even if it has just memorized the examples rather than learned anything useful. That is overfitting, and it gives you a completely false sense of how the model will perform in the real world.

The three standard subsets are:

- **Training Set** — What the model learns from. All the adjustments happen based on this data.
- **Test Set** — Data the model never sees until the very end. Used once to measure real performance.
- **Validation Set** — Used during development to fine-tune settings without touching the test set.

### Common Ways to Split the Data

| Split Type | Training | Validation | Test |
|---|---|---|---|
| Simple 80/20 | 80% | — | 20% |
| Three-way 70/15/15 | 70% | 15% | 15% |
| Large dataset 80/10/10 | 80% | 10% | 10% |

A study published in PMC (National Institutes of Health, 2024) tested split ratios from 60:40 all the way to 95:05 on medical imaging data. The researchers found "significant variations in accuracies across these ratios, emphasizing the critical need to strike a balance to avoid overfitting or underfitting." There is no single correct ratio — it depends on how much data you have and how complex the problem is.

### Two Important Rules

**Shuffle before you split.**
If your data is ordered by time or any other sequence, taking the first 80% as training data gives you a biased split. Always shuffle the data randomly before dividing it, so both sets represent the full range of examples.

**Use stratified sampling when classes are unbalanced.**
If only 2% of your records are fraud cases, a random split might give the test set almost no fraud examples at all. Stratified sampling makes sure the same proportion of each class appears in both the training and test sets.

### Why Does This Matter?

Encord (2026) puts it directly: "splitting data helps prevent overfitting and ensures the model generalizes well... this creates a more robust and versatile model for real-world use."

Think of the test set as a mock exam. The student (the model) studies from the training material. The test is the first time they see the exam questions. If the student passes, you have real evidence they understood the subject — not just that they memorized the study materials.

The test set represents the future: data the model will meet after it is deployed, that it has never processed before.

---

## Q6 — Case Study: ML in Healthcare

**Source:** Iparraguirre-Villanueva, O., Espinola-Linares, K., Flores Castaneda, R. O., and Cabanillas-Carbonell, M. (2023). Application of Machine Learning Models for Early Detection and Accurate Classification of Type 2 Diabetes. *Diagnostics*, 13(14), 2383. https://doi.org/10.3390/diagnostics13142383

### Background: Why This Matters

Type 2 diabetes is one of the most common long-term illnesses in the world. By 2021, around 537 million adults were living with it. The International Diabetes Federation estimated that number will rise to 643 million by 2030 and 784 million by 2045.

The problem with diabetes is that by the time people notice symptoms, damage to the kidneys, nerves, and eyes may already be happening. Catching it early makes a significant difference. But standard diagnosis requires lab tests and a doctor's time — expensive and not always accessible.

This study asked a simple question: can a machine learning model detect diabetes early using basic clinical measurements that are already easy to collect?

### What the Researchers Did

They used the **Pima Indian Diabetes Dataset** — 768 patient records, each with eight simple health measurements:

- Number of pregnancies
- Blood glucose level
- Blood pressure
- Skin thickness
- Insulin level
- BMI (body mass index)
- Diabetes pedigree function (a measure of family history)
- Age

Each patient was labeled as **diabetic (1)** or **non-diabetic (0)**. Five supervised ML models were trained and compared:

| # | Algorithm | What It Does Simply |
|---|---|---|
| 1 | K-Nearest Neighbors (K-NN) | Finds the most similar past patients and uses their diagnosis |
| 2 | Bernoulli Naive Bayes (BNB) | Uses probability to classify based on features |
| 3 | Decision Tree (DT) | Asks a series of yes/no questions to reach a conclusion |
| 4 | Logistic Regression (LR) | Calculates the probability of belonging to each class |
| 5 | Support Vector Machine (SVM) | Draws the best boundary line between diabetic and non-diabetic cases |

Each model was tested on data it had not seen during training, using four measures: accuracy, precision, recall, and F1-score.

### What They Found

All five models were able to predict diabetes risk from routine clinical data with meaningful accuracy. The **Support Vector Machine (SVM)** came out on top. The researchers concluded that ML models trained on basic health information can reliably support early diabetes detection and could be used as a tool to help doctors make faster decisions.

### Where Does This Fit in the Data Science Lifecycle?

This study follows all six CRISP-DM stages:

| Lifecycle Stage | What the Study Did |
|---|---|
| Business Understanding | Goal: detect Type 2 diabetes early to reduce complications |
| Data Understanding | Explored 768 patient records with 8 clinical features |
| Data Preparation | Cleaned missing values, normalized measurements for each algorithm |
| Modeling | Trained 5 supervised ML classifiers and tuned their settings |
| Evaluation | Compared all models using accuracy, precision, recall, and F1-score |
| Deployment (proposed) | Recommended the best model as a clinical decision-support tool |

The data pipeline — collection, cleaning, and feature preparation — is the Data Science part. The five classification algorithms are the Machine Learning part. Together, they show exactly how the two fields work side by side to solve a real healthcare problem.

---

## References

1. Sartorius. (2020). *Understanding the relationship between Data Science, Artificial Intelligence and Machine Learning*. https://www.sartorius.com/en/knowledge/science-snippets/data-science-vs-artificial-intelligence-vs-machine-learning-602514

2. Pangeanic. (2023). *The relationship between data science and machine learning*. https://blog.pangeanic.com/trelationship-between-data-science-and-machine-learning

3. IBM. (2025). *Data science vs. machine learning: What's the difference?* https://www.ibm.com/think/topics/data-science-vs-machine-learning

4. Syracuse University iSchool. (2025). *Data Science vs. Machine Learning: Key differences explained*. https://ischool.syracuse.edu/data-science-vs-machine-learning/

5. Excelsior University. (n.d.). *Chapter 1.4: The Data Science Lifecycle (CRISP-DM)*. https://express.excelsior.edu/datascience/chapter/1-4-the-data-science-lifecycle-crisp-dm/

6. Melo, G. (2024). *CRISP-DM: A comprehensive guide to the structured Data Science methodology*. Medium. https://medium.com/@gcesarmelo7/crisp-dm

7. Studocu. (2025). *CRISP-DM Model Lifecycle: Steps, challenges, and best practices*. https://www.studocu.com

8. IBM. (2025). *Supervised vs. unsupervised learning: What's the difference?* https://www.ibm.com/think/topics/supervised-vs-unsupervised-learning

9. AWS. (2025). *Supervised vs unsupervised learning: Difference between machine learning algorithms*. https://aws.amazon.com/compare/the-difference-between-machine-learning-supervised-and-unsupervised/

10. Lightly.ai. (2024). *Overfitting in machine learning: Causes, detection, and prevention*. https://www.lightly.ai/blog/overfitting

11. Aya Data. (2025). *Underfitting vs. overfitting in machine learning: A complete 2025 guide*. https://www.ayadata.ai/a-guide-to-overfitting-and-underfitting-in-machine-learning/

12. Jaro Education. (2025). *Bias-variance tradeoff in machine learning explained with examples*. https://www.jaroeducation.com/blog/bias-variance-tradeoff-in-machine-learning

13. EMB Global. (2024). *Train and test data: Best practices for machine learning*. https://blog.emb.global/train-and-test-data/

14. Encord. (2026). *How to split machine learning datasets: Training, validation and test sets*. https://encord.com/blog/train-val-test-split/

15. Alnuaimi, N., Dermawan, D., Kamaruzaman, H. F., and Alotaiq, N. (2024). *Trade-off between training and testing ratio in machine learning for medical image processing*. PMC / National Institutes of Health. https://pmc.ncbi.nlm.nih.gov/articles/PMC11419616/

16. Iparraguirre-Villanueva, O., Espinola-Linares, K., Flores Castaneda, R. O., and Cabanillas-Carbonell, M. (2023). Application of machine learning models for early detection and accurate classification of type 2 diabetes. *Diagnostics*, 13(14), 2383. https://doi.org/10.3390/diagnostics13142383

---
