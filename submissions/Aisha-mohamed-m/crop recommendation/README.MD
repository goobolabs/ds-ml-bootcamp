# 🌾 Smart Crop Recommendation System

An AI-powered Smart Crop Recommendation System that helps farmers select the most suitable crop based on soil nutrients and environmental conditions using Machine Learning.

---

## 📖 Project Overview

The Smart Crop Recommendation System is a decision support application designed to assist farmers in choosing the best crop for cultivation.

The system analyzes:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

Using Machine Learning algorithms, the system predicts the most suitable crop with high accuracy.

---

## 🎯 Objectives

- Help farmers make informed planting decisions.
- Improve agricultural productivity.
- Reduce crop selection errors.
- Utilize Artificial Intelligence in agriculture.
- Provide quick and accurate crop recommendations.

---

## 🚀 Features

- 🌱 Crop Recommendation
- 🤖 AI-powered Prediction
- 📊 Interactive Dashboard
- 📖 Crop Guide
- 📜 Recommendation History
- 📄 Download Recommendation Report (PDF)
- 🌙 Dark & Light Theme
- 📱 Responsive User Interface
- ⚡ Fast Prediction
- 🎨 Modern UI/UX

---

## 🧠 Machine Learning Models

The system supports three prediction models:

- Random Forest
- XGBoost
- Logistic Regression

### Prediction Modes

**Automatic Mode**

The system automatically selects the most suitable prediction model.

**Advanced Mode**

Users can manually choose:

- Random Forest
- XGBoost
- Logistic Regression

for comparison purposes.

---

## 🏗️ System Architecture

Frontend

- Streamlit

Backend

- Flask API

Machine Learning

- Random Forest
- XGBoost
- Logistic Regression

Dataset

- Crop Recommendation Dataset

---

## 📂 Project Structure

```text
final_project/

│── app.py
│── streamlit_app.py
│── model.py
│── processing.py
│── utils.py
│── requirements.txt
│── README.md

├── models/
│     ├── crop_random_forest.pkl
│     ├── crop_xgboost.pkl
│     └── crop_logistic_regression.pkl

├── dataset/
│     └── clean_crop_dataset.csv

├── static/

├── templates/
```

---

## ⚙️ Installation

### Clone the project

```bash
git clone https://github.com/yourusername/smart-crop-recommendation.git
```

### Navigate to the project

```bash
cd smart-crop-recommendation
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Flask API

```bash
python app.py
```

---

## ▶️ Run Streamlit

```bash
streamlit run streamlit_app.py
```

---

## 🌐 API Endpoint

POST

```
/predict
```

Example

```json
{
  "N":90,
  "P":42,
  "K":43,
  "temperature":23.6,
  "humidity":80.3,
  "ph":6.7,
  "rainfall":210.5
}
```

---

## 🌽 Prediction Result

The system returns:

- Recommended Crop
- Confidence Score
- Prediction Mode
- AI Model Used
- Recommendation Explanation

---

## 📄 Recommendation Report

After prediction, users can download a professional PDF report containing:

- Input Data
- Recommended Crop
- Confidence Score
- Explainable AI
- Crop Information
- Growing Tips
- Water Requirement
- Harvest Time
- Fertilizer Recommendation

---

## 📊 Technologies Used

### Frontend

- Streamlit

### Backend

- Flask

### Machine Learning

- Scikit-learn
- XGBoost
- Joblib

### Data Processing

- Pandas
- NumPy

### Visualization

- Plotly

---

## 🌱 Input Features

| Feature | Description |
|----------|-------------|
| Nitrogen | Nitrogen level in soil |
| Phosphorus | Phosphorus level |
| Potassium | Potassium level |
| Temperature | Temperature in Celsius |
| Humidity | Relative humidity |
| pH | Soil pH |
| Rainfall | Rainfall in mm |

---

## 🌾 Supported Crops

Examples include:

- Rice
- Maize
- Chickpea
- Kidney Beans
- Pigeon Peas
- Moth Beans
- Mung Bean
- Black Gram
- Lentil
- Pomegranate
- Banana
- Mango
- Grapes
- Watermelon
- Muskmelon
- Apple
- Orange
- Papaya
- Coconut
- Cotton
- Jute
- Coffee

---

## 👩‍💻 Developed By

**Aisha Mahamad**

Final Year Project

Department of Computer Science

---

## 📜 License

This project is developed for educational and research purposes.

---

## ⭐ Future Improvements

- Weather API Integration
- Multi-language Support (English & Somali)
- Mobile Application
- Explainable AI Dashboard
- Cloud Deployment
- User Authentication
- Database Integration
- Advanced Analytics