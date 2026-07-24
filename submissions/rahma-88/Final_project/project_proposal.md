# Income Level Prediction using Adult Census Data

## Certification Name

- **Rahma Mohamud Abdi**

## 1. Project Title and Description

### Predictive Modeling for Socioeconomic Status: Adult Census Income Classification

This project addresses the real-world challenge of predicting an individual's income bracket (whether they earn over \$50,000 annually) based on demographic, employment, and educational characteristics. Understanding the drivers of income inequality and socioeconomic status is crucial for non-profit organizations, credit institutions, and government policymakers. By analyzing these relationships, financial institutions can better assess risk and creditworthiness, while public agencies and charitable groups can optimize resource allocation and design targeted wealth-building interventions to assist underserved communities.

---

## 2. Problem Type

This project is a **Binary Classification** problem. The objective is to map various personal, financial, and employment attributes to a categorical target variable with two distinct classes: `>50K` (high income) and `<=50K` (low-to-moderate income). Because this is a supervised classification task, the model will output a predictive category alongside a class probability score, making it straightforward to deploy via a RESTful `/predict` API endpoint.

---

## 3. Dataset

- **Source:** UCI Machine Learning Repository / Kaggle
  - [Kaggle Dataset Link](https://www.kaggle.com/datasets/uciml/adult-census-income)
  - [UCI Repository Link](https://archive.ics.uci.edu/dataset/2/adult+income)
- **Size:** The dataset contains **48,842 rows** (combined training and testing splits), easily exceeding the 1,000-row minimum requirement.
- **Target Column:** `income` (Categorical: `>50K` or `<=50K`), representing whether an individual’s annual income exceeds \$50,000.
- **Main Features:**
  - `age`: Continuous numerical variable representing the individual's age.
  - `workclass`: Categorical variable indicating the employment sector (e.g., Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov).
  - `education`: Categorical variable indicating the highest level of education completed (e.g., Bachelors, HS-grad, Masters, Doctorate).
  - `education.num`: Continuous numerical variable representing the educational achievements as an ordered numeric scale.
  - `marital.status`: Categorical variable indicating relationship status (e.g., Married-civ-spouse, Divorced, Never-married).
  - `occupation`: Categorical variable describing the type of job (e.g., Tech-support, Craft-repair, Exec-managerial, Prof-specialty).
  - `relationship`: Categorical variable describing the role within the household (e.g., Wife, Own-child, Husband, Not-in-family).
  - `race`: Categorical variable representing racial background (e.g., White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black).
  - `sex`: Categorical variable for gender (Male, Female).
  - `capital.gain`: Continuous numerical variable recording capital profits from financial investments.
  - `capital.loss`: Continuous numerical variable recording capital losses from financial investments.
  - `hours.per.week`: Continuous numerical variable tracking working hours per week.
  - `native.country`: Categorical variable stating the country of origin.

---

## 4. Algorithms You Plan to Train

To identify the most robust predictive model, three distinct machine learning algorithms will be evaluated:

1.  **Logistic Regression (Bootcamp Core):** This linear baseline fits the classification task well because it handles high-dimensional, encoded categorical features efficiently and provides a clear probabilistic interpretation of feature coefficients.
2.  **Random Forest Classifier (Bootcamp Core):** This ensemble method is ideal because it handles non-linear relationships, interacts well with skewed continuous features like `capital.gain`, and naturally resists overfitting through tree bagging.
3.  **XGBoost / Gradient Boosting Classifier (Self-Researched):** This advanced tree-boosting technique is selected because it sequentially corrects errors made by weak learners, routinely achieving state-of-the-art predictive performance on highly diverse tabular datasets.

---

## 5. Evaluation Plan

- **Comparison Metrics:** Models will be comprehensively cross-evaluated using **Accuracy**, **Precision**, **Recall (Sensitivity)**, and the **F1-Score**.
- **Primary Decision Metric:** The **F1-Score** will be used to select the final champion model.
- **Justification:** The Adult Census dataset exhibits a notable class imbalance, with roughly 75% of individuals earning `<=50K` and only 25% earning `>50K`. Optimizing for pure accuracy would yield a deceptive model that ignores the minority class; the F1-Score acts as the harmonic mean of precision and recall, ensuring that the model maintains a high true positive rate while minimizing false alarms.

---

## 6. Deployment Sketch

- **Framework:** **FastAPI** will be used to build the production application due to its high performance, native asynchronous architecture, and automated OpenAPI documentation generation.
- **Endpoint Input (`/predict` JSON payload):**
  ```json
  {
    "age": 38,
    "workclass": "Private",
    "education": "Bachelors",
    "education_num": 13,
    "marital_status": "Married-civ-spouse",
    "occupation": "Exec-managerial",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital_gain": 15024,
    "capital_loss": 0,
    "hours_per_week": 40,
    "native_country": "United-States"
  }
  ```
- **Endpoint Output (JSON response):**
  ```json
  {
    "prediction": ">50K",
    "probability_above_50k": 0.892,
    "model_version": "1.0.0",
    "status": "success"
  }
  ```


# REPO URL
https://github.com/rahma-88/census_adult_income