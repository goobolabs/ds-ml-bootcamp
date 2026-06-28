# Car rental Dataset

## What is your dataset about?

The Dataset contains car rental information, The initial data seed was taken from [Honsi Rental Car](https://hosnirentalcar.com/) and then generated dirty data using llm(Chatgpt).

<a href="./honsi_seed_data.txt">Seed Data: 18 Cars</a>
<br>
<a href="./cars.csv">Dataset: 100 Cars</a>

## How did you collect it?

I collected the seed data by visiting [Honsi Rental Car website](https://hosnirentalcar.com/vehicles) and manually gathering the information of cars such as name of the car rate,seats,transmission,fuel,price_per_day.

## Description of Features & Labels?

The dataset has four possible features and one label/target value.

| features     | info                                      |
| ------------ | ----------------------------------------- |
| transmission | weather car is auto/manual                |
| seats        | how many seats does the car have          |
| fuel         | fuel type                                 |
| category     | type of car for family,work,single person |

<br>

| label         | info             |
| ------------- | ---------------- |
| price_per_day | Daily price rate |

## Dataset Structure?

The structure of the dataset was (98,7), 98 rows and 7 columns.

| name         | rating | transmission | seats   | fuel     | price_per_day | category |
| ------------ | ------ | ------------ | ------- | -------- | ------------- | -------- |
| Saruf        | 4.5    | Automatic    | 5 Seats | Gasoline | $85/day       | Single   |
| Saruf        | 4.4    | Automatic    | 5 Seats | Gasoline | $85/day       | Single   |
| Saruf        | 4.3    | Automatic    | 5 Seats | Gasoline | $85/day       | Single   |
| Prado Tx     | 4.8    | Automatic    | 7 Seats | Gasoline | $120/day      | Family   |
| Prado Tx     | 4.9    | Automatic    | 7 Seats | Gasoline | $120/day      | Family   |
| Prado Tx     | 5.0    | Automatic    | 7 Seats | Gasoline | $120/day      | Family   |
| Toyota Sarif | 4.5    | Manual       | 5 Seats | Gasoline | $85/day       | Work     |
| Toyota Sarif | 4.4    | Manual       | 5 Seats | Gasoline | $85/day       | Work     |
| Toyota Sarif | 4.3    | Manual       | 5 Seats | Gasoline | $85/day       | Work     |

## Quality Issues?

The dataset has many quality issues such as missing,inconsistency,type errors.

example of quality issue

| name         | rating    | transmission | seats      | fuel     | price_per_day | category |
| ------------ | --------- | ------------ | ---------- | -------- | ------------- | -------- |
| Saruf        | 4.5       | Automatic    | 5 Seats    | Gasoline | $85/day       | Single   |
| Saruf        | %4.4%     |              | 5 Seats    | Gasoline | $85/day       | Single   |
| Saruf        | 4.3       |              | Five Seats | Diesel   | $85/day       |          |
| Prado Tx     | %4.8      | Automatic    | 7 Seats    | Gasoline | $120/day      | Family   |
| Prado Tx     | 4.9       | Automatic    | 7 Seats    | Gasoline | $120/day      |          |
| Prado Tx     | 5.0       | Automatic    | 7 Seats    | Gasoline | $120/day      | Family   |
| Toyota Sarif | Excellent | Manual       | 5 Seats    | Gasoline | $85/day       | Work     |
| Toyota Sarif | 4.4       | Manual       | 5 Seats    | Diesel   | $85/day       | Work     |
| Toyota Sarif | 4.3       | Manual       | 5 Seats    | Diesel   |               |          |

This dataset is not consistency, has missing values, has typo errors.

## Learning Type?

The learning type of this dataset is supervised because we have features/inputs and label/output which supervised learning type requires.

## Use Case?

The machine learning use case for this dataset is supervised learning, specifically regression. It is a regression problem because the target (label) is a continuous numerical value.

This dataset will be useful for cars daily price rate prediction and statistical analysis to uncover hidden insights.

### Where would it fit in the Data Science lifecycle?

It fits into the Problem Definition and Data Collection phases of the data science lifecycle.
