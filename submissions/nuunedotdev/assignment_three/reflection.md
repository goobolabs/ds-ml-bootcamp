# Assignment Three - CARS DATASET

## Why used Median & Mode

**What it is:** You line up all your numbers from smallest to largest and pick the exact number right in the middle.

**Reasons for using:** Use it if your data is distorted or has a lot of outliers. The median just considers what is going on in the center, entirely ignoring how crazy the extreme ends are.

**What it is:** The number or category that appears the most often.

**Reasons for using it:** Use it when you need to determine the single most popular option or when working with categorical data (words or labels rather than numbers).

## Why IQR Caping

The main reason **IQR Capping** is utilized in data cleaning is that it provides a strong middle ground by mitigating the negative effects of outliers without discarding your important data.

Example
---
Your dataset will get smaller if you remove every row that has an outlier. If a row contains excellent, important data in the some columns like "house_age, location and size" but a crazy outlier in the Price column, eliminating the entire row would waste that great information.

## which features you engineered and why

1. safely calulation km_per_year
    ICreated a brand-new feature by dividing the Odometer_km by the Car_Age.
2. IQR Caping on PRICE & ODOMETER_KM
    Calculated the boundaries using Q1 - 1.5 X IQR and Q3 + 1.5 X IQR, then used np.clip() to cap values outside these boundaries.
3. One-Hot Encoding (pd.dummies())
    Converted categorical text features (like Location) into separate binary columns (0s and 1s).
4. 