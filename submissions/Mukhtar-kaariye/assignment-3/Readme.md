#  Car Dataset Preprocessing

This project cleans and prepares a raw car dataset for analysis and machine learning.  
It applies a full data preprocessing pipeline including cleaning, feature engineering, encoding, scaling, and saving the final dataset.

##  Project Structure
assignment3/
├── car_preprocess.py
├── raw_car_dataset.csv
├── clean_car_dataset.csv
├── reflection.md
└── README.md

##  What the Script Does

The script performs the following steps:

### 1. Load Dataset
- Loads raw data from `raw_car_dataset.csv`
- Displays basic structure (shape, info, missing values)

### 2. Clean Price Column
- Removes currency symbols (e.g. `$`)
- Removes commas
- Converts Price into numeric format

### 3. Fix Category Errors
- Cleans `Location` column
- Standardizes spelling mistakes (e.g., Subrb → Suburb)
- Converts invalid values like `??` and `unknown` into missing values

### 4. Handle Missing Values
- Odometer_km → Median
- Doors → Mode
- Accidents → Mode
- Location → Mode
### 5. Remove Duplicates
- Detects and removes duplicate rows
- Ensures each record is unique

### 6. Outlier Handling (IQR Capping)
- Applies IQR method to detect outliers
- Caps extreme values in:
  - Price
  - Odometer_km

### 7. One-Hot Encoding
- Converts `Location` into numeric columns:
  - Location_City
  - Location_Suburb
  - Location_Rural

### 8. Feature Engineering
New features created:

- **CarAge** → Age of the car (2026 - Year)
- **Km_per_year** → Average yearly usage
- **Is_Urban** → 1 if City/Suburb, else 0
- **LogPrice** → log(Price + 1) (target variable, not feature)

### 9. Feature Scaling
- Standardizes numerical features using `StandardScaler`
- Scaled features:
  - Odometer_km
  - Year
  - CarAge
  - Km_per_year
- Does NOT scale:
  - Price
  - LogPrice
  - Dummy variables
### 10. Save Cleaned Dataset
- Final dataset saved as:

clean_car_dataset.csv

##  Goal of This Project

To practice real-world data preprocessing techniques used in machine learning, including:

- Data cleaning
- Handling missing values
- Feature engineering
- Encoding categorical variables
- Scaling numerical features
## Output

After running the script, you get a fully cleaned dataset ready for machine learning models.


