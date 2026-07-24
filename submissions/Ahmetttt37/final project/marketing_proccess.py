import pandas as pd
import numpy as np
import os
import joblib
from sklearn.preprocessing import StandardScaler

# Load Dataset

CSV_PATH = r"C:\Users\Ali Black\Desktop\bootcamp1\ds-ml-bootcamp\submissions\Ahmetttt37\final project\marketing_campaign.csv"

df = pd.read_csv(CSV_PATH, sep="\t")

# Missing Values

df["Income"] = df["Income"].fillna(df["Income"].median())

# Date Processing

df["Dt_Customer"] = pd.to_datetime(
    df["Dt_Customer"],
    format="%d-%m-%Y"
)

CURRENT_DATE = pd.Timestamp("2026-01-01")

df["Customer_Years"] = (
    CURRENT_DATE - df["Dt_Customer"]
).dt.days / 365


# Feature Engineering

CURRENT_YEAR = 2026
df["Age"] = CURRENT_YEAR - df["Year_Birth"]
df["Children"] = (df["Kidhome"] + df["Teenhome"])
df["TotalSpent"] = (df["MntWines"] + df["MntFruits"]  + df["MntMeatProducts"]  + df["MntFishProducts"] + df["MntSweetProducts"] + df["MntGoldProds"])
df["TotalPurchases"] = (df["NumWebPurchases"] + df["NumCatalogPurchases"] + df["NumStorePurchases"])
df["TotalAcceptedCmp"] = (df["AcceptedCmp1"] + df["AcceptedCmp2"]  + df["AcceptedCmp3"] + df["AcceptedCmp4"] + df["AcceptedCmp5"])

# Clean Age Outliers
df = df[(df["Age"] > 18) &(df["Age"] < 100)]

# Clean Marital Status

df["Marital_Status"] = df["Marital_Status"].replace(
{
    "Married": "Partner",
    "Together": "Partner",
    "Single": "Single",
    "Divorced": "Single",
    "Widow": "Single",
    "Alone": "Single",
    "YOLO": "Single",
    "Absurd": "Single"
}
)

# One Hot Encoding

df = pd.get_dummies(df, columns=["Education", "Marital_Status"], drop_first=True, dtype=int)

# Drop Unnecessary Columns

df = df.drop(columns=["ID", "Dt_Customer", "Year_Birth", "Z_CostContact", "Z_Revenue"])

# Features and Target

X = df.drop(columns=["Response"])
y = df["Response"]

# Scaling

scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X),columns=X.columns)

# Save Files

os.makedirs(
    "models",
    exist_ok=True
)
# Save scaler

joblib.dump(
    scaler,
    "models/scaler.pkl"
)
# Save processed features

X_scaled.to_csv(
    "models/processed_features.csv",
    index=False)
# Save target

y.to_csv(
    "models/target.csv",
    index=False)

# Check Result

print("Preprocessing Completed Successfully!")
print("Features Shape:", X_scaled.shape)
print("Target Shape:", y.shape)
print(X_scaled.head())

