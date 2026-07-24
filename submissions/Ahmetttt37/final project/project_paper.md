# Customer Personality Analysis - Machine Learning Project Paper

## GitHub Repository

The complete project code, preprocessing scripts, trained models, and API deployment files are available on GitHub:

## git hup link
https://github.com/Ahmetttt37/customer-personality-analysis.git

---

# 1. Introduction

Customer behavior analysis is an important task for businesses because understanding customer preferences helps improve marketing decisions and increase campaign success.

In this project, machine learning techniques were applied to analyze customer personality and purchasing behavior using a marketing campaign dataset.

The main objectives of this project are:

1. Predict whether a customer will respond positively to a marketing campaign.
2. Identify different customer groups based on their purchasing patterns.

The project combines supervised learning and unsupervised learning approaches.

Supervised learning models are used for customer response prediction, while K-Means clustering is used for customer segmentation.

---

# 2. Dataset Description

The dataset used in this project is the **Marketing Campaign Dataset**.

The dataset contains customer demographic information, purchasing behavior, and previous marketing campaign responses.

Main features include:

## Customer Information

* Age
* Income
* Education
* Marital Status
* Number of children

## Purchase Information

* Wine spending
* Fruit spending
* Meat product spending
* Fish product spending
* Sweet product spending
* Gold product spending

## Purchase Channels

* Web purchases
* Catalog purchases
* Store purchases

## Campaign Information

* Previous campaign responses
* Customer response

Target variable:

```
Response
```

Values:

* 0 → Customer did not accept the campaign
* 1 → Customer accepted the campaign

---

# 3. Data Preprocessing

Before applying machine learning algorithms, the dataset was cleaned and prepared.

The following preprocessing steps were performed:

## Missing Value Handling

The Income feature contained missing values. These missing values were replaced using the median value to maintain data consistency.

---

## Date Processing

The customer registration date was converted into datetime format.

A new feature called:

```
Customer_Years
```

was created to represent how long each customer has been registered.

---

## Feature Engineering

New features were created to improve model performance:

### Age

Customer age was calculated using birth year information.

### Children

The total number of children was calculated:

```
Children = Kidhome + Teenhome
```

### Total Spending

A new feature was created by combining spending categories:

```
TotalSpent =
Wines + Fruits + Meat + Fish + Sweet + Gold
```

### Total Purchases

Purchase channels were combined:

```
TotalPurchases =
Web Purchases + Catalog Purchases + Store Purchases
```

### Total Accepted Campaigns

Previous campaign responses were combined into one feature.

---

## Categorical Data Processing

Categorical features such as:

* Education
* Marital Status

were transformed using One-Hot Encoding.

---

## Removing Unnecessary Features

The following unnecessary columns were removed:

* ID
* Year_Birth
* Z_CostContact
* Z_Revenue

---

## Feature Scaling

StandardScaler was applied to numerical features.

Scaling helps machine learning algorithms perform better by putting features into a similar range.

---

# 4. Machine Learning Approach

This project used three supervised learning algorithms:

---

## Logistic Regression

Logistic Regression was used as a baseline classification model.

It predicts whether a customer accepts the marketing campaign based on customer features.

---

## Random Forest Classifier

Random Forest is an ensemble learning algorithm that combines multiple decision trees.

It improves prediction stability and reduces overfitting.

---

## XGBoost Classifier

XGBoost is a gradient boosting algorithm designed for high-performance prediction on structured datasets.

It was included because it often performs well on customer behavior datasets.

---

# 5. Customer Segmentation Approach

For unsupervised learning, K-Means clustering was applied.

The clustering model used six customer spending features:

* MntWines
* MntFruits
* MntMeatProducts
* MntFishProducts
* MntSweetProducts
* MntGoldProds

The goal was to discover groups of customers with similar purchasing behaviors.

The optimal clustering process identified four customer segments.

---

# 6. Model Comparison

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

Results:

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 89.06%   |
| Random Forest       | 89.06%   |
| XGBoost             | 89.51%   |

