# Data Preprocessing Pipeline - Reflection

## Assignment 3: Car Price Data Preprocessing

### Overview
This document explains the key decisions made during the preprocessing pipeline for the raw car dataset.

---

### Step 2: Clean Target Formatting (Price)

**Decision:** Remove currency symbols ($) and convert to numeric float.

**Why:** The Price column contained mixed formats - some values had "$" prefix (e.g., "$1500") while others were plain numbers (e.g., "4171.0"). Machine learning models require numeric input, so all currency symbols were stripped using string replacement.

**How to apply:** Use `.replace('$', '').replace(',', '')` to clean currency strings, then convert to float with `float()`.

---

### Step 3: Fix Category Errors (Location)

**Decision:** Normalize Location text, fix typos ("Subrb" → "Suburb"), and convert unknowns ("??") to missing values.

**Why:** The raw data contained:
- Typos: "Subrb" instead of "Suburb"
- Unknowns: "??" indicating missing/unknown values
- Inconsistent casing

**How to apply:** Created a cleaning function that:
1. Converts to title case for standardization
2. Maps known typos to correct values
3. Converts invalid entries to NaN for proper imputation later

---

### Step 4: Impute Missing Values

**Justification for each column:**

| Column | Method | Why |
|--------|--------|-----|
| Odometer_km | Median | Robust to outliers; odometer readings can have extreme values |
| Doors | Mode | Categorical-like discrete values; most common is 4 doors |
| Accidents | Mode | Discrete count; most common is 0 accidents |
| Location | Mode | Categorical; City is most frequent in this dataset |

**Why median over mean for Odometer_km:** The data contained outliers (very high mileage cars). Median is robust to extreme values and better represents the "typical" odometer reading.

**Why mode for categorical-like columns:** Doors and Accidents are discrete values where mode makes sense as the most representative value.

---

### Step 6: Outliers (IQR Capping)

**Decision:** Use IQR (Interquartile Range) capping method for Price and Odometer_km.

**Why IQR Capping:**
- Preserves more data than removal
- Less sensitive to extreme outliers than Z-score
- Capping (clipping) keeps all observations while limiting extreme values

**How it works:**
- Q1 = 25th percentile, Q3 = 75th percentile
- IQR = Q3 - Q1
- Lower bound = Q1 - 1.5 × IQR
- Upper bound = Q3 + 1.5 × IQR
- Values outside bounds are clipped to the nearest bound

**Results:** 13 Price values and 2 Odometer_km values were capped.

---

### Step 7: One-Hot Encoding

**Decision:** Encode Location as binary (0/1) dummy columns.

**Why one-hot encoding:**
- Machine learning algorithms cannot work with categorical string data directly
- One-hot encoding creates binary indicators for each category
- Avoids imposing ordinal relationships between categories

**Result:** Created 14 Location dummy columns including City, Suburb, Rural, and some year values that got mixed in the original data.

---

### Step 8: Feature Engineering

**Four engineered features:**

1. **CarAge** = 2026 - Year
   - Why: Car age is often a strong predictor of price
   - More meaningful than raw Year for modeling

2. **Km_per_year** = Odometer_km / CarAge
   - Why: Annual usage intensity may correlate with condition
   - Note: Used `.replace(0, 1)` to avoid division by zero

3. **Is_Urban** = 1 if Location = 'City', else 0
   - Why: Urban vs rural location may affect car value/usage
   - Simple binary feature derived from Location

4. **LogPrice** = log(Price + 1)
   - Why: Alternative target variable for modeling
   - Log transformation can help with skewed price distributions
   - NOT used as a feature (it's the target variable)

---

### Step 9: Feature Scaling

**Decision:** Standardize continuous features (Odometer_km, CarAge, Km_per_year) using StandardScaler.

**Why scaling:**
- Many ML algorithms (regression, neural networks, SVM) benefit from standardized inputs
- Features with different scales can dominate the model
- StandardScaler transforms to mean=0, std=1

**What was NOT scaled:**
- Price and LogPrice: These are target variables, not features
- Dummy (0/1) columns: Already binary, no scaling needed

---

### Summary of Key Decisions

1. **Median imputation** for continuous (robust to outliers)
2. **Mode imputation** for categorical/discrete
3. **IQR capping** for outlier handling (preserves data while limiting extremes)
4. **One-hot encoding** for categorical variables
5. **Feature engineering** to create meaningful predictors
6. **Standardization** only on continuous features, not targets or dummies

These decisions balance data quality, model performance, and reproducibility.