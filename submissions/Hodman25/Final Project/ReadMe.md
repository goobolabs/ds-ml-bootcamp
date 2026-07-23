# 💧 Water Potability Prediction System

A machine learning project that predicts whether water is safe for drinking based on water quality measurements. The project includes data preprocessing, model training and comparison, a FastAPI backend, and a React frontend.


##  Project Overview

Access to clean and safe drinking water is critical for public health. This project uses machine learning to predict water potability using various water quality indicators.

The system allows users to enter water quality measurements and receive an instant prediction indicating whether the water is potable or not.



## Objectives

- Clean and preprocess water quality data.
- Train and compare multiple machine learning models.
- Select the best-performing model.
- Deploy the model using FastAPI.
- Build a React frontend for user interaction.



##  Dataset

### Water Potability Dataset

The dataset contains water quality measurements and a target variable indicating whether the water is safe for drinking.

### Features

- pH
- Hardness
- Solids
- Chloramines
- Sulfate
- Conductivity
- Organic Carbon
- Trihalomethanes
- Turbidity

### Target

| Value | Meaning |
|---------|---------|
| 0 | Not Potable |
| 1 | Potable |

---

## Data Preprocessing

The following preprocessing steps were performed:

### Missing Value Handling

Missing values were found in:

| Feature | Missing Values |
|----------|----------|
| pH | 491 |
| Sulfate | 781 |
| Trihalomethanes | 162 |

Missing values were replaced using mean imputation.

### Feature Scaling

Numerical features were scaled using:

```python
StandardScaler()
```

### Saved Artifacts

- `best_model.joblib`
- `scaler.pkl`
- `columns.json`

---

##  Machine Learning Models

The following classification algorithms were trained and evaluated:

1. Logistic Regression
2. Support Vector Machine (SVM)
3. Random Forest
4. XGBoost

---

## Model Performance

| Model | Accuracy |
|---------|---------|
| Logistic Regression | 0.50 |
| SVM | 0.686 |
| Random Forest | **0.690** |
| XGBoost | 0.646 |

### Best Model

✅ Random Forest

Random Forest achieved the highest accuracy and overall performance and was selected for deployment.

---

## 🔍 Evaluation Metrics

### Random Forest Classification Report

| Metric | Class 0 | Class 1 |
|----------|----------|----------|
| Precision | 0.70 | 0.67 |
| Recall | 0.90 | 0.34 |
| F1-Score | 0.79 | 0.45 |

**Overall Accuracy:** 69%



## ✅ Sanity Checks

Three unseen test samples were evaluated using the Random Forest model.

| Sample | Actual | Predicted |
|---------|---------|---------|
| #9 | Not Potable | Not Potable |
| #25 | Not Potable | Not Potable |
| #50 | Potable | Not Potable |

The model correctly classified two of the three selected samples.

---

#  API Deployment

The trained model was deployed using FastAPI.

## Run Backend

```bash
cd api
uvicorn app:app --reload
```

### API Endpoint

```http
POST /predict
```

### Example Request

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

### Example Response

```json
{
  "prediction": "Potable",
"probability": "67%"

}
```

---

# 💻 Frontend

The frontend was built using:

- React
- Axios
- Tailwind CSS
- Lucide React

### Run Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 📂 Project Structure

# Project Structure

```text
WATER-QUALITY-PREDICTION/
│
├── api/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── app.py
│   ├── schemas.py
│   └── utilits.py
│
├── data/
│   ├── processed-data.csv
│   └── water_potability.csv
│
├── frontend/
│
├── models/
│   ├── best_model.joblib
│   ├── columns.json
│   └── scaler.pkl
│
├── notebooks/
│   ├── .ipynb_checkpoints/
│   ├── EDA_and_Preprocessing.ipynb
│   └── Model_Training.ipynb
│
├── .gitignore
├── project_paper.md
├── project-proposal.md
├── README.md
└── requirements.txt
```




## 🛠 Technologies Used

### Machine Learning

- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost

### Backend

- FastAPI
- Uvicorn

### Frontend

- React
- Axios
- Tailwind CSS

### Version Control

- Git
- GitHub


## 📚 Lessons Learned

Through this project I learned:

- Data preprocessing and feature scaling
- Model evaluation and comparison
- Machine learning deployment with FastAPI
- Integrating a React frontend with an ML API
- Building an end-to-end machine learning application



## Author

**Hodan Maxamed Ibraahim**

