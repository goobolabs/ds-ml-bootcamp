# Practical Assignment: Data Preprocessing Pipeline

**Due:** Wednesday, June 24, 2026 — 12:00 PM (Africa/Mogadishu / EAT)

**Goal:** Build a clean, reproducible preprocessing pipeline on a messy tabular dataset, applying the cleaning, encoding, scaling, and feature engineering techniques from Lesson 3.

## Instructions

- **Dataset (required):** Use the Car Price dataset — **dataset/raw_car_dataset.csv**.
- The file intentionally includes missing values, typos, outliers, and duplicates.
- Columns: Price (mixed numeric and currency strings), Odometer_km, Doors, Accidents, Location (City/Suburb/Rural plus typos/unknowns), Year.
- You may use AI **only for advice and concept clarification** (e.g., "What is IQR capping?", "When should I use mode imputation?").
- **Do not use AI to generate code or full solutions.** All implementation must be written by **you**.

---

## Task

Follow these ten steps, with a brief print checkpoint after each.

1. **Load & Inspect**

   - Show head(10), shape, info, missing counts, and Location value counts.
   - Note the key issues you find.

2. **Clean Target Formatting (Price)**

   - Remove currency symbols and commas; ensure the column is numeric.
   - Report the dtype and skewness.

3. **Fix Category Errors before Imputation**

   - Normalize Location text and map typos (e.g., Subrb → Suburb).
   - Convert unknowns (e.g., "??") to missing, then recount including missing.

4. **Impute Missing Values (justify choices)**

   - Odometer_km → median; Doors/Accidents → mode; Location → mode.
   - Confirm post-imputation missing counts.

5. **Remove Duplicates**

   - Report shape before/after and the number of rows removed.

6. **Outliers (IQR capping)**

   - Compute bounds and clip for Price and Odometer_km.
   - Show a short summary after capping.

7. **One-Hot Encode Categorical(s)**

   - Encode Location as 0/1 columns and list the new columns created.

8. **Feature Engineering (no leakage)**

   - Add at least three sensible features (e.g., CarAge, Km_per_year with safe handling, Is_Urban).
   - Add **LogPrice = log(Price + 1)** as an alternative target (not a feature).

9. **Feature Scaling (X only)**

   - Standardize continuous features; do **not** scale Price or LogPrice.
   - Prefer leaving 0/1 dummies unscaled; show a small sample of scaled values.

10. **Final Checks & Save**

    - Show final info, missing counts (all zero), and a small describe table.
    - Save the result to **clean_car_dataset.csv**.

---

## Deliverables

- **Script:** `car_preprocess.py` implementing Steps 1–10 with clear print checkpoints.
- **Cleaned data:** `clean_car_dataset.csv`.
- **Reflection:** `reflection.md` (≤ 1 page) explaining your decisions for each major step (why median vs mode, why IQR capping, which features you engineered and why).
- **requirements.txt** with the exact package versions you used.

---

## Sanity checks (recommended as assertions)

- Price is float; LogPrice exists and is numeric.
- No missing values remain at the end.
- At least one Location_* dummy column exists.
- Scaled columns have mean ≈ 0 and population std ≈ 1.

---
