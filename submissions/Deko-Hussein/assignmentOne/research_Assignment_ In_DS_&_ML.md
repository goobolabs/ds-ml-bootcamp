# Data Science and Machine Learning Assignment

## Overview

This assignment explains the basic concepts of Data Science and Machine Learning, their relationship, the Data Science lifecycle, supervised and unsupervised learning, overfitting, training and test data splitting, and one case study showing how Machine Learning is applied in transportation.

Most of the examples in this assignment are connected to a **Bajaj transportation business** to make the explanation practical and easy to understand.

---

## 1. Define Data Science and Machine Learning. What is the relationship between them? Use a real-life example to illustrate how they work together.

## Data Science and Machine Learning

Data Science is the process of collecting, cleaning, analyzing, and interpreting data to gain useful knowledge and support decision-making. It helps individuals and organizations understand patterns, trends, and useful information hidden inside data.

Machine Learning is a subset of Artificial Intelligence (AI) that uses algorithms to learn from data and make predictions or decisions automatically. Instead of being programmed for every task, a machine learning model improves its performance by learning from previous data.

### Relationship Between Data Science and Machine Learning

Data Science and Machine Learning are closely related. Data Science focuses on collecting, preparing, cleaning, and analyzing data, while Machine Learning uses that prepared data to build models that can make predictions or discover patterns.

In simple terms, Data Science provides the foundation, and Machine Learning uses the data to generate intelligent results. Without proper data collection, cleaning, and analysis, machine learning models may produce inaccurate results.

### Real-Life Example: Bajaj Transportation Business

A Bajaj owner may want to understand how the business operates and how to increase profit. Using Data Science, the owner can collect and analyze information such as:

* Daily number of customers.
* Busiest working hours.
* Daily fuel expenses.
* Daily income.
* Common routes.
* Trip distance.
* Customer demand at different times of the day.

After the data has been collected, cleaned, and analyzed, Machine Learning can be used to learn patterns from the data. For example, if a Bajaj works for 12 hours per day, a machine learning model can predict the expected income and fuel cost for future days. It can also identify the most profitable routes and the busiest working hours.

This example shows how Data Science and Machine Learning work together. Data Science prepares and analyzes Bajaj business data, while Machine Learning uses that data to make predictions and support better business decisions.

---

## 2. Describe the Data Science lifecycle. At which stage is Machine Learning mainly used, and why?

## Data Science Lifecycle

The Data Science lifecycle is a structured process used to solve problems using data. It explains the main steps followed from understanding a problem to building and using a data-based solution.

The main stages of the Data Science lifecycle are problem definition, data collection, data cleaning, exploratory data analysis, feature engineering, modeling, evaluation, and deployment.

| Stage                     | Description                                                             | Bajaj Business Example                                                               |
| ------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Problem Definition        | Identifying the problem that needs to be solved.                        | The Bajaj owner wants to increase daily income and reduce fuel cost.                 |
| Data Collection           | Gathering data from different sources.                                  | The owner collects data about trips, routes, customers, fuel cost, and income.       |
| Data Cleaning             | Removing errors, missing values, duplicates, and incorrect information. | Incorrect trip records, missing income values, and duplicate entries are removed.    |
| Exploratory Data Analysis | Studying the data to understand patterns and relationships.             | The owner checks which routes and hours bring more income.                           |
| Feature Engineering       | Selecting or creating useful variables for the model.                   | Features such as income per hour, fuel cost per trip, and trip distance are created. |
| Modeling                  | Building a machine learning model using prepared data.                  | A model is trained to predict daily income or fuel cost.                             |
| Evaluation                | Testing the model to check how well it performs.                        | The model predictions are compared with actual Bajaj income records.                 |
| Deployment                | Using the model in real life.                                           | The Bajaj owner uses the model to plan routes and working hours.                     |

### Data Science Lifecycle Flow

Problem Definition → Data Collection → Data Cleaning → Exploratory Data Analysis → Feature Engineering → Modeling → Evaluation → Deployment

Machine Learning is mainly used in the **modeling stage**. This is because the modeling stage is where algorithms are trained using prepared data to learn patterns and make predictions.

However, Machine Learning also depends on earlier stages such as data cleaning and feature engineering. If the Bajaj data is incomplete, incorrect, or poorly prepared, the model may give poor predictions. Therefore, the success of Machine Learning depends strongly on the quality of the Data Science lifecycle.

---

## 3. Differentiate between Supervised Learning and Unsupervised Learning. Give one example of each.

## Supervised and Unsupervised Learning

