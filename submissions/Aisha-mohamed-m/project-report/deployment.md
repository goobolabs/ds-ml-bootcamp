# 🌾 Smart Crop Recommendation System

**Name:** Aisha Mahamad

---

# 📖 Short Description

Smart Crop Recommendation System is an end-to-end Machine Learning application designed to help farmers select the most suitable crop based on soil nutrients and environmental conditions.

The system analyzes agricultural parameters such as:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

It then predicts the most suitable crop for cultivation using Machine Learning algorithms.

The project supports three Machine Learning models:

🌲 Random Forest

⚡ XGBoost

📈 Logistic Regression

Users can choose between:

✅ Automatic Prediction Mode (Recommended)

or

✅ Manual Model Selection (Advanced Mode)

The trained Machine Learning models are deployed through a Flask REST API, while the user interface is built using Streamlit to provide farmers with a simple, responsive, and interactive experience.

---

# 🌱 Problem Being Solved

Many farmers still rely on traditional experience or guesswork when selecting crops.

Incorrect crop selection can result in:

- Low crop productivity
- Poor soil utilization
- Financial losses
- Water wastage
- Fertilizer wastage
- Reduced agricultural efficiency

Smart Crop Recommendation System provides an AI-powered decision support tool that helps farmers choose the most suitable crop based on scientific analysis of soil nutrients and environmental conditions.

---

# 🤖 Machine Learning Models

## Models Used

- 🌲 Random Forest
- ⚡ XGBoost
- 📈 Logistic Regression

---

## Why These Models Were Selected

### Random Forest

- High prediction accuracy
- Handles non-linear relationships
- Robust against overfitting
- Suitable for agricultural datasets

### XGBoost

- Fast prediction
- Excellent classification performance
- Efficient boosting algorithm
- Handles complex feature interactions

### Logistic Regression

- Simple baseline classifier
- Fast inference
- Easy comparison with other models
- Lightweight and interpretable

---

# 🔄 Machine Learning Pipeline

Crop Recommendation Dataset

↓

Data Cleaning

↓

Feature Selection

↓

Data Preprocessing

↓

Feature Scaling (where applicable)

↓

Model Training

↓

Model Evaluation

↓

Save Trained Models

↓

Flask REST API

↓

Streamlit User Interface

↓

Crop Recommendation Result

---

# 🌟 Main Features

- AI-powered Crop Recommendation
- Automatic Prediction Mode
- Manual Model Selection
- Random Forest Prediction
- XGBoost Prediction
- Logistic Regression Prediction
- Explainable AI (Why This Crop?)
- Crop Guide
- Recommendation History
- Download Recommendation Report (PDF)
- Responsive User Interface
- Real-time Prediction
- Interactive Charts

---

# 💻 Technologies Used

## Machine Learning & Backend

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Joblib
- Flask
- Flask-CORS

---

## Frontend

- Streamlit
- Plotly
- HTML
- CSS

---

## Development Tools

- Git
- GitHub
- VS Code

---

# 🏗️ System Architecture

Farmer

↓

Streamlit Frontend

↓

Flask REST API

↓

Machine Learning Models

(Random Forest / XGBoost / Logistic Regression)

↓

Crop Recommendation

↓

Recommendation Displayed to User

↓

Download Recommendation Report

---

# 📂 Project Structure

```text
crop-recommendation/

│── app.py
│── streamlit_app.py
│── processing.py
│── utils.py
│── requirements.txt
│── README.md
│── REPORT.md
│── DEPLOYMENT.md

├── dataset/
│   └── Crop_Recommendation.csv

├── models/
│   ├── crop_random_forest.pkl
│   ├── crop_xgboost.pkl
│   └── crop_logistic_regression.pkl

├── static/

└── screenshots/
```

---

# 📊 Dataset

Dataset Name

Crop Recommendation Dataset

Dataset Source

Kaggle

Dataset Link

https://www.kaggle.com/datasets/madhuraatmarambhagat/crop-recommendation-dataset

The dataset contains:

- Nitrogen
- Phosphorus
- Potassium
- Temperature
- Humidity
- Soil pH
- Rainfall
- Crop Label

---

# 🌐 Live Application

Frontend

Coming Soon

Backend API

Coming Soon

---

# 🔗 GitHub Repository

https://github.com/Aisha-mohamed-m/crop-recommendation

---

# 🚀 Future Improvements

- Weather API Integration
- User Authentication
- Multi-language Support
- Cloud Deployment
- Mobile Application
- Explainable AI Dashboard
- Prediction Analytics
- Farmer Profile Management
- Recommendation History Database
- Advanced AI Models

---

# 🙏 Acknowledgement

I would like to express my sincere gratitude to my supervisors, instructors, classmates, and everyone who supported me throughout the development of this Machine Learning project.

Special thanks to the open-source community, the creators of the Crop Recommendation Dataset on Kaggle, and the developers of Flask, Streamlit, Scikit-learn, and XGBoost for providing the tools and resources that made this project possible.

---

# 👩‍💻 Author

**Aisha Mahamad**

GitHub:

https://github.com/Aisha-mohamed-m/crop-recommendation/tree/main



If you find this project useful, please consider giving the repository a star.