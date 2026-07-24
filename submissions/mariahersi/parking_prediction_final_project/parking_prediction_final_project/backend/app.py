from __future__ import annotations

import json
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "model"
METADATA_PATH = MODEL_DIR / "metadata.json"

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# The simple public form only asks for the seven details a user can reasonably
# provide.  The remaining model inputs are completed below by the backend.
REQUIRED_FIELDS = ["Capacity", "Occupancy", "month", "day", "WorkingDay", "hour", "period"]


def load_registry():
    metadata = json.loads(METADATA_PATH.read_text(encoding="utf-8"))
    registry = {}
    for model in metadata["models"]:
        model_path = MODEL_DIR / model["file"]
        if model_path.exists():
            registry[model["id"]] = {**model, "pipeline": joblib.load(model_path)}
    return metadata, registry


METADATA, MODELS = load_registry()


def label_from_prediction(value: float) -> tuple[int, str]:
    code = int(np.clip(np.rint(value), 0, len(METADATA["labels"]) - 1))
    return code, METADATA["labels"][code]


def nearest_facility_code(capacity: float) -> str:
    facilities = METADATA.get("facilities", [])
    if not facilities:
        raise ValueError("Parking facility metadata is unavailable. Run train_models.py again.")
    return min(facilities, key=lambda facility: abs(float(facility["capacity"]) - capacity))["code"]


@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "models_loaded": len(MODELS)})


@app.get("/api/models")
def models():
    return jsonify({"models": [{key: value for key, value in model.items() if key != "pipeline"} for model in MODELS.values()]})


@app.post("/api/predict")
def predict():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Send a valid JSON object."}), 400
    missing = [field for field in REQUIRED_FIELDS if data.get(field) in (None, "")]
    if missing:
        return jsonify({"error": "Missing required fields", "fields": missing}), 400
    model_id = data.get("model_id", "random_forest")
    selected = MODELS.get(model_id)
    if selected is None:
        return jsonify({"error": "Choose a valid saved model.", "available_models": list(MODELS)}), 400
    try:
        capacity, occupancy = float(data["Capacity"]), float(data["Occupancy"])
        hour = int(data["hour"])
        if capacity <= 0: raise ValueError("Capacity must be greater than 0.")
        if occupancy < 0 or occupancy > capacity: raise ValueError("Occupancy must be between 0 and Capacity.")
        if not 0 <= hour <= 23: raise ValueError("Hour must be between 0 and 23.")
        period = str(data["period"]).strip().upper()
        if period not in {"AM", "PM"}: raise ValueError("Period must be AM or PM.")
        system_code = nearest_facility_code(capacity)
        per_usage = round((occupancy / capacity) * 100, 2)
        year = int(METADATA.get("default_year", 2016))
        row = pd.DataFrame([{
            "SystemCodeNumber": system_code, "Capacity": capacity,
            "Occupancy": occupancy, "per_usage": per_usage, "year": year,
            "month": str(data["month"]).strip(), "day": str(data["day"]).strip(),
            "WorkingDay": str(data["WorkingDay"]).strip(), "hour": hour, "period": period,
        }])
        raw_prediction = float(selected["pipeline"].predict(row)[0])
        prediction_code, occupancy_level = label_from_prediction(raw_prediction)
        return jsonify({
            "model": {key: value for key, value in selected.items() if key not in {"pipeline", "file"}},
            "prediction_code": prediction_code,
            "prediction": occupancy_level,
            "occupancy_level": occupancy_level,
            "raw_prediction": round(raw_prediction, 3),
            "calculated_usage": per_usage,
            "facility_reference": system_code,
            "message": f"{selected['name']} estimates parking occupancy at {occupancy_level}.",
        })
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400
    except Exception as exc:
        app.logger.exception("Prediction failed")
        return jsonify({"error": "Prediction failed", "details": str(exc)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
