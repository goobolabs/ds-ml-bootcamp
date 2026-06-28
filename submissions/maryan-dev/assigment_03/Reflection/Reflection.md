## Price Cleaning

The Price column contained currency symbols ($) and commas. These characters were removed and the column was converted to float to make it suitable for numerical analysis and machine learning.

## Location Cleaning

The Location column contained inconsistent values such as "Subrb" and "??". "Subrb" was corrected to "Suburb" and invalid values were treated as missing.

## Missing Values

Median was used for Odometer_km because it is more robust to outliers than the mean. Mode was used for Doors, Accidents, and Location because these are categorical or discrete variables.

## Duplicate Removal

Duplicate rows were removed to prevent the same observation from influencing the model multiple times.

## Outlier Handling

IQR capping was applied to Price and Odometer_km because both variables contained extreme values. Capping reduces the influence of outliers while preserving observations.

## Encoding

One-Hot Encoding was applied to the Location column because machine learning models require numeric input.

## Feature Engineering

Several new features were created:

* CarAge = 2026 - Year
* Km_per_year = Odometer_km / CarAge
* Is_Urban based on Location_City
* LogPrice using logarithmic transformation

These features capture useful information about vehicle age, usage intensity, urban location, and price distribution.

## Scaling

StandardScaler was used to standardize numerical features so they have approximately mean 0 and standard deviation 1. This improves model performance for many algorithms.
.....


