## 1. Title & Collection Method
> A Framework for Predictive Automotive Valuation

Our dataset focuses on predictive automotive valuation. It is designed to model how a vehicle's secondary market value (price) is influenced by its structural characteristics and usage history. The dataset contains 60 samples and features a multi-variable architecture with 4 independent input features (X) mapping to 1 continuous numeric target (y)

## 2. Description of Feature & Labels

This dataset contains vehicle’s secondary market value.

✓ **Vehicle Model:** Fuses brand and body silhouette (e.g., Toyota SUV, BMW Coupe) to capture manufacturer equity and market tier.\
✓ **Year:** Represents the production year, acting as a chronological metric for absolute depreciation. \
✓ **Mileage:** Measures total distance driven, serving as a proxy for mechanical fatigue and wear.\
✓ **Fuel Type:** Captures the vehicle's powertrain mechanics (Gasoline, Diesel, Hybrid, Electric), reflecting market demands driven by modern fuel economics.\
✓ **Price (Target Label):** The estimated market value of the vehicle in USD.

## 3. Dataset Structure
The dataset consists of exactly 60 rows (samples) and 5 columns (variables).

### Sample Table
Below is a 5-row slice of the raw, uncleaned dataset. It highlights the exact structural layout of the 5 columns alongside the deliberate, real-world data-quality anomalies (such as missing values, shorthand dates, string pollution, and mixed text casing) that must be resolved during preprocessing:

| vehicle_model     | year    | mileage    | fuel_type | price   |
|--------------     |------   |---------   |-----------|------   |
| Ford Electric EV  |  2015   |  154320.0  | electric  | 5000.0  |
| Ford Coupe        | 2021    | 47,269     |  Elec     | 6400.0  |
| BMW Coupe         |  2015   | 87219.0    | Diesel    |  $5000  |
| BMW Electric EV   | '18     | 59203.0    |  electric |13700.0  |
| Hyundai SUV       |  2016   | NaN        | Gasoline  | 5000.0  |


## 4. Quality Issue
A thorough exploratory data analysis (EDA) of the raw dataset reveals five distinct data-quality issues embedded across both the features and the target label. These issues represent common, real-world data collection anomalies that must be structurally resolved during the preprocessing phase before the dataset can be utilized by any machine learning algorithm: 

### a. Missing data values: \
    i. Numerical Features: the mileage column has completely blank entries (represented as NaN). \
    ii. Categorical Features: the fuel type column lacks data points for specific entries \
### b. Mixed formatting and structural clashes (Data type) \
    i.	In the Year column, chronological variables alternate inconsistently between standard 4-digit integers (2020), float syntax with unnecessary decimals (2021.0), and abbreviated text string shorthand’s (such as 18 or 22) \
### c.	String pollution in numerical features \
The mileage column contains text and formatting characters instead of clean integers or floats \

    i.	It includes commas as thousands separators (47, 269), standard string suffixes (120k miles) , and descriptive text placeholders for unknown data (UNKNOWN) \
### d.	Categorical inconsistency
The text columns suffer from poor naming conventions, splitting single logical concepts into multiple redundant groups \

    i.	Fuel type: the concept of a gasoline engine is divided into Gasoline, Gas and gasoline. Similarly, electric propulsion split into Elec and electric. \
    ii.	Vehicle model: text boundaries contain erratic spacing (BMW     Coupe with multiple hidden spaces) and inconsistent case error (lowercase toyota suv) \
### e.	Target variable pollution \
     i.	It mixes raw numerical floats (5000.0) with embedded string currency characters ($19400 or $5000) \
    ii.	Furthermore, some samples have completely missing target labels


## 5. The type of this problem (supervised or unsupervised)
This problem is classified as a **Supervised Learning** problem.

### Justification
a.	Unsupervised Learning deals with unlabeled data; the algorithm is given a collection of features and is tasked with exploring the dataset to find hidden patterns, structures, or natural groupings (such as clustering similar customer profiles together) without any pre-defined correct answers. \
b.	Supervised Learning relies on a structured dataset where every training sample consists of an input pair: a set of predictive features (X) and a corresponding, clearly defined output label (y). The algorithm's objective is to analyze these historical pairs, learn the underlying mathematical relationship between the inputs and outputs, and build a predictive function.

In our vehicle dataset, we have a clear, explicit target label (y): the Price column


## 6. Use Case

### a.	Machine learning applications 
    i. Regressions: this is the primary use case for the dataset because the target variable (price) is a continuous numerical value. Models like Linear Regression or Random Forest Regressors can be trained using features like Year and Mileage to predict the exact market value of a vehicle. This can be used by dealerships for automated trade-in evaluations. \
    ii.	Classification: The dataset can be adapted into a classification problem by transforming the continuous Price column into discrete categories. For example, vehicles can be binned into "Budget" (under $10,000) or "Premium" (above $10,000). Alternatively, a model could predict a binary label like Is_Electric based on the vehicle attributes. \
    iii. Clustering: By completely removing the Price column, unsupervised learning algorithms like K-Means Clustering can look strictly at the independent features (Vehicle_Model, Mileage, Year, Fuel_Type) to find natural groupings in the data. This allows businesses to automatically discover hidden market segments, such as clustering high-mileage commercial trucks separate from commuter hybrids. \

### b.	Placement in the data science lifecycle 
    i.	Data acquisition & understanding: The process begins with generating or loading the raw, uncleaned vehicle CSV file to evaluate its initial structural shape (60 rows, 5 columns) and form baseline hypotheses. \
    ii.	Data Preparation & Preprocessing: This is the most critical phase for this specific dataset. Due to the intentional noise, this step involves stripping text characters (like $ and ,), parsing inconsistent dates, standardizing categorical text naming, and using statistical methods (median/mode) to impute missing NaN values. \
    iii. Modeling & Training: The cleaned dataset is transformed into a mathematical array and split into a Training Set (80%) to teach the regression model depreciation patterns, and a Testing Set (20%) to evaluate performance. \
    iv.	Evaluation: In this final stage, the model’s price predictions on the hidden test set are calculated and verified using metrics such as $R^2$ Score (variance explained) and Mean Absolute Error (MAE) to check accuracy before deployment.





