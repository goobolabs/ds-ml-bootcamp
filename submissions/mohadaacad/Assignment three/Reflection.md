# 📊 Reflection – Data Preprocessing Pipeline

## 🧩 Overview

In this assignment, I built a complete preprocessing pipeline to transform a messy car dataset into a clean, model-ready dataset.

---

## 🧹 Handling Missing Values

For missing values:

* I used **median imputation for `Odometer_km`** because it is robust to outliers.
* I applied **mode imputation for `Doors`, `Accidents`, and `Location`** since these are categorical or discrete variables.

---

## 💰 Cleaning the Target Variable

I cleaned the `Price` column by:

* Removing currency symbols (`$`)
* Removing commas
* Converting the column into a numeric format

This ensured consistency and usability for analysis and modeling.

---

## 🏷️ Fixing Categorical Errors

Before performing imputation:

* I standardized the `Location` column (e.g., fixing typos like *Subrb → Suburb*)
* Converted unknown values (e.g., `"??"`, `"Unknown"`) into missing values

This step prevented incorrect mode calculations.

---

## 🔁 Removing Duplicates

I removed duplicate rows to:

* Eliminate redundant data
* Improve data quality
* Prevent bias in model training

---

## 📉 Handling Outliers

I applied **IQR (Interquartile Range) capping** to:

* Limit extreme values in `Price` and `Odometer_km`
* Preserve data instead of removing rows

---

## 🔢 Encoding Categorical Data

I used **one-hot encoding** for the `Location` column:

* Converted categories into binary (0/1) columns
* Made the dataset compatible with machine learning algorithms

---

## ⚙️ Feature Engineering

I created the following features:

* **CarAge** → captures depreciation based on year
* **Km_per_year** → measures usage intensity
* **Is_Urban** → simplifies location grouping
* **LogPrice** → reduces skewness of the target variable

---

## 📏 Feature Scaling

I applied **StandardScaler** to continuous variables:

* Ensured features are on a similar scale
* Improved model performance

Binary (0/1) variables were intentionally left unscaled.

---

## ✅ Final Outcome

This preprocessing pipeline:

* Cleans and standardizes the dataset
* Handles missing values and outliers
* Creates meaningful features
* Prepares the data for machine learning

The final dataset is consistent, reliable, and ready for modeling.
