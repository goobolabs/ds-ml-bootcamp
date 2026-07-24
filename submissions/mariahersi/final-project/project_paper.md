
# ParkSense: Parking Occupancy Prediction Web Application
---
replinke:https:https://github.com/mariahersi/parking_prediction_final_project

**Student:** Maryamo Hersi Hassan  
**Project type:** Supervised Machine Learning - Ordinal Prediction / Regression  
**Date:** July 2026

## Project Summary

ParkSense is a complete machine learning solution for estimating parking occupancy levels from historical parking data. The application predicts one of four occupancy ranges: `0 - 25`, `25 - 50`, `50 - 75`, and `75 - 100`. It provides a simple React interface where users enter parking capacity, current occupancy, and time-related details, then receive a prediction from a selected trained model.

The system combines five machine learning models with a Flask REST API and a React + Vite frontend. Each saved model includes its preprocessing pipeline, so the API can safely transform raw inputs in the same way as the training process before making a prediction.

## Core Project Requirements

| Requirement | Implementation |
| --- | --- |
| **Machine learning problem** | Supervised ordinal prediction of a parking occupancy range. |
| **Dataset** | Historical parking records in `ParkingDataset.xlsx`. |
| **Model comparison** | Linear Regression, Decision Tree, Random Forest, Gradient Boosting, and Support Vector Regression. |
| **Deployment** | Flask API with working health, model-listing, and prediction endpoints. |
| **Frontend** | Responsive React and Vite application with light and dark modes. |
| **Documentation** | README, analysis notebook, project proposal, and this project paper. |

## 1. Business Problem

Finding parking in busy areas can be difficult. Drivers may spend a long time searching for an available space, which contributes to delays, congestion, and fuel use. Parking operators also need a clearer understanding of when facilities are likely to be lightly used or busy.

Parking occupancy changes according to characteristics such as facility capacity, current use, day of the week, whether it is a working day, and the time of day. ParkSense addresses this problem by learning these historical patterns and returning an easy-to-understand occupancy estimate. The result can support more informed parking decisions and help operators recognize demand patterns.

## 2. Dataset and Target Variable

The project uses `ParkingDataset.xlsx`, which contains historical parking observations. After duplicate removal and filtering rows with a valid target, the training script uses 33,949 records.

The prediction target is `per_occupancy`, an occupancy-range label. The categories are converted to numerical codes during training and converted back to a readable label when the API returns a result.

| Numerical code | Occupancy range |
| ---: | --- |
| 0 | `0 - 25` |
| 1 | `25 - 50` |
| 2 | `50 - 75` |
| 3 | `75 - 100` |

The model pipeline uses the following features:

- `SystemCodeNumber`: parking facility identifier
- `Capacity`: total parking spaces
- `Occupancy`: occupied spaces
- `per_usage`: percentage use of the facility
- `year`, `month`, `day`, and `WorkingDay`
- `hour` and `period`

Numeric features are imputed with their median and standardized. Categorical features are imputed with their most frequent value and one-hot encoded. These steps are saved inside each trained pipeline.

## 3. Methodology

The dataset is split into training and testing sets with an 80/20 split. Stratification is used to preserve the distribution of the occupancy categories in both sets. The random state is fixed at 42 so that the experiment is reproducible.

Five regression algorithms are trained and compared:

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor
4. Gradient Boosting Regressor
5. Support Vector Regression (SVR)

Regression outputs are rounded and clipped to the valid class codes from 0 to 3. This makes it possible to evaluate both continuous prediction quality and correct occupancy-category prediction. The models are evaluated using mean absolute error (MAE), root mean squared error (RMSE), R-squared, and category accuracy.

For practical training time, SVR is trained using a seeded, stratified sample of 6,000 training rows. The other models use the full training split.

## 4. Model Results

The following metrics are exported in `backend/model/metadata.json` after training:

| Model | MAE | RMSE | R-squared | Category accuracy |
| --- | ---: | ---: | ---: | ---: |
| Linear Regression | 0.2359 | 0.2772 | 0.9326 | 96.77% |
| Decision Tree | 0.0000 | 0.0000 | 1.0000 | 100.00% |
| Random Forest | 0.0000 | 0.0004 | 1.0000 | 100.00% |
| Gradient Boosting | 0.0000 | 0.0001 | 1.0000 | 100.00% |
| Support Vector Regression | 0.1963 | 0.2833 | 0.9296 | 89.01% |

The tree-based models achieved the strongest results on this test split. Random Forest is selected as the default model in the user interface, but the interface allows a user to compare predictions from all five saved models.

## 5. System Design and Deployment

The application has two parts:

```text
React + Vite frontend
        |
        | JSON request to /api/predict
        v
Flask API
        |
        | loads selected joblib pipeline
        v
Prediction response with occupancy range
```

The React frontend collects seven user-friendly fields: capacity, current occupancy, month, day, working-day status, hour, and AM/PM period. The Flask API validates these values, calculates `per_usage`, selects the nearest available facility reference using capacity, and supplies the default year from the model metadata. It then calls the selected saved pipeline and returns the predicted range as JSON.

The API exposes the following endpoints:

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `GET` | `/api/health` | Check that the service is running and count loaded models. |
| `GET` | `/api/models` | Return the available models and their metrics. |
| `POST` | `/api/predict` | Validate input and return an occupancy prediction. |

An example request is:

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

The response includes the selected model, the predicted occupancy range, calculated usage, and a readable message for the user.

## 6. How to Run the Project

Start the backend:

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Start the frontend in a second terminal:

```bash
cd frontend
npm install
npm run dev
```

The backend runs at `http://localhost:5000`; Vite normally serves the frontend at `http://localhost:5173`.

To retrain the models from the project root, run:

```bash
python backend/train_models.py
```

## 7. Limitations and Future Work

ParkSense provides an estimate based on historical patterns; it is not a live parking-space availability system. The current `Occupancy` and calculated `per_usage` fields are closely related to the occupancy-range target. This relationship helps explain the high scores achieved by some models, so the results should be interpreted with care.

Future work could create a true future-demand model that excludes current-state inputs, uses only information available before arrival, and predicts occupancy for a future date and time. Other improvements could include real-time sensor or booking data, additional weather and event features, model monitoring, and cloud deployment.

## Conclusion

ParkSense demonstrates a complete machine learning workflow: data preparation, model training and comparison, pipeline export, API development, and frontend integration. It transforms historical parking data into a simple occupancy estimate that can help users and parking managers understand expected demand.
