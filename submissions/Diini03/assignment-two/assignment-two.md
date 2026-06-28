# Assignment-two : Dataset Collection and Description

---

## Title & Collection Method

**Dataset Title:** Event Guest Registration & Attendance Dataset

**Collection Method:** Web Scraping / System Logging

This dataset was collected from a live event management web application I built and currently maintain. The system handles guest registration, event creation, and check-in tracking for various event types. I wrote a script to extract and export guest-level records from the system's backend, then anonymized the data by removing personal identifiers like names, emails, and phone numbers — replacing them with derived features like `name_length` and `email_domain` before those were later dropped as well.

The data reflects real user behavior: how guests register, when they register, what events they attend, and whether they actually show up. This makes it a realistic, self-collected dataset rather than a synthetic or pre-made one.

---

## Description of Features & Labels

| Column                       | Type        | Description                                                     |
| ---------------------------- | ----------- | --------------------------------------------------------------- |
| `guest_id`                   | String      | Unique identifier per guest (anonymized)                        |
| `event_category`             | Categorical | Type of event: Seminar, Workshop, Conference, Festival          |
| `name_length`                | Numeric     | Character length of the guest's name                            |
| `status`                     | Categorical | Registration status: registered, pending, invited, rejected     |
| `days_since_registration`    | Numeric     | Days between registration and the event date                    |
| `registration_hour`          | Numeric     | Hour of day when the guest registered (0–23)                    |
| `registration_weekday`       | Numeric     | Day of week when the guest registered (0=Monday, 6=Sunday)      |
| `ticket_price_usd`           | Numeric     | Price of the ticket in USD                                      |
| `num_events_attended_before` | Numeric     | How many previous events the guest attended                     |
| `registered_via_mobile`      | Binary      | 1 if registered from a mobile device, 0 if desktop              |
| `checked_in`                 | Binary      | **Label (y):** 1 if the guest checked in on event day, 0 if not |

**Features (X):** all columns except `guest_id` and `checked_in`

**Label (y):** `checked_in` — this is what we want to predict

---

## Dataset Structure

- **Rows:** 115
- **Columns:** 11
- **Label:** `checked_in` (binary: 0 or 1)

**Sample (first 8 rows):**

| guest_id | event_category | name_length | status     | days_since_reg | reg_hour | reg_weekday | ticket_price | prev_events | mobile | checked_in |
| -------- | -------------- | ----------- | ---------- | -------------- | -------- | ----------- | ------------ | ----------- | ------ | ---------- |
| G0001    | Seminar        | 0           | invited    | 213            | 15       | 6           | 10           | 5           | 1      | 0          |
| G0002    | Seminar        | 0           | invited    | 213            | 15       | 6           | 10           | 4           | 0      | 0          |
| G0003    | Seminar        | 0           | invited    | 213            | 15       | 6           | 1            | 0           | 0      | 0          |
| G0005    | Conference     | 5           | registered | 95             | 23       | 5           | 46           | 4           | 1      | 0          |
| G0006    | Seminar        | 7           | registered | 208            | 10       | 5           | 0            | 4           | 1      | 0          |
| G0007    | Workshop       | NaN         | registered | 85             | 20       | 1           | 9            | NaN         | 1      | 1          |
| G0008    | Seminar        | 4           | Registered | 207            | 10       | 5           | 14           | 3           | 0      | 0          |
| G0010    | Seminar        | 4           | pending    | 205            | 11       | 0           | 4            | 3           | 0      | 0          |

---

## Quality Issues

Even though this came from a structured system, a few issues exist — which is normal for any real scraped or exported dataset:

1. **Missing values** — `name_length` (5 nulls), `ticket_price_usd` (4 nulls), `num_events_attended_before` (6 nulls), `registration_hour` (2 nulls). These happened when the scraper missed a field or the user left it blank.

2. **Typo / inconsistent casing** — one row has `status = "Registered"` (capital R) instead of `"registered"`. Small inconsistency but breaks grouping and encoding.

3. **Outlier** — one row has `days_since_registration = 9999`, which is clearly a parsing bug from the system. No event is planned 27 years out.

4. **Class imbalance** — only 23 out of 115 guests actually checked in (about 20%). The label is imbalanced, which needs to be handled during modeling.

5. **Zero values in name_length** — several guests have `name_length = 0`, which likely means the name field was empty or not captured properly.

---

## Learning Type

This is a **supervised learning** problem.

We have a clear label — `checked_in` — which tells us exactly whether a guest showed up or not. The model learns from past records where the outcome is already known, then uses that to predict future guests.

More specifically, this is a **binary classification** task: the output is either 0 (did not check in) or 1 (checked in).

---

## Use Case

**Goal:** predict whether a registered guest will actually show up to an event.

This is useful for event organizers — if you know 40% of registered guests won't show up, you can oversell tickets, send targeted reminders, or adjust catering and seating.

**Algorithm candidates:**

- Logistic Regression (simple baseline)
- Random Forest Classifier (handles mixed feature types well)
- XGBoost (better with imbalanced data)

**Where it fits in the DS lifecycle:**

| Stage              | What happens                                               |
| ------------------ | ---------------------------------------------------------- |
| Problem Definition | Predict guest check-in from registration data              |
| Data Collection    | Exported from the live event management system             |
| Data Cleaning      | Fix casing, handle nulls, remove outlier                   |
| EDA                | Check distributions, correlations, class balance           |
| Modeling           | Train a classification model on historical guest data      |
| Evaluation         | Measure with F1-score and ROC-AUC (due to class imbalance) |
| Deployment         | Integrate predictions into the system dashboard            |
