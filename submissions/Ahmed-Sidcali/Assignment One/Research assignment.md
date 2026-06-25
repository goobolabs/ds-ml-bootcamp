# Research assignment in data science and machine learning 

## 1. Define data science and machine leaning 
* **Data science**: combines math and statistics, specialized programming, advanced analytics, artificial inteligence (AI) and machine learning with specific subject matter expertise to uncover actionable insights hidden in an organization's data.
* **Machine learning**: is the subset of artificial intelligence (AI) focused on algorithms that can "learn" the patterns of training data and, subsequently, make accurate inferences about new data.

### Relationship
* Data science involves studying and extracting meaning from data, whereas machine learning utilizes data to improve performance or inform predictions.

### Real-life examples 
* **Data science**: *Banking and finance* You can use data science tools to analyse the past performance of financial products, like stocks or managed funds, to make predictions about how those assets will perform, providing valuable data to drive decisions.
* **Machine learning**: *Vertual personal assistance* Virtual personal assistants are devices you might have in your own home, such as Amazon Alexa, Google Home, or the Apple iPhone’s Siri. These devices use a combination of speech recognition technology and machine learning to capture data on what you're requesting and how often the device is accurate in its delivery. They detect when you start speaking and what you’re saying, and then deliver on the command.

---

## 2. Data science lifecycle 
* **1. Problem definition**: Outlines business goals, defines project objectives, and determines if a predictive or analytical solution is required.
* **2. Data collection**:  Aggregates raw, unstructured, or structured data from relevant sources such as APIs, databases, and logs.
* **3. Data cleaning and processing**: Identifies and resolves missing values, duplicates, and formatting inconsistencies to ensure high-quality, reliable data.
* **4. Explanatory Data Analysis  (EDA)**: Analyzes the data using visual charts and summary statistics to uncover hidden patterns and relationships.
* **5. Feature Engineering**: Transforms and selects the most relevant data variables to enhance the efficiency and predictive power of the model.
* **6. Modeling (Machine Learning)**: Trains and tunes chosen algorithms (like regression, neural networks, or decision trees) to recognize patterns and make predictions.
* **7. Evaluation**: Tests the model's performance against predefined metrics (e.g., accuracy, precision, recall) to ensure it performs reliably before it is released.
* **8. Deployment & Monitoring**: Puts the model into a live production environment (often using APIs and containers) so it can serve real-time predictions, while continuously monitoring for performance drops.
### Where Machine learning fits and why
* Machine learning typically fits in the modelling and evaluation stages.
* *why it fits here:*
* **Pattern Recognition**: Machine learning thrives on historical data. Once the preceding data engineering phases have cleaned and prepared the data, ML algorithms are the engines used to parse through massive variables and map them to desired outcomes.
* **Automation and Scale**: Rather than relying on hard-coded, rigid business rules, ML allows systems to automatically "learn" relationships, adapt to new inputs, and scale decisions in real-time.

---

## 3. Supervised Learning and Unsupervised Learning
* **Supervised learning** trains a model on labeled data to predict outcomes, making it ideal for classification and regression.
  *Example*: Email Spam Filtering.
* **Unsupervised learning** analyzes raw, unlabeled data to discover hidden patterns or groupings on its own, making it best for exploratory data analysis and anomaly detection.
  *Example*: E-commerce Customer Segmentation.

---

## 4. Overfitting 
* **Overfitting** occurs when a machine learning model learns the training data too well—memorizing its exact noise and random fluctuations rather than understanding the underlying patterns.
### How to Prevent Overfitting
* **Cross-Validation**: Divide the dataset into training, validation, and test sets. This allows you to tune the model on unseen data and get a reliable estimate of its real-world performance.
* **Regularization**: Apply mathematical penalties (such as L1 and L2 regularization) to the loss function, which discourages the model from becoming overly complex.
* **Early Stopping**: Pause the training process automatically when the model's performance on the validation set stops improving.

---

## 5. Training data and test data
  Splitting data into training and test sets is a core model validation technique used to simulate how a machine learning model will perform on new, unseen data.
### Why the process is Necessary
* **Prevents Overfitting**: Without a separate test set, a model might "memorize" the training data instead of actually learning general rules. A model that memorizes will score perfectly on its training data but fail miserably in the real world.
* **Measures Generalization**: The ultimate goal of machine learning is to build models that generalize well to new data. Testing the model on a completely held-out dataset provides an unbiased estimate of its true accuracy.
* **Avoids Overoptimistic Evaluation**: Evaluating a model on the same data used to train it creates a massive confirmation bias. It provides a false sense of security regarding how accurate the system actually is.
* 
  
---

## 6. Case Study: Starbucks — ML-Powered Customer Personalization
* **Overview**: Starbucks built an AI/ML system called Deep Brew to power hyper-personalized customer experiences through its rewards app, analyzing behavior across multiple channels.
* **Summary**: The core problem was irrelevant offers reaching the wrong customers. The solution was a machine learning recommendation engine using purchase history, location, time, and weather. The result was improved loyalty and record-breaking earnings.
* **Lifecycle stages** This case study is unique because it covers all 7 stages of the Data Science lifecycle, from defining the business goal all the way through deployment and performance evaluation — making it a complete, real-world example of the full DS process in action.

---

## Refference 

* **coursera org.**
* **IBM org.**
* **GeeksforGeeks org.**
