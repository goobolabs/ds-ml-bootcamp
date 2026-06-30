# Reflection — Climate Dataset Cleaning

## Overview

This reflection documents the decisions, challenges, and lessons learned while cleaning the `climate_dataset.csv` dataset using Python and Pandas. The goal was to prepare raw, messy climate data for machine learning use.

---

## 1. Understanding the Raw Data

Before writing a single line of cleaning code, exploring the dataset with `.head()`, `.shape()`, `.info()`, and `.isnull().sum()` was essential. The dataset contained **51 rows** and **7 columns**:

| Column | Type | Issues Found |
|---|---|---|
| `RecordID` | String | Corrupted IDs (`??`, `-`, `P010`, `PO41`) |
| `RainfallAmount_mm` | String/Float | Special characters (`$`, `%`, `@`), outliers |
| `AvgTemperature_C` | Float | Extreme outlier (`70.0°C`) |
| `Humidity_percent` | Float | Missing values, outlier (`130%`) |
| `RainyDaysCount` | Float | Missing values |
| `SoilMoistureLevel` | String | Inconsistent casing (`Med`, `MEDIUM`, `medium`) |
| `ClimateCondition` | String | Inconsistent casing (`drought`, `RAINY`, `rainy`) |

---

## 2. Challenges Encountered

### Special Characters in Numeric Data
The `RainfallAmount_mm` column stored numbers as strings with symbols like `$99.1`, `%61.3`, and `@30.8`. These had to be stripped using regex before converting to `float`. This was a reminder that real-world data can be formatted by human error or inconsistent data entry systems.

### Inconsistent Categorical Values
Both `SoilMoistureLevel` and `ClimateCondition` had the same values written in multiple formats (e.g., `"low"`, `"LOW"`, `"Low"`). A manual replacement dictionary was used to normalise them all to a consistent title-case format. While this worked, it required carefully inspecting every unique value first — a step that is easy to skip but costly if missed.

### Misplaced Value in `SoilMoistureLevel`
The value `"Drought"` appeared in the `SoilMoistureLevel` column, which is clearly a data entry error (Drought is a climate condition, not a moisture level). The decision was made to treat it as `NaN` and impute it with the column mode. This highlights how important domain knowledge is when cleaning data.

### Corrupted `RecordID` Values
Entries like `??`, `-`, `P010`, and `PO41` were identified in the `RecordID` column. Since `RecordID` is an identifier and not used as a feature for modelling, these were left as-is rather than corrected or dropped, to avoid accidental data loss.

### Outlier Detection and Clipping
The IQR (Interquartile Range) method was used to detect outliers. Notable extreme values included:
- `RainfallAmount_mm = 999.0` — clearly erroneous
- `AvgTemperature_C = 70.0°C` — physically impossible for a surface climate reading
- `Humidity_percent = 130%` — impossible, humidity cannot exceed 100%

Clipping (rather than dropping) was chosen to preserve the row count while bounding values to a reasonable range.

> **Bug noted:** In the clipping step for `Humidity_percent`, the upper bound was accidentally set to `high_temp` (the temperature upper bound) instead of `highHumid`. This is a subtle bug that could skew humidity statistics and should be corrected in a future revision.

---

## 3. Decisions Made

| Decision | Reasoning |
|---|---|
| Filled numeric nulls with **median** | Median is robust to outliers, which were present in this dataset |
| Filled categorical nulls with **mode** | Most frequent value is the safest assumption for small datasets |
| Used **clipping** instead of dropping outliers | Preserves data while reducing extreme influence |
| Applied **one-hot encoding** to categoricals | Prepares data for ML models that require numeric input |
| Created binary columns `isItDrought` / `isItRainy` | Makes target-like features explicit and easy to use |
| Did **not** clean `RecordID` | It is an ID column, not a feature — does not affect model training |

---

## 4. Lessons Learned

- **Always explore before cleaning.** Running `.value_counts(dropna=False)` on every column before touching anything revealed most of the issues upfront.
- **Categorical inconsistency is subtle.** It is easy to miss that `"Med"`, `"MEDIUM"`, and `"medium"` are the same thing unless you explicitly look at unique values.
- **Variable naming matters.** The bug where `high_temp` was used instead of `highHumid` in the clipping step is a direct result of similar-looking variable names. More descriptive names (e.g., `humidity_upper`) would reduce this risk.
- **Domain knowledge guides imputation.** Knowing that `"Drought"` cannot be a soil moisture level required understanding the subject matter, not just the data.
- **Document your assumptions.** Each cleaning decision rests on an assumption (e.g., "this outlier is erroneous"). Writing those assumptions down makes the pipeline easier to audit and revise.

---

## 5. What Could Be Improved

- Fix the `Humidity_percent` clipping bug (use `highHumid` as upper bound).
- Standardise or drop the corrupted `RecordID` entries for a cleaner dataset.
- Consider using a pipeline (`sklearn.Pipeline`) to make the cleaning steps reproducible and testable.
- Add unit tests or assertions (e.g., `assert df["Humidity_percent"].max() <= 100`) to catch logic errors automatically.
- For a larger dataset, automated outlier detection (e.g., Z-score or Isolation Forest) would scale better than manual IQR thresholds.

---

*Prepared as part of a data preprocessing project on climate condition analysis.*
