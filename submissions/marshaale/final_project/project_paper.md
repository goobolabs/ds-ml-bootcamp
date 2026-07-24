## Problem statement and motivation

**Goal:** Predict the number of Olympic medals a country will win and identify potential medal-winning countries before the Olympic Games.

**Motivation:** A fun sports analytics project that applies machine learning to analyze historical Olympic performance and forecast future medal outcomes for participating countries.

## Dataset and preprocessing

- **Source:** [120 years of Olympic history: athletes and results](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results?select=athlete_events.csv) (basic bio data on athletes and medal results from Athens 1896 to Rio 2016).
- **Size:** ~271116 rows, 15 columns.

Implemented two step data processing first step pre-clean simple handling age,height,weight missing value then feature extraction based year and season olympic event.

List of features

```py
features_cols = [
  "noc",
  "season",
  "year",
  "athletes",
  "athletes_female_percentage",
  "avg_age",
  "agv_height",
  "avg_weight",
  "prev_medals",
  "prev_gold_medals",
  "sports",
  "events",
  "total_medals",
];
```

Second step clean-dataset handling missing models replace 0 because NA models equal to zero.
encoding categorical season feature with label/binary encoding.
tried iqr capping(handling outlier) and skipped due to medal features massive outliers.then inspect and save.

For scaling i will use RobustScaler which is good for handling massive outliers effectively.

## Algorithms

### Clustering

- Kmeans
- AgglomerativeClustering

`Why` Simple, fast, and widely used algorithms.

### Classification

- Logistic Regression
- Xgboost
- Random Forest

`Why` LR Best for simple linear relationships, Xgboost best for large tabular dataset, Random Forest best for nonlinear relationships

### Regression

- Linear Regression
- Xgboost
- Random Forest

`Why` LR Best for simple linear relationships,Xgboost best for large tabular dataset, Random Forest best for nonlinear relationships

## Results and discussion

### Classification

```
XGboost Performance:
  Accuracy : 0.969
  Precision: 0.736
  Recall   : 0.739
  F1-Score : 0.734

Random forest Performance:
  Accuracy : 0.964
  Precision: 0.723
  Recall   : 0.805
  F1-Score : 0.759

Logistic regression Performance:
  Accuracy : 0.915
  Precision: 0.577
  Recall   : 0.785
  F1-Score : 0.618
```

This concise how model learns the different classes.

```
XGB
              precision    recall  f1-score   support

           0       1.00      0.98      0.99       690
           1       0.78      0.90      0.84        69
           2       0.43      0.33      0.38         9

    accuracy                           0.97       768
   macro avg       0.74      0.74      0.73       768
weighted avg       0.97      0.97      0.97       768
```

```
RF
              precision    recall  f1-score   support

           0       1.00      0.98      0.99       690
           1       0.75      0.88      0.81        69
           2       0.42      0.56      0.48         9

    accuracy                           0.96       768
   macro avg       0.72      0.81      0.76       768
weighted avg       0.97      0.96      0.97       768
```

```
LR
              precision    recall  f1-score   support

           0       0.90      0.87      0.88       690
           1       0.11      0.10      0.10        69
           2       0.00      0.00      0.00         9

    accuracy                           0.79       768
   macro avg       0.34      0.32      0.33       768
weighted avg       0.82      0.79      0.80       768

```

#### Sanity Checks

```py
data = pd.DataFrame([{
    'athletes':24,
    'avg_age':24.0,
    'agv_height':172.0,
    'avg_weight':73.0,
    'prev_medals':19,
    'sports':19,'events':32,
},
{
    'athletes':28,
    'avg_age':22.0,
    'agv_height':172.0,
    'avg_weight':76.0,
    'prev_medals':15,
    'sports':11,'events':23,
},
{
    'athletes':32,
    'avg_age':28.0,
    'agv_height':172.0,
    'avg_weight':76.0,
    'prev_medals':26,
    'sports':17,'events':30,
}],index=[0,1,2])
```

**XGB** Predictions [1,1,1]

**RF** Predictions [1,1,1]

The best model is random forest learns minority classes better than xgboost and higher f1 score.

### Regression

```
LinearRegression Performance:
  R²   : 0.783
  MAE  : 3
  MSE  : 55
  RMSE : 7

Xgboost Performance:
  R²   : 0.860
  MAE  : 2
  MSE  : 35
  RMSE : 6

RandomForest Performance:
  R²   : 0.833
  MAE  : 2
  MSE  : 42
  RMSE : 6
```

#### Sanity Checks

```py
data = pd.DataFrame([{
    'season':0,
    'year':2000,
    'athletes':24,
    'avg_age':24.0,
    'agv_height':172.0,
    'avg_weight':73.0,
    'prev_medals':19,
    'prev_gold_medals':8,
    'sports':19,'events':32,
},
{
    'season':1,
    'year':2004,
    'athletes':24,
    'avg_age':24.0,
    'agv_height':172.0,
    'avg_weight':73.0,
    'prev_medals':19,
    'prev_gold_medals':8,
    'sports':19,'events':32,
},
{
    'season':0,
    'year':2008,
    'athletes':32,
    'avg_age':24.0,
    'agv_height':172.0,
    'avg_weight':73.0,
    'prev_medals':22,
    'prev_gold_medals':12,
    'sports':22,'events':36,
}],index=[0,1,2])
```

**XGB** Medals [15.802446 13.714566 15.951689]

**LR** Medals [0.58053159 0.72516295 4.82904523]

**RF** Medals [13.88478169 13.26434861 17.36645122]

The best model is xgboost has higher r2 and low mae,mse and rmse.

## Deployment notes

### Request

```bash
curl -X POST 'https://dsml.sotechho.com/api/v1/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "season": "summer",
    "year": 2024,
    "athletes": 120,
    "avg_age": 25.5,
    "avg_height": 178,
    "avg_weight": 74,
    "prev_medals": 10,
    "prev_gold_medals": 3,
    "sports": 15,
    "events": 40
  }'
```

### Response

```json
{
  "medals": 8,
  "country_strength": "Emerging Nation 🥉"
}
```

### Frontend

Created simple frontend using html,css,js, The frontend has input panel and result panel with error handling

> Deployed the api and frontend in digital ocean vps. Live site (https://dsml.sotechho.com/)

## Lessons learned

Lessons i learned during this project the `data preparation` i tried different steps and still missing something.

Massive outliers between medals and athletes.

- what you would improve: The dataset improvement is what needs to improve and clustering
- key takeaways: trying what i learned and implement based on my decisions.
