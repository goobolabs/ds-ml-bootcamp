# Laptop Prices in Somalia Dataset

## Practical Assignment: Data Foundations for Machine Learning

### Student Information

**Name:** Hayat Mohamud Hassan

---

## 1. Introduction

Data Science is the process of collecting, organizing, analyzing, and interpreting data to gain useful insights and support decision-making. Machine Learning is a branch of Data Science that enables computers to learn patterns from data and make predictions.

This project focuses on a dataset of laptop prices collected from local computer shops and online marketplaces in Somalia. The purpose of the dataset is to understand how laptop specifications influence market prices and how the data can be used in a machine learning project.

---

## 2. Data Collection Method

The dataset was collected manually by observing laptop advertisements and computer shops. Information such as laptop brand, RAM size, storage capacity, processor type, screen size, condition, and price was recorded in a spreadsheet.

A total of **50 laptop records** were collected.

The dataset was created specifically for this assignment and was not taken from Kaggle, UCI, or any other public dataset repository.

---

## 3. Features and Label

Machine Learning datasets contain features (inputs) and labels (outputs).

### Features (X)

1. Brand
2. RAM_GB
3. Storage_GB
4. Processor
5. Screen_Size
6. Condition

### Label (y)

* Price_USD

The features describe the characteristics of a laptop, while the label represents the price that a machine learning model will attempt to predict.

---

## 4. Dataset Structure

The dataset contains:

* Number of Rows (Samples): 50
* Number of Columns: 7
* Features: 6
* Label: 1

### Sample Records

| Brand  | RAM_GB | Storage_GB | Processor | Screen_Size | Condition | Price_USD |
| ------ | ------ | ---------- | --------- | ----------- | --------- | --------- |
| HP     | 8      | 256        | i5        | 14          | Used      | 280       |
| Dell   | 16     | 512        | i7        | 15.6        | Used      | 450       |
| Lenovo | 8      | 256        | i5        | 14          | New       | 380       |
| HP     | 4      | 128        | i3        | 14          | Used      | 180       |
| Apple  | 8      | 256        | M1        | 13.3        | Used      | 750       |

---

## 5. Data Quality Issues

Real-world datasets often contain quality issues that must be addressed before machine learning can be applied.

Possible issues in this dataset include:

* Missing values in some laptop specifications.
* Typographical errors during data entry.
* Duplicate records.
* Inconsistent naming formats.
* Outliers where prices may be unusually high or low.

These issues will be handled during data preprocessing through cleaning, encoding, and validation.

---

## 6. Learning Type

This dataset is suitable for **Supervised Learning** because it contains a clearly defined target variable (Price_USD).

The machine learning algorithm will learn from the relationship between laptop specifications and their prices.

This problem is specifically a **Regression Problem** because the output variable (price) is a continuous numerical value.

---

## 7. Use Case and Data Science Lifecycle

This dataset can be used to build a machine learning model that predicts laptop prices based on their specifications.

Possible applications include:

* Laptop price prediction.
* Market price analysis.
* E-commerce pricing systems.
* Product recommendation platforms.

Within the Data Science lifecycle, this dataset belongs primarily to the following stages:

1. Data Collection
2. Data Understanding
3. Data Preparation
4. Model Building
5. Evaluation and Deployment

---

## 8. Conclusion

The Laptop Prices in Somalia Dataset provides a practical example of data collection and preparation for machine learning. The dataset contains meaningful features and a numerical target variable, making it suitable for supervised machine learning regression tasks.

Future work will include preprocessing the data, performing exploratory data analysis, training machine learning models, and evaluating prediction performance.
