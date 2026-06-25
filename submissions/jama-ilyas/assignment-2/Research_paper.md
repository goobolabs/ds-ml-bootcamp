# Customer Satisfaction and Return Prediction Dataset for a Local Restaurant

## 1. Introduction

This research paper presents a small dataset collected about customer satisfaction in a local restaurant or café. The purpose of this dataset is to understand customer experience and predict whether a customer is likely to return again or not. Customer satisfaction is very important for any business because happy customers are more likely to come back, recommend the business to others, and help the business grow.

The dataset focuses on different factors that may affect customer satisfaction, such as the time of visit, type of order, waiting time, service rating, price rating, and whether the customer would return. This topic was chosen because restaurant businesses deal with customers every day, and collecting customer data can help the management make better decisions.

This dataset is useful in Data Science because it shows how real-world data can be collected, organized, analyzed, and prepared for machine learning. It also helps explain important machine learning concepts such as features, labels, supervised learning, classification, and data quality issues.

## 2. Dataset Title and Collection Method

The title of this dataset is **Customer Satisfaction and Return Prediction Dataset for a Local Restaurant**.

The dataset was collected manually using a short customer survey and observation. The survey was designed to collect simple information from customers after they received service. Some information, such as visit time and waiting time, could also be observed directly.

The data contains 50 customer records. Each row represents one customer. The dataset was created to reflect real-world data collection, so it includes some missing values, spelling mistakes, inconsistent capitalization, and mixed data formats. These issues are common in real datasets and will need to be handled during preprocessing.

The questions used to collect the data included:

1. What is your age group?
2. What time did you visit the restaurant?
3. What type of order did you make?
4. How many minutes did you wait?
5. How would you rate the service from 1 to 5?
6. How do you rate the price?
7. Would you return to the restaurant again?

## 3. Description of Features and Label

The dataset contains input variables called features and one output variable called the label.

The features are the columns used to describe the customer experience. These features can help a machine learning model understand patterns in customer behavior.

| Feature              | Description                                       |
| -------------------- | ------------------------------------------------- |
| Customer_ID          | A unique number given to each customer record     |
| Age_Group            | The age category of the customer                  |
| Visit_Time           | The time when the customer visited the restaurant |
| Order_Type           | The type of order made by the customer            |
| Waiting_Time_Minutes | The number of minutes the customer waited         |
| Service_Rating       | The customer’s rating of the service from 1 to 5  |
| Price_Rating         | The customer’s opinion about the price            |

The label is:

| Label        | Description                                          |
| ------------ | ---------------------------------------------------- |
| Would_Return | Shows whether the customer would return again or not |

In this dataset, **Would_Return** is the output variable because it is the value we want to predict. The possible answers are **Yes** or **No**.

## 4. Dataset Structure

The dataset has **50 rows** and **8 columns**. Each row represents one customer, while each column represents one type of information collected from the customer.

The dataset structure is as follows:

| Column Name          | Data Type   |
| -------------------- | ----------- |
| Customer_ID          | Numerical   |
| Age_Group            | Categorical |
| Visit_Time           | Categorical |
| Order_Type           | Categorical |
| Waiting_Time_Minutes | Numerical   |
| Service_Rating       | Numerical   |
| Price_Rating         | Categorical |
| Would_Return         | Categorical |

A small sample of the dataset is shown below:

| Customer_ID | Age_Group | Visit_Time | Order_Type | Waiting_Time_Minutes | Service_Rating | Price_Rating | Would_Return |
| ----------- | --------- | ---------- | ---------- | -------------------: | -------------: | ------------ | ------------ |
| 1           | 18-25     | Morning    | Drink      |                    5 |              5 | Fair         | Yes          |
| 2           | 26-35     | Afternoon  | Food       |                   15 |              3 | Expensive    | No           |
| 3           | 18-25     | Evening    | Food+Drink |                   10 |              4 | Fair         | Yes          |
| 4           | 36-45     | Morning    | Food       |                    8 |              5 | Cheap        | Yes          |
| 5           | 26-35     | Evening    | Drink      |                   12 |              3 | Fair         | Yes          |
| 6           | 46+       | Afternoon  | Food       |                   20 |              2 | Expensive    | No           |
| 7           | 18-25     | Evening    | Food+Drink |                    7 |              4 | Cheap        | Yes          |
| 8           | 36-45     | Afternoon  | Drink      |                    6 |              5 | Fair         | Yes          |

