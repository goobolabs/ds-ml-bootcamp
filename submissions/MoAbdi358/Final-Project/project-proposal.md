# Final Project Proposal

## 1. Certificate Name

Mohamed Abdi Ahmed

## 2. Project Title and Description

**Title:** Customer Repeat Purchase Prediction API

When people buy from an online store for the first time, many of them never come back. This is a big problem for businesses because keeping an existing customer is cheaper than finding a new one. This project builds a machine learning model that looks at a customer's early purchase behavior and predicts whether they will buy again within a set follow-up window. It uses information like how much they spent, how many items they bought, and what country they are from. The final result is a REST API that takes customer data as JSON and returns a prediction with a probability score. Marketing teams can use this to find likely one-time buyers early and send them discounts or follow-up emails to bring them back.

## 3. Problem Type

**Classification — binary output:** Repeat Buyer (1) or One-Time Buyer (0).

This is supervised learning. The target column is `repeat_purchase`. I will create this label using a **time-cutoff approach** to avoid data leakage (see Section 4 for details): a customer is labeled 1 if they made at least one more purchase after a defined observation window following their first purchase, and 0 if they did not.

## 4. Dataset

**Source:** Online Retail II — UCI Machine Learning Repository (Kaggle mirror by mashlyn).
- Kaggle link: https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci
- UCI link: https://archive.ics.uci.edu/dataset/502/online+retail+ii

**Size:** The raw data has 1,067,371 transaction rows from an online store in the UK between 01/12/2009 and 09/12/2011 (confirmed via the UCI Machine Learning Repository listing). This is the base dataset and is far above the 1,000-row minimum. After cleaning and grouping by customer, the working (per-customer) dataset will have approximately 5,942 rows — one row per customer — which is also documented clearly as a derived modeling table in the README and paper.

**Original columns in the dataset:**
- Invoice — the invoice number for each transaction
- StockCode — the product code
- Description — product name
- Quantity — how many items were bought
- InvoiceDate — date and time of the purchase
- Price — price of one item (in GBP)
- Customer ID — unique customer number
- Country — which country the customer is from

**Avoiding data leakage — time-cutoff approach:**
If I built features from a customer's *entire* purchase history (e.g. `total_transactions`, `total_spend` across all their invoices) and then labeled `repeat_purchase` based on whether that same history contains more than one invoice, the label would leak directly into the features (e.g. `total_transactions > 1` would almost perfectly predict `repeat_purchase = 1`). To avoid this, I will use only the information available in a **90-day observation window after each customer's first purchase** to build features, and I will define the label using purchases that happen **after** that window:
- **Observation window:** first purchase date (day 0) through day 90.
- **Features** are computed only from transactions inside this 90-day window.
- **Label (`repeat_purchase`):** 1 if the customer has at least one more purchase *after* day 90, 0 if they do not.
- Customers whose first purchase is too close to the end of the dataset's date range (i.e. there isn't enough time left to observe a possible repeat purchase) will be excluded, since we cannot fairly label them.

**Target column (created from the data):**
- `repeat_purchase` — 1 if the customer purchased again after the 90-day observation window, 0 if they did not

**Features I will create from the raw data (all computed only within the 90-day observation window):**
- `total_spend` — total money the customer spent in the window (Quantity x Price, added up)
- `avg_order_value` — average money spent per invoice in the window
- `total_items` — total number of items bought in the window
- `total_transactions` — number of invoices in the window
- `unique_products` — how many different products bought in the window
- `days_between_first_and_last_purchase` — spread of purchasing activity within the window
- `purchase_frequency` — transactions divided by active days in the window
- `avg_items_per_order` — average number of items per invoice in the window
- `country` — customer's country (will be encoded as a number)
- `has_returned_items` — 1 if the customer returned an item during the window, 0 if not

**Preprocessing steps:**
- Remove rows where Customer ID is missing
- Remove or separately flag cancelled orders (invoices that start with "C")
- Determine each customer's first purchase date, then build the 90-day observation window per customer
- Exclude customers whose first purchase is too close to the end of the dataset (not enough remaining time to observe a repeat purchase)
- Group transactions within each customer's window to calculate the features above
- Label each customer using purchases that occur after their window
- Encode the Country column so the model can use it
- Scale all numeric features using StandardScaler
- Split data into 80% training and 20% testing, keeping the same ratio of repeat vs one-time buyers in both sets (stratified split)

