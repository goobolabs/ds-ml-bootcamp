# Car Dataset Preprocessing

This project cleans and prepares a raw car dataset for analysis or machine learning.

## Files

```text
assignment3/
├── car_preprocess.py
├── raw_car_dataset.csv
├── clean_car_dataset.csv
├── reflection.md
└── README.md
```

## What the Script Does

The script performs these main steps:

1. Loads the raw dataset from `raw_car_dataset.csv`.
2. Cleans the `Price` column by removing symbols like `$` and commas.
3. Fixes incorrect category values in `Location`.
4. Handles missing values:

   * Median for `Odometer_km`
   * Mode for `Doors` and `Location`
5. Removes duplicate rows.
6. Caps outliers in `Price` and `Odometer_km` using the IQR method.
7. One-hot encodes the `Location` column.
8. Creates new features:

   * `Car_Age`
   * `km_per_year`
   * `accident_rate`
   * `Is_City`
   * `LogPrice`
9. Scales selected numeric columns using `StandardScaler`.
10. Saves the cleaned dataset as `clean_car_dataset.csv`.

## Requirements

Install the required libraries:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pandas numpy scikit-learn
```

## How to Run

From the project root folder, run:

```bash
python submissions/Abdikani94/assignment3/car_preprocess.py
```

The cleaned file will be saved inside the same folder as the script:

```text
submissions/Abdikani94/assignment3/clean_car_dataset.csv
```

## Output

The final dataset is cleaned, encoded, feature-engineered, scaled, and ready for analysis or machine learning.