---

## Logistic Regression Results

Accuracy:

```
89.06%
```

The model performed well in identifying customers who do not accept campaigns.

However, recall for positive customers was lower.

---

## Random Forest Results

Accuracy:

```
89.06%
```

Random Forest achieved similar accuracy but lower recall for customers who accepted campaigns.

---

## XGBoost Results

Accuracy:

```
89.51%
```

XGBoost achieved the best overall performance.

It provided better detection of positive customer responses compared with the other models.

Therefore, XGBoost was selected as the final classification model.

---

# 7. Customer Segmentation Analysis

K-Means clustering was used to divide customers into four different groups based on spending behavior.

---

## Cluster 0: Low Spending Customers

Number of customers:

```
1258
```

Characteristics:

* Low spending in all product categories.
* Limited purchasing activity.

Recommendation:

* Provide discounts.
* Send personalized recommendations.
* Encourage first-time purchases.

---

## Cluster 1: Wine and Meat Customers

Number of customers:

```
375
```

Characteristics:

* High spending on wine products.
* High spending on meat products.

Recommendation:

* Create product bundles.
* Offer loyalty rewards.
* Promote premium food and wine packages.

---

## Cluster 2: Wine and Gold Product Customers

Number of customers:

```
360
```

Characteristics:

* High wine purchases.
* Higher interest in gold products.

Recommendation:

* Provide luxury product recommendations.
* Create exclusive offers.

---

## Cluster 3: Premium Multi-Category Customers

Number of customers:

```
247
```

Characteristics:

* High spending across multiple categories.
* Highest customer value.

Recommendation:

* Create VIP membership programs.
* Provide personalized marketing campaigns.
* Reward customer loyalty.

---

# 8. Model Deployment Using FastAPI

The trained machine learning models were deployed using FastAPI.

Two API endpoints were created:

## Customer Segmentation API

Endpoint:

```
POST /segment
```

Purpose:

* Predict customer cluster based on purchasing behavior.

---

## Customer Response Prediction API

Endpoint:

```
POST /predict
```

Purpose:

* Predict whether a customer will accept a marketing campaign.

The trained models were saved using Joblib:

```
models/xgboost.pkl
models/kmeans.pkl
models/scaler.pkl
models/cluster_scaler.pkl
```

---

# 9. Tools and Technologies Used

Programming Language:

* Python

Libraries:

* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Joblib

Machine Learning Algorithms:

* Logistic Regression
* Random Forest
* XGBoost
* K-Means Clustering

Deployment:

* FastAPI
* Uvicorn

Development Tools:

* Jupyter Notebook
* VS Code
* GitHub

---

# 10. Project Structure

```
Customer Personality Analysis/

│
├── dataset/
│   ├── marketing_campaign.csv
│   ├── processed_features.csv
│   └── target.csv
│
├── models/
│   ├── xgboost.pkl
│   ├── random_forest.pkl
│   ├── logistic_regression.pkl
│   ├── kmeans.pkl
│   ├── scaler.pkl
│   └── cluster_scaler.pkl
│
├── api/
│   └── app.py
│
├── notebooks/
│
├── README.md
└── requirements.txt
```

---

# 11. Limitations and Future Improvements

Although the project achieved good results, there are some possible improvements:

* Test additional machine learning algorithms.
* Perform hyperparameter tuning.
* Improve class imbalance handling.
* Create a web dashboard for customer analysis.
* Deploy the API online using cloud services.

---

# 12. Conclusion

This project successfully applied machine learning techniques to understand customer behavior and improve marketing decisions.

Supervised learning models were used to predict customer campaign responses, while K-Means clustering identified different customer groups based on purchasing behavior.

Among the classification models, XGBoost achieved the highest accuracy and provided the best overall performance.

The customer segmentation results provide valuable insights that businesses can use to create targeted marketing strategies and improve customer relationships.

This project demonstrates how machine learning can support data-driven decision making in customer analytics.
