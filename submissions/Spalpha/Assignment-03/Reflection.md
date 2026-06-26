```md
# Suhaip Hassan Mohamoud 
## git remote -vData Preprocessing Reflection

## 1) Loading data and basic inspection
I first loaded `raw_car_dataset.csv` into a pandas DataFrame and printed:
- the first few rows (`head`)
- dataset shape and info (`shape`, `info`)
- missing values per column

This step is important to detect unexpected data types (e.g., numeric columns stored as strings) and to understand where data quality issues exist before applying any transformations.

## 2) Cleaning the target / numeric field (Price)
`Price` appeared to contain currency formatting (e.g., `$` and commas), so I removed those characters and converted the column to `float`. This ensures the target is treated as numeric by later preprocessing and modeling steps, and avoids errors or incorrect scaling/log transforms.

## 3) Missing value handling: median vs mode
I used **median imputation for numeric continuous features** and **mode imputation for discrete/categorical features**:

- **`Odometer_km` → median**
  - The odometer distribution can be skewed and may contain extreme values.
  - Median is robust to outliers and preserves the central tendency better than mean.

- **`Doors` → mode**
  - Doors is a discrete count, so it’s appropriate to fill missing entries with the most common value.
  - Using mode avoids introducing non-integer or unrealistic values.

- **`Location` → mode**
  - Location is a categorical variable (after cleaning typos like `Subrb` → `Suburb` and mapping invalid tokens to missing).
  - Mode keeps the most frequent category without inventing new labels.

This approach reduces distortion from outliers and keeps each feature consistent with its data type.

## 4) Duplicate removal
I removed duplicate rows with `drop_duplicates()`. Duplicates can:
- bias model training by over-weighting certain examples
- distort summary statistics (and therefore scaling and outlier logic)

## 5) Outlier handling: IQR capping
I computed IQR bounds for:
- `Price`
- `Odometer_km`

**Why IQR capping?**
- IQR is based on quartiles, so it is robust (doesn’t assume normality).
- Outliers can strongly affect algorithms that use variance/scale (e.g., `StandardScaler`) and can destabilize model training.
- Capping limits extreme values while still retaining most of the dataset.

> In the provided `sp.py`, I computed the IQR lower/upper bounds, but I did not actually apply the capping to the DataFrame. If finalizing the pipeline, I would clamp values to those bounds for both columns.

## 6) Encoding categorical features
I converted `Location` into one-hot encoded columns using `pd.get_dummies` with:
- `drop_first=True` to avoid redundant dummy columns (reference category behavior)

Engineered categorical features:
- `Location_Rural`
- `Location_Suburb`
(others are dropped as reference)

## 7) Feature engineering (what and why)
I engineered new features to better reflect relationships that drive car pricing:

1. **`car_age` = CURRENT_YEAR − Year**
   - Age tends to be more predictive than raw `Year`.

2. **`km/Year` = Odometer_km / (car_age + 1)**
   - Usage intensity can influence wear and therefore price.
   - `+1` prevents division by zero for very new cars.

3. **`accident_rate` = Accidents / Odometer_km**
   - Represents accidents per unit distance (normalizing accidents by usage).

4. **`LogPrice` = log1p(Price)**
   - Price is often skewed; log transforms reduce skew and stabilize variance.
   - Using `log1p` is safe when price values could include zeros.

## 8) Scaling continuous features
I applied `StandardScaler` to continuous engineered columns:
- `Odometer_km`, `car_age`, `km/Year`, `accident_rate`

**Why scaling?**
- Standardization makes features comparable by centering and scaling to unit variance, which helps many ML algorithms and improves numerical stability.

## 9) Final output
After cleaning, encoding, engineering, and scaling, I saved the prepared dataset to `car_l3_clean_ready.csv` to be used for model training.
```