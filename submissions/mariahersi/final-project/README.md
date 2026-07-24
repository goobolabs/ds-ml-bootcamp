# ParkSense - Parking Occupancy Prediction
---
replinke:https:https://github.com/mariahersi/parking_prediction_final_project

A full-stack machine learning web application that estimates the expected occupancy range of a parking facility. Users select one of five trained models, enter parking and time details, and receive a real prediction from the saved model pipeline.

**Student:** Maryamo Hersi Hassan  
**Project type:** Supervised machine learning / parking occupancy prediction

## Features

- React and Vite frontend with responsive Light and Dark modes
- Flask REST API
- Five selectable trained models
- Saved preprocessing + model pipelines for consistent predictions
- Seven simple parking inputs; the backend completes technical model fields automatically
- Input validation and helpful error messages
- Parking occupancy results shown as ranges: `0 - 25`, `25 - 50`, `50 - 75`, and `75-100`

## Models

The application lets users choose between these trained regression models:

| Model ID | Model name |
| --- | --- |
| `linear_regression` | Linear Regression |
| `decision_tree` | Decision Tree |
| `random_forest` | Random Forest |
| `gradient_boosting` | Gradient Boosting |
| `svr` | Support Vector Regression |

Each `.joblib` file in `backend/model/` contains both the data preprocessing steps and the fitted model. Flask therefore receives raw form values safely and uses the exact preprocessing used during training.

## Project structure

```text
parking-prediction-fullstack/
├── ParkingDataset.xlsx          # Training dataset
├── Parking.ipynb                # Analysis and notebook export command
├── backend/
│   ├── app.py                   # Flask API
│   ├── train_models.py          # Reproducible five-model training script
│   ├── requirements.txt
│   └── model/                   # Saved model pipelines and metadata
└── frontend/
    ├── src/
    │   ├── App.jsx
    │   ├── index.css
    │   └── components/PredictionForm.jsx
    └── package.json
```

## Run the application

### 1. Start the backend

Open a terminal in the project folder:

```bash
cd backend
python -m venv venv
```

On Windows, activate the virtual environment and install packages:

```bash
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

The API runs at `http://localhost:5000`.

### 2. Start the frontend

Open a second terminal:

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173` in your browser.

> Both the backend and frontend must be running for predictions to work.

## Train or refresh the five models

The final section of `Parking.ipynb` includes the export command. You can also run it directly from the project root:

```bash
python backend/train_models.py
```

This trains all five models using `ParkingDataset.xlsx`, evaluates them, and saves the production pipelines and `metadata.json` in `backend/model/`.

## API

### Health check

```http
GET /api/health
```

### List available models

```http
GET /api/models
```

### Make a prediction

```http
POST /api/predict
Content-Type: application/json
```

Example request body:

```json
{
  "model_id": "random_forest",
  "Capacity": 577,
  "Occupancy": 150,
  "month": "Oct",
  "day": "Tue",
  "WorkingDay": "Yes",
  "hour": 9,
  "period": "AM"
}
```

Example response:

```json
{
  "prediction": "25 - 50",
  "occupancy_level": "25 - 50",
  "model": {
    "id": "random_forest",
    "name": "Random Forest"
  }
}
```

## Important note

Predictions are based on historical parking records and are estimates, not live space-by-space availability. The current `Occupancy` and `per_usage` inputs are strongly related to the target occupancy range, so the model scores should be interpreted with care. A future-demand version can be trained without these current-state fields.
