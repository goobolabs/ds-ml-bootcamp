# Predicting Annual Climate Condition: Rainy Year vs. Drought Year
*A Self-Collected Dataset for Seasonal Climate Classification*

## 1. Title and Collection Method

This dataset, **"Annual Climate Condition Dataset (Rainy vs. Drought Year),"** investigates whether a year's local climate indicators can be used to predict whether the year will trend toward being a **rainy year** or a **drought year**. The guiding question: can rainfall, temperature, humidity, rainy-day frequency, and soil moisture observed over time signal which way a season is heading?

Data was collected through **manual field observation and local weather-station logging**. Each record represents one observation period (e.g., a month or recurring interval) for which rainfall total, average temperature, humidity, the number of rainy days, and a soil-moisture estimate were recorded by hand, alongside an overall classification of that period as "Rainy" or "Drought" based on local conditions and farmer/community reports. Because entries were logged manually over time, the raw file carries the small inconsistencies typical of field data collection (see Section 4).

A total of **50 records** were collected, each assigned a unique identifier (R001–R049, plus one duplicate).

## 2. Description of Features and Labels

The dataset has **five input features (X)** and **one output label (y)**.

**Features (X):**
- **Rainfall Amount (mm)** — numeric, total rainfall recorded for the period
- **Average Temperature (°C)** — numeric, mean temperature for the period
- **Humidity (%)** — numeric, average relative humidity
- **Rainy Days Count** — numeric (integer), number of days with measurable rain in the period
- **Soil Moisture Level** — categorical (Low/Medium/High), field-estimated ground moisture

**Label (y):**
- **Climate Condition** — categorical (Rainy / Drought), the overall classification of the period, the value the model is intended to predict

## 3. Dataset Structure

The dataset contains **50 rows** (one per observed period) and **7 columns** (1 ID column, 5 features, 1 label).

| RecordID | RainfallAmount_mm | AvgTemperature_C | Humidity_percent | RainyDaysCount | SoilMoistureLevel | ClimateCondition |
|---|---|---|---|---|---|---|
| R013 | 99.1 | 22.3 | 71 | 13 | Medium | Rainy |
| R018 | 61.3 | 25.4 | 61 | 8 | Low | Drought |
| R023 | 48.6 | 27.9 | 48 | 0 | High | Drought |
| R047 | 103.2 | 22.9 | 59 | 20 | High | Rainy |
| R007 | 55.1 | 26.0 | 71 | 4 | High | Drought |
| R012 | 62.6 | 26.0 | 55 | *(missing)* | High | Drought |
| R004 | 147.7 | 22.0 | 82 | 17 | High | *(missing)* |
| R039 | 121.1 | 24.5 | 74 | 13 | Medium | Rainy |
| R011 | 132.1 | 19.2 | 52 | 15 | Medium | Rainy |
| R032 | 149.5 | 24.3 | 66 | 17 | High | Rainy |

*(Full 50-row dataset provided in the companion file `climate_dataset.md`.)*

## 4. Quality Issues

Because the data was logged manually across multiple observation periods, it carries the imperfections typical of real-world field data, left in place for the preprocessing stage:

- **Missing values** — scattered blanks across several columns (3 missing in Humidity, 1 in Rainy Days Count, 1 in Soil Moisture Level, 2 in Climate Condition), likely from incomplete field readings.
- **Inconsistent categorical formatting** — the "Soil Moisture Level" column appears in over a dozen text variants of the same three categories (e.g., "Medium", "Med", "MEDIUM", "medium"; "High", "HIGH", "High "), and the label itself varies in casing ("Rainy" vs. "rainy" vs. "RAINY"; "Drought" vs. "drought" vs. "Drought "), all needing standardization before encoding.
- **Typing errors** — one Rainy Days Count value was entered as "12,5" using a comma instead of a plain integer, likely a decimal-separator slip.
- **Outliers / out-of-range values** — an average temperature of 70.0°C (implausible, likely a misplaced digit), a rainfall reading of 999.0 mm (far above any realistic monthly total, likely a placeholder/error value), and a humidity reading of 130% (impossible, since humidity is capped at 100%) — all signs of entry mistakes.
- **Duplicate record** — Record R007 appears twice with identical values, likely a double log entry.
- **Class imbalance** — once labels are normalized, "Drought" periods substantially outnumber "Rainy" periods (roughly 3:1 in this sample), which is worth accounting for during model training (e.g., via class weighting or resampling).

None of these issues were corrected here; they are flagged deliberately so they can be addressed using the cleaning, encoding, and scaling techniques from Lesson 3.

## 5. Learning Type

This is a **supervised learning** problem. Every row has a known, explicit output — Climate Condition — paired with input features describing that period's weather. Since the goal is to learn a mapping from known inputs (rainfall, temperature, humidity, rainy days, soil moisture) to a known, categorical output (Rainy or Drought), the data has the labeled X → y structure that defines supervised learning, unlike unsupervised learning, where no target variable exists and the goal is instead to discover hidden structure or natural groupings in the data.

## 6. Use Case

Because Climate Condition is a categorical label with two classes, the most natural ML application is **classification** — e.g., training a logistic regression, decision tree, or random forest classifier to predict whether a given period will be "Rainy" or "Drought" based on its climate indicators. The same underlying numeric features (rainfall, temperature, humidity, rainy days) could also support a **regression** framing if the goal shifted to predicting a continuous quantity, such as total expected rainfall. As a secondary, unsupervised use case, dropping the label and **clustering** periods by their climate indicators alone could reveal natural climate "regimes" (e.g., hot-dry vs. humid-wet clusters) without reference to the Rainy/Drought outcome.

Within the **data science lifecycle**, this dataset currently sits at the end of data collection and the start of data preparation. The next steps — cleaning missing values, standardizing the Soil Moisture and label categories, correcting outliers, removing the duplicate, and encoding/scaling features — correspond to the preprocessing stage (Lesson 3). After preprocessing, the dataset would move into exploratory analysis and model building (training a classifier to predict Climate Condition), followed by evaluation and, potentially, deployment as an early-warning tool flagging an upcoming drought risk based on current-season readings.

---
*Dataset file: `climate_dataset.md` (50 rows × 7 columns, raw/uncleaned)*
