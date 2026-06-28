# Assignment 3 Reflection: Data Preprocessing Pipeline

**Prepared by:** [Hanaan bashir dahir / GitHub Username:xanaa-ayan]  
**Course:** Data Science & Machine Learning Bootcamp  

## Overview
This reflection document explains the engineering decisions and technical rationales behind each major phase of the data preprocessing pipeline implemented in `car_preprocess.py`.

---

## 1. Missing Data Strategy: Median vs. Mode Imputation
During Step 4, missing values were detected in both continuous/numerical columns (`Odometer_km`, `Doors`) and categorical columns (`Location`).

* **Numerical Columns (Median):** The *Median* was selected rather than the *Mean* because numerical features in real-world data (such as mileage or prices) often contain skewed distributions or extreme outliers. The mean is highly sensitive to these anomalies, whereas the median provides a robust central tendency that does not distort the original data distribution.
* **Categorical Columns (Mode):** The *Mode* (the most frequently occurring value) was used for the `Location` column. Since categorical text data cannot be mathematically averaged, the mode represents the most statistically sound guess to preserve the probability distribution of the categories.

---

## 2. Outlier Handling: IQR Capping
In Step 5, instead of discarding rows containing extreme values (outliers), an **IQR (Interquartile Range) Capping (or Winsorization)** technique was used.

* **Why Cap instead of Drop?** Dropping outliers leads to data loss, reducing the dataset's sample size and potentially stripping away critical, legitimate information. Capping bounds the extreme values to the $Q1 - 1.5 \times IQR$ and $Q3 + 1.5 \times IQR$ limits. This preserves the rows entirely while squeezing extreme variances down so they do not disorient or overpower the Machine Learning algorithms during training.

---

## 3. Feature Engineering Choices
In Step 7, four key features were designed to enhance the predictive patterns available to a machine learning model:

1.  **`CarAge` (Current Year - Year):** Transforming a raw calendar year into an absolute age makes it easier for linear models to map the depreciation value of a car directly.
2.  **`Km_per_year` (Kilometers_Driven / CarAge):** Measures the driver's usage intensity. To safely prevent a `ZeroDivisionError` for brand new cars where `CarAge == 0`, a safe conditional replacement (`np.where`) was integrated to treat age as 1 or safely handle the denominator.
3.  **`Is_High_Mileage` (Binary Indicator):** Creates a threshold feature (1 if kilometers driven exceed 100,000, else 0). This handles non-linear price drops that occur once a vehicle passes milestones commonly scrutinized by buyers.
4.  **`LogPrice` (Alternative Target):** Applied a Log transformation ($\log(x + 1)$) to the target variable (`Price`). Car prices are frequently right-skewed; transforming the target makes the distribution normal, stabilizing the error terms for regression modeling.

---

## 4. Feature Scaling Rationale
In Step 8, a `StandardScaler` was applied exclusively to continuous features (`CarAge`, etc.).

* **X-Only Limitation:** Feature scaling must never be applied to the target variable ($y$ or `LogPrice`) to keep predictions interpretable, nor to binary dummy variables ($0/1$ columns generated from One-Hot Encoding) as scaling them ruins their physical binary meaning.
* **Mathematical Necessity:** Distance-based models (e.g., KNN, SVM) and gradient-descent algorithms are heavily biased toward features with wider numeric scales. Standardization ensures every numeric feature contributes equally to the loss function by centering the mean around $0$ with a standard deviation of $1$.