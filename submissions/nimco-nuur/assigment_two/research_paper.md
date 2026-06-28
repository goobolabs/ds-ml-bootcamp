# Consumer Technology FOMO and Upgrade Intention Dataset

**Author: Nimco Nuur Gesey**
**Course: DS-ML Bootcamp – Assignment 2**
**Due: Saturday, June 20, 2026**

---

# 1. Title and Collection Method

## Title

**Consumer Technology FOMO and Upgrade Intention Dataset**

## Collection Method

Technology companies constantly introduce new smartphones, laptops, smartwatches, and other digital devices. While some consumers upgrade their devices immediately after a new release, others continue using their existing devices for several years. Understanding the factors that influence upgrade decisions is important for businesses, marketers, and technology companies.

This dataset was created to examine the relationship between technology-related behaviors and consumers' intentions to upgrade their devices. The data was collected through a survey questionnaire distributed to technology users. Participants were asked about their gadget preferences, technology media consumption habits, peer influence, financial behavior, and perceptions regarding device obsolescence.

A total of **50 responses** were collected and stored in a CSV dataset. The dataset was created specifically for this assignment and was not obtained from Kaggle, UCI, or any other public dataset repository.

The goal of the dataset is to identify patterns that influence whether a consumer intends to upgrade to a newer device.

---

# 2. Description of Features and Labels

In Machine Learning, the dataset is divided into input variables (**features X**) and an output variable (**label y**).

The features represent the information used by the model to make predictions, while the label is the value the model attempts to predict.

## Features (X)

| No. | Feature                | Type        | Description                                                            |
| --- | ---------------------- | ----------- | ---------------------------------------------------------------------- |
| 1   | Primary_Gadget_Focus   | Categorical | Main device the participant is interested in                           |
| 2   | Tech_Media_Consumption | Categorical | Frequency of consuming technology-related content                      |
| 3   | Peer_Tech_Influence    | Categorical | Influence of friends and peers on technology purchasing decisions      |
| 4   | Financial_Sacrifice    | Categorical | Willingness to spend or sacrifice financially for new technology       |
| 5   | Perceived_Obsolescence | Categorical | Whether the participant believes their device becomes outdated quickly |

## Label (y)

| Label             | Type        | Values  |
| ----------------- | ----------- | ------- |
| Intent_To_Upgrade | Categorical | Yes, No |

The label indicates whether the participant plans to upgrade their device in the near future.

---

# 3. Dataset Structure

The dataset consists of:

| Property             | Value |
| -------------------- | ----- |
| Total Rows (Samples) | 50    |
| Total Columns        | 6     |
| Features             | 5     |
| Label                | 1     |

## Sample Dataset

| Primary_Gadget_Focus | Tech_Media_Consumption | Peer_Tech_Influence | Financial_Sacrifice | Perceived_Obsolescence | Intent_To_Upgrade |
| -------------------- | ---------------------- | ------------------- | ------------------- | ---------------------- | ----------------- |
| Smartphone           | Every day              | Very much           | Yes                 | Yes                    | Yes               |
| Laptop               | Sometimes              | No                  | No                  | No                     | No                |
| Smartphone           | A few times a week     | A little            | No                  | Yes                    | Yes               |
| Laptop               | Every day              | Very much           | Yes                 | Yes                    | Yes               |
| Smartphone           | Sometimes              | No                  | No                  | No                     | No                |
| Smartwatch           | Every day              | Very much           | Yes                 | Yes                    | Yes               |
| Laptop               | A few times a week     | A little            | No                  | No                     | No                |

From the sample data, it appears that participants who consume technology content frequently and perceive their devices as outdated are more likely to express an intention to upgrade.

---

# 4. Quality Issues

Real-world datasets often contain quality problems that must be addressed before Machine Learning models can be trained effectively.

The first issue in this dataset is that all variables are categorical. Machine Learning algorithms generally require numerical data, so the categorical values must be transformed using encoding techniques such as Label Encoding or One-Hot Encoding.

Another issue is the relatively small dataset size. With only 50 samples, the dataset may not fully represent the behavior of all technology consumers. A larger dataset would improve the model's ability to learn meaningful patterns and generalize to new users.

The dataset may also contain class imbalance. If most participants answered "Yes" for Intent_To_Upgrade and only a few answered "No," the model could become biased toward the majority class. This issue can be addressed using resampling techniques during preprocessing.

Survey response bias is another possible challenge. Participants may exaggerate their interest in technology or provide inaccurate answers about their purchasing behavior. Because the responses are self-reported, they may not always reflect actual consumer actions.

5. Learning Type

This dataset represents a **Supervised Learning** problem.

A supervised learning problem contains both input variables (features) and a known output variable (label). In this dataset, every participant has a recorded value for **Intent_To_Upgrade**, which serves as the target variable.

The Machine Learning model can learn the relationship between the features and the known label. By studying many examples, the model can identify patterns that distinguish users who intend to upgrade from those who do not.

More specifically, this is a **Classification** problem because the target variable contains categories ("Yes" and "No") rather than numerical values.

If the target variable were a number, such as the amount of money spent on technology products, the problem would be a regression task. However, because the goal is to predict one of two categories, classification is the most appropriate approach.

---

# 6. Use Case and Data Science Lifecycle

This dataset has several practical applications in Machine Learning and Data Science.

The primary use case is **classification**, where a model predicts whether a consumer intends to upgrade their device based on their technology-related behaviors and attitudes. Algorithms such as Logistic Regression, Decision Trees, Random Forests, and Naive Bayes can be used for this task.

The dataset can also support **consumer behavior analysis**. Businesses can identify which factors have the strongest influence on upgrade decisions, such as peer influence, media consumption, or perceived obsolescence.

In addition, the dataset can be used for **clustering**, an unsupervised learning technique. Consumers can be grouped into categories such as high-FOMO users, frequent upgraders, budget-conscious users, and low-interest technology users. These groups can help businesses design targeted marketing strategies.

Within the **Data Science Lifecycle**, this dataset fits into several stages. The process begins with problem definition, where the objective is to understand what drives device upgrade intentions. The next stage is data collection through surveys. After collection, the data undergoes preprocessing to handle encoding, duplicates, and other quality issues. Exploratory Data Analysis (EDA) is then performed to discover trends and relationships. Following analysis, Machine Learning models are trained and evaluated. Finally, the resulting model can be deployed to support business decision-making and marketing campaigns.

---

# Conclusion

The Consumer Technology FOMO and Upgrade Intention Dataset was developed to investigate the factors that influence consumers' decisions to upgrade their technology devices. The dataset contains 50 samples, five input features, and one target label. Because it includes a clearly defined output variable, it is suitable for supervised Machine Learning classification tasks. Despite challenges such as categorical data, potential class imbalance, and survey bias, the dataset provides a valuable opportunity to apply data preprocessing, exploratory analysis, and predictive modeling techniques within the Data Science lifecycle.
