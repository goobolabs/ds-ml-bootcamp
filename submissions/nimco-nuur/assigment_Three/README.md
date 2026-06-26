#  Car Dataset Preprocessing

## Overview
This project cleans and prepares a raw car dataset for machine learning.

---

##  Steps

### 1️⃣ Data Cleaning
- Removed symbols from Price (`$`, `,`)
- Converted Price to numeric
- Fixed Location typos and invalid values

### 2️⃣ Missing Values
- Odometer_km → median
- Doors → mode
- Accidents → mode
- Location → mode

### 3️⃣ Outliers (IQR)
- Used IQR method
- Applied capping (clip) for Price and Odometer_km

### 4️⃣ Feature Engineering
- CarAge = 2026 - Year
- Km_per_year = Odometer_km / CarAge
- Is_Urban = City = 1 else 0
- LogPrice = log(Price + 1)

### 5️⃣ Scaling
- StandardScaler applied to numeric features

---

## Output
Clean dataset saved as:

---

##  Result
Dataset is now clean, structured, and ready for ML models.
