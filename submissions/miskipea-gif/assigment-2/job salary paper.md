
Jobs and Salary Levels in Somalia
                 A Machine Learning Dataset Research Paper


Project Goal
The goal of this assignment is to collect an original dataset and explain how it can be used in a Machine Learning project. The dataset focuses on job listings and salary levels across major Somali cities and follows the requirements of the Data Science assignment.

Dataset Collection
The dataset was collected through direct observation and manual logging. Job information was gathered by visiting local businesses, reviewing job postings shared through WhatsApp and Telegram groups, and conducting short interviews with HR contacts at NGOs, hospitals, technology companies, and government offices across Mogadishu and Hargeisa.

Dataset Summary
Collection Method: Direct Observation, Job Postings, and Interviews
Distribution Cities: Mogadishu, Hargeisa, Bosaso, Kismayo, Galkayo, Baidoa
Total Records (Samples): 60
Total Columns: 11
Assignment Requirement: At least 50 samples and at least 5 features ✔️

Features (X)
The dataset contains the following input features:

•	Job Title
•	Industry
•	Experience Required (Years)
•	Education Level
•	Location (City)
•	Job Type
•	Company Size
•	Remote Option
•	Monthly Salary (USD)

Label (y)
Salary Category (Low / Mid / High)

This variable is used as the target label for the machine learning model. It was derived by comparing each job's monthly salary against typical compensation norms for that role type and industry within the Somali labour market.

Dataset Structure
Rows (Samples): 60
Columns: 11

Each row represents one job listing, while each column represents one variable collected during the observation process. The dataset covers a wide range of roles from informal self-employed workers such as street vendors and farmers to highly skilled professionals such as doctors, engineers, and data scientists.

Sample Dataset

Job Title	Industry	Exp (yrs)	Education	Location	Job Type	Company Size	Remote	Salary (USD)	Category
Data Analyst	Technology	2	University	Mogadishu	Full-time	Large	Yes	850	Mid
Teacher	Education	2	University	Hargeisa	Full-time	Medium	No	320	Low
Software Engineer	Technology	4	University	Mogadishu	Full-time	Large	Yes	1100	High
Doctor	Healthcare	6	University	Mogadishu	Full-time	Large	No	1800	High
Street Vendor	Retail	0	Primary	Mogadishu	Self-employed	Small	No	90	Low
NGO Worker	Humanitarian	3	University	Mogadishu	Full-time	Large	No	950	High
Farmer	Agriculture	0	Primary	Kismayo	Self-employed	Small	No	120	Low
Nurse	Healthcare	2	University	Hargeisa	Full-time	Medium	No	380	Mid
Camel Trader	Agriculture	0	Primary	Galkayo	Self-employed	Small	No	300	Low
Data Scientist	Technology	5	University	Mogadishu	Full-time	Large	Yes	1400	High

The table above shows only a small sample of the dataset.

Quality Issues
Possible quality issues in the dataset include:

•	Class imbalance — Low category has more rows than Mid and High
•	Categorical columns require encoding before modelling
•	Ordinal columns (education level, company size) need ordered mapping
•	Numeric columns (experience, salary) are on different scales and require normalisation
•	High cardinality in job_title column (60 unique values)

These issues can be addressed during the data preprocessing stage.

Learning Type
This dataset is suitable for Supervised Learning because it contains input features (X) and a clearly defined target label (y).

Machine Learning Task
Classification

The model can be trained to classify each job listing into one of three salary categories: Low, Mid, or High, based on the job's characteristics such as industry, required experience, education level, city, and company size.

Use Case
This dataset can be used to build a Machine Learning classification model that predicts the salary category of a job listing in Somalia. It can also be used to analyse how factors such as industry, education level, city, and remote availability relate to salary levels in the Somali labour market.

Data Science Lifecycle
This dataset follows the early stages of the Data Science lifecycle:

1.	Problem Definition
2.	Data Collection (Observation, Job Postings, Interviews)
3.	Data Cleaning and Preprocessing
4.	Exploratory Data Analysis (EDA)
5.	Machine Learning Model Building (Classification)
6.	Model Evaluation

Repository Contents
•	  – Project description and dataset documentation.README.md
•	  – Dataset collected through observation and job postings.somalia_jobs_salary.csv