Machine Learning can be divided into different types. Two common types are supervised learning and unsupervised learning.

### Supervised Learning

Supervised Learning uses labeled data. This means the dataset already contains both the input data and the correct output. The model learns from these examples and later uses the learned patterns to predict outputs for new data.

In a Bajaj transportation business, supervised learning can be used to predict daily income. For example, the owner may have past records showing working hours, route type, number of customers, fuel cost, and total daily income. Since the correct income values are already known, the model can learn from this labeled data.

For example, if the Bajaj works 10 hours on a busy route with many customers, the model may predict that the income will be high. This is supervised learning because the model learns from previous examples where the correct output is already available.

### Unsupervised Learning

Unsupervised Learning uses unlabeled data. This means the dataset does not contain predefined answers. The model tries to discover hidden patterns, groups, or structures in the data by itself.

In a Bajaj transportation business, unsupervised learning can be used to group customers or routes. For example, the owner may collect data about trip times, routes, customer locations, and payment amounts without already knowing the customer groups.

The model may discover that some customers mostly travel in the morning, some use the Bajaj during school or work hours, and others use it at night. It may also group routes into busy routes, normal routes, and low-demand routes.

### Comparison Between Supervised and Unsupervised Learning

| Feature       | Supervised Learning                           | Unsupervised Learning                          |
| ------------- | --------------------------------------------- | ---------------------------------------------- |
| Type of data  | Labeled data                                  | Unlabeled data                                 |
| Main purpose  | Prediction or classification                  | Pattern discovery or grouping                  |
| Output        | Known output is provided during training      | No predefined output                           |
| Bajaj example | Predicting daily income from previous records | Grouping routes or customers based on behavior |
| Common tasks  | Classification and regression                 | Clustering and association                     |

Supervised learning is useful when the correct answers are already available in the dataset. Unsupervised learning is useful when the goal is to discover hidden patterns without predefined labels.

---

## 4. What best describes overfitting? What causes overfitting, and how can it be prevented?

## Overfitting in Machine Learning

Overfitting occurs when a machine learning model learns the training data too well, including noise, errors, and unnecessary details. As a result, the model performs very well on training data but poorly on new, unseen data.

A good machine learning model should learn general patterns from data. However, an overfitted model memorizes the training data instead of learning patterns that can work on new data.

### Bajaj Example of Overfitting

Overfitting can happen if a machine learning model memorizes Bajaj business data instead of learning general patterns. For example, suppose the model is trained using only one week of Bajaj income data. During that week, there may have been unusual events such as rain, road closure, school exams, or a public holiday.

If the model learns only those special conditions, it may make poor predictions for normal days. It may perform well on the training data but fail when used on new days.

For example, the model may predict very high income every Friday because one Friday in the training data had unusually high customers. However, this pattern may not happen every Friday. This means the model has overfitted the training data.

### Causes of Overfitting

Several factors can cause overfitting. One cause is having a small training dataset, which makes the model memorize limited examples instead of learning general patterns. Another cause is using a very complex model with too many parameters. Overfitting can also occur when the model is trained for too long or when the dataset contains irrelevant features and noisy data.

### Prevention of Overfitting

Overfitting can be prevented in several ways. Using more clean and diverse data helps the model learn better patterns. Feature selection can remove unnecessary columns that do not contribute to predictions. Early stopping can prevent the model from training for too long. Simpler models and regularization techniques can also reduce overfitting.

In addition, train-test splitting and cross-validation help detect whether the model generalizes well to new data.

| Causes of Overfitting        | Prevention Methods                        |
| ---------------------------- | ----------------------------------------- |
| Small dataset                | Use more data                             |
| Complex model                | Use a simpler model                       |
| Noisy data                   | Clean the dataset                         |
| Too many irrelevant features | Use feature selection                     |
| Training for too long        | Apply early stopping                      |
| Poor evaluation method       | Use train-test split and cross-validation |

Therefore, overfitting can be described as a situation where a model memorizes the training data instead of learning useful patterns that can be applied to unseen data.

---

## 5. Explain how training data and test data are split, and why this process is necessary.

## Training Data and Test Data Split

In Machine Learning, a dataset is usually divided into two main parts: training data and test data. This separation helps evaluate whether a machine learning model can perform well on new data, not only on the data it has already seen.

Using a Bajaj transportation business as an example, the dataset may include information such as daily income, fuel cost, number of customers, working hours, routes used, trip distance, and time of day.

