# Final Project Proposal

## 1. Certificate Name: 
**Abdisemed Abdi Gure**

---

## 2. Project Title and Description
**Title**: *"The Impact of Generative Artificial Intelligence on Students' Academic Performance and Well-being"*

Nowadays the impact of Artificial Intellegency (Ai) on students has become a widely discussed topic, with debates focusing on both its positive and negative effects. Although AI help us to improve learning effeciency and increase our productivity, on the other hand, it can reduce critical thinking, increase stress and lower knowledge retension and can bring overdependency.
In this project, I will use machine learning techniques to analyze students data and train different models to predict how AI usage influence students' Academic Performance and Well-being.
Finally, the findings will help to understand the key factors associated with positive and nagative outcomes and provide insights that help students, educators, and educational institutions to promote resposible AI use.

---


## 3. Problem Type

**Regression** - Continuous Output: Post_Semester_GPA.

The target column is `Post_Semester_GPA`. This is a supervised Learning problem because the model is trained using a historical student data where the *Post_semester_GPA* is already known. The goal is to predict students' performance based on factors such as: (AI usage, study habit, etc)

**Clustering** - Grouped Output

I will use *Clustering* as an unsupervised learning technique to group students with AI usage patterns and learning behaviors. Since the *Clustering* doesn't want target variable it helps us to identify hidden patterns to provide insights of impacts of students' performance and Well-being.

---

## 4. Dataset

- **Source**: [Impact of Ai on Students](https://www.kaggle.com/datasets/laveshjadon/ai-impact-on-students) (Kaggle).
- **Size**: 5000 rows and 14+ columns.
- **Target**(Regression): *Post_Semester_GPA* students' GPA at the end of the semester.
- **Clustering**: No target variable is use. I will use it to group similar students' AI usage and learning behaviours.
- **Main Features**: 
  - **Major_Category** - student's field of study 
  - **Year_of_Study** - academic year 
  - **Pre_Semester_GPA** - GPA before AI usage 
  - **Post_Semester_GPA** - GPA before AI usage 
  - **Weekly_GenAI_Hours** - hours spent using generative AI each week 
  - **Primary_Use_Case** - main purpose of using AI 
  - **Prompt_Engineering_Skill** - prompt-writing skill level 
  - **Tool_Diversity** - number of different AI tools used 
  - **Paid_Subscription** - whether the student has a paid AI subscription 
  - **Traditional_Study_Hours** - weekly study hours without AI 
  - **Perceived_AI_Dependency** - student's perceived dependence on AI 
  - **Institutional_Policy** - university AI policy 
  - **Anxiety_Level_During_Exams** - exam anxiety level 
  - **Skill_Retention_Score** - score measuring retained knowledge 
  - **Burnout_Risk_Level** - burnout risk (Low, Medium, High) 

- **Preprocessing Plan**: Drop duplicates, fill missing value (although they said in their doc that there are no missing values), encoding categorical features, shrinking Outliers, scaling features the want to and train/test split(80/20).

    - If I complete the main project before the planned deadline, I will add a **classification model** using `Burnout_Risk_Level` as the target variable.

---

## 5. Algorithms I Plan to Train

| **Algorithm**       | **Why it fits**                                  | 
|--------------|---------------------------------------------------|
| Linear Regression | Predicts students' Post_Semester_GPA a continues numeric values,and helps measure how AI usage and study-related factors influence academic performance |
| Decision Tree Regressor | Captures non-linear relationship between AI usage, study habits and GPA making it usefull for comparing linear regression. |
| Random forest Regressor | Improves prediction accuracy by combining multiple decision trees and reduces overfitting, making it suitable for complex educational data. |
| K-Means Clustering | Grouping students with similar AI usage patterns and learning behaviour without requiring target variable, helping identify different student segments. |
| Agglomerative Clustering | Builds clusters by merging the most similar students based on their characteristics, making it useful for discovering natural groupings in AI usage and learning behaviors. |

## 6. Evaluation Plan

- **Metrics for Regression Models**

  - **R² Score** – Measures how well the model explains the variation in students' post-semester GPA.
  - **Mean Absolute Error (MAE)** - Measures the average absolute difference between the predicted and actual GPA.
  - **Root Mean Squared Error (RMSE)** - Measures the prediction error while giving greater weight to larger errors.

*I will use the **R² Score** to select the best regression model because it measures how well the model explains the variation in students' post_semester_GPA. A higher R² score indicates better predictive performance.* 

- **Metrics for Clustering Models**

  - **Silhouette Score** - Measures how well students fit within their assigned clusters.
  - **Davies–Bouldin Index (DBI)** – Evaluates cluster quality by measuring the similarity between clusters. Lower values indicate better clustering.

*I will use the **Silhouette Score** to select the best Clustering model because it measures how well students fit within their assigned clusters. A higher Silhouette Score indicates better-defined and more distinct clusters.* 


## 7. Deployment Sketch

### Framework

I will use **FastAPI** because it is lightweight, fast, and well suited for deploying machine learning models as REST APIs. It also provides automatic API documentation and integrates easily with Python ML libraries.

### `/predict` Endpoint

The `/predict` endpoint will accept a JSON request containing the input features used by the trained model. Example fields include:

```json
{
  "Major_Category": "STEM",
  "Year_of_Study": "Junior",
  "Pre_Semester_GPA": 3.45,
  "Weekly_GenAI_Hours": 6.5,
  "Primary_Use_Case": "Debugging/Troubleshooting",
  "Prompt_Engineering_Skill": "Beginner",
  "Tool_Diversity": 1,
  "Paid_Subscription": false,
  "Traditional_Study_Hours": 14.19,
  "Perceived_AI_Dependency": 4,
  "Institutional_Policy": "Allowed_With_Citation",
  "Anxiety_Level_During_Exams": 5,
  "Post_Semester_GPA": 3.67
}
```

### Response

The API will return the predicted AI impact score generated by the regression model. For example:

```json
{
  "predicted_ai_impact_score": 7.84
}
```

```json
{  
  "cluster_id": 2,
  "cluster_description": "High AI usage with strong academic engagement"
}
```


## 8. Repository Plan

## GitHub Repository Structure

```text
ai-impact-on-students/
│
├── dataset/
│   ├── raw
│   └── processed
│
├── notebooks/
│   ├── data_preprocessing.ipynb
│   ├── regression_model.ipynb
│   ├── clustering_model.ipynb
│   └── model_evaluation.ipynb
│
├── models/
│   ├── regression_model.pkl
│   ├── clustering_model.pkl
│
├── app/
│   ├── main.py
│   ├── predict.py
│   ├── preprocess.py
│
├── reports/
│   ├── final_report.md
│
├── README.md

```


