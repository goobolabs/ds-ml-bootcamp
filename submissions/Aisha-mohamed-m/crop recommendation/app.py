# app.py — Crop Classifier API
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

# 1) Halkan ka soo jiid shaqada habaynta xogta ee utils.py
from utils import prepare_features_from_raw

app = Flask(__name__)
CORS(app)



# ---------------------------------------------------------
# 2) Soo rar Moodellada iyo  Magacyada Dalagyada
# ---------------------------------------------------------
MODELS = {
    "lr": joblib.load("models/lr_crop_model.joblib"),
    "rf": joblib.load("models/rf_crop_model.joblib"),
    "xgb": joblib.load("models/xgb_crop_model.joblib"),
}

mapping_data = json.load(open("models/crop_mapping.json", "r"))
idx_to_crop = mapping_data["idx_to_crop"]


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Crop Recommendation API",
        "endpoints": {
            "POST /predict?model=lr|rf|xgb": {
                "expects_json": {
                    "N": "number",
                    "P": "number",
                    "K": "number",
                    "temperature": "number",
                    "humidity": "number",
                    "ph": "number",
                    "rainfall": "number",
                }
            }
        }
    })


@app.route("/predict", methods=["POST"])
def predict():
    choice = (request.args.get("model") or "rf").lower().strip()
    if choice not in MODELS:
        return jsonify({"error": "Unknown model. Use model=lr, model=rf, or model=xgb"}), 400
    model = MODELS[choice]

    data = request.get_json(silent=True) or {}
    required = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
    
    missing = [k for k in required if k not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {missing}"}), 400

    try:
        # ---------------------------------------------------------
        # 3) KAN WAA HALKII AAD WEYDIISAY (Gudaha predict()...)
        # ---------------------------------------------------------
        x_new = prepare_features_from_raw(data)   # Habaynta xogta iyadoo la wacay utils
        pred_idx = int(model.predict(x_new)[0])   # Saadaalinta index-ka dalagga
        
        # U beddel index-ka magaca rasmiga ah ee dalagga (tusaale: "Rice")
        crop_label = idx_to_crop[str(pred_idx)].capitalize()
        
        model_names = {
            "lr": "logistic_regression",
            "rf": "random_forest",
            "xgb": "xgboost"
        }

        payload = {
            "model": model_names[choice],
            "input": {k: float(data[k]) for k in required},
            "prediction": pred_idx,
            "label": crop_label,
        }
        
        # Xisaabinta boqolleyda kalsoonida haddii uu moodelku leeyahay
        if hasattr(model, "predict_proba"):
            probs = model.predict_proba(x_new)[0]
            payload["confidence"] = round(float(probs[pred_idx]), 3)
            
        return jsonify(payload)
        
    except Exception as e:
        return jsonify({"error": f"Failed to prepare/predict: {e}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)