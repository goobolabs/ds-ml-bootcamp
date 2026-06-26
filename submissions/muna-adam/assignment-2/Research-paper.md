# Cryptocurrency Price Observation Dataset: 

## Collection Method

This dataset was created to analyze and predict the market trend of cryptocurrencies. The data was collected from cryptocurrency market platforms such as CoinMarketCap and TradingView by observing the top cryptocurrencies based on market capitalization.

For each cryptocurrency, important market indicators were recorded, including trading volume, RSI (Relative Strength Index), chart trend, 24-hour price change percentage, and market capitalization. Based on these indicators, a trend label (Up or Down) was assigned.

The dataset contains observations from 50 cryptocurrencies and is intended for Machine Learning classification tasks.

## Description of Features and Label

In Machine Learning, the input variables are called features (X) and the output variable is called the label (y).

Features (X)

| Feature              | Description                                                      |
|----------------------|------------------------------------------------------------------|
| Volume              | Total trading volume of the cryptocurrency.                      |
| RSI                 | Relative Strength Index, measuring market momentum.              |
| Chart Trend         | Market direction observed from the chart (Bullish, Bearish, Sideway). |
| 24h Price Change %  | Percentage change in price over the last 24 hours.               |
| Market Cap          | Total market value of the cryptocurrency.                        |

Label (y)


| Label | Description |
|-------|-------------|
| Trend | Final market direction (Up or Down). |

The goal of the model is to use the features to predict whether the cryptocurrency trend will move Up or Down.

## Dataset Structure

The dataset contains:

•	Rows: 50
•	Columns: 6
•	Features: 5
•	Label: 1

### Sample Dataset

| Volume | RSI | Chart Trend | 24h Price Change % | Market Cap | Trend |
|--------|----:|-------------|-------------------:|-----------:|-------|
| 25.53B | 33 | Bearish | -2.30% | 1.25T | Down |
| 11.7B | 32 | Bearish | -3.04% | 203.74B | Down |
| 1.08B | 53 | Bullish | -7.14% | 16.87B | Up |
| 570M | 60 | Bullish | -4.00% | 2.06B | Up |
| 29.6M | 55 | Bullish | +15.10% | 1.39B | Up |
| 48.28M | 42 | Bearish | -0.30% | 885M | Down |

##  Quality Issues
Several data quality issues were identified in the dataset:

### Missing Values
Some rows have missing values in the Trend column, especially where the Chart Trend is recorded as "Sideway."

### Class Imbalance
Most records belong to the "Down" class, while fewer records belong to the "Up" class. This may cause the model to favor predicting the majority class.

### Inconsistent Formats
Volume and Market Cap values use different units such as M (Million), B (Billion), and T (Trillion). These values would need preprocessing before training a model.

### Limited Dataset Size
The dataset contains only 50 samples, which may not be sufficient for building a highly accurate Machine Learning model.

## Learning Type

This dataset represents a Supervised Learning problem.
The reason is that the dataset contains a clear label (y), which is the Trend column.

The Machine Learning model learns from historical examples where both the features and the correct trend label are already known.

#### Features (X)
•	Volume
•	RSI
•	Chart Trend
•	24h Price Change %
•	Market Cap

#### Label (y)
•	Trend (Up or Down)

Because the correct output is already provided during training, the problem is classified as supervised learning.

## 6. Use Case and Data Science Lifecycle
Machine Learning Use Case
This dataset can be used for a Classification problem because the target variable contains categories:
•	Up
•	Down

The model would learn patterns from market indicators and predict the future direction of cryptocurrency prices.
Possible algorithms include:
•	Logistic Regression
•	Decision Tree
•	Random Forest
•	Support Vector Machine (SVM)

## Data Science Lifecycle
This dataset fits several stages of the Data Science Lifecycle:

1.	Data Collection
o	Gathering cryptocurrency market information.
2.	Data Preparation
o	Cleaning missing values and converting units.
3.	Exploratory Data Analysis
o	Studying relationships between RSI, Volume, and Trend.
4.	Model Building
o	Training a classification model.
5.	Evaluation
o	Measuring prediction accuracy.
6.	Deployment
o	Using the model to support cryptocurrency trading decisions.

## Conclusion

The Cryptocurrency Price Observation Dataset was created to study cryptocurrency market behavior and predict future trends. The dataset contains 50 observations and includes five important features: Volume, RSI, Chart Trend, 24h Price Change Percentage, and Market Capitalization. Since the dataset contains a clear target variable (Trend), it is suitable for supervised learning classification tasks. After preprocessing and cleaning, the dataset can be used to train Machine Learning models that help investors and traders make better decisions in cryptocurrency markets.

