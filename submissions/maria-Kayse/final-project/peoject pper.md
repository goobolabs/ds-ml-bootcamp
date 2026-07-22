# 🏨 Machine Learning Framework for Hotel Booking Cancellation Prediction and Customer Segmentation

**Author:** Maryan Ahmed Warsame  
**GitHub Repository:** https://github.com/maria-Kayse/hotel-booking-cancellation
---

## Abstract
Uncertainty in hotel room reservations presents a critical financial and operational challenge for the hospitality industry. Unannounced cancellations directly impair revenue forecasting, room capacity management, and staffing efficiency. 
This paper presents an end-to-end Machine Learning pipeline engineered to predict hotel booking cancellations in real time and perform unsupervised customer behavioral segmentation. 
Utilizing the Hotel Booking Demand dataset (reduced from 119,390 to 87,396 records post-cleaning and deduplication), three classification algorithms—Logistic Regression, Random Forest, and XGBoost—were systematically trained and evaluated.
 Although XGBoost achieved a higher overall accuracy (0.75), Random Forest was selected for production deployment due to its superior F1-Score (0.52 vs 0.32) and effective handling of minority class imbalance via `class_weight="balanced"`. Furthermore, customer segmentation using K-Means and Agglomerative Clustering was performed to discover hidden customer groups. The optimal classification pipeline was deployed as a FastAPI web service integrated with a responsive web interface.

---

## 1. Problem Statement and Motivation

Booking cancellations are among the most revenue-disruptive factors in hotel operations. When a guest cancels a reservation on short notice, the room often remains vacant, leading to direct financial loss and inefficient resource allocation. Traditional mitigation techniques, such as overbooking or non-refundable policies, can degrade guest satisfaction if managed improperly.

By leveraging predictive analytics, hotel managers can proactively identify high-risk bookings prior to arrival. Accurate predictions enable targeted retention strategies (e.g., offering customized discounts, requiring early deposits, or sending personalized follow-ups), thereby safeguarding operational revenue. 

The primary objective of this project is twofold:
1. Develop a supervised classification pipeline to accurately predict whether a booking will be **Canceled (1)** or **Not Canceled (0)** at inference time.
2. Apply unsupervised clustering to discover implicit customer behavioral segments to assist hotel strategy teams.

---

## 2. Dataset and Preprocessing

### 2.1 Dataset Description
The dataset used in this study is the benchmark **Hotel Booking Demand Dataset**, initially comprising **119,390 records** and **32 raw attributes**. The dataset captures booking details from both Resort and City hotels.

### 2.2 Data Cleaning & Quality Control
A rigorous data preparation methodology was executed to prevent data leakage and noise:
* **Missing Value Imputation:** Missing instances in the `Children` feature were imputed with `0`.
* **Deduplication:** A total of **31,994 exact duplicate rows** were identified and purged, yielding a refined clean dataset of **87,396 unique observations**.
* **Outlier Mitigation:** The Interquartile Range (IQR) thresholding technique was applied to continuous numerical features including `LeadTime`, `ADR`, `Adults`, `Children`, `PreviousCancellations`, `PreviousBookingsNotCanceled`, and `BookingChanges`.
* **Leakage Prevention:** Attributes that reveal information available only after reservation finalization—such as `ReservationStatus`, `ReservationStatusDate`, `AssignedRoomType`, `Company`, `Agent`, `ArrivalDateYear`, and `Country`—were explicitly dropped. The final subset contains **16 core features**.

### 2.3 Feature Engineering and Transformation
Categorical attributes (`ArrivalDateMonth`, `Meal`, `MarketSegment`, `DistributionChannel`, `DepositType`, and `CustomerType`) were converted into numerical features using **One-Hot Encoding**, resulting in **40 input dimensions**. Continuous numerical predictors were standardized using Scikit-Learn’s `StandardScaler` prior to model training.

### 2.4 Class Imbalance Strategy
The clean dataset exhibited an intrinsic skew toward non-canceled bookings. To address majority class bias, the Random Forest model was trained with **`class_weight="balanced"`**, improving its sensitivity and ability to detect actual canceled bookings.

---

## 3. Algorithms