Training data is the portion of the dataset used to train the model. For example, if the Bajaj owner has previous records of trips and income, most of those records can be used to teach the model. The model learns patterns such as which routes bring more customers, which hours are busiest, and how fuel cost affects daily profit.

Test data is a separate portion of the dataset that is not shown to the model during training. It is used only after the model has been trained. For example, some Bajaj trip records are kept aside and later used to test whether the model can correctly predict income, fuel cost, or customer demand for new trips.

The dataset is commonly split using ratios such as 70/30 or 80/20. For example, if the Bajaj owner has 1,000 trip records, 800 records can be used for training and 200 records can be used for testing.

| Total Bajaj Records | Training Data | Test Data   |
| ------------------- | ------------- | ----------- |
| 1,000 trip records  | 800 records   | 200 records |

This approach is necessary because the goal is not for the model to memorize old Bajaj records. Instead, the model should learn general patterns that can be applied to future trips and new working days.

By testing the model on unseen Bajaj data, the owner can measure whether the model generalizes well and can detect problems such as overfitting. For example, if the model performs very well on the training records but gives poor predictions on the test records, this may mean the model has overfitted.

Therefore, separating training data and test data is important because it gives a more realistic evaluation of the model’s performance.

---

## 6. Find one case study that explains how Data Science or Machine Learning has been applied in healthcare, business, or transportation. Summarize its findings and identify which part of the Data Science lifecycle it covers.

## Case Study: Application of Data Science and Machine Learning in Transportation

One case study is the research paper **“Data Science in Transportation Networks with Graph Neural Networks: A Review and Outlook.”** The paper explains how Data Science and Machine Learning are used in transportation networks to predict traffic, estimate travel time, improve route planning, and support traffic control.

The study focuses on **Graph Neural Networks (GNNs)**. Transportation systems can be represented as graphs, where nodes represent places such as road segments, intersections, or traffic sensors, and edges represent the roads connecting them. This helps the model understand how traffic in one area affects nearby areas.

The findings show that GNNs are useful for predicting traffic speed, traffic flow, congestion, travel time, and transportation demand. The paper also mentions real-world applications such as Google Maps, where machine learning is used to predict estimated time of arrival and help users choose better routes.

This case study can be related to a Bajaj transportation business. A Bajaj driver can collect data about routes, trip time, fuel cost, number of customers, and daily income. Machine Learning can then help predict busy routes, profitable working hours, and ways to reduce fuel waste.

This case study covers several stages of the Data Science lifecycle, including problem definition, data collection, data processing, feature engineering, modeling, evaluation, and deployment. However, the most important stage it covers is the **modeling stage**, because Graph Neural Networks are used to learn from transportation data and make predictions.

In conclusion, the case study shows that Data Science and Machine Learning can improve transportation systems by helping predict traffic conditions, reduce delays, support route planning, and improve overall transportation efficiency.

---

## Conclusion

Data Science and Machine Learning are important fields that help people and organizations make better decisions using data. Data Science focuses on collecting, cleaning, analyzing, and interpreting data, while Machine Learning uses that data to build models that can make predictions.

The Data Science lifecycle provides a clear process for solving data problems. Machine Learning is mainly used in the modeling stage, but it depends on earlier stages such as data cleaning and feature engineering.

Supervised learning uses labeled data for prediction, while unsupervised learning uses unlabeled data to find hidden patterns. In a Bajaj transportation business, supervised learning can predict income, while unsupervised learning can group customers or routes.

Overfitting is one of the major challenges in Machine Learning because it causes models to perform poorly on new data. This problem can be prevented using more data, simpler models, regularization, early stopping, feature selection, train-test splitting, and cross-validation.

Training and test data splitting is necessary because it helps evaluate whether a model can generalize to unseen data. Finally, the transportation case study shows how Machine Learning can be used in a real-world transportation system to predict busy routes, reduce fuel waste, and improve business performance.

---

## References

Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.

Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.

Han, J., Kamber, M., & Pei, J. (2012). *Data Mining: Concepts and Techniques* (3rd ed.). Morgan Kaufmann.

James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning: With Applications in R* (2nd ed.). Springer.

Mitchell, T. M. (1997). *Machine Learning*. McGraw-Hill.

Xue, J., Tan, R., Ma, J., & Ukkusuri, S. V. (2025). *Data Science in Transportation Networks with Graph Neural Networks: A Review and Outlook*. Data Science for Transportation, 7, 10.



## Author

Name:Deko Hussein Said
Course: Data Science and Machine Learning Bootcamp
Topic:Data Science and Machine Learning Assignment
