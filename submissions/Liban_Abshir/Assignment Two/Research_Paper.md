# Study Habits and Midterm Performance Among University Classmates

**Student:** Liban Abshir  
**Course:** Data Foundations for Machine Learning  
**Date:** June 2026

---

## Title and Collection Method

For this assignment I built a small dataset about how my classmates study and how they did on our recent Data Structures midterm. I wanted something I could actually collect myself without downloading from Kaggle or UCI, so I went with a short survey.

I sent a Google Form link to a WhatsApp group of CS students at my university (around 60 people in the group). The form asked seven questions and I left it open for five days, from June 10 to June 14, 2026. Most responses came in the first two days; a few people filled it late. I told everyone answers would stay anonymous and I only needed honest estimates — no need to be exact to the minute.

In total I got 56 responses saved in `study_habits_dataset.csv`. One person accidentally submitted twice (same answers both times), which I kept on purpose because real data is never perfectly clean.

---

## Description of Features and Labels

**Features (input variables, X):**

| Feature | Description |
|---------|-------------|
| `respondent_id` | Anonymous code (R01, R02, …) — not used for modeling, just for tracking |
| `hours_studied_daily` | Average hours spent studying per day during the two weeks before the midterm |
| `sleep_hours` | Average hours of sleep per night in the same period |
| `caffeine_cups` | Daily cups of coffee or tea while studying |
| `study_location` | Main place they study: home, library, hostel, or cafe |
| `phone_screen_hours` | Rough daily phone/social media use in hours |

**Label (output variable, y):**

| Label | Description |
|-------|-------------|
| `midterm_score` | Score out of 100 on the Data Structures midterm (continuous numeric value) |

The label is something we already know from the exam — it is recorded data, not something we are trying to discover from scratch. That matters when we classify the learning type below.

---

## Dataset Structure

The dataset has **56 rows** (including one duplicate submission) and **7 columns** (6 usable features plus the label; `respondent_id` is an identifier only).

Below is a sample of 8 rows from the file:

| respondent_id | hours_studied_daily | sleep_hours | caffeine_cups | study_location | phone_screen_hours | midterm_score |
|---------------|---------------------|-------------|---------------|----------------|--------------------|---------------|
| R01 | 2 | 6 | 1 | home | 4.5 | 58 |
| R03 | 3-4 | 5.5 | | libary | 6 | 65 |
| R07 | 6 | 5 | 4 | library | 1.5 | 88 |
| R08 | 2 | 7 | 1 | hom | 4 | 55 |
| R11 | 7 | 4 | 5 | cafe | 2 | 92 |
| R14 | 1 | 9 | 0 | home | 8 | 38 |
| R21 | 8 | 4 | 6 | cafe | 1.5 | 95 |
| R19 | 4 | 6 | 2 | library | 3.8 | 73 |

Most numeric fields are decimals or whole numbers. `study_location` is text/categorical. A few cells are empty or use ranges instead of single numbers.

---

## Quality Issues

This dataset is messy in several ways, which is expected from a self-reported survey:

1. **Missing values** — Some people skipped questions. For example, `caffeine_cups` is blank for R03 and R44, and `sleep_hours` is missing for R06 and R29.

2. **Typos and inconsistent text** — `study_location` has spelling mistakes (`libary`, `hom`) and mixed capitalization (`Library`, `Hostel`, `hostel`). These need standardization before encoding.

3. **Mixed formats** — R03 wrote `3-4` for study hours instead of one number. That cannot go directly into a model without splitting or taking a midpoint.

4. **Duplicate row** — R19 appears twice with identical values. I need to drop one copy during cleaning.

5. **Possible outliers** — R21 reported 8 hours of daily study and R14 reported 9 hours of sleep with only 1 hour of study. They might be true or exaggerated; worth checking in preprocessing.

6. **Self-report bias** — People tend to round numbers and may under-report phone time. This is a data quality issue we cannot fully fix, only be aware of.

7. **Small sample** — 56 rows is enough for this assignment but not large enough for a production ML system. More responses would help.

These issues are exactly what Lesson 3 preprocessing is for: imputation, encoding categories, handling duplicates, and maybe scaling numeric columns.

---

## Learning Type: Supervised

This is a **supervised learning** problem.

Reason: we have a clear target variable `midterm_score` (y) paired with each row of features (X). In Lesson 2 terms, the model would learn the mapping from study habits → exam score using labeled examples. We are not grouping students without a target or searching for hidden structure alone.

More specifically:

- **Regression** — Predict the exact score (0–100) from habits. This fits best because the label is continuous.
- **Classification (optional)** — We could bin scores into Pass/Fail (e.g., ≥ 50 = pass) and treat it as binary classification, but the natural label here is numeric.

It is **not** unsupervised because we are not asking “what groups exist?” without labels. Clustering students by location alone, with no exam score, would be unsupervised — but that is not the main question I care about for this project.

---

## Use Case and Data Science Lifecycle

**Machine learning use:** A simple linear regression or random forest could predict midterm score from the habit features. That could help answer whether sleep, phone time, or study location seems associated with performance — useful for academic advising or personal planning, though causation would need more careful study.

**Where it fits in the lifecycle (Lesson 1):**

1. **Problem definition** — Can we predict exam performance from self-reported study behavior?
2. **Data collection** — This assignment; survey via Google Form.
3. **Data preparation** — Next step in Lesson 3: fix typos, encode `study_location`, handle missing values, remove duplicate, maybe normalize hours.
4. **Exploration / modeling** — Train/test split, fit regression, check errors.
5. **Evaluation & deployment** — Compare models, interpret which features matter; “deployment” here might just mean sharing findings with classmates, not a live app.

The dataset sits early in the lifecycle: we have raw observational data with known quality problems, and preprocessing must happen before any reliable model.

---

## Files Submitted

- `study_habits_dataset.csv` — Raw collected data (56 rows × 7 columns)
- `Research_Paper.md` — This document
