# Data cleaning Reflection: Used Cars Dataset

**Date:** June 2026

## 1. Missing Value Imputation Strategy

During the data cleaning phase, inconsistent entries and structural artifacts (such as `"Subrb"` and text placeholders like `"??"`) were successfully mapped using Pandas `.replace()`. When addressing missing data across features, the following logic was applied:

- **Continuous Numerical Features (`Odometer_km`, `Price`):** The **Median** was selected over the mean for imputation. Used car datasets are highly prone to heavy right-skews (e.g., rare luxury cars or non-functional vehicles). The median provides a robust central tendency that ignores these extreme tails, preventing imputed values from artificially distorting the true baseline distribution.
- **Categorical Features (`Location`):** The **Mode** (most frequent value) was utilized. Since categorical text data possesses no numerical scale, mathematical averages are impossible, making the mode the mathematically sound choice to preserve the structural probability of the categories.

## 2. Outlier Handling via IQR Capping

Rather than dropping records containing extreme data points, an **Interquartile Range (IQR) Capping (Winsorization)** method was built natively using a custom Python function (`iqr_func`).

- **Why Capping over Deletion:** Dropping rows with extreme values risk-depletes rows containing valid structural data in secondary columns (e.g., a car with an extreme odometer reading may still hold an entirely normal, predictable price pattern).
- **Mechanism:** Using the calculated bounds **$[Q1 - 1.5 \times IQR, Q3 + 1.5 \times IQR]$**, extreme outliers were reined in using Pandas `.clip()`. This preserves the complete row volume of the dataset while dampening the variance inflation that otherwise destabilizes gradient weights in distance-sensitive machine learning models.

## 3. Engineered Features & Analytical Justification

To expose hidden predictive patterns to downstream machine learning models, targeted features were engineered using the baseline current timeline variable (`CURRENT_YEAR = 2026`):

- **`Car_age` (Temporal Duration):** Calculated via `2026 - df["Year"]`. This transforms a static calendar timestamp into an easily interpretable, continuous duration vector.
- **`Km_Per_Year` (Usage Intensity via NaN Handling):** Calculated by dividing `df["Odometer_km"]` by `df["Car_age"].replace(0, np.nan)`. Instead of altering the age mathematically, cars with an age of 0 were temporarily treated as `NaN` during the division. This elegantly avoids a `ZeroDivisionError` and assigns a null value to brand-new cars, correctly representing that a 0-year-old car does not yet have a historical annual mileage average.
- **`Age_x_Odometer` (Depreciation Interaction):** Formed via cross-product multiplication. Car value reduction behaves exponentially rather than linearly when an asset is simultaneously aged _and_ heavily driven. This interaction term serves as an explicit mathematical proxy for compound mechanical depreciation.

## 4. Feature Selection & Feature Scaling Pipeline

Prior to executing mathematical scaling, a strict filtering process was designed to isolate features based on structural semantics:

- **Retention of Raw `Year`:** Both `Year` and `Car_age` were intentionally retained in the dataset. While linear models are sensitive to this duplication, keeping both provides powerful split-points for non-linear tree-based architectures (e.g., Random Forests, XGBoost) to distinguish between historical trends and purely relative vehicle age.
- **Exclusion of Target & Encoded Elements:** The target variable (`Price`) was preserved in its raw unit scale to keep validation metrics interpretable. One-hot encoded location indicators (`Location_Rural`, `Location_Suburb`) were excluded from the scaling list to prevent the destruction of their structural binary identity (**$0$** or **$1$**).
- **Continuous Scaling Matrix:** Continuous attributes (`Odometer_km`, `Car_age`, `Km_Per_Year`, `Age_x_Odometer`) were cleanly isolated using `.select_dtypes().columns.tolist()` for numeric uniform normalization, ensuring distance calculations remain entirely unbiased.
