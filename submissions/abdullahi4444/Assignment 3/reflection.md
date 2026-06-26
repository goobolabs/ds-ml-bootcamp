Reflection — Data Preprocessing Decisions

This short reflection explains the main decisions made in the preprocessing pipeline.

- Price cleaning: removed currency symbols and commas, coerced to numeric. Strings and stray characters would have broken downstream numeric ops and skew/transform calculations.
- Imputation choices:
  - Odometer_km → median: odometer has long tails/outliers; median is robust and preserves a realistic central value.
  - Doors, Accidents → mode: these are discrete counts/categories where the most common value is a simple, unbiased fill.
  - Location → mode: preserves the most common locality and avoids creating many small categories.

- Outlier handling: IQR capping (clip to [Q1-1.5·IQR, Q3+1.5·IQR]) for `Price` and `Odometer_km`. IQR capping reduces the influence of extreme values while keeping all rows (no deletion), which is useful for modeling and consistent with course guidance.

- Encoding: one-hot encode `Location` to avoid ordinal assumptions. Kept all dummy columns (no drop-first) so downstream pipelines can decide how to treat multicollinearity.

- Feature engineering (no leakage):
  - `CarAge` = current_year - `Year` (or `YearBuilt`) — useful predictor of depreciation.
  - `Km_per_year` = `Odometer_km / CarAge` with safe handling for zero/unknown ages — gives an annual usage rate.
  - `Is_Urban` inferred from Location dummy `Location_City` — captures urban vs non-urban effects.
  - `LogPrice` = log(Price + 1) as an alternative target to reduce skew for regression.

- Scaling: Standardized continuous features (mean ≈ 0, std ≈ 1) while leaving `Price`/`LogPrice` and 0/1 dummies unscaled. Keeping targets unscaled preserves interpretability.

These choices balance robustness and simplicity, follow course guidance (median for skewed numerics, mode for categorical), and avoid leakage into the target.
Reflection — Data Preprocessing (≤ 1 page)

1. Price cleaning
- Removed currency symbols and thousand separators to convert `Price` to numeric. This ensures consistent numeric analyses and avoids parsing errors.

2. Imputation choices
- `Odometer_km`: median imputation chosen because odometer is continuous and median is robust to outliers.
- `Doors`, `Accidents`, `Location`: mode imputation (most frequent) chosen because these are categorical/discrete and mode preserves common categories.

3. Outlier handling
- Used IQR capping (1.5*IQR) to limit extreme values while preserving distributional shape. This reduces the influence of outliers on scaling and models without dropping rows.

4. Feature engineering
- `CarAge`: current year minus `Year` gives vehicle age; handled non-positive or missing years by setting a safe fallback (1 year) to avoid division by zero.
- `Km_per_year`: `Odometer_km / CarAge` gives usage rate; computed after safe CarAge adjustment.
- `Is_Urban`: binary indicator derived from `Location` (City/Suburb considered urban) to capture location-driven demand differences.
- `LogPrice`: log(Price + 1) created as an alternative target to stabilize skewness in price distribution.

5. Scaling
- Standardized continuous features (`Odometer_km`, `CarAge`, `Km_per_year`) to mean 0 and std 1 for model readiness. Kept `Price` and `LogPrice` unscaled and left 0/1 dummies unscaled.

6. Sanity checks
- Assert `Price` is float, `LogPrice` exists, no missing values remain, at least one `Location_*` dummy exists, and scaled columns have mean≈0 and population std≈1.

These choices balance robustness and interpretability while avoiding leakage into the target.
