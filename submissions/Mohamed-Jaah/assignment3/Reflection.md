# Reflection: Car Dataset Cleaning Pipeline

## Overview

This script cleans and engineers features for a used car listings dataset
(`raw_car_dataset.csv`), following a load → inspect → clean → impute → deduplicate →
cap outliers → encode → engineer → scale → save pipeline.

## Dataset

The raw dataset contains 145 rows and 6 columns:

| Column        | Type    | Notes                                    |
|---------------|---------|-------------------------------------------|
| Price         | string  | mixed formats, some with `$` and commas   |
| Odometer_km   | float   | 7 missing values                          |
| Doors         | float   | 7 missing values                          |
| Accidents     | int     | count of prior accidents                  |
| Location      | string  | 5 missing, plus a typo and a placeholder  |
| Year          | int     | manufacturing year                        |

## Key Decisions

**1. Target formatting.** `Price` mixed formatted (`$1,500`) and plain numeric strings.
Stripped `$` and `,` via regex, then cast to float.

**2. Categorical cleanup before imputation.** `Location` had a typo (`"Subrb"` → `"Suburb"`)
and a placeholder (`"??"`) that needed to become missing rather than a real category. This
runs *before* mode imputation so `"??"` can't get counted as, or become, the fill value.

**3. Imputation targets.** `Odometer_km` filled with the median (mileage can be skewed by a
few very old or very new cars, so median is more robust than mean). `Doors` filled with the
mode, since door count is a small discrete set of values. `Location` also filled with its
mode after the typo/placeholder cleanup.

**4. Duplicate removal.** 5 duplicate rows dropped, logged with a before/after shape print.
This happens after categorical/target cleanup but before outlier capping, so duplicates don't
skew the IQR bounds.

**5. Outlier capping.** IQR-based clipping applied to `Price` and `Odometer_km` — the two
continuous columns most exposed to data-entry extremes. `Doors`, `Accidents`, and `Year` were
left as-is, since their ranges are small and discrete enough that unusual values are more
likely genuine than erroneous.

**6. Feature engineering.**
- `CarAge` = 2025 − `Year`
- `Km_per_Year` = `Odometer_km` / `CarAge` (zero-`CarAge` rows mapped to 1 instead of `NaN`,
  so brand-new cars still get a usage-rate value instead of a missing one)
- `Price_per_Door` = `Price` / `Doors`
- `Has_Accident` = binary flag for `Accidents > 0`
- `Is_City` = binary flag copied from the one-hot `Location_City` column
- `LogPrice` = `log1p(Price)`, an alternate, less skewed version of the target

**7. Scaling scope.** All numeric features were scaled except the targets (`Price`,
`LogPrice`) and columns that are already 0/1 indicators (`Location_*` dummies, `Is_City`,
`Has_Accident`).

## A Concern Worth Flagging: Target Leakage in `Price_per_Door`

`Price_per_Door` is calculated directly from `Price`, the prediction target. Including it as
a feature would let a model "cheat" — it could reconstruct `Price` almost exactly (`Price ≈
Price_per_Door × Doors`), producing artificially strong training performance that would not
hold up on genuinely new data where `Price` is unknown. If this dataset is meant for
predictive modeling, `Price_per_Door` should either be dropped before training or only ever
computed downstream from a model's *predicted* price, never from the actual target column. A
non-leaky alternative in the same spirit would be a feature built only from input columns —
e.g. `Accidents_per_Door` — the way `Km_per_Year` is built from `Odometer_km` and `CarAge`.

## Other Notes

- `CarAge.replace(0, 1)` avoids introducing new missing values for brand-new cars, at the cost
  of slightly understating their usage rate (dividing by 1 year rather than a true fractional
  age). This is a reasonable simplification for this dataset size but worth documenting.
- `Has_Accident` is a useful complement to the raw `Accidents` count — it captures "any
  accident at all" as a simple binary signal, which may be a cleaner predictor than the raw
  count if accident severity/count is noisy or sparse.

## Verification

Ran the script end-to-end. After cleaning: 140 rows (5 duplicates dropped), 14 columns, and
zero missing values across every column. Output written successfully to
`clean_car_dataset.csv`.

## Possible Next Steps

- Remove or replace `Price_per_Door` before using this dataset for training, to eliminate
  target leakage.
- Check whether `Odometer_km` and `Doors` are missing at random or systematically (e.g. from a
  specific data source), which would affect whether median/mode imputation is appropriate.
- Add a train/test split before fitting `StandardScaler`, so scaling parameters come only from
  training data rather than the full dataset.
