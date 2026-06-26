# 🌦️ Climate Dataset Cleaning

A Python data preprocessing project that cleans and prepares a raw climate dataset for machine learning, handling missing values, inconsistent formatting, outliers, and categorical encoding.

---

## 📁 Project Structure

```
├── climate_dataset.csv   # Raw input dataset
├── main.py               # Data cleaning script
├── Reflection.md         # Project reflection and lessons learned
└── README.md             # This file
```

---

## 📊 Dataset

**File:** `climate_dataset.csv`  
**Records:** 51 rows | **Features:** 7 columns

| Column | Description |
|---|---|
| `RecordID` | Unique identifier for each record |
| `RainfallAmount_mm` | Monthly rainfall amount in millimetres |
| `AvgTemperature_C` | Average temperature in degrees Celsius |
| `Humidity_percent` | Relative humidity as a percentage |
| `RainyDaysCount` | Number of rainy days in the month |
| `SoilMoistureLevel` | Categorical soil moisture (`Low`, `Medium`, `High`) |
| `ClimateCondition` | Categorical climate label (`Drought`, `Rainy`) |

---

## ⚙️ What the Script Does

### 1. Fixes Dirty Numeric Data
Strips special characters (`$`, `%`, `@`) from `RainfallAmount_mm` and converts the column to `float`.

### 2. Standardises Categorical Values
Normalises inconsistent casing and abbreviations in `SoilMoistureLevel` and `ClimateCondition` to a consistent title-case format (e.g., `"MEDIUM"` → `"Medium"`, `"drought"` → `"Drought"`).

### 3. Handles Invalid Entries
Replaces the erroneous value `"Drought"` found inside `SoilMoistureLevel` with `NaN`, since it belongs to a different column entirely.

### 4. Imputes Missing Values

| Column | Strategy |
|---|---|
| `RainfallAmount_mm` | Median |
| `Humidity_percent` | Median |
| `RainyDaysCount` | Median |
| `SoilMoistureLevel` | Mode |
| `ClimateCondition` | Mode |

Median is used for numeric columns to resist the influence of outliers; mode is used for categoricals.

### 5. Removes Duplicates
Drops exact duplicate rows using `drop_duplicates()`.

### 6. Caps Outliers with IQR Clipping
Computes IQR-based lower and upper bounds for each numeric column and clips values to those bounds — preserving all rows while neutralising extreme values.

### 7. Encodes Categorical Columns
Applies one-hot encoding via `pd.get_dummies()` to `SoilMoistureLevel` and `ClimateCondition`, converting them into binary numeric columns suitable for ML models.

### 8. Creates Binary Target Columns
Adds two explicit integer columns for easy use as features or targets:
- `isItDrought` — `1` if `ClimateCondition` was Drought, else `0`
- `isItRainy` — `1` if `ClimateCondition` was Rainy, else `0`

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pandas
- numpy

### Installation

```bash
pip install pandas numpy
```

### Running the Script

```bash
python main.py
```

The script will print a final null-check (`df.isnull().sum()`) to confirm the dataset is fully clean.

---

## 🐛 Known Issues

- **Humidity clipping bug:** The upper clip bound for `Humidity_percent` currently uses `high_temp` (temperature upper bound) instead of `highHumid`. This should be corrected to `highHumid` for accurate results.
- **RecordID corruption:** Entries like `??`, `-`, `P010`, and `PO41` are not corrected in the current version. Since `RecordID` is not used as a model feature, this does not affect output quality, but should be addressed for data integrity.

---

## 📝 Notes

- The dataset is small (51 rows), so median/mode imputation is preferred over model-based imputation.
- Clipping is chosen over dropping outliers to retain every available data point.
- See `Reflection.md` for a detailed discussion of decisions, challenges, and lessons learned during this project.

---

*Climate data preprocessing project — Python & Pandas.*
