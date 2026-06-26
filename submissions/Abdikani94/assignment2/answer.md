
# Mogadishu Mobile Data Bundle Price Dataset

**Course:** Data Foundations for Machine Learning  
**Assignment:** Practical Assignment  Lessons 1-3  
**Student:** Abdi Kani  Mohamed
**Date:** June 20, 2026

---

## 1. Title & Collection Method

**Dataset:** Retail prices of mobile internet data bundles sold by Somali's four telecom providers  Hormuud, Telesom, Somtel, and Golis.

Somalia runs mostly on USD for telecom payments. There is no public database comparing bundle prices across providers, so I collected this myself over four days (June 17–20, 2026).

**How I collected it:**

- **Mobile apps** Hormuud EVC Plus and Telesom's app both list live bundle catalogs. I opened each one, went through every bundle category (daily, weekly, monthly), and typed the values into a spreadsheet.
- **USSD menus**  Dialed `*712#` (Hormuud), `*388#` (Telesom), `*700#` (Somtel), `*600#` (Golis). Each code pulls up a menu of current bundles with prices. Wrote them down as I went.
- **Provider websites**  Telesom.net and Golis.so have pricing pages. Used Python (`requests` + `BeautifulSoup`) to scrape the tables where they existed.
- **In-store visit**  Walked into one agent shop per provider to check printed tariff sheets. Caught one Golis weekly bundle that wasn't showing correctly in the app yet.

Final count: **55 rows, 14 columns.**

---

## 2. Features & Labels

The dataset has one label `y` and 12 features `X`. One column (`bundle_id`) is just an identifier.

| Feature | Type | Description | Role |
|---|---|---|---|
| `bundle_id` | Integer | Row identifier | ID only |
| `provider` | Categorical | Telecom company (Hormuud, Telesom, Somtel, Golis) | Feature X |
| `bundle_type` | Categorical | Daily, Weekly, or Monthly | Feature X |
| `data_gb` | Numeric | Data allowance in GB | Feature X |
| `validity_days` | Numeric | How many days the bundle lasts | Feature X |
| `price_usd` | Numeric | Price in US Dollars | **Label y** |
| `network_gen` | Categorical | 3G or 4G | Feature X |
| `data_speed_mbps` | Numeric | Advertised download speed | Feature X |
| `bonus_gb` | Numeric | Extra data added on purchase | Feature X |
| `purchase_method` | Categorical | App or USSD | Feature X |
| `user_rating` | Numeric | Average customer rating (1–5) | Feature X |
| `active_sub_k` | Numeric | Provider's active subscribers in thousands | Feature X |
| `auto_renew` | Binary | Whether the bundle auto-renews (Yes/No) | Feature X |
| `price_per_gb` | Numeric | Derived: `price_usd / data_gb` | Derived feature X |

**The label is `price_usd`.** The ML task is to predict the price of a bundle from its specs and provider info.

`price_per_gb` is not a raw measurement  I calculated it from the other columns. It's kept because it makes the per-unit cost visible and should help any clustering task.

---

## 3. Dataset Structure

- **Rows:** 55
- **Columns:** 14
- **Providers:** Hormuud (14 bundles), Telesom (12), Somtel (10), Golis (10), mixed rows (9)

### Sample — 10 rows

| bundle_id | provider | bundle_type | data_gb | validity_days | price_usd | network_gen | data_speed_mbps | bonus_gb | purchase_method | user_rating | active_sub_k | auto_renew | price_per_gb |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Hormuud | Monthly | 10 | 30 | 5.00 | 4G | 25 | 1 | App | 4.6 | 850 | Yes | 0.50 |
| 2 | Hormuud | Monthly | 50 | 30 | 15.00 | 4G | 30 | 5 | App | 4.8 | 850 | Yes | 0.30 |
| 3 | Telesom | Weekly | 5 | 7 | 2.50 | 4G | 20 | 0.3 | App | 4.3 | 620 | Yes | 0.50 |
| 4 | Telesom | Monthly | 100 | 30 | 30.00 | 4G | 25 | 10 | App | 4.8 | 620 | Yes | 0.30 |
| 5 | Somtel | Monthly | 20 | 30 | 10.00 | 4G | 18 | 1 | USSD | 4.0 | 310 | No | 0.50 |
| 6 | Golis | Weekly | 5 | 7 | 3.50 | 4G | 15 | 0 | USSD | 3.6 | 180 | No | 0.70 |
| 7 | Hormuud | Daily | 0.5 | 1 | 0.30 | 4G | 25 | 0 | App | 4.2 | 850 | Yes | 0.60 |
| 8 | Somtel | Daily | 0.5 | 1 | *(missing)* | 4G | 18 | 0 | USSD | 3.5 | 310 | No | *(missing)* |
| 9 | Golis | Monthly | 30 | 30 | 15.00 | 4G | 15 | 1 | App | 3.8 | 180 | Yes | 0.50 |
| 10 | Telesom | Daily | 2 | 1 | 0.90 | 4G | 20 | 0 | App | 4.2 | 620 | Yes | 0.45 |

