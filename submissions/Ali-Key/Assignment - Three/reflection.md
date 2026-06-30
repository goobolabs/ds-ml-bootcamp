# Practical Assignment: Data Preprocessing Report

**Author: Ali Omar Abdi**                                          
**Course: DS-ML Bootcamp — Assignment 2**                               
**Due: Wednesday, June 24, 2026 — 12:00 PM (EAT)**      

---

## Table of Contents

* [Introduction](#introduction)
* [Loading and Exploring the Data](#loading-and-exploring-the-data)
* [Cleaning the Price Column](#cleaning-the-price-column)
* [Fixing Errors in Location](#fixing-errors-in-location)
* [Handling Missing Values](#handling-missing-values)
* [Removing Duplicate Records](#removing-duplicate-records)
* [Handling Outliers](#handling-outliers)
* [Encoding the Location Column](#encoding-the-location-column)
* [Creating New Features](#creating-new-features)
* [Scaling Numerical Features](#scaling-numerical-features)
* [Final Checks and Saving the Data](#final-checks-and-saving-the-data)
* [Conclusion](#conclusion)

---


## Introduction

In this assignment, I cleaned and prepared the `raw_car_dataset.csv` dataset for machine learning. Raw data often contains missing values, mistakes, duplicate records, and inconsistent formats. These issues must be fixed before building a machine learning model.

---

## 1. Loading and Exploring the Data

I started by loading the dataset into pandas and examining its structure. I checked the first few rows, data types, missing values, and the different values in the `Location` column.

**Why?**
Before cleaning data, it is important to understand what the dataset contains and identify any problems that need to be fixed.

---

## 2. Cleaning the Price Column

The `Price` column contained values such as `$12,000`, which included symbols and commas. I removed these characters and converted the column into a numeric format.

**Why?**
Machine learning models work with numbers, not text or currency symbols.

---

## 3. Fixing Errors in Location

The `Location` column contained spelling mistakes such as `Subrb` and unknown values such as `??`. I corrected the spelling mistakes and treated unknown values as missing data.

**Why?**
Different spellings of the same category can confuse the model and reduce data quality.

---

## 4. Handling Missing Values

Missing values were filled using appropriate methods:

* `Odometer_km` → Median
* `Doors` → Mode
* `Accidents` → Mode
* `Location` → Mode

**Why?**
Most machine learning algorithms cannot work with missing values, so they must be filled before training.

---

## 5. Removing Duplicate Records

I checked for duplicate rows and removed them from the dataset.

**Why?**
Duplicate records can make some observations appear more important than they actually are.

---

## 6. Handling Outliers

I used the IQR (Interquartile Range) method to identify unusually large or small values in `Price` and `Odometer_km`. These values were capped to keep them within a reasonable range.

**Why?**
Extreme values can have a strong influence on model performance and may lead to inaccurate results.

---

## 7. Encoding the Location Column

Since machine learning models cannot directly understand text categories, I converted the `Location` column into numerical dummy variables such as:

* Location_City
* Location_Rural
* Location_Suburb

**Why?**
This allows the model to use location information during training.

---

## 8. Creating New Features

To provide more useful information to the model, I created the following features:

* **CarAge** – Age of the vehicle
* **Km_per_year** – Average distance driven per year
* **Is_Urban** – Indicates whether the car is located in a city or suburb
* **LogPrice** – Log-transformed version of the price

**Why?**
Well-designed features can improve the model’s ability to find patterns in the data.

---

## 9. Scaling Numerical Features

I standardized continuous numerical features so they share a similar scale. Binary columns and target variables were not scaled.

**Why?**
Scaling helps many machine learning algorithms perform more effectively.

---

## 10. Final Checks and Saving the Data

After preprocessing, I verified that:

* No missing values remained.
* Data types were correct.
* New features were successfully created.

Finally, I saved the cleaned dataset as:

`clean_car_dataset.csv`

---

## Conclusion

This preprocessing pipeline transformed the raw dataset into a clean and structured dataset ready for machine learning. The process included cleaning data, handling missing values, removing duplicates, treating outliers, encoding categorical variables, creating new features, and scaling numerical data. These steps improve data quality and help build more reliable machine learning models.

*Submitted for DS-ML Bootcamp — Assignment 3*
*Due: Wednesday, June 24, 2026*
