from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import os


app = Flask(__name__)
CORS(app)


# Load model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(
    BASE_DIR,
    "models",
    "random_forest.pkl"
)

model = joblib.load(model_path)


# Same encoding used during training
encoders = {
    "Resources": {
        "High": 0,
        "Medium": 1,
        "Low": 2
    },

    "Extracurricular": {
        "Yes": 1,
        "No": 0
    },

    "Motivation": {
        "High": 0,
        "Medium": 1,
        "Low": 2
    },

    "Internet": {
        "Yes": 1,
        "No": 0
    },

    "Gender": {
        "Male": 1,
        "Female": 0
    },

    "LearningStyle": {
        "Visual": 0,
        "Auditory": 1,
        "Reading": 2
    },

    "OnlineCourses": {
        "Yes": 1,
        "No": 0
    },

    "Discussions": {
        "Yes": 1,
        "No": 0
    },

    "EduTech": {
        "Yes": 1,
        "No": 0
    },

    "StressLevel": {
        "High": 0,
        "Medium": 1,
        "Low": 2
    }
}


@app.route("/")
def home():
    return jsonify({
        "message": "Student Performance Prediction API is running"
    })


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    input_data = pd.DataFrame([data])


    # Encode categorical columns
    for column, mapping in encoders.items():
        if column in input_data.columns:
            input_data[column] = input_data[column].map(mapping)


    prediction = model.predict(input_data)


    result = "Pass" if prediction[0] == 1 else "Fail"


    return jsonify({
        "prediction": result
    })


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )