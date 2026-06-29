# Car Price Dataset - Preprocessing Pipeline

## Dataset Overview

This dataset contains car price information with various features including odometer readings, number of doors, accident history, location, and manufacturing year.

## Columns

| Column | Description | Data Type |
|--------|-------------|-----------|
| Price | Car price (with currency symbols) | String/Float |
| Odometer_km | Kilometers driven | Float |
| Doors | Number of doors | Float |
| Accidents | Number of accidents | Float |
| Location | City/Suburb/Rural | String |
| Year | Manufacturing year | Float |

## Key Issues in Raw Data

- **Price**: Mixed formats ($1,500 vs 1500.0), currency symbols
- **Location**: Typos (Subrb), unknowns (??), missing values
- **Missing Values**: Present in Location and Year columns
- **Duplicates**: Some duplicate rows present
- **Outliers**: Extreme values in Price and Odometer_km

## Preprocessing Steps

1. Load and inspect data
2. Clean Price column (remove $, convert to numeric)
3. Fix Location errors (typos, unknowns)
4. Impute missing values
5. Remove duplicates
6. Handle outliers (IQR capping)
7. One-hot encode Location
8. Feature engineering (CarAge, Km_per_year, Is_Urban, LogPrice)
9. Scale continuous features
10. Save cleaned dataset

## Output

- `clean_car_dataset.csv` - Cleaned dataset ready for modeling
- Shape: 140 rows × 24 columns

## Requirements

- pandas==3.0.3
- numpy==2.5.0
- scipy==1.18.0
- scikit-learn==1.9.0