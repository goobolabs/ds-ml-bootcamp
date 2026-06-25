import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

#----1.Load & Inspect----#
df=pd.read_csv('raw_car_dataset.csv')
# print(df.head(10))
# print(df.info())
# print(df.isnull().sum())
# # i make this step to chech if there a typo error in the columns
# print(df['Location'].value_counts())

#----2. Clean Target Formatting (Price)----#
# remove the $ sign and convert to float
df["Price"]=df["Price"].replace(r"[\$,?]", "", regex=True).astype(float)
# print("Before skew:",df["Price"].skew())  
# df["Price"].skew()=7.87 so we will use log transformation to reduce the skewness because there is so much outliers in the price column
df["Price_log"]=np.log1p(df["Price"]) 
# print("after skew:", df["Price_log"].skew())  
# print(df[["Price","Price_log"]].dtypes)

#----3.Fix Category Errors before Imputation (Location)----#
# print("Before fixing category errors:", df['Location'].value_counts())
df["Location"]=df["Location"].replace({"Subrb":"Suburb","??": pd.NA})
# print("After fixing category errors:", df['Location'].value_counts())

#----4Impute Missing Values (justify choices)-----#
# print("Before : \n", df.isnull().sum())
# There is 12 missing values in the Location column,7 odometer_km and 7 doors missing values
df["Location"]=df["Location"].fillna(df["Location"].mode()[0]) 
df["Odometer_km"]=df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"]=df["Doors"].fillna(df["Doors"].mode()[0])
# print("After : \n", df.isnull().sum())
# Now there is no missing values in our dataset

#----5.Remove Duplicates----#
# print("Before : \n", df.duplicated())
# print("Number of duplicates we will remove:", df.duplicated().sum())
# print("before duplicate rows:", df.shape)
# so now we have 5 duplicates in our dataset, we will remove them
df=df.drop_duplicates()
# print("After dropping duplicates :", df.shape)

#----6.Outliers (IQR capping)s)----#
print("Before removing outliers:", df.shape)
def remove_outliers_iqr(columns, k=1.5):
    q1,q3=columns.quantile([0.25,0.75])
    iqr=q3-q1
    lower=q1-(k*iqr)
    upper=q3+(k*iqr)
    return lower, upper
lower_Price, upper_Price = remove_outliers_iqr(df["Price_log"])
lower_Odometer_km, upper_Odometer_km = remove_outliers_iqr(df["Odometer_km"])

df["Price_log"]=df["Price_log"].clip(lower_Price, upper_Price)
df["Odometer_km"]=df["Odometer_km"].clip(lower_Odometer_km, upper_Odometer_km)
# print("After removing outliers:", df.shape)
# print(df["Price_log"].skew())

# ----7.One-Hot Encode Categorical(s)----#
# df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")
df=pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")
# print(df.head(5))

#----8.Feature Engineering (no leakage)----# 
current_year = 2026
df["carAge"] = current_year - df["Year"]
df["Km_per_year"] = df["Odometer_km"] / df["carAge"].replace(0,1)
df["Accidents_per_year"] = df["Accidents"] / df["carAge"].replace(0,1)
df["Km_per_Accident"] = df["Odometer_km"] / df["Accidents"].replace(0,1)
df["Is_Urban"] = (df["Location_City"] == 1 )| (df["Location_Suburb"] == 1)
df["Is_Urban"] = df["Is_Urban"].astype(int)
# print(df.head(10))
df["Price_log"] = np.log1p(df["Price"])

#----9.Feature Scaling (X only)----#
dont_scale={"Price","Price_log"}
numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
exclude = [c for c in df.columns if c.startswith("Location_")] + ["Is_Urban"]
num_features_to_scale = [c for c in numeric_columns if c not in dont_scale and c not in exclude]

scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])

 #---10.Final Checks---# 
# === FINAL SNAPSHOT ===
print("\n=== FINAL HEAD ===")
print(df.head())

print("\n=== FINAL INFO ===")
print(df.info())

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())

#----10.Save Preprocessed Data----#
df.to_csv("Cleaned_Car_Dataset.csv", index=False)
