

```markdown
# Flood Prediction Using Machine Learning

> Abdrihman Hussein  


---

# 1. Problem Statement and Motivation

Flooding is one of the most common natural disasters, causing damage to infrastructure, agriculture, and communities. Predicting flood risk early can help reduce possible losses and improve preparation.

The objective of this project is to develop a machine learning regression model that predicts `FloodProbability` based on environmental and human-related factors.

This project covers the complete ML workflow, including data preprocessing, model training, evaluation, and API deployment.

---

# 2. Dataset and Preprocessing

## Dataset Source

The project uses the **Kaggle Flood Prediction Dataset**.

- Dataset size: 50,000+ records
- Problem type: Regression
- Target variable: `FloodProbability`

The dataset contains different environmental and infrastructure factors that influence flood risk.

Main features used:

- MonsoonIntensity
- DrainageSystems
- Urbanization
- ClimateChange
- Deforestation
- RiverManagement
- TopographyDrainage
- Siltation

## Preprocessing Steps

The following steps were applied before model training:

- **Missing values:** Filled using median values to maintain data consistency.
- **Duplicates:** Removed duplicate records to avoid repeated samples.
- **Outliers:** Managed using IQR capping to reduce the effect of extreme values.
- **Feature selection:** Mutual Information was used to select the most important features.
- **Scaling:** RobustScaler was applied to normalize feature values.

---

# 3. Algorithms

Three regression algorithms were trained and compared.

## Linear Regression

Linear Regression predicts flood probability by learning a linear relationship between input features and the target value.

**Why selected:**
- Simple and interpretable
- Fast training
- Good baseline regression model

---

## Random Forest Regressor

Random Forest combines multiple decision trees to produce a stronger prediction.

**Why selected:**
- Handles complex relationships
- Reduces overfitting
- Works well with structured data

---

## Gradient Boosting Regressor

Gradient Boosting builds multiple trees sequentially, where each new tree improves previous prediction errors.

**Why selected:**
- Captures complex patterns
- Often performs well on tabular datasets

---

# 4. Results and Discussion

The models were evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

## Model Comparison

| Model | R² Score | MAE | RMSE |
|---|---|---|---|
| Linear Regression | **0.9943** | **0.0022** | **0.0038** |
| Gradient Boosting | 0.8368 | 0.0159 | 0.0202 |
| Random Forest | 0.6481 | 0.0235 | 0.0296 |

## Best Model

Linear Regression achieved the highest performance with an R² score of **0.9943**.

This means the model explains approximately 99.43% of the variation in flood probability.

The reason it performed best is that the selected features have a strong linear relationship with the target variable.

## Sanity Checks

The final model was tested with different scenarios:

| Scenario | Prediction | Risk Level |
|---|---|---|
| High Risk | 0.82 | High |
| Low Risk | 0.18 | Low |
| Medium Risk | 0.49 | Moderate |

The predictions matched the expected risk categories.

---

# 5. Deployment Notes

The selected Linear Regression model was deployed as a Flask REST API.

The API uses:

- Saved trained model (`best_model.pkl`)
- Saved preprocessing pipeline (`scaler.pkl`)

The API receives feature values as JSON and returns the predicted flood probability.

## Endpoint

```

POST /predict

````

## Example Request

```json
{
"MonsoonIntensity":6,
"DrainageSystems":7,
"Urbanization":5,
"ClimateChange":6,
"Deforestation":4,
"RiverManagement":6,
"TopographyDrainage":7,
"Siltation":5
}
````

## Example Response

```json
{
"FloodProbability":0.54,
"RiskLevel":"Moderate"
}
```

---

# 6. Lessons Learned

This project improved understanding of the complete machine learning lifecycle.

Key lessons:

* Data preprocessing has a major impact on model performance.
* Feature selection helps remove unnecessary information and improves efficiency.
* Different algorithms perform differently depending on the dataset structure.
* Simple models can sometimes outperform complex models.
* Deployment requires saving both the model and preprocessing steps.

## Repository link
(https://github.com/Abdrihman-Hussein/Flood-prediction-/)
```
