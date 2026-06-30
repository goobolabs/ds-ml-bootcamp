# Project Reflection: Car Dataset Preprocessing

This document outlines the technical decisions made during the cleaning of `raw_car_dataset.csv`.

## 1. Handling Missing Values

* **Decision:** Used **Median** for `Odometer_km` and **Mode** for `Doors`, `Accidents`, and `Location`.
* **Rationale:** Median is robust against outliers in continuous data like mileage. Mode is appropriate for categorical and discrete data (like number of doors or categories of locations) where taking an average is mathematically invalid.

## 2. Outlier Management

* **Decision:** Applied **IQR Capping** for `Price` and `Odometer_km`.
* **Rationale:** I wanted to retain the information from extreme data points rather than deleting them. By clipping values at the $1.5 \times \text{IQR}$ thresholds, I reduced the skewness of the distribution without sacrificing sample size, which helps the model generalize better.

## 3. Feature Engineering

* **Decision:** Created `Car_age`, `Km_per_year`, and `is_Urban`.
* **Rationale:**
* `Car_age` (derived from `Year`): Provides a more intuitive linear relationship with price than raw years.
* `Km_per_year`: Normalizes usage intensity, distinguishing between cars that are old but rarely driven versus daily drivers.
* `is_Urban`: A binary feature derived from `Location` to explicitly capture the premium or discount associated with city-based vehicles.

## 4. Feature Scaling

* **Decision:** Used `StandardScaler` on numerical columns.
* **Rationale:** Standardizing features to a mean of $0$ and a standard deviation of $1$ ensures that the machine learning algorithm treats all numerical inputs with equal weight, preventing variables with larger raw magnitudes from dominating the cost function.

---
