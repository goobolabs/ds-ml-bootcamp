# Architectural Reflection: Car Dataset Preprocessing Pipeline

This document details the core data science rationales behind the architecture of the processing script.

## 1. Quality Issues & Targets Extraction
The raw matrix contained substantial environmental structural noises. The primary engine component, `Price`, was stored in string representations containing structural prefixes (`$`) and comma notation strings. Stripping this syntax using vector string replacements and converting down to a standard float primitive fixed this type error. 

Additionally, because the target feature contains a floor concentration of lower boundaries alongside highly expanded asset variations (e.g., standard price instances around $1,500 vs luxury entries exceeding $120,000), a `LogPrice` transformation using $log1p$ was engineered. This configuration minimizes severe right-skew distribution artifacts to scale error terms proportionally for downstream linear regression estimators.

## 2. Categorical Standardizations
The source structural arrays contained mixed categorical representations due to transcription errors (such as `Subrb` instead of `Suburb`). Standardizing categorical levels before executing statistical imputation prevents dimensional explosion during encoding. Furthermore, abstract string representations or symbols like `??` were explicitly mapped to real Null (`np.nan`) values so they could be properly handled by pandas' missing data methods.

## 3. Imputation Strategy
- **Continuous Parameters (`Odometer_km`)**: Imputed using the **Median** statistic. Continuous distance parameters are susceptible to long-tailed extreme values, making the mean unreliable. The median provides a robust central tendency baseline.
- **Discrete & Nominal Metrics (`Doors`, `Accidents`, `Location`)**: Imputed via the mathematical **Mode**. Because a car cannot possess a decimal quantity of doors or accidents, filling missing entries using the most common whole integer maintains logical data constraints.

## 4. Outlier Handling via IQR Capping
To ensure statistical robustness without discarding data volume, a soft-capping approach using the Interquartile Range (IQR) was implemented. Data distributions beyond $1.5 \times IQR$ from the upper/lower quartiles were capped at their respective boundaries. This approach prevents extreme points from distorting model parameter convergence while retaining valid operational rows.

## 5. Feature Engineering
- **CarAge**: Formulated relative to the current temporal marker (2026). This converts static registration years into continuous lifetime metrics.
- **Km_per_year**: Computes asset utilization intensity. To prevent zero-division operational errors for vehicles built in the current year, a minimum age constraint of 1 year was strictly applied.
- **Is_Urban**: Engineered as a macro-spatial indicator by combining the `City` and `Suburb` flags, providing a condensed feature for geographic localization.

## 6. Continuous Feature Scaling
Applying standard normalization via `StandardScaler` centers continuous distributions around a mean of 0 with a standard deviation of 1. Dummy encoded columns and target profiles were explicitly excluded from this step to preserve their specific binary thresholds and logarithmic interpretability.