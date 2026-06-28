import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.preprocessing import StandardScaler

print("\n========= PART ZERO SETUP ============")
ROOT_DIR=Path(__file__).parent.parent.parent.parent
DATASET_DIR = f"{ROOT_DIR}/dataset"
CSV_FILE=f"{DATASET_DIR}/raw_car_dataset.csv"
OUT_PATH=f"{Path(__file__).parent}/data/car_clean_dataset.csv"

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

df = pd.get_dummies(df,columns=['Location'],drop_first=False,dtype='int')

print(df)

print("\n========= PART EIGHT FEATURE ENGINEERING ============")

CURRENT_YEAR = 2026
df['Car_Age'] = CURRENT_YEAR - df['Year']
df['Km_per_year'] = df['Odometer_km'] / df['Car_Age'].replace(0,np.nan)
df['Is_Urban'] = df['Location_city'].astype(int)
df['LogPrice'] = np.log1p(df['Price'])
print(df)

print("\n========= PART NINE FEATURE SCALING ============")
print(df.info())
numeric_cols = df.select_dtypes(include=['int64','float64']).columns.to_list()
print(numeric_cols)
exclude_scale = [x for x in numeric_cols if x.startswith('Location')] + ['LogPrice','Price','Is_Urban']
print(exclude_scale)
to_scale_cols = [x for x in numeric_cols if x not in exclude_scale]
print(to_scale_cols)

scaler = StandardScaler()
df[to_scale_cols] = scaler.fit_transform(df[to_scale_cols])

print(df[to_scale_cols])

print("\n========= PART TEN CHECK AND SAVE ============")
print(df.head())
print(df.describe())
print(df.info())
print(df.isna().sum())

df.to_csv(OUT_PATH)