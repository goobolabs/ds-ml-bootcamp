"""Train and export the five parking-occupancy models used by the web app.

Run from the project root:
    python backend/train_models.py

The exported files are complete sklearn pipelines.  They contain the input
preprocessing as well as the fitted estimator, so Flask can predict directly
from the raw values submitted by the React form.
"""

from __future__ import annotations

import json
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_DIR / "ParkingDataset.xlsx"
MODEL_DIR = Path(__file__).resolve().parent / "model"
MODEL_DIR.mkdir(exist_ok=True)

FEATURES = [
    "SystemCodeNumber", "Capacity", "Occupancy", "per_usage", "year",
    "month", "day", "WorkingDay", "hour", "period",
]
NUMERIC_FEATURES = ["Capacity", "Occupancy", "per_usage", "year", "hour"]
CATEGORICAL_FEATURES = [feature for feature in FEATURES if feature not in NUMERIC_FEATURES]
LABELS = ["0 - 25", "25 - 50", "50 - 75", "75-100"]


def make_preprocessor() -> ColumnTransformer:
    return ColumnTransformer(
        transformers=[
            ("numeric", Pipeline([("imputer", SimpleImputer(strategy="median")), ("scale", StandardScaler())]), NUMERIC_FEATURES),
            ("categorical", Pipeline([("imputer", SimpleImputer(strategy="most_frequent")), ("encode", OneHotEncoder(handle_unknown="ignore"))]), CATEGORICAL_FEATURES),
        ]
    )


def occupancy_label(value: float) -> str:
    return LABELS[int(np.clip(np.rint(value), 0, len(LABELS) - 1))]


def main() -> None:
    data = pd.read_excel(DATA_PATH).drop_duplicates().copy()
    data = data.dropna(subset=["per_occupancy"])
    label_to_code = {label: code for code, label in enumerate(LABELS)}
    data = data[data["per_occupancy"].isin(label_to_code)].copy()
    X = data[FEATURES]
    y = data["per_occupancy"].map(label_to_code).astype(float)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)

    estimators = {
        "linear_regression": ("Linear Regression", LinearRegression()),
        "decision_tree": ("Decision Tree", DecisionTreeRegressor(max_depth=18, min_samples_leaf=2, random_state=42)),
        "random_forest": ("Random Forest", RandomForestRegressor(n_estimators=100, min_samples_leaf=1, random_state=42, n_jobs=1)),
        "gradient_boosting": ("Gradient Boosting", GradientBoostingRegressor(n_estimators=150, learning_rate=0.07, max_depth=3, random_state=42)),
        "svr": ("Support Vector Regression", SVR(C=5.0, epsilon=0.03, kernel="rbf")),
    }

    exported_models, results = {}, []
    for model_id, (display_name, estimator) in estimators.items():
        pipeline = Pipeline([("preprocessor", make_preprocessor()), ("model", estimator)])
        # Kernel SVR becomes prohibitively slow with all 27k rows.  A seeded,
        # stratified 6k training sample keeps it a real fitted SVR while making
        # the exported web model practical to create and serve.
        fit_X, fit_y = X_train, y_train
        if model_id == "svr":
            fit_X, _, fit_y, _ = train_test_split(X_train, y_train, train_size=6000, random_state=42, stratify=y_train)
        pipeline.fit(fit_X, fit_y)
        predictions = pipeline.predict(X_test)
        predicted_codes = np.clip(np.rint(predictions), 0, len(LABELS) - 1)
        accuracy = float((predicted_codes == y_test.to_numpy()).mean())
        metrics = {
            "id": model_id,
            "name": display_name,
            "mae": round(float(mean_absolute_error(y_test, predictions)), 4),
            "rmse": round(float(mean_squared_error(y_test, predictions) ** 0.5), 4),
            "r2": round(float(r2_score(y_test, predictions)), 4),
            "category_accuracy": round(accuracy, 4),
            "training_rows": int(len(fit_X)),
        }
        filename = f"{model_id}.joblib"
        joblib.dump(pipeline, MODEL_DIR / filename)
        metrics["file"] = filename
        exported_models[model_id] = pipeline
        results.append(metrics)
        print(f"{display_name}: accuracy={accuracy:.4f}, R2={metrics['r2']:.4f}")

    facility_capacities = (
        data.groupby("SystemCodeNumber", as_index=False)["Capacity"]
        .median()
        .rename(columns={"SystemCodeNumber": "code", "Capacity": "capacity"})
        .to_dict(orient="records")
    )
    metadata = {
        "rows": int(len(data)), "features": FEATURES, "labels": LABELS,
        "default_year": int(data["year"].mode().iloc[0]),
        "facilities": facility_capacities,
        "models": results,
    }
    (MODEL_DIR / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    print(f"\nSaved {len(results)} production pipelines to {MODEL_DIR}")


if __name__ == "__main__":
    main()
