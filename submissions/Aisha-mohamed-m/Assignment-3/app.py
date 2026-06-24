print("Loading data and Exploring data...")
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

print("Reading the csv data....")
CSV_PATH = "raw_car_dataset.csv"
df = pd.read_csv(CSV_PATH)
print(df.head())

print("Data analysis complete.")
print(df.describe())
print(df.info())
print(df.shape)

print("Checking for null values in the dataset...")
print(df.isnull().sum())

print("cleaning the data...")
# 1. Ka saar calaamadaha dollar-ka iyo koodhka kale ee Price
df["Price"] = df["Price"].replace(r"[$,]", "", regex=True).astype(float)
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})
print(df["Location"].value_counts())

# 2. Buuxi meelaha banaan (Imputation)
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

print(df.isnull().sum())

print("Removing duplicates from the dataset...")
df = df.drop_duplicates()
print(df.shape)

print("Handling outliers using IQR...")
# 3. Ka saar outliers-ka iyadoo la adeegsanayo IQR
def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - (k * iqr)
    upper = q3 + (k * iqr)
    return lower, upper

low_price, high_price = iqr_fun(df["Price"])
low_size, high_size = iqr_fun(df["Odometer_km"])

df["Price"] = df["Price"].clip(lower=low_price, upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_size, upper=high_size)

print("one hot encoding the categorical features...")
df = pd.get_dummies(df, columns=["Location"], drop_first=True)
print(df.head())

print("feature engineering on numerical features...")
CURRENT_YEAR = 2026
df["carage"] = CURRENT_YEAR - df["Year"]
df["km_per_Year"] = df["Odometer_km"] / (df["carage"] + 1)
df["accident_rate"] = df["Accidents"] / df["Odometer_km"]

# 4. Samee Groupby si nidaamsan (Hubi qoraalka Suburb)
df["Temp_location"] = "Rural"
if "Location_City" in df.columns:
    df.loc[df["Location_City"] == 1, "Temp_location"] = 'City'
if "Location_Suburb" in df.columns:
    df.loc[df["Location_Suburb"] == 1, "Temp_location"] = 'Suburb'

# Xariiqan hadda wuxuu u qoran yahay si nidaamsan (Avg yar leh)
df["Location_Avg_Price"] = df.groupby(by="Temp_location")["Price"].transform("mean")
df.drop(columns=["Temp_location"], inplace=True)
df["logPrice"] = np.log1p(df["Price"])

print("Scaling the numerical features...")
dont_scale = {"Price", "logPrice"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()

# Sifee tiirarka si sax ah
num_features_to_scale = [
    c for c in numeric_cols 
    if c not in dont_scale and not c.startswith("Location")
] 

scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])

print("saving data.")
OUT_PATH = "cars_clean.csv"
# 5. index=False ku dar si aan faylku u khasan
df.to_csv(OUT_PATH, index=False)
print("saved successfully!")


