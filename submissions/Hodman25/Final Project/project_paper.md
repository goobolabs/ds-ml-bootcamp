# Water Potability Prediction Using Machine Learning

## Problem Statement and Motivation

Access to safe drinking water is essential for human health and well-being. Traditional water quality testing methods can be expensive and time-consuming. This project aims to develop a machine learning model that predicts whether water is safe for drinking based on various water quality measurements.

The goal is to provide a fast and automated way to assess water potability using data-driven techniques.


## Dataset and Preprocessing

**Dataset Source**(https://www.kaggle.com/datasets/uom190346a/water-quality-and-potability)
### Dataset Size

- Total Records: 3,276
- Features: 9 numerical features
- Target Variable:
  - 0 = Not Potable
  - 1 = Potable

### Features

The dataset contains the following water quality indicators:

- pH
- Hardness
- Solids
- Chloramines
- Sulfate
- Conductivity
- Organic Carbon
- Trihalomethanes
- Turbidity

### Data Cleaning

The dataset contained missing values in several columns:

| Feature | Missing Values |
|----------|----------|
| pH | 491 |
| Sulfate | 781 |
| Trihalomethanes | 162 |

To handle missing values, mean imputation was applied:

- Missing values in **pH** were replaced with the mean pH value.
- Missing values in **Sulfate** were replaced with the mean Sulfate value.
- Missing values in **Trihalomethanes** were replaced with the mean Trihalomethanes value.

After imputation, all missing values were successfully removed.

### Duplicate Check

The dataset was checked for duplicate records before model training.

### Feature Scaling

To ensure numerical features were on a comparable scale, StandardScaler was applied to all input features:
Feature scaling improves the performance of algorithms such as Logistic Regression and Support Vector Machine (SVM).

### Saved Artifacts

To support deployment, preprocessing artifacts were saved:

- `scaler.pkl` — saved StandardScaler object
- `columns.json` — training feature columns
- `processed-data.csv` — cleaned dataset

These files are used by the FastAPI application to preprocess incoming prediction requests in the same way as the training data.




## Algorithms

Four machine learning algorithms were trained and evaluated.

### 1. Logistic Regression

Logistic Regression is a linear classification algorithm that predicts the probability of a class.

**Why chosen:**
- Simple and interpretable
- Good baseline model

### 2. Support Vector Machine (SVM)

SVM finds the optimal decision boundary between classes.

**Why chosen:**
- Effective for classification tasks
- Handles non-linear relationships

### 3. Random Forest

Random Forest is an ensemble learning algorithm that combines multiple decision trees.

**Why chosen:**
- Handles complex patterns
- Reduces overfitting
- Strong performance on tabular datasets

### 4. XGBoost

XGBoost is a gradient boosting algorithm that builds trees sequentially to improve performance.

**Why chosen:**
- High predictive power
- Popular in machine learning competitions



## Results and Discussion

### Model Comparison

| Model | Accuracy |
|---------|---------|
| Logistic Regression | 0.50 |
| SVM | 0.686 |
| Random Forest | 0.690 |
| XGBoost | 0.646 |

### Best Model

The Random Forest model achieved the highest accuracy and overall performance among all evaluated models.

### Random Forest Classification Report

| Metric | Class 0 | Class 1 |
|----------|----------|----------|
| Precision | 0.70 | 0.67 |
| Recall | 0.90 | 0.34 |
| F1-Score | 0.79 | 0.45 |

**Overall Accuracy:** 69.0%

### Sanity Checks

Three unseen samples from the test dataset were evaluated using the Random Forest model, which was selected as the best-performing model.

#### Sanity Check 1

**Actual Label:** Not Potable (0)

**Predicted Label:** Not Potable (0)

**Result:** Correct Prediction ✓

---

#### Sanity Check 2


**Actual Label:** Not Potable (0)

**Predicted Label:** Not Potable (0)

**Result:** Correct Prediction ✓


#### Sanity Check 3

**Actual Label:** Potable (1)

**Predicted Label:** Not Potable (0)

**Result:** Incorrect Prediction ✗

### Discussion

The Random Forest model correctly classified two out of the three selected test samples. The third sample was misclassified, indicating that while the model performs reasonably well overall, it still struggles to identify some potable water samples. This observation is consistent with the evaluation results, where the recall score for the potable class was lower than that of the non-potable class.


## Deployment Notes

### Model Saving

The best model was saved using Joblib.

```python
joblib.dump(rf, "best_model.joblib")
```

### FastAPI Backend

The trained model was deployed using FastAPI.

#### Endpoint

```http
POST /predict
```

#### Example Request

```json
{
  "ph": 7.2,
  "Hardness": 210,
  "Solids": 18000,
  "Chloramines": 7.1,
  "Sulfate": 320,
  "Conductivity": 450,
  "Organic_carbon": 12,
  "Trihalomethanes": 65,
  "Turbidity": 4.5
}
```

#### Example Response

```json
{
  "prediction": "Potable",
  "probability": "67%"
}
```

### Frontend

A React frontend was developed to:

- Accept water quality measurements.
- Send requests to the FastAPI API.
- Display prediction results to users.



## Lessons Learned

This project provided practical experience in the complete machine learning workflow.

### Challenges Faced

- Handling missing values.
- Selecting suitable evaluation metrics.
- Comparing multiple machine learning algorithms.
- Deploying a machine learning model with FastAPI.
- Connecting a React frontend to the backend API.

### Key Takeaways

- Data preprocessing significantly impacts model performance.
- Ensemble models such as Random Forest often outperform simpler models.
- Model deployment is essential for real-world machine learning applications.
- Building an end-to-end machine learning solution requires both data science and software engineering skills.



## Conclusion

This project successfully developed and deployed a machine learning system for water potability prediction. After comparing four classification algorithms, Random Forest achieved the best overall performance and was selected for deployment. The final solution includes a trained model, FastAPI backend, and React frontend for user interaction.



## Repository Link
(https://github.com/Hodman25/water-quality-prediction)


