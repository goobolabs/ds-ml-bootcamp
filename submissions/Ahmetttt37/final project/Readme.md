# Customer Personality Analysis - Machine Learning Project

## Project Title

**Customer Personality Analysis: Customer Response Prediction and Customer Segmentation Using Machine Learning**

---

# Problem Statement

Businesses collect large amounts of customer data but often struggle to understand customer behavior and identify customers who are most likely to respond to marketing campaigns.

The goal of this project is to build a machine learning solution that can:

1. Predict whether a customer will accept a marketing campaign offer.
2. Segment customers into different groups based on their purchasing behavior.

This helps businesses create targeted marketing strategies, improve customer engagement, and increase campaign effectiveness.

---

# Dataset Description

The dataset used in this project is the **Marketing Campaign Dataset**.

It contains customer demographic information, purchasing behavior, and campaign response data.

Main features include:

## Customer Information
- Age
- Income
- Education
- Marital Status
- Number of children

## Purchase Information
- Wines spending
- Fruits spending
- Meat products spending
- Fish products spending
- Sweet products spending
- Gold products spending

## Purchase Channels
- Web purchases
- Catalog purchases
- Store purchases

## Campaign Information
- Previous campaign responses
- Response (target variable)

Target variable:

```
Response
```

Values:

- 0 → Customer did not accept the campaign offer
- 1 → Customer accepted the campaign offer

---

# Data Cleaning and Preprocessing Steps

The following preprocessing steps were applied:

## 1. Missing Value Handling

- Missing values in the Income column were replaced using the median value.

## 2. Date Processing

The customer registration date was converted into datetime format.

A new feature was created:

```
Customer_Years
```

This represents how long the customer has been registered.

## 3. Feature Engineering

New features were created:

- Age
- Children
- TotalSpent
- TotalPurchases
- TotalAcceptedCampaigns

Examples:

```
TotalSpent =
MntWines + MntFruits + MntMeatProducts +
MntFishProducts + MntSweetProducts + MntGoldProds
```

```
TotalPurchases =
NumWebPurchases +
NumCatalogPurchases +
NumStorePurchases
```

## 4. Categorical Data Processing

Categorical columns were converted using One-Hot Encoding.

Processed columns:

- Education
- Marital Status

## 5. Removing Unnecessary Columns

The following columns were removed:

- ID
- Year_Birth
- Z_CostContact
- Z_Revenue

## 6. Feature Scaling

StandardScaler was applied to numerical features to normalize the data before training machine learning models.

---

# Machine Learning Models Used

Three supervised learning algorithms were trained and compared:

## 1. Logistic Regression

A baseline classification algorithm used to predict customer campaign response.

## 2. Random Forest Classifier

An ensemble machine learning algorithm that combines multiple decision trees to improve prediction performance.

## 3. XGBoost Classifier

A gradient boosting algorithm that provides strong performance on structured datasets.

---

# Model Results

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

| Model | Accuracy |
|---|---|
| Logistic Regression | 89.06% |
| Random Forest | 89.06% |
| XGBoost | 89.51% |

## Best Model

**XGBoost achieved the best performance.**

Results:

```
Accuracy: 89.51%

Precision (Class 1): 0.71
Recall (Class 1): 0.51
F1-score (Class 1): 0.59
```

XGBoost was selected as the strongest model because it achieved the highest accuracy and better prediction ability for customers who accepted the campaign.

---

# Customer Segmentation Using K-Means

Unsupervised learning was performed using K-Means clustering.

The following spending features were used:

- MntWines
- MntFruits
- MntMeatProducts
- MntFishProducts
- MntSweetProducts
- MntGoldProds

The analysis identified **4 customer segments**.

---

# Customer Segments

## Cluster 0 - Low Spending Customers

Number of customers:

```
1258
```

Characteristics:

- Low spending across all product categories.
- Less engagement with products.

Business Recommendation:

- Provide discounts, promotions, and personalized recommendations to increase purchases.

---

## Cluster 1 - Wine and Meat High Value Customers

Number of customers:

```
375
```

Characteristics:

- High spending on wines.
- High spending on meat products.

Business Recommendation:

- Provide premium packages, loyalty rewards, and exclusive offers.

---

## Cluster 2 - Wine and Gold Product Customers

Number of customers:

```
360
```

Characteristics:

- Strong preference for wine products.
- Higher spending on gold products.

Business Recommendation:

- Promote luxury products and special bundle offers.

---

## Cluster 3 - Premium Multi-Category Customers

Number of customers:

```
247
```

Characteristics:

- High spending across many product categories.
- Most valuable customer group.

Business Recommendation:

- Create VIP membership programs and personalized marketing campaigns.

---

# Conclusion

This project successfully combined supervised and unsupervised machine learning techniques.

Supervised models were used to predict customer campaign responses, while K-Means clustering was used to discover different customer groups based on purchasing behavior.

The results show that machine learning can help businesses understand customers better, improve marketing strategies, and increase campaign success.