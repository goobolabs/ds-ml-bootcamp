### ANSWER 1
- Data Science is the process of collecting, cleaning, analyzing, and interpreting data to uncover meaningful insights and support decision-making.
- Machine Learning is a branch of AI which focuses on learning from the data that the data science come up with to create insights that improve performance, prediction and decision.
- The relationship between Data Science and Machine Learning is data.
#### Real-life example
```
A hospital collected data from 120 heart disease patients. Data Science was used to organize and analyze the data, revealing that 70% of patients had a genetic history of the condition, most patients were male, and more than half were over 60 years old. Machine Learning then used these patterns to predict the risk of heart disease in new patients based on factors such as age, gender, and family history.
```

##### Reference:
Link 1: https://seas.harvard.edu/news/what-data-science-definition-skills-applications-more <br>
Link 2: https://www.ibm.com/think/topics/data-science-vs-machine-learning

---

### ANSWER 2

**Problem definition**: Clearly identify the business or research problem, define objectives, and determine what questions need to be answered.

**Obtaining data**: you should gather data that is relevant to the problem you're trying to solve to avoid wasting time and effort with all the other steps that follow.

**Cleaning data**: After the data is collected, it requires us to format the data for analysis and deal with missing values, duplicates, and other errors.

**Exploring data**: At this stage, the data is ready, so data scientists begin the so-called exploratory data analysis (EDA) process. The aim is to understand the data's underlying structures and main characteristics and identify patterns.

**Modeling data**: Next, data scientists use machine learning algorithms or different statistical techniques in order to predict outcomes or explain relationships within the data. Depending on the problem, these models can be predictive, such as forecasting future sales, or descriptive, such as clustering customers by behavior.

**Model evaluation**: Here the model is evaluated for checking if it is geared up to be deployed. The model is examined on an unseen data, evaluated on a cautiously thought out set of assessment metrics. We additionally need to make positive that the model conforms to reality. If we do not acquire a quality end result in the evaluation, we have to re-iterate the complete modelling procedure until the preferred stage of metrics is achieved.

**Model deployment**: The model after a rigorous assessment is at the end deployed in the preferred structure and channel. This is the last step in the data science life cycle. Each step in the data science life cycle defined above must be laboured upon carefully. If any step is performed improperly, and hence, have an effect on the subsequent step and the complete effort goes to waste.

- ML fits on data modeling stage because at this stage the data scientist uses it to predict outcomes or explain relationships within the data.

##### Reference:
Link 1: https://seas.harvard.edu/news/what-data-science-definition-skills-applications-more <br>
Link 2: https://www.geeksforgeeks.org/data-science/data-science-lifecycle/

---

### ANSWER 3

- The main distinction between the two approaches is the use of labeled data sets. To put it simply, supervised learning uses labeled input and output data, while an unsupervised learning algorithm does not.


#### Example of Supervised learning
```
Imagine we have a basket full of different fruits that we want the machine to identify. The machine first looks at the image of a fruit and extracts features like its shape, color and texture. Then it compares these features to the fruits it has already learned during training. If the new fruit’s features closely match those of an apple, the machine will predict that the fruit is an apple.

For example, suppose we train the machine by showing it fruits one by one:

If the fruit is round, has a small depression at the top and is red, it is labeled as an Apple.
If the fruit is long, curved and greenish-yellow, it is labeled as a Banana.

Now after this training, if we give the machine a new fruit (say a banana) from the basket and ask it to identify it, the machine will use what it has learned during training. It will analyze the shape and color of the new fruit and classify it as a Banana placing it in the correct category. In this way, the machine learns from the training data (the basket with labeled fruits) and applies that knowledge to recognize new, unseen fruits.
```

#### Example of Unsupervised learning
```
Imagine we have a machine learning model trained on many unlabeled images of dogs and cats. The model has never seen any labeled example that says “dog” or “cat” before so it doesn’t know how these animals look like.

Now, if we give the model a new image that contains both dogs and cats it won’t be able to directly label them as “dog” or “cat.” It will group parts of the image based on similarities and differences in features like shape or texture. It might separate the image into two groups one with dog-like features and other with cat-like features.

This happens because unsupervised learning doesn’t rely on prior knowledge or training with labeled data. It finds patterns and organizes data on its own helps in discovering information that wasn’t given before.
```

##### Reference:
Link 1: https://www.geeksforgeeks.org/machine-learning/supervised-unsupervised-learning/

---

### ANSWER 4

