# 🏨 Hotel Booking Cancellation Prediction API

This project predicts whether a hotel booking will be canceled using Machine Learning. It provides an end-to-end pipeline from data preprocessing to model evaluation and interactive web-API deployment.

---

## 📅 Dataset Details

* **Source:** [Hotel booking demand datasets (Kaggle)]https://www.kaggle.com/datasets/pattae/hotel-booking-demand-datasets
* **Size:** Originally 119,390 records and 32 features. After cleaning and deduplication, the final dataset contains **87,396 records** and **16 core features**.
* **Target Variable:** `is_canceled` (0 = Not Canceled, 1 = Canceled)

---

## 🤖 Algorithms Used

At least three distinct algorithms were trained and evaluated on the same preprocessed dataset:
1. **Logistic Regression** (Linear baseline model)
2. **Random Forest Classifier** (Ensemble tree-based model with class balancing)
3. **XGBoost Classifier** (Gradient boosting algorithm)

---

## 📊 Comparison Table & Winning Model

| Algorithm | Accuracy | F1-Score (Canceled) | ROC-AUC | Status |
| :--- | :---: | :---: | :---: | :---: |
| **Logistic Regression** | 0.65 | 0.53 | 0.72 | Baseline |
| **Random Forest** | **0.72** | **0.52** | **0.75** | **WINNER (Deployed)** |
| **XGBoost** | 0.75 | 0.32 | 0.76 | Rejected (Low F1) |

🏆 **Winning Model:** **Random Forest** was selected for deployment because it provided the best balance for predicting canceled bookings (higher F1-Score on class 1 and effective handling of class imbalance) compared to XGBoost, which struggled with minority class recall.

---

## 🛠️ Example Commands

### 1. Install Dependencies
```bash
pip install -r requirements.txt
python src/train.py


curl -X POST [http://127.0.0.1:8000/predict](http://127.0.0.1:8000/predict) \
  -H "Content-Type: application/json" \
  -d '{
    "LeadTime": 30,
    "ArrivalDateMonth": "July",
    "StaysInWeekendNights": 0,
    "StaysInWeekNights": 2,
    "Adults": 2,
    "Children": 0,
    "Meal": "BB",
    "MarketSegment": "Online TA",
    "DistributionChannel": "TA/TO",
    "PreviousCancellations": 0,
    "PreviousBookingsNotCanceled": 0,
    "BookingChanges": 0,
    "DepositType": "No Deposit",
    "CustomerType": "Transient",
    "ADR": 100.0
  }'

  
  JSON
{
  "model": "Random Forest",
  "prediction": 1,
  "label": "Canceled",
  "confidence": 0.629
}

#### **7. Results Summary**
Preprocessing and removing 31,994 duplicate records significantly improved model reliability. Although XGBoost achieved the highest overall accuracy, Random Forest proved superior in detecting actual booking cancellations by maintaining a higher F1-score on the minority class. This makes Random Forest the most viable operational model for reducing hotel revenue loss.

---

#### **Author**
* **Maryan Ahmed Warsame** 

GitHub Repository:   https://github.com/maria-Kayse/hotel-booking-cancellation.git