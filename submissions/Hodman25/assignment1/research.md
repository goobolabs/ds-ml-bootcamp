# Research Assignment: Introduction to Data Science and Machine Learning



1.Define Data Science and Machine Learning. What is the relationship between them? Use a real-life example to illustrate how they work together.
-------------------------------------------------------------------------------------------
Ans. 

## definition of  Data Science:
 is the study of data used to extract meaningful insights for business decisions. It combines mathematics, computing and domain knowledge to solve real-world problems and uncover hidden patterns. 
 It processes raw data to address business challenges and predict future trends.

 ### For example
  from large company datasets, data science can help answer questions like:
  - What do customer want?
  - How can we improve our services?
  - What will the upcoming trend in sales?
  - How much stock they need for upcoming festival.

## definition of Machine Learning.
Machine learning is the subset of artificial intelligence (AI) focused on algorithms that can “learn” the patterns of training data and, subsequently, make accurate inferences about new data. This pattern recognition ability enables machine learning models to make decisions or predictions without explicit, hard-coded instructions.
#### In simple words,  ML teaches systems to think and understand like humans by learning from the data.

# What is the relationship between them
The terms Data Science and Machine Learning are often used interchangeably, but they actually refer to different fields. While Machine Learning is a subset of Artificial Intelligence that focuses on algorithms for prediction, Data Science is a broader domain that encompasses the entire process of extracting insights from data.


### Data Science vs. Machine Learning

Let's see the difference between data science and machine learning,

| Aspect | Data Science | Machine Learning |
|--------|--------------|------------------|
|Scope & Application | Broad covers data collection, cleaning, analysis, visualization and modeling | Narrower focuses only on building predictive models |
| Techniques  | Statistics, data analysis, visualization, ML, business intelligence | Algorithms like regression, decision trees, clustering, neural networks |
| Goal | 	Extract insights and support decision-making | Automate predictions and pattern recognition |
| Output | Reports, dashboards, insights, models | Predictive or classification models |


###  Real-Life Example: Weather Forecasting:
#### Data Science

Meteorologists and data scientists collect huge amounts of data from:
- Weather stations
- Satellites
- Radar systems
- Ocean sensors
- Historical weather records

They clean and organize the data and analyze trends such as:

- Temperature changes
- Humidity levels
- Wind speed
- Air pressure

####  Machine Learning

Machine learning models are trained using years of weather data.
The models learn patterns like:
- Certain pressure patterns often lead to rain.
- Specific temperature and humidity combinations may indicate storms.
- Wind patterns can help predict future weather conditions.

# 2.Describe the Data Science lifecycle (from problem definition to deployment). At which stage does Machine Learning typically fit in, and why?


## Problem Definition
Every data science project begins with a clear definition of the problem to be solved. This involves collaborating with key stakeholders to identify objectives and desired outcomes. Data scientists must understand the context and scope of the project to ensure that the goals align with business or research needs.

## Data Collection
In the data collection phase, data scientists and data engineers work together and gather relevant data from diverse data sources. This includes both structured and unstructured data, such as historical records, new data, or data streams.

## Data Preparation
This stage addresses the quality of raw data by cleaning and organizing it for analysis. Tasks such as treating inaccurate data, handling missing values, and converting raw data into usable formats are central to this stage. This stage prepares the data for further and more detailed analysis.

## Exploratory Data Analysis (EDA)
The exploratory data analysis stage is where the “data processing” happens. This stage focuses on uncovering patterns, trends, and relationships within the data. Through data visualization techniques such as bar graphs and statistical models, data scientists perform a thorough data analysis and gain insights into the data’s structure and characteristics.

## Model Building and Evaluation
The model-building phase involves developing predictive or machine learning models tailored to the defined problem. Data scientists experiment with various machine learning algorithms and statistical models to determine the best approach. 

## Deployment and Monitoring
The final stage of this generic data science lifecycle involves deploying the model into a production environment. Here, data scientists, machine learning engineers, and quality assurance teams ensure that the model operates effectively within existing software systems. 


# 3.Compare Supervised Learning and Unsupervised Learning, giving an example of each.

## what is Supervised Learning:-
Supervised Learning is the machine learning approach defined by its use of labeled datasets to train algorithms to classify data and predict outcomes.

##### example of supervised learnig :- email spam filtering 

## what is UnSupervised Learning:-
Unsupervised Learning is a type of machine learning in which the algorithms are provided with data that does not contain any labels or explicit instructions on what to do with it. 

##### example of Unsupervised learnig :- customer segmentation in marketing,

# 4.What causes Overfitting? How can it be prevented?

## Causes of Overfitting
Overfitting occurs when a machine learning model learns the training data too well.

* Complexity of the Model: Using a model that is too complex for the given dataset can lead to overfitting. 
* Insufficient Training Data: When the training dataset is small, the model may memorize the training examples instead of learning the underlying patterns, resulting in overfitting.
* Lack of Regularization: Without regularization techniques such as L1 or L2 regularization, the model may overfit by fitting the training data too closely.

## How Can Overfitting Be Prevented?
To avoid overfitting, several strategies can be employed:
- Cross-Validation
- Feature Selection
- Regularization
- Early Stopping
- Simpler Models


# 5.Explain how training data and test data are split, and why this process is necessary.

Training Set:  consists of data that forms the foundation for machine learning models. This dataset is used during the “learning” process of the model and provides the fundamental data needed to optimize the model’s parameters.

Test Set:  is used in the final and most critical evaluation phase of the model.

### A common split is:
- 80% Training Data
- 20% Test Data

## Why is this process necessary?
* Evaluates Model Performance
* Detects Overfitting
* Measures Generalization
* Provides Fair Evaluation

# 6. Find one case study (research paper or article) that explains how Data Science or Machine Learning has been applied in healthcare, business, or transportation. Summarize its findings and identify which part of the Data Science lifecycle it covers.


## Case Study (Healthcare): Machine Learning
A well-known healthcare case study is “Machine Learning for Early Sepsis Detection using Electronic Health Records” (used in several hospital-based research projects, including studies published in medical informatics journals).

### How Machine Learning was Applied
Researchers used Electronic Health Records (EHRs) from hospital patients to build a machine learning model that can:

- Monitor patient vital signs (temperature, heart rate, blood pressure, etc.)
- Detect hidden patterns that may lead to sepsis
- Predict sepsis hours before symptoms become severe
The model was trained on thousands of patient records using historical hospital data.

### Findings
- The ML model could detect early signs of sepsis earlier than doctors in many cases
- It improved early warning accuracy compared to traditional clinical scoring systems
- Early prediction helped hospitals:
    - Start treatment faster
    - Reduce patient mortality risk
    - Improve ICU decision-making

## Data Science Lifecycle Stages Covered
1. Data Collection: Patient data was collected from hospital electronic health records (EHRs).
2. Data Preparation: Data was cleaned, organized, and missing values handled.
3. Model Building: A machine learning model was trained to predict sepsis risk.
4. Model Evaluation: The model was tested using unseen patient data to measure accuracy.
5. Deployment: The model was used in hospitals to help doctors detect sepsis early.




## Summary
This healthcare case study shows how Machine Learning is used to analyze patient medical data and predict diseases like sepsis early. It improves diagnosis speed, supports doctors, and can save lives by enabling early treatment.



# Refference

### geeksforgeeks
### roadmap.sh
### v7labs,
### studocu,
### ruveydakardelcetin.medium,
### Datavid,
### Kaggle,
### IBM



