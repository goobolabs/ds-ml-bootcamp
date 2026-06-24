import pandas as pd
import numpy as np
from pathlib import Path

print("\n========= PART ZERO SETUP ============")
ROOT_DIR=Path(__file__).parent.parent.parent.parent
DATASET_DIR = f"{ROOT_DIR}/dataset"
CSV_FILE=f"{DATASET_DIR}/raw_car_dataset.csv"

print(ROOT_DIR)
print(DATASET_DIR)
print(CSV_FILE)

print(pd.__version__)
print(np.__version__)

print("\n========= PART ONE LOADING AND EDA ============")

df = pd.read_csv(CSV_FILE)
 
print(df)
print("Dataset Shape (Rows,Columns):",df.shape)
columns = df.columns.to_list()
print('Column names:',columns)
print('==== Dataset information =====')
print(df.info())
print('====== Sum of each column missing values ======\n',df.isna().sum())
categorical_columns = ['Location']
print('==== Categorical columns value counts =====\n',df[categorical_columns].value_counts())

print("\n========= PART TWO CLEAN TARGET & FORMAT ============")
print('before cleaning & formatting')
print(df['Price'])
df['Price'] = df['Price'].replace(r'[^0-9.]','',regex=True)
df['Price'] = df['Price'].replace('',np.nan).astype(float)
print('after cleaning & formatting')
print(df['Price'])
print(df['Price'].describe())

print("\n========= PART THREE FIX CATEGORICAL DATA STANDARD AND CONSISTENCE ============")
df['Location'] = df['Location'].str.strip()
print(df['Location'].value_counts())
df['Location'] = df['Location'].str.lower()
print(df['Location'].value_counts())
df['Location'] = df['Location'].replace({'subrb':'suburb','??':np.nan})
print(df['Location'].value_counts())

print("\n========= PART FOUR IMPUTE MISSING VALUEs ============")
print('before filling\n',df.isna().sum())
df['Location'] = df['Location'].fillna(df['Location'].mode()[0])
df['Accidents'] = df['Accidents'].fillna(df['Accidents'].mode()[0])
df['Doors'] = df['Doors'].fillna(df['Doors'].mode()[0])
df['Odometer_km'] = df['Odometer_km'].fillna(df['Odometer_km'].median())
print('after filled\n',df.isna().sum())
print(df.describe())

print("\n========= PART FIVE REMOVE DUPLICATES ============")
print("Before removing duplicates dataset Shape (Rows,Columns):",df.shape)
df = df.drop_duplicates()
print("After removed duplicates dataset Shape (Rows,Columns):",df.shape)

print("\n========= PART SIX HANDLE OUTLIERS (IQR CAPPING) ============")

def calculate_iqr_range(series:pd.Series,k=1.5):
    print(series.name,':')
    q1,q3 = series.quantile([0.25,0.75])
    print('Quantiles',[q1,q3])
    iqr = q3 - q1
    print('IQR',iqr)
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    print('lower',lower)
    print('upper',upper)
    return lower,upper

lower_price,upper_price = calculate_iqr_range(df['Price'])
lower_odometer_km,upper_odometer_km = calculate_iqr_range(df['Odometer_km'])

print('\nbefore clipping\n',df[['Price','Odometer_km']].describe())
df['Price'] = df['Price'].clip(lower=lower_price,upper=upper_price)
df['Odometer_km'] = df['Odometer_km'].clip(lower=lower_odometer_km,upper=upper_odometer_km)
print('\nafter clipped\n',df[['Price','Odometer_km']].describe())

print("\n========= PART SEVEN ONE HOT ENCODING ============")

df = pd.get_dummies(df,columns=['Location'],drop_first=False)

print(df)

