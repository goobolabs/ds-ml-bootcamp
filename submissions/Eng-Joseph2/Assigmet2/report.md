# Market Sales Prediction Dataset (Local Business Analytics)

# name: Abdiqani Yacqub Hassan

## 1. Title & Collection Method

This dataset represents daily sales performance of a small local market stall.

It was created using simulated real-world business conditions such as temperature, customer flow, pricing, and promotions.

The goal is to understand how environmental and business factors affect daily sales.

---

## 2. Features & Label Description

### Features (X):

- Day: Day number in observation period
- TemperatureC: Daily temperature in Celsius
- FootTraffic: Number of customers visiting the market
- PriceIndex: Relative price level of goods
- Promotion: Whether a discount/promotion is active (1 = yes, 0 = no)
- CompetitorsNearby: Number of nearby competing stalls

### Label (Y):

- DailySales: Total sales made per day

---

## 3. Dataset Structure

- Rows: 50
- Columns: 7

### Sample Data (First 5 Rows)

| Day | Temp | FootTraffic | PriceIndex | Promo | Competitors | Sales |
| --- | ---- | ----------- | ---------- | ----- | ----------- | ----- |
| 1   | 30   | 120         | 1.0        | 1     | 2           | 85    |
| 2   | 31   | 130         | 1.1        | 1     | 2           | 90    |
| 3   | 29   | 110         | 1.0        | 0     | 3           | 70    |
| 4   | 28   | 100         | 1.2        | 0     | 4           | 65    |
| 5   | 32   | 140         | 1.0        | 1     | 2           | 95    |

---

## 4. Data Quality Issues

This dataset may include real-world challenges such as:

- Possible missing values in future data collection
- Noise in customer counts (human estimation errors)
- Outliers during special events or holidays
- Seasonal patterns affecting sales
- Correlation between features (multicollinearity)

These issues will be handled in preprocessing steps such as cleaning, scaling, and feature selection.

---

## 5. Type of Machine Learning Problem

This is a **Supervised Learning** problem because:

- The dataset contains a target variable (DailySales)
- The model learns relationships between inputs and outputs

### Task Type:

- Regression (predicting continuous numeric values)

📌 Reference:
https://scikit-learn.org/stable/supervised_learning.html

---

## 6. Use Case & Data Science Lifecycle

### Use Case:

- Predict daily market sales
- Improve pricing strategies
- Optimize promotions and staffing
- Analyze customer behavior patterns

### Data Science Lifecycle Stage:

This dataset fits into:

1. Problem Definition – understanding sales performance
2. Data Collection – manual/simulated business data
3. Data Cleaning – handling missing/noisy data
4. Modeling – training regression models
5. Evaluation – measuring prediction accuracy
6. Deployment – using model for business decisions

📌 Reference:
https://www.ibm.com/topics/data-science

---

## Conclusion

This dataset provides a practical foundation for learning regression in machine learning. It connects real-world business analytics with core data science concepts such as feature engineering, supervised learning, and predictive modeling.
