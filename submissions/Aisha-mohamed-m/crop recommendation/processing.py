# processing_crop.py
# Pipeline-ka habaynta xogta dalagyada iyo kaydinta scaler-ka iyo tiirarka.
import json
import os

import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

CSV_PATH = "Crop_recommendation-1.csv"
OUT_PATH = "clean_crop_dataset.csv"

# --------------------------------
# 1) Load + initial snapshot
# --------------------------------
if not os.path.exists(CSV_PATH):
    raise FileNotFoundError(f"Faylka {CSV_PATH} lagama helin galka hadda furan!")

df = pd.read_csv(CSV_PATH)

print("\n=== INITIAL HEAD ===")
print(df.head())

print("\n=== INITIAL INFO ===")
print(df.info())

print("\n=== INITIAL MISSING VALUES ===")
print(df.isnull().sum())

# --------------------------------
# 2) Normalize categorical typos BEFORE imputation
# --------------------------------
# Sababtoo ah magacyada dalagyada qaarkood waxaa laga yaabaa inay ku qoran yihiin xarfo yaryar/waawayn ama firaaqo (spaces)
df["label"] = df["label"].astype(str).str.strip().str.lower()

# --------------------------------
# 3) Impute missing values (Haddii ay jiraan)
# --------------------------------
# Tiirarka tirada ah (Numeric) waxaa lagu buuxinayaa Median-ka
numeric_cols = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Tiirka la saadaalinayo (Categorical target) waxaa lagu buuxinayaa Mode-ka
df["label"] = df["label"].fillna(df["label"].mode()[0])

# --------------------------------
# 4) Remove duplicates
# --------------------------------
before = df.shape[0]
df = df.drop_duplicates()
print(f"\nDropped duplicates: {before} -> {df.shape[0]} rows")

# --------------------------------
# 5) IQR capping on numeric columns (Xakamaynta xogta ka fog caadiga)
# --------------------------------
def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

for col in numeric_cols:
    low_bound, high_bound = iqr_fun(df[col])
    df[col] = df[col].clip(lower=low_bound, upper=high_bound)

# --------------------------------
# 6) Class balance check (Hubinta dheelitirka dalagyada)
# --------------------------------
print("\n=== CLASS DISTRIBUTION ===")
print(df["label"].value_counts())
class_ratio = df["label"].value_counts(normalize=True).min()

if class_ratio < 0.02:  # Maadaama ay dalagyo badan yihiin, saamigu waa ka duwan yahay binary-ga
    print("\nWarning: severely imbalanced classes — consider balancing techniques.")
else:
    print("\nClass balance OK for Multi-class baseline Accuracy.")

# --------------------------------
# 7) Label Encoding for Target (Dalagyada u beddel lambaro)
# --------------------------------
# Maadaama uu yahay Multi-class (dalagyo badan), waxaan u samaynaynaa khariidad (mapping)
unique_crops = sorted(df["label"].unique())
crop_to_idx = {crop: idx for idx, crop in enumerate(unique_crops)}
idx_to_crop = {idx: crop for idx, crop in enumerate(unique_crops)}

df["label"] = df["label"].map(crop_to_idx).astype(int)

# --------------------------------
# 8) Feature engineering (Tusaale: Saamiga N-P-K iyo Nafaqada Guud)
# --------------------------------
df["Total_NPK"] = df["N"] + df["P"] + df["K"]
df["Temp_to_Humidity"] = df["temperature"] / df["humidity"].replace(0, np.nan)

# Cusboonaysii liiska tiirarka tirada ah ka dib feature engineering-ka
scale_cols = numeric_cols + ["Total_NPK", "Temp_to_Humidity"]

# --------------------------------
# 9) StandardScaler on numeric features
# --------------------------------
scaler = StandardScaler()
df[scale_cols] = scaler.fit_transform(df[scale_cols])

# Kaydi scaler-ka iyo tiirarka loogu talagalay isticmaalka API-ga dibadda ah
os.makedirs("models", exist_ok=True)
joblib.dump(scaler, "models/crop_scaler.pkl")
joblib.dump(scale_cols, "models/scale_cols.joblib")

# Kaydi khariidadda magacyada dalagyada (Crop Mapping) si loo ogaado lambar kasta dalagga uu yahay
json.dump({"crop_to_idx": crop_to_idx, "idx_to_crop": idx_to_crop}, open("models/crop_mapping.json", "w"))

TRAIN_COLUMNS = df.drop(columns=["label"]).columns.tolist()
json.dump(TRAIN_COLUMNS, open("models/train_columns.json", "w"))
print(f"\nSaved scaler, mapping + {len(TRAIN_COLUMNS)} train columns → models/")

# --------------------------------
# 10) Final snapshot + save
# --------------------------------
print("\n=== FINAL HEAD ===")
print(df.head())

print("\n=== FINAL INFO ===")
print(df.info())

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())

df.to_csv(OUT_PATH, index=False)
print(f"\nSaved cleaned dataset to {OUT_PATH}")