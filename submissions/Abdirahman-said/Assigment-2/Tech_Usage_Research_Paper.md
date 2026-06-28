# Tech Usage and Perceived Productivity: A Preliminary Data Analysis

**Author:** [Abdirahman]  
**Course:** Data Science and Machine Learning 

---

## 1. Title & Collection Method
**Dataset Title:** The Technology Usage and Productivity Questionnaire  
**Collection Method:** This dataset was compiled to analyze the relationship between personal technology habits and self-reported productivity. The primary data was collected via a digital survey distributed using Google Forms, gathering demographic information, device usage statistics, and behavioral patterns regarding screen time and notifications. 

## 2. Description of Features & Labels
In the context of predicting how technology habits influence a person's workflow, the dataset is divided into input variables (Features, $X$) and the target output variable (Label, $y$).

### The Output Variable (Label $y$)
* **`Do you feel your tech usage affects your productivity?`**: This is the target variable we want to predict. It is a multi-class categorical variable with responses including "Yes, positively," "Yes, negatively," "No effect," and "Not sure."

### The Input Variables (Features $X$)
These are the 11 attributes used to make the prediction, encompassing demographics, quantitative usage, and qualitative habits:
* **Demographics:** `Age`, `Gender`, `Occupation`
* **Usage Metrics:** `Daily smartphone usage`, `Number of apps used daily`, `Daily social media time`
* **Self-Assessments:** `Tech‑savviness rating` (Scale 1-5), `Privacy concern level` (Scale 1-5)
* **Behavioral Context:** `Primary device used daily`, `Purpose of most daily screen time`, `Frequency of checking notifications`

## 3. Dataset Structure
Final dataset consists of **52 rows** (samples) and **12 columns** (11 features + 1 label). 

### Sample Data Table (First 5 Rows)

| Age | Gender | Occupation | Daily smartphone usage | Apps used | Daily social media time | Tech‑savviness | Privacy concern | Primary device | Purpose of most daily screen time | Frequency of checking notifications | Productivity Effect ($y$) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 24-26 | Male | Student | 2-4 hours | 7-10 | 2-4 hours | 3 | 4 | Laptop | Work or study, Entertainment... | Every 1–2 hours | *NaN* |
| 24-26 | Female | Student | 4-6 hours | 4-6 | 2-4 hours | 1 | 2 | Other | Work or study | Only when needed | Not sure |
| 24-26 | Male | Employed | 8+ | 4-6 | 6+ hours | 3 | 1 | Laptop | Social media, Work or study... | Every few minutes | No effect |
| 24-26 | Female | Unemployed | 2-4 hours | 1-3 | 2-4 hours | 2 | 1 | Smartphone | Social media, Entertainment... | Every few minutes | Yes, positively |
| 27-29 | Male | Other | 8+ | 1-3 | 6+ hours | 2 | 2 | Smartphone | Social media | Every few minutes | Yes, positively |

## 4. Quality Issues
As expected in raw, user-generated survey data, several data quality and integrity issues exist that must be addressed before modeling:
* **Missing Values:** There are null values in the target variable. These rows cannot be used for supervised training and must be dropped or imputed.
* **Formatting and Typos:** There are inconsistencies in the column headers, including trailing and leading spaces. Furthermore, there are typos in the categorical data entries, such as `"Self-empployed"`, which will create separate, erroneous categories if not corrected.
* **Class Imbalance:** The dataset is heavily skewed demographically and in the target variable, with a strong bias toward the "Yes, positively" label.
* **High Cardinality/Complex Strings:** The `Purpose of most daily screen time` column contains comma-separated lists of multiple selections, requiring complex parsing.

## 5. Learning Type
This dataset requires a **Supervised Learning** approach. Supervised learning is defined by the presence of a known, clear label ($y$) that the algorithm learns to predict. Because our goal is to map the input features ($X$) to a specific, predefined output category, we are providing the algorithm with the "ground truth" during training.

## 6. Use Case & The Data Science Lifecycle
### Machine Learning Use Case
This dataset is suited for a **Multi-Class Classification** project. By training an algorithm (such as a Decision Tree, Random Forest, or Logistic Regression), we could build a model that takes a new person's technology habits as input and categorizes whether those habits are likely to have a positive, negative, or neutral impact on their productivity. 

### Position in the Data Science Lifecycle
This project is currently straddling the transition from the **Data Collection** phase to the **Data Preparation (Cleaning)** phase. We have established our business understanding and acquired the raw data. Immediate next steps focus on Data Preparation: fixing headers, handling missing values, and encoding text strings into numeric formats.

---
