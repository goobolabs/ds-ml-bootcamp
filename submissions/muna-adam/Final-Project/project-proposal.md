# 1. Certificate Name

MAYMUN ADEN MOHAMED

# 2. Project Title and Description

**Pulmonary Disease Prediction Using Machine Learning**

## Project Description

This project aims to predict whether a person is at risk of pulmonary disease using demographic information, lifestyle habits, medical history, and health-related symptoms.

The machine learning model analyzes features such as:

- Age
- Smoking status
- Exposure to pollution
- Breathing issues
- Oxygen saturation (SpO₂)
- Family history of pulmonary disease
- Other relevant health indicators

Based on these features, the model classifies individuals as either:

- **At Risk of Pulmonary Disease**
- **Not At Risk of Pulmonary Disease**

The project demonstrates how machine learning can support healthcare researchers, students, and medical professionals by assisting in disease risk prediction and early assessment using healthcare data.

## 3. Problem Type

### Classification (Binary Classification)

This project is a **binary classification** problem because the objective is to predict a categorical outcome rather than a continuous numerical value. The target variable, **PULMONARY_DISEASE**, has two possible classes:

- **1** – Has Pulmonary Disease
- **0** – Does Not Have Pulmonary Disease

The machine learning model learns patterns from patient information, including:

- Age
- Smoking status
- Exposure to pollution
- Breathing issues
- Oxygen saturation (SpO₂)
- Family history
- Other health-related features

Using these inputs, the model predicts whether an individual is **at risk of pulmonary disease** or **not at risk of .

# 4. Dataset

## Source

**Kaggle – Lung Cancer Prediction Dataset**

Dataset https://www.kaggle.com/datasets/shantanugarg274/lung-cancer-prediction-dataset

## Size

- **Rows (Instances):** 5,000

## Target Column

**PULMONARY_DISEASE**

This is the target variable used for binary classification. It indicates whether an individual has pulmonary disease.

- **1** = Has Pulmonary Disease
- **0** = Does Not Have Pulmonary Disease

## Main Features
## Main Features
## Main Features

| Feature | Description |
|---------|-------------|
| Age | Age of the individual. |
| Gender | Gender of the individual. |
| Smoking | Indicates whether the individual is a smoker. |
| Finger_Discoloration | Presence of finger discoloration. |
| Mental_Stress | Level of mental stress experienced by the individual. |
| Exposure_to_Pollution | Level of exposure to environmental air pollution. |
| Long_Term_Illness | Indicates whether the individual has a long-term illness. |
| Energy_Level | Energy level of the individual. |
| Immune_Weakness | Indicates whether the individual has a weakened immune system. |
| Breathing_Issue | Presence of breathing difficulties. |
| Alcohol_Consumption | Alcohol consumption status. |
| Throat_Discomfort | Presence of throat discomfort. |
| Oxygen_Saturation | Blood oxygen (SpO₂) level. |
| Chest_Tightness | Presence of chest tightness. |
| Family_History | Family history of pulmonary disease. |
| Smoking_Family_History | Family history of smoking. |
| Stress_Immune | Indicates whether stress has affected the immune system. |
| Pulmonary_Disease | **Target variable** indicating whether the individual has pulmonary disease (Yes/No). |
sease (Yes/No). |
```
# 5. Algorithms You Plan to Train

The following machine learning algorithms will be trained and compared to determine which model performs best for predicting pulmonary disease.

| Algorithm | Why It Fits This Problem |
|-----------|---------------------------|
| **Logistic Regression** | Logistic Regression is a strong baseline algorithm for binary classification and predicts whether a patient has pulmonary disease (1) or not (0). |
| **Decision Tree Classifier** | Decision Tree can capture non-linear relationships between patient characteristics and disease status, while also providing easy-to-understand decision rules. |
| **Random Forest Classifier** | Random Forest combines multiple decision trees to improve prediction accuracy, reduce overfitting, and handle complex healthcare data effectively. |
| **XGBoost Classifier** | XGBoost is an advanced ensemble learning algorithm that often achieves high performance by efficiently learning complex patterns in structured datasets. |

# 6. Evaluation Plan

To evaluate and compare the performance of the machine learning models, the following classification metrics will be used:

- **Accuracy** – Measures the overall percentage of correctly classified predictions.
- **Precision** – Measures how many patients predicted to have pulmonary disease actually have the disease.
- **Recall** – Measures how many actual pulmonary disease cases are correctly identified by the model.
- **F1-Score** – Combines Precision and Recall into a single metric, providing a balanced measure of model performance.

## Best Model Selection

The **F1-Score** will be used as the primary metric to select the best model.

**Reason:** In disease prediction, both **False Positives** and **False Negatives** are important. A model with a high F1-Score balances **Precision** and **Recall**, making it more reliable for identifying patients at risk while minimizing incorrect predictions. Therefore, F1-Score is a more suitable metric than Accuracy alone for this binary classifica

tion problem.able metric than Accuracy alone for selecting the best overall model.

## 7. Deployment Sketch

### Deployment Method

This project will be deployed using **Streamlit**, which provides an interactive web application for the machine learning model. Users will enter patient information through a simple web interface, and the application will instantly display the predicted lung cancer risk level.

## User Input

The Streamlit application will allow users to enter the following information:

- Age
- Gender
- Smoking
- Finger Discoloration
- Mental Stress
- Exposure to Pollution
- Long-Term Illness
- Energy Level
- Immune Weakness
- Breathing Issue
- Alcohol Consumption
- Throat Discomfort
- Oxygen Saturation
- Chest Tightness
- Family History
- Smoking Family History
- Stress Immune

## Output

After clicking the **Predict** button, the application will display:

- **Predicted Pulmonary Disease Status** (Yes or No)
- **Prediction Confidence (%)**
- **Risk Status:** High Risk or Low Risk based on the model's prediction

## 8. Repository Plan

The GitHub repository will be organized to keep the project files clear, simple, and easy to navigate.

```text
lung-cancer-risk-level-prediction/
│
├── dataset/                 # Contains the dataset used for training and evaluation
│   └── pulmonary_disease.csv
│
├── models/                  # Trained machine learning files
│   ├── best_model.pkl
│   └── scaler.pkl
│
├── app.py                   # Main Streamlit application (User interface and prediction)
│
├── README.md                # Project overview, setup instructions, and usage guide
│
├── project_paper.md         # Detailed project report and documentation
```_encoder.pkl
│
├── app.py                   # Main Streamlit application (User interface and prediction)
│
├── README.md                # Project overview, setup instructions, and usage guide
│
├── project_paper.md         # Detailed project report and documentation
│
```
