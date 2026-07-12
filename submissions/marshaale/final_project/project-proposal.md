## 1. Certificate Name

**Muktar Ahmed Mohamed**

---

## 2. Project Title and Description

**Title:** Olympic Medals Prediction and Country Strength Classification

---

A Multi modal machine learning predicting how many medals a country will win and classifies it's strength using historical data.

The benefits is predicting medals winners and favorite candidates.

## 3. Problem Type

**Regression** — Continues numbers output: how many medals a country will win.

**Clustering** — Clustering will be used to automatically discover country strength level groups (Optional).

**Classification** — Multi class output: country strength example top level (favorite to win most medals),middle,low level (underdogs).

For regression the target column is `total_medals`. This is supervised learning: we train on historical olympic where the outcome is already known.

For classification the target column is `country_strength`. This is supervised learning: we train on historical olympic where the outcome is already known.

For team country_strength grouping i will use clustering or i will hard code it. So clustering wil be optional

---

## 4. Dataset

- **Source:** [120 years of Olympic history: athletes and results](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results?select=athlete_events.csv) (basic bio data on athletes and medal results from Athens 1896 to Rio 2016).
- **Size:** ~271116 rows, 15 columns.

The dataset has one athlete result per row. so the features will be engineered from.

- ID - Unique number for each athlete
- Name - Athlete's name
- Sex - M or F
- Age - Integer
- Height - In centimeters
- Weight - In kilograms
- Team - Team name
- NOC - National Olympic Committee 3-letter code
- Games - Year and season
- Year - Integer
- Season - Summer or Winter
- City - Host city
- Sport - Sport
- Event - Event
- Medal - Gold, Silver, Bronze, or NA

- **Target:** `total_medals` and `country_strength`.

Expected features after engineering

- **Main features:**
  - `athletes` — number of athletes to participate
  - `athletes_female_percentage` — Percentage of female athletes
  - `prev_medals` — number of previous/last year medals win.
  - `avg_age` — avg age for athletes
  - `agv_height` — avg height for athletes
  - `avg_weight` — avg weight for athletes
  - `prev_gold_medals` — number of gold medals win.
  - `sports` — how many different sports the country participates in.
  - `events` — how many individual events the country enters.
  - `season` — summer or winter will be categorical binary encoding

**Preprocessing plan:** standardize features,impute missing values,feature engineering,outlier handling,scale numeric features, stratified train/test split (80/20).

---

## 5. Algorithms I Plan to Train

| #   | Algorithm                       | Why it fits                                                                               |
| --- | ------------------------------- | ----------------------------------------------------------------------------------------- |
| 1   | **Logistic Regression**         | Bootcamp baseline for binary classification; fast, interpretable coefficients.            |
| 2   | **Random Forest**               | Bootcamp ensemble reduces overfitting vs a single tree, handles mixed feature types well. |
| 3   | **Linear Regression**           | Bootcamp baseline for continues numbers; fast,simple.                                     |
| 4   | **Gradient Boosting (sklearn)** | Strong on structured/tabular data good candidate for best model.                          |
| 5   | **Kmeans**                      | Bootcamp baseline for clustering                                                          |

---

## 6. Evaluation Plan

**Metrics for all models:**

**Classification** → Accuracy, Precision, Recall, F1; Pick best by F1 because it combines precision and recall.

**Regression** → MAE, RMSE, R²; Pick best by highest R² and lowest MAE/RMSE because higher R² means better fit, while lower MAE/RMSE means lower prediction error.

**Clustering** → Silhouette, Davies–Bouldin; Pick best by highest Silhouette and low Davies–Bouldin tells how compact clusters.

**Best-model rule:** Rank all models in each case regression,classification choose the best and save it.

---

## 7. Deployment Sketch

- **Framework:** FastAPI (simple, modern, auto-generates API docs at `/docs`).
- **Endpoint:** `POST /predict`
- **Input JSON example:**

```json
{
  "athletes": 50,
  "sports": 8,
  "agv_height": 185,
  "athletes_female_percentage": 30,
  "avg_age": 21,
  "avg_weight": 75,
  "prev_medals": 120,
  "prev_gold_medals": 30,
  "events": 28,
  "season": "summer"
}
```

- **Output JSON example:**

```json
{
  "medals": 110,
  "country_strength": "Top level"
}
```

---

## 8. Repository Plan

```
olympic_medals/
├── dataset/
│   └── athlete_events.csv
│   └── *.csv # all others
├── notebooks/
│   ├── preprocess.ipynb      # cleaning, encoding, scaling, train/test split
│   └── regression.ipynb           # train all models, compare, save best
│   └── clustring.ipynb           # train all models, compare, save best. optional
│   └── classification.ipynb           # train all models, compare, save best
├── api/
│   └── app.py             # FastAPI app with /predict
├── models/
│   ├── regression_model.joblib
│   └── clarification_model.joblib
├── helpers/
│   └── *.py  # for helpers methods and classes
├── docs/
│   └── *.md  # docs during implementations
├── frontend/ # Optional
│   └── index.html
│   └── style.css
│   └── script.js
├── README.md
├── requirements.txt
```

## References

[Kaggle Dataset](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results)

[Youtube](https://www.youtube.com/watch?v=Hr06nSA-qww)

[Github](https://github.com/dataquestio/project-walkthroughs/tree/master/beginner_ml)
