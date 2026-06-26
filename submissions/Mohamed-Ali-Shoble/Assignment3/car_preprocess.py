import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

print("---------------------------------------------------------------------\n1. Load and inspect\n")
PATH=r"D:\Downloads\DS-ML COURSE/raw_car_dataset.csv"
df=pd.read_csv(PATH)
print("The first 10 samples of the Dataset:\n",df.head(10))
print("\nThe shape of the Dataset we have (Rows and Columns):\n",df.shape)
print("\nMore info to our Dataset:")
print(df.info())
print("\nthe sum of the columns with null values:\n",df.isnull().sum())
print("\nLocation value counts:")
print(df["Location"].value_counts(dropna=False))
print("\nfound here that the column(Label) price is (str) have to convert to numbers")
print("these (Odometer_km,Doors,Location) columns have missing values have to fill it.")

print("--------------------------------------------------------------------------------------------------\n2. clean target formatting(Price)\n")
df["Price"]=df["Price"].replace(r"[\$,]", "", regex=True).astype(float)
print("After removing the symbols and converting to numeric:")
print(df["Price"].info())
print("\nthe skewness of the target column(Price):",df["Price"].skew(),"\nneed to solve it by IQR for the outlier\n")

print("--------------------------------------------------------------------------------------------------\n3. Fix Category Errors before Imputation\n")
print("Before fixing the column Location:\n",df["Location"].value_counts(dropna=False))
df["Location"]=df["Location"].replace({"Subrb":"Suburb", "??":pd.NA})
print("\nAfter fixing the column Location:\n",df["Location"].value_counts(dropna=False))

print("--------------------------------------------------------------------------------------------------\n4. Impute Missing Values\n")
df["Odometer_km"]=df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"]=df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"]=df["Location"].fillna(df["Location"].mode()[0])
df["Accidents"]=df["Accidents"].fillna(df["Accidents"].mode()[0])
print("After filling the null columns with median and mode:")
print(df["Odometer_km"].isnull().sum())
print(df["Doors"].isnull().sum())
print(df["Location"].isnull().sum())
print(df["Accidents"].isnull().sum())

print("--------------------------------------------------------------------------------------------------\n5. Remove Duplicates\n")
before=df.shape
df=df.drop_duplicates()
after=df.shape
print("Before removed duplicates:",before)
print("After removed duplicates:",after)

print("--------------------------------------------------------------------------------------------------\n6. Outliers (IQR capping)\n")

def iqr_outliers(columns,x=1.5):
    q1,q3=columns.quantile([0.25, 0.75])
    iqr=q3 - q1
    lower=q1 - x*iqr
    upper=q3 + x*iqr
    return lower,upper

print("\nthe skewness of the target column(Price):",df["Price"].skew(),"\nneed to solve it by IQR for the outlier\n")
print("\nthe skewness of the column(Odometer_km):",df["Odometer_km"].skew(),"\nneed to solve it by IQR for the outlier\n")

lowest_price,highest_price=iqr_outliers(df["Price"])
lowest_km,highest_km=iqr_outliers(df["Odometer_km"])
print("lowest price: ",lowest_price,"\nhighest price:",highest_price)
print("lowest km: ",lowest_km,"\nhighest km:",highest_km)

df["Price"]=df["Price"].clip(lower=lowest_price,upper=highest_price)
df["Odometer_km"]=df["Odometer_km"].clip(lower=lowest_km,upper=highest_km)

print("\nthe column(Price) after the IQR:",df["Price"].describe())
print("\nthe column(Odometer_km) after the IQR:",df["Odometer_km"].describe())

print("--------------------------------------------------------------------------------------------------\n7. One-Hot Encode Categorical(s)\n")
df=pd.get_dummies(df, columns=["Location"], drop_first=False,dtype=int)
print("After applied one-hot-encoding:")
print(df.head())

print("--------------------------------------------------------------------------------------------------\n8. Feature Engineering\n")
CURRENT_YEAR=2026
df["Car_Age"]=CURRENT_YEAR-df["Year"]
df["Km_per_year"]=df["Odometer_km"]/(df["Car_Age"]).replace(0,np.nan)
df["Is_Urban"]=df["Location_Suburb"].astype(int)
df["LogPrice"]=np.log1p(df["Price"])
print(df.head(10))

print("--------------------------------------------------------------------------------------------------\n9. Feature Scaling (X only)\n")
not_scale={"Price", "LogPrice"}
num_columns=df.select_dtypes(include=["int64", "float64"]).columns.to_list()
not_include_scale=[col for col in df.columns if col.startswith("Location_")] + ["Is_Urban"]
to_scale=[col for col in num_columns if col not in not_scale and col not in not_include_scale]
scaler=StandardScaler()
df[to_scale]=scaler.fit_transform(df[to_scale])

print("--------------------------------------------------------------------------------------------------\n10. Final Checks & Save\n")
print("After scaling:\n",df.head())
print("\nfinal info:\n",df.info())
print("\nfinal count missing values:\n",df.isnull().sum())
SAVE_PATH=r"D:\Downloads\DS-ML COURSE/clean_car_dataset.csv"
df.to_csv(SAVE_PATH,index=False)
print("\nsaved!\n")

