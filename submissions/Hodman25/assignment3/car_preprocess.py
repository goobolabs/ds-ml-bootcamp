import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler



DATA_PATH = "raw_car_dataset (1).csv"

df = pd.read_csv(DATA_PATH)

print(df.shape)

print(df.head(10))

print(df.info())

#inaa ogado mising valueska
print("missig values of all columns")
print(df.isnull().sum())

#location value counts
print(df['Location'].value_counts(dropna=False))

#Clean Target Formatting (Price)
df['Price'] = df['Price'].replace(r"[\$,]", "", regex=True).astype(float)
# print(df.head(30))

#Report the dtype and skewness.
print(df['Price'].skew())

#Fix Category Errors before Imputation
df['Location'] = df['Location'].replace({"Subrb": "Suburb", "??": pd.NA})
print(df["Location"].value_counts(dropna=False))

#in labuuxiyo columnka odometer_km
df['Odometer_km'] = df['Odometer_km'].fillna(df['Odometer_km'].median())

# impute Doors
df['Doors'] = df['Doors'].fillna(df['Doors'].mode()[0])

#location
df['Location'] = df['Location'].fillna(df['Location'].mode()[0])
print(df.isnull().sum())

#Remove Duplicates
before = df.shape
df = df.drop_duplicates()
after = df.shape
print("before data: ", before, "after removing duplicates: ", after)

#Outliers (IQR capping) 
def outlier_fun(series, k=1.5):
    q1,q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

low_price, high_price = outlier_fun(df['Price'])
low_odometer, high_odometer = outlier_fun(df['Odometer_km']) 

print("=====IQR od price and odometer_km")
print("low price is: ", low_price, "high price is: ", high_price)
print("low odometer_km is: ", low_odometer, "high odometer_km is: ", high_odometer)

# clip for Price and Odometer_km.
df['Price'] = df['Price'].clip(lower=low_price, upper=high_price)
df['Odometer_km'] = df['Odometer_km'].clip(lower=low_odometer, upper=high_odometer)
print("After capping ")
print(df['Price'].describe())
print(df['Odometer_km'].describe())

#One-Hot Encode Categorical(s)
df = pd.get_dummies(df, columns=['Location'], drop_first=False, dtype=int)
print([c for c in df.columns if c.startswith("Location")])
print(df.head())

#Feature Engineering
CURRENT_YEAR = 2026
df['car_Age'] = CURRENT_YEAR - df['Year']

df['Km_per_year'] =  df['Odometer_km'] / df['car_Age']
print(df.head())

df['Is_Urban'] = df['Location_City'].astype(int)

#Add LogPrice
df['Log_price'] =  np.log1p(df['Price'])
print(df.head())

#Feature Scaling
not_scale = {"Price", "Log_price"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
exclude = [f for f in df.columns if f.startswith("Location_")] + ["Is_Urban"]
features_scale = [c for c in numeric_cols if c not in not_scale and c not in exclude]
scaler = StandardScaler()
df[features_scale] = scaler.fit_transform(df[features_scale])
print(df.head())

#Final Checks
print("====checking ======")
print(df.info())
print(df.isnull().sum())
print(df.describe())

#saving
PATH = 'clean_car_dataset.csv'
df.to_csv(PATH, index=False)
print("save cleaned data")

