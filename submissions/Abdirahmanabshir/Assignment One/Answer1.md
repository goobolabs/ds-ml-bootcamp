##### Queastion1:

### Data Science
 is the process of collecting, cleaning, analysing, and interpreting large amounts of data to extract meaningful insights that can guide real-world decisions. It combines statistics, programming, and domain knowledge to make sense of raw data.

### Machine Learning
 is a branch of Artificial Intelligence where algorithms are trained on data to recognise patterns and make predictions or decisions without being explicitly programmed for each task.

### The relationship between them is:
 that Machine Learning is one of the key tools used within Data Science. Data Science is the broader field that asks the questions and frames the problems, while Machine Learning provides the predictive power to answer them.

### Example: 
In a supermarket, Data Science might reveal that a certain product sells more on weekends by analysing historical sales data. Machine Learning then goes a step further by building a model that predicts when that product is likely to run out of stock, allowing the store to reorder automatically before shelves go empty.


#### Question 2: Describe the Data Science lifecycle. At which stage does Machine Learning fit in?

### The Data Science lifecycle follows these stages:

- Problem Definition – Identifying the business question or problem to solve
- Data Collection – Gathering relevant data from various sources
- Data Cleaning – Removing errors, duplicates, and inconsistencies from the data
- Exploratory Data Analysis (EDA) – Visualising and summarising the data to understand patterns
- Feature Engineering – Selecting and transforming variables to improve model performance
- Modelling – Building and training machine learning or statistical models
- Evaluation – Testing how well the model performs using metrics like accuracy or error rate
- Deployment & Communication – Putting the model into production and sharing findings with stakeholders

Machine Learning fits in primarily at the Modelling stage. This is where the patterns discovered during EDA are used to train algorithms that can make predictions. However, ML also influences Feature Engineering, since the choice of features directly affects how well a model learns.

#### Question 3: Compare Supervised and Unsupervised Learning


### Supervised Learning 
is a type of machine learning where the model is trained on labelled data — meaning both the input and the expected output are already known. The model learns by comparing its predictions to the correct answers and adjusting accordingly.
 Example: Predicting house prices based on features like size, location, and number of rooms. The training data includes houses with known prices, so the model learns the relationship between those features and the price.
### Unsupervised Learning
 is where the model is given data with no labels — the output is unknown. Instead of predicting a specific value, the model looks for hidden patterns or natural groupings within the data.
 ### Example: 
 Analysing customer purchasing behaviour without any predefined categories. The model might group customers into segments such as "frequent buyers," "seasonal shoppers," and "one-time buyers," which the business can then use for targeted marketing.




#### Question 4: What causes Overfitting? How can it be prevented?


Overfitting occurs when a model learns the training data too well — including its noise and random fluctuations — to the point where it performs excellently on training data but poorly on new, unseen data. Essentially, the model memorises rather than generalises.

### Causes of overfitting:

Excessive model complexity – Using a model with too many parameters relative to the amount of data
Over-training – Training the model for too many iterations
Insufficient training data – Too little data means the model picks up on noise rather than true patterns
Noise and outliers – Irregular data points that mislead the model
Prevention methods (consider adding these to strengthen your answer):
Using cross-validation to test the model on multiple data splits
Applying regularisation techniques (like L1/L2) to penalise complexity
Simplifying the model by reducing the number of features or layers
Collecting more training data
Using early stopping during training

#### Question 5: Explain how training and test data are split, and why it is necessary


When building a machine learning model, the available dataset is typically split into two portions — a training set and a test set. A common split ratio is 80% for training and 20% for testing, though 70/30 is also widely used.

The training set is used to teach the model by exposing it to patterns in the data. The test set is kept completely separate and is only used after training to evaluate how well the model performs on data it has never seen before.

#### This process is necessary for two key reasons:

To get a fair and honest measure of performance – If we tested on the same data we trained on, the model would score very high simply because it has already seen the answers, which would be misleading.

To detect overfitting – A big gap between training accuracy and test accuracy is a strong signal that the model has overfit and won't generalise well to real-world data.

#### Question 6: Case Study Summary

### Case Study: American Express – Machine Learning for Fraud Detection

American Express (AmEx) implemented a machine learning-based fraud detection system to identify suspicious transactions in real time across millions of daily card transactions worldwide.

The system was built using a combination of Gradient Boosting Machines (GBMs) and Long Short-Term Memory (LSTM) neural networks, trained on over 1,000 data signals per transaction — including purchase location, merchant category, transaction time, and historical spending patterns.

The model runs within 2 milliseconds per transaction, allowing fraud decisions to be made instantly at the point of sale without disrupting the customer experience.

### Data Science Lifecycle stages covered:

Feature Engineering – Over 1,000 variables were carefully engineered from raw transaction data
Modelling – Multiple ML algorithms were combined for higher accuracy
Deployment & Operations – The model was deployed at scale in a real-time production environment

#### Here is the reference link for the research:
https://www.techbrew.com/stories/2021/03/10/amexs-fraud-detection-ai-ready-go-live-covid-hit


