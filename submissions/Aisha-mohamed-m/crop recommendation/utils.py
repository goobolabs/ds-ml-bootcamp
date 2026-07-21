
import json
import numpy as np
import joblib
import pandas as pd

# Soo rar xogta lagama maarmaanka ah ee habaynta
TRAIN_COLUMNS = json.load(open("models/train_columns.json"))
SCALER = joblib.load("models/crop_scaler.pkl")
SCALE_COLS = joblib.load("models/scale_cols.joblib")


def prepare_features_from_raw(record: dict) -> pd.DataFrame:
    """
    Convert raw agricultural input into the engineered, scaled feature row
    that matches training (columns == TRAIN_COLUMNS).
    """
    # 1) Soo qabashada xogta cayriin ee laga soo diray API-ga ama Form-ka
    n = float(record["N"])
    p = float(record["P"])
    k = float(record["K"])
    temp = float(record["temperature"])
    humidity = float(record["humidity"])
    ph = float(record["ph"])
    rainfall = float(record["rainfall"])

    # 2) Feature Engineering )
    total_npk = n + p + k
    # Ka badbaadi xogta in loo qaybiyo eber (zero division error)
    temp_to_humidity = temp / humidity if humidity != 0 else 0.0

    # 3) Dhisidda safka xogta oo u dhigma tiirarkii saxda ahaa ee tababarka
    row = {col: 0.0 for col in TRAIN_COLUMNS}
    values = {
        "N": n,
        "P": p,
        "K": k,
        "temperature": temp,
        "humidity": humidity,
        "ph": ph,
        "rainfall": rainfall,
        "Total_NPK": total_npk,
        "Temp_to_Humidity": temp_to_humidity,
    }
    
    # Ku shub xogta meelaha ay ku leeyihiin safka dhexdiisa
    for name, val in values.items():
        if name in row:
            row[name] = float(val)

    # U beddel DataFrame hal saf ah
    df_one = pd.DataFrame([row], columns=TRAIN_COLUMNS)

    # 4) Nadiifinta iyo Miisaamidda xogta (Scaling)
    cols_to_scale = [c for c in SCALE_COLS if c in df_one.columns]
    df_one[cols_to_scale] = SCALER.transform(df_one[cols_to_scale])

    return df_one