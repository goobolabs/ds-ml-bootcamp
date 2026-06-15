# Data Science & Machine Learning Study Notes

---

## Table of Contents

1. [Definitions](#1-definitions)
2. [Data Science Lifecycle](#2-data-science-lifecycle)
3. [Supervised vs Unsupervised Learning](#3-supervised-vs-unsupervised-learning)
4. [Overfitting & Underfitting](#4-overfitting--underfitting)
5. [Training Data & Test Data](#5-training-data--test-data)
6. [Case Study  ML in Healthcare](#6-case-study--ml-in-healthcare)

---

## 1. Definitions

### Data Science
The big field that studies data to find answers and help people make better decisions.

> **Analogy:** Data Science is the whole kitchen.

### Machine Learning
A branch of Artificial Intelligence that builds algorithms and models that learn patterns from data and make predictions without being explicitly programmed.

> **Analogy:** Machine Learning is one tool inside the kitchen.

### How They Relate
| | Data Science | Machine Learning |
|---|---|---|
| Scope | Broad field | One tool within DS |
| Goal | Understand data, find answers | Learn patterns, make predictions |
| Uses | Stats, charts, storytelling, ML | Algorithms, models, training data |

### Real-Life Example  Netflix Recommendations

| Step | Who Does It | What Happens |
|---|---|---|
| 1. Collect data | Data Science | Records what you watch, skip, and rate |
| 2. Clean the data | Data Science | Removes errors, fills missing values |
| 3. Train the model | Machine Learning | Finds pattern: *"Action fans also like Thrillers"* |
| 4. Make prediction | Machine Learning | Suggests 10 movies next time you open Netflix |
| 5. Check results | Data Science | Did users click? Did they watch? Measures success |

---

## 2. Data Science Lifecycle

ML fits in **Step 5**  after the data is clean and explored, before deployment.

```
1. Define the problem    →  What question are we answering?
2. Collect data          →  Surveys, logs, sensors, databases
3. Clean the data        →  Fix errors, fill gaps, remove duplicates
4. Explore the data      →  Charts, patterns, early insights
5. Build the model  ◄──  ML LIVES HERE
6. Evaluate the model    →  Test accuracy, fix errors, retrain
7. Deploy + Monitor      →  Ship to product. Watch it over time.
```

### Why ML fits in Step 5 specifically

- **Before Step 5**  data is messy. ML trained on bad data learns bad patterns.
- **After Step 5**   a human still needs to evaluate results and push the model live.

> ML is powerful. But it needs humans around it  before and after.

---

## 3. Supervised vs Unsupervised Learning

### Supervised Learning
You teach the computer with labeled data answers already included.

**Example — Fruit Sorting Machine:**
- Show computer 1,000 fruit photos: 500 labeled *"apple"*, 500 labeled *"orange"*
- Computer learns: *"Round + red = apple. Round + orange = orange."*
- New photo arrives → computer decides alone

### Unsupervised Learning
No answers given. The computer finds patterns on its own.

**Example — Students in a Classroom:**
- Computer watches 30 students with no labels
- Finds groups on its own:
  - *Group A: quiet, finishes work fast*
  - *Group B: talks a lot, needs help*
  - *Group C: works alone, takes longer*
- Nobody told it these groups exist. It discovered them.

### Comparison

| | Supervised | Unsupervised |
|---|---|---|
| Labels? | Yes | No |
| Knows the answer? | Yes, during training | Never |
| Goal | Predict | Discover |
| Example | Fruit sorter | Student groups |
| One-line summary | Student with answer key | Explorer with no map |

---

## 4. Overfitting & Underfitting

### Overfitting
Model studies too hard. Memorizes everything including noise and mistakes.

**Example:** Student memorizes 10 exam questions word for word. New exam arrives with different questions. Student fails knew too much about too little.

**Why it happens:**
- Too much training on too little data
- Model learns noise, not the real pattern
- Works perfectly on training data, falls apart on new data

**How to fix:**
- Add more training data
- Stop training earlier (before the model goes too deep)
- Remove irrelevant features
- Use a simpler model

---

### Underfitting
Model studies too little. Learns nothing useful.

**Example:** Student never opens the book. Guesses everything on the exam. Fails because they knew too little about everything.

**Why it happens:**
- Model is too simple for the problem
- Not enough training time
- Not enough useful features provided

**How to fix:**
- Train longer
- Provide better, more relevant features
- Use a more complex model

---

### Comparison

| | Overfitting | Underfitting |
|---|---|---|
| Learns? | Too much | Too little |
| Training result | Perfect | Poor |
| New data result | Terrible | Also poor |
| Fix | Less complexity, more data | More complexity, more training |

> **Cooking analogy:** Underfitting = raw food (not cooked enough). Overfitting = burnt food (cooked too long). Good model = cooked just right.

---

## 5. Training Data & Test Data

You have data. You split it in two.

| Split | Purpose | Analogy |
|---|---|---|
| Training data (80%) | Model learns patterns here | Student reads the book |
| Test data (20%) | Model is evaluated here never seen before | Surprise exam, book closed |

### Why Split?

If the model trains and tests on the **same data**, it just memorizes. Looks perfect. Means nothing.

Splitting gives you an **honest score**  how well it performs on data it has never seen.

> Training data teaches the model. Test data checks if it actually learned  or just memorized.

---

## 6. Case Study — ML in Healthcare

**Title:** *A Roadmap to Implementing Machine Learning in Healthcare: From Concept to Practice*
**Source:** Frontiers in Digital Health, 2025  PubMed / US National Library of Medicine
**Link:** https://pmc.ncbi.nlm.nih.gov/articles/PMC11788154/

### What They Did
Researchers at The Hospital for Sick Children (Toronto) launched a program called **PREDICT** in 2023. Goal: build and deploy ML models to help sick children using their hospital records.

### Real Problem Solved
Children receiving chemotherapy often suffer severe vomiting  one of the worst side effects of cancer treatment. Doctors frequently miss the best guidelines to prevent it.

**Solution:** An ML model flags high-risk patients early. Doctors receive an alert and give better anti-nausea medication before vomiting starts.

### What They Found
- Built a central data system with patient records in **18 clean tables** covering diagnoses, medications, lab results, and visit history
- This made it easy to train ML models across many hospital projects
- Models need ongoing monitoring  patient data changes over time, and old models can quietly get worse

### Lifecycle Coverage

| Lifecycle Stage | What They Did |
|---|---|
| Define problem | Which children are at high risk of vomiting from chemo? |
| Collect data | Hospital records  medications, lab results, visit history |
| Clean data | Built one clean, centralized database |
| Build model | ML trained on patient records to predict vomiting risk |
| Evaluate model | Silent trials  results tracked before going live |
| Deploy | Alerts sent to pharmacists with high-risk patient names |
| Monitor | Model checked nightly for prediction quality |


---

*Notes compiled from study sessions on Data Science and Machine Learning fundamentals.*