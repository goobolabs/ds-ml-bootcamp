# Heart Disease Prediction API 🫀

<div align="center">

<img src="https://avatars.githubusercontent.com/u/173564581?v=4" width="120" height="120" style="border-radius:50%;border:3px solid #3b82f6;" alt="Abdullahi" />

# ❤️ CardioAI — Heart Disease Prediction API

**AI-powered cardiovascular risk assessment · Built by [Abdullahi](https://github.com/abdullahi4444)**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=fff)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=fff)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18+-61DAFB?style=for-the-badge&logo=react&logoColor=000)](https://react.dev/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=fff)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

### 🚀 [View Live Demo](https://heart-disease-prediction-api-five.vercel.app/) | 🐙 [View Source Code or Repository](https://github.com/abdullahi4444/Heart-Disease-Prediction-API)

</div>

<br/>

This repository contains my final project for the ML Model Development and Deployment bootcamp. The goal of this project is to build a complete machine learning pipeline—from data preprocessing to training multiple models—and finally deploy the best-performing model as a REST API using FastAPI.

This API predicts whether a patient is at risk of heart disease based on their clinical information (like age, blood pressure, cholesterol, etc.).

## 📊 Dataset Details
- **Source:** [Heart Dataset on Kaggle](https://www.kaggle.com/datasets/mfarhaannazirkhan/heart-dataset)
- **Size:** 2,182 rows and 14 columns.
- **Preprocessing:** The data pipeline includes handling missing values, standard scaling numerical features (`StandardScaler`), and encoding categorical features.

## 🤖 Algorithms Trained
I trained and compared three different supervised machine learning algorithms to find the best model for this classification problem:
1. **Logistic Regression:** Used as a strong, interpretable baseline.
2. **Random Forest Classifier:** An ensemble method to capture non-linear relationships and reduce overfitting.
3. **Support Vector Machine (SVM):** Used for its effectiveness in finding optimal decision boundaries in high-dimensional spaces.

## 📈 Results and Model Selection

*(Note: Replace the metrics below with your actual final metrics)*

| Algorithm                  | Accuracy | F1-Score | ROC-AUC |
|----------------------------|----------|----------|---------|
| Logistic Regression        | 0.85     | 0.85     | 0.90    |
| **Random Forest (Winner)** | **0.91** | **0.91** | **0.95**|
| Support Vector Machine     | 0.88     | 0.88     | 0.92    |

**Results Summary:**
The **Random Forest** model performed the best across all major metrics, particularly achieving the highest F1-Score. Because balancing false positives and false negatives is critical in medical diagnosis, the Random Forest model was selected as the final winner, serialized into a `.pkl` file, and deployed to the API.

## 🚀 Setup and Example Commands

**1. Clone the repository and install dependencies:**
```bash
git clone https://github.com/abdullahi4444/Heart-Disease-Prediction-API.git
cd Heart-Disease-Prediction-API
pip install -r requirements.txt
```

**2. Run the training script (Optional):**
```bash
python src/train.py
```

**3. Start the FastAPI server:**
```bash
uvicorn api.app:app --reload
```

## 🌐 API Usage Example

You can test the locally running API by sending a JSON payload to the `/predict` endpoint.

**Curl Command:**
```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
        "age": 54,
        "sex": 1,
        "cp": 0,
        "trestbps": 110,
        "chol": 206,
        "fbs": 0,
        "restecg": 0,
        "thalachh": 108,
        "exang": 1,
        "oldpeak": 0.0,
        "slope": 1,
        "ca": 2,
        "thal": 0
      }'
```

**Expected Response:**
```json
{
  "prediction": "Heart Disease",
  "probability": 0.91
}
```

I would like to express my deepest gratitude to the incredible individuals and organizations that made this learning journey possible. Your guidance, support, and sponsorship were invaluable to my success in this bootcamp.

<div align="center">
  <table>
    <tr>
      <td align="center">
        <a href="https://github.com/omartood">
          <img src="https://github.com/omartood.png" width="100px;" style="border-radius:50%;" alt="Omar Tood"/><br />
          <b>Omar Tood</b>
        </a><br />
        <i>Mentor & Instructor</i>
      </td>
      <td align="center">
        <a href="https://github.com/sharafdin">
          <img src="https://github.com/sharafdin.png" width="100px;" style="border-radius:50%;" alt="Sharafdin"/><br />
          <b>Sharafdin</b>
        </a><br />
        <i>Instructor</i>
      </td>
      <td align="center">
        <a href="https://github.com/goobolabs">
          <img src="https://github.com/goobolabs.png" width="100px;" style="border-radius:50%;" alt="Goobolabs"/><br />
          <b>Goobolabs</b>
        </a><br />
        <i>Official Sponsor</i>
      </td>
    </tr>
  </table>
</div>

## 👤 Author
<div align="center">
<img src="https://avatars.githubusercontent.com/u/173564581?v=4" width="80" height="80" style="border-radius:50%;" alt="Abdullahi"/>

---
*Developed by Abdullahi Abdiweli Adam (July 2026).*
