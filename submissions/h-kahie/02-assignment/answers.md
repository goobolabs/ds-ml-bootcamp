# Practical Assignment: Data Foundations for Machine Learning

**Subject:** Data Foundations for Machine Learning (Lessons 1–3)  
**Topic:** University Student Dataset  

---

## 1. Title & Collection Method
* **Project Title:** Predicting University Students' GPA Based on Daily Habits.
* **Collection Method:** I collected this dataset myself using an online survey (Google Forms). I shared the link in university WhatsApp and Telegram groups. Exactly 50 students answered the questions, providing real-world data about their studies and daily lives.

## 2. Description of Features & Labels
In Machine Learning, we need inputs to predict an output. Here is how my dataset is divided:

**The Inputs / Features (X):**
* **Faculty:** The department the student belongs to (e.g., Computer Science, Business).
* **Semester:** The student's current semester (1 to 8).
* **Study_Hours:** How many hours they study per day.
* **Daily_Expense_USD:** How much money they spend daily.
* **Has_Job:** Whether they have a part-time job (Yes / No).

**The Output / Label (y):**
* **GPA:** The student’s current Grade Point Average. This is the exact value we want our Machine Learning model to predict.

## 3. Dataset Structure
* **Total Rows (Samples):** 50 rows.
* **Total Columns:** 6 columns (5 features + 1 label).

### Sample Table (First 7 Rows of Raw Data)
Here is a small sample of the actual data I collected. It shows exactly how the students typed their answers:

| Faculty | Semester | Study_Hours | Daily_Expense_USD | Has_Job | GPA |
|---|---|---|---|---|---|
| Computer Science | 4 | 3 | 2 | No | 2.94 |
| Account and finance | 2 | 3 | 2.5 | Yes | A |
| Computer Science | 1 | 2 hours | Wxba 0.5ka khadka oo kliya 😂 | No | Dhibco dhexe |
| Social work | 4 | 2 hours | *[Blank]* | Yes | *[Blank]* |
| Social work | 2 | I study 4 hours per day | 3 USD | No | 4 |
| Computer Science | 3 | 12 | $6 | Yes | $500 |
| Computer Science | 2 | 6hours | 1 dollars | No | I don’t know |

## 4. Data Quality Issues (To be cleaned in Lesson 4)
Because this is real data from real people, it is very messy. Here are the quality issues I found that need preprocessing:
1.  **Text mixed with numbers:** Instead of just writing "2", students wrote `"2 hours"` or `"5 saacadood"`. A computer only understands numbers, so the text needs to be removed.
2.  **Jokes and Unclear Answers:** One student wrote *"Wxba 0.5ka khadka oo kliya 😂"* for expenses, and another wrote *"I don't know"* for GPA. We need to drop or replace these.
3.  **Missing Values:** Some students left the GPA or Expense questions blank.
4.  **Wrong Data Types:** GPA should be a number (like 3.5), but some students wrote letters like `"A"` or `"passed"`.

## 5. Learning Type
This dataset requires **Supervised Learning**.
* **Justification:** Supervised learning is used when we know the answer we are looking for. Because my dataset has a clear target variable / label (y), which is the **GPA**, we can train an algorithm to learn the relationship between the students' habits (X) and their GPA (y). 

## 6. Machine Learning Use Case & Lifecycle
* **Use Case:** This is a **Regression** problem. Regression is used to predict continuous numbers. Since we are trying to predict a student's exact GPA score (e.g., 3.2 or 3.8), a regression model (like Linear Regression) would be the best fit.
* **Data Science Lifecycle:** This assignment fits perfectly into the **Data Collection** phase of the Data Science lifecycle (Lesson 1). The next step (Lesson 4) will be **Data Preprocessing**, where we clean the messy strings, handle the missing values, and prepare the dataset for the model.