Row 8 shows what a missing value looks like in this dataset  I missed recording the price during the Somtel USSD session and caught it too late.

---

## 4. Quality Issues

| Issue | Where | Fix in Lesson 3 |
|---|---|---|
| Missing `price_usd` | Rows 51, 52 | Impute with median per provider group |
| Missing `user_rating` | Row 52 | Impute with provider median |
| Missing `data_speed_mbps` | Row 53 | Impute with provider + network_gen median |
| Missing `price_per_gb` | Rows 51, 52 (derived from missing price) | Recompute after imputing `price_usd` |
| Categorical strings | `provider`, `bundle_type`, `network_gen`, `purchase_method` | One-hot encode |
| Binary strings | `auto_renew` stored as "Yes"/"No" | Map to 1/0 |
| Scale gap | `active_sub_k` goes 180–850, `bonus_gb` goes 0–10 | Standard scale or min-max |
| Right skew | `price_usd` and `data_gb` skewed right (most bundles are cheap and small) | Log transform before regression |
| Mild imbalance | Hormuud has 14 rows, Golis has 10 | Stratified split if classifying by provider |

No duplicate rows. Missing values are about 5.5% of total cells  manageable.

---

## 5. Learning Type

### Primary: Supervised Learning (Regression)

This is a supervised problem because every bundle has a recorded price  that's a clear label `y`.

The model learns:

```
f(provider, bundle_type, data_gb, validity_days, network_gen, ...) → price_usd
```

52 of 55 rows have a complete `price_usd`. The 3 missing values are collection gaps, not a structural problem. A regression model (Linear Regression, Random Forest) trained on the 52 complete rows can also be used to fill in those 3 missing prices as a sanity check.

**This fits Lesson 2's definition of supervised:** labeled data exists, the output is continuous, the goal is prediction.

### Secondary: Unsupervised Learning (Clustering)

Drop `price_usd` and the feature space  especially `data_gb`, `validity_days`, `data_speed_mbps`, `price_per_gb` naturally groups bundles into tiers without being told what the tiers are.

K-Means or DBSCAN would probably find something like Budget / Standard / Premium on its own. That's useful for a price-comparison app: you don't need to manually define tiers, the data shows you where the natural breaks are.

---

## 6. Use Case & Data Science Lifecycle

### What this dataset can be used for

**Regression**  Predict `price_usd` from bundle specs. A new telecom entering Mogadishu could use this to benchmark their pricing before launch.

**Classification**  Bin `price_usd` into Budget / Standard / Premium tiers (by quantile), then train a classifier. Useful for a recommendation system ("show me budget 4G monthly bundles").

**Clustering**  Segment the market without predefined labels. Good for competitive analysis: where does each provider sit relative to others on the price-per-GB axis?

**Anomaly Detection**  Flag bundles where `price_per_gb` is way above or below what the model expects. Useful if you're checking for pricing errors before publishing.

### Where this fits in the Data Science Lifecycle (Lesson 1)

| Stage | Status |
|---|---|
| Business Understanding | Done Somali consumers have no central place to compare data prices |
| Data Collection | Done  55 rows from apps, USSD, websites, in-store |
| Data Preparation | **Next (Lesson 3)** impute, encode, scale, re-derive `price_per_gb` |
| Exploratory Analysis | After Lesson 3  price distributions, provider comparisons, correlation with `data_gb` |
| Modeling | Regression (Random Forest or Linear) to predict `price_usd` |
| Evaluation | RMSE, R² on held-out test set |
| Deployment | FastAPI endpoint → React price-comparison frontend |

The deployment stage is realistic here. I already have the stack for it (React + FastAPI). The dataset is small enough that a trained model could run as a lightweight API without any special infrastructure.

---

## Files

```
somalia_mobile_data.csv   the raw dataset (55 rows × 14 columns)
answers.md                   this file
```

---

## Notes

Prices were current as of June 17–20, 2026. Telecom promotions change often  especially Hormuud's bonus GB offers  so some values may be outdated within weeks.

The `active_sub_k` numbers are estimates from publicly available reports, not official figures. Treat them as approximate.
