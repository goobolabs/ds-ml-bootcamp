# Data Science and Machine Learning

## How Data Science and Machine Learning Work Together

Data Science is a field in science that deals with the study of data and also the process of collecting, storing, processing, cleaning and analyzing complex data to extract a meaningful information to support better decision-making.

###### In simple way, data science is the process of converting raw data into meaningful information by using mathematics, technology and analyzing technique.

Machine Learning  is a subset of artificial intelligence that enables systems to learn from data and improve from experience without being explicitly programmed.
Instead of hard-coded instructions, ML uses algorithms to identify patterns in historical data and make accurate predictions or decisions on new, unseen data.
Data Science and Machine Learning are closely related fields that work together to solve problems and make better decisions from data.
Data Science prepares and analyzes the data, while Machine Learning uses that data to build predictive models.
Data Science lifecycle
The Data Science Lifecycle is a structured process used to transform raw data into valuable insights and solutions. It consists of 8 phases from identifying problem to deployment.
1.	Identifying Problem
-	Before any other task, data scientists must know what problem should they want to solve to reach remarkable solutions. So this stage focuses to knowing the problem to be solved.
-	For-example, the government want to know the causes of the subsequent droughts in the country.
2.	Collecting data 
-	After the government identified the problem scope, it must collects data from all of the regions to gain the answer of what causes continuous droughts. 
-	For-example, data about rainfall, temperature, soil moisture, water levels, and agricultural activity.

3.	Data cleaning
-	after the data has been collected, it must be turn into information to be ready to understand.
-	For-example, to remove the data from duplications, to organize it and to categorize like every region’s temperature, rainfall, soil moisture information like this, to get quick understand.
4.	Exploratory data Analysis
-	after data is been cleaned, it must be analyzed and visualized to understand its main characteristics and how the variables are inter-connected to know if one variable is chanced what occur to the other.
-	For-example, during this stage, data is interpreted into making bar graphs, pi charts, Histograms or even Scatter plots, and now we can understand which regions gets higher temperature and rainfall and which gets lower.
5.	Feature engineering
-	After data is being visualized, it must be prepared a way in which machine learning models can understand and make more accurate predictions.
-	 For-example, The government collects raw data such as: Rainfall (mm), Temperature (°C), Soil moisture, so during feature engineering, government may create better features like : average temperature over time, Rainfall Deficit, number of consecutive days without rain and even, the government can conduct Drought Risk Score, which comes from the combination indicator from all factors.
6.	Model Building
-	This is a stage in the Data Science lifecycle where we use machine learning algorithms to train a model that can learn patterns from data and make predictions or decisions. 
-	For-example, the government will build models and train them to the previous collected and interpreted data to predict future climatic changes.
7.	Model evaluation
-	During this process, we will test how well a previous trained machine learning model performs before it is used in the real world.
-	For-example, The government tests the drought prediction model using new data, the model predicts which regions will face drought then the government compare this data with real drought occurrences, so if the model correctly predicts most drought areas, it is considered good.
8.	Model Deployment
-	Within this stage, we will the making the model available for real use.
-	For-example, the model will be deployed to the national monitoring system.
Within all this staged, Machine Learning typically fit in: 
Model Building stages because it relies on the clean, prepared, and analyzed data produced during the earlier stages of the Data Science Lifecycle.
Supervised Learning and Unsupervised Learning
1.	Supervised Learning: is when a model is trained using data that already has known its results (answer).
-	For-example, The government uses past climate data where it is already known whether a drought happened or not in each region. The model is taught using past drought examples where the answers are already known, so it can predict future droughts.
			
Rainfall	Temperature	Soil Moisture	Answer (Label)
Low	High	Low	Drought (Yes)
High	Moderate	High	No Drought (No)
-	The dataset might look like this:

-	🧠 Simple idea:
The model is already told in past data whether drought happened or not, so it learns the pattern.

2.	Unsupervised Learning:
-	It is when a model learns from data that has no correct answers or labels attached to it.
-	For-example, The government collects data like: Rainfall ,Temperature, Soil moisture and Groundwater levels , but there is NO column saying “Drought = Yes or No”.
-	🧠 the idea:
The model tries to: Find patterns in the data , group similar regions together and detect hidden structures for-example, it may discover:
•	Group 1: very dry regions (high drought risk) 
•	Group 2: normal regions 
•	Group 3: wet regions
Simple Meaning:
The model learns without answers and tries to discover patterns or groups in the data.
What causes Overfitting?
Overfitting happens when a machine learning model learns the training data too well, including noise and small random details, instead of learning the general pattern.
As a result, the model performs very well on training data but poorly on new (test) data.
Main causes of Overfitting:
1.	Too complex model
-  The model is too advanced and learns too many details. 
2.	Small training dataset
-  There is not enough data for the model to learn properly. 
3.	Noisy data
-  The data has mistakes, strange values, or useless information. 
4.	Training for too long
- The model keeps memorizing the training data instead of learning general patterns. 
5.	Irrelevant features
- The data includes unnecessary information that confuses the model. 
How can Overfitting be prevented?
1. Use more training data
•	More data helps the model learn general patterns instead of memorizing 
2. Simplify the model
•	Use less complex models (e.g., limit depth of decision trees) 
3. Cross-validation
•	Test the model on different subsets of data to ensure it generalizes well 
4. Regularization
•	Adds a penalty for complexity (e.g., L1 or L2 regularization) 
5. Early stopping
•	Stop training when performance on validation data starts to get worse 
6. Feature selection
•	Remove unnecessary or irrelevant features 
Simple Example
A model learns exam questions by memorizing answers instead of understanding concepts.
•	It scores 100% in practice exams (training data) 
•	But fails in the real exam (new data) 
👉 This is overfitting.




















