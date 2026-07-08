# Reflection — Car Price Preprocessing (Lesson 3)

**Liban Abshir**

---

### Step 1 — Load & Inspect

When I first loaded the data, the main problems were obvious: Price wasn't numeric (had `$` and commas), Location had spelling mistakes like "Subrb" and "??", and there were gaps in Odometer, Doors, Accidents, and Year. I also expected duplicates since the assignment said they're in there on purpose.

### Step 2 — Price Cleaning

I stripped `$` and commas then converted to float. Skewness was positive, which makes sense for car prices — most cars cluster at lower/mid range with a few expensive ones pulling the tail right. That later motivated using LogPrice as an alternative target.

### Step 3 — Location Normalization

I fixed typos *before* imputation because filling missing Location with mode while "Subrb" still existed would treat it as a separate category. I lowercased and trimmed text, mapped known typos to City/Suburb/Rural, and turned "??" and blanks into NaN.

### Step 4 — Imputation

| Column | Method | Why |
|--------|--------|-----|
| Odometer_km | Median | Continuous, often skewed — median is robust |
| Doors, Accidents | Mode | Small integer counts, mode = most typical value |
| Location | Mode | Categorical, no natural "average" |
| Year, Price | Median | Needed complete rows; median avoids outlier pull |

### Step 5 — Duplicates

Removed exact duplicate rows after cleaning so imputed values wouldn't hide repeated listings.

### Step 6 — IQR Capping

Used 1.5×IQR rule on Price and Odometer_km. I chose **capping** over dropping rows because we still want sample size for modeling — extreme values get pulled to the fence instead of deleted. Price had obvious entry errors (e.g. $850k) that would wreck a regression.

### Step 7 — One-Hot Encoding

Location became binary columns (`Location_City`, `Location_Suburb`, `Location_Rural`). One-hot avoids implying an order (Rural < Suburb < City).

### Step 8 — Feature Engineering

- **CarAge** — older cars usually cheaper; simple and interpretable.
- **Km_per_year** — usage intensity; divided by CarAge with zero-safe handling (replace 0 with 1).
- **Is_Urban** — City + Suburb vs Rural; captures demand/price differences.
- **LogPrice** — log(Price+1) as alternative **target** only, not fed into X (no leakage).

### Step 9 — Scaling

Standardized continuous predictors (z-score, population std). Left **Price**, **LogPrice**, **Is_Urban**, and Location dummies unscaled — dummies are already 0/1, and targets shouldn't be scaled for interpretation.

### Step 10 — Final Output

Zero missing values, assertions passed (float Price, numeric LogPrice, Location dummies exist, scaled cols ≈ mean 0 / std 1). Saved to `car_l3_clean_ready.csv` and `clean_car_dataset.csv`.