Overfitting is caused by:
- Complexity in Models
- Insufficient or Noisy Training Data
- Overtraining on the Same Dataset

To prevent overfitting, the main objective is to make the model generalize well to new data instead of memorizing the training set. This can be achieved by controlling model complexity and improving data usage.

##### Reference: 
Link 1: https://www.udacity.com/blog/what-is-overfitting-in-machine-learning-causes-and-how-to-avoid-it/ <br>
Link 2: https://www.geeksforgeeks.org/machine-learning/how-to-avoid-overfitting-in-machine-learning/

---

### ANSWER 5
- We use 80% of the data for training to teach the model patterns and 20% for testing to check how well the model performs on new, unseen information.
- Because this ensures our AI is genuinely learning, not just memorizing.

##### Reference: 
Link 1: https://medium.com/@ishikacasley764/train-test-split-explained-simply-for-ml-beginners-7d4d9ebb7659

---

### ANSWER 6

## Case Study: Machine Learning for Railway Predictive Maintenance in Transportation

**Paper Title:** *"An Explainable Machine Learning Framework for Railway Predictive Maintenance using Data Streams from the Metro Operator of Portugal"*  
**Authors:** Silvia García-Méndez, Francisco de Arriba-Pérez, et al.  
**Published:** Scientific Reports (Nature), July 27, 2025 [arxiv](https://arxiv.org/abs/2508.05388)

***

### Key Findings

| Metric | Result |
|--------|--------|
| **Best Model** | Adaptive Random Forest Classifier (ARFC)  [arxiv](https://arxiv.org/abs/2508.05388) |
| **Accuracy** | **99.62%** (Scenario 2)  [arxiv](https://arxiv.org/abs/2508.05388) |
| **F-measure (Macro)** | **98.90%**  [arxiv](https://arxiv.org/abs/2508.05388) |
| **F-measure (Micro)** | **98.90%**  |
| **Dataset** | MetroPT: 606,424 samples from Porto Metro (Jan–Jun 2022)  [arxiv](https://arxiv.org/abs/2508.05388) |
| **Failure Types Detected** | Oil leak (compressor), Air leak (dryer/client)  |

**Key Innovations:**
1. **First online fault prediction** with both natural language AND visual explainability [arxiv](https://arxiv.org/abs/2508.05388)
2. **Real-time processing pipeline** with 3 modules: pre-processing → classification → explainability 
3. **Dynamic feature engineering** using FIR filters + FFT to detect anomalous frequencies 
4. Maintains high performance despite **class imbalance** (oil leak: 202,684 vs. air leak client: 9,001) 

**Practical Impact:**
- Enables **proactive maintenance decisions** by identifying early failure signs 2 hours before breakdown 
- Reduces **train downtime, operating costs, and improves safety** [arxiv](https://arxiv.org/abs/2508.05388)
- Natural language explanations help maintenance teams understand **which sensors exhibit abnormal behavior** 

***

### Data Science Lifecycle Stage Covered

This research comprehensively covers **multiple stages** of the Data Science lifecycle:

| Lifecycle Stage | Coverage in This Study |
|----------------|------------------------|
| **Problem Definition** | ✓ Predict railway failures in real-time for predictive maintenance  |
| **Data Collection** | ✓ 16 sensor features (pressure, temperature, current, GPS) from MetroPT dataset  |
| **Data Preprocessing** | ✓ FIR filtering, sliding windows, variance thresholding (0.5) for feature selection  |
| **Feature Engineering** | ✓ 384 engineered features (avg, std, Q1–Q3, FFT) from 4 FIR filters  |
| **Model Building** | ✓ 4 stream-based classifiers: GNB, HTC, HATC, ARFC  |
| **Hyperparameter Tuning** | ✓ Adaptive Grid Search with prequential evaluation  |
| **Model Evaluation** | ✓ Accuracy, F-measure (macro/micro), runtime using prequential protocol  |
| **Model Interpretation** | ✓ SHAP-like explainability: natural language + visual dashboards  [arxiv](https://arxiv.org/abs/2508.05388) |
| **Deployment** | ✓ Real-time streaming system for Metro do Porto operations  |

**Primary Stage:** **Model Building and Evaluation** (with strong coverage of **Online Data Preprocessing** and **Model Interpretation/Explainability**)

The study is unique because it addresses the **explainability gap** in predictive maintenance—most ML models are "black boxes," but this framework provides transparent, intelligible explanations for each failure prediction, making it practical for maintenance technicians. [arxiv](https://arxiv.org/abs/2508.05388)