Three distinct supervised classification algorithms and two unsupervised clustering techniques were evaluated:

### 3.1 Classification Algorithms
1. **Logistic Regression (Baseline Model):** Serves as a benchmark linear model to establish baseline performance metrics.
2. **Random Forest Classifier (Bagging Architecture):** An ensemble of randomized decision trees that handles non-linear feature interactions and built-in class weight balancing.
3. **XGBoost Classifier (Gradient Boosting Framework):** An optimized gradient boosting framework evaluated for comparison against bagging models.

### 3.2 Unsupervised Clustering Algorithms
* **K-Means & Agglomerative Clustering:** Applied using key behavioral features (`LeadTime`, stay duration, `Adults`, `PreviousCancellations`, `BookingChanges`, and `ADR`) to discover hidden customer groups and generate strategic business insights. Clustering was used solely for exploratory analysis and customer segmentation, rather than real-time cancellation predictions.

---

## 4. Results and Discussion

### 4.1 Comparative Model Performance
Models were evaluated using Accuracy, Precision, Recall, F1-Score, and ROC-AUC. F1-Score was prioritized as the primary metric due to class imbalance in cancellation labels.

| Model | Accuracy | F1-Score | ROC-AUC | Decision Status |
| :--- | :---: | :---: | :---: | :---: |
| **Logistic Regression** | 0.65 | 0.53 | 0.72 | Baseline |
| **Random Forest** | **0.72** | **0.52** | **0.75** | **SELECTED FOR DEPLOYMENT** |
| **XGBoost** | 0.75 | 0.32 | 0.76 | Rejected (Low F1-Score) |

### 4.2 Selection Rationale
Although **XGBoost** achieved the highest raw Accuracy (0.75) and ROC-AUC (0.76), its **F1-Score dropped to 0.32** on the canceled class, meaning it missed a significant number of actual cancellations. **Random Forest** was chosen as the winning model because it maintained a balanced F1-Score (0.52) and effective minority-class detection, providing superior practical utility for hotel revenue protection.

### 4.3 Model Sanity Checks
Three sample scenarios were tested against the deployed model pipeline to verify prediction integrity:

* **Sanity Check 1 (High Lead-Time & Cancellations):** Input with `LeadTime: 250`, `PreviousCancellations: 2`, `DepositType: "No Deposit"`.  
  * *Result:* `Prediction: 1 (Canceled) | Confidence: 62.9%` *(Passed)*
* **Sanity Check 2 (Short Lead-Time & Regular Guest):** Input with `LeadTime: 5`, `PreviousBookingsNotCanceled: 4`, `CustomerType: "Transient"`.  
  * *Result:* `Prediction: 0 (Not Canceled)` *(Passed)*
* **Sanity Check 3 (Non-Refundable Deposit):** Input with `LeadTime: 120`, `DepositType: "Non Refund"`.  
  * *Result:* `Prediction: 0 (Not Canceled)` *(Passed)*

---

## 5. Deployment Notes

The solution follows a decoupled Client-Server architecture:

1. **Backend API:** Built using **FastAPI**, serving a `/predict` REST endpoint. It accepts booking payload JSON, applies scaling and feature alignment, and returns predictions with confidence scores.
2. **Frontend Interface:** A modern, responsive HTML/CSS/JavaScript interface that communicates with the backend via Async Fetch API requests.

### 5.1 Example API Request (`curl`)
```bash
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

## 6. Lessons Learned

### 6.1 Challenges Faced & Key Takeaways
* **CORS & Data Pipeline Integration:** Configuring FastAPI headers to allow seamless cross-origin communication with local browser contexts.
* **Schema Alignment:** Ensuring categorical columns encoded during model training aligned perfectly with inference payloads using feature reindexing routines.
* **Evaluation Metrics Matter:** Learning that overall accuracy can be misleading in imbalanced problems, and F1-score is crucial for choosing the right operational model.

### 6.2 Future Improvements
* Fine-tuning hyperparameters using Optuna or GridSearch.
* Testing advanced class imbalance handling techniques.
* Additional feature engineering to extract richer behavioral signals.
* Containerizing with Docker and deploying to cloud platforms (e.g., Render or AWS).