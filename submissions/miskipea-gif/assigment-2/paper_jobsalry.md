
PRACTICAL ASSIGNMENT
Data Foundations for Machine Learning
Somalia Jobs & Salary Dataset

1. Title & Collection Method
Dataset Title:  Somalia Jobs & Salary Dataset

This dataset documents job listings and their associated salary information across six major cities in Somalia: Mogadishu, Hargeisa, Bosaso, Kismayo, Galkayo, and Baidoa. The dataset was created to capture the relationship between job characteristics — such as industry, required education, experience level, company size, and remote availability — and the resulting monthly salary in USD.

Data was collected through a combination of direct observation and structured manual logging. Job information was gathered by visiting local businesses, reviewing job postings shared on WhatsApp groups and Telegram channels, and interviewing HR contacts at NGOs, hospitals, tech companies, and government offices in Mogadishu and Hargeisa. For each job, eleven fields were recorded covering the role, industry, requirements, and compensation.

The dataset contains 60 rows and 11 columns, including both well-known professional roles (Doctor, Software Engineer, Lawyer) and Somalia-specific occupations (Camel Trader, Fisherman, Port Worker, Midwife, Translator). Salary figures are realistic for the Somali labour market, where monthly pay ranges from approximately $90 USD for informal street vendors to $1,800 USD for senior medical doctors.
2. Description of Features & Labels
The dataset has 11 columns in total: 9 input features (X), 1 numeric salary column that also acts as a supporting feature, and 1 derived categorical label (y). The table below describes every column.

#	Column Name	Type	Role	Description
1	job_id	Numeric	Identifier	Unique row number for each job record (1–60). Not used as a feature.
2	job_title	Categorical	Feature X	Name of the job role (60 distinct titles across 20+ industries).
3	industry	Categorical	Feature X	Sector the job belongs to: Technology, Healthcare, Education, NGO, etc.
4	experience_required_years	Numeric	Feature X	Minimum years of experience required for the job (0–6).
5	education_level	Ordinal	Feature X	Minimum education required: Primary / Secondary / University.
6	location	Categorical	Feature X	Somali city where the job is based (Mogadishu, Hargeisa, Bosaso, Kismayo, Galkayo, Baidoa).
7	job_type	Categorical	Feature X	Employment arrangement: Full-time, Part-time, or Self-employed.
8	company_size	Ordinal	Feature X	Size of the hiring organisation: Small / Medium / Large.
9	remote_option	Binary	Feature X	Whether the job can be done remotely: Yes or No.
10	monthly_salary_usd	Numeric	Feature X	Monthly gross salary in USD. Somalia-realistic range: $90–$1,800.
11	salary_category	Categorical	Label y	Target variable: Low / Mid / High — derived from salary relative to job type and industry norms in Somalia.

Features X (9 inputs):  job_title, industry, experience_required_years, education_level, location, job_type, company_size, remote_option, monthly_salary_usd.
Label y:  salary_category — a three-class categorical variable: Low / Mid / High. Derived by comparing each job’s monthly salary against typical compensation norms for that role type and industry within the Somali labour market.

The salary category thresholds for this dataset are as follows:

Category	Salary Range (USD/month)	Typical Jobs	Count in Dataset
Low	$90 – $350	Street Vendor, Cleaner, Farmer, Cashier, Security Guard, Waiter, Fisherman	26 rows
Mid	$351 – $700	Teacher, Nurse, Accountant, Graphic Designer, Bank Teller, Social Worker	22 rows
High	$701 – $1,800	Doctor, Software Engineer, NGO Worker, Financial Analyst, Cybersecurity Analyst	12 rows

3. Dataset Structure
Dimensions:  60 rows × 11 columns (60 unique job records, no duplicates).
The table below shows 10 representative rows selected from across the dataset to illustrate the variety of job types, salary levels, locations, and categories present.

job_id	job_title	industry	exp_yrs	education	location	job_type	company_size	remote	salary_usd	category
1	Data Analyst	Technology	2	University	Mogadishu	Full-time	Large	Yes	850	Mid
2	Teacher	Education	2	University	Hargeisa	Full-time	Medium	No	320	Low
3	Software Engineer	Technology	4	University	Mogadishu	Full-time	Large	Yes	1100	High
5	Cashier	Retail	0	Secondary	Mogadishu	Part-time	Small	No	150	Low
6	Doctor	Healthcare	6	University	Mogadishu	Full-time	Large	No	1800	High
10	NGO Worker	Humanitarian	3	University	Mogadishu	Full-time	Large	No	950	High
17	Cleaner	Facilities	0	Primary	Mogadishu	Part-time	Small	No	100	Low
29	Farmer	Agriculture	0	Primary	Kismayo	Self-employed	Small	No	120	Low
50	Street Vendor	Retail	0	Primary	Mogadishu	Self-employed	Small	No	90	Low
60	Data Scientist	Technology	5	University	Mogadishu	Full-time	Large	Yes	1400	High

