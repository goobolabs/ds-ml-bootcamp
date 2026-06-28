import pandas as pd
import numpy as np
import sklearn as skl
from sklearn.preprocessing import StandardScaler

# STEP 1: Load & Inspect

# Loading data
CSV_PATH = "./dataset/raw_car_dataset.csv"
dataFrame = pd.read_csv(CSV_PATH)

print(dataFrame.head(10)) # displaying the first 10 row
print("________________\n")
print("The shape of data (rows, columns): ", dataFrame.shape)
print("________________\n")

print(dataFrame.info) # displaying complete information about the data
print("________________\n")

print("Counting the missing data:\n", dataFrame.isnull().sum())
print("________________\n")

print(dataFrame['Location'].value_counts()) # displaying Location value counts
print("________________\n")

# STEP 2: Clean Target Formatting (Price)

# removing "$" and "," symbols from the price column then turning it to numerical
dataFrame['Price'] = dataFrame['Price'].replace(r"[\$,]", "", regex=True).astype(float)

print("Price datatype: ", dataFrame['Price'].dtype) # displaying the data type of Price
print("Price skewness: ", dataFrame['Price'].skew()) # displaying the skew value of Price
print("________________\n")

# STEP 3: Fix Category Errors before Imputation
dataFrame['Location'] = dataFrame['Location'].replace({"Subrb": "Suburb", "??": pd.NA})

print(dataFrame.isnull().sum()) # recounting missing value again
print("________________\n")

# STEP 4: Impute Missing Values (justify choices)
dataFrame['Odometer_km'] = dataFrame['Odometer_km'].fillna(dataFrame['Odometer_km'].median())
dataFrame['Doors'] = dataFrame['Doors'].fillna(dataFrame['Doors'].mode()[0])
dataFrame['Accidents'] = dataFrame['Accidents'].fillna(dataFrame['Accidents'].mode()[0])
dataFrame['Location'] = dataFrame['Location'].fillna(dataFrame['Location'].mode()[0])

print(dataFrame.isnull().sum()) # confirming imputed missing counts
print("________________\n")

# STEP 5: Remove Duplicates
beforeDataFrameShape = dataFrame.shape
dataFrame = dataFrame.drop_duplicates()
afterDataFrameShape = dataFrame.shape

print(f"Dropped duplicate rows: {beforeDataFrameShape} -> {afterDataFrameShape}")
print("________________\n")

# STEP 6: Outliers (IQR capping)
def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

lowPrice, highPrice = iqr_fun(dataFrame['Price'])
lowOdometer_km, highOdometer_km = iqr_fun(dataFrame['Odometer_km'])

dataFrame['Price'] = dataFrame['Price'].clip(lower=lowPrice, upper=highPrice)
dataFrame['Odometer_km'] = dataFrame['Odometer_km'].clip(lower=lowOdometer_km, upper=highOdometer_km)

print("---- AFTER IQR ----")
print("Price: ", dataFrame['Price'].describe())
print("\nOdometer_km: ", dataFrame['Odometer_km'].describe())
print("_______________\n")

# STEP 7: One-Hot Encode Categorical(s)
dataFrame = pd.get_dummies(dataFrame, columns=['Location'], drop_first=False, dtype="int")

# STEP 8: Feature Engineering (no leakage)
CURRENT_YEAR = 2026
dataFrame['CarAge'] = CURRENT_YEAR - dataFrame['Year']
dataFrame['Km_per_year'] = dataFrame['Odometer_km'] / dataFrame['CarAge']
dataFrame['LogPrice'] = np.log1p(dataFrame['Price'])
dataFrame['Is_Urban'] = dataFrame['Location_City'].astype(int)

# print(dataFrame.head(10))

# STEP 9: Feature Scaling (X only)
dontScale = {"Price", "LogPrice"}
numericColumns = dataFrame.select_dtypes(include=["int64", "float64"]).columns.tolist()
exclude = [column for column in dataFrame.columns if column.startswith("Location_")] + ['Is_Urban']
numFeaturesToScale = [col for col in numericColumns if col not in dontScale and col not in exclude]

scaler = StandardScaler()
dataFrame[numFeaturesToScale] = scaler.fit_transform(dataFrame[numFeaturesToScale])

print(dataFrame[numFeaturesToScale].head(10))
print("_______________\n")

# STEP 10: Final Checks & Save
print("---- Final Head ----")
print(dataFrame.head())

print("---- Final Info ----")
print(dataFrame.info)

print("---- Final Missing Values ----")
print(dataFrame.isnull().sum())

# Saving data
OUT_PATH = "./dataset/clean_car_dataset.csv"
dataFrame.to_csv(OUT_PATH, index=False)
