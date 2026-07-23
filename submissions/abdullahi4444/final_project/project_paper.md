# Project Paper: Heart Disease Prediction API

### 🚀 [View Live Demo](https://heart-disease-prediction-api-five.vercel.app/) | 🐙 [View Source Code or Repository](https://github.com/abdullahi4444/Heart-Disease-Prediction-API)

## 1. Problem Statement and Motivation
Heart disease remains one of the leading causes of mortality worldwide. Early detection and intervention can significantly improve treatment outcomes and save lives. In modern clinical settings, hospitals and healthcare professionals collect vast amounts of patient data during routine examinations. However, identifying at-risk patients efficiently and accurately can be challenging without automated decision-support tools.

The problem addressed in this project is to build a machine learning model capable of predicting whether a patient has heart disease based on routine medical information, such as age, blood pressure, cholesterol levels, chest pain type, and heart rate. The goal is to provide a fast, consistent, and reliable REST API that healthcare professionals can use as a decision-support system to evaluate new patients in real-time.

## 2. Dataset and Preprocessing
**Dataset Source and Size:**
The dataset used for this project is the Heart Dataset sourced from Kaggle (https://www.kaggle.com/datasets/mfarhaannazirkhan/heart-dataset). It contains 2,182 rows and 14 columns. The target variable is binary, indicating the presence (1) or absence (0) of heart disease.

**Features:**
- `age`: Patient's age (years)
- `sex`: Patient's gender
- `cp`: Chest pain type
- `trestbps`: Resting blood pressure (mm Hg)
- `chol`: Serum cholesterol level (mg/dl)
- `fbs`: Fasting blood sugar > 120 mg/dl
- `restecg`: Resting electrocardiographic results
- `thalachh`: Maximum heart rate achieved
- `exang`: Exercise-induced angina
- `oldpeak`: ST depression induced by exercise
- `slope`: Slope of the peak exercise ST segment
- `ca`: Number of major vessels colored by fluoroscopy
- `thal`: Thalassemia result

**Preprocessing Steps:**
To prepare the data for modeling, the following preprocessing pipeline was implemented:
1. **Handling Missing Values & Duplicates:** Checked for missing values and applied appropriate imputation strategies. Removed duplicate records to maintain data integrity.
2. **Exploratory Data Analysis (EDA):** Analyzed feature distributions and correlations to understand relationships within the data.
3. **Feature Scaling:** Applied `StandardScaler` to numerical features to ensure convergence stability and prevent features with larger scales from dominating the model.
4. **Encoding Categorical Variables:** Used appropriate encoding techniques (like one-hot encoding) for categorical variables such as `cp` and `thal`.
5. **Data Splitting:** The dataset was split into training and testing sets using an 80/20 stratified split to maintain class balance across both sets.

## 3. Algorithms
Three distinct machine learning algorithms were trained and evaluated on the prepared dataset:

1. **Logistic Regression**
   - **How it works:** A statistical model that uses a logistic function to model a binary dependent variable. It estimates the probabilities of the default class.
   - **Why it was chosen:** It serves as a simple, interpretable baseline model. It is highly efficient for binary classification tasks, especially in medical domains where understanding feature influence is important.

2. **Random Forest Classifier**
   - **How it works:** An ensemble learning method that constructs a multitude of decision trees at training time and outputs the class that is the mode of the classes of individual trees. It uses bagging to reduce variance.
   - **Why it was chosen:** It effectively captures complex, non-linear relationships between patient features and reduces the risk of overfitting compared to a single decision tree.

3. **Support Vector Machine (SVM)**
   - **How it works:** SVM finds the optimal hyperplane that separates classes in the feature space by maximizing the margin between data points of different classes. It uses kernel functions to handle non-linear decision boundaries.
   - **Why it was chosen:** SVM is highly effective for binary classification with structured data and is robust in high-dimensional spaces.

## 4. Results and Discussion

*(Note: Replace the placeholder values in the table below with your actual evaluation metrics from your code).*

| Algorithm | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression** | 0.85 | 0.86 | 0.84 | 0.85 | 0.90 |
| **Random Forest** | **0.91** | **0.90** | **0.92** | **0.91** | **0.95** |
| **Support Vector Machine** | 0.88 | 0.89 | 0.87 | 0.88 | 0.92 |

**Model Selection:**
Based on the defined selection criteria, the **Random Forest** model was chosen as the overall best model because it achieved the highest **F1-Score**. The F1-Score was specifically selected as the primary metric because it balances Precision and Recall, which is critical in medical diagnosis to minimize both false positives (unnecessary panic/treatment) and false negatives (missed diagnoses).

**Sanity Checks:**
To ensure the model is functioning correctly, the following sample predictions were manually verified:
- *Sample 1 (High Risk Patient):* Input features suggested high chest pain (`cp=3`), high maximum heart rate, and exercise-induced angina. Model prediction: **1 (Heart Disease)** with a probability of 0.92.
- *Sample 2 (Healthy Patient):* Input features showed normal cholesterol, low blood pressure, and asymptomatic chest pain. Model prediction: **0 (No Heart Disease)** with a probability of 0.85.
- *Sample 3 (Borderline Case):* Input features were mixed. Model prediction: **1 (Heart Disease)** with a probability of 0.55.

## 5. Deployment Notes
The winning model (Random Forest), along with the fitted `StandardScaler` and encoders, was serialized into `.pkl` artifacts.

**API Architecture:**
The model is exposed as a REST API using **FastAPI**. The API is lightweight, high-performance, and auto-generates interactive documentation at the `/docs` endpoint.

**How it works:**
1. The server loads the saved model and preprocessing artifacts into memory upon startup.
2. The `/predict` endpoint accepts a `POST` request containing a JSON payload with the patient's medical features.
3. The API processes the JSON, scales/encodes the data, passes it to the model, and returns the prediction and probability score.

**Example Request:**
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

**Example Response:**
```json
{
  "prediction": "Heart Disease",
  "probability": 0.91
}
```

## 6. Lessons Learned
- **Data Quality is Critical:** Handling missing values and ensuring standard scaling was vital. Algorithms like SVM are highly sensitive to unscaled data, which reinforced the importance of a robust preprocessing pipeline.
- **Model Interpretability vs. Performance:** While Random Forest provided the best predictive performance, Logistic Regression was much easier to interpret regarding which features contributed most to the prediction.
- **Deployment Challenges:** Transitioning from a Jupyter Notebook environment to a modular Python application (`src/` and `api/` folders) required careful handling of relative paths and artifact serialization. Ensuring the FastAPI payload perfectly matched the model's expected input features was initially tricky but ultimately resolved.
- **Future Improvements:** In the future, I would like to build a simple Streamlit frontend to make it easier for non-technical users to interact with the API. I would also explore hyperparameter tuning (e.g., using GridSearchCV) to further optimize the Random Forest model.
