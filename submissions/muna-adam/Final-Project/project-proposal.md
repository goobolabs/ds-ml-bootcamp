## 1. Certificate Name

MAYMUN ADEN MOHAMED

## 2. Project Title and Description

**Lung Cancer Risk Level Prediction System**

### Project Description

Lung cancer is one of the leading causes of cancer-related deaths worldwide, and early risk assessment can help improve prevention, diagnosis, and treatment outcomes.

This project develops a machine learning model that predicts a patient's **lung cancer risk level** (**Low**, **Medium**, or **High**) based on demographic information, lifestyle factors, environmental exposure, and medical symptoms, including:

- Age
- Smoking
- Air Pollution
- Alcohol Use
- Genetic Risk
- Chest Pain
- Wheezing
- Shortness of Breath
- Other clinically relevant factors

The goal is to provide an intelligent decision-support tool that helps healthcare professionals identify high-risk individuals more efficiently and encourages early medical evaluation.

## 3. Problem Type

### Problem Type: Multi-Class Classification

This project is a **multi-class classification** problem because the target variable, **Level**, contains three categories:

- **Low**
- **Medium**
- **High**

The machine learning model will learn from patient demographic information, lifestyle factors, environmental exposure, and medical symptoms to predict the correct lung cancer risk level for a new patient.

## 4. Dataset

### Source

The dataset was obtained from **Kaggle**.

**Dataset Link:**  
https://www.kaggle.com/datasets/thedevastator/cancer-patients-and-air-pollution-a-new-link

### Size

The dataset contains **1,000 rows** and **18 columns**. It includes demographic information, lifestyle factors, environmental exposure, and medical symptoms related to lung cancer risk.

### Target Column

**Target Column:** `Level`

The **Level** column represents the predicted lung cancer risk category for each patient. It contains three classes:

- **Low** – Low risk of lung cancer.
- **Medium** – Moderate risk of lung cancer.
- **High** – High risk of lung cancer.

This makes the project a **multi-class classification** problem.

## 5. Algorithms I Plan to Train

To identify the best-performing model, I will train and compare multiple classification algorithms. Since the target variable (**Level**) has three categories (**Low**, **Medium**, and **High**), this project is a **multi-class classification** problem.

| ### | Algorithm | Why It Fits |
|---|-----------|-------------|
| 1 | Logistic Regression | Logistic Regression will be used as a baseline model because it supports multi-class classification and provides an easy-to-interpret benchmark for comparing more advanced models. |
| 2 | Decision Tree Classifier | Decision Trees are suitable because they can learn decision rules from patient symptoms, lifestyle factors, and environmental risk factors, making the predictions easy to understand and explain. |
| 3 | Random Forest Classifier | Random Forest combines multiple decision trees, making it more accurate and less likely to overfit. It performs well on structured medical datasets with many health-related features. |
| 4 | Gradient Boosting Classifier | Gradient Boosting is a powerful ensemble algorithm that captures complex relationships between multiple lung cancer risk factors and often achieves high predictive performance on tabular datasets. |

## 6. Evaluation Plan

To compare the performance of all classification models, I will use the following evaluation metrics:

- **Accuracy** – Measures the overall percentage of correctly classified patients.
- **Precision** – Measures how many patients predicted to belong to a specific risk level are actually in that risk level.
- **Recall** – Measures how many patients in each actual risk level are correctly identified by the model.
- **F1-Score** – Balances Precision and Recall, providing a reliable measure of overall classification performance, especially when class distributions are not perfectly balanced.

### Best Model Selection

The best model will be selected based on the **F1-Score**.

**Reason:**  

This project is a **multi-class classification** problem with three classes (**Low**, **Medium**, and **High**). The **F1-Score** is the most appropriate metric because it balances **Precision** and **Recall**, ensuring that the model not only makes accurate predictions but also correctly identifies patients in each lung cancer risk category. This makes it a more reliable metric than Accuracy alone for selecting the best overall model.

## 7. Deployment Sketch

### Deployment Method

This project will be deployed using **Streamlit**, which provides an interactive web application for the machine learning model. Users will enter patient information through a simple web interface, and the application will instantly display the predicted lung cancer risk level.

### User Input

The Streamlit application will allow users to enter the following information:

- Age
- Gender
- Air Pollution
- Alcohol Use
- Dust Allergy
- Occupational Hazards
- Genetic Risk
- Chronic Lung Disease
- Smoking
- Passive Smoker
- Chest Pain
- Coughing of Blood
- Fatigue
- Weight Loss
- Shortness of Breath
- Wheezing
- Swallowing Difficulty
- Dry Cough

### Output

After clicking the **Predict** button, the application will display:

- **Predicted Lung Cancer Risk Level** (Low, Medium, or High)
- **Prediction Confidence (Probability)**

The interface will be simple, interactive, and user-friendly, allowing users to quickly enter patient information and receive an instant lung cancer risk level prediction.

## 8. Repository Plan

The GitHub repository will be organized to keep the project files clear, simple, and easy to navigate.

```text
lung-cancer-risk-level-prediction/
│
├── dataset/                 # Contains the dataset used for training and evaluation
│   └── lung_cancer_data.csv
│
├── models/                  # Stores the trained machine learning model(s)
│   ├── lung_cancer_model.pkl
│   └── label_encoder.pkl
│
├── app.py                   # Main Streamlit application (User interface and prediction)
│
├── README.md                # Project overview, setup instructions, and usage guide
│
├── project_paper.md         # Detailed project report and documentation
│
```
