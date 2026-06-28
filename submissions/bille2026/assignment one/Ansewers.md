# 1.	Define Data Science and Machine Learning ?
•	Data Science is a multidisciplinary field focused on extracting insights from data, while Machine Learning is a subset of artificial intelligence that enables systems to learn from data and make predictions.
# 2.	What is the relationship between them ?
•	While Data Science and Machine Learning are related, they serve different purposes. Data Science is broader and encompasses the entire process of data analysis, including data preparation, exploration, and visualization. In contrast, Machine Learning specifically focuses on creating predictive models and algorithms that learn from data. Essentially, Machine Learning is a tool used within the broader framework of Data Science to derive insights and make predictions
# 3.Use a real-life example to illustrate how they work together ?
•	Real-Life Application: You hire a data scientist to explore your sales data. They find that customers tend to buy more cappuccinos on rainy days, and your peak hours are between 8-10 AM.
•	Outcome: Based on these insights, you can plan promotions or adjust your coffee shop's hours to align with customer behavior. Data Science helps you understand what’s happening and identify patterns.

•	Real-Life Application: Now that you know cappuccinos sell well on rainy days, you decide to train a machine learning model. Using past weather and sales data, your ML model learns the relationship between weather patterns and sales.
•	Outcome: With the ML model, you can now predict how many cappuccinos you’ll sell if it rains next Tuesday. This helps you manage inventory, staffing, and marketing ahead of time.
# 4. The Data Science lifecycle is a systematic process that transforms raw data into actionable insights and deployed solutions. It typically includes seven key stages:
Data Science Lifecycle Stages

Stage	Description
1. Problem Definition (Business Understanding)	Clearly define and comprehend the problem you aim to address, understanding the business goal towardsdatascience+1
2. Data Investigation & Collection	Identify what data is available/needed, gather all accessible data sources datascience-pm+1
3. Data Cleaning & Preparation	Clean data, handle missing values, treat inaccuracies, remove outliers, integrate datasets, create new features datascience-pm+1
4. Exploratory Data Analysis (EDA)	Analyze data to understand patterns, features, and relationships affecting the problem before building models youtuberoadmap

5. Model Development (Data Modeling)	Experiment with Machine Learning algorithms and statistical models to determine the best approach roadmap+1
6. Model Evaluation	Test the model on unseen data using evaluation metrics to check if it's ready for deployment geeksforgeeks+1
7. Deployment & Maintenance	Deploy the model into production and ensure it operates effectively, with ongoing monitoring and enhancements towardsdatascience+1

Machine Learning typically fits in Stage 5 (Model Development), with its lifecycle spanning Stages 5-6 as well.
Why?

Reason	Explanation
Core purpose	ML algorithms are specifically designed to develop predictive models that take prepared data as input and produce output predictions geeksforgeeks+1
Bridges EDA to deployment	ML modeling bridges insights gained during EDA with actionable predictions used in deployment roadmap

Requires prepared data	ML models need clean, prepared data from Stage 3 as input, and their output must be evaluated in Stage 6 geeksforgeeks+1
Experimental phase	This stage involves experimenting with various ML algorithms to find the best approach for the defined problem roadmap




# 5.Compare Supervised Learning and Unsupervised Learning, giving an example of each

•	Supervised learning uses labeled data to predict outcomes, while unsupervised learning uses unlabeled data to discover patterns.
Example of Supervised Learning 
•	Credit Card Fraud Detection: Predicting whether a transaction is fraudulent using historical labeled transaction data  
•	House Price Prediction: Estimating property prices based on features like size, location, and number of bedrooms 

•	Example of Unsupervised Learning
•	Customer Segmentation: Grouping customers based on purchasing behavior to identify market segments 
•	Market Basket Analysis: Discovering products that are frequently bought together, useful for recommendation systems

# 6. What causes Overfitting? How can it be prevented?
•	Overfitting occurs when a machine learning model memorizes the training data instead of learning general patterns that apply to new data. This typically happens due to several factors:
Insufficient Training Data: Small datasets provide limited examples, causing the model to treat random variations as important patterns
Noisy Data or Outliers: Errors or unusual values in the dataset can mislead the model into learning irrelevant patterns
Excessive Training: Training for too many epochs, especially in neural networks, allows the model to gradually memorize the training set
# 7. Explain how training data and test data are split, and why this process is necessary.
The process of splitting training and test data is essential in machine learning to ensure that the model does not overfit to the training data and can generalize well to unseen data. Here's how the data is typically split:
•	Training Data: This is the dataset used to train the model, where the model learns patterns and relationships from the data. It usually consists of labeled examples, where the correct output is known.
•	Test Data: This is used to evaluate the model's performance on unseen data. It helps to measure the model's accuracy and generalization ability.
The split is often done in a 70-20 ratio, with 70% for training and 20% for testing. This ratio is a common practice, but it can vary based on the dataset size, complexity of the problem, and characteristics of the model being used.
The necessity of this process lies in the model's ability to learn from the training data and then apply this knowledge to new, unseen data. By using the test data, the model can be evaluated on real-world data, ensuring that it provides consistent and reliable results in production scenarios. Properly split datasets are crucial for the successful development and evaluation of machine learning models.





# 8. Find one case study (research paper or article) that explains how Data Science or Machine Learning has been applied in healthcare, business, or transportation. Summarize its findings and identify which part of the Data Science lifecycle it covers.
•	🧠 1. Summary of the Case Study
•	This study applied Machine Learning (ML) on Electronic Health Records (EHR) from COVID-19 patients to predict important health outcomes.
•	🎯 Goals:
•	The model was built to predict:
•	Whether a patient will test positive for COVID-19 
•	Whether a patient will need ventilation 
•	Risk of death 
•	Length of hospital stay 
•	Length of ICU stay 
•	________________________________________
•	⚙️ Methods Used:
•	Machine Learning models trained on hospital data 
•	Analysis of patient medical records 
•	Feature interaction analysis (finding important risk factors) 
•	________________________________________
•	📊 Key Findings:
•	The ML models achieved high accuracy (up to 99% AUC in some predictions) 
•	The system successfully identified important risk factors, such as: 
•	Blood biomarkers 
•	Age-related health interactions 
•	It showed ML can support clinical decision-making in real time 
•	________________________________________
•	🏥 2. Real-World Impact
•	The model was integrated into a decision support system, meaning:
•	👉 Doctors can use it to help decide:
•	Who needs ICU care 
•	Who is at high risk 
•	How to allocate hospital resources 
•	________________________________________
•	🔄 3. Data Science Lifecycle Coverage
•	This case study covers almost the full Data Science lifecycle:
•	1. 🧩 Problem Definition
•	Predict COVID-19 outcomes (death, ICU, ventilation) 
•	2. 📊 Data Collection
•	Electronic Health Records (EHR) from hospitals 
•	3. 🧹 Data Preprocessing
•	Cleaning medical records 
•	Selecting relevant features 
•	4. 🔍 EDA (Exploratory Data Analysis)
•	Studying patterns in patient data 
•	Identifying risk factors 
•	5. 🤖 Model Building
•	Training ML models for prediction 
•	6. 📈 Evaluation
•	Measuring accuracy, AUC, and performance 
•	7. 🚀 Deployment
•	Integrated into a clinical decision support tool 


# References
https://www.geeksforgeeks.org/machine-learning/machine-learning-lifecycle/
https://www.analyticsinsight.net/data-science/best-power-bi-competitors-in-2026-10-modern-bi-tools-explained
https://link.springer.com/article/10.1007/s12553-024-00861-8