## 5. Data Quality Issues

The dataset contains some quality issues because it was collected manually. This is normal in real-world data collection. Before using the dataset in a machine learning model, these problems need to be cleaned during preprocessing.

Some of the quality issues include:

### Missing Values

Some rows have missing values. For example, some customers may not provide their age group, service rating, waiting time, or return intention. Missing values can affect analysis and machine learning accuracy if they are not handled properly.

### Spelling Mistakes

There are some spelling mistakes in the dataset. For example, the word **Expensive** may appear as **expensiv**. This can create problems because the computer may treat the two words as different categories.

### Inconsistent Capitalization

Some values are written in different formats. For example, **Yes**, **YES**, and **yes** all mean the same thing, but a computer may treat them as different values unless they are standardized.

### Mixed Data Formats

The column **Waiting_Time_Minutes** should contain numbers, but one row contains the text value **ten** instead of the number **10**. This must be corrected before analysis.

### Categorical Data

Several columns contain text categories, such as Age_Group, Visit_Time, Order_Type, and Price_Rating. These values need to be encoded into numerical form before they can be used in most machine learning models.

### Possible Imbalance

The dataset may contain more **Yes** values than **No** values in the Would_Return column. This can cause class imbalance, meaning the model may learn more about one class than the other.

## 6. Learning Type

This dataset is suitable for **supervised learning** because it has a clear label called **Would_Return**. Supervised learning is used when the dataset contains both input features and an output label.

In this case, the input features include Age_Group, Visit_Time, Order_Type, Waiting_Time_Minutes, Service_Rating, and Price_Rating. The output label is Would_Return.

The machine learning problem is a **classification problem** because the output has categories: **Yes** or **No**. The goal is to predict whether a customer will return to the restaurant again based on their experience.

## 7. Use Case in Machine Learning

This dataset can be used in a machine learning project to predict customer return behavior. A restaurant can use this prediction to understand what affects customer loyalty.

For example, if customers with long waiting times and low service ratings often choose not to return, the business can improve service speed and staff training. If customers who rate the price as expensive are less likely to return, the restaurant can review its pricing strategy or introduce promotions.

This dataset could be used for:

* **Classification:** Predicting whether a customer will return: Yes or No.
* **Data Analysis:** Understanding patterns in customer satisfaction.
* **Business Decision Making:** Improving service, pricing, and customer experience.

## 8. Position in the Data Science Lifecycle

This dataset fits into the Data Science lifecycle in the following way:

First, data is collected from customers through surveys and observation. Second, the data is stored in a structured format such as CSV. Third, the data is cleaned during preprocessing by handling missing values, fixing spelling mistakes, standardizing text, encoding categorical variables, and correcting mixed formats.

After preprocessing, the data can be analyzed to find patterns. Then a machine learning model can be trained to predict whether customers are likely to return. Finally, the results can be used by the restaurant to make better business decisions.

## 9. Conclusion

In conclusion, this research paper explains a customer satisfaction dataset collected from a local restaurant. The dataset contains 50 rows and 8 columns, including customer information, service experience, price opinion, and return intention.

The dataset is suitable for supervised learning because it has a clear label, Would_Return. It is also a classification problem because the output has two categories: Yes and No.

Although the dataset contains quality issues such as missing values, spelling mistakes, inconsistent capitalization, and mixed formats, these problems are useful because they represent real-world data challenges. These issues can be handled through preprocessing in Lesson 4.

This assignment helped me understand how data is collected, structured, described, and prepared for machine learning. It also showed how Data Science can be used to solve real business problems such as improving customer satisfaction and increasing customer return rates.
