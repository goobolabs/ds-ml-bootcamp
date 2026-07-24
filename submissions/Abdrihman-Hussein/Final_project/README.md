# Flood Probability Prediction API
# 🌊 Flood Probability Prediction API

## 📌 Project Overview

The **Flood Probability Prediction API** is a Machine Learning web application and REST API that predicts whether a region is at risk of flooding based on environmental, geographical, and human-related indicators.

The application is built using **Python**, **Scikit-learn**, and **Flask** to provide a real-time risk assessment dashboard and prediction API.

## 🌐 Repositories & Submission

👉 **[Flood Prediction GitHub Repository](https://github.com/Abdrihman-Hussein/Flood-prediction-)**

👉 **[Bootcamp Final Project Submission Directory](https://github.com/Abdrihman-Hussein/ds-ml-bootcamp/tree/main/submissions/Abdrihman-Hussein/Final_project)**

# 🎯 Objectives

* Predict continuous flood probability using Machine Learning regression models.
* Assist disaster management agencies and urban planners in early risk assessment.
* Provide an easy-to-use web interface and RESTful API for real-time predictions.
* Demonstrate an end-to-end Machine Learning lifecycle from raw data preprocessing to API deployment.

# 🚀 Features

* Interactive Flask web dashboard
* Real-time flood risk prediction API (`POST /predict`)
* Categorized risk levels (**Low**, **Moderate**, **High**)
* Linear Regression Machine Learning model ($R^2 = 0.9943$)
* Data preprocessing using `RobustScaler` and IQR outlier capping
* Dynamic input controls and visual gauge updates

## 📁 Project Structure

```text
Flood-prediction-/
│
├── data/
│   ├── flood.csv              # Raw Kaggle dataset (50,000+ rows)
│   └── processed_flood.csv    # Preprocessed dataset
│
├── models/
│   ├── best_model.pkl         # Winning Linear Regression model
│   ├── scaler.pkl             # Fitted RobustScaler object
│   ├── selected_features.pkl  # Serialized feature list
│   └── top_8_features.json    # Selected feature importances
│
├── templates/
│   └── index.html             # Dashboard UI layout
│
├── static/
│   ├── css/
│   │   └── style.css          # Styling (Dark mode glassmorphism)
│   └── js/
│       └── main.js            # Live updates & Chart.js gauge
│
├── client/                    # Sample client test scripts
├── app.py                     # Flask web app & REST API server
├── processing.py              # Cleaning, IQR capping, scaling & feature selection
├── model.py                   # Model training script
├── predict.py                 # Standalone inference engine
├── utils.py                   # Helper & validation routines
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

# 📊 Dataset Information

Dataset Name:

**[Kaggle Flood Prediction Dataset](https://www.kaggle.com/datasets/naiyakhalid/flood-prediction-dataset)**

Number of Rows:

* 50,000+

Number of Features:

* 20 Input Features (Top 8 selected)
* 1 Target Variable

Target Variable:

* `FloodProbability` (Continuous value from 0.0 to 1.0)

# 🏞️ Input Features (Top Selected)

| Feature | Description |
| --- | --- |
| **MonsoonIntensity** | Intensity and volume of monsoon rainfall |
| **DrainageSystems** | Quality and capacity of drainage infrastructure |
| **Urbanization** | Level of urban development and concrete coverage |
| **ClimateChange** | Climate change severity impact score |
| **Deforestation** | Rate of tree loss affecting soil absorption |
| **RiverManagement** | Effectiveness of river embankments and dams |
| **TopographyDrainage** | Natural slope and elevation drainage capability |
| **Siltation** | Level of sediment clogging rivers and channels |

# 🎯 Target Variable & Risk Levels

| Probability Range | Risk Level | Meaning |
| --- | --- | --- |
| $0.00 - 0.35$ | **Low** | Minimal risk of flooding |
| $0.35 - 0.65$ | **Moderate** | Moderate flood risk; monitoring advised |
| $0.65 - 1.00$ | **High** | Critical flood threat; emergency prep required |

# 🛠️ Technologies Used

* Python
* Pandas & NumPy
* Scikit-learn
* Flask
* Joblib
* HTML5 / CSS3 / JavaScript (Chart.js)

# 🤖 Machine Learning Models

The following regression models were trained and evaluated on an 80/20 train/test split:

* Linear Regression
* Gradient Boosting Regressor
* Random Forest Regressor

# 📈 Model Performance

| Model | R² Score | MAE | RMSE | Status |
| --- | --- | --- | --- | --- |
| **Linear Regression** | **0.9943** | **0.0022** | **0.0038** | **Selected (`best_model.pkl`)** |
| Gradient Boosting | 0.8368 | 0.0159 | 0.0202 | Evaluated |
| Random Forest | 0.6481 | 0.0235 | 0.0296 | Evaluated |

The **Linear Regression** model achieved the highest accuracy ($R^2 = 0.9943$) and was selected as the deployed model because the feature indicators in this dataset have a strong linear/additive relationship with flood probability.

# ⭐ Feature Importance Ranking

Mutual Information scoring identified the top features driving flood probability:

| Rank | Feature | Importance Score |
| --- | --- | --- |
| 1 | Monsoon Intensity | 0.1245 |
| 2 | Drainage Systems | 0.0987 |
| 3 | Urbanization | 0.0876 |
| 4 | Climate Change | 0.0854 |
| 5 | Deforestation | 0.0821 |
| 6 | River Management | 0.0798 |
| 7 | Topography Drainage | 0.0765 |
| 8 | Siltation | 0.0732 |

# ⚙️ Data Preprocessing

The following preprocessing pipeline was applied:

* Handled missing values using median imputation
* Removed duplicate records to prevent learning bias
* Capped extreme feature outliers using the **Interquartile Range (IQR)** method
* Selected top features using **Mutual Information** scoring
* Normalized continuous variables using **RobustScaler**

# 💻 Installation & Setup

Clone the repository:

```bash
git clone https://github.com/Abdrihman-Hussein/Flood-prediction-.git

```

Go to the project folder:

```bash
cd Flood-prediction-

```

Install dependencies:

```bash
pip install -r requirements.txt

```

Run preprocessing & model training:

```bash
python processing.py
python model.py

```

Run the application:

```bash
python app.py

```

# 🖥️ Application Workflow

1. Open your browser at `[http://127.0.0.1:5000/](http://127.0.0.1:5000/)`.
2. Adjust the environmental feature sliders.
3. Click **Predict**.
4. The model processes inputs through `RobustScaler` and the trained regression model.
5. The predicted flood probability and risk level (**Low**, **Moderate**, **High**) are displayed on the dashboard.

# 📄 Example Prediction

Input Payload:

* MonsoonIntensity: 8
* DrainageSystems: 3
* Urbanization: 8
* ClimateChange: 8
* Deforestation: 7
* RiverManagement: 4
* TopographyDrainage: 3
* Siltation: 8

Output:

```text
Flood Probability:
0.82
Risk Level:
High
```

# 📦 Sample JSON Response

```json
{
    "FloodProbability": 0.82,
    "RiskLevel": "High"
}