The dataset covers 60 distinct job titles spanning more than 20 industries. Locations are spread across all major Somali regions: Mogadishu (Benadir), Hargeisa (Somaliland), Bosaso (Puntland), Kismayo (Jubaland), Galkayo (Mudug), and Baidoa (South West). Job types include Full-time (42 rows), Part-time (6 rows), and Self-employed (12 rows). Remote work is available for 18 of the 60 roles, primarily in Technology and Creative industries based in Mogadishu.
4. Quality Issues
Unlike the earlier messy version of this dataset, this version was carefully cleaned and standardised during collection. However, several inherent structural challenges are still present that will need to be addressed before machine learning modelling can begin.

•	The Low category dominates with 26 rows (43%), while Mid has 22 rows (37%) and High has only 12 rows (20%). This imbalance could cause a classifier to be biased toward predicting Low. Techniques such as SMOTE oversampling or class-weight adjustment will be needed.Class Imbalance:  
•	Columns such as job_title, industry, location, job_type, company_size, education_level, and remote_option are all stored as text strings. They must be encoded (label encoding or one-hot encoding) before any ML algorithm can process them.Categorical Encoding Required:  
•	education_level (Primary < Secondary < University) and company_size (Small < Medium < Large) are ordinal but stored as plain text. They should be mapped to integers to preserve their natural order during modelling.Ordinal Variables Need Ordering:  
•	experience_required_years (0–6) and monthly_salary_usd (90–1,800) are on very different numeric scales. Standardisation or min-max scaling will be needed so that distance-based models are not dominated by the larger salary values.Feature Scaling Required:  
•	With 60 unique job titles across 60 rows, one-hot encoding this column directly would create 60 binary columns, causing a dimensionality problem. It may be better to group job titles by industry or drop the column in favour of industry alone.High Cardinality in job_title:  
5. Learning Type
Learning Type:  Supervised Learning — Multi-class Classification

This is a supervised learning problem because every row in the dataset has a clearly assigned label y = salary_category (Low, Mid, or High). The label was determined at collection time by comparing each job’s monthly_salary_usd to established compensation norms for that role in Somalia, giving the model a ground truth to learn from.

The problem is multi-class classification specifically because:
•	The output variable salary_category is categorical, not continuous.
•	There are three distinct and ordered classes: Low, Mid, and High.
•	The goal is to predict which salary class a new, unseen job listing belongs to, given its features.

A related but different framing would be regression — predicting the exact monthly_salary_usd value rather than its tier. That would also be supervised learning, but the output would be a continuous number rather than a category. The classification approach was selected here because salary tiers are more directly useful for job seekers and employers who want a quick, interpretable signal rather than a precise dollar figure.
6. Use Case & Data Science Lifecycle
6.1 Machine Learning Use Case
A trained classification model on this dataset could serve several practical purposes within the Somali context:
•	Given a new job posting’s industry, required experience, education level, city, and company size, predict whether the salary will be Low, Mid, or High. This helps job seekers evaluate opportunities quickly.Job salary prediction:  
•	Identify which industries, cities, and company sizes consistently offer High-category salaries in Somalia, giving policymakers and NGOs insight into where skilled labour is being rewarded.Labour market analysis:  
•	Help Somali companies benchmark their salary offers against the dataset to ensure they are competitive within their sector and city.Recruitment support:  
•	Show students which combinations of education level and industry are most likely to lead to Mid or High salary outcomes in Somalia.Education and career guidance:  

Suitable algorithms to evaluate during modelling include Logistic Regression (interpretable baseline), Decision Tree, Random Forest, and Gradient Boosting classifiers such as XGBoost. Feature importance outputs from tree-based models would reveal whether industry, experience_required_years, or location is the strongest predictor of salary category in Somalia.
6.2 Position in the Data Science Lifecycle
As introduced in Lesson 1, the Data Science lifecycle consists of: Problem Definition → Data Collection → Data Preprocessing → Exploratory Data Analysis (EDA) → Modelling → Evaluation → Deployment & Monitoring.

This assignment covers the first two stages in full:
•	Understand what drives salary levels in the Somali labour market and build a model to classify new job listings into salary tiers (Low / Mid / High).Problem Definition:  
•	Manually recorded 60 job listings across 6 Somali cities and 20+ industries, capturing 10 features per job via observation, online postings, and interviews.Data Collection:  


