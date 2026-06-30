# Data Foundations for Machine Learning: Predicting Graduate Employment

   Collection Method

### Title

**Predicting Graduate Employment Based on Academic and Professional Development Factors**

### Collection Method

This dataset was created to study factors that may influence whether a university graduate obtains employment after graduation. The data was collected through manual data collection and structured observations of realistic graduate profiles. The dataset contains information about academic performance, professional development activities, internship experience, and employment outcomes.

The purpose of collecting this dataset is to explore how different academic and career-related factors may contribute to employability and to prepare the data for future Machine Learning tasks.

---

## 2. Description of Features and Label

The dataset contains four input variables (features X) and one output variable (label y).

### Features (X)

| Feature              | Description                     D                           |
| -------------------- | -------------------------------------------------------------- |
| GPA                  | Student's Grade Point Average on a 4.0 scale                      |
| Certifications_Count/skills    | Number of professional certifications obtained  
                 |
| Workshops_Attended   | Number of workshops, seminars, or professional events attended |

| Internship_Exp       | Whether the student completed an internship (Yes/No)           |

### Label (y)

| Label      | Description                                                        |
| ---------- | ------------------------------------------------------------------ |
| Employment | Whether the graduate obtained employment after graduation (Yes/No) |

The features represent academic achievement and professional development activities, while the label represents the employment outcome that the model will attempt to predict.

---

## 3. Dataset Structure

The dataset contains:

* 100 rows (samples)
* 5 columns
* 4 features
* 1 label

### Sample of the Dataset

| GPA   | Certifications_Count | Workshops_Attended | Internship_Exp | Employment |
| --- | -------------------- | ------------------ | -------------- | ---------- |
| 3.6 | 3                    | 4                  | Yes            | Yes        |
| 2.0 | 1                    | 3                  | No             | No         |
| 3.2 | 2                    | 3                  | Yes            | Yes        |
| 2.5 | 0                    | 1                  | No             | No         |
| 3.9 | 4                    | 5                  | Yes            | Yes        |

Each row represents one graduate and their associated academic and professional characteristics.

---

## 4. Data Quality Issues

Like many real-world datasets, this dataset may contain several quality issues that should be addressed before training a Machine Learning model.

### Missing Values

Some records may contain missing information, such as unknown GPA values or missing certification counts.

### Categorical Data

The variables Internship_Exp and Employment contain text values (Yes/No), which must be converted into numerical values through encoding.

### Class Imbalance

The number of employed graduates may not be perfectly balanced with unemployed graduates, which could affect model performance.

### Inconsistent Data Entry

Different users may enter information in different formats, creating inconsistencies that require cleaning.

### Noise and Outliers

Certain records may not follow the common pattern, such as graduates with low GPA obtaining employment or graduates with high GPA remaining unemployed.

These issues highlight the importance of preprocessing before model training.

---

## 5. Learning Type

This problem is a **Supervised Learning** problem.

The reason is that the dataset contains a clear target variable (Employment), which is known for every sample. The Machine Learning model can learn the relationship between the input features and the employment outcome.

Because the target variable has two categories (Yes or No), this is specifically a **Classification Problem**.

---

## 6. Use Case and Data Science Lifecycle

### Machine Learning Use Case

This dataset can be used to build a classification model that predicts whether a graduate is likely to obtain employment based on academic performance and professional development activities.

Potential applications include:

* Graduate employability prediction
* Career readiness assessment
* Student success analysis
* Educational decision support systems

### Position in the Data Science Lifecycle

This dataset fits into the following stages of the Data Science Lifecycle:

1. Problem Definition: – Predict graduate employment.
2. Data Collection: – Gather academic and professional development information.
3. Data Preparation: – Clean and preprocess the dataset.
4. Model Building: – Train a classification model.
5. Evaluation: – Measure model performance.
6. Deployment: – Use the model to support career planning and decision-making.

---

## 7. Conclusion

This project demonstrates the importance of data foundations in Machine Learning. A dataset was created containing information about GPA, certifications, workshop participation, internship experience, and employment outcomes. The problem was identified as a supervised classification task because it includes a known target variable. Before training a Machine Learning model, preprocessing steps such as handling missing values, encoding categorical variables, and cleaning inconsistencies will be required. This dataset provides a foundation for future Machine Learning experiments focused on predicting graduate employability.