## 5. Algorithms I Plan to Train

| # | Algorithm | Why I chose it |
|---|-----------|----------------|
| 1 | **Logistic Regression** | This is from the bootcamp. It is a good starting point for binary classification. It is fast and easy to understand. It also shows which features matter most for predicting repeat purchases. |
| 2 | **Decision Tree** | This is from the bootcamp. It can find patterns that are not straight lines. For example, it can learn rules like "if a customer spends more than X and buys more than Y products, they will likely return." It is also easy to draw and explain. |
| 3 | **Random Forest** | This is from the bootcamp. It builds many decision trees and combines their results. This reduces overfitting compared to a single tree. It also tells us which features are most important. |
| 4 | **Gradient Boosting (sklearn)** | This is one I will research on my own. It builds trees one at a time, where each new tree fixes the mistakes of the previous ones. It often performs very well on table data like this. |

I will train four algorithms, which is more than the required three. Three of them (Logistic Regression, Decision Tree, Random Forest) were taught in the bootcamp. I will learn Gradient Boosting from the scikit-learn documentation and tutorials. I may add more algorithms if I have time.

## 6. Evaluation Plan

**Metrics I will use for all models** (tested on the same test set):
- **Accuracy** — how many predictions are correct overall
- **Precision** — out of all customers predicted as repeat buyers, how many actually are
- **Recall** — out of all actual repeat buyers, how many did the model find
- **F1-Score** — the average of Precision and Recall
- **Confusion Matrix** — a table showing true positives, true negatives, false positives, and false negatives

**How I will pick the best model:** I will rank all models by **F1-Score** on the test set. I chose F1 because it balances Precision and Recall, and both matter here. A false positive means we waste marketing money on someone who was not going to return. A false negative means we miss a real repeat buyer who could have been kept with a small offer. If two models have the same F1-Score, I will pick the one with higher Recall, because it is better to reach more real repeat buyers even if we spend a little extra.

I will print a comparison table with one row per algorithm and only save and deploy the winning model.

## 7. Deployment Sketch

**Framework:** FastAPI. It is simple, modern, and creates API documentation automatically at `/docs`.

**Endpoint:** `POST /predict`

**Input JSON example:**
```json
{
  "total_spend": 350.50,
  "avg_order_value": 87.62,
  "total_items": 45,
  "total_transactions": 4,
  "unique_products": 12,
  "days_between_first_and_last_purchase": 30,
  "purchase_frequency": 0.13,
  "avg_items_per_order": 11.25,
  "country": "United Kingdom",
  "has_returned_items": 0
}
```

**Output JSON example:**
```json
{
  "prediction": "Repeat Buyer",
  "probability": 0.82
}
```

The API will load the best model from `models/best_model.pkl`. It will also load the scaler from `models/scaler.pkl`. When a request comes in, the API will apply the same preprocessing (scaling and encoding) that was used during training, then pass the data to the model and return the prediction. Note: the input represents a customer's activity within their first 90-day observation window, matching how the model was trained.

## 8. Repository Plan

```
customer-repeat-prediction-api/
├── dataset/
│   └── online_retail_II.csv        # raw data downloaded from Kaggle
├── src/
│   ├── preprocess.py               # cleaning, time-cutoff feature/label creation, encoding, scaling, train/test split
│   └── train.py                    # train all models, print comparison table, save best model
├── api/
│   └── app.py                      # FastAPI app with POST /predict endpoint
├── models/
│   ├── best_model.pkl              # the winning model (saved after training)
│   └── scaler.pkl                  # the fitted scaler (needed at prediction time)
├── notebooks/
│   └── exploration.ipynb           # optional: early data exploration
├── README.md                       # how to set up and run the project
├── requirements.txt                # all Python packages needed
└── project_paper.md                # 3-5 page report about the project
```

**Run commands:**
```bash
python src/train.py                  # trains all models, prints results, saves the best one
uvicorn api.app:app --reload         # starts the API server locally
```
