# Customer Segmentation & Churn Prediction System

**Prepared by:** Muhiadin Said Hassan  
**Project Type:** Unsupervised Learning (Clustering) & Supervised Learning (Classification)  
**Technologies:** Python, Jupyter Notebook, Scikit-Learn, Pandas, NumPy, Matplotlib, Seaborn

---

## 📌 1. Project Overview & Objective
This project integrates both main branches of Machine Learning to solve one of the most expensive challenges faced by telecom companies and subscription-based services: identifying customers who are on the verge of leaving the company (**Customer Churn**). 

Instead of treating all customers uniformly, the project pipeline is divided into two strategic phases:
1. **Unsupervised Clustering (K-Means):** Used to segment customers into 3 distinct behavioral groups based on their usage metrics and financial engagement (`tenure`, `MonthlyCharges`, `TotalCharges`).
2. **Supervised Classification:** After generating a unique identification for each group (`Segment_ID`), we trained different classification models, namely **Logistic Regression** and **Random Forest**, to predict whether a given customer will cancel their service (Churn: Yes/No).

---

## 📊 2. Dataset Summary
The project is built upon the well-known **Telco Customer Churn dataset (IBM sample data)**.
* **Total Rows:** ~7,043 customers.
* **Key Columns (Features):**
  * `tenure`: Number of months the customer has stayed with the company.
  * `MonthlyCharges` & `TotalCharges`: The monthly and total amount charged to the customer.
  * `Contract`, `InternetService`, `OnlineSecurity`, `TechSupport`: Supplementary services utilized by the customer.
  * `Churn` (Target Variable): Whether the customer churned (1) or stayed (0).

---

## 🛠️ 3. Project Pipeline Steps

### Step 1: Data Preprocessing
* Removed irrelevant columns such as `customerID`.
* Converted the `TotalCharges` column into a numeric format and handled missing values using the median.
* Converted the target column (`Churn`) into a binary format (`0` and `1`).

### Step 2: K-Means Customer Segmentation
* Scaled continuous features using `StandardScaler`.
* Utilized the **Elbow Method** to determine the optimal number of clusters ($K=3$).
* The resulting K-Means assignment (`Segment_ID`) was appended back to the master dataframe to be used as an input feature for the next model phase.

### Step 3: Model Training & Evaluation
* Split the dataset into **80% Train** and **20% Test** sets.
* Applied `OneHotEncoder` to transform categorical variables into numeric values.
* Trained a **Logistic Regression** and a **Random Forest Classifier**, prioritizing the **F1-Score** metric to balance Precision and Recall due to severe class imbalance (more non-churners than churners).

---

## 📈 4. Model Metrics & Evaluation

Below are the performance results captured during model evaluation:

| Model | Accuracy | Precision | Recall | F1-Score |
| :--- | :---: | :---: | :---: | :---: |
| **Logistic Regression** | ~80.2% | ~65.1% | ~54.2% | **~59.1%** |
| **Random Forest** | ~78.8% | ~63.8% | ~47.6% | ~54.5% |

* **Final Decision:** *Logistic Regression* was selected as the optimal deployment model because it produced a higher F1-Score compared to Random Forest, which is crucial for accurately capturing at-risk customers without wasting retention marketing budgets.

---

## 📁 5. Directory Structure

```text
churn-segmentation-project/
│
├── dataset/
│   └── Telco-Customer-Churn.csv         # Raw source customer dataset
│
├── customer_segmentation.ipynb         # Master Jupyter Notebook with end-to-end pipeline
├── elbow_telecom.png                   # Elbow method plot generated from the code
├── telecom_segmented_customers.csv     # Final processed dataset containing Segment_ID
└── README.md                           # This documentation file