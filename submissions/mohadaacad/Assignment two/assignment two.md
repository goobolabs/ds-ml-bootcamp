# **Ass Public Perception of Artificial Intelligence Dataset**

---

## **1. Introduction & Collection Method**

This dataset explores public opinions and perceptions about Artificial Intelligence (A.I), including its impact on society, ethics, regulation, and future risks.

The data was collected using an **online survey (Google Form)** distributed to participants. Respondents provided demographic information (such as age and sex) and answered multiple questions related to A.I.

The dataset contains **81 samples (responses)** and was collected manually through a questionnaire, making it an original dataset created for this assignment.

---

## **2. Description of Features and Label (X and y)**

From the dataset, **5 important features (X)** were selected along with **1 label (y)**.

### **Features (X):**

1. **Age** – Age of the respondent  
2. **Sex** – Gender of the respondent  
3. **AI_Regulation** – Opinion on whether A.I should be regulated by the government  
4. **Job_Loss** – Opinion on whether A.I will lead to widespread job loss  
5. **Data_Privacy** – Opinion on whether A.I should prioritize data privacy and security  

### **Label (y):**

- **AI_Impact** – Opinion on whether A.I will have a significant impact on society in the next 10 years  

These features were chosen because they are directly related to how people perceive A.I and help predict whether someone believes A.I will significantly impact society.

---

## **3. Dataset Structure**

The dataset includes:

- **81 rows (samples)**  
- **6 columns (5 features + 1 label selected from 17 total columns)**  

Each row represents one respondent, and each column represents a variable.

### **Sample Dataset (First 8 Rows):**

| Age | Sex    | AI_Regulation | Job_Loss | Data_Privacy | AI_Impact |
|-----|--------|--------------|----------|--------------|-----------|
| 21  | Male   | Agree        | Yes      | Agree        | Agree     |
| 22  | Female | Agree        | Yes      | Agree        | Agree     |
| 20  | Male   | Disagree     | No       | Agree        | Agree     |
| 23  | Female | Agree        | Yes      | Agree        | Agree     |
| 21  | Male   | Agree        | Yes      | Disagree     | Agree     |
| 24  | Female | Agree        | No       | Agree        | Disagree  |
| 22  | Male   | Disagree     | Yes      | Agree        | Agree     |
| 21  | Female | Agree        | Yes      | Agree        | Agree     |

Each row is a **sample**, and the full table is the **dataset**.

---

## **4. Data Quality Issues**

Several data quality issues were observed:

- **Missing Values:** Some respondents may have skipped questions  
- **Inconsistent Categories:** Responses like “Agree”, “agree”, or “Strongly Agree”  
- **Categorical Complexity:** Some questions allow multiple answers  
- **Noise:** Some responses may not be accurate or realistic  
- **Imbalance:** Majority of responses may favor one category (e.g., Agree)  

These issues must be handled during preprocessing.

---

## **5. Learning Type (Supervised vs. Unsupervised)**

This is a **Supervised Learning problem** because:

- A clear **label (AI_Impact)** exists  
- The model learns relationships between features and the label  
- The goal is to predict whether a person believes A.I will have a significant impact  

---

## **6. Use Case in Machine Learning**

This dataset can be used for:

- **Classification:** Predict whether a person agrees or disagrees about A.I impact  
- **Public Opinion Analysis:** Understand attitudes toward A.I  
- **Policy Insights:** Help decision-makers understand public concerns  

---

## **7. Role in Data Science Lifecycle**

This dataset fits into the Data Science lifecycle as follows:

1. **Problem Definition** – Understand public perception of A.I  
2. **Data Collection** – Survey responses from participants  
3. **Data Cleaning & Preprocessing** – Handle missing values and encode categorical data  
4. **Modeling** – Apply classification algorithms  
5. **Evaluation** – Measure model performance  
6. **Deployment** – Use insights for decision-making or research  

---
