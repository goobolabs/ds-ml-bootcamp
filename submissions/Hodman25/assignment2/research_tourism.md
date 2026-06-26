## 1. Title: Tourism in Somalia dataset

## Collection Method:
This dataset is about domestic tourism in Somalia. I collected the data using a questionnaire distributed to people who travel within the country.


## 2.Description of Features & Labels:

### Features (x):
Number_of_Tourists: -> the number of people going on the trip together
Destination: -> the place they are traveling to within the country
Tourism_Type: -> the type of tourism they are doing, for example going to mountains, beaches, deserts, etc.
Days: -> the number of days they stay on the trip
Transport_type: -> the type of transport they use for travel e.g: bus,plane or boat

### label(Y)
-Price: is the value we are trying to predict. It is the output (target) in the dataset. The model uses the input features to estimate the price of the tourism trip.

## 3.Dataset Structure:

- Number of Rows: 50
- Number of Columns: 6

## Sample of the Dataset (10 Rows)

| Number_of_Tourists| Destination| Tourism_Type| Days | Transport_type | price|
|-------------------|------------|-------------|------|----------------|------|
|4|laascaseer|beach,4-7|bus|$30
|1|jalalaqsi|historical|4-7|bus|$20
|1|zaylac|beach|2-3|plane|$30
|1|xingalool-sanaag|mountain|4-7|bus|$20
|3|calmadow|mountain|4-7|bus|$30
|1|qoryooleey|historical|4-7|bus|20
|2|goobweyn|historical|4-7|bus|$30
|1|mareero|beach|2-3|boat|$30


## 4.Quality Issues:
- Missing values if some respondents do not answer all questionnaire questions.
- Duplicate records  the same response is entered more than once.


## 5.Learning Type:
* Learning Type: Supervised Learning

Justification:
--------------
This is a supervised learning problem because the dataset has a clear target variable (y), which is Price. The model learns from the input features such as Number_of_Tourists, Destination, Tourism_Type, Days, and Transport_Type to predict the price of a tourism trip. Since the target variable is a numeric value, this is a regression problem.

## Use Case:
This dataset can be used to build a machine learning project that predicts the price of a tourism trip a person wants to take. The model can learn from past tourism data such as number of tourists, destination, type of tourism, number of days, and transport type. Based on these features, it can estimate how much a new trip will cost.


## Data Science Lifecycle Stages:
- Data Collection
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering, Model Building
- Evaluation
- Deployment.

## Conclusion

This tourism dataset provides useful information about domestic tourism in Somalia. It can be used to analyze tourism patterns and build machine learning models to predict trip prices. By collecting and cleaning the data properly, the dataset can support data-driven decision-making in the tourism sector.

