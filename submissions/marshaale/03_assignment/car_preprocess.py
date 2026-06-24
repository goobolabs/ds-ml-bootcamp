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